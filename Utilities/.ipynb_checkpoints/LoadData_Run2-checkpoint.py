"""
Utilities/LoadData_Run2.py

This script:
- Load generator-level top quark kinematics and mlb-weighting reconstruction result from Juan Duarte's root files, 
- Load Transformer inference result from Ethan Colbert's root files
- Process all the dataset with listed era. 

Usage:
    Process root files and save only the variables that are necessary for evaluating model performance.
    
Author: Yao Yao
Date: 2026-01-14
"""

import awkward as ak
import math
import numpy as np
import os
import uproot
import vector

from Utilities.SpinCorr import get_spincorr_vars
from Utilities.VecArray import set4DVecPtEtaPhiM, set2DVecPtPhi, convertAwkToNumpy


datasets = {
    '2016preVFP': '/depot/cms/users/jduarteq/2016preVFP/spinCorrInput_2016preVFP_November2024/Nominal',
    '2016postVFP': '/depot/cms/users/jduarteq/2016postVFP/spinCorrInput_2016postVFP_November2024/Nominal',
    '2017': '/depot/cms/users/jduarteq/2017/spinCorrInput_2017_November2024/Nominal',
    '2018': '/depot/cms/users/jduarteq/2018/spinCorrInput_2018_November2024/Nominal',
}

tf_results = {
    '2016preVFP': '/depot/cms/top/colberte/top-reco-framework/studies/Model_v0_0_6/output/2016preVFP/Nominal',
    '2016postVFP': '/depot/cms/top/colberte/top-reco-framework/studies/Model_v0_0_6/output/2016postVFP/Nominal',
    '2018': '/depot/cms/top/colberte/top-reco-framework/studies/Model_v0_0_6/output/2018/Nominal',
}

def getFilterPerFile(path_to_inputFile):
    rootfile = uproot.open(path_to_inputFile)
    tree = rootfile["reconstruction_mask"]
    filter_dilepton = tree["mask"]
    return filter_dilepton

def getTfResultPerFile(path_to_inputFile):
    rootfile = uproot.open(path_to_inputFile)
    tree = rootfile["predictions_step7"]
    tf_top = set4DVecPtEtaPhiM(tree["ml_top_pt"],      
                                tree["ml_top_eta"],      
                                tree["ml_top_phi"],      
                                tree["ml_top_mass"])
    tf_topbar = set4DVecPtEtaPhiM(tree["ml_tbar_pt"],   
                                   tree["ml_tbar_eta"],     
                                   tree["ml_tbar_phi"],     
                                   tree["ml_tbar_mass"])
    weight = tree["eventWeight"].array(library="np")
    
    objs = {"tf_top": tf_top,
            "tf_topbar": tf_topbar,
            "weight" : weight
           }
    
    tf_top_array = np.array((objs["tf_top"].px, objs["tf_topbar"].px,
                      objs["tf_top"].py, objs["tf_topbar"].py,
                      objs["tf_top"].pz, objs["tf_topbar"].pz,
                      objs["tf_top"].E, objs["tf_topbar"].E)).T

    weight_array = np.array((objs["weight"])).T

    return tf_top_array , weight_array    

    
