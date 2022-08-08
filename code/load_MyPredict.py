#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: RV Schulte
"""

import os
import h5py
import matplotlib.pyplot as plt

# Path to data files
path = '../MyPredict 1'
subj = 'MP105.hdf5'

# Load first file
hf = h5py.File(os.path.join(path,subj))

# Iterate over file structure
for day in hf:
    if 'Meta' in day:
        print('Meta data: {}'.format({k:v[()] for k,v in hf[day].items()}))
    else:
        print('Trials: {}'.format(list(hf[day].keys())))

# Print contents of one trial
print('Contents: {}'.format(list(hf['Day_1']['Trial_16'].keys())))

# And check out marker data as well:
print('Markers: {}'.format(list(hf['Day_1']['Trial_16']['Markers'].keys())))


# Load data from one trial and plot labels
trial = hf['Day_1']['Trial_05']
time = trial['Time'][()] # [()] actually loads the data, else it's only referenced
knee_r = trial['Ang_Right_Knee'][()]
knee_l = trial['Ang_Left_Knee'][()]
label = trial['Label'][()]

fig,ax = plt.subplots()
ax1 = ax.twinx()
ax.plot(time,knee_r[:,-1],'r') # Only sagittal plane
ax.plot(time,knee_l[:,-1],'b')
ax1.plot(time,label,'k')

# Combine label with marker positions
marker = trial['Markers']
mrk_time = marker['Time'][()] # Marker data is at 100Hz, instead of 1000Hz
mrk_pelvis = marker['Mrk_Sacrum'][()]

fig,ax = plt.subplots()
ax1 = ax.twinx()
ax.plot(mrk_time,mrk_pelvis)
ax1.plot(time,label,'k')