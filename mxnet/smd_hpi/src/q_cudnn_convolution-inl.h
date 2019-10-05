/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

/*!
 * Copyright (c) 2017 by Contributors
 * \file cudnn_convolution-inl.h
 * \brief
 * \author HPI-DeepLearning, Bing Xu
*/
#ifndef MXNET_OPERATOR_Q_CUDNN_CONVOLUTION_INL_H_
#define MXNET_OPERATOR_Q_CUDNN_CONVOLUTION_INL_H_

#include <algorithm>
#include <vector>
#include <mutex>
#include <string>
#include "./q_convolution-inl.h"
#include "../../src/operator/cudnn_algoreg-inl.h"
#include "../../src/common/cuda_utils.h"

namespace mxnet {
namespace op {
#if MXNET_USE_CUDNN == 1

/*!
 * \brief The Operator used to perform convolution using cuDNN kernels.
 */
template<typename DType>
class QCuDNNConvolutionOp : public Operator {
 public:
  explicit QCuDNNConvolutionOp(const QConvolutionParam& param,
                              int forward_compute_type,
                              int backward_compute_type,
                              const std::vector<TShape>& in_shape,
                              const std::vector<TShape>& out_shape,
                              const Context& ctx) {
    using namespace mshadow;
    this->param_ = param;
    InitBufferForParam();
    auto cudnn_forward_compute_type = convertToCuDNNDataType(forward_compute_type);
    auto cudnn_backward_compute_type = convertToCuDNNDataType(backward_compute_type);
    // convert MB to words
    param_.workspace = (param_.workspace << 20) / sizeof(DType);
    init_cudnn_ = false;
    init_temp_size_ = false;
    dtype_ = DataType<DType>::kCudnnFlag;
    // TensorCore algos only allowed on fp16-I/O convolutions if permitted by the global policy.
    cudnn_tensor_core_ = DataType<DType>::kFlag == kFloat16 && GetEnvAllowTensorCore();

    //============================================//
    //            limits of q_cudnn               //
    CHECK_EQ(param_.kernel.ndim(), 2) << "ndim != 2 not supported for q_cudnn calculation";
    //We remove this constraint firstly to enable our experiments		
    //CHECK_EQ(param_.num_group, 1) << "q_cudnn does not (yet) support groups";
    //============================================//

#if CUDNN_MAJOR >= 5
    MSHADOW_LAYOUT_SWITCH(param_.layout.value(), Layout, {
      format_ = LayoutType<Layout>::kCudnnFlag;
    });
#else
    CHECK(param_.layout.value() == kNCHW || param_.layout.value() == kNCDHW)
      << "Need CuDNN > 5.0 for layout support";
#endif
    // Double check to make sure this class supports the operation
    if (!Supports(param, forward_compute_type, backward_compute_type, ctx))
      LOG(FATAL) << "Need CuDNN >= 6.0 for dilated convolution.";

    InitDescriptors(ctx, in_shape, out_shape,
                    cudnn_forward_compute_type, cudnn_backward_compute_type);

    if (!param_.cudnn_tune) {
      param_.cudnn_tune = dmlc::GetEnv("MXNET_CUDNN_AUTOTUNE_DEFAULT", 1);
    }
    // In cuDNN_v6, dilated convolution descriptors are compatible with only a
    // single convolution algorithm.  Despite this, we go through the algorithm
    // selection process, which will return the only algorithm supported.  This
    // approach keeps the treatment of convolution cases uniform and will
    // naturally respond to more algorithms supporting dilated convolutions in
    // future cuDNN releases.
    SelectAlgo(ctx, in_shape, out_shape,
               cudnn_forward_compute_type, cudnn_backward_compute_type);
  }

  ~QCuDNNConvolutionOp() {
    if (init_cudnn_) {
      CUDNN_CALL(cudnnDestroyTensorDescriptor(in_desc_));
      CUDNN_CALL(cudnnDestroyTensorDescriptor(in_desc_padded_));
      CUDNN_CALL(cudnnDestroyTensorDescriptor(out_desc_));
      CUDNN_CALL(cudnnDestroyTensorDescriptor(bias_desc_));
      CUDNN_CALL(cudnnDestroyFilterDescriptor(filter_desc_));
      CUDNN_CALL(cudnnDestroyConvolutionDescriptor(forward_conv_desc_));
      CUDNN_CALL(cudnnDestroyConvolutionDescriptor(back_conv_desc_));
      CUDNN_CALL(cudnnDestroyConvolutionDescriptor(back_conv_desc_w_));
    }
  }