def getObjsPerFile(path_to_inputFile):
    ''' 
    return a dictionary that contains 4D/2D momentum vector numpy array for all the objects that are needed for training/testing. 
    '''

    # Get the tree
    rootfile = uproot.open(path_to_inputFile)
    tree = rootfile["ttBar_treeVariables_step7"]

    mlb_top = set4DVecPtEtaPhiM(tree["top_pt"],      
                                tree["top_eta"],      
                                tree["top_phi"],      
                                tree["top_mass"])
    mlb_topbar = set4DVecPtEtaPhiM(tree["tbar_pt"],   
                                   tree["tbar_eta"],     
                                   tree["tbar_phi"],     
                                   tree["tbar_mass"])
    gen_top = set4DVecPtEtaPhiM(tree["gen_top_pt"],  
                                tree["gen_top_eta"],  
                                tree["gen_top_phi"],  
                                tree["gen_top_mass"])
    gen_topbar = set4DVecPtEtaPhiM(tree["gen_tbar_pt"],
                                   tree["gen_tbar_eta"], 
                                   tree["gen_tbar_phi"], 
                                   tree["gen_tbar_mass"])

    weight = tree["eventWeight"].array(library="np")
    mlb_filter = (tree["top_pt"].array(library="np") > -1)
    # Return a dictionary
    objs = {"mlb_top" : mlb_top,
            "mlb_topbar" : mlb_topbar,
            "gen_top" : gen_top,
            "gen_topbar" : gen_topbar,
            "weight" : weight,
            "mlb_filter" : mlb_filter,
           }

    gen_top_array = np.array((objs["gen_top"].px, objs["gen_topbar"].px,
                      objs["gen_top"].py, objs["gen_topbar"].py,
                      objs["gen_top"].pz, objs["gen_topbar"].pz,
                      objs["gen_top"].E, objs["gen_topbar"].E)).T
    mlb_top_array = np.array((objs["mlb_top"].px, objs["mlb_topbar"].px,
                         objs["mlb_top"].py, objs["mlb_topbar"].py,
                         objs["mlb_top"].pz, objs["mlb_topbar"].pz,
                         objs["mlb_top"].E, objs["mlb_topbar"].E)).T
    weight_array = np.array((objs["weight"])).T
    mlb_filter_array = np.array((objs["mlb_filter"])).T
    
    return gen_top_array, mlb_top_array, weight_array, mlb_filter_array


def getAllData(process_eras=[], xrootd=False):
    ''' Concatenate the numpy arrays from different channels and eras together.'''
    gen_top_tot = {key: [] for key in process_eras}
    mlb_top_tot = {key: [] for key in process_eras}
    tf_top_tot = {key: [] for key in process_eras}
    weight_tot = {key: [] for key in process_eras}
    filter_dilepton_tot = {key: [] for key in process_eras}
    filter_mlb_tot = {key: [] for key in process_eras}

    channels = ["ee", "emu", "mumu"]
    for era, dir in datasets.items():
        if era not in process_eras:
            continue
        for channel in channels:
            ttbar_files = []
            path_to_dir = f"{dir}/{channel}/"
            path_to_tf = ''
            if era != '2017': # skip 2017 because some of the events are used in training
                path_to_tf = f"{tf_results[era]}/{channel}/"
            files = os.listdir(path_to_dir)
            ttbar_files = [x for x in files if "ttbarsignal" in x and "boundstate" not in x]
            for filename in ttbar_files:
                path_to_file = f"{path_to_dir}/{filename}"
                print(path_to_file)
                gen_top, mlb_top, weight, mlb_filter = getObjsPerFile(path_to_file)
                gen_top_tot[era].append(gen_top)
                mlb_top_tot[era].append(mlb_top)
                weight_tot[era].append(weight)
                filter_mlb_tot[era].append(mlb_filter)
                if era != '2017':
                    path_to_tffile = f"{path_to_tf}/{filename}"
                    tf_top, _ = getTfResultPerFile(path_to_tffile)
                    tf_top_tot[era].append(tf_top)
                    filter_dilepton = getFilterPerFile(path_to_tffile)
                    filter_dilepton_tot[era].append(filter_dilepton)
                else:
                    print(len(mlb_top))
                    filter_dilepton_tot[era].append(np.ones(len(mlb_top), dtype=bool))
                
    for era, _list in filter_dilepton_tot.items():
        filter_dilepton_tot[era] = np.concatenate(_list)
    
    for era, _list in gen_top_tot.items():
        _list = np.concatenate(_list)
        gen_top_tot[era] = _list[filter_dilepton_tot[era]]
        
    for era, _list in mlb_top_tot.items():
        _list = np.concatenate(_list)
        mlb_top_tot[era] = _list[filter_dilepton_tot[era]]

    for era, _list in tf_top_tot.items():
        tf_top_tot[era] = np.concatenate(_list)

    for era, _list in weight_tot.items():
        _list = np.concatenate(_list)
        weight_tot[era] = _list[filter_dilepton_tot[era]]

    for era, _list in filter_mlb_tot.items():
        _list = np.concatenate(_list)
        filter_mlb_tot[era] = _list[filter_dilepton_tot[era]]

    return gen_top_tot, mlb_top_tot, tf_top_tot, weight_tot, filter_mlb_tot