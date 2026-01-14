"""
Utilities/Statistics.py

This script provides functions:
- Calculates various statistic quantities (rms, mean, median...) for a group of values
- Split data into bins
- Compute statistic quantities for binned data  

Usage:
    See definition of the functions:
        rms(x)
        weighted_rms(x, weights)
        weighted_mean(x, weights)
        median(x)
        Q84Q16(x)
        weighted_variance(x, weights)
        SplitInBins(data, x, weight, bins=20)
        ComputeStats(x, y, weight, bins=20)
    
Author: Yao Yao
Date: 2026-01-14
"""


import os
import numpy as np
from matplotlib import pyplot as plt
import mplhep as hep
import hist
from hist import Hist
import math

def rms(x):
    return np.sqrt(np.mean(x**2))


def weighted_rms(x, weights):
    total_weight = np.sum(weights)
    if total_weight == 0:
        return 0.0
    return np.sqrt(np.average(x**2, weights=weights))


def weighted_mean(x, weights):
    total_weight = np.sum(weights)
    if total_weight == 0:
        return 0.0
    return np.average(x, weights=weights)


def median(x):
    sorted_x = np.sort(x)
    p50 = np.percentile(sorted_x, 50)
    return p50


def Q84Q16(x):
    sorted_x = np.sort(x)
    q84 = np.percentile(sorted_x, 84)  # 84th percentile
    q16 = np.percentile(sorted_x, 16)  # 16th percentile
    return (q84-q16)


def weighted_variance(x, weights):
    total_weight = np.sum(weights)
    if total_weight == 0:
        return 0.0
    average = np.average(x, weights=weights)
    variance = np.average((x-average)**2, weights=weights)
    return variance


def SplitInBins(data, x, weight, bins=20):
    
    '''
        split bins based on `x`. 
        `data` has the same length as `x`.
        `bins` can be an integer or bin_edges (list)
            if `bins` is an integer, it will be an even split with respect to the min/max of the `x`.
        return a dict that key is the bin_midpoint and value is the data points in the bin
    '''
    min_value = np.amin(x)
    max_value = np.amax(x)

    if isinstance(bins, int):
        min_value = np.amin(x)
        max_value = np.amax(x)
        bins = np.linspace(float(math.floor(min_value)), float(math.ceil(max_value)), bins)
    
    bin_midpoints = (bins[:-1] + bins[1:]) / 2

    binned_data = {}
    for index, midpoint in enumerate(bin_midpoints):
        binned_data[midpoint] = {}
        bin_mask = ((x >= bins[index]) & (x < bins[index+1]))
        binned_data[midpoint]['data'] = data[bin_mask]
        binned_data[midpoint]['weight'] = weight[bin_mask]
        
    return binned_data, bins


def ComputeStats(x, y, weight, bins=20):

    '''
        `x` is the gen, and it is the one that is binned and fits are made in each bin
        `y` can be the residual = reco - gen, or can be the percentage: (reco-gen) /gen
    
        Return a dictionary that statistic quantities are calculated for each bin  
    '''

    result = {
        'bins': [],
        'q84q16': [],
        'mean': [],
        'median':[],
        'rms': [],
        'variance': [],
    }

    # split the data into bins
    binned_residuals, bins = SplitInBins(y, x, weight, bins=bins)

    # for each gen_ttbar mass bin, bin_name in binned_residuals.keys():
    for (bin_name, data_dict) in binned_residuals.items():
        data = data_dict['data']
        weight = data_dict['weight']

        if data.shape[0] < 5:
            result['bins'].append(bin_name)
            result['q84q16'].append(0)
            result['mean'].append(0)
            result['median'].append(0)
            result['variance'].append(0)
            result['rms'].append(0)
            continue
        result['bins'].append(bin_name)
        result['q84q16'].append(Q84Q16(data))
        result['mean'].append(weighted_mean(data, weight))
        result['median'].append(median(data))
        result['variance'].append(weighted_variance(data, weight))
        result['rms'].append(weighted_rms(data, weight))

    for key in result:
        result[key] = np.array(result[key])
    return result