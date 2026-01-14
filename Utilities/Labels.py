"""
Utilities/Labels.py

This script:
- Defines Axis labels for plots
- Defines Legend labels for some methods

Usage:
    from Utilities.Labels import AXIS_LABELS
    from Utilities.Labels import LEGEND_LABELS

    label_b1k = AXIS_LABELS['b1k']
    label_mlb = LEGEND_LABELS['mlb-weighting']
    
Author: Yao Yao
Date: 2026-01-14
"""

AXIS_LABELS = {
    # Spin correlation variables
    'll_cHel': r"$\cos \varphi$",
    'b1k': r"$\cos \theta_1^k$",
    'b2k': r"$\cos \theta_2^k$",
    'b1n': r"$\cos \theta_1^n$",
    'b2n': r"$\cos \theta_2^n$",
    'b1r': r"$\cos \theta_1^r$",
    'b2r': r"$\cos \theta_2^r$",
    'c_kk': r"$\cos \theta_1^k \: \cos \theta_2^k$",
    'c_rr': r"$\cos \theta_1^r \: \cos \theta_2^r$",
    'c_nn': r"$\cos \theta_1^n \: \cos \theta_2^n$",
    'c_rk': r"$\cos \theta_1^r \: \cos \theta_2^k$",
    'c_kr': r"$\cos \theta_1^k \: \cos \theta_2^r$",
    'c_nr': r"$\cos \theta_1^n \: \cos \theta_2^r$",
    'c_rn': r"$\cos \theta_1^r \: \cos \theta_2^n$",
    'c_nk': r"$\cos \theta_1^n \: \cos \theta_2^k$",
    'c_kn': r"$\cos \theta_1^k \: \cos \theta_2^n$",
    'c_hel': r"$c_{hel}$",
    'c_han': r"$c_{han}$",
    'llbar_delta_eta': r"$| \Delta \eta_{\ell \bar{\ell}} |$",
    'llbar_delta_phi': r"$| \Delta \phi_{\ell \bar{\ell}} |$",

    # ttbar
    'ttbar_p': r"$p (t \bar{t})$ [GeV]",
    'ttbar_pt': r"$p_T (t \bar{t})$ [GeV]",
    'ttbar_eta': r"$\eta (t \bar{t})$",
    'ttbar_phi': r"$\phi (t \bar{t})$",
    'ttbar_mass': r"$m (t \bar{t})$ [GeV]",
    'ttbar_energy': r"$E (t \bar{t})$ [GeV]",
    'ttbar_px': r"$p_x (t \bar{t})$ [GeV]",
    'ttbar_py': r"$p_y (t \bar{t})$ [GeV]",
    'ttbar_pz': r"$p_z (t \bar{t})$ [GeV]",
    'ttbar_delta_eta': r"$\Delta \eta (t \bar{t})$",
    'ttbar_delta_phi': r"$\Delta \phi (t \bar{t})$",
    'ttbar_delta_r': r"$\Delta R (t \bar{t})$",
    'gen_ttbar_mass': r"Gen $m (t \bar{t})$ [GeV]",

    # t 
    't_p': r"$p (t)$ [GeV]",
    't_px': r"$p_x (t)$ [GeV]",
    't_py': r"$p_y (t)$ [GeV]",
    't_pz': r"$p_z (t)$ [GeV]",
    't_pt': r"$p_T (t)$ [GeV]",
    't_phi': r"$\phi (t)$",
    't_eta': r"$\eta (t)$",
    't_mass': r"$m (t)$ [GeV]",
    't_energy': r"$E (t)$ [GeV]",
    # tbar
    'tbar_p': r"$p (\bar{t})$ [GeV]",
    'tbar_px': r"$p_x (\bar{t})$ [GeV]",
    'tbar_py': r"$p_y (\bar{t})$ [GeV]",
    'tbar_pz': r"$p_z (\bar{t})$ [GeV]",
    'tbar_pt': r"$p_T (\bar{t})$ [GeV]",
    'tbar_phi': r"$\phi (\bar{t})$",
    'tbar_eta': r"$\eta (\bar{t})$",
    'tbar_mass': r"$m (\bar{t})$ [GeV]",
    'tbar_energy': r"$E (\bar{t})$ [GeV]",

    # boosted_top 
    'boosted_t': r"$p^{t boosted}$ [GeV]",
    'boosted_t_px': r"$p_x^{t boosted}$ [GeV]",
    'boosted_t_py': r"$p_y^{t boosted}$ [GeV]",
    'boosted_t_pz': r"$p_z^{t boosted}$ [GeV]",
    'boosted_t_pt': r"$p_T^{t boosted}$ [GeV]",
    'boosted_t_phi': r"$\phi^{t boosted}$",
    'boosted_t_eta': r"$\eta^{t boosted}$",
    'boosted_t_mass': r"$m^{t boosted}$ [GeV]",
    'boosted_t_energy': r"$E^{t boosted}$ [GeV]",

    # boosted_tbar
    'boosted_tbar': r"$p^{\bar{t} boosted}$ [GeV]",
    'boosted_tbar_px': r"$p_x^{\bar{t} boosted}$ [GeV]",
    'boosted_tbar_py': r"$p_y^{\bar{t} boosted}$ [GeV]",
    'boosted_tbar_pz': r"$p_z^{\bar{t} boosted}$ [GeV]",
    'boosted_tbar_pt': r"$p_T^{\bar{t} boosted}$ [GeV]",
    'boosted_tbar_phi': r"$\phi^{\bar{t} boosted}$",
    'boosted_tbar_eta': r"$\eta^{\bar{t} boosted}$",
    'boosted_tbar_mass': r"$m^{\bar{t} boosted}$ [GeV]",
    'boosted_tbar_energy': r"$E^{\bar{t} boosted}$ [GeV]",

    # nu
    'nu_pt': r"$p_T^{\nu}$ [GeV]",
    'nu_eta': r"$\eta^{\nu}$",
    'nu_phi': r"$\phi^{\nu}$",
    'nu_mass': r"$m^{\nu}$ [GeV]",
    # nubar
    'nubar_pt': r"$p_T^{\bar{\nu}}$ [GeV]",
    'nubar_eta': r"$\eta^{\bar{\nu}}$",
    'nubar_phi': r"$\phi^{\bar{\nu}}$",
    'nubar_mass': r"$m^{\bar{\nu}}$ [GeV]",
    # nu and nubar
    'nunubar_delta_eta': r"$| \Delta \eta_{\nu \bar{\nu}} |$",
    'nunubar_delta_phi': r"$| \Delta \phi_{\nu \bar{\nu}} |$",
    'nunubar_delta_eta_signed': r"$\Delta \eta_{\nu \bar{\nu}}$",
    'nunubar_delta_phi_signed': r"$\Delta \phi_{\nu \bar{\nu}}$",
    # l and b
    'l_pt': r"$p_T^{\ell}$ [GeV]",
    'lbar_pt': r"$p_T^{\bar{\ell}}$ [GeV]",
    'b_pt': r"$p_T^{b}$ [GeV]",
    'bbar_pt': r"$p_T^{\bar{b}}$ [GeV]",
    'b_energy': r"$E^{b}$ [GeV]",
    'bbar_energy': r"$E^{\bar{b}}$ [GeV]",

    # others
    'resolution': r"Resolution [GeV]",
    'bias': r"Bias [GeV]",
}

LEGEND_LABELS = {
    'mlb-weighting': r"$m_{lb}$-weighting",
}
