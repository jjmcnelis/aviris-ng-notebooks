# Overview of AVIRIS-NG data format

**Some notes about the AVIRIS-NG tar file contents borrowed from this [repo at ORNL DAAC](https://github.com/ornldaac/above-airborne-avirisng-python/blob/master/above-airborne-avirisng-python.ipynb) that has some examples subsetting the dataset over the bands, x, and y dimensions:**

Each flight line in the dataset has two corresponding granules, each in a zipped tarfile:
>level 1 radiance, e.g. ang20180814t224053.tar.gz
level 2 reflectance, e.g. ang20180814t224053rfl.tar.gz

This tutorial works with the L2 reflectance data for a flight on August 14, 2018. Download the zip at the following link: https://daac.ornl.gov/daacdata/above/ABoVE_Airborne_AVIRIS_NG/data/ang20180814t224053rfl.tar.gz

Each reflectance tarfile contains two pairs of ENVI (Harris Geospatial) binary image files (no extension) and accompanying header files (.hdr):
>Orthocorrected and atmospherically corrected reflectance data:
*angYYYYMMDDtHHNNSS_corr_VVV_img +hdr*

Atmospherically corrected water-leaving reflectance (Gao et al. 1993; Thompson et al. 2015); 425 bands at 5-nm intervals in the visible to shortwave infrared spectral range from 380 to 2510 nm
>Orthocorrected water absorption data: 
*angYYYYMMDDtHHNNSS_h2o_VVV_img +hdr*

Retrieved column water vapor and optical absorption paths for liquid H2O and ice; 3 bands: 
>1. Column water vapor (cm),
>2. Total liquid H2O absorption path (cm), 
>3. Total ice absorption path (cm)