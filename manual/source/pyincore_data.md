## pyIncore data

Utility package for preparing and handling the data associated with pyIncore is called **pyIncore-data**. It contains advanced Python packages 
and methods required for preparing and manipulating the IN-CORE result. 

### Features
1. Acquiring the data, such as census data.
2. Data manipulation including handling shapefile, dataframe, and others.

### Prerequisites

- **Virtual environment**: We recommend that users work with virtual environment managers called [Anaconda](https://www.anaconda.com/) 
or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).


### Installation

1. To install pyIncore-data, navigate to the directory you want to use and run the following command:
    ```
    conda install -c in-core pyincore-data
    ```
   
   For update replace `install` with `update`.
   
2. To check that the package is installed run 
    ```
    conda list
    ```
    It will again list all packages currently installed.

### Example

Jupyter notebook showing the acquisition of the census block group data and convert it to various format, 
such as shape files and other format. The shapefile format is a geospatial vector data 
format for geographic information system (GIS) software developed by Esri for interoperability among GIS software products.

Example: [pyincore-data-example.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/pyincore-data-example.ipynb)
