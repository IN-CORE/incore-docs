# pyIncore data

**pyIncore-data** is a utility package for preparing data for use in pyIncore. It contains advanced Python packages and 
methods for acquiring data from different sources and preparing it for use in IN-CORE. 

## Features
1. Acquiring data from sources such as census data.
2. Data manipulation including handling shapefiles, dataframes, etc.

## Prerequisites

- **Virtual environment**: We recommend that users work with a virtual environment manager such as [Anaconda](https://www.anaconda.com/) 
or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

## Installation

1. To install pyIncore-data, navigate to the directory you want to use and run the following command:
    ```
    conda install -c in-core pyincore-data
    ```

   If you have trouble installing pyincore-data or it is taking a long time to resolve the dependencies, try using the
   libmamba solver by running the following command:

    ```
    conda install -c in-core pyincore-data --solver=libmamba
    ```
   If the installed pyincore-data version is not the latest or lower than the desired one, specify the version number in installation command.
    ```
    conda install -c in-core pyincore-data=0.5.0 (or your version of choice)
    ```
   Version information for pyincore-data can be found in
   - https://anaconda.org/IN-CORE/pyincore-data
   
   For updating pyIncore-data, replace `install` with `update` in the above command.
   

2. To check that the pyIncore-data package is installed, run the following command:
    ```
    conda list
    ```
   
    This will list all packages currently installed.

## Example

The Jupyter notebook below uses pyIncore-data to acquire census block group data and converts it 
to different formats including shapefile and other formats. The shapefile format is a geospatial vector data 
format for geographic information system (GIS) software developed by Esri for interoperability among GIS software products.

Example: [pyincore-data-example.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/pyincore-data-example.ipynb)
