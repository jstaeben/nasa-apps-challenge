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
    
    - If you select True for saving images and GIF:
        > Everything from False
        > Images and GIF saved into the BrightTempImages directory 
"""
import sys
import os
import time
import h5py as h5
import matplotlib.pyplot as plt
import imageio

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
    f1 = h5.File(filename, "r")

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
    actualAvgBrightness += 280 # MAKE SURE THIS VALUE IS RIGHT

    # pretty output
    print("\n~~~~~~ {} ~~~~~~\n".format(filename))
    print("Total Brightness Temperature: {}".format(totalBrightness))
    toc = time.perf_counter()
    print("Time elapsed: {} seconds".format(int(toc - tic)))

    # add brightness temperature to list
    brightness_dict[ filename[:-3] ] =  totalBrightness

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
        speed = 1
        for x in range(speed):
            img_files.append(img_filename)

    f1.close()

if len(sys.argv) < 2:
    print("Syntax: python3 h5_parser.py [True/False]")
    print("=> True = Save images and GIF\n=> False = Don't save images and GIF")
    sys.exit()

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

# print out the brightness dict
for key, val in brightness_dict.items():
    print(key + ": {}".format(val))
    # this can be used to also just pull the brightness values from the dict
