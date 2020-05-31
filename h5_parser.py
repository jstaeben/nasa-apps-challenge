#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 14:37:18 2020

@author: jamiestaeben
@co-author: danielgetter

Usage: python3 h5_parser.py [True/False] 
       - True = Save images and GIF
       - False = Don't save images and GIF"
       
Output: 
    - If you select False for saving images and GIF:
        > Total Brightness Temperature for each data file
        > Time elapsed for that calculation
        > Full list of Dates and the corresponding Brightness Temperature
        > Saves plot of Date vs. Brightness Temperature into the BrightTempImages directory  
    
    - If you select True for saving images and GIF:
        > Everything from the above section
        > Images and GIF saved into the BrightTempImages/ directory  
        
What you need:
       - HDF5 files in a h5files/ directory (located in working directory)
       - List of HDF5 file names in data_files.txt 
              > Ideally these would be named after the Month/Day the data was collected (ex: Jan01.h5)
"""
import sys
import os
import time
import h5py as h5
import matplotlib.pyplot as plt
import imageio
import numpy as np
import datetime

# open a file containing list of .h5 files
data_files = open("data_files.txt", "r")
data_file_list = data_files.read().splitlines()

img_files = []
brightness_dict = {}

# parse through h5 file and print total brightness temperature
def parseFile(filename, save_imgs):
    plt.ion()

    # start timer
    tic = time.perf_counter()

    # open h5 file
    f1 = h5.File("h5files/" + filename, "r")

    # some weird h5 file stuff
    dset = f1['HDFEOS']
    dset_grid = dset['GRIDS']
    dset_vnp = dset_grid['VNP_Grid_DNB']
    dset_data = dset_vnp['Data Fields']

    # this is the data we want
    # it's a 2400x24000 2D array of brightness temperature data
    dset_rad = dset_data['BrightnessTemperature_M12']

    totalBrightness = 0
    actualAvgBrightness = 0

    # go through each value and att it to the totalBrigtness var
    for i in dset_rad:
        for j in i:
            totalBrightness += j

    # calculate the actual avg brightness
    actualAvgBrightness = int(totalBrightness/5760000)
    actualAvgBrightness *= 0.0025
    actualAvgBrightness = round(actualAvgBrightness, 2)

    # pretty output
    print("\n~~~~~~ {} ~~~~~~\n".format(filename))
#    print("Total Brightness Temperature: {}".format(totalBrightness))
    print("Average Brightness Temperature: {}".format(actualAvgBrightness))
    
    # end timer
    toc = time.perf_counter()
    print("Time elapsed: {} seconds".format(int(toc - tic)))

    # add avg brightness temperature to list
    brightness_dict[filename[:-3]] =  actualAvgBrightness

    # save images if user says to
    if save_imgs == "True":
        # check if image dir exists, if not, make one
        if not os.path.exists("BrightTempImages"):
            os.mkdir("BrightTempImages")

        # Create path and file name for the image (cut off .h5 from end of filename)
        img_filename = "BrightTempImages/" + filename[:-3] + ".png"

        # save image of brightness temperature data
        plt.imsave(img_filename, dset_rad)


        # add image filenames to the gif list
        # speed is the number of the same picture that is added to the gif
        # the higher the number, the slower the speed of the gif, and vice-versa
        # (because it will go through several of the same pic before switching to a new one)
        speed = 2
        for x in range(speed):
            img_files.append(img_filename)

    f1.close()

# check proper command syntax
if len(sys.argv) < 2:
    print("Syntax: python3 h5_parser.py [True/False]")
    print("=> True = Save images and GIF\n=> False = Don't save images and GIF")
    sys.exit()

# start timer
starttime = time.perf_counter()

# go through each data file in our list and get its brightness temperature
for data_file_name in data_file_list:
    parseFile(data_file_name, sys.argv[1])

# Make a GIF if user wants
if sys.argv[1] == "True":
    images = []
    for file in img_files:
        images.append(imageio.imread(file))
    imageio.mimsave('BrightTempImages/GIF.gif', images)

# pretty seperator
print("\n~~~~~~ DONE, yay! ~~~~~~\n")

# end timer
endtime = time.perf_counter()
# convert time to h:m:s
elapsedtime = int(endtime - starttime)
hms = str(datetime.timedelta(seconds=elapsedtime))

print("Total time elapsed: {}".format(hms))

# print out the brightness dict
print("\n~~~~~~ All Brightness Temperature Values ~~~~~~\n")
for key, val in brightness_dict.items():
    print(key + ": {}".format(val))
    # this can be used to also just pull the brightness values from the dict

# plot Brightness Temperature Changes Over Time
y_values = []
for val in brightness_dict.values():
    y_values.append(val)
    
text_values = []
for key in brightness_dict.keys():
    text_values.append(key)
    
x_values = np.arange(1, len(text_values) + 1, 1)
fig, ax = plt.subplots(figsize=(18,10))
plt.ylabel('Brightness Temperature (K)',size=30)
plt.ylabel('Date',size=30)
plt.title('Brightness Temperature Changes Over Time',size=50)
fig.autofmt_xdate()
plt.plot(x_values, y_values,"-")
plt.xticks(x_values, text_values)

# save the plot as a png
plotting_dir = "BrightTempImages/"
if not os.path.exists(plotting_dir):
    os.mkdir(plotting_dir)
plt.savefig(plotting_dir + 'Temp' '.png')
plt.close()
