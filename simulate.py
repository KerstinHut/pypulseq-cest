"""
simulate.py
    Script to run the C++ SimPulseqSBB simulation based on the defined parameters.
    You need to define the files containing sample and experimental parameters, as well as the sequence file.
"""
from pySimPulseqSBB import SimPulseqSBB
from sim.parse_params import parse_params
from sim.utils.utils import get_zspec
from bmctool.set_params import load_params
from bmctool.utils.eval import plot_z


# set the necessary filepaths

sim_config = 'library/config_example.yaml'
seq_file = 'library/seq_example.seq'

# load the parameters
sp = load_params(sim_config)
# parse for C++ handling
sim_params = parse_params(sp=sp, seq_file=seq_file)
# run the simulation
SimPulseqSBB(sim_params, seq_file)

# retrieve the calculated magnetization
m_out = sim_params.GetFinalMagnetizationVectors()
offsets, mz = get_zspec(m_out=m_out, sp=sp, seq_file=seq_file)

# plot
plot_z(mz=mz, offsets=offsets, plot_mtr_asym=True)
