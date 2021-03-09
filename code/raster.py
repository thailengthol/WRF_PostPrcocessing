# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:52:11 2020

@author: Rajitha
"""
from __future__ import print_function
from netCDF4 import Dataset
from wrf import getvar
import numpy as np
from osgeo import gdal
from osgeo import osr

ncfile = Dataset("wrfcdx_d02_2019-03-21_17_00_49")

# Get the lat,lon, and sunshine duration
lat = getvar(ncfile, "LAT", meta=False)
lon = getvar(ncfile, "LON", meta=False)
SUND = getvar(ncfile, "SUND", meta=False)

#Digital number for each pixel
array = np.array(SUND)

# My image array      
lat = np.array(lat)
lon = np.array(lon)

# For each pixel I know it's latitude and longitude.
# As you'll see below you only really need the coordinates of
# one corner, and the resolution of the file.

xmin,ymin,xmax,ymax = [lon.min(),lat.min(),lon.max(),lat.max()]
nrows,ncols = np.shape(array)
xres = (xmax-xmin)/float(ncols)
yres = (ymax-ymin)/float(nrows)
geotransform=(xmin,xres,0,ymax,0, -yres)   


output_raster = gdal.GetDriverByName('GTiff').Create('myraster2.tif',ncols, nrows, 1 ,gdal.GDT_Float32)  # Open the file
output_raster.SetGeoTransform(geotransform)  # Specify its coordinates
srs = osr.SpatialReference()                 # Establish its coordinate encoding
srs.ImportFromEPSG(4326)                     # This one specifies WGS84 lat long.
                                             
                                          
output_raster.SetProjection( srs.ExportToWkt() )   # Exports the coordinate system 
                                                   # to the file
output_raster.GetRasterBand(1).WriteArray(array)   # Writes my array to the raster

output_raster.FlushCache()