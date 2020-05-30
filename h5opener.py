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


if __name__ == '__main__':
    # import required libraries


    # Read H5 file
#    filename = "VNP46A1.A2020001.h10v06.001.2020003085759.h5"
#    g = gdal.Open(filename)
#
#    if g is None:
#        print ("Problem opening file", filename)
#    else:
#        print ("File ", filename, " opened fine")
#
#    subdatasets = g.GetSubDatasets()
#    for fname, name in subdatasets:
#        #print (name)
#        print ("\t", fname)
#
#    selected_layers = ['//HDFEOS/GRIDS/VNP_Grid_DNB/Data_Fields/Radiance_M10']
#    data = {}
#    
#    file_template = "VNP46A1.A2020001.h10v06.001.2020003085759.h5"
#    g = gdal.Open(file_template)
#    print(g)
#    if g is None:
#        raise IOError
#    data[0] = g.ReadAsArray()
#    print(g.ReadAsArray())        
        
#    file_template = 'HDF4_EOS:EOS_GRID:"%s":MOD_Grid_MOD15A2:%s'
#    for i, layer in enumerate ( selected_layers ):
#    this_file = file_template % ( filename, layer )
#    print("Opening Layer %d: %s" % (i+1, this_file ))
#    g = gdal.Open ( this_file )
#    
#    if g is None:
#        raise IOError
#    data[layer] = g.ReadAsArray() 
#    print("\t>>> Read %s!" % layer)
    tic = time.perf_counter()
    plt.ion()
    filename = "VNP46A1.A2020003.h11v05.001.2020007042628.h5" #jan 1st
    f = h5.File(filename, "r")
    # Get and print list of datasets within the H5 file
    f_list = list(f.keys()) 
#    print(f_list)
    dset = f['HDFEOS']
#    print(dset)
#    for name in dset:
#        print(name)
    dset_add = dset['ADDITIONAL']
    dset_grid = dset['GRIDS']
#    for name in dset_add:
#        print(name)
    dset_file_add = dset_add['FILE_ATTRIBUTES']
#    print (dset_file_add)
#    for name in dset_grid:
#        print(name)
    dset_vnp = dset_grid['VNP_Grid_DNB']
#    for name in dset_vnp:
#        print(name)
    dset_data = dset_vnp['Data Fields']
#    for name in dset_data:
#        print(name)
    #dset_rad = dset_data['Radiance_M10']
    dset_rad = dset_data['BrightnessTemperature_M12']
#    print(dset_rad)
#    print(dset_rad[0])
#    print(len(dset_rad[0]))
#    print(len(dset_rad))
    adjusted = dset_rad
    
    totalBrightness = 0
    counter = 0
    for i in adjusted:
        for j in i:
            counter += 1
            totalBrightness+= j
    print(counter)
    print(totalBrightness)
#    plt.imshow(adjusted, interpolation='none')
#    plt.title("brightness temperature January")
#    plt.colorbar()
    
    f.close()
    filename_apr = "VNP46A1.A2020092.h11v05.001.2020121041802.h5" #april 1st
    f2 = h5.File(filename_apr, "r")
    dset2 = f2['HDFEOS']
    dset2_grid = dset2['GRIDS']
    dset2_vnp = dset2_grid['VNP_Grid_DNB']
    dset2_data = dset2_vnp['Data Fields']
    dset2_rad = dset2_data['BrightnessTemperature_M12']
    
    counter2 = 0
    totalBrightness2 = 0
    for i in dset2_rad:
        for j in i:
            counter2 += 1
            totalBrightness2+= j
    print(counter2)
    print(totalBrightness2)
    
    plt.imshow(dset2_rad, interpolation='none')
    plt.title("brightness temperature April")
    plt.colorbar()
    toc = time.perf_counter()
    print("Time: {toc - tic:0.4f} seconds") #5:11:30 2.5 min per run

#    
#    f.close()

#        print(n)

    # extract reflectance data from the H5 file
#    HDFEOS = f['HDFEOS']
#    print(HDFEOS)
#    for i in HDFEOS:
#        print(i)
    # extract one pixel from the data
    #reflectanceData = reflectance[:,49,392]
    #reflectanceData = reflectanceData.astype(float)

#    # divide the data by the scale factor
#    # note: this information would be accessed from the metadata
#    scaleFactor = 10000.0
#    reflectanceData /= scaleFactor
#    wavelength = f['wavelength']
#    wavelengthData = wavelength[:]
#    #transpose the data so wavelength values are in one column
#    wavelengthData = np.reshape(wavelengthData, 426)
#
#    # Print the attributes (metadata):
#    print("Data Description : ", reflectance.attrs['Description'])
#    print("Data dimensions : ", reflectance.shape, reflectance.attrs['DIMENSION_LABELS'])
#    # print a list of attributes in the H5 file
#    for n in reflectance.attrs:
#    print(n)
#    # close the h5 file
#    f.close()
#
#    # Plot
#    plt.plot(wavelengthData, reflectanceData)
#    plt.title("Vegetation Spectra")
#    plt.ylabel('Reflectance')
#    plt.ylim((0,1))
#    plt.xlabel('Wavelength [$\mu m$]')
#    plt.show()
#
#    # Write a new HDF file containing this spectrum
#    f = h5.File("VegetationSpectra.h5", "w")
#    rdata = f.create_dataset("VegetationSpectra", data=reflectanceData)
#    attrs = rdata.attrs
#    attrs.create("Wavelengths", data=wavelengthData)
    f.close()