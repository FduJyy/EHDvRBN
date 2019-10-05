# File content is auto-generated. Do not modify.
# pylint: skip-file
from ._internal import SymbolBase
from ..base import _Null

def _CachedOp(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _CrossDeviceCopy(name=None, attr=None, out=None, **kwargs):
    r"""Special op to copy data cross device

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _CustomFunction(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _Div(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""Divides arguments element-wise.

    The storage type of ``elemwise_div`` output is always dense



    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _DivScalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Divide an array with a scalar.

    ``_div_scalar`` only operates on data array of input if input is sparse.

    For example, if input of shape (100, 100) has only 2 non zero elements,
    i.e. input.data = [5, 6], scalar = nan,
    it will result output.data = [nan, nan] instead of 10000 nans.



    Defined in /home/jyy/hotspot/mxnet/src/operator/tensor/elemwise_binary_scalar_op_basic.cc:L164

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _Equal(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _EqualScalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _Greater(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _GreaterEqualScalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _GreaterScalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _Greater_Equal(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _Hypot(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""Given the "legs" of a right triangle, return its hypotenuse.



    Defined in /home/jyy/hotspot/mxnet/src/operator/tensor/elemwise_binary_op_extended.cc:L79

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _HypotScalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _Lesser(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _LesserEqualScalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _LesserScalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _Lesser_Equal(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _Maximum(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _MaximumScalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _Minimum(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _MinimumScalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _Minus(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""Subtracts arguments element-wise.

    The storage type of ``elemwise_sub`` output depends on storage types of inputs

       - elemwise_sub(row_sparse, row_sparse) = row_sparse
       - elemwise_sub(csr, csr) = csr
       - otherwise, ``elemwise_sub`` generates output with default storage



    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _MinusScalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _Mod(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _ModScalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _Mul(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""Multiplies arguments element-wise.

    The storage type of ``elemwise_mul`` output depends on storage types of inputs

       - elemwise_mul(default, default) = default
       - elemwise_mul(row_sparse, row_sparse) = row_sparse
       - elemwise_mul(default, row_sparse) = default
       - elemwise_mul(row_sparse, default) = default
       - elemwise_mul(csr, csr) = csr
       - otherwise, ``elemwise_mul`` generates output with default storage



    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _MulScalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Multiply an array with a scalar.

    ``_mul_scalar`` only operates on data array of input if input is sparse.

    For example, if input of shape (100, 100) has only 2 non zero elements,
    i.e. input.data = [5, 6], scalar = nan,
    it will result output.data = [nan, nan] instead of 10000 nans.



    Defined in /home/jyy/hotspot/mxnet/src/operator/tensor/elemwise_binary_scalar_op_basic.cc:L142

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _NDArray(*data, **kwargs):
    r"""Stub for implementing an operator implemented in native frontend language with ndarray.

    Parameters
    ----------
    data : Symbol[]
        Input data for the custom operator.
    info : ptr, required

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _Native(*data, **kwargs):
    r"""Stub for implementing an operator implemented in native frontend language.

    Parameters
    ----------
    data : Symbol[]
        Input data for the custom operator.
    info : ptr, required
    need_top_grad : boolean, optional, default=1
        Whether this layer needs out grad for backward. Should be false for loss layers.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _NoGradient(name=None, attr=None, out=None, **kwargs):
    r"""Place holder for variable who cannot perform gradient

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _NotEqualScalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _Not_Equal(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _Plus(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""Adds arguments element-wise.

    The storage type of ``elemwise_add`` output depends on storage types of inputs

       - elemwise_add(row_sparse, row_sparse) = row_sparse
       - elemwise_add(csr, csr) = csr
       - otherwise, ``elemwise_add`` generates output with default storage



    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _PlusScalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _Power(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _PowerScalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _RDivScalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _RMinusScalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _RModScalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _RPowerScalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _add(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""Adds arguments element-wise.

    The storage type of ``elemwise_add`` output depends on storage types of inputs

       - elemwise_add(row_sparse, row_sparse) = row_sparse
       - elemwise_add(csr, csr) = csr
       - otherwise, ``elemwise_add`` generates output with default storage



    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _arange(start=_Null, stop=_Null, step=_Null, repeat=_Null, ctx=_Null, dtype=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Return evenly spaced values within a given interval. Similar to Numpy

    Parameters
    ----------
    start : double, required
        Start of interval. The interval includes this value. The default start value is 0.
    stop : double or None, optional, default=None
        End of interval. The interval does not include this value, except in some cases where step is not an integer and floating point round-off affects the length of out.
    step : double, optional, default=1
        Spacing between values.
    repeat : int, optional, default='1'
        The repeating time of all elements. E.g repeat=3, the element a will be repeated three times --> a, a, a.
    ctx : string, optional, default=''
        Context of output, in format [cpu|gpu|cpu_pinned](n).Only used for imperative calls.
    dtype : {'float16', 'float32', 'float64', 'int32', 'int64', 'uint8'},optional, default='float32'
        Target data type.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_Activation(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_BatchNorm(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_BatchNorm_v1(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_BilinearSampler(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_CachedOp(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_Concat(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_Convolution(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_Convolution_v1(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_Correlation(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_Crop(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_CuDNNBatchNorm(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_Custom(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_CustomFunction(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_Deconvolution(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_Dropout(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_Embedding(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_FullyConnected(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_GridGenerator(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_IdentityAttachKLSparseReg(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_InstanceNorm(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_L2Normalization(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_LRN(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_LeakyReLU(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_LinearRegressionOutput(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_LogisticRegressionOutput(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_MAERegressionOutput(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_MakeLoss(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_Pad(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_Pooling(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_Pooling_v1(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_QActivation(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_QConvolution(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_QConvolution_v1(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_QFullyConnected(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_RNN(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_ROIPooling(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_SVMOutput(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_SequenceLast(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_SequenceMask(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_SequenceReverse(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_SliceChannel(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_Softmax(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_SoftmaxActivation(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_SoftmaxOutput(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_SparseEmbedding(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_SpatialTransformer(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_SwapAxis(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_UpSampling(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward__CrossDeviceCopy(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward__NDArray(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward__Native(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward__contrib_CTCLoss(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward__contrib_DeformableConvolution(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward__contrib_DeformablePSROIPooling(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward__contrib_MultiBoxDetection(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward__contrib_MultiBoxPrior(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward__contrib_MultiBoxTarget(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward__contrib_MultiProposal(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward__contrib_PSROIPooling(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward__contrib_Proposal(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward__contrib_count_sketch(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward__contrib_fft(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward__contrib_ifft(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_abs(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_add(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_arccos(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_arccosh(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_arcsin(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_arcsinh(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_arctan(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_arctanh(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_batch_dot(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_broadcast_add(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_broadcast_div(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_broadcast_hypot(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_broadcast_maximum(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_broadcast_minimum(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_broadcast_mod(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_broadcast_mul(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_broadcast_power(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_broadcast_sub(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_cast(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_cbrt(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_clip(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_copy(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_cos(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_cosh(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_degrees(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_div(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_div_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_dot(transpose_a=_Null, transpose_b=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    transpose_a : boolean, optional, default=0
        If true then transpose the first input before dot.
    transpose_b : boolean, optional, default=0
        If true then transpose the second input before dot.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_expm1(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_gamma(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_gammaln(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_hypot(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_hypot_scalar(lhs=None, rhs=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input
    scalar : float
        scalar value

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_linalg_gelqf(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_linalg_gemm(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_linalg_gemm2(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_linalg_potrf(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_linalg_potri(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_linalg_sumlogdiag(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_linalg_syevd(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_linalg_syrk(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_linalg_trmm(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_linalg_trsm(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_log(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_log10(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_log1p(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_log2(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_log_softmax(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_max(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_maximum(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_maximum_scalar(lhs=None, rhs=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input
    scalar : float
        scalar value

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_mean(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_min(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_minimum(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_minimum_scalar(lhs=None, rhs=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input
    scalar : float
        scalar value

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_mod(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_mod_scalar(lhs=None, rhs=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input
    scalar : float
        scalar value

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_mul(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_mul_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_nanprod(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_nansum(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_pick(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_power(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_power_scalar(lhs=None, rhs=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input
    scalar : float
        scalar value

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_prod(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_radians(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_rcbrt(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_rdiv_scalar(lhs=None, rhs=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input
    scalar : float
        scalar value

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_reciprocal(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_relu(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_repeat(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_reverse(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_rmod_scalar(lhs=None, rhs=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input
    scalar : float
        scalar value

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_rpower_scalar(lhs=None, rhs=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input
    scalar : float
        scalar value

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_rsqrt(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_sample_multinomial(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_sigmoid(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_sign(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_sin(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_sinh(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_slice(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_slice_axis(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_smooth_l1(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_softmax(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_softmax_cross_entropy(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_sparse_retain(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_sqrt(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_square(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_square_sum(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_stack(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_sub(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_sum(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_take(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_tan(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_tanh(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_tile(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_topk(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _backward_where(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _broadcast_backward(name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------


    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _copy(data=None, name=None, attr=None, out=None, **kwargs):
    r"""Returns a copy of the input.

    From:/home/jyy/hotspot/mxnet/src/operator/tensor/elemwise_unary_op_basic.cc:112

    Parameters
    ----------
    data : Symbol
        The input array.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _copyto(data=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : NDArray
        input data

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _crop_assign(lhs=None, rhs=None, begin=_Null, end=_Null, step=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Assign the rhs to a cropped subset of lhs.

    Requirements
    ------------
    - output should be explicitly given and be the same as lhs.
    - lhs and rhs are of the same data type, and on the same device.


    From:/home/jyy/hotspot/mxnet/src/operator/tensor/matrix_op.cc:319

    Parameters
    ----------
    lhs : Symbol
        Source input
    rhs : Symbol
        value to assign
    begin : Shape(tuple), required
        starting indices for the slice operation, supports negative indices.
    end : Shape(tuple), required
        ending indices for the slice operation, supports negative indices.
    step : Shape(tuple), optional, default=[]
        step for the slice operation, supports negative values.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _crop_assign_scalar(data=None, scalar=_Null, begin=_Null, end=_Null, step=_Null, name=None, attr=None, out=None, **kwargs):
    r"""(Assign the scalar to a cropped subset of the input.

    Requirements
    ------------
    - output should be explicitly given and be the same as input
    )

    From:/home/jyy/hotspot/mxnet/src/operator/tensor/matrix_op.cc:344

    Parameters
    ----------
    data : Symbol
        Source input
    scalar : float, optional, default=0
        The scalar value for assignment.
    begin : Shape(tuple), required
        starting indices for the slice operation, supports negative indices.
    end : Shape(tuple), required
        ending indices for the slice operation, supports negative indices.
    step : Shape(tuple), optional, default=[]
        step for the slice operation, supports negative values.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _cvcopyMakeBorder(src=None, top=_Null, bot=_Null, left=_Null, right=_Null, type=_Null, value=_Null, values=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Pad image border with OpenCV. 


    Parameters
    ----------
    src : NDArray
        source image
    top : int, required
        Top margin.
    bot : int, required
        Bottom margin.
    left : int, required
        Left margin.
    right : int, required
        Right margin.
    type : int, optional, default='0'
        Filling type (default=cv2.BORDER_CONSTANT).
    value : double, optional, default=0
        (Deprecated! Use ``values`` instead.) Fill with single value.
    values : tuple of <double>, optional, default=[]
        Fill with value(RGB[A] or gray), up to 4 channels.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _cvimdecode(buf=None, flag=_Null, to_rgb=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Decode image with OpenCV. 
    Note: return image in RGB by default, instead of OpenCV's default BGR.

    Parameters
    ----------
    buf : NDArray
        Buffer containing binary encoded image
    flag : int, optional, default='1'
        Convert decoded image to grayscale (0) or color (1).
    to_rgb : boolean, optional, default=1
        Whether to convert decoded image to mxnet's default RGB format (instead of opencv's default BGR).

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _cvimread(filename=_Null, flag=_Null, to_rgb=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Read and decode image with OpenCV. 
    Note: return image in RGB by default, instead of OpenCV's default BGR.

    Parameters
    ----------
    filename : string, required
        Name of the image file to be loaded.
    flag : int, optional, default='1'
        Convert decoded image to grayscale (0) or color (1).
    to_rgb : boolean, optional, default=1
        Whether to convert decoded image to mxnet's default RGB format (instead of opencv's default BGR).

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _cvimresize(src=None, w=_Null, h=_Null, interp=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Resize image with OpenCV. 


    Parameters
    ----------
    src : NDArray
        source image
    w : int, required
        Width of resized image.
    h : int, required
        Height of resized image.
    interp : int, optional, default='1'
        Interpolation method (default=cv2.INTER_LINEAR).

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _div(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""Divides arguments element-wise.

    The storage type of ``elemwise_div`` output is always dense



    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _div_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Divide an array with a scalar.

    ``_div_scalar`` only operates on data array of input if input is sparse.

    For example, if input of shape (100, 100) has only 2 non zero elements,
    i.e. input.data = [5, 6], scalar = nan,
    it will result output.data = [nan, nan] instead of 10000 nans.



    Defined in /home/jyy/hotspot/mxnet/src/operator/tensor/elemwise_binary_scalar_op_basic.cc:L164

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _equal(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _equal_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _full(shape=_Null, ctx=_Null, dtype=_Null, value=_Null, name=None, attr=None, out=None, **kwargs):
    r"""fill target with a scalar value

    Parameters
    ----------
    shape : Shape(tuple), optional, default=[]
        The shape of the output
    ctx : string, optional, default=''
        Context of output, in format [cpu|gpu|cpu_pinned](n).Only used for imperative calls.
    dtype : {'float16', 'float32', 'float64', 'int32', 'uint8'},optional, default='float32'
        Target data type.
    value : double, required
        Value with which to fill newly created tensor

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _grad_add(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _greater(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _greater_equal(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _greater_equal_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _greater_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _hypot(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""Given the "legs" of a right triangle, return its hypotenuse.



    Defined in /home/jyy/hotspot/mxnet/src/operator/tensor/elemwise_binary_op_extended.cc:L79

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _hypot_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _identity_with_attr_like_rhs(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        First input.
    rhs : Symbol
        Second input.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _imdecode(mean=None, index=_Null, x0=_Null, y0=_Null, x1=_Null, y1=_Null, c=_Null, size=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Decode an image, clip to (x0, y0, x1, y1), subtract mean, and write to buffer

    Parameters
    ----------
    mean : Symbol
        image mean
    index : int
        buffer position for output
    x0 : int
        x0
    y0 : int
        y0
    x1 : int
        x1
    y1 : int
        y1
    c : int
        channel
    size : int
        length of str_img

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _lesser(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _lesser_equal(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _lesser_equal_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _lesser_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _maximum(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _maximum_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _minimum(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _minimum_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _minus(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""Subtracts arguments element-wise.

    The storage type of ``elemwise_sub`` output depends on storage types of inputs

       - elemwise_sub(row_sparse, row_sparse) = row_sparse
       - elemwise_sub(csr, csr) = csr
       - otherwise, ``elemwise_sub`` generates output with default storage



    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _minus_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _mod(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _mod_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _mul(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""Multiplies arguments element-wise.

    The storage type of ``elemwise_mul`` output depends on storage types of inputs

       - elemwise_mul(default, default) = default
       - elemwise_mul(row_sparse, row_sparse) = row_sparse
       - elemwise_mul(default, row_sparse) = default
       - elemwise_mul(row_sparse, default) = default
       - elemwise_mul(csr, csr) = csr
       - otherwise, ``elemwise_mul`` generates output with default storage



    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _mul_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Multiply an array with a scalar.

    ``_mul_scalar`` only operates on data array of input if input is sparse.

    For example, if input of shape (100, 100) has only 2 non zero elements,
    i.e. input.data = [5, 6], scalar = nan,
    it will result output.data = [nan, nan] instead of 10000 nans.



    Defined in /home/jyy/hotspot/mxnet/src/operator/tensor/elemwise_binary_scalar_op_basic.cc:L142

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _not_equal(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _not_equal_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _onehot_encode(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : NDArray
        Left operand to the function.
    rhs : NDArray
        Right operand to the function.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _ones(shape=_Null, ctx=_Null, dtype=_Null, name=None, attr=None, out=None, **kwargs):
    r"""fill target with ones

    Parameters
    ----------
    shape : Shape(tuple), optional, default=[]
        The shape of the output
    ctx : string, optional, default=''
        Context of output, in format [cpu|gpu|cpu_pinned](n).Only used for imperative calls.
    dtype : {'float16', 'float32', 'float64', 'int32', 'uint8'},optional, default='float32'
        Target data type.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _plus(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""Adds arguments element-wise.

    The storage type of ``elemwise_add`` output depends on storage types of inputs

       - elemwise_add(row_sparse, row_sparse) = row_sparse
       - elemwise_add(csr, csr) = csr
       - otherwise, ``elemwise_add`` generates output with default storage



    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _plus_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _power(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _power_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _random_exponential(lam=_Null, shape=_Null, ctx=_Null, dtype=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Draw random samples from an exponential distribution.

    Samples are distributed according to an exponential distribution parametrized by *lambda* (rate).

    Example::

       exponential(lam=4, shape=(2,2)) = [[ 0.0097189 ,  0.08999364],
                                          [ 0.04146638,  0.31715935]]


    Defined in /home/jyy/hotspot/mxnet/src/operator/random/sample_op.cc:L115

    Parameters
    ----------
    lam : float, optional, default=1
        Lambda parameter (rate) of the exponential distribution.
    shape : Shape(tuple), optional, default=[]
        Shape of the output.
    ctx : string, optional, default=''
        Context of output, in format [cpu|gpu|cpu_pinned](n). Only used for imperative calls.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _random_gamma(alpha=_Null, beta=_Null, shape=_Null, ctx=_Null, dtype=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Draw random samples from a gamma distribution.

    Samples are distributed according to a gamma distribution parametrized by *alpha* (shape) and *beta* (scale).

    Example::

       gamma(alpha=9, beta=0.5, shape=(2,2)) = [[ 7.10486984,  3.37695289],
                                                [ 3.91697288,  3.65933681]]


    Defined in /home/jyy/hotspot/mxnet/src/operator/random/sample_op.cc:L100

    Parameters
    ----------
    alpha : float, optional, default=1
        Alpha parameter (shape) of the gamma distribution.
    beta : float, optional, default=1
        Beta parameter (scale) of the gamma distribution.
    shape : Shape(tuple), optional, default=[]
        Shape of the output.
    ctx : string, optional, default=''
        Context of output, in format [cpu|gpu|cpu_pinned](n). Only used for imperative calls.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _random_generalized_negative_binomial(mu=_Null, alpha=_Null, shape=_Null, ctx=_Null, dtype=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Draw random samples from a generalized negative binomial distribution.

    Samples are distributed according to a generalized negative binomial distribution parametrized by
    *mu* (mean) and *alpha* (dispersion). *alpha* is defined as *1/k* where *k* is the failure limit of the
    number of unsuccessful experiments (generalized to real numbers).
    Samples will always be returned as a floating point data type.

    Example::

       generalized_negative_binomial(mu=2.0, alpha=0.3, shape=(2,2)) = [[ 2.,  1.],
                                                                        [ 6.,  4.]]


    Defined in /home/jyy/hotspot/mxnet/src/operator/random/sample_op.cc:L168

    Parameters
    ----------
    mu : float, optional, default=1
        Mean of the negative binomial distribution.
    alpha : float, optional, default=1
        Alpha (dispersion) parameter of the negative binomial distribution.
    shape : Shape(tuple), optional, default=[]
        Shape of the output.
    ctx : string, optional, default=''
        Context of output, in format [cpu|gpu|cpu_pinned](n). Only used for imperative calls.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _random_negative_binomial(k=_Null, p=_Null, shape=_Null, ctx=_Null, dtype=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Draw random samples from a negative binomial distribution.

    Samples are distributed according to a negative binomial distribution parametrized by
    *k* (limit of unsuccessful experiments) and *p* (failure probability in each experiment).
    Samples will always be returned as a floating point data type.

    Example::

       negative_binomial(k=3, p=0.4, shape=(2,2)) = [[ 4.,  7.],
                                                     [ 2.,  5.]]


    Defined in /home/jyy/hotspot/mxnet/src/operator/random/sample_op.cc:L149

    Parameters
    ----------
    k : int, optional, default='1'
        Limit of unsuccessful experiments.
    p : float, optional, default=1
        Failure probability in each experiment.
    shape : Shape(tuple), optional, default=[]
        Shape of the output.
    ctx : string, optional, default=''
        Context of output, in format [cpu|gpu|cpu_pinned](n). Only used for imperative calls.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _random_normal(loc=_Null, scale=_Null, shape=_Null, ctx=_Null, dtype=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Draw random samples from a normal (Gaussian) distribution.

    .. note:: The existing alias ``normal`` is deprecated.

    Samples are distributed according to a normal distribution parametrized by *loc* (mean) and *scale* (standard deviation).

    Example::

       normal(loc=0, scale=1, shape=(2,2)) = [[ 1.89171135, -1.16881478],
                                              [-1.23474145,  1.55807114]]


    Defined in /home/jyy/hotspot/mxnet/src/operator/random/sample_op.cc:L85

    Parameters
    ----------
    loc : float, optional, default=0
        Mean of the distribution.
    scale : float, optional, default=1
        Standard deviation of the distribution.
    shape : Shape(tuple), optional, default=[]
        Shape of the output.
    ctx : string, optional, default=''
        Context of output, in format [cpu|gpu|cpu_pinned](n). Only used for imperative calls.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _random_poisson(lam=_Null, shape=_Null, ctx=_Null, dtype=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Draw random samples from a Poisson distribution.

    Samples are distributed according to a Poisson distribution parametrized by *lambda* (rate).
    Samples will always be returned as a floating point data type.

    Example::

       poisson(lam=4, shape=(2,2)) = [[ 5.,  2.],
                                      [ 4.,  6.]]


    Defined in /home/jyy/hotspot/mxnet/src/operator/random/sample_op.cc:L132

    Parameters
    ----------
    lam : float, optional, default=1
        Lambda parameter (rate) of the Poisson distribution.
    shape : Shape(tuple), optional, default=[]
        Shape of the output.
    ctx : string, optional, default=''
        Context of output, in format [cpu|gpu|cpu_pinned](n). Only used for imperative calls.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _random_uniform(low=_Null, high=_Null, shape=_Null, ctx=_Null, dtype=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Draw random samples from a uniform distribution.

    .. note:: The existing alias ``uniform`` is deprecated.

    Samples are uniformly distributed over the half-open interval *[low, high)*
    (includes *low*, but excludes *high*).

    Example::

       uniform(low=0, high=1, shape=(2,2)) = [[ 0.60276335,  0.85794562],
                                              [ 0.54488319,  0.84725171]]



    Defined in /home/jyy/hotspot/mxnet/src/operator/random/sample_op.cc:L66

    Parameters
    ----------
    low : float, optional, default=0
        Lower bound of the distribution.
    high : float, optional, default=1
        Upper bound of the distribution.
    shape : Shape(tuple), optional, default=[]
        Shape of the output.
    ctx : string, optional, default=''
        Context of output, in format [cpu|gpu|cpu_pinned](n). Only used for imperative calls.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _rdiv_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _rminus_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _rmod_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _rpower_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _sample_exponential(lam=None, shape=_Null, dtype=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Concurrent sampling from multiple
    exponential distributions with parameters lambda (rate).

    The parameters of the distributions are provided as an input array.
    Let *[s]* be the shape of the input array, *n* be the dimension of *[s]*, *[t]*
    be the shape specified as the parameter of the operator, and *m* be the dimension
    of *[t]*. Then the output will be a *(n+m)*-dimensional array with shape *[s]x[t]*.

    For any valid *n*-dimensional index *i* with respect to the input array, *output[i]*
    will be an *m*-dimensional array that holds randomly drawn samples from the distribution
    which is parameterized by the input value at index *i*. If the shape parameter of the
    operator is not set, then one sample will be drawn per distribution and the output array
    has the same shape as the input array.

    Examples::

       lam = [ 1.0, 8.5 ]

       // Draw a single sample for each distribution
       sample_exponential(lam) = [ 0.51837951,  0.09994757]

       // Draw a vector containing two samples for each distribution
       sample_exponential(lam, shape=(2)) = [[ 0.51837951,  0.19866663],
                                             [ 0.09994757,  0.50447971]]


    Defined in /home/jyy/hotspot/mxnet/src/operator/random/multisample_op.cc:L283

    Parameters
    ----------
    lam : Symbol
        Lambda (rate) parameters of the distributions.
    shape : Shape(tuple), optional, default=[]
        Shape to be sampled from each random distribution.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _sample_gamma(alpha=None, beta=None, shape=_Null, dtype=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Concurrent sampling from multiple
    gamma distributions with parameters *alpha* (shape) and *beta* (scale).

    The parameters of the distributions are provided as input arrays.
    Let *[s]* be the shape of the input arrays, *n* be the dimension of *[s]*, *[t]*
    be the shape specified as the parameter of the operator, and *m* be the dimension
    of *[t]*. Then the output will be a *(n+m)*-dimensional array with shape *[s]x[t]*.

    For any valid *n*-dimensional index *i* with respect to the input arrays, *output[i]*
    will be an *m*-dimensional array that holds randomly drawn samples from the distribution
    which is parameterized by the input values at index *i*. If the shape parameter of the
    operator is not set, then one sample will be drawn per distribution and the output array
    has the same shape as the input arrays.

    Examples::

       alpha = [ 0.0, 2.5 ]
       beta = [ 1.0, 0.7 ]

       // Draw a single sample for each distribution
       sample_gamma(alpha, beta) = [ 0.        ,  2.25797319]

       // Draw a vector containing two samples for each distribution
       sample_gamma(alpha, beta, shape=(2)) = [[ 0.        ,  0.        ],
                                               [ 2.25797319,  1.70734084]]


    Defined in /home/jyy/hotspot/mxnet/src/operator/random/multisample_op.cc:L281

    Parameters
    ----------
    alpha : Symbol
        Alpha (shape) parameters of the distributions.
    shape : Shape(tuple), optional, default=[]
        Shape to be sampled from each random distribution.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).
    beta : Symbol
        Beta (scale) parameters of the distributions.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _sample_generalized_negative_binomial(mu=None, alpha=None, shape=_Null, dtype=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Concurrent sampling from multiple
    generalized negative binomial distributions with parameters *mu* (mean) and *alpha* (dispersion).

    The parameters of the distributions are provided as input arrays.
    Let *[s]* be the shape of the input arrays, *n* be the dimension of *[s]*, *[t]*
    be the shape specified as the parameter of the operator, and *m* be the dimension
    of *[t]*. Then the output will be a *(n+m)*-dimensional array with shape *[s]x[t]*.

    For any valid *n*-dimensional index *i* with respect to the input arrays, *output[i]*
    will be an *m*-dimensional array that holds randomly drawn samples from the distribution
    which is parameterized by the input values at index *i*. If the shape parameter of the
    operator is not set, then one sample will be drawn per distribution and the output array
    has the same shape as the input arrays.

    Samples will always be returned as a floating point data type.

    Examples::

       mu = [ 2.0, 2.5 ]
       alpha = [ 1.0, 0.1 ]

       // Draw a single sample for each distribution
       sample_generalized_negative_binomial(mu, alpha) = [ 0.,  3.]

       // Draw a vector containing two samples for each distribution
       sample_generalized_negative_binomial(mu, alpha, shape=(2)) = [[ 0.,  3.],
                                                                     [ 3.,  1.]]


    Defined in /home/jyy/hotspot/mxnet/src/operator/random/multisample_op.cc:L292

    Parameters
    ----------
    mu : Symbol
        Means of the distributions.
    shape : Shape(tuple), optional, default=[]
        Shape to be sampled from each random distribution.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).
    alpha : Symbol
        Alpha (dispersion) parameters of the distributions.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _sample_multinomial(data=None, shape=_Null, get_prob=_Null, dtype=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Concurrent sampling from multiple multinomial distributions.

    *data* is an *n* dimensional array whose last dimension has length *k*, where
    *k* is the number of possible outcomes of each multinomial distribution. This
    operator will draw *shape* samples from each distribution. If shape is empty
    one sample will be drawn from each distribution.

    If *get_prob* is true, a second array containing log likelihood of the drawn
    samples will also be returned. This is usually used for reinforcement learning
    where you can provide reward as head gradient for this array to estimate
    gradient.

    Note that the input distribution must be normalized, i.e. *data* must sum to
    1 along its last axis.

    Examples::

       probs = [[0, 0.1, 0.2, 0.3, 0.4], [0.4, 0.3, 0.2, 0.1, 0]]

       // Draw a single sample for each distribution
       sample_multinomial(probs) = [3, 0]

       // Draw a vector containing two samples for each distribution
       sample_multinomial(probs, shape=(2)) = [[4, 2],
                                               [0, 0]]

       // requests log likelihood
       sample_multinomial(probs, get_prob=True) = [2, 1], [0.2, 0.3]


    Parameters
    ----------
    data : Symbol
        Distribution probabilities. Must sum to one on the last axis.
    shape : Shape(tuple), optional, default=[]
        Shape to be sampled from each random distribution.
    get_prob : boolean, optional, default=0
        Whether to also return the log probability of sampled result. This is usually used for differentiating through stochastic variables, e.g. in reinforcement learning.
    dtype : {'int32'},optional, default='int32'
        DType of the output in case this can't be inferred. Only support int32 for now.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _sample_negative_binomial(k=None, p=None, shape=_Null, dtype=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Concurrent sampling from multiple
    negative binomial distributions with parameters *k* (failure limit) and *p* (failure probability).

    The parameters of the distributions are provided as input arrays.
    Let *[s]* be the shape of the input arrays, *n* be the dimension of *[s]*, *[t]*
    be the shape specified as the parameter of the operator, and *m* be the dimension
    of *[t]*. Then the output will be a *(n+m)*-dimensional array with shape *[s]x[t]*.

    For any valid *n*-dimensional index *i* with respect to the input arrays, *output[i]*
    will be an *m*-dimensional array that holds randomly drawn samples from the distribution
    which is parameterized by the input values at index *i*. If the shape parameter of the
    operator is not set, then one sample will be drawn per distribution and the output array
    has the same shape as the input arrays.

    Samples will always be returned as a floating point data type.

    Examples::

       k = [ 20, 49 ]
       p = [ 0.4 , 0.77 ]

       // Draw a single sample for each distribution
       sample_negative_binomial(k, p) = [ 15.,  16.]

       // Draw a vector containing two samples for each distribution
       sample_negative_binomial(k, p, shape=(2)) = [[ 15.,  50.],
                                                    [ 16.,  12.]]


    Defined in /home/jyy/hotspot/mxnet/src/operator/random/multisample_op.cc:L288

    Parameters
    ----------
    k : Symbol
        Limits of unsuccessful experiments.
    shape : Shape(tuple), optional, default=[]
        Shape to be sampled from each random distribution.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).
    p : Symbol
        Failure probabilities in each experiment.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _sample_normal(mu=None, sigma=None, shape=_Null, dtype=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Concurrent sampling from multiple
    normal distributions with parameters *mu* (mean) and *sigma* (standard deviation).

    The parameters of the distributions are provided as input arrays.
    Let *[s]* be the shape of the input arrays, *n* be the dimension of *[s]*, *[t]*
    be the shape specified as the parameter of the operator, and *m* be the dimension
    of *[t]*. Then the output will be a *(n+m)*-dimensional array with shape *[s]x[t]*.

    For any valid *n*-dimensional index *i* with respect to the input arrays, *output[i]*
    will be an *m*-dimensional array that holds randomly drawn samples from the distribution
    which is parameterized by the input values at index *i*. If the shape parameter of the
    operator is not set, then one sample will be drawn per distribution and the output array
    has the same shape as the input arrays.

    Examples::

       mu = [ 0.0, 2.5 ]
       sigma = [ 1.0, 3.7 ]

       // Draw a single sample for each distribution
       sample_normal(mu, sigma) = [-0.56410581,  0.95934606]

       // Draw a vector containing two samples for each distribution
       sample_normal(mu, sigma, shape=(2)) = [[-0.56410581,  0.2928229 ],
                                              [ 0.95934606,  4.48287058]]


    Defined in /home/jyy/hotspot/mxnet/src/operator/random/multisample_op.cc:L278

    Parameters
    ----------
    mu : Symbol
        Means of the distributions.
    shape : Shape(tuple), optional, default=[]
        Shape to be sampled from each random distribution.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).
    sigma : Symbol
        Standard deviations of the distributions.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _sample_poisson(lam=None, shape=_Null, dtype=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Concurrent sampling from multiple
    Poisson distributions with parameters lambda (rate).

    The parameters of the distributions are provided as an input array.
    Let *[s]* be the shape of the input array, *n* be the dimension of *[s]*, *[t]*
    be the shape specified as the parameter of the operator, and *m* be the dimension
    of *[t]*. Then the output will be a *(n+m)*-dimensional array with shape *[s]x[t]*.

    For any valid *n*-dimensional index *i* with respect to the input array, *output[i]*
    will be an *m*-dimensional array that holds randomly drawn samples from the distribution
    which is parameterized by the input value at index *i*. If the shape parameter of the
    operator is not set, then one sample will be drawn per distribution and the output array
    has the same shape as the input array.

    Samples will always be returned as a floating point data type.

    Examples::

       lam = [ 1.0, 8.5 ]

       // Draw a single sample for each distribution
       sample_poisson(lam) = [  0.,  13.]

       // Draw a vector containing two samples for each distribution
       sample_poisson(lam, shape=(2)) = [[  0.,   4.],
                                         [ 13.,   8.]]


    Defined in /home/jyy/hotspot/mxnet/src/operator/random/multisample_op.cc:L285

    Parameters
    ----------
    lam : Symbol
        Lambda (rate) parameters of the distributions.
    shape : Shape(tuple), optional, default=[]
        Shape to be sampled from each random distribution.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _sample_uniform(low=None, high=None, shape=_Null, dtype=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Concurrent sampling from multiple
    uniform distributions on the intervals given by *[low,high)*.

    The parameters of the distributions are provided as input arrays.
    Let *[s]* be the shape of the input arrays, *n* be the dimension of *[s]*, *[t]*
    be the shape specified as the parameter of the operator, and *m* be the dimension
    of *[t]*. Then the output will be a *(n+m)*-dimensional array with shape *[s]x[t]*.

    For any valid *n*-dimensional index *i* with respect to the input arrays, *output[i]*
    will be an *m*-dimensional array that holds randomly drawn samples from the distribution
    which is parameterized by the input values at index *i*. If the shape parameter of the
    operator is not set, then one sample will be drawn per distribution and the output array
    has the same shape as the input arrays.

    Examples::

       low = [ 0.0, 2.5 ]
       high = [ 1.0, 3.7 ]

       // Draw a single sample for each distribution
       sample_uniform(low, high) = [ 0.40451524,  3.18687344]

       // Draw a vector containing two samples for each distribution
       sample_uniform(low, high, shape=(2)) = [[ 0.40451524,  0.18017688],
                                               [ 3.18687344,  3.68352246]]


    Defined in /home/jyy/hotspot/mxnet/src/operator/random/multisample_op.cc:L276

    Parameters
    ----------
    low : Symbol
        Lower bounds of the distributions.
    shape : Shape(tuple), optional, default=[]
        Shape to be sampled from each random distribution.
    dtype : {'None', 'float16', 'float32', 'float64'},optional, default='None'
        DType of the output in case this can't be inferred. Defaults to float32 if not defined (dtype=None).
    high : Symbol
        Upper bounds of the distributions.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _scatter_elemwise_div(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""Divides arguments element-wise.  If the left-hand-side input is 'row_sparse', then
    only the values which exist in the left-hand sparse array are computed.  The 'missing' values
    are ignored.

    The storage type of ``_scatter_elemwise_div`` output depends on storage types of inputs

    - _scatter_elemwise_div(row_sparse, row_sparse) = row_sparse
    - _scatter_elemwise_div(row_sparse, dense) = row_sparse
    - _scatter_elemwise_div(row_sparse, csr) = row_sparse
    - otherwise, ``_scatter_elemwise_div`` behaves exactly like elemwise_div and generates output
    with default storage



    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _scatter_minus_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Subtracts a scalar to a tensor element-wise.  If the left-hand-side input is
    'row_sparse' or 'csr', then only the values which exist in the left-hand sparse array are computed.
    The 'missing' values are ignored.

    The storage type of ``_scatter_minus_scalar`` output depends on storage types of inputs

    - _scatter_minus_scalar(row_sparse, scalar) = row_sparse
    - _scatter_minus_scalar(csr, scalar) = csr
    - otherwise, ``_scatter_minus_scalar`` behaves exactly like _minus_scalar and generates output
    with default storage



    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _scatter_plus_scalar(data=None, scalar=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Adds a scalar to a tensor element-wise.  If the left-hand-side input is
    'row_sparse' or 'csr', then only the values which exist in the left-hand sparse array are computed.
    The 'missing' values are ignored.

    The storage type of ``_scatter_plus_scalar`` output depends on storage types of inputs

    - _scatter_plus_scalar(row_sparse, scalar) = row_sparse
    - _scatter_plus_scalar(csr, scalar) = csr
    - otherwise, ``_scatter_plus_scalar`` behaves exactly like _plus_scalar and generates output
    with default storage



    Parameters
    ----------
    data : Symbol
        source input
    scalar : float
        scalar input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _scatter_set_nd(data=None, indices=None, shape=_Null, name=None, attr=None, out=None, **kwargs):
    r"""This operator has the same functionality as scatter_nd
    except that it does not reset the elements not indexed by the input
    index `NDArray` in the input data `NDArray`.

    .. note:: This operator is for internal use only.

    Examples::

      data = [2, 3, 0]
      indices = [[1, 1, 0], [0, 1, 0]]
      out = [[1, 1], [1, 1]]
      scatter_nd(data=data, indices=indices, out=out)
      out = [[0, 1], [2, 3]]



    Parameters
    ----------
    data : Symbol
        data
    indices : Symbol
        indices
    shape : Shape(tuple), required
        Shape of output.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _set_value(src=_Null, name=None, attr=None, out=None, **kwargs):
    r"""

    Parameters
    ----------
    src : real_t
        Source input to the function.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _slice_assign(lhs=None, rhs=None, begin=_Null, end=_Null, step=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Assign the rhs to a cropped subset of lhs.

    Requirements
    ------------
    - output should be explicitly given and be the same as lhs.
    - lhs and rhs are of the same data type, and on the same device.


    From:/home/jyy/hotspot/mxnet/src/operator/tensor/matrix_op.cc:319

    Parameters
    ----------
    lhs : Symbol
        Source input
    rhs : Symbol
        value to assign
    begin : Shape(tuple), required
        starting indices for the slice operation, supports negative indices.
    end : Shape(tuple), required
        ending indices for the slice operation, supports negative indices.
    step : Shape(tuple), optional, default=[]
        step for the slice operation, supports negative values.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _slice_assign_scalar(data=None, scalar=_Null, begin=_Null, end=_Null, step=_Null, name=None, attr=None, out=None, **kwargs):
    r"""(Assign the scalar to a cropped subset of the input.

    Requirements
    ------------
    - output should be explicitly given and be the same as input
    )

    From:/home/jyy/hotspot/mxnet/src/operator/tensor/matrix_op.cc:344

    Parameters
    ----------
    data : Symbol
        Source input
    scalar : float, optional, default=0
        The scalar value for assignment.
    begin : Shape(tuple), required
        starting indices for the slice operation, supports negative indices.
    end : Shape(tuple), required
        ending indices for the slice operation, supports negative indices.
    step : Shape(tuple), optional, default=[]
        step for the slice operation, supports negative values.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _square_sum(data=None, axis=_Null, keepdims=_Null, exclude=_Null, name=None, attr=None, out=None, **kwargs):
    r"""Computes the square sum of array elements over a given axis
    for row-sparse matrix. This is a temporary solution for fusing ops square and
    sum together for row-sparse matrix to save memory for storing gradients.
    It will become deprecated once the functionality of fusing operators is finished
    in the future.

    Example::

      dns = mx.nd.array([[0, 0], [1, 2], [0, 0], [3, 4], [0, 0]])
      rsp = dns.tostype('row_sparse')
      sum = mx.nd._internal._square_sum(rsp, axis=1)
      sum = [0, 5, 0, 25, 0]


    Defined in /home/jyy/hotspot/mxnet/src/operator/tensor/square_sum.cc:L41

    Parameters
    ----------
    data : Symbol
        The input
    axis : Shape(tuple), optional, default=[]
        The axis or axes along which to perform the reduction.

          The default, `axis=()`, will compute over all elements into a
          scalar array with shape `(1,)`.

          If `axis` is int, a reduction is performed on a particular axis.

          If `axis` is a tuple of ints, a reduction is performed on all the axes
          specified in the tuple.

          If `exclude` is true, reduction will be performed on the axes that are
          NOT in axis instead.

          Negative values means indexing from right to left.
    keepdims : boolean, optional, default=0
        If this is set to `True`, the reduced axes are left in the result as dimension with size one.
    exclude : boolean, optional, default=0
        Whether to perform reduction on axis that are NOT in axis instead.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _sub(lhs=None, rhs=None, name=None, attr=None, out=None, **kwargs):
    r"""Subtracts arguments element-wise.

    The storage type of ``elemwise_sub`` output depends on storage types of inputs

       - elemwise_sub(row_sparse, row_sparse) = row_sparse
       - elemwise_sub(csr, csr) = csr
       - otherwise, ``elemwise_sub`` generates output with default storage



    Parameters
    ----------
    lhs : Symbol
        first input
    rhs : Symbol
        second input

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

def _zeros(shape=_Null, ctx=_Null, dtype=_Null, name=None, attr=None, out=None, **kwargs):
    r"""fill target with zeros

    Parameters
    ----------
    shape : Shape(tuple), optional, default=[]
        The shape of the output
    ctx : string, optional, default=''
        Context of output, in format [cpu|gpu|cpu_pinned](n).Only used for imperative calls.
    dtype : {'float16', 'float32', 'float64', 'int32', 'uint8'},optional, default='float32'
        Target data type.

    name : string, optional.
        Name of the resulting symbol.

    Returns
    -------
    Symbol
        The result symbol.
    """
    return (0,)

__all__ = ['_CachedOp', '_CrossDeviceCopy', '_CustomFunction', '_Div', '_DivScalar', '_Equal', '_EqualScalar', '_Greater', '_GreaterEqualScalar', '_GreaterScalar', '_Greater_Equal', '_Hypot', '_HypotScalar', '_Lesser', '_LesserEqualScalar', '_LesserScalar', '_Lesser_Equal', '_Maximum', '_MaximumScalar', '_Minimum', '_MinimumScalar', '_Minus', '_MinusScalar', '_Mod', '_ModScalar', '_Mul', '_MulScalar', '_NDArray', '_Native', '_NoGradient', '_NotEqualScalar', '_Not_Equal', '_Plus', '_PlusScalar', '_Power', '_PowerScalar', '_RDivScalar', '_RMinusScalar', '_RModScalar', '_RPowerScalar', '_add', '_arange', '_backward_Activation', '_backward_BatchNorm', '_backward_BatchNorm_v1', '_backward_BilinearSampler', '_backward_CachedOp', '_backward_Concat', '_backward_Convolution', '_backward_Convolution_v1', '_backward_Correlation', '_backward_Crop', '_backward_CuDNNBatchNorm', '_backward_Custom', '_backward_CustomFunction', '_backward_Deconvolution', '_backward_Dropout', '_backward_Embedding', '_backward_FullyConnected', '_backward_GridGenerator', '_backward_IdentityAttachKLSparseReg', '_backward_InstanceNorm', '_backward_L2Normalization', '_backward_LRN', '_backward_LeakyReLU', '_backward_LinearRegressionOutput', '_backward_LogisticRegressionOutput', '_backward_MAERegressionOutput', '_backward_MakeLoss', '_backward_Pad', '_backward_Pooling', '_backward_Pooling_v1', '_backward_QActivation', '_backward_QConvolution', '_backward_QConvolution_v1', '_backward_QFullyConnected', '_backward_RNN', '_backward_ROIPooling', '_backward_SVMOutput', '_backward_SequenceLast', '_backward_SequenceMask', '_backward_SequenceReverse', '_backward_SliceChannel', '_backward_Softmax', '_backward_SoftmaxActivation', '_backward_SoftmaxOutput', '_backward_SparseEmbedding', '_backward_SpatialTransformer', '_backward_SwapAxis', '_backward_UpSampling', '_backward__CrossDeviceCopy', '_backward__NDArray', '_backward__Native', '_backward__contrib_CTCLoss', '_backward__contrib_DeformableConvolution', '_backward__contrib_DeformablePSROIPooling', '_backward__contrib_MultiBoxDetection', '_backward__contrib_MultiBoxPrior', '_backward__contrib_MultiBoxTarget', '_backward__contrib_MultiProposal', '_backward__contrib_PSROIPooling', '_backward__contrib_Proposal', '_backward__contrib_count_sketch', '_backward__contrib_fft', '_backward__contrib_ifft', '_backward_abs', '_backward_add', '_backward_arccos', '_backward_arccosh', '_backward_arcsin', '_backward_arcsinh', '_backward_arctan', '_backward_arctanh', '_backward_batch_dot', '_backward_broadcast_add', '_backward_broadcast_div', '_backward_broadcast_hypot', '_backward_broadcast_maximum', '_backward_broadcast_minimum', '_backward_broadcast_mod', '_backward_broadcast_mul', '_backward_broadcast_power', '_backward_broadcast_sub', '_backward_cast', '_backward_cbrt', '_backward_clip', '_backward_copy', '_backward_cos', '_backward_cosh', '_backward_degrees', '_backward_div', '_backward_div_scalar', '_backward_dot', '_backward_expm1', '_backward_gamma', '_backward_gammaln', '_backward_hypot', '_backward_hypot_scalar', '_backward_linalg_gelqf', '_backward_linalg_gemm', '_backward_linalg_gemm2', '_backward_linalg_potrf', '_backward_linalg_potri', '_backward_linalg_sumlogdiag', '_backward_linalg_syevd', '_backward_linalg_syrk', '_backward_linalg_trmm', '_backward_linalg_trsm', '_backward_log', '_backward_log10', '_backward_log1p', '_backward_log2', '_backward_log_softmax', '_backward_max', '_backward_maximum', '_backward_maximum_scalar', '_backward_mean', '_backward_min', '_backward_minimum', '_backward_minimum_scalar', '_backward_mod', '_backward_mod_scalar', '_backward_mul', '_backward_mul_scalar', '_backward_nanprod', '_backward_nansum', '_backward_pick', '_backward_power', '_backward_power_scalar', '_backward_prod', '_backward_radians', '_backward_rcbrt', '_backward_rdiv_scalar', '_backward_reciprocal', '_backward_relu', '_backward_repeat', '_backward_reverse', '_backward_rmod_scalar', '_backward_rpower_scalar', '_backward_rsqrt', '_backward_sample_multinomial', '_backward_sigmoid', '_backward_sign', '_backward_sin', '_backward_sinh', '_backward_slice', '_backward_slice_axis', '_backward_smooth_l1', '_backward_softmax', '_backward_softmax_cross_entropy', '_backward_sparse_retain', '_backward_sqrt', '_backward_square', '_backward_square_sum', '_backward_stack', '_backward_sub', '_backward_sum', '_backward_take', '_backward_tan', '_backward_tanh', '_backward_tile', '_backward_topk', '_backward_where', '_broadcast_backward', '_copy', '_copyto', '_crop_assign', '_crop_assign_scalar', '_cvcopyMakeBorder', '_cvimdecode', '_cvimread', '_cvimresize', '_div', '_div_scalar', '_equal', '_equal_scalar', '_full', '_grad_add', '_greater', '_greater_equal', '_greater_equal_scalar', '_greater_scalar', '_hypot', '_hypot_scalar', '_identity_with_attr_like_rhs', '_imdecode', '_lesser', '_lesser_equal', '_lesser_equal_scalar', '_lesser_scalar', '_maximum', '_maximum_scalar', '_minimum', '_minimum_scalar', '_minus', '_minus_scalar', '_mod', '_mod_scalar', '_mul', '_mul_scalar', '_not_equal', '_not_equal_scalar', '_onehot_encode', '_ones', '_plus', '_plus_scalar', '_power', '_power_scalar', '_random_exponential', '_random_gamma', '_random_generalized_negative_binomial', '_random_negative_binomial', '_random_normal', '_random_poisson', '_random_uniform', '_rdiv_scalar', '_rminus_scalar', '_rmod_scalar', '_rpower_scalar', '_sample_exponential', '_sample_gamma', '_sample_generalized_negative_binomial', '_sample_multinomial', '_sample_negative_binomial', '_sample_normal', '_sample_poisson', '_sample_uniform', '_scatter_elemwise_div', '_scatter_minus_scalar', '_scatter_plus_scalar', '_scatter_set_nd', '_set_value', '_slice_assign', '_slice_assign_scalar', '_square_sum', '_sub', '_zeros']