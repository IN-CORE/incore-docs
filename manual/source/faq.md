##  Frequently asked questions

### IN-CORE account

- *I want to try your IN-CORE services. Do I need to register?*

    A user must have an account [registered](https://identity.ncsa.illinois.edu/register/UUMK36FU2M) with NCSA IN-CORE service. User credentials are required 
    in accessing repositories with hazard, fragility, restoration, geographic and other data sets. 
    They are also used for accessing documentation server and Jupyter notebook files.

    The username/password you chose during registration process in NCSA IN-CORE system is called 
    LDAP password, based on specific Lightweight Directory Access Protocol authentication. 
    You can test your registration credentials by accessing the [documentation server](http://incore2.ncsa.illinois.edu/).

### pyIncore

- *What is pyIncore? How does to differ from pyincore?*

    **pyIncore** is a Python module that can be used to develop scientific hazard analysis and algorithm. 
    We recommend using Jupyter notebook for running the pyIncore projects, either locally or in 
    NCSA's [IN-CORE Lab](https://incore.ncsa.illinois.edu/lab).

    **Insatalling pyincore**
    
- *Should I use virtual environment for running the pyIncore?*

    We recommend using environment manager [Anaconda](https://www.anaconda.com/distribution/) 
    or [Miniconda](https://docs.conda.io/en/latest/miniconda.html); tools that help keep dependencies 
    separate for different Python projects. If you decide to use virtual environment or manager you must do it 
    at the beginning of the installation, in the prerequisite step. Some of the underlying libraries, 
    however have to be present globally (e.g. gdal on Windows OS). Therefore pyIncore installation 
    slightly differs for virtual environments and we will be happy to help you. Contact us at 
    <incore-dev@lists.illinois.edu>.

- *What’s the difference between Anaconda, conda, and Miniconda?*
    
    The [Anaconda](https://www.anaconda.com/distribution/) Python distribution started out as a bundle 
    of scientific Python packages and libraries that were otherwise difficult to install. Many packaging 
    problems (such as compatibility of various versions) had to be solved in order to provide a cross-platform 
    bundle, and one of the tools that came out of that work 
    was the [conda](https://docs.conda.io/projects/conda/en/latest/index.html) package manager. 
    The conda Python installer is called [Miniconda](https://docs.conda.io/en/latest/miniconda.html), a small 
    version of Anaconda that includes only **conda**, **Python**, the packages they depend on and a small 
    number of other useful packages, including **pip**. 
    
    In a nutshell, *conda* is a package manager, *Miniconda* is the conda installer, and *Anaconda* is a Python 
    distribution that also includes conda and 150+ automatically installed, open source packages and their 
    dependencies that have been tested to work well together.   

- *I have Python 3 installed but pip3 command does not work.*

    We prefer **conda** installation over **pip**. Conda is a packaging tool and installer that handles library 
    dependencies as well as the Python packages themselves. In any case make sure you are running the correct 
    version of Python (you can check by running `python3 --version`). Following links will help you navigate 
    through various installations; [Python 3 Installation & Setup Guide](https://realpython.com/installing-python/), 
    [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/#the-hitchhiker-s-guide-to-python), 
    OS specific [downloads](https://www.python.org/downloads/).

    **Running pyincore**

- *I am getting “Module not Found" when I run pyIncore* 

    This can be caused by many factors. You need to make sure the module is installed for your versions of Python.
    Run ``conda list`` to obtain the packages installed using conda in the active environment.

- *I am trying to run buildingdamage.ipynb on my computer but nothing happens.*

    We assume that you are running Jupyter Notebook in your browser. Run each individual cell 
    by clicking >|Run. The cursor (box) will highlight the next cell. The actual calculation is called 
    in the last cell with the `bldg_dmg.run_analysis()` command. When successful a Comma delimited 
    file (csv) appears in the Notebook and in the Jupyter tree under Files tab.
    
### Creating and running analyses

- *What is a mapping and how do I create one?*

    We use mapping to associate each element of a given set such as Building inventory with one or more 
    elements of a second set of Fragility curves.

- *Is mapping related to a map?*

    We use noun mapping for *operation that associates each element of a given set with one or more elements 
    of a second set*. In *IN-CORE* and *pyIncore* specifically, for example a Building inventory (given set) 
    is mapped to a (second) set of Fragility curves.

- *What is dataset_id and how do I create it?*

    Each set being it a data, mapping, inventory, fragility or restoration set in IN-CORE system 
    has assigned ID, an identifier, which uniquely identifies it for the services and *pyIncore*. The unique ID 
    is assigned when the set is uploaded to the IN-CORE services. For details how to do it see technical 
    documentation or contact us at <incore-dev@lists.illinois.edu>.

- *Is Geopandas (package x) part of pyIncore?*

    The full set of Python packages available in *pyIncore* is listed in the *setup.py* file. The basic set of 
    packages is as follows: `fiona`, `folium`, `jsonpickle`, `matplotlib`, `networkx`, `numpy`, `owslib`, 
    `pandas`, `plotly`, `pyproj`, `pyyaml`, `rasterio`, `requests`, `rtree`, `scipy`, `shapely`, `wntr`, 
    `seaborn`, `pyomo`. We are currently working on creating visualization package so some packages such as 
    `folium`, `matplotlib`, `plotly` will be removed from future version of **pyIncore** core and they will 
    be moved to **pyIncore viz**.
    
- *What is the best Image processing library for Python.*

    The most common Image manipulation and processing packages are [Pillow](https://pillow.readthedocs.io/en/stable/) 
    which is a continuation of the PIL (Python Imaging Library), [scikit-image](https://scikit-image.org/), 
    a collection of algorithms for image processing, 
    [scipy](https://docs.scipy.org/doc/scipy-0.14.0/reference/ndimage.html) which is already a dependency 
    of *pyIncore* and which provides a various image processing functions that can be operated with arrays 
    of any dimensionality.   

- *My tornado analysis is returning 0 for each inventory. When I put them together in QGIS, I can see that 
   the inventories fall within the tornado’s path.*

    The dataset is probably using different projection than WGS84. QGIS converts the projections behind the scene 
    putting the inventory and tornado paths in the same place.  
    
- *Warning: Boto3 is not present.*

    Boto3 is a package for connectivity with Amazon AWS. **pyIncore** does not use it however the warning comes 
    from the package build. We beleive that certain combination of conda channels causes the warning to appear. 
    A user can ignore the warning or additionally install **boto3**.
 