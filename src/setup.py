#!/usr/bin/env python
"""
setup.py file from src_old
"""

from distutils.core import setup, Extension
import numpy

try:
    numpy_include = numpy.get_include()
except AttributeError:
    numpy_include = numpy.get_numpy_include()

eigen_include = '3rdParty/Eigen'

SimPulseqSBB_module = Extension('_SimPulseqSBB', sources=['SimPulseqSBB_wrap.cxx', 'SimPulseqSBB.cpp',
                                                          'SimulationParameters.cpp', 'ExternalSequence.cpp'],
                                include_dirs=[numpy_include, numpy_include + '/numpy', eigen_include],
                                language="c++",
                                )

ExternalSequence_module = Extension('_SimPulseqSBB', sources=['ExternalSequence_wrap.cxx', 'ExternalSequence.cpp'],
                               language="c++",
                              )



setup(name='SimPulseqSBB',
      version='0.1',
      author="K Heinecke",
      description="SimPulseqSBB",
      ext_modules=[SimPulseqSBB_module, ExternalSequence_module],
      py_modules=["SimPulseqSBB", "ExternalSequence"],
      )
