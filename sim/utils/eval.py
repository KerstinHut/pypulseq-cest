"""
eval.py
    Tool independent functions for plotting and calculations
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from sim.utils.utils import sim_noise
from sim.params import Params


def calc_mtr_asym(z: np.ndarray) -> np.ndarray:
    """
    calculating MTRasym from the magnetization vector
    :param z: magnetization
    :return: MTRasym
    """
    return np.flip(z) - z


def get_zspec(m_out: np.ndarray,
              sp: Params,
              noise: (bool, tuple) = False) \
        -> np.ndarray:
    """
    returns the Z- spectra and optionally simulates noise
    :param m_out: Output magnetization from the simulation
    :param sp: Params object containing the simulation parameters
    :param noise: bool or tuple, toggle to simulate standard gaussian noise on the spectra or set values (mean, std)
    """
    if np.any(m_out):
        if sp.m0_scan:
            zspec = np.abs(m_out[sp.mz_loc, 1:] / m_out[sp.mz_loc, 0])
        else:
            zspec = np.abs(m_out[sp.mz_loc, :])
        if noise:
            zspec = sim_noise(zspec, set_vals=noise)
    else:
        raise ValueError('No valid M0 defined.')
    return zspec


def plot_z(mz: np.array,
           offsets: np.array = None,
           plot_mtr_asym: bool = False,
           title: str = None) \
        -> Figure:
    """
    initiating calculations and plotting functions
    :param mz: magnetization vector
    :param offsets: offsets to plot the magnetization on
    :param plot_mtr_asym: boolean wether MTRasym should be plotted as well
    :param title: optional title for the plot
    """
    if offsets is None:
        offsets = range(len(mz))

    if title is None:
        title = 'Z-Spec'

    fig, ax1 = plt.subplots()
    ax1.set_ylim([0, 1])
    ax1.set_ylabel('Z', color='b')
    ax1.set_xlabel('Offsets')
    plt.plot(offsets, mz, '.--', label='$Z$', color='b')
    plt.gca().invert_xaxis()
    ax1.tick_params(axis='y', labelcolor='b')

    if plot_mtr_asym:
        mtr_asym = calc_mtr_asym(mz)

        ax2 = ax1.twinx()
        ax2.set_ylim([0, round(np.max(mtr_asym) + 0.01, 2)])
        ax2.set_ylabel('$MTR_{asym}$', color='y')
        ax2.plot(offsets, mtr_asym, label='$MTR_{asym}$', color='y')
        ax2.tick_params(axis='y', labelcolor='y')
        fig.tight_layout()

    plt.title(title)
    plt.show()
    return fig