  virtual void Forward(const OpContext &ctx,
                       const std::vector<TBlob> &in_data,
                       const std::vector<OpReqType> &req,
                       const std::vector<TBlob> &out_data,
                       const std::vector<TBlob> &aux_args) {
    using namespace mshadow;
    size_t expected = param_.no_bias ? 2 : 3;
    DType *data_ptr = NULL;
    DType *wmat_ptr = NULL;
    DType *out_ptr = NULL;
    CHECK_EQ(in_data.size(), expected);
    CHECK_EQ(out_data.size(), 1U);
    Stream<gpu> *s = ctx.get_stream<gpu>();
    GetTempSize(ctx);
    Tensor<gpu, 1, DType> workspace = AllocateTempWorkspace(ctx, forward_workspace_byte_);
    size_t workspace_size = TensorSizeBytes(workspace);

    Tensor<gpu, 4, DType> data = in_data[qconv::kData].get<gpu, 4, DType>(s);
    Tensor<gpu, 4, DType> wmat = in_data[qconv::kWeight].get<gpu, 4, DType>(s);
    Tensor<gpu, 4, DType> out = out_data[qconv::kOut].get<gpu, 4, DType>(s);
    CHECK_EQ(data.CheckContiguous(), true);
    CHECK_EQ(wmat.CheckContiguous(), true);
    CHECK_EQ(out.CheckContiguous(), true);
    data_ptr = data.dptr_;
    wmat_ptr = wmat.dptr_;
    out_ptr = out.dptr_;


    //============================================//
    //calc the scaling scalar for 1-bit mode.
    //Note that should on original weights and activations              
    DType scaling_scalar_w;
    //DType scaling_scalar_i;
    if(this->param_.act_bit == 1 && this->param_.weight_bit == 1 
       && param_.scaling_mode.value() == qconv::scaling_forward){
      //calc scaling scalar of original weights
      scaling_scalar_w = q_helper::get_scaling_scalar(wmat);

      //Note: the current experiment results show that with input scaling, we 
      //cannot even get acceptable result on MNIST dataset!
      //scaling_scalar_i = q_helper::get_scaling_scalar(data);        
      //debug information
      //std::cout << "scaling mode:" << param_.scaling_mode.value() << std::endl;
      //printf("scl w : %f, scal in: %f\n", scaling_scalar_w, scaling_scalar_i);       
    }

    //============================================//  

    //============================================//
    //            WEIGHTS quantization            //
    // for training mode,                         //
    // we apply quantization function on weights. //
    //                                            //
    // mf quantize weights                        //
    Tensor<gpu, 1, DType> w1d = in_data[qconv::kWeight].FlatTo1D<gpu, DType>(s);
    Tensor<gpu, 1, DType> w1d_copy;
    if (this->param_.gradient_update_mode.value() != qconv::bb){
      w1d_copy = mshadow::NewTensor<gpu>(w1d.shape_, DType(1.0), true, w1d.stream_);
      mshadow::Copy(w1d_copy, w1d, w1d.stream_);
    }
    q_helper::quantize_weights(w1d, this->param_.weight_bit);
    // /mf quantize weights                       //
    //============================================//

    //============================================//
    //             INPUT quantization + padding   //
    // for training or prediction in gpu mode,    //
    // we apply quantization function on input    //
    // This process should be after padding elemt //
    // since the padding elements are all "0"     //
    //                                            //
    mshadow::Tensor<gpu, 4, DType> padded_data = data;

    bool padded = (param_.pad[0] != 0) || (param_.pad[1] != 0);
    if (padded) {
      Shape<4> padded_shape = Shape4(data.shape_[0],
                                     data.shape_[1],
                                     data.shape_[2] + 2 * param_.pad[0],
                                     data.shape_[3] + 2 * param_.pad[1]);
      padded_data = mshadow::NewTensor<gpu>(padded_shape, static_cast<DType>(0), true,
                                                                           data.stream_);
      if (this->param_.act_bit == 1) {            //
        padded_data = mshadow::expr::F<mshadow_op::det_sign>(pad(data, param_.pad[0], param_.pad[1]));
      } else {                                    //
        padded_data = mshadow::expr::F<mshadow_op::quantize>(mshadow::expr::F<mshadow_op::maximum>(
                                                         mshadow::expr::F<mshadow_op::minimum>(pad(data, param_.pad[0], param_.pad[1]), mshadow::expr::scalar(DType(1))),
                                                         mshadow::expr::scalar(DType(0))), //clip to [0, 1]
                                                      mshadow::expr::scalar(DType(this->param_.act_bit)));
      }
      data_ptr = padded_data.dptr_;
    } else { // no padding    
      q_helper::quantize_activations(data, this->param_.act_bit);
    }                                             
    //============================================//

    for (uint32_t g = 0; g < param_.num_group; ++g) { // for our tests: num_group == 1, so not-a-loop
      typename DataType<DType>::ScaleType alpha = 1.0f;
      typename DataType<DType>::ScaleType beta = 0.0f;
      typename DataType<DType>::ScaleType beta_add = 1.0f;
      CUDNN_CALL(cudnnConvolutionForward(s->dnn_handle_,
                                       &alpha,
                                       in_desc_padded_,
                                       data_ptr + data_offset_padded_ * g,
                                       filter_desc_,
                                       wmat_ptr + weight_offset_ * g,
                                       forward_conv_desc_,
                                       forward_algo_.AlgoNumber(),
                                       workspace.dptr_,
                                       workspace_size,
                                       req[qconv::kOut] == kAddTo? &beta_add : &beta,
                                       out_desc_,
                                       out_ptr + out_offset_ * g));
      if (!param_.no_bias) {
        Tensor<gpu, 1, DType> bias = in_data[qconv::kBias].get<gpu, 1, DType>(s);
        #if CUDNN_MAJOR >= 4
        CUDNN_CALL(cudnnAddTensor(s->dnn_handle_,
                                &alpha,
                                bias_desc_,
                                bias.dptr_ + bias_offset_ * g,
                                &beta_add,
                                out_desc_,
                                out_ptr + out_offset_ * g));
        #endif
        #if CUDNN_MAJOR == 3
        CUDNN_CALL(cudnnAddTensor(s->dnn_handle_,
                                CUDNN_ADD_SAME_C,
                                &alpha,
                                bias_desc_,
                                bias.dptr_ + bias_offset_ * g,
                                &beta_add,
                                out_desc_,
                                out_ptr + out_offset_ * g));
        #endif
      }
    }
    //============================================//
    //             OUT SCALING                    //
    // this converting is just for mimicing       //
    // 1-bit xnor-popc operations                 //
    if (this->param_.act_bit == 1 && this->param_.weight_bit == 1) {              //
      int k = in_data[qconv::kWeight].shape_[1] / param_.num_group * in_data[qconv::kWeight].shape_[2] * in_data[qconv::kWeight].shape_[3];

      //LOG(INFO) << "in_data[qconv::kData].shape_ = " << in_data[qconv::kWeight].shape_(1) *;
      out = (mshadow::expr::ScalarExp<DType>(k) + out) / mshadow::expr::scalar(DType(2.0));
    }                                             //
    //============================================//
    if (padded) {
      mshadow::FreeSpace(&padded_data);
    }

    //============================================//
    //calc the scaling scalar
    if(this->param_.act_bit == 1 && this->param_.weight_bit == 1 
       && param_.scaling_mode.value() == qconv::scaling_forward){
      //q_helper::tensor_mul_scalar(out, scaling_scalar_i);
      q_helper::tensor_mul_scalar(out, scaling_scalar_w);
      //store the binary weights*scaling_scalar_w
      //q_helper::tensor_mul_scalar(binary_weights, scaling_scalar_w);      
    }
    //============================================//    
    //============================================//
    //copy back the weights
    if (this->param_.gradient_update_mode.value() != qconv::bb){
    	mshadow::Copy(w1d, w1d_copy, w1d_copy.stream_);
    	mshadow::FreeSpace(&w1d_copy);
    }
  	//============================================//
  }

