import awkward as ak
import math
import numpy as np
import os

import uproot
import vector

from Utilities.SpinCorr import get_spincorr_vars
from Utilities.VecArray import set4DVecPtEtaPhiM, set2DVecPtPhi, convertAwkToNumpy


datasets = {'2022preEE': '/depot/cms/users/jduarteq/2022preEE/spinCorrInput_2022preEE_December2025v2/Nominal',
            '2022postEE': '/depot/cms/users/jduarteq/2022postEE/spinCorrInput_2022postEE_December2025v2/Nominal',
            '2023preBPix': '/depot/cms/users/jduarteq/2023preBPix/spinCorrInput_2023preBPix_December2025v2/Nominal',
            '2023postBPix': '/depot/cms/users/jduarteq/2023postBPix/spinCorrInput_2023postBPix_December2025v2/Nominal'
           }
tf_results = {'2022preEE': '/depot/cms/top/colberte/top-reco-framework/studies/Model_v0_0_6/output/2022preEE/Nominal',
              '2022postEE': '/depot/cms/top/colberte/top-reco-framework/studies/Model_v0_0_6/output/2022postEE/Nominal',
              '2023preBPix': '/depot/cms/top/colberte/top-reco-framework/studies/Model_v0_0_6/output/2023preBPix/Nominal',
              '2023postBPix': '/depot/cms/top/colberte/top-reco-framework/studies/Model_v0_0_6/output/2023postBPix/Nominal'
             }

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

    '''
    # mlb reconstruction is not there yet
    mlb_top = set4DVecPtEtaPhiM(tree["top_pt"],      
                                tree["top_eta"],      
                                tree["top_phi"],      
                                tree["top_mass"])
    mlb_topbar = set4DVecPtEtaPhiM(tree["tbar_pt"],   
                                   tree["tbar_eta"],     
                                   tree["tbar_phi"],     
                                   tree["tbar_mass"])
    '''
    gen_t_pt = np.concatenate((tree["gen_top_pt"].array(library="np")))
    gen_t_eta = np.concatenate((tree["gen_top_eta"].array(library="np")))
    gen_t_phi = np.concatenate((tree["gen_top_phi"].array(library="np")))
    gen_t_mass = np.concatenate((tree["gen_top_mass"].array(library="np")))

    gen_tbar_pt = tree["gen_tbar_pt"].array(library="np")
    gen_tbar_eta = tree["gen_tbar_eta"].array(library="np")
    gen_tbar_phi = tree["gen_tbar_phi"].array(library="np")
    gen_tbar_mass = tree["gen_tbar_mass"].array(library="np")

    '''
    gen_top = set4DVecPtEtaPhiM(tree["gen_top_pt"],  
                                tree["gen_top_eta"],  
                                tree["gen_top_phi"],  
                                tree["gen_top_mass"])
    gen_topbar = set4DVecPtEtaPhiM(tree["gen_tbar_pt"],
                                   tree["gen_tbar_eta"], 
                                   tree["gen_tbar_phi"], 
                                   tree["gen_tbar_mass"])
    '''
    gen_t = set4DVecPtEtaPhiM(gen_t_pt,  
                                gen_t_eta,  
                                gen_t_phi,  
                                gen_t_mass)
    gen_tbar = set4DVecPtEtaPhiM(gen_tbar_pt,
                                 gen_tbar_eta, 
                                 gen_tbar_phi, 
                                 gen_tbar_mass)
    
    weight = tree["eventWeight"].array(library="np")
    # mlb_filter = (tree["top_pt"].array(library="np") > -1)
    # Return a dictionary
    objs = {#"mlb_top" : mlb_top,
            #"mlb_topbar" : mlb_topbar,
            "gen_t" : gen_t,
            "gen_tbar" : gen_tbar,
            "weight" : weight,
            #"mlb_filter" : mlb_filter,
           }

    gen_t_array = np.array((objs["gen_t"].px, objs["gen_tbar"].px,
                      objs["gen_t"].py, objs["gen_tbar"].py,
                      objs["gen_t"].pz, objs["gen_tbar"].pz,
                      objs["gen_t"].E, objs["gen_tbar"].E)).T
    '''
    mlb_top_array = np.array((objs["mlb_top"].px, objs["mlb_topbar"].px,
                         objs["mlb_top"].py, objs["mlb_topbar"].py,
                         objs["mlb_top"].pz, objs["mlb_topbar"].pz,
                         objs["mlb_top"].E, objs["mlb_topbar"].E)).T
    '''
    weight_array = np.array((objs["weight"])).T
    #mlb_filter_array = np.array((objs["mlb_filter"])).T
    
    #return gen_top_array, mlb_top_array, weight_array, mlb_filter_array
    return gen_t_array, weight_array

def getAllData(xrootd=False):
    ''' Concatenate the numpy arrays from different channels and eras together.'''
    gen_top_tot = {key: [] for key in datasets.keys()}
    #mlb_top_tot = {{key: [] for key in datasets}}
    tf_top_tot = {key: [] for key in datasets.keys()}
    weight_tot = {key: [] for key in datasets.keys()}
    #filter_dilepton_tot = {key: [] for key in datasets.keys()} # does it still exist?
    #filter_mlb_tot = {{key: [] for key in datasets}}
    
    channels = ["ee", "emu", "mumu"]
    #channels = ["mumu"]
    for era, dir in datasets.items():
        for channel in channels:
            ttbar_files = []
            path_to_dir = f"{dir}/{channel}/"
            path_to_tf = f"{tf_results[era]}/{channel}/"
            files = os.listdir(path_to_dir)
            ttbar_files = [x for x in files if "ttbar_fromDilepton" in x]
            for filename in ttbar_files:
                path_to_file = f"{path_to_dir}/{filename}"
                print(path_to_file)
                #gen_top, mlb_top, weight, mlb_filter = getObjsPerFile(path_to_file)
                gen_top, weight = getObjsPerFile(path_to_file)
                gen_top_tot[era].append(gen_top)
                #mlb_top_tot[era].append(mlb_top)
                weight_tot[era].append(weight)
                #filter_mlb_tot[era].append(mlb_filter)
                
                path_to_tffile = f"{path_to_tf}/{filename}"
                tf_top, _ = getTfResultPerFile(path_to_tffile)
                tf_top_tot[era].append(tf_top)
                
    
    for era, _list in gen_top_tot.items():
        gen_top_tot[era] = np.concatenate(_list)

    '''
    for era, _list in mlb_top_tot.items():
        _list = np.concatenate(_list)
        mlb_top_tot[era] = _list[filter_dilepton_tot[era]]
    '''
    
    for era, _list in tf_top_tot.items():
        tf_top_tot[era] = np.concatenate(_list)

    for era, _list in weight_tot.items():
        weight_tot[era] = np.concatenate(_list)

    '''
    for era, _sist in filter_mlb_tot.items():
        _list = np.concatenate(_list)
        filter_mlb_tot[era] = _list[filter_dilepton_tot[era]]
    '''
    #return gen_top_tot, mlb_top_tot, tf_top_tot, weight_tot, filter_mlb_tot
    return gen_top_tot, tf_top_tot, weight_tot