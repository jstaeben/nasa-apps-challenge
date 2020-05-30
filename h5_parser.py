#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 14:37:18 2020

@author: jamiestaeben
"""
import h5py as h5
import gdal
import numpy as np
import matplotlib.pyplot as plt
import time
  
# open a file containing list of .h5 files 
data_files = open("data_files.txt", "r")
data_file_list = data_files.read().splitlines()

# parse through h5 file and print total brightness temperature
def parseFile(filename):
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

    # go through each value and att it to the totalBrigtness var
    for i in dset_rad:
        for j in i:
            totalBrightness += j

    # pretty output
    print("\n~~~~~~ {} ~~~~~~\n".format(fname))
    print("Total Brightness Temperature: {}".format(totalBrightness))
    toc = time.perf_counter()
    print("Time elapsed: {} seconds".format(int(toc - tic)))

    f1.close()


# go through each data file in our list and get its brightness temperature
for data_file_name in data_file_list:
    parseFile(data_file_name)