  virtual void Backward(const OpContext &ctx,
                        const std::vector<TBlob> &out_grad,
                        const std::vector<TBlob> &in_data,
                        const std::vector<TBlob> &out_data,
                        const std::vector<OpReqType> &req,
                        const std::vector<TBlob> &in_grad,
                        const std::vector<TBlob> &aux_args) {
    using namespace mshadow;
    using namespace mshadow::expr;
    size_t expected = param_.no_bias == 0 ? 3 : 2;
    DType *grad_ptr = NULL;
    DType *wmat_ptr = NULL;
    DType *gwmat_ptr = NULL;
    DType *data_ptr = NULL;
    DType *gdata_ptr = NULL;
    CHECK_EQ(out_grad.size(), 1U);
    CHECK(in_data.size() == expected && in_grad.size() == expected);
    Stream<gpu> *s = ctx.get_stream<gpu>();
    if (param_.kernel.ndim() == 2) {
      Tensor<gpu, 4, DType> grad = out_grad[qconv::kOut].get<gpu, 4, DType>(s);
      Tensor<gpu, 4, DType> wmat = in_data[qconv::kWeight].get<gpu, 4, DType>(s);
      Tensor<gpu, 4, DType> gwmat = in_grad[qconv::kWeight].get<gpu, 4, DType>(s);
      Tensor<gpu, 4, DType> data = in_data[qconv::kData].get<gpu, 4, DType>(s);
      Tensor<gpu, 4, DType> gdata = in_grad[qconv::kData].get<gpu, 4, DType>(s);
      grad_ptr = grad.dptr_;
      wmat_ptr = wmat.dptr_;
      gwmat_ptr = gwmat.dptr_;
      data_ptr = data.dptr_;
      gdata_ptr = gdata.dptr_;
    } else {
      Tensor<gpu, 5, DType> grad = out_grad[qconv::kOut].get<gpu, 5, DType>(s);
      Tensor<gpu, 5, DType> wmat = in_data[qconv::kWeight].get<gpu, 5, DType>(s);
      Tensor<gpu, 5, DType> gwmat = in_grad[qconv::kWeight].get<gpu, 5, DType>(s);
      Tensor<gpu, 5, DType> data = in_data[qconv::kData].get<gpu, 5, DType>(s);
      Tensor<gpu, 5, DType> gdata = in_grad[qconv::kData].get<gpu, 5, DType>(s);
      grad_ptr = grad.dptr_;
      wmat_ptr = wmat.dptr_;
      gwmat_ptr = gwmat.dptr_;
      data_ptr = data.dptr_;
      gdata_ptr = gdata.dptr_;
    }

    //============================================//
    //calc the scaling scalar for 1-bit mode.   
    //Note: gradient_update_mode "ff" don't need a scaling process, since
    //full precision weights in use.
    DType scaling_scalar_w;
    Tensor<gpu, 1, DType> w1d = in_data[qconv::kWeight].FlatTo1D<gpu, DType>(s);
    if(this->param_.act_bit == 1 
        && this->param_.weight_bit == 1
        && this->param_.scaling_mode.value() != qconv::scaling_none
        && this->param_.gradient_update_mode.value() != qconv::ff){
      scaling_scalar_w = q_helper::get_scaling_scalar(w1d);
    }
    //============================================//         

    //========================================//
    // calculate gradients for binarized      //
    // or quantized weights, then later apply //
    // to original weights                    //
    // save here once, copy back later        //
    Tensor<gpu, 1, DType> w1d_copy;
    //use binary/quantized weights for gradient calc,
    if (this->param_.gradient_update_mode.value() == qconv::bf){  
      w1d_copy = mshadow::NewTensor<gpu>(w1d.shape_, DType(1.0), true, w1d.stream_);
      mshadow::Copy(w1d_copy, w1d, w1d.stream_);
      q_helper::quantize_weights(w1d, this->param_.weight_bit);
    }
    //                                        //
    //========================================//

    //============================================//
    //calc the scaling scalar for 1-bit mode.    
    if(this->param_.act_bit == 1 
      && this->param_.weight_bit == 1
      && this->param_.scaling_mode.value() != qconv::scaling_none
      && this->param_.gradient_update_mode.value() != qconv::ff)
    {    
        q_helper::tensor_mul_scalar(w1d, scaling_scalar_w);              
    }
    //============================================//         

    Tensor<gpu, 1, DType> workspace = AllocateTempWorkspace(ctx, backward_workspace_byte_);
    size_t workspace_size = TensorSizeBytes(workspace);
    for (uint32_t g = 0; g < param_.num_group; ++g) {
      typename DataType<DType>::ScaleType alpha = 1.0f;
      typename DataType<DType>::ScaleType beta = 0.0f;
      typename DataType<DType>::ScaleType beta_add = 1.0f;
      if (!param_.no_bias && (req[qconv::kBias] != kNullOp)) {
        Tensor<gpu, 1, DType> gbias = in_grad[qconv::kBias].get<gpu, 1, DType>(s);
        CUDNN_CALL(cudnnConvolutionBackwardBias(s->dnn_handle_,
                                              &alpha,
                                              out_desc_,
                                              grad_ptr + out_offset_ * g,
                                              req[qconv::kBias] == kAddTo ? &beta_add : &beta,
                                              bias_desc_,
                                              gbias.dptr_ + bias_offset_ * g));
      }
      if (req[qconv::kWeight] != kNullOp) {
        #if CUDNN_MAJOR <= 4
          CUDNN_CALL(cudnnConvolutionBackwardFilter_v3(s->dnn_handle_,
               &alpha,
               in_desc_,
               data_ptr + data_offset_ * g,
               out_desc_,
               grad_ptr + out_offset_ * g,
               back_conv_desc_w_,
               back_algo_w_.AlgoNumber(),
               workspace.dptr_,
               workspace_size,
               req[qconv::kWeight] == kAddTo? &beta_add : &beta,
               filter_desc_,
               gwmat_ptr + weight_offset_ * g));
        #elif CUDNN_MAJOR >= 5
          CUDNN_CALL(cudnnConvolutionBackwardFilter(s->dnn_handle_,
               &alpha,
               in_desc_,
               data_ptr + data_offset_ * g,
               out_desc_,
               grad_ptr + out_offset_ * g,
               back_conv_desc_w_,
               back_algo_w_.AlgoNumber(),
               workspace.dptr_,
               workspace_size,
               req[qconv::kWeight] == kAddTo? &beta_add : &beta,
               filter_desc_,
               gwmat_ptr + weight_offset_ * g));
        #endif
      }
      if (req[qconv::kData] != kNullOp) {
        #if CUDNN_MAJOR <= 4
          CUDNN_CALL(cudnnConvolutionBackwardData_v3(s->dnn_handle_,
               &alpha,
               filter_desc_,
               wmat_ptr + weight_offset_ * g,
               out_desc_,
               grad_ptr + out_offset_ * g,
               back_conv_desc_,
               back_algo_.AlgoNumber(),
               workspace.dptr_,
               workspace_size,
               req[qconv::kData] == kAddTo? &beta_add : &beta,
               in_desc_,
               gdata_ptr + data_offset_ * g));
        #elif CUDNN_MAJOR >= 5
          CUDNN_CALL(cudnnConvolutionBackwardData(s->dnn_handle_,
               &alpha,
               filter_desc_,
               wmat_ptr + weight_offset_ * g,
               out_desc_,
               grad_ptr + out_offset_ * g,
               back_conv_desc_,
               back_algo_.AlgoNumber(),
               workspace.dptr_,
               workspace_size,
               req[qconv::kData] == kAddTo? &beta_add : &beta,
               in_desc_,
               gdata_ptr + data_offset_ * g));
        #endif
      }
    }
    //========================================//
    // gradient calculation done, swap back   //
    // weights and also free space            //
    if (param_.gradient_update_mode.value() == qconv::bf){      
      mshadow::Copy(w1d, w1d_copy, w1d_copy.stream_);
      mshadow::FreeSpace(&w1d_copy);
    }
    //                                        //
    //========================================//
  }

/*!
 * \brief Returns whether the cuDNN library version supports the convolution
 * operation described by `param`: cuDNN v5 and earlier does not support
 * dilated convolutions.  Dilation only enabled after v6.0.20.
 */
  static bool Supports(QConvolutionParam param,
                       int forward_compute_type,
                       int backward_compute_type,
                       const Context &ctx) {
    using namespace mshadow;

    // NDHWC not supported, NHWC not supported in true fp16
    auto layout_val = param.layout.value();
    auto true_fp16 = DataType<DType>::kFlag == kFloat16 &&
      (forward_compute_type == kFloat16 || backward_compute_type == kFloat16);
    if (layout_val == kNDHWC || layout_val == kNHWC && true_fp16)
      return false;

    // Permits graceful fallback to pseudo-fp16 on heterogenous systems
    if (!SupportsFloat16Compute(ctx.dev_id) &&
        (forward_compute_type == kFloat16 || backward_compute_type == kFloat16)) {
      return false;
    }

    // The factor by which the effective filter size grows based on dilation.
    auto filterDilationFactor = param.dilate.Size();

    // The v6 kernels that backprop a dilated convolution don't handle fp16.
    // Dilation support across all architectures only available after v6.0.20.
    return filterDilationFactor == 1 ||
           filterDilationFactor > 1 && (CUDNN_VERSION > 6020) &&
           (backward_compute_type != kFloat16);
  }

