import numpy as np
from osgeo import gdal, osr
from pyproj import Proj, transform

def get_global_attributes(hdr):
    """Rudimentary parser for ENVI header file. Improve."""
    
    with open(hdr,'r') as f:
        header = [ln.strip() for ln in f.readlines()]

        global_atts = dict(
            description = header[2][:-1],
            samples = header[3].split("=")[1].strip(),
            lines = header[4].split("=")[1].strip(),
            bands = header[5].split("=")[1].strip(),
            data_type = header[8].split("=")[1].strip(),
            source_type = header[7].split("=")[1].strip(),
            interleave = header[9].split("=")[1].strip(),
            byte_order = header[10].split("=")[1].strip(),
            map_info = header[11].split("=")[1].strip(),
            wavelength_units = header[13].split("=")[1].strip(),
            missing_value = header[24].split("=")[1].strip())
        global_atts["Conventions"] = "CF-1.6"
    
    return(global_atts)
    

def get_shape(ds):
    """Get number of bands, columns, and rows in raster."""
    
    return(ds.RasterCount,  # band count
           ds.RasterXSize,  # col count
           ds.RasterYSize)  # row count


def get_xy_arrays(ds):
    """Generate two 1d x,y coordinate arrays."""
    
    # get raster shape
    bands, cols, rows = get_shape(ds)
    
    # get the raster geotransform as its component parts
    xmin, xres, xrot, ymax, yrot, yres = ds.GetGeoTransform()
    
    # generate coordinate arrays
    xarr = np.array([xmin+i*xres for i in range(0,cols)])
    yarr = np.array([ymax+i*yres for i in range(0,rows)])

    return(xarr, yarr)
    
    
def get_proj(ds):
    """Returns the osr spatial reference object and proj4."""
    
    native_srs = osr.SpatialReference()
    native_srs.ImportFromWkt(ds.GetProjection())
    proj4 = native_srs.ExportToProj4()
    
    return(native_srs, proj4)
    
    
def get_latlon_arrays(ds):
    """Generate two 2d lat,lon coordinate arrays."""
    
    native_srs, proj4 = get_proj(ds)
    
    inproj = Proj(proj4)
    outproj = Proj(init="epsg:4326")
    
    xarr, yarr = get_xy_arrays(ds)
    lon, lat = transform(inproj, outproj, xarr[0], yarr[0])

    # get two 2d arrays of lats and lons
    xarr2d, yarr2d = np.meshgrid(xarr, yarr)

    # flatten both arrays and transform
    lonarr, latarr = transform(
        inproj,                   # input raster srs
        outproj,                  # output raster srs
        xarr2d.flatten(),         # flat 2d array of x coordinates
        yarr2d.flatten())         # flat 2d array of y coordinates

    # return flat arrays to shape of input raster
    lonarr2d = lonarr.reshape(xarr2d.shape)
    latarr2d = latarr.reshape(yarr2d.shape)
    
    return(lonarr2d, latarr2d)