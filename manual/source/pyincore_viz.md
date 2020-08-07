## pyIncore viz

Visualization package associated with pyIncore is called **pyIncore-viz**. It contains advanced Python packages and code  
required for visualizing and disseminating the IN-CORE results, mainly via Jupyter Notebooks. At least one powerful  
library called [Matplotlib](https://matplotlib.org/) for creating static, animated, and interactive visualizations in Python 
is already part of pyIncore (as a dependency). We decided however to keep 
more interactive visualization in a separate package. An example would be for example geo-referenced mapping with 
[ipyleaflet](https://ipyleaflet.readthedocs.io/en/latest/).
 
### Prerequisites

- **pyIncore**: A user must have pyIncore package installed. See [pyIncore section](pyincore) for details.

- **Virtual environment**: We recommend that users work with virtual environment managers called [Anaconda](https://www.anaconda.com/) 
or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

- Mac OS specific notes: There is a Mac specific `matplotlib` installation issue addressed 
  at StackOverflow [link 1](https://stackoverflow.com/questions/4130355/python-matplotlib-framework-under-macosx) and [link 2](https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python). In a nutshell, insert line:
    ```
        backend : Agg
    ```
    
    into `~/.matplotlib/matplotlibrc` file. You must create the file (`matplotlibrc`) if it does not exist.

### Installation

1. To install pyIncore-viz, navigate to the directory you want to use for running Jupyter Notebooks and run the following command:
    ```
    conda install -c in-core pyincore-viz
    ```
   
   For update replace `install` with `update`.
   
2. To check that the package is installed run 
    ```
    conda list
    ```
    It will again list all packages currently installed. You can check if **pyincore** and **pyincore-viz** exist in the list.

### Example

Example of Jupyter notebook code showing a shape file using **matplotlib** and **ipyleaflet**. The shapefile format is a geospatial vector 
data format for geographic information system (GIS) software developed by Esri for interoperability among GIS software products.