 private:
/*!
 * \brief Translate an mxnet datatype to the corresponding cudnnDataType_t.
 */
  cudnnDataType_t convertToCuDNNDataType(int dtype) {
    cudnnDataType_t converted = CUDNN_DATA_FLOAT;
    // The following will always assign to `converted` or throw an exception.
    MSHADOW_REAL_TYPE_SWITCH(dtype, mxDType, {
      converted = mshadow::DataType<mxDType>::kCudnnFlag;
    })
    return converted;
  }

  void InitDescriptors(const Context& ctx,
                       const std::vector<TShape>& in_shape,
                       const std::vector<TShape>& out_shape,
                       cudnnDataType_t cudnn_forward_compute_type,
                       cudnnDataType_t cudnn_backward_compute_type) {
    using namespace mshadow;
    size_t expected = param_.no_bias ? 2 : 3;
    CHECK_EQ(in_shape.size(), expected);
    CHECK_EQ(out_shape.size(), 1U);
    CUDNN_CALL(cudnnCreateTensorDescriptor(&in_desc_));
    CUDNN_CALL(cudnnCreateTensorDescriptor(&in_desc_padded_));
    CUDNN_CALL(cudnnCreateTensorDescriptor(&out_desc_));
    CUDNN_CALL(cudnnCreateTensorDescriptor(&bias_desc_));
    CUDNN_CALL(cudnnCreateFilterDescriptor(&filter_desc_));
    CUDNN_CALL(cudnnCreateConvolutionDescriptor(&forward_conv_desc_));
    CUDNN_CALL(cudnnCreateConvolutionDescriptor(&back_conv_desc_));
    CUDNN_CALL(cudnnCreateConvolutionDescriptor(&back_conv_desc_w_));

    TShape dshape = in_shape[qconv::kData];
    //============================================//
    //  adjust input size to be already padded    //
    //  keep original shape for seperate desc     //
    TShape dshape_padded = dshape;                //
    dshape_padded[2] += 2 * param_.pad[0];        //
    dshape_padded[3] += 2 * param_.pad[1];        //
    //============================================//
    TShape wshape = in_shape[qconv::kWeight];
    TShape oshape = out_shape[qconv::kOut];
    TShape dstride, dstride_padded, ostride;
    wshape[0] /= param_.num_group;
    if (param_.kernel.ndim() == 2) {
      // 2d conv

      // As of cuDNN_v6, the unsuffixed version of cudnnSetConvolution2dDescriptor()
      // requires an additional 'computeType' parameter to set the precision of the
      // convolution calculation.  This facility was available as of v5 in
      // cudnnSetConvolution2dDescriptor_v5(), but was never accessed.
      #if CUDNN_MAJOR >= 6
      CUDNN_CALL(cudnnSetConvolution2dDescriptor(forward_conv_desc_,
                                               0, //param_.pad[0],
                                               0, //param_.pad[1],
                                               param_.stride[0],
                                               param_.stride[1],
                                               param_.dilate[0],
                                               param_.dilate[1],
                                               CUDNN_CROSS_CORRELATION,
                                               cudnn_forward_compute_type));
      CUDNN_CALL(cudnnSetConvolution2dDescriptor(back_conv_desc_,
                                               param_.pad[0],
                                               param_.pad[1],
                                               param_.stride[0],
                                               param_.stride[1],
                                               param_.dilate[0],
                                               param_.dilate[1],
                                               CUDNN_CROSS_CORRELATION,
                                               cudnn_backward_compute_type));
      CUDNN_CALL(cudnnSetConvolution2dDescriptor(back_conv_desc_w_,
                                               param_.pad[0],
                                               param_.pad[1],
                                               param_.stride[0],
                                               param_.stride[1],
                                               param_.dilate[0],
                                               param_.dilate[1],
                                               CUDNN_CROSS_CORRELATION,
                                               cudnn_backward_compute_type));
      #else
      CUDNN_CALL(cudnnSetConvolution2dDescriptor(forward_conv_desc_,
                                                 0, //param_.pad[0],
                                                 0, //param_.pad[1],
                                                 param_.stride[0],
                                                 param_.stride[1],
                                                 param_.dilate[0],
                                                 param_.dilate[1],
                                                 CUDNN_CROSS_CORRELATION));
      CUDNN_CALL(cudnnSetConvolution2dDescriptor(back_conv_desc_,
                                                 param_.pad[0],
                                                 param_.pad[1],
                                                 param_.stride[0],
                                                 param_.stride[1],
                                                 param_.dilate[0],
                                                 param_.dilate[1],
                                                 CUDNN_CROSS_CORRELATION));
      CUDNN_CALL(cudnnSetConvolution2dDescriptor(back_conv_desc_w_,
                                                 param_.pad[0],
                                                 param_.pad[1],
                                                 param_.stride[0],
                                                 param_.stride[1],
                                                 param_.dilate[0],
                                                 param_.dilate[1],
                                                 CUDNN_CROSS_CORRELATION));
      #endif

      #if CUDNN_MAJOR >= 5
      wshape = ConvertLayout(wshape.get<4>(), param_.layout.value(), kNCHW);
      CUDNN_CALL(cudnnSetFilter4dDescriptor(filter_desc_,
                                          dtype_,
                                          format_,
                                          wshape[0],
                                          wshape[1],
                                          wshape[2],
                                          wshape[3]));
      #else
      CHECK_EQ(param_.layout.value(), kNCHW) << "CuDNN V4 only support NCHW layout";
      CUDNN_CALL(cudnnSetFilter4dDescriptor(filter_desc_,
                                          dtype_,
                                          wshape[0],
                                          wshape[1],
                                          wshape[2],
                                          wshape[3]));
      #endif

      dstride = ConvertLayout(Shape4(dshape[1] * dshape[2] * dshape[3],
                                     dshape[2] * dshape[3],
                                     dshape[3],
                                     1),
                              param_.layout.value(), kNCHW);
      dshape = ConvertLayout(dshape.get<4>(), param_.layout.value(), kNCHW);
      dstride_padded = ConvertLayout(Shape4(dshape_padded[1] * dshape_padded[2] * dshape_padded[3],
                                            dshape_padded[2] * dshape_padded[3],
                                            dshape_padded[3],
                                            1),
                              param_.layout.value(), kNCHW);
      dshape_padded = ConvertLayout(dshape_padded.get<4>(), param_.layout.value(), kNCHW);

      ostride = ConvertLayout(Shape4(oshape[1] * oshape[2] * oshape[3],
                                     oshape[2] * oshape[3],
                                     oshape[3],
                                     1),
                              param_.layout.value(), kNCHW);
      oshape = ConvertLayout(oshape.get<4>(), param_.layout.value(), kNCHW);
    } else if (param_.kernel.ndim() == 3) {
      LOG(WARNING) << "ndim != 2 completely untested for q_cudnn calculation - might have to set cudnn_off=True";
      // 3d conv
      #if CUDNN_MAJOR >= 5
      CHECK_EQ(param_.layout.value(), kNCDHW) << "CuDNN only support 3D conv with NCDHW layout";
      std::vector<int> wshape_buffer(wshape.ndim());
      CUDNN_CALL(cudnnSetFilterNdDescriptor(filter_desc_,
                                          dtype_,
                                          CUDNN_TENSOR_NCHW,
                                          static_cast<int>(wshape.ndim()),
                                          CastTShapeToIntPtr(wshape, &wshape_buffer)));
      #else
      LOG(FATAL) << "Only support CUDNN V5 for 3D convolution";
      #endif
      CUDNN_CALL(cudnnSetConvolutionNdDescriptor(forward_conv_desc_,
                                               3,
                                               param_pad_.data(),
                                               param_stride_.data(),
                                               param_dilate_.data(),
                                               CUDNN_CROSS_CORRELATION,
                                               cudnn_forward_compute_type));

      CUDNN_CALL(cudnnSetConvolutionNdDescriptor(back_conv_desc_,
                                               3,
                                               param_pad_.data(),
                                               param_stride_.data(),
                                               param_dilate_.data(),
                                               CUDNN_CROSS_CORRELATION,
                                               cudnn_backward_compute_type));

      CUDNN_CALL(cudnnSetConvolutionNdDescriptor(back_conv_desc_w_,
                                                 3,
                                                 param_pad_.data(),
                                                 param_stride_.data(),
                                                 param_dilate_.data(),
                                                 CUDNN_CROSS_CORRELATION,
                                                 cudnn_backward_compute_type));

      dstride = ConvertLayout(Shape5(dshape[1] * dshape[2] * dshape[3] * dshape[4],
                                     dshape[2] * dshape[3] * dshape[4],
                                     dshape[3] * dshape[4],
                                     dshape[4],
                                     1),
                              param_.layout.value(), kNCDHW);
      dshape = ConvertLayout(dshape.get<5>(), param_.layout.value(), kNCDHW);

      ostride = ConvertLayout(Shape5(oshape[1] * oshape[2] * oshape[3] * oshape[4],
                                     oshape[2] * oshape[3] * oshape[4],
                                     oshape[3] * oshape[4],
                                     oshape[4],
                                     1),
                              param_.layout.value(), kNCDHW);
      oshape = ConvertLayout(oshape.get<5>(), param_.layout.value(), kNCDHW);
    }
    // Set "allow tensor core" flag in convolution descriptors, if available.
    #if CUDNN_MAJOR >= 7
      cudnnMathType_t math_type = cudnn_tensor_core_ ? CUDNN_TENSOR_OP_MATH
                                                      : CUDNN_DEFAULT_MATH;
      CUDNN_CALL(cudnnSetConvolutionMathType(forward_conv_desc_, math_type));
      CUDNN_CALL(cudnnSetConvolutionMathType(back_conv_desc_, math_type));
      CUDNN_CALL(cudnnSetConvolutionMathType(back_conv_desc_w_, math_type));
    #endif
    dshape[1] /= param_.num_group;
    dshape_padded[1] /= param_.num_group;
    oshape[1] /= param_.num_group;
    weight_offset_ = wshape.Size();
    data_offset_ = dstride[1] * dshape[1];
    data_offset_padded_ = dstride_padded[1] * dshape_padded[1];
    out_offset_ = ostride[1] * oshape[1];

    std::vector<int> dshape_buffer(dshape.ndim());
    nnvm::ShapeTypeCast(dshape.begin(), dshape.end(), dshape_buffer.data());
    std::vector<int> dshape_buffer_padded(dshape_padded.ndim());
    nnvm::ShapeTypeCast(dshape_padded.begin(), dshape_padded.end(), dshape_buffer_padded.data());

    std::vector<int> dstride_buffer(dstride.ndim());
    nnvm::ShapeTypeCast(dstride.begin(), dstride.end(), dstride_buffer.data());
    std::vector<int> dstride_buffer_padded(dstride_padded.ndim());
    nnvm::ShapeTypeCast(dstride_padded.begin(), dstride_padded.end(), dstride_buffer_padded.data());

    CUDNN_CALL(cudnnSetTensorNdDescriptor(in_desc_,
                                          dtype_,
                                          static_cast<int>(dshape.ndim()),
                                          dshape_buffer.data(),
                                          dstride_buffer.data()));

    CUDNN_CALL(cudnnSetTensorNdDescriptor(in_desc_padded_,
                                          dtype_,
                                          static_cast<int>(dshape_padded.ndim()),
                                          dshape_buffer_padded.data(),
                                          dstride_buffer_padded.data()));

    std::vector<int> oshape_buffer(oshape.ndim());
    nnvm::ShapeTypeCast(oshape.begin(), oshape.end(), oshape_buffer.data());
    std::vector<int> ostride_buffer(ostride.ndim());
    nnvm::ShapeTypeCast(ostride.begin(), ostride.end(), ostride_buffer.data());
    CUDNN_CALL(cudnnSetTensorNdDescriptor(out_desc_,
                                          dtype_,
                                          static_cast<int>(oshape.ndim()),
                                          oshape_buffer.data(),
                                          ostride_buffer.data()));

    if (!param_.no_bias) {
      TShape bias = in_shape[qconv::kBias];
      bias_offset_ = bias[0] / param_.num_group;
      std::vector<int> bias_shape = {1,
                                     static_cast<int>(bias[0] / param_.num_group),
                                     1, 1};
      std::vector<int> bias_stride = {static_cast<int>(bias_offset_), 1, 1, 1};
      if (param_.kernel.ndim() == 3) {
        bias_shape.push_back(1);
        bias_stride.push_back(1);
      }
      CUDNN_CALL(cudnnSetTensorNdDescriptor(bias_desc_,
                                          dtype_,
                                          static_cast<int>(bias_shape.size()),
                                          &bias_shape[0],
                                          &bias_stride[0]));
    }
    init_cudnn_ = true;
  }

