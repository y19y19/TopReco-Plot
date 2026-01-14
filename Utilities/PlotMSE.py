"""
Utilities/PlotMSE.py

This script provides functions:
- plot RMSE and bias in CMS style

Usage:
    See definition of the function:
        plot_MSE
    
Author: Yao Yao
Date: 2026-01-14
"""


import matplotlib.pyplot as plt
import mplhep as hep
import numpy as np
import os
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.colors import to_rgba
from Utilities.Labels import AXIS_LABELS, LEGEND_LABELS


def plot_MSE(bias_array_list, 
                 rmse_array_list, 
                 method_label_list,
                 bin_edges,
                 xlabel='',
                 ylabel='',
                 ymax=None,
                 save_folder="./",
                 era='2017',
                 name_addition='',
                 legend_loc=0,
                 ):

    '''
        It plots RMSE, bias and |bias| for all methods on the same plot.
        Input: a list of numpy arrays of each method's bias
               a list of numpy arrays of each method's rmse,
               a list of labels for each method,
               xlabel: title for x_axis,
               ylabel: title for y_axis,
               ymax: Manually set y axis upper limit
               save_folder: path to store output plots
               era: '2016preVFP', '2016postVFP', '2017', '2018' 
           
    '''
    # set up dict of bias and rmse with each method
    bias_hist_dict = {}
    for i in range(len(method_label_list)):
        bias_hist_dict[method_label_list[i]] = bias_array_list[i]
    rmse_hist_dict = {}
    for i in range(len(method_label_list)):
        rmse_hist_dict[method_label_list[i]] = rmse_array_list[i]

    # create a save_folder to store plots
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Set up colors for each distribution
    colors = {
        'MLP': '#ffa90e', # yellow
        'mlb-weighting': '#bd1f01', # red
        'Transformer': '#3f90da', # blue
        'mlb-weighting fail': '#bd1f01',
        'mlb-weighting succeed': '#3f90da',
        # Specify colors for other distributions
        # A few available colors:               
        # '#832db6' # deep purple
        # '#a96b59' # clay brown
        # '#e76300' # orange
        # '#b9ac70' # yellow-green
        # '#717581' # blue-gray
        # '#92dadd' # soft cyan
    }

    # Identify center-of-mass energy from `era`
    com = 0
    if "2016" in era or "2017" in era or "2018" in era: 
        com = 13
    elif "2022" in era or "2023" in era or "2024" in era:
        com = 13.6
    else:
        print("Error: not Run 2 or Run 3 era")
        return
        
    # Set plot CMS tdr style
    plt.style.use(hep.style.CMS)

    ################ Plot ################

    # Set up canvas
    fig, ax = plt.subplots(1, 1, figsize=(9, 7))
    hep.cms.label(label='Preliminary', data=False, year=era, com=com, loc=0, ax=ax, fontsize=22) 

    max_height = -999
    min_height = 999

    bin_centers = []
    bin_widths = []

    # |biases|
    for index, (key, weight) in enumerate(bias_hist_dict.items()): 
        value = (bin_edges[1:] + bin_edges[:-1])/2
        bin_centers = value
        bin_widths = bin_edges[1:] - bin_edges[:-1]
        value = value[weight<0]
        weight = weight[weight<0]
        
        counts, _, patches = ax.hist(value,
                               bins=bin_edges, 
                               weights=np.abs(weight), # absolute value of bias
                               histtype='step',
                               edgecolor=colors[key],
                               lw=2,
                               label=LEGEND_LABELS.get(key,key), 
                               linestyle='--',
                               color=colors[key])

    # line at y = 0
    plt.axhline(y=0, color='black', linestyle='-', linewidth=3.0) 
    
    # biases
    for index, (key, weight) in enumerate(bias_hist_dict.items()): 
        value = (bin_edges[1:] + bin_edges[:-1])/2
        bin_centers = value
        bin_widths = bin_edges[1:] - bin_edges[:-1]
        plt.plot(value, 
                 weight, 
                 marker='^', markersize=4, 
                 color=colors[key], 
                 linestyle='None', 
                 label=LEGEND_LABELS.get(key,key))
        if weight.min() < min_height:
            min_height = weight.min()
        
    # RMSE
    for index, (key, weight) in enumerate(rmse_hist_dict.items()):
        value = (bin_edges[1:] + bin_edges[:-1])/2
        counts, _, patches = ax.hist(value,
                               bins=bin_edges, 
                               weights=weight,
                               histtype='step', 
                               edgecolor=colors[key], 
                               lw=2.5,
                               facecolor="none", 
                               label=LEGEND_LABELS.get(key,key))
        if counts.max() > max_height:
            max_height = counts.max()

    ################## Customize Legend ####################
    # Create legend entries
    custom_line_rmse = Line2D([0], [0], color='black', linestyle='-', 
                              label='RMSE')
    custom_line_bias = Line2D([0], [0], marker='^', color='black', markerfacecolor='black',
                              markeredgecolor='black', markersize=9, linestyle='None', 
                              label='Bias')
    custom_line_absbias = Line2D([0], [0], color='black', linestyle='--', 
                                 label='|Bias|')
    custom_patch_blank = Patch(facecolor='none', edgecolor='none', 
                               label='')
    custom_patch_tf_only = Patch(facecolor='none', edgecolor='none', 
                                 label='Transformer reconstruction')

    custom_patch_mlp = Patch(facecolor='#ffa90e', alpha = 0.7, edgecolor='#ffa90e', 
                             label='MLP')
    custom_patch_mlb = Patch(facecolor='#bd1f01', alpha = 0.7, edgecolor='#bd1f01', 
                             label=LEGEND_LABELS.get('mlb-weighting','mlb-weighting'))
    custom_patch_tf = Patch(facecolor='#3f90da', alpha = 0.7, edgecolor='#3f90da', 
                            label='Transformer')

    custom_patch_tf_mlb_fail = Patch(facecolor='#bd1f01', alpha = 0.7, edgecolor='#bd1f01', 
                                     label='mlb-weighting fail')
    custom_patch_tf_mlb_succeed = Patch(facecolor='#3f90da', alpha = 0.7, edgecolor='#3f90da', 
                                        label='mlb-weighting succeed')

    # Assemble legends
    legend_fontsize=24
    if legend_loc == 0: # for results when mlb-weighting, mlp and transformer exist, for note publication
        ax.legend(handles=[custom_line_rmse, custom_line_bias, custom_line_absbias, 
                           custom_patch_mlb, custom_patch_tf, custom_patch_mlp], 
                  loc='upper right', ncol=2,  fontsize=legend_fontsize, columnspacing=0.5) 
    elif legend_loc == 1: # special for pz, insert a empty column in the middle, for note publication
        ax.legend(handles=[custom_patch_mlb, custom_patch_tf, custom_patch_mlp, 
                           custom_patch_blank, custom_patch_blank, custom_patch_blank, 
                           custom_line_rmse, custom_line_bias, custom_line_absbias], 
                  loc='upper left', ncol=3, fontsize=legend_fontsize, columnspacing=1.5, bbox_to_anchor=(-0.02, 1.02))
    elif legend_loc == 2: # for 2016 events fail mlb-weighting method, for note publication
        ax.legend(handles=[custom_line_rmse, custom_line_bias, custom_line_absbias, 
                           custom_patch_tf_mlb_fail, custom_patch_tf_mlb_succeed], 
                  loc='upper center', ncol=2,  fontsize=legend_fontsize, columnspacing=1.0, bbox_to_anchor=(0.5, 1.02))
        ax.text(0.5, 0.68, "Transformer Reconstruction", transform=ax.transAxes, fontsize=legend_fontsize, 
                ha='center', va='top', bbox=dict(facecolor='none', edgecolor='none'))
    elif legend_loc == 3: # for results when only transformer results exist, temporary for Run 3
        ax.legend(handles=[custom_line_rmse, custom_patch_tf, 
                           custom_line_bias, custom_patch_blank, 
                           custom_line_absbias, custom_patch_blank], 
                  loc='upper center', ncol=3, fontsize=legend_fontsize, columnspacing=1.0, bbox_to_anchor=(0.5, 1.02))
    elif legend_loc == 4: # for results when only mlb-weighting and transformer exist, for Run 2
        ax.legend(handles=[custom_line_rmse, custom_line_bias, custom_line_absbias, 
                           custom_patch_mlb, custom_patch_tf], 
                  loc='upper right', ncol=2, fontsize=legend_fontsize, columnspacing=0.5) 

    # Set x axis
    ax.set_xlim(bin_edges[0], bin_edges[-1])
    xlabel_tot = xlabel.split()
    xlabel_tot = [AXIS_LABELS.get(x, x) for x in xlabel_tot]
    xlabel_tot = ' '.join(xlabel_tot)
    ax.set_xlabel(xlabel_tot, fontsize=30)
    ax.tick_params(axis='both', labelsize=28)
    ax.xaxis.set_tick_params(pad=10)

    # Set y axis
    ax.set_ylabel(ylabel, fontsize=30)
    ax.set_ylim(top=1.9 * max_height)
    if legend_loc == 1:
        ax.set_ylim(top=1.75*max_height)
    if ymax is not None:
        ax.set_ylim(top=ymax)
    ax.set_ylim(bottom=1.2 * min_height)

    # Save plot
    xlabel = xlabel.replace(' ', '_')
    plt.savefig(f'{save_folder}/{xlabel}{name_addition}.pdf', bbox_inches="tight")

    plt.close()