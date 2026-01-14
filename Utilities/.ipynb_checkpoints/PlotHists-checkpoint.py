"""
Utilities/PlotHists.py

This script:
- Defines plot_TopReco_Hists function
    - Plots 1D distributions for target and all top reco methods on the same plot
    - Plots 2D distributions for each reco method with respect to target.

Usage:
    from Utilities.PlotHists import plot_TopReco_Hists
    See definition of functions

Author: Yao Yao
Date: 2026-01-14
"""

import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np
import os
import seaborn as sns

from matplotlib.colors import LogNorm
from Utilities.Labels import AXIS_LABELS, LEGEND_LABELS
from Utilities.Hist import hist_1D, hist_2D


def plot_TopReco_Hists(target_array_list, 
                       method_array_list, 
                       method_label_list,
                       xmin, 
                       xmax, 
                       nbins,
                       xlabel='',
                       xticks=None,
                       xticks_label=None,
                       save_folder="./",
                       era='2017',
                       name_addition='',
                       weights=None,
                      ):

    '''
    It plots 1D distribution and 2D distributions that compare target with all methods in CMS style.
    Input: a list of numpy array of target value for each method,
           a list of numpy arrays of prediced value for each method,
           a list of labels for each method,
           xlabel: title for x_axis,
           xmin,
           xmax,
           nbins,
           save_folder: path to store output plots
           year: '2016preVFP', '2016postVFP', '2017', '2018'
           
    '''

    """
    Plots 1D distribution and 2D distributions that compare target with all methods in CMS style.

    Parameters
    ----------
    target_array_list : list of np.ndarray
        Each array contains target values for each method.  
    method_array_list : list of np.ndarray
        Each array contains prediction values for each method.
    method_label_list: list of str
        Each str is the label for the top reco method.
    xmin: float
        The x axis minimum value for the plot.
    xmax: float
        The x axis maximum value for the plot.
    nbins: int
        Number of bins on x axis.
    xlabel: str, optional, default: ''
        Title for x axis.
    xticks : list or np.ndarray, optional, default: None
        If specified, x axis ticks will be set as specified.
    xticks_label : list of str, optional, default: None 
        If specified, x axis ticks' label will be set as specified.
    save_folder : str, optional, default: '.'
        The path to the directory where the plot will be saved.
    era : str, optional, default: '2017'
        The experiment era. Example: "2016 preAPV", "2016 postAPV", "2017", "2018".
    name_addition : str, optional, default: ''
        Additional string added to the file name of the plot.
    weights : np.ndarray or dict of {str: np.ndarray}, optional, default: None
        Weights for each event. Use a np.ndarray when all histograms have 
        the same number of events and share the same weights.

    Returns
    -------
    None
        The function saves the plots in the specified `save_folder`.
    """
    
    # Set bin edges
    bin_edges = np.linspace(xmin, xmax, num=nbins+1)

    ################ Plot ################
    # Plot 1D distributions
    fill_hist_dict = {
        "Target": target_array_list[0], # only plot one target array shape
    }
    
    nofill_hist_dict = {}
    for i in range(len(method_label_list)):
        nofill_hist_dict[method_label_list[i]] = method_array_list[i]
                
    hist_1D(fill_hist_dict, 
            nofill_hist_dict, 
            xlabel=xlabel,
            xticks=xticks,
            xticks_label=xticks_label,
            bin_edges=bin_edges,
            density=True,
            save_folder=save_folder,
            era=era,
            name_addition=name_addition,
            weights=weights,
            ufof=True, # underflow and overflow
           )

    # Plot 2D distributions for each top reco method
    for i, method_label in enumerate(method_label_list):
        hist_2D(target_array_list[i], 
                method_array_list[i], 
                xlabel=f'Gen {xlabel}', 
                ylabel=f'{method_label} {xlabel}', 
                x_bin_edges=bin_edges, 
                y_bin_edges=bin_edges, 
                log=True,
                diag=True,
                density=False,
                save_folder=save_folder,
                era=era,
                name_addition=f"_{method_label}{name_addition}",
                weights=weights[method_label],
               )