    void SelectAlgo(const Context& ctx,
                    const std::vector<TShape>& in_shape,
                    const std::vector<TShape>& out_shape,
                    cudnnDataType_t cudnn_forward_compute_type,
                    cudnnDataType_t cudnn_backward_compute_type) {
      ConvolutionParam conv_param = ConvolutionParam(
        param_.kernel, param_.stride, param_.dilate, param_.pad,
        param_.num_filter, param_.num_group, param_.workspace,
        param_.no_bias, param_.cudnn_tune, param_.cudnn_off, param_.layout);
      if (!CuDNNConvAlgoReg::Get()->Find(conv_param, in_shape, out_shape, dtype_,
                                         cudnn_forward_compute_type, cudnn_backward_compute_type,
                                         SMArch(ctx.dev_id), &forward_algo_, &back_algo_,
                                         &back_algo_w_)) {
        // Not in algo registry, must determine via *Get*() or *Find*()
        Engine::VarHandle var = Engine::Get()->NewVariable();
        Engine::Get()->PushAsync([=](RunContext rctx, Engine::CallbackOnComplete on_complete) {
            mshadow::Stream<gpu> *s = rctx.get_stream<gpu>();
            CHECK_EQ(s->dnn_handle_ownership_, mshadow::Stream<gpu>::OwnHandle);
            size_t workspace_byte = static_cast<size_t>(param_.workspace * sizeof(DType));
            #if CUDNN_MAJOR >= 7
              // Starting with cuDNNv7, the algo number returned by *Get*() is not the entire
              // story: the notion of whether the algo ran in Tensor Core mode is not known.
              // Since we want to report the Tensor Core mode in the verbose output, we switch
              // to using the new *Get*_v7() call.  Since the function signature of *Get*_v7() matches
              // that of *Find*(), we can unify the find-vs-get logic by using function pointers.

              // Forward Algorithm Find/Get() v7
              std::vector<cudnnConvolutionFwdAlgoPerf_t> fwd_results(MaxForwardAlgos(s->dnn_handle_));
              int actual_fwd_algos = 0;
              auto fwd_algo_discoverer =
                param_.cudnn_tune.value() == conv::kOff ? cudnnGetConvolutionForwardAlgorithm_v7
                                                        : cudnnFindConvolutionForwardAlgorithm;
              CUDNN_CALL((*fwd_algo_discoverer)(s->dnn_handle_,
                                                in_desc_padded_,
                                                filter_desc_,
                                                forward_conv_desc_,
                                                out_desc_,
                                                fwd_results.size(),
                                                &actual_fwd_algos,
                                                fwd_results.data()));
              fwd_results.resize(actual_fwd_algos);
              AlgoFinalSelect<cudnnConvolutionFwdAlgoPerf_t,
                              cudnnConvolutionFwdAlgo_t>(fwd_results, "forward",
                                                         workspace_byte, &forward_algo_);

              // Backprop-to-Filter Algorithm Find/Get() v7
              auto max_bwd_filt_algos = MaxBackwardFilterAlgos(s->dnn_handle_);
              std::vector<cudnnConvolutionBwdFilterAlgoPerf_t> bwd_filt_results(max_bwd_filt_algos);
              int actual_bwd_filter_algos = 0;
              auto bwd_filter_algo_discoverer =
                param_.cudnn_tune.value() == qconv::kOff ? cudnnGetConvolutionBackwardFilterAlgorithm_v7
                                                        : cudnnFindConvolutionBackwardFilterAlgorithm;
              CUDNN_CALL((*bwd_filter_algo_discoverer)(s->dnn_handle_,
                                                       in_desc_,
                                                       out_desc_,
                                                       back_conv_desc_w_,
                                                       filter_desc_,
                                                       bwd_filt_results.size(),
                                                       &actual_bwd_filter_algos,
                                                       bwd_filt_results.data()));
              bwd_filt_results.resize(actual_bwd_filter_algos);
              AlgoFinalSelect<cudnnConvolutionBwdFilterAlgoPerf_t,
                              cudnnConvolutionBwdFilterAlgo_t>(bwd_filt_results, "backprop-to-filter",
                                           workspace_byte, &back_algo_w_);

              // Backprop-to-Data Algorithm Find/Get() v7
              auto max_bwd_data_algos = MaxBackwardDataAlgos(s->dnn_handle_);
              std::vector<cudnnConvolutionBwdDataAlgoPerf_t> bwd_data_results(max_bwd_data_algos);
              int actual_bwd_data_algos = 0;
              auto bwd_data_algo_discoverer =
                param_.cudnn_tune.value() == qconv::kOff ? cudnnGetConvolutionBackwardDataAlgorithm_v7
                                                        : cudnnFindConvolutionBackwardDataAlgorithm;
              CUDNN_CALL((*bwd_data_algo_discoverer)(s->dnn_handle_,
                                                     filter_desc_,
                                                     out_desc_,
                                                     back_conv_desc_,
                                                     in_desc_,
                                                     bwd_data_results.size(),
                                                     &actual_bwd_data_algos,
                                                     bwd_data_results.data()));
              bwd_data_results.resize(actual_bwd_data_algos);
              AlgoFinalSelect<cudnnConvolutionBwdDataAlgoPerf_t,
                              cudnnConvolutionBwdDataAlgo_t>(bwd_data_results, "backprop-to-data",
                                            workspace_byte, &back_algo_);
            #else
              // CUDNN_MAJOR < 7
              const int kMaxAlgos = 10;
              int nalgo = kMaxAlgos;
              int i = 0;
              // Forward Algorithm Find/Get, v6 and earlier
              if (CUDNN_MAJOR == 6 && param_.layout.value() == mshadow::kNHWC) {
                // In cuDNNv6, for kNHWC, only CUDNN_CONVOLUTION_FWD_ALGO_IMPLICIT_GEMM is
                // supported.  Hard-coded this since the algo find() or get() throws an FPE.
                forward_algo_.Set(CUDNN_CONVOLUTION_FWD_ALGO_IMPLICIT_GEMM, false);
              } else if (!param_.cudnn_tune.value()) {
                cudnnConvolutionFwdAlgo_t fastest_fwd_algo;
                CUDNN_CALL(cudnnGetConvolutionForwardAlgorithm(s->dnn_handle_,
                                                               in_desc_padded_,
                                                               filter_desc_,
                                                               forward_conv_desc_,
                                                               out_desc_,
                                                               CUDNN_CONVOLUTION_FWD_SPECIFY_WORKSPACE_LIMIT,
                                                               workspace_byte,
                                                               &fastest_fwd_algo));
                forward_algo_.Set(fastest_fwd_algo, false);
              } else {
                cudnnConvolutionFwdAlgoPerf_t fwd_algo[kMaxAlgos];
                CUDNN_CALL(cudnnFindConvolutionForwardAlgorithm(s->dnn_handle_,
                                                                in_desc_padded_,
                                                                filter_desc_,
                                                                forward_conv_desc_,
                                                                out_desc_,
                                                                kMaxAlgos,
                                                                &nalgo,
                                                                fwd_algo));
                i = 0;
                while (i < nalgo
                       && (fwd_algo[i].status != CUDNN_STATUS_SUCCESS
                           || (param_.cudnn_tune.value() == qconv::kLimited
                               && fwd_algo[i].memory > workspace_byte)))
                  ++i;
                if (i == nalgo) {
                  LOG(FATAL) << "Failed to find a forward convolution algorithm.";
                } else {
                  forward_algo_.Set(fwd_algo[i].algo, false);
                }
              }
              // Backprop-to-Filter Algorithm Find/Get, v6 and earlier
              if (!param_.cudnn_tune.value()) {
                cudnnConvolutionBwdFilterAlgo_t fastest_bwd_filt_algo;
                CUDNN_CALL(cudnnGetConvolutionBackwardFilterAlgorithm(s->dnn_handle_,
                                                                      in_desc_,
                                                                      out_desc_,
                                                                      back_conv_desc_w_,
                                                                      filter_desc_,
                                                                      CUDNN_CONVOLUTION_BWD_FILTER_SPECIFY_WORKSPACE_LIMIT,
                                                                      workspace_byte,
                                                                      &fastest_bwd_filt_algo));
                back_algo_w_.Set(fastest_bwd_filt_algo, false);
              } else {
                cudnnConvolutionBwdFilterAlgoPerf_t bwd_filter_algo[kMaxAlgos];
                CUDNN_CALL(cudnnFindConvolutionBackwardFilterAlgorithm(s->dnn_handle_,
                                                                       in_desc_,
                                                                       out_desc_,
                                                                       back_conv_desc_w_,
                                                                       filter_desc_,
                                                                       kMaxAlgos,
                                                                       &nalgo,
                                                                       bwd_filter_algo));
                i = 0;
                while (i < nalgo
                       && (bwd_filter_algo[i].status != CUDNN_STATUS_SUCCESS
                           || (param_.cudnn_tune.value() == qconv::kLimited
                               && bwd_filter_algo[i].memory > workspace_byte)))
                  ++i;
                if (i == nalgo) {
                  LOG(FATAL) << "Failed to find a backward filter convolution algorithm.";
                } else {
                  back_algo_w_.Set(bwd_filter_algo[i].algo, false);
                }
              }
              // Backprop-to-Data Algorithm Get(), v6 and earlier
              if (!param_.cudnn_tune.value()) {
                cudnnConvolutionBwdDataAlgo_t fastest_bwd_data_algo;
                CUDNN_CALL(cudnnGetConvolutionBackwardDataAlgorithm(s->dnn_handle_,
                                                                    filter_desc_,
                                                                    out_desc_,
                                                                    back_conv_desc_,
                                                                    in_desc_,
                                                                    CUDNN_CONVOLUTION_BWD_DATA_SPECIFY_WORKSPACE_LIMIT,
                                                                    workspace_byte,
                                                                    &fastest_bwd_data_algo));
                back_algo_.Set(fastest_bwd_data_algo, false);
              } else {
                cudnnConvolutionBwdDataAlgoPerf_t bwd_data_algo[kMaxAlgos];
                CUDNN_CALL(cudnnFindConvolutionBackwardDataAlgorithm(s->dnn_handle_,
                                                                     filter_desc_,
                                                                     out_desc_,
                                                                     back_conv_desc_,
                                                                     in_desc_,
                                                                     kMaxAlgos,
                                                                     &nalgo,
                                                                     bwd_data_algo));
                i = 0;
                while (i < nalgo
                       && (bwd_data_algo[i].status != CUDNN_STATUS_SUCCESS
                           || (param_.cudnn_tune.value() == qconv::kLimited
                               && bwd_data_algo[i].memory > workspace_byte)))
                  ++i;
                if (i == nalgo) {
                  LOG(FATAL) << "Failed to find a backward data convolution algorithm.";
                } else {
                  back_algo_.Set(bwd_data_algo[i].algo, false);
                }
              }
            #endif  // CUDNN_MAJOR < 7
            // An algo specification by the user may be cached here, but another
            // convolution will match only if identically specified.
            // We're caching results of *Get* as well as *Find*, but these records
            // will be held distinctly because param_.cudnn_tune is part of the key.
            CuDNNConvAlgoReg::Get()->Register(conv_param, in_shape, out_shape, dtype_,
                                              cudnn_forward_compute_type,
                                              cudnn_backward_compute_type,
                                              SMArch(ctx.dev_id), this->forward_algo_,
                                              this->back_algo_, this->back_algo_w_);
            on_complete();
        }, ctx, {}, {var});
        Engine::Get()->WaitForVar(var);
        Engine::Get()->DeleteVariable([](RunContext s) {}, ctx, var);
      }
      // If we're allowing Tensor Core variants of the algos to be considered in
      // *Find*() or *Get*(), but a non-Tensor-Core algo variant is the fastest,
      // we must change the descriptor to preclude Tensor Core.  Simplest is to
      // once again set the mathType in all cases.
      #if CUDNN_MAJOR >= 7
        CUDNN_CALL(cudnnSetConvolutionMathType(forward_conv_desc_, forward_algo_.MathType()));
        CUDNN_CALL(cudnnSetConvolutionMathType(back_conv_desc_, back_algo_.MathType()));
        CUDNN_CALL(cudnnSetConvolutionMathType(back_conv_desc_w_, back_algo_w_.MathType()));
      #endif
    }

