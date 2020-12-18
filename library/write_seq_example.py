"""
Script to output a seq file for test purposes.
parameter settings:
     pulse shape = block
     B1 = 1 uT
     n = 10
     t_p = 100 ms
     t_d = 10 ms
     T_rec = 2/12 s (saturated/M0)
"""

import numpy as np

from pypulseq.Sequence.sequence import Sequence
from pypulseq.make_adc import make_adc
from pypulseq.make_delay import make_delay
from pypulseq.make_trap_pulse import make_trapezoid
from pypulseq.make_block_pulse import make_block_pulse
from pypulseq.opts import Opts
from sim.utils.seq.conversion import convert_seq_12_to_pseudo_13

seq = Sequence()

offset_range = 10  # [ppm]
num_offsets = 51  # 100  # number of measurements (not including M0)
run_m0_scan = True  # if you want an M0 scan at the beginning
t_rec = 3  # recovery time between scans [s]
m0_t_rec = 12  # recovery time before m0 scan [s]
sat_b1 = 2  # mean sat pulse b1 [uT]
t_p = 100e-3  # sat pulse duration [s]
t_d = 10e-3  # delay between pulses [s]
n_pulses = 10  # number of sat pulses per measurement
b0 = 7  # B0 [T]
spoiling = 1  # 0=no spoiling, 1=before readout, Gradient in x,y,z

seq_filename = 'seq_example.seq'  # filename

# scanner limits
sys = Opts(max_grad=40, grad_unit='mT/m', max_slew=130, slew_unit='T/m/s', rf_ringdown_time=30e-6, rf_dead_time=100e-6,
           rf_raster_time=1e-6)
gamma = sys.gamma * 1e-6

# scanner events
# sat pulse
flip_angle_sat = sat_b1 * gamma * 2 * np.pi * t_p  # rad
rf_sat, _ = make_block_pulse(flip_angle=flip_angle_sat, duration=t_p, system=sys, time_bw_product=3)

# spoilers
spoil_amp = 0.8 * sys.max_grad  # Hz/m
spoil_dur = 4.5e-3  # 4.5 ms
rise_time = 1.0e-6  # 1.0 ms
gx_spoil, gy_spoil, gz_spoil = [make_trapezoid(channel=c, system=sys, amplitude=spoil_amp, duration=spoil_dur,
                                               rise_time=rise_time) for c in ['x', 'y', 'z']]

# pseudo adc (not played out)
pseudo_adc = make_adc(num_samples=1, duration=1e-3)

# loop through z spectrum offsets
offsets_ppm = np.linspace(-offset_range, offset_range, num_offsets)
offsets = offsets_ppm * gamma * b0

if run_m0_scan:
    seq.add_block(make_delay(m0_t_rec))
    seq.add_block(pseudo_adc)

# loop through offsets and set pulses and delays
for offset in offsets:
    # take care of phase accumulation during off-res pulse
    accum_phase = 0
    seq.add_block(make_delay(t_rec))  # recovery time
    rf_sat.freq_offset = offset
    for n in range(n_pulses):
        rf_sat.phase_offset = accum_phase
        seq.add_block(rf_sat)
        accum_phase = np.mod(accum_phase + offset * 2 * np.pi * np.where(np.abs(rf_sat.signal) > 0)[0].size * 1e-6, 2 * np.pi)
        if n < n_pulses-1:
            seq.add_block(make_delay(t_d))
    print(np.where(offsets == offset)[0][0], '/', len(offsets), ': offset ', offset)
    if spoiling:
        seq.add_block(gx_spoil, gy_spoil, gz_spoil)
    seq.add_block(pseudo_adc)

seq.set_definition('offsets_ppm', offsets_ppm)
seq.set_definition('run_m0_scan', str(run_m0_scan))

# plot the sequence
# seq.plot()

# print shape library
print(seq.shape_library)

# write seq file
seq.write(seq_filename)

# convert to pseudo version 1.3
convert_seq_12_to_pseudo_13(seq_filename)