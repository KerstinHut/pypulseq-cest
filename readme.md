# Simulation tool and seq-file preparation for CEST saturation blocks

## Sequence design in open file format for MR sequences
This repository contains the necessary code and tools to build CEST saturation blocks with [pypulseq](https://github.com/imr-framework/pypulseq)
which in itself is a python adaption of the matlab-based [pulseq](https://github.com/pulseq/pulseq). The documentation
of the open file format for MR sequences can be found [here](https://pulseq.github.io/specification.pdf).

An example script and sequences can be found in the [example](example) subfolder. Please find further remarks in that subfolders [readme](./example/readme.md)
Since pypulseq is producing files of the version 1.2, we provide a function to create a pseudo 1.3 file and one to load files of either of these versions in the [seq_util submodule](seq_util).
You can use the following to change the 1.2 file into a pseudo 1.3 version:
````python
from seq_util.conversion import convert_seq_12_to_pseudo_13
convert_seq_12_to_pseudo_13(file_path)
````

To load any sequence file of version 1.2 or 1.3, use:
````python
from seq_util.read import read_any_version
seq = read_any_version(file_path)
````


## Simulation of CEST sequences
The goal of this repository is to enable the simulation for CEST spectra in python. Therefore, we provide a python implementation of the C++ based simulation tool [pulseq-cest-sim](https://github.com/kherz/pulseq-cest/tree/master/pulseq-cest-sim)
by Kai Herz, which was originally made available for use in MATLAB. The installation of the python package is necessary 
(see section *Installation* below). You can simulate your own Z-Spectra by defining your parameters similar to the template files for [experimental (scanner etc.) parameters](param_configs/experimental_params.yaml) and [parameters regarding the sample](param_configs/sample_params.yaml).
We also provide config files to set parameters for an exemplary standard simulation and to simulate the WASABI approach. 
You can then run the simulation with the [simulate](simulate.py) script.
 
Parameter handling and evaluation tools are defined in the [sim_pulseq_sbb](sim) folder. The package code and C++ source code can be found in the [src](sim/src) subfolder.

## Installation
Please refer to the [readme](sim/src/readme.md) in [sim_pulseq_sbb/src](sim/src) for 
installation of the necessary python module.

## Prerequisites
Other package prerequisites are:
- numpy
- matplotlib
- yaml