    // Look over the results from *Find*() or *Get*() and pick the fastest algo given possible
    // workspace constraints.
    template <typename PerfType, typename AlgoType>
    void AlgoFinalSelect(const std::vector<PerfType> &perf_results, std::string kernel_name,
                         size_t workspace_byte, CuDNNAlgo<AlgoType> *algo) {
      // Determine the fastest acceptable algo that matches the algo_preference (-1 = any),
      // regardless of mathType.
      for (decltype(perf_results.size()) i = 0; i != perf_results.size(); ++i) {
        const auto &result = perf_results[i];
        bool algo_is_tensor_core = false;
        #if CUDNN_MAJOR >= 7
          algo_is_tensor_core = result.mathType == CUDNN_TENSOR_OP_MATH;
        #endif
        if (result.status == CUDNN_STATUS_SUCCESS &&
            (param_.cudnn_tune.value() != conv::kLimited || result.memory <= workspace_byte)) {
          algo->Set(result.algo, algo_is_tensor_core);
          return;
        }
      }
      auto mode = param_.cudnn_tune.value() == conv::kOff ? " get " : " find ";
      LOG(FATAL) << "Failed to" << mode << "any " << kernel_name << " convolution algorithm.";
    }

  void GetTempSize(const OpContext& ctx) {
    if (init_temp_size_) return;
    mshadow::Stream<gpu> *s = ctx.get_stream<gpu>();
    size_t back_size = 0, back_size_w = 0;
    CUDNN_CALL(cudnnGetConvolutionBackwardDataWorkspaceSize(s->dnn_handle_,
               filter_desc_,
               out_desc_,
               back_conv_desc_,
               in_desc_,
               back_algo_.AlgoNumber(),
               &back_size));
    CUDNN_CALL(cudnnGetConvolutionBackwardFilterWorkspaceSize(s->dnn_handle_,
               in_desc_,
               out_desc_,
               back_conv_desc_,
               filter_desc_,
               back_algo_w_.AlgoNumber(),
               &back_size_w));
    backward_workspace_byte_ = std::max(back_size, back_size_w);
    CUDNN_CALL(cudnnGetConvolutionForwardWorkspaceSize(s->dnn_handle_,
               in_desc_padded_,
               filter_desc_,
               forward_conv_desc_,
               out_desc_,
               forward_algo_.AlgoNumber(),
               &forward_workspace_byte_));

    init_temp_size_ = true;
  }

