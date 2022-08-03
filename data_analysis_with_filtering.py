import pyxdf
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.signal import find_peaks, butter, lfilter, freqz
import unittest
import os
import sys

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

cwd = os.getcwd()


f = fd.askopenfile()

data, header = pyxdf.load_xdf(f.buffer)

for stream in data:
    leg_data = stream['time_series']
    legName = stream['info']['name']
    #Create figure
    num_variables = leg_data.shape[1]
    #fig, ax = plt.subplots(num_variables,1)
    plt.figure()
    plt.suptitle(legName )
    plt.tight_layout()

    torque_index = 3
    angular_index = 2

   

    order = 6
    fs = 30.0       
    cutoff = 3.667 

    y = butter_lowpass_filter(leg_data[:,torque_index], cutoff, fs, order)

     # Creating the data for filteration
    T = len(y)        # value taken in seconds
    n = len(y) # indicates total samples
    t = np.linspace(0, T, n, endpoint=False)
    
    plt.plot(leg_data[:,torque_index])
    plt.plot(t,y,'g-', label='filtered data')
    peaks,_ = find_peaks(leg_data[:,torque_index],height=3)
    negative_peaks,_ = find_peaks(-leg_data[:,torque_index],height=3)
    plt.plot(peaks, leg_data[peaks,torque_index], "x")
    plt.plot(negative_peaks, leg_data[negative_peaks,torque_index], "x")
    dpeaks=np.diff(peaks)
    flexion_off = np.where(dpeaks > 50)
    flexion_on = flexion_off[0] + 1
    dnegative_peaks=np.diff(negative_peaks)
    extension_off = np.where(dnegative_peaks > 50)
    extension_on = extension_off[0] + 1
    plt.plot(peaks[flexion_off], leg_data[peaks[flexion_off],torque_index], "go")
    plt.plot(peaks[flexion_on], leg_data[peaks[flexion_on],torque_index], "ro")
    plt.plot(negative_peaks[extension_off], leg_data[negative_peaks[extension_off],torque_index], "go")
    plt.plot(negative_peaks[extension_on], leg_data[negative_peaks[extension_on],torque_index], "ro")


    print(legName)
    test_fail = 0

    timeDelta_ms = 10
    #Calculate Slopes
    #calculate flexion turn off
    x_next = peaks[flexion_off]+ timeDelta_ms
    flexion_off_slope = (leg_data[x_next,torque_index] - leg_data[peaks[flexion_off],torque_index])/(timeDelta_ms/1000)
    #calculate flexion turn on
    x_next = peaks[flexion_on] - timeDelta_ms
    flexion_on_slope = (leg_data[peaks[flexion_on],torque_index] - leg_data[x_next,torque_index])/(timeDelta_ms/1000)

    #calculate extension turn off
    x_next = negative_peaks[extension_off]+ timeDelta_ms
    extension_off_slope = (leg_data[x_next,torque_index] - leg_data[negative_peaks[extension_off],torque_index])/(timeDelta_ms/1000)

    #calculate extension turn on 
    x_next = negative_peaks[extension_on] - timeDelta_ms
    extension_on_slope = (leg_data[negative_peaks[extension_on],torque_index] - leg_data[x_next,torque_index])/(timeDelta_ms/1000)
     
    #Statistical operations
    ave_flexion_off_slope = np.absolute(np.mean(flexion_off_slope))
    ave_flexion_on_slope = np.absolute(np.mean(flexion_on_slope))
    ave_extension_off_slope = np.absolute(np.mean(extension_off_slope))
    ave_extension_on_slope = np.absolute(np.mean(extension_on_slope))

    try:
        msg = "Flexion Turn Off Slope "
        msg1 = " is greater than: "
        msg2 = " Test Failed."
        assert ave_flexion_off_slope < 70,  msg +  str(ave_flexion_off_slope) + msg1 + str(70) + msg2
    except:
        print(sys.exc_info()[1])
        test_fail = 1
    try:
        msg = "Flexion Turn Off Slope "
        msg1 = " is less than: "
        msg2 = " Test Failed."
        assert ave_flexion_off_slope > 50,  msg +  str(ave_flexion_off_slope) + msg1 + str(50) + msg2
    except:
        print(sys.exc_info()[1])
        test_fail = 1

    try:
        msg = "Flexion Turn On Slope "
        msg1 = " is greater than: "
        msg2 = " Test Failed."
        assert ave_flexion_on_slope < 70,  msg +  str(ave_flexion_on_slope) + msg1 + str(70) + msg2
    except:
        print(sys.exc_info()[1])
        test_fail = 1
    try:
        msg = "Flexion Turn On Slope "
        msg1 = " is less than: "
        msg2 = " Test Failed."
        assert ave_flexion_on_slope > 50,  msg +  str(ave_flexion_on_slope) + msg1 + str(50) + msg2
    except:
        print(sys.exc_info()[1])
        test_fail = 1

    try:
        msg = "Extension Turn Off Slope "
        msg1 = " is greater than: "
        msg2 = " Test Failed."
        assert ave_extension_off_slope < 110,  msg +  str(ave_extension_off_slope) + msg1 + str(110) + msg2
    except:
        print(sys.exc_info()[1])
        test_fail = 1
    try:
        msg = "Extension Turn Off Slope "
        msg1 = " is less than: "
        msg2 = " Test Failed."
        assert ave_extension_off_slope > 90,  msg +  str(ave_extension_off_slope) + msg1 + str(90) + msg2
    except:
        print(sys.exc_info()[1])
        test_fail = 1

    try:
        msg = "Extension Turn On Slope "
        msg1 = " is greater than: "
        msg2 = " Test Failed."
        assert ave_extension_on_slope < 110,  msg +  str(ave_extension_on_slope) + msg1 + str(110) + msg2
    except:
        print(sys.exc_info()[1])
        test_fail = 1
    try:
        msg = "Extension Turn On Slope "
        msg1 = " is less than: "
        msg2 = " Test Failed."
        assert ave_extension_on_slope > 90,  msg +  str(ave_extension_on_slope) + msg1 + str(90) + msg2
    except:
        print(sys.exc_info()[1])
        test_fail = 1

if test_fail:
    print("Test Failed")
else:
    print("Test Passed")
plt.show()
