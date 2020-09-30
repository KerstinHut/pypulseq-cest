from SimPulseqSBB import SimulationParameters, WaterPool, MTPool, CESTPool
from params import Params
from SimPulseqSBB import Lorentzian, SuperLorentzian, NoLineshape


def parse_sp(sp: Params, seq_file: str):
    # sp = Params()
    sp_sim = SimulationParameters()
    # init magnetization vector
    num_adc_events = get_num_adc_events(seq_file)
    sp_sim.InitMagnetizationVectors(sp.m_vec, num_adc_events)
    # constructwater pool
    water_pool = WaterPool(sp.water_pool['r1'], sp.water_pool['r2'], sp.water_pool['f'])
    sp_sim.SetWaterPool(water_pool)
    if sp.mt_pool:
        lineshape = set_lineshape(sp.mt_pool['lineshape'])
        mt_pool = MTPool(sp.mt_pool['r1'], sp.mt_pool['r2'], sp.mt_pool['f'], sp.mt_pool['dw'], sp.mt_pool['k'], lineshape)
        sp_sim.SetMTPool(mt_pool)
    for i in range(len(sp.cest_pools)):
        cest_pool = CESTPool(sp.cest_pools[i]['r1'], sp.cest_pools[i]['r2'], sp.cest_pools[i]['f'], sp.cest_pools[i]['dw'], sp.cest_pools[i]['k'])
        sp_sim.SetCESTPool(cest_pool, i)
    sp_sim.InitScanner(sp.scanner['b0'], sp.scanner['rel_b1'], sp.scanner['gamma'], sp.scanner['b0_inhomogeneity'])
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


def get_num_adc_events(seq_file):
    with open(seq_file) as search:
        num_lines = 0
        while True:
            num_lines += 1
            line = search.readline()
            if 'offsets_ppm' in line:
                offsets = line.replace('offsets_ppm', '').strip().split()
                break
            if num_lines == 20:
                print('Could not read offsets from seq-file.')
    num_adc_events = len(offsets)
    return num_adc_events
