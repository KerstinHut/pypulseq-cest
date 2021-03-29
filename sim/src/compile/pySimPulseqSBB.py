# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _pySimPulseqSBB
else:
    import _pySimPulseqSBB

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _pySimPulseqSBB.delete_SwigPyIterator

    def value(self):
        return _pySimPulseqSBB.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _pySimPulseqSBB.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _pySimPulseqSBB.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _pySimPulseqSBB.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _pySimPulseqSBB.SwigPyIterator_equal(self, x)

    def copy(self):
        return _pySimPulseqSBB.SwigPyIterator_copy(self)

    def next(self):
        return _pySimPulseqSBB.SwigPyIterator_next(self)

    def __next__(self):
        return _pySimPulseqSBB.SwigPyIterator___next__(self)

    def previous(self):
        return _pySimPulseqSBB.SwigPyIterator_previous(self)

    def advance(self, n):
        return _pySimPulseqSBB.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _pySimPulseqSBB.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _pySimPulseqSBB.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _pySimPulseqSBB.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _pySimPulseqSBB.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _pySimPulseqSBB.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _pySimPulseqSBB.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _pySimPulseqSBB:
_pySimPulseqSBB.SwigPyIterator_swigregister(SwigPyIterator)

class vectorMatrixXd(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _pySimPulseqSBB.vectorMatrixXd_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pySimPulseqSBB.vectorMatrixXd___nonzero__(self)

    def __bool__(self):
        return _pySimPulseqSBB.vectorMatrixXd___bool__(self)

    def __len__(self):
        return _pySimPulseqSBB.vectorMatrixXd___len__(self)

    def __getslice__(self, i, j):
        return _pySimPulseqSBB.vectorMatrixXd___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pySimPulseqSBB.vectorMatrixXd___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pySimPulseqSBB.vectorMatrixXd___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pySimPulseqSBB.vectorMatrixXd___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pySimPulseqSBB.vectorMatrixXd___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pySimPulseqSBB.vectorMatrixXd___setitem__(self, *args)

    def pop(self):
        return _pySimPulseqSBB.vectorMatrixXd_pop(self)

    def append(self, x):
        return _pySimPulseqSBB.vectorMatrixXd_append(self, x)

    def empty(self):
        return _pySimPulseqSBB.vectorMatrixXd_empty(self)

    def size(self):
        return _pySimPulseqSBB.vectorMatrixXd_size(self)

    def swap(self, v):
        return _pySimPulseqSBB.vectorMatrixXd_swap(self, v)

    def begin(self):
        return _pySimPulseqSBB.vectorMatrixXd_begin(self)

    def end(self):
        return _pySimPulseqSBB.vectorMatrixXd_end(self)

    def rbegin(self):
        return _pySimPulseqSBB.vectorMatrixXd_rbegin(self)

    def rend(self):
        return _pySimPulseqSBB.vectorMatrixXd_rend(self)

    def clear(self):
        return _pySimPulseqSBB.vectorMatrixXd_clear(self)

    def get_allocator(self):
        return _pySimPulseqSBB.vectorMatrixXd_get_allocator(self)

    def pop_back(self):
        return _pySimPulseqSBB.vectorMatrixXd_pop_back(self)

    def erase(self, *args):
        return _pySimPulseqSBB.vectorMatrixXd_erase(self, *args)

    def __init__(self, *args):
        _pySimPulseqSBB.vectorMatrixXd_swiginit(self, _pySimPulseqSBB.new_vectorMatrixXd(*args))

    def push_back(self, x):
        return _pySimPulseqSBB.vectorMatrixXd_push_back(self, x)

    def front(self):
        return _pySimPulseqSBB.vectorMatrixXd_front(self)

    def back(self):
        return _pySimPulseqSBB.vectorMatrixXd_back(self)

    def assign(self, n, x):
        return _pySimPulseqSBB.vectorMatrixXd_assign(self, n, x)

    def resize(self, *args):
        return _pySimPulseqSBB.vectorMatrixXd_resize(self, *args)

    def insert(self, *args):
        return _pySimPulseqSBB.vectorMatrixXd_insert(self, *args)

    def reserve(self, n):
        return _pySimPulseqSBB.vectorMatrixXd_reserve(self, n)

    def capacity(self):
        return _pySimPulseqSBB.vectorMatrixXd_capacity(self)
    __swig_destroy__ = _pySimPulseqSBB.delete_vectorMatrixXd

# Register vectorMatrixXd in _pySimPulseqSBB:
_pySimPulseqSBB.vectorMatrixXd_swigregister(vectorMatrixXd)

class vectorVectorXd(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def iterator(self):
        return _pySimPulseqSBB.vectorVectorXd_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _pySimPulseqSBB.vectorVectorXd___nonzero__(self)

    def __bool__(self):
        return _pySimPulseqSBB.vectorVectorXd___bool__(self)

    def __len__(self):
        return _pySimPulseqSBB.vectorVectorXd___len__(self)

    def __getslice__(self, i, j):
        return _pySimPulseqSBB.vectorVectorXd___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _pySimPulseqSBB.vectorVectorXd___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _pySimPulseqSBB.vectorVectorXd___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _pySimPulseqSBB.vectorVectorXd___delitem__(self, *args)

    def __getitem__(self, *args):
        return _pySimPulseqSBB.vectorVectorXd___getitem__(self, *args)

    def __setitem__(self, *args):
        return _pySimPulseqSBB.vectorVectorXd___setitem__(self, *args)

    def pop(self):
        return _pySimPulseqSBB.vectorVectorXd_pop(self)

    def append(self, x):
        return _pySimPulseqSBB.vectorVectorXd_append(self, x)

    def empty(self):
        return _pySimPulseqSBB.vectorVectorXd_empty(self)

    def size(self):
        return _pySimPulseqSBB.vectorVectorXd_size(self)

    def swap(self, v):
        return _pySimPulseqSBB.vectorVectorXd_swap(self, v)

    def begin(self):
        return _pySimPulseqSBB.vectorVectorXd_begin(self)

    def end(self):
        return _pySimPulseqSBB.vectorVectorXd_end(self)

    def rbegin(self):
        return _pySimPulseqSBB.vectorVectorXd_rbegin(self)

    def rend(self):
        return _pySimPulseqSBB.vectorVectorXd_rend(self)

    def clear(self):
        return _pySimPulseqSBB.vectorVectorXd_clear(self)

    def get_allocator(self):
        return _pySimPulseqSBB.vectorVectorXd_get_allocator(self)

    def pop_back(self):
        return _pySimPulseqSBB.vectorVectorXd_pop_back(self)

    def erase(self, *args):
        return _pySimPulseqSBB.vectorVectorXd_erase(self, *args)

    def __init__(self, *args):
        _pySimPulseqSBB.vectorVectorXd_swiginit(self, _pySimPulseqSBB.new_vectorVectorXd(*args))

    def push_back(self, x):
        return _pySimPulseqSBB.vectorVectorXd_push_back(self, x)

    def front(self):
        return _pySimPulseqSBB.vectorVectorXd_front(self)

    def back(self):
        return _pySimPulseqSBB.vectorVectorXd_back(self)

    def assign(self, n, x):
        return _pySimPulseqSBB.vectorVectorXd_assign(self, n, x)

    def resize(self, *args):
        return _pySimPulseqSBB.vectorVectorXd_resize(self, *args)

    def insert(self, *args):
        return _pySimPulseqSBB.vectorVectorXd_insert(self, *args)

    def reserve(self, n):
        return _pySimPulseqSBB.vectorVectorXd_reserve(self, n)

    def capacity(self):
        return _pySimPulseqSBB.vectorVectorXd_capacity(self)
    __swig_destroy__ = _pySimPulseqSBB.delete_vectorVectorXd

# Register vectorVectorXd in _pySimPulseqSBB:
_pySimPulseqSBB.vectorVectorXd_swigregister(vectorVectorXd)

M_PI = _pySimPulseqSBB.M_PI
class Scanner(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    B0 = property(_pySimPulseqSBB.Scanner_B0_get, _pySimPulseqSBB.Scanner_B0_set)
    relB1 = property(_pySimPulseqSBB.Scanner_relB1_get, _pySimPulseqSBB.Scanner_relB1_set)
    B0Inhomogeneity = property(_pySimPulseqSBB.Scanner_B0Inhomogeneity_get, _pySimPulseqSBB.Scanner_B0Inhomogeneity_set)
    Gamma = property(_pySimPulseqSBB.Scanner_Gamma_get, _pySimPulseqSBB.Scanner_Gamma_set)

    def __init__(self):
        _pySimPulseqSBB.Scanner_swiginit(self, _pySimPulseqSBB.new_Scanner())
    __swig_destroy__ = _pySimPulseqSBB.delete_Scanner

# Register Scanner in _pySimPulseqSBB:
_pySimPulseqSBB.Scanner_swigregister(Scanner)

SuperLorentzian = _pySimPulseqSBB.SuperLorentzian
Lorentzian = _pySimPulseqSBB.Lorentzian
NoLineshape = _pySimPulseqSBB.NoLineshape
class WaterPool(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _pySimPulseqSBB.WaterPool_swiginit(self, _pySimPulseqSBB.new_WaterPool(*args))
    __swig_destroy__ = _pySimPulseqSBB.delete_WaterPool

    def GetR1(self):
        return _pySimPulseqSBB.WaterPool_GetR1(self)

    def GetR2(self):
        return _pySimPulseqSBB.WaterPool_GetR2(self)

    def GetFraction(self):
        return _pySimPulseqSBB.WaterPool_GetFraction(self)

    def SetR1(self, nR1):
        return _pySimPulseqSBB.WaterPool_SetR1(self, nR1)

    def SetR2(self, nR2):
        return _pySimPulseqSBB.WaterPool_SetR2(self, nR2)

    def SetFraction(self, nf):
        return _pySimPulseqSBB.WaterPool_SetFraction(self, nf)

# Register WaterPool in _pySimPulseqSBB:
_pySimPulseqSBB.WaterPool_swigregister(WaterPool)

class CESTPool(WaterPool):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _pySimPulseqSBB.CESTPool_swiginit(self, _pySimPulseqSBB.new_CESTPool(*args))
    __swig_destroy__ = _pySimPulseqSBB.delete_CESTPool

    def GetShiftinPPM(self):
        return _pySimPulseqSBB.CESTPool_GetShiftinPPM(self)

    def GetExchangeRateInHz(self):
        return _pySimPulseqSBB.CESTPool_GetExchangeRateInHz(self)

    def SetShiftinPPM(self, ndw):
        return _pySimPulseqSBB.CESTPool_SetShiftinPPM(self, ndw)

    def SetExchangeRateInHz(self, nk):
        return _pySimPulseqSBB.CESTPool_SetExchangeRateInHz(self, nk)

# Register CESTPool in _pySimPulseqSBB:
_pySimPulseqSBB.CESTPool_swigregister(CESTPool)

class MTPool(CESTPool):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _pySimPulseqSBB.MTPool_swiginit(self, _pySimPulseqSBB.new_MTPool(*args))
    __swig_destroy__ = _pySimPulseqSBB.delete_MTPool

    def GetMTLineShape(self):
        return _pySimPulseqSBB.MTPool_GetMTLineShape(self)

    def SetMTLineShape(self, nls):
        return _pySimPulseqSBB.MTPool_SetMTLineShape(self, nls)

    def GetMTLineAtCurrentOffset(self, offset, omega0):
        return _pySimPulseqSBB.MTPool_GetMTLineAtCurrentOffset(self, offset, omega0)

# Register MTPool in _pySimPulseqSBB:
_pySimPulseqSBB.MTPool_swigregister(MTPool)

class SimulationParameters(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _pySimPulseqSBB.SimulationParameters_swiginit(self, _pySimPulseqSBB.new_SimulationParameters())
    __swig_destroy__ = _pySimPulseqSBB.delete_SimulationParameters

    def SetExternalSequence(self, seq):
        return _pySimPulseqSBB.SimulationParameters_SetExternalSequence(self, seq)

    def GetExternalSequence(self):
        return _pySimPulseqSBB.SimulationParameters_GetExternalSequence(self)

    def InitMagnetizationVectors(self, M, numOutput):
        return _pySimPulseqSBB.SimulationParameters_InitMagnetizationVectors(self, M, numOutput)

    def GetMagnetizationVectors(self):
        return _pySimPulseqSBB.SimulationParameters_GetMagnetizationVectors(self)

    def GetFinalMagnetizationVectors(self):
        return _pySimPulseqSBB.SimulationParameters_GetFinalMagnetizationVectors(self)

    def SetWaterPool(self, waterPool):
        return _pySimPulseqSBB.SimulationParameters_SetWaterPool(self, waterPool)

    def GetWaterPool(self):
        return _pySimPulseqSBB.SimulationParameters_GetWaterPool(self)

    def InitCESTPoolMemory(self, numPools):
        return _pySimPulseqSBB.SimulationParameters_InitCESTPoolMemory(self, numPools)

    def SetCESTPool(self, cp, poolIdx):
        return _pySimPulseqSBB.SimulationParameters_SetCESTPool(self, cp, poolIdx)

    def GetCESTPool(self, poolIdx):
        return _pySimPulseqSBB.SimulationParameters_GetCESTPool(self, poolIdx)

    def SetMTPool(self, cp):
        return _pySimPulseqSBB.SimulationParameters_SetMTPool(self, cp)

    def GetMTPool(self):
        return _pySimPulseqSBB.SimulationParameters_GetMTPool(self)

    def InitScanner(self, *args):
        return _pySimPulseqSBB.SimulationParameters_InitScanner(self, *args)

    def GetScannerB0(self):
        return _pySimPulseqSBB.SimulationParameters_GetScannerB0(self)

    def GetScannerRelB1(self):
        return _pySimPulseqSBB.SimulationParameters_GetScannerRelB1(self)

    def GetScannerB0Inhom(self):
        return _pySimPulseqSBB.SimulationParameters_GetScannerB0Inhom(self)

    def GetScannerGamma(self):
        return _pySimPulseqSBB.SimulationParameters_GetScannerGamma(self)

    def IsMTActive(self):
        return _pySimPulseqSBB.SimulationParameters_IsMTActive(self)

    def GetNumberOfCESTPools(self):
        return _pySimPulseqSBB.SimulationParameters_GetNumberOfCESTPools(self)

    def SetVerbose(self, v):
        return _pySimPulseqSBB.SimulationParameters_SetVerbose(self, v)

    def IsVerbose(self):
        return _pySimPulseqSBB.SimulationParameters_IsVerbose(self)

    def SetUseInitMagnetization(self, initMag):
        return _pySimPulseqSBB.SimulationParameters_SetUseInitMagnetization(self, initMag)

    def GetUseInitMagnetization(self):
        return _pySimPulseqSBB.SimulationParameters_GetUseInitMagnetization(self)

    def SetMaxNumberOfPulseSamples(self, numSamples):
        return _pySimPulseqSBB.SimulationParameters_SetMaxNumberOfPulseSamples(self, numSamples)

    def GetMaxNumberOfPulseSamples(self):
        return _pySimPulseqSBB.SimulationParameters_GetMaxNumberOfPulseSamples(self)

# Register SimulationParameters in _pySimPulseqSBB:
_pySimPulseqSBB.SimulationParameters_swigregister(SimulationParameters)


def SimPulseqSBB(sp, seq_filename):
    return _pySimPulseqSBB.SimPulseqSBB(sp, seq_filename)