  int *CastTShapeToIntPtr(const TShape& s, std::vector<int> *buffer) {
    buffer->resize(s.ndim());
    nnvm::ShapeTypeCast(s.begin(), s.end(), buffer->data());
    return buffer->data();
  }

  void InitBufferForParam() {
    CastTShapeToIntPtr(param_.stride, &param_stride_);
    CastTShapeToIntPtr(param_.dilate, &param_dilate_);
    CastTShapeToIntPtr(param_.pad, &param_pad_);
  }

  // Allocates a 1D Tensor of words with size in bytes >= `size_bytes`.
  // Always allocates at least one word.
  mshadow::Tensor<gpu, 1, DType> AllocateTempWorkspace(const OpContext &ctx, size_t size_bytes) {
    mshadow::Stream<gpu> *s = ctx.get_stream<gpu>();
    size_t size_words = size_bytes / sizeof(DType) + 1;
    return ctx.requested[conv::kTempSpace].get_space_typed<gpu, 1, DType>(
        mshadow::Shape1(size_words), s);
  }

  // Returns the size in bytes of the 1D Tensor of words.
  size_t TensorSizeBytes(const mshadow::Tensor<gpu, 1, DType> &tensor) {
    return tensor.MSize() * sizeof(DType);
  }

  std::vector<int> param_stride_;
  std::vector<int> param_dilate_;
  std::vector<int> param_pad_;

