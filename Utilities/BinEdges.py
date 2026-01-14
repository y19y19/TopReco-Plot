"""
Utilities/BinEdges.py

This script:
- Defines the bin edges for variables when plotting their 1-D or 2-D distribution.
    - For each variable, either 'min', 'max', 'bins' are defined with scalers, or 'bin_edges' is defined with a list. 
- Defines the bin edges for variables when plotting their Root-Mean-Square error (RMSE), bias and variance
    - For each variable, a 'bin_edges' is defined with a list. 

Usage:
    from Utilities.BinEdges import BIN_EDGES
    xmin=BIN_EDGES['kinematics']['ttbar_phi']['min'] 
    xmax=BIN_EDGES['kinematics']['ttbar_phi']['max'] 
    nbins=BIN_EDGES['kinematics']['ttbar_phi']['bins'] 
    xticks=BIN_EDGES['kinematics']['ttbar_phi]['xticks'] # for variables that need to speicfy x-axis tick labels
    xticks_label=BIN_EDGES['kinematics']['ttbar_phi']['xticks_label'] # for variables that need to speicfy x-axis tick labels

Author: Yao Yao
Date: 2026-01-14
"""

import math

BIN_EDGES = {
    'kinematics': {    
        # Spin correlation variables
        'll_cHel': {
            'min': -1,
            'max': 1,
            'bins': 80,
            'bin_edges': None
        },
        'b1k': {
            'min': -1,
            'max': 1,
            'bins': 80,
            'bin_edges': None
        },
        'b2k': {
            'min': -1,
            'max': 1,
            'bins': 80,
            'bin_edges': None
        },
        'b1n': {
            'min': -1,
            'max': 1,
            'bins': 80,
            'bin_edges': None
        },
        'b2n': {
            'min': -1,
            'max': 1,
            'bins': 80,
            'bin_edges': None
        },
        'b1r': {
            'min': -1,
            'max': 1,
            'bins': 80,
            'bin_edges': None
        },
        'b2r': {
            'min': -1,
            'max': 1,
            'bins': 80,
            'bin_edges': None
        },
        'c_kk': {
            'min': -1,
            'max': 1,
            'bins': 80,
            'bin_edges': None
        },
        'c_rr': {
            'min': -1,
            'max': 1,
            'bins': 80,
            'bin_edges': None
        },
        'c_nn': {
            'min': -1,
            'max': 1,
            'bins': 80,
            'bin_edges': None
        },
        'c_rk': {
            'min': -1,
            'max': 1,
            'bins': 80,
            'bin_edges': None
        },
        'c_kr': {
            'min': -1,
            'max': 1,
            'bins': 80,
            'bin_edges': None
        },
        'c_nr': {
            'min': -1,
            'max': 1,
            'bins': 80,
            'bin_edges': None
        },
        'c_rn': {
            'min': -1,
            'max': 1,
            'bins': 80,
            'bin_edges': None
        },
        'c_nk': {
            'min': -1,
            'max': 1,
            'bins': 80,
            'bin_edges': None
        },
        'c_kn': {
            'min': -1,
            'max': 1,
            'bins': 80,
            'bin_edges': None
        },
        'c_hel': {
            'min': -1,
            'max': 1,
            'bins': 80,
            'bin_edges': None
        },
        'c_han': {
            'min': -1,
            'max': 1,
            'bins': 80,
            'bin_edges': None
        },
    
        # ttbar
        'ttbar_p': {
            'min': 0,
            'max': 1200,
            'bins': 80,
            'bin_edges': None
        },
        'ttbar_px': {
            'min': -200,
            'max': 200,
            'bins': 80,
            'bin_edges': None
        },
        'ttbar_py': {
            'min': -200,
            'max': 200,
            'bins': 80,
            'bin_edges': None
        },
        'ttbar_pz': {
            'min': -1500,
            'max': 1500,
            'bins': 80,
            'bin_edges': None
        },
        'ttbar_energy': {
            'min': 300,
            'max': 1700,
            'bins': 80,
            'bin_edges': None
        },
        'ttbar_pt': {
            'min': 0,
            'max': 400,
            'bins': 80,
            'bin_edges': None
        },
        'ttbar_eta': {
            'min': -6,
            'max': 6,
            'bins': 80,
            'bin_edges': None
        },
        'ttbar_phi': {
            'min': -3.15,
            'max': 3.15,
            'bins': 80,
            'bin_edges': None,
            'xticks': [-math.pi, -math.pi/2, 0, math.pi/2, math.pi],
            'xticks_label': [r'$-\pi$',r'$-\frac{\pi}{2}$','0', r'$\frac{\pi}{2}$', r'$\pi$']
        },
        'ttbar_mass': {
            'min': 300,
            'max': 1300,
            'bins': 80,
            'bin_edges': None
        },
        'ttbar_delta_eta': {
            'min': 0,
            'max': 10,
            'bins': 80,
            'bin_edges': None
        },
        'ttbar_delta_phi': {
            'min': 0,
            'max': 3.15,
            'bins': 80,
            'bin_edges': None
        },
        'ttbar_delta_r': {
            'min': 0,
            'max': 10,
            'bins': 80,
            'bin_edges': None
        },
    
        # t 
        't_p': {
            'min': 0,
            'max': 850,
            'bins': 80,
            'bin_edges': None
        },
        't_px': {
            'min': -400,
            'max': 400,
            'bins': 80,
            'bin_edges': None
        },
        't_py': {
            'min': -400,
            'max': 400,
            'bins': 80,
            'bin_edges': None
        },
        't_pz': {
            'min': -1500,
            'max': 1500,
            'bins': 80,
            'bin_edges': None
        },
        't_energy': {
            'min': 170,
            'max': 1000,
            'bins': 80,
            'bin_edges': None
        },
        't_pt': {
            'min': 0,
            'max': 500,
            'bins': 80,
            'bin_edges': None
        },
        't_eta': {
            'min': -6,
            'max': 6,
            'bins': 80,
            'bin_edges': None
        },
        't_phi': {
            'min': -3.15,
            'max': 3.15,
            'bins': 80,
            'bin_edges': None,
            'xticks': [-math.pi, -math.pi/2, 0, math.pi/2, math.pi],
            'xticks_label': [r'$-\pi$',r'$-\frac{\pi}{2}$','0', r'$\frac{\pi}{2}$', r'$\pi$']
        },
        't_mass': {
            'min': 165.25,
            'max': 180.25,
            'bins': 30,
            'bin_edges': None
        },

        # tbar 
        'tbar_p': {
            'min': 0,
            'max': 850,
            'bins': 80,
            'bin_edges': None
        },
        'tbar_px': {
            'min': -400,
            'max': 400,
            'bins': 80,
            'bin_edges': None
        },
        'tbar_py': {
            'min': -400,
            'max': 400,
            'bins': 80,
            'bin_edges': None
        },
        'tbar_pz': {
            'min': -1500,
            'max': 1500,
            'bins': 80,
            'bin_edges': None
        },
        'tbar_energy': {
            'min': 170,
            'max': 1000,
            'bins': 80,
            'bin_edges': None
        },
        'tbar_pt': {
            'min': 0,
            'max': 500,
            'bins': 80,
            'bin_edges': None
        },
        'tbar_eta': {
            'min': -6,
            'max': 6,
            'bins': 80,
            'bin_edges': None
        },
        'tbar_phi': {
            'min': -3.15,
            'max': 3.15,
            'bins': 80,
            'bin_edges': None,
            'xticks': [-math.pi, -math.pi/2, 0, math.pi/2, math.pi],
            'xticks_label': [r'$-\pi$',r'$-\frac{\pi}{2}$','0', r'$\frac{\pi}{2}$', r'$\pi$']
        },
        'tbar_mass': {
            'min': 165.25,
            'max': 180.25,
            'bins': 30,
            'bin_edges': None
        },

        # boosted t
        'boosted_t_p': {
            'min': 0,
            'max': 500,
            'bins': 80,
            'bin_edges': None
        },
        'boosted_t_px': {
            'min': -400,
            'max': 400,
            'bins': 80,
            'bin_edges': None
        },
        'boosted_t_py': {
            'min': -400,
            'max': 400,
            'bins': 80,
            'bin_edges': None
        },
        'boosted_t_pz': {
            'min': -500,
            'max': 500,
            'bins': 80,
            'bin_edges': None
        },
        'boosted_t_energy': {
            'min': 170,
            'max': 700,
            'bins': 80,
            'bin_edges': None
        },
        'boosted_t_pt': {
            'min': 0,
            'max': 500,
            'bins': 80,
            'bin_edges': None
        },
        'boosted_t_eta': {
            'min': -6,
            'max': 6,
            'bins': 80,
            'bin_edges': None
        },
        'boosted_t_phi': {
            'min': -3.15,
            'max': 3.15,
            'bins': 80,
            'bin_edges': None,
            'xticks': [-math.pi, -math.pi/2, 0, math.pi/2, math.pi],
            'xticks_label': [r'$-\pi$',r'$-\frac{\pi}{2}$','0', r'$\frac{\pi}{2}$', r'$\pi$']
        },
        'boosted_t_mass': {
            'min': 165.25,
            'max': 180.25,
            'bins': 30,
            'bin_edges': None
        },

        # boosted tbar 
        'boosted_tbar_p': {
            'min': 0,
            'max': 500,
            'bins': 80,
            'bin_edges': None
        },
        'boosted_tbar_px': {
            'min': -400,
            'max': 400,
            'bins': 80,
            'bin_edges': None
        },
        'boosted_tbar_py': {
            'min': -400,
            'max': 400,
            'bins': 80,
            'bin_edges': None
        },
        'boosted_tbar_pz': {
            'min': -500,
            'max': 500,
            'bins': 80,
            'bin_edges': None
        },
        'boosted_tbar_energy': {
            'min': 170,
            'max': 700,
            'bins': 80,
            'bin_edges': None
        },
        'boosted_tbar_pt': {
            'min': 0,
            'max': 500,
            'bins': 80,
            'bin_edges': None
        },
        'boosted_tbar_eta': {
            'min': -6,
            'max': 6,
            'bins': 80,
            'bin_edges': None
        },
        'boosted_tbar_phi': {
            'min': -3.15,
            'max': 3.15,
            'bins': 80,
            'bin_edges': None,
            'xticks': [-math.pi, -math.pi/2, 0, math.pi/2, math.pi],
            'xticks_label': [r'$-\pi$',r'$-\frac{\pi}{2}$','0', r'$\frac{\pi}{2}$', r'$\pi$']
        },
        'boosted_tbar_mass': {
            'min': 165.25,
            'max': 180.25,
            'bins': 30,
            'bin_edges': None
        },
    },
    'rmse' : {
        'ttbar_mass': {
            'bin_edges': [300.0, 310.0, 320.0, 330.0, 340.0, 350.0, 360.0, 370.0, 380.0, 390.0, 
                          400.0, 410.0, 420.0, 430.0, 440.0, 450.0, 460.0, 470.0, 480.0, 490.0, 
                          500.0, 510.0, 520.0, 530.0, 540.0, 550.0, 560.0, 570.0, 580.0, 590.0, 
                          600.0, 610.0, 620.0, 630.0, 640.0, 650.0, 660.0, 670.0, 680.0, 690.0, 
                          700.0, 720.0, 740.0, 760.0, 780.0, 800.0, 820.0, 860.0, 900.0, 940.0, 
                          980.0, 1060.0, 1140.0, 1220.0, 1300.0]
        },
        'ttbar_pt': {
            'bin_edges': [0.0, 4.0, 8.0, 12.0, 16.0, 20.0, 24.0, 28.0, 32.0, 36.0, 
                          40.0, 44.0, 48.0, 52.0, 56.0, 60.0, 64.0, 68.0, 72.0, 76.0, 
                          80.0, 90.0, 100.0, 110.0, 120.0, 130.0, 140.0, 150.0, 160.0, 170.0, 
                          180.0, 190.0, 200.0, 220.0, 240.0, 260.0, 280.0, 300.0, 320.0, 340.0, 
                          360.0, 400.0]
        },
        'ttbar_p': {
            'bin_edges': [0.0, 4.0, 8.0, 12.0, 16.0, 20.0, 24.0, 28.0, 32.0, 36.0, 
                          40.0, 44.0, 48.0, 52.0, 56.0, 60.0, 64.0, 68.0, 72.0, 76.0, 
                          80.0, 90.0, 100.0, 110.0, 120.0, 130.0, 140.0, 150.0, 160.0, 170.0, 
                          180.0, 190.0, 200.0, 220.0, 240.0, 260.0, 280.0, 300.0, 320.0, 340.0, 
                          360.0, 400.0]
        },
        'ttbar_energy': {
            'bin_edges': [300.0, 320.0, 330.0, 340.0, 350.0, 365.0, 380.0, 395.0, 410.0, 425.0, 
                          440.0, 455.0, 470.0, 485.0, 500.0, 515.0, 530.0, 545.0, 560.0, 575.0, 
                          590.0, 605.0, 620.0, 635.0, 650.0, 665.0, 680.0, 695.0, 710.0, 725.0, 
                          740.0, 755.0, 770.0, 785.0, 800.0, 815.0, 830.0, 845.0, 860.0, 875.0, 
                          890.0, 905.0, 920.0, 935.0, 950.0, 970.0, 990.0, 1010.0, 1030.0, 1050.0, 
                          1070.0, 1090.0, 1110.0, 1130.0, 1150.0, 1170.0, 1190.0, 1210.0, 1250.0, 1290.0, 
                          1330.0, 1370.0, 1410.0, 1450.0, 1500.0, 1550.0, 1600.0, 1650.0, 1700.0]
        },
        'ttbar_pz': {
            'bin_edges': [-1500.0, -1400.0, -1320.0, -1240.0, -1160.0, -1080.0, -1040.0, -1000.0, 
                          -960.0, -920.0, -880.0, -840.0, -800.0, -760.0, -720.0, -680.0, -640.0, 
                          -600.0, -560.0, -520.0, -480.0, -440.0, -400.0, -360.0, -320.0, -280.0, 
                          -240.0, -200.0, -160.0, -120.0, -80.0, -40.0, -0.0, 40.0, 80.0, 120.0, 
                          160.0, 200.0, 240.0, 280.0, 320.0, 360.0, 400.0, 440.0, 480.0, 520.0, 
                          560.0, 600.0, 640.0, 680.0, 720.0, 760.0, 800.0, 840.0, 880.0, 920.0, 
                          960.0, 1000.0, 1040.0, 1080.0, 1160.0, 1240.0, 1320.0, 1400.0, 1500.0]
        },
        't_pt': {
            'bin_edges': [  0.,  10.,  20.,  30.,  40.,  50.,  60.,  70.,  80.,  90., 100.,
                          110., 120., 130., 140., 150., 160., 170., 180., 190., 200., 210.,
                          220., 230., 240., 250., 260., 270., 280., 290., 300., 320.,
                          340., 360., 380., 400., 
                          440., 500.]
        },
        't_p': {
            'bin_edges': [  0.,  10.,  20.,  30.,  40.,  50.,  60.,  70.,  80.,  90., 100.,
                          110., 120., 130., 140., 150., 160., 170., 180., 190., 200., 210.,
                          220., 230., 240., 250., 260., 270., 280., 290., 300., 320.,
                          340., 360., 380., 400., 
                          440., 500.]
        },
        't_energy': {
            'bin_edges': [ 170.,  180.,  190.,  200.,  210.,  220.,  230.,  240.,  250.,
                           260.,  270.,  280.,  290.,  300.,  310.,  320.,  330.,  340.,
                           350.,  360.,  370.,  380.,  390.,  400.,  420.,  440.,
                           460.,  480.,  500.,  520.,  540.,  560.,  580.,  600.,  620.,
                           640.,  660.,  680.,  700.,  720.,  740.,  760.,  780.,  800.,
                           840.,   880.,  920.,  960.,  
                          1000.]
        },
        't_pz': {
            'bin_edges': [-1500.0, -1400.0, -1320.0, -1240.0, -1160.0, -1120.0, -1080.0, 
                          -1040.0, -1000.0, -960.0, -920.0, -880.0, -840.0, -800.0, -760.0, 
                          -720.0, -680.0, -640.0, -600.0, -560.0, -520.0, -480.0, -440.0,
                          -400.0, -360.0, -320.0, -280.0, -240.0, -200.0, -160.0, -120.0, 
                          -80.0, -40.0, -0.0, 40.0, 80.0, 120.0, 160.0, 200.0, 240.0, 280.0, 
                          320.0, 360.0, 400.0, 440.0, 480.0, 520.0, 560.0, 600.0, 640.0, 680.0, 
                          720.0, 760.0, 800.0, 840.0, 880.0, 920.0, 960.0, 1000.0, 1040.0, 1080.0, 
                          1120.0, 1160.0, 1240.0, 1320.0, 1400.0, 1500.0]
        },
        'boosted_t_pt': {
            'bin_edges': [  0.,  10.,  20.,  30.,  40.,  50.,  60.,  70.,  80.,  90., 100.,
                          110., 120., 130., 140., 150., 160., 170., 180., 190., 200., 210.,
                          220., 230., 240., 250., 260., 270., 280., 290., 300., 310., 320.,
                          330., 340., 350., 360., 370., 380., 390., 400., 410., 420., 430.,
                          440., 450., 460., 470., 480., 490., 500.]
        },
        'boosted_t_p': {
            'bin_edges': [  0.,  10.,  20.,  30.,  40.,  50.,  60.,  70.,  80.,  90., 100.]
        },
        'boosted_t_energy': {
            'bin_edges': [170., 180., 190., 200., 210., 220., 230., 240., 250., 260., 270.,
                          280., 290., 300., 310., 320., 330., 340., 350., 360., 370., 380.,
                          390., 400., 420., 440., 460., 480., 500., 520., 540., 560.,
                          580., 600., 620., 640., 660., 680., 700.]
        },
        'boosted_t_pz': {
            'bin_edges': [-500.0, -450.0, -400.0, -350.0, -300.0, -280.0, -260.0, -240.0, 
                          -220.0, -200.0, -180.0, -160.0, -140.0, -120.0, -100.0, -80.0, 
                          -60.0,  -40.0,  -20.0,  -0.0,   20.0,   40.0,   60.0,   80.0, 
                          100.0,  120.0,  140.0,  160.0,  180.0,  200.0,  220.0,  240.0, 
                          260.0,  280.0,  300.0,  350.0,  400.0,  450.0,  500.0]
        }
    }
}
