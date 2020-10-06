from SimPulseqSBB import SimulationParameters, WaterPool, MTPool, CESTPool
from sim_pulseq_sbb.params import Params
from SimPulseqSBB import Lorentzian, SuperLorentzian, NoLineshape
from pypulseq.Sequence.sequence import Sequence


def parse_sp(sp: Params, seq_file: str):
    # sp = Params()
    sp_sim = SimulationParameters()
    # init magnetization vector
    num_adc_events = get_num_adc_events(seq_file) +1
    sp_sim.InitMagnetizationVectors(sp.m_vec, num_adc_events)
    # constructwater pool
    water_pool = WaterPool(sp.water_pool['r1'], sp.water_pool['r2'], sp.water_pool['f'])
    sp_sim.SetWaterPool(water_pool)
    if sp.mt_pool:
        lineshape = set_lineshape(sp.mt_pool['lineshape'])
        mt_pool = MTPool(sp.mt_pool['r1'], sp.mt_pool['r2'], sp.mt_pool['f'], sp.mt_pool['dw'], sp.mt_pool['k'], lineshape)
        sp_sim.SetMTPool(mt_pool)
    sp_sim.InitCESTPoolMemory(len(sp.cest_pools))
    for i in range(len(sp.cest_pools)):
        cest_pool = CESTPool(sp.cest_pools[i]['r1'], sp.cest_pools[i]['r2'], sp.cest_pools[i]['f'], sp.cest_pools[i]['dw'], sp.cest_pools[i]['k'])
        sp_sim.SetCESTPool(cest_pool, i)
    sp_sim.InitScanner(sp.scanner['b0'], sp.scanner['rel_b1'], sp.scanner['b0_inhomogeneity'], sp.scanner['gamma'])
    if 'verbose' in sp.options.keys():
        sp_sim.SetVerbose(sp.options['verbose'])
    if 'reset_init_mag' in sp.options.keys():
        sp_sim.SetUseInitMagnetization(sp.options['reset_init_mag'])
    if 'max_pulse_samples' in sp.options.keys():
        sp_sim.SetMaxNumberOfPulseSamples(sp.options['max_pulse_samples'])
    return sp_sim


def set_lineshape(ls):
    try:
        if ls == 'Lorentzian':
            return Lorentzian
        elif ls == 'SuperLorentzian':
            return SuperLorentzian
        elif not ls:
            return NoLineshape
    except ValueError:
        print(ls + ' is not a valid lineshape for MT Pool.')


def get_offsets(seq_file):
    seq = Sequence(version=1.3)
    seq.read(seq_file)
    try:
        offsets = list(seq.definitions['offsets_ppm'])
    except ValueError:
        print('Could not read offsets from seq-file.')
    # with open(seq_file) as search:
    #     num_lines = 0
    #     while True:
    #         num_lines += 1
    #         line = search.readline()
    #         if 'offsets_ppm' in line:
    #             o = line.replace('offsets_ppm', '').strip().split()
    #             offsets = [float(x) for x in o]
    #             break
    #         if num_lines == 20:
    #             print('Could not read offsets from seq-file.')
    return offsets


def get_num_adc_events(seq_file):
    offsets = get_offsets(seq_file)
    num_adc_events = len(offsets)
    return num_adc_events


def check_m0(seq_file):
    seq = Sequence(version=1.3)
    seq.read(seq_file)
    if 1 in seq.definitions['run_m0_scan'] or 'True' in seq.definitions['run_m0_scan']:
        return True
    else:
        return False




