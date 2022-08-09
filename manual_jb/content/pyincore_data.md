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
