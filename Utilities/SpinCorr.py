"""
Utilities/SpinCorr.py

This script:
- Defines functions to calculate spin-correlation variables

Usage:
    from Utilities.SpinCorr import get_spincorr_vars

Author: Yao Yao
Date: 2026-01-14
"""

import numpy as np
import vector

def get_spincorr_vars(tops, tbars, ls, lbars):

    """
    Calculate spincorr variables.

    Parameters
    ----------
    tops : Momentum4D array
        Example: vector.array({"pt" : pt, "eta": eta, "phi": phi, "mass": mass})
    tbars : Momentum4D array
        Example: vector.array({"pt" : pt, "eta": eta, "phi": phi, "mass": mass})
    ls : Momentum4D array
        Example: vector.array({"pt" : pt, "eta": eta, "phi": phi, "mass": mass})
    lbars : Momentum4D array
        Example: vector.array({"pt" : pt, "eta": eta, "phi": phi, "mass": mass})

    Returns
    -------
    ttbar_spincorr_vars: dict{'spincorr_var': np.ndarray} 
        It returns a dictionary of spincorr variables.
        Accessible variables include: 'b1k', 'b1r', 'b1n', 'b2k', 'b2r', 'b2n'
        'c_kk', 'c_kr', 'c_kn', ... 
        'll_cHel', 'c_hel', 'c_han'
    """    
    
    ttbar_frame = tops + tbars
    boosted_tops = tops.boostCM_of(ttbar_frame)
    boosted_tbars = tbars.boostCM_of(ttbar_frame)
    
    boosted_ls = ls.boostCM_of(ttbar_frame)
    boosted_ls = boosted_ls.boostCM_of(boosted_tbars)
    
    boosted_lbars = lbars.boostCM_of(ttbar_frame)
    boosted_lbars = boosted_lbars.boostCM_of(boosted_tops)
    
    p_axis = vector.obj(x=0, y=0, z=1) # proton axis = +1z
    k_axis = boosted_tops.to_xyz().unit() # k-axis is defined by ttbar system
    scattering_angle = k_axis.theta # theta is the angle betwen k_axis and z
    sin_scat_angle = np.sin(scattering_angle)
    #print(sin_scat_angle)
    sin_scat_angle = np.where(np.abs(sin_scat_angle) < 1e-9, 1e-9, sin_scat_angle) # replace values near zero with +/- 1e-5
    axis_coeff = np.sign(np.cos(scattering_angle)) / np.abs(sin_scat_angle)
    
    r_axis = axis_coeff * (p_axis - (k_axis * np.cos(scattering_angle)))
    n_axis = axis_coeff * p_axis.cross(k_axis)
    
    ttbar_spincorr_vars = {}
    
    ttbar_spincorr_vars['ll_cHel'] = np.cos(boosted_lbars.deltaangle(boosted_ls))
    
    ttbar_spincorr_vars['b1k'] = np.cos(boosted_lbars.deltaangle(k_axis))
    ttbar_spincorr_vars['b1r'] = np.cos(boosted_lbars.deltaangle(r_axis))
    ttbar_spincorr_vars['b1n'] = np.cos(boosted_lbars.deltaangle(n_axis))
    ttbar_spincorr_vars['b2k'] = np.cos(boosted_ls.deltaangle(-1 * k_axis))
    ttbar_spincorr_vars['b2r'] = np.cos(boosted_ls.deltaangle(-1 * r_axis))
    ttbar_spincorr_vars['b2n'] = np.cos(boosted_ls.deltaangle(-1 * n_axis))
    
    ttbar_spincorr_vars['c_kk'] = ttbar_spincorr_vars['b1k'] * ttbar_spincorr_vars['b2k']
    ttbar_spincorr_vars['c_rr'] = ttbar_spincorr_vars['b1r'] * ttbar_spincorr_vars['b2r']
    ttbar_spincorr_vars['c_nn'] = ttbar_spincorr_vars['b1n'] * ttbar_spincorr_vars['b2n']
    ttbar_spincorr_vars['c_rk'] = ttbar_spincorr_vars['b1r'] * ttbar_spincorr_vars['b2k']
    ttbar_spincorr_vars['c_kn'] = ttbar_spincorr_vars['b1k'] * ttbar_spincorr_vars['b2n']
    ttbar_spincorr_vars['c_nr'] = ttbar_spincorr_vars['b1n'] * ttbar_spincorr_vars['b2r']
    ttbar_spincorr_vars['c_kr'] = ttbar_spincorr_vars['b1k'] * ttbar_spincorr_vars['b2r']
    ttbar_spincorr_vars['c_rn'] = ttbar_spincorr_vars['b1r'] * ttbar_spincorr_vars['b2n']
    ttbar_spincorr_vars['c_nk'] = ttbar_spincorr_vars['b1n'] * ttbar_spincorr_vars['b2k']

    ttbar_spincorr_vars['c_han'] = ttbar_spincorr_vars['c_kk'] - ttbar_spincorr_vars['c_rr'] - ttbar_spincorr_vars['c_nn']
    ttbar_spincorr_vars['c_hel'] = -ttbar_spincorr_vars['c_kk'] - ttbar_spincorr_vars['c_rr'] - ttbar_spincorr_vars['c_nn']
    return ttbar_spincorr_vars