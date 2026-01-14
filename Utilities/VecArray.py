"""
Utilities/VecArray.py

This script:
- Defines helper functions for converting particles into Momentum-4D/2D from tree branches or numpy arrays.

Usage:
    from Utilities.VecArray import set4DVecPtEtaPhiM,
                                   set4DVecPtEtaPhiE,
                                   set4DVecPxPyPzE,
                                   set2DVecPtPhi,
                                   set2DVecPxPy,
                                   convertAwkToNumpy,
    
    Each function takes both numpy arrays and Tree branches (be aware of Tree and Branch version)
    Each function takes a filter for numpy array to select events.
    convertAwkToNumpy clips an awkward array with certain length.

Author: Yao Yao
Date: 2026-01-14
"""


import awkward as ak
import numpy as np
import uproot
import vector

# Add new tree types and branch types to read from root files, if it is updated
tree_types = (uproot.models.TTree.Model_TTree_v20)
branch_types = (uproot.models.TBranch.Model_TBranch_v13)


def set4DVecPtEtaPhiM(pt, eta, phi, mass, filter=None):
    if isinstance(pt, branch_types):
        pt = pt.array(library="np")
    if isinstance(eta, branch_types):
        eta = eta.array(library="np")
    if isinstance(phi, branch_types):
        phi = phi.array(library="np")
    if isinstance(mass, branch_types):
        mass = mass.array(library="np")

    if not isinstance(pt, np.ndarray) \
            or not isinstance(eta, np.ndarray) \
            or not isinstance(phi, np.ndarray) \
            or not isinstance(mass, np.ndarray):
        print("Inputs cannot be converted to np ndarray")
        return

    if filter is None:
        filter = np.ones(mass.shape, dtype=bool)

    if not isinstance(filter, np.ndarray):
        print("Filter is not np.ndarray")
        return

    return vector.array({
        "pt" : pt[filter],
        "eta": eta[filter],
        "phi": phi[filter],
        "mass": mass[filter],
    })


def set4DVecPtEtaPhiE(pt, eta, phi, energy, filter=None):
    if isinstance(pt, branch_types):
        pt = pt.array(library="np")
    if isinstance(eta, branch_types):
        eta = eta.array(library="np")
    if isinstance(phi, branch_types):
        phi = phi.array(library="np")
    if isinstance(energy, branch_types):
        energy = energy.array(library="np")

    if not isinstance(pt, np.ndarray) \
            or not isinstance(eta, np.ndarray) \
            or not isinstance(phi, np.ndarray) \
            or not isinstance(energy, np.ndarray):
        print("Inputs cannot be converted to np ndarray")
        return

    if filter is None:
        filter = np.ones(energy.shape, dtype=bool)

    if not isinstance(filter, np.ndarray):
        print("Filter is not np.ndarray")
        return
        
    return vector.array({
        "pt" : pt[filter],
        "eta": eta[filter],
        "phi": phi[filter],
        "energy": energy[filter],
    })

    
def set4DVecPxPyPzE(px, py, pz, e, filter=None):
    if isinstance(px, branch_types):
        px = px.array(library="np")
    if isinstance(py, branch_types):
        py = py.array(library="np")
    if isinstance(pz, branch_types):
        pz = pz.array(library="np")
    if isinstance(e, branch_types):
        e = e.array(library="np")

    if not isinstance(px, np.ndarray) \
            or not isinstance(py, np.ndarray) \
            or not isinstance(pz, np.ndarray) \
            or not isinstance(e, np.ndarray):
        print("Inputs cannot be converted to np ndarray")
        return

    if filter is None:
        filter = np.ones(e.shape, dtype=bool)

    if not isinstance(filter, np.ndarray):
        print("Filter is not np.ndarray")
        return
        
    return vector.array({
        "px" : px[filter],
        "py": py[filter],
        "pz": pz[filter],
        "E": e[filter],
    })

    
def set2DVecPtPhi(pt, phi, filter=None):
    if isinstance(pt, branch_types):
        pt = pt.array(library="np")
    if isinstance(phi, branch_types):
        phi = phi.array(library="np")

    if not isinstance(pt, np.ndarray) \
            or not isinstance(phi, np.ndarray):
        print("Inputs cannot be converted to np ndarray")
        return

    if filter is None:
        filter = np.ones(phi.shape, dtype=bool)

    if not isinstance(filter, np.ndarray):
        print("Filter is not np.ndarray")
        return

    return vector.array({
        "pt" : pt[filter],
        "phi": phi[filter],
    })


def set2DVecPxPy(px, py, filter=None):
    if isinstance(px, branch_types):
        px = px.array(library="np")
    if isinstance(py, branch_types):
        py = py.array(library="np")

    if not isinstance(px, np.ndarray) \
            or not isinstance(py, np.ndarray):
        print("Inputs cannot be converted to np ndarray")
        return

    if filter is None:
        filter = np.ones(py.shape, dtype=bool)
    
    if not isinstance(filter, np.ndarray):
        print("Filter is not np.ndarray")
        return

    return vector.array({
        "px" : px[filter],
        "py": py[filter],
    })


def convertAwkToNumpy(awk_array, length, filter):
    awk_array = ak.pad_none(awk_array,length,axis=1,clip=True)
    awk_array = ak.fill_none(awk_array,0)
    return ak.to_numpy(awk_array)[filter]