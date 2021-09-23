# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 15:40:09 2021

@author: TT User
"""


import numpy as np
import matplotlib.pyplot as plt
from time import gmtime, strftime
from scipy.signal import butter, lfilter
from QRSDetectorOffline import QRSDetectorOffline

#%%
qrs_detector = QRSDetectorOffline(ecg_data_path="ecg_data_1.csv", verbose=True,
                                  log_data=True, plot_data=True, show_plot=True)