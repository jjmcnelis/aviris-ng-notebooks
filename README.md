# Jupyter Notebooks for AVIRIS-NG

*Check out [this repo](https://github.com/ornldaac/above-airborne-avirisng-python) at ORNL DAAC's GitHub page for more AVIRIS-NG examples using data from ABoVE.*

A number of generic functions are defined in the notebooks to simplify steps previously covered. All functions take exactly one argument, a gdal.Dataset from an ENVI format binary image file.

## Notebooks

0. Introduction to AVIRIS-NG in Python      
* [Read with python-gdal](notebooks/0_read_with_gdal.ipynb)
* [Read with xarray (via rasterio)](notebooks/0_read_with_xarray.ipynb)
1. Convert from ENVI binary image to common raster formats      
* [to NetCDF](notebooks/1_convert_to_netcdf.ipynb)      
* [to GeoTIFF](notebooks/1_convert_to_geotiff.ipynb) # Coming soon      
2. [Band math](notebooks/2_band_math.ipynb)      
