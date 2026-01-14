"""
Utilities/Hist.py

This script:
- Defines hist_1D function
    - Plot and save 1D histogram in CMS Style.
    - Plots multiple 1D distributions on the same canvas without stacking. 
    - Both color-filled style and no-filled style are available.
    - Options include weighted events, 
                      event filter, 
                      density, 
                      log scale in y axis, 
                      underflow and overflow bins, 
                      specify x-axis ticks and label. 
- Defines hist_2D function
    - Plot and save 2D histogram in CMS Style.
    - Options include weighted events,
                      density,
                      log scale in heat map.

Usage:
    from Utilities.Hist import hist_1D
    from Utilities.Hist import hist_2D
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
from typing import Union, Optional 
from Utilities.Labels import AXIS_LABELS, LEGEND_LABELS


def hist_1D(fill_hists: dict[str, np.ndarray], 
            nofill_hists: dict[str, np.ndarray],
            xlabel: str, 
            bin_edges: np.ndarray,
            save_folder: Optional[str] = ".",
            era: Optional[str] = "2017",
            name_addition: Optional[str] = "",
            weights: Optional[Union[np.ndarray, dict[str, np.ndarray]]] = None,
            density: Optional[bool] = True,
            log: Optional[bool]=False,
            ufof: Optional[bool]=True,
            xticks: Optional[Union[list, np.ndarray]] = None,
            xticks_label: Optional[list[str]] = None,
           ) -> None:
    
    """
    Plot and save a 1D histogram in CMS Style for multiple physics processes .

    Parameters
    ----------
    fill_hists : dict of {str: np.ndarray}
        A dictionary of histograms that will be plotted with filled color.
        Example: {"label", numpy_1D_array}.
    nofill_hists : dict of {str: np.ndarray}
        A dictionary of histograms that will be plotted without filled color.
        Example: {"label", numpy_1D_array}.
    xlabel : str
        The x-axis label.
    bin_edges : np.ndarray
        The bin edges of the x-axis.
    save_folder : str, optional, default: '.'
        The path to the directory where the plot will be saved.
    era : str, optional, default: '2017'
        The experiment era. Example: "2016 preAPV", "2016 postAPV", "2017", "2018".
    name_addition : str, optional, default: ''
        Additional string added to the file name of the plot.
    weights : np.ndarray or dict of {str: np.ndarray}, optional, default: None
        Weights for each event. Use a np.ndarray when all histograms have 
        the same number of events and share the same weights.
    density : bool, optional, default: True
        If True, the histogram will be normalized to form a probability density.
    log : bool, optional, default: False
        If True, the y-axis will be in logarithmic scale.
    ufof : bool, optional, default: True
        If True, underflow and overflow bins will be plotted
    xticks : list or np.ndarray, optional, default: None
        If specified, x axis ticks will be set as specified.
    xticks_label : list of str, optional, default: None 
        If specified, x axis ticks' label will be set as specified.

    Returns
    -------
    None
        The function saves the plot as a PDF in the specified `save_folder`.
    """
    
    # Create a `save_folder` to store plot
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Set up colors for each distribution
    colors = {
        'Target': '#94a4a2', # gray
        'MLP': '#ffa90e', # yellow
        'mlb-weighting': '#bd1f01', # red
        'Transformer': '#3f90da', # blue
        # Specify colors for other distributions
        # A few available colors:               
        # '#832db6' # deep purple
        # '#a96b59' # clay brown
        # '#e76300' # orange
        # '#b9ac70' # yellow-green
        # '#717581' # blue-gray
        # '#92dadd' # soft cyan
    }
    
    # Set plot CMS tdr style
    plt.style.use(hep.style.CMS)

    ################ Plot ################
    # Create `weights` dictionary
    # 1) if `weights` is None, assign 1 as weight for each event, and form a numpy 1D array.
    # 2) if `weights` is a numpy 1D array (which includes the scenario 1), 
    #    assign each process the same weights, and form a dictionary.

    if weights is None:
        first_hist = list(fill_hists.values())[0]
        weights = np.ones(first_hist.shape)
    if isinstance(weights, np.ndarray):
        _weights_tmp = weights
        weights = {}
        merged_hists = dict(fill_hists, **nofill_hists)
        for key in merged_hists.keys():
            weights[key] = _weights_tmp

    # Identify center-of-mass energy from `era`
    com = 0
    if "2016" in era or "2017" in era or "2018" in era: 
        com = 13
    elif "2022" in era or "2023" in era or "2024" in era:
        com = 13.6
    else:
        print("Error: not Run 2 or Run 3 era")
        return
        
    # Set canvas
    fig, ax = plt.subplots(1, 1, figsize=(8, 7))
    hep.cms.label(label='Preliminary', data=False, year=era, com=com, loc=1, ax=ax)
    
    # Scientific notation on y axis
    ax.ticklabel_format(style="sci", axis='y', scilimits=(-2, 2), useMathText=True)

    # For underflow/overflow event, manually replace its value with 
    # `uf_value_replace`/`of_value_replace`.
    uf_value_replace = bin_edges[0] + (bin_edges[1] - bin_edges[0])/2
    of_value_replace = bin_edges[-1] - (bin_edges[-1] - bin_edges[-2])/2

    # Define max_height for leaving space for legends
    max_height = -999

    # Plot filled histograms
    # key is the distribution's label: "Target", "MLP".
    for index, (key, value) in enumerate(fill_hists.items()):
        value_tmp = value.copy()
        if ufof: # replace value for uf/of
            value_tmp[value_tmp < bin_edges[0]] = uf_value_replace
            value_tmp[value_tmp > bin_edges[-1]] = of_value_replace
        counts, _, _ = ax.hist(value_tmp, 
                               weights=weights[key],
                               bins=bin_edges, 
                               #alpha=0.5, # transparency, not recommended unless necessary
                               edgecolor=colors[key], 
                               label=LEGEND_LABELS.get(key,key), 
                               color=colors[key], 
                               density=density, 
                               log=log)
        if counts.max() > max_height:
            max_height = counts.max()
            
    # Plot no-fill histograms
    for index, (key, value) in enumerate(nofill_hists.items()):
        value_tmp = value.copy()
        if ufof:
            value_tmp[value_tmp < bin_edges[0]] = uf_value_replace
            value_tmp[value_tmp > bin_edges[-1]] = of_value_replace
        # plot without marker
        counts, _, _ = ax.hist(value_tmp,
                               weights=weights[key],
                               bins=bin_edges, 
                               histtype='step', 
                               edgecolor=colors[key], 
                               lw=1.5, 
                               facecolor="none", 
                               label=LEGEND_LABELS.get(key,key), 
                               density=density, 
                               log=log)
        
        if counts.max() > max_height:
            max_height = counts.max()

    # Set legend
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 0.9), ncol=2, fontsize=24, markerscale=2.5)
    # Set x axis
    ax.set_xlim(bin_edges[0], bin_edges[-1])    
    ax.set_xlabel(AXIS_LABELS.get(xlabel, xlabel), fontsize=28)
    if xticks is not None:
        ax.set_xticks(xticks)
    if xticks_label is not None:
        ax.set_xticklabels(xticks_label)
    ax.tick_params(axis='both', labelsize=24)
    ax.xaxis.set_tick_params(pad=10)
    # Set y axis
    ax.set_ylabel('Density' if density else 'Entries', fontsize=28)
    ax.set_ylim(top=1.55 * max_height)

    # Save plot
    plt.savefig(f'{save_folder}/{xlabel}{name_addition}.pdf', bbox_inches="tight")
    plt.close()


def hist_2D(x: np.ndarray, 
            y: np.ndarray, 
            xlabel: list, 
            ylabel: list,
            x_bin_edges: Union[list, np.ndarray], 
            y_bin_edges: Union[list, np.ndarray], 
            log: Optional[bool]=True,
            diag: Optional[bool]=False,
            density: Optional[bool]=True,
            save_folder: Optional[str]=".",
            era: Optional[str]='2017',
            name_addition: Optional[str]="",
            weights: Optional[np.ndarray]=None,
           ):
    """
    Plot and save a 2D histogram in CMS Style.

    Parameters
    ----------
    x : np.ndarray
        An array of x value of each event. 
    y : np.ndarray
        An array of y value of each event.
    xlabel : str
        The x-axis label. If xlabel has corresponding raw string defined in Labels.py, 
        it uses the raw string. Otherwise the xlabel will be placed under x-axis. 
    ylabel : str
        The y-axis label. If ylabel has corresponding raw string defined in Labels.py, 
        it uses the raw string. Otherwise the ylabel will be placed under y-axis.
    x_bin_edges : list or numbers or np.ndarray
        The bin edges of the x-axis.
    y_bin_edges : list or numbers or np.ndarray
        The bin edges of the y-axis.
    save_folder : str, optional, default: '.'
        The path to the directory where the plot will be saved.
    era : str, optional, default: '2017'
        The experiment era. Example: "2016 preAPV", "2016 postAPV", "2017", "2018".
    name_addition : str, optional, default: ''
        Additional string added to the file name of the plot.
    weights : np.ndarray or dict of {str: np.ndarray}, optional, default: None
        Weights for each event. Specify this when all histograms share the same weights.
    density : bool, optional, default: True
        If True, the histogram will be normalized to form a probability density.
    log : bool, optional, default: False
        If True, the y-axis will be in logarithmic scale.
    diag : bool, optional, default: False
        If True, the histogram will have a red diagnal line. 

    Returns
    -------
    None
        The function saves the plot as a PDF in the specified `save_folder`.
    """
    
    # Create a `save_folder` to store plot
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Set plot CMS tdr style
    plt.style.use(hep.style.CMS)

    # Process weights
    if weights is not None:
        weights = weights / np.sum(weights)
    else:
        weights = np.ones(x.shape)

    # Identify center-of-mass energy from `era`
    com = 0
    if "2016" in era or "2017" in era or "2018" in era: 
        com = 13
    elif "2022" in era or "2023" in era or "2024" in era:
        com = 13.6
    else:
        print("Error: not Run 2 or Run 3 era")
        return

    
    # Create heat map
    extent = [x_bin_edges[0], x_bin_edges[-1], y_bin_edges[0], y_bin_edges[-1]]
    bin_range = x_bin_edges[-1] - x_bin_edges[0]
    fig, ax = plt.subplots(1, 1, figsize=(12, 9))
    heatmap, xedges, yedges = np.histogram2d(x, y, bins=[x_bin_edges, y_bin_edges], 
                                             density=density, 
                                             weights=weights)
    if log:
        im = ax.imshow(heatmap.T, extent=extent, origin='lower', 
                       aspect='auto', norm=LogNorm(), cmap='viridis')
    else:
        im = ax.imshow(heatmap.T, extent=extent, origin='lower', 
                       aspect='auto', cmap='viridis')
    fig.colorbar(im, ax=ax)
    
    hep.cms.label(label='Preliminary', data=False, year=era, com=com, loc=0, ax=ax)

    # Set x axis
    xlabel_tot = xlabel.split()
    xlabel_tot = [AXIS_LABELS.get(x, x) for x in xlabel_tot]
    xlabel_tot = ' '.join(xlabel_tot) # like "Target ttbar_pt" "Transformer ttbar_pt"
    ax.set_xlabel(xlabel_tot)

    # Set y axis
    ylabel_tot = ylabel.split()
    ylabel_tot = [AXIS_LABELS.get(y, y) for y in ylabel_tot]
    ylabel_tot = ' '.join(ylabel_tot)
    ax.set_ylabel(ylabel_tot)

    # Add diagonal line 
    if diag:
        diagline_x = np.array([x_bin_edges[0], x_bin_edges[-1]])
        diagline_y = np.array([y_bin_edges[0], y_bin_edges[-1]])
        ax.plot(diagline_x, diagline_y, color='red')

    # Save plot, replace space with underscore for the file name. 
    xlabel = xlabel.replace(' ', '_')
    ylabel = ylabel.replace(' ', '_')
    plt.savefig(f"{save_folder}/{ylabel}_vs_{xlabel}{name_addition}.pdf", bbox_inches="tight")
    plt.close()