  bool init_cudnn_;
  bool init_temp_size_;
  // Temp workspace size in bytes needed for Forward() operation.
  size_t forward_workspace_byte_;
  // Temp workspace size in bytes needed for Backward() operation.
  size_t backward_workspace_byte_;
  size_t data_offset_;
  size_t data_offset_padded_;
  size_t out_offset_;
  size_t weight_offset_;
  size_t bias_offset_;
  cudnnDataType_t dtype_;
  cudnnTensorDescriptor_t in_desc_;
  cudnnTensorDescriptor_t in_desc_padded_;
  cudnnTensorDescriptor_t out_desc_;
  cudnnTensorDescriptor_t bias_desc_;
  cudnnFilterDescriptor_t filter_desc_;
  // Convolution descriptor for forward inference operation
  cudnnConvolutionDescriptor_t forward_conv_desc_;
  // Convolution descriptor for back-prop operations to the data
  cudnnConvolutionDescriptor_t back_conv_desc_;
  // Convolution descriptor for back-prop operations to the weights
  cudnnConvolutionDescriptor_t back_conv_desc_w_;
  // Algorithm for the forward inference operation
  CuDNNAlgo<cudnnConvolutionFwdAlgo_t> forward_algo_;
  // Algorithm for the back-prop operation to the data
  CuDNNAlgo<cudnnConvolutionBwdDataAlgo_t> back_algo_;
  // Algorithm for the back-prop operation to the weights
  CuDNNAlgo<cudnnConvolutionBwdFilterAlgo_t> back_algo_w_;
  cudnnTensorFormat_t format_;
  // Allow TensorCore algo policy
  bool cudnn_tensor_core_;
  QConvolutionParam param_;
};
#endif  // __CUDACC__ && CUDNN
}  // namespace op
}  // namespace mxnet

#endif  // MXNET_OPERATOR_Q_CUDNN_CONVOLUTION_INL_H_
