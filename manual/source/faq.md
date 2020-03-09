##  Frequently asked questions

### IN-CORE account

- *I want to try your IN-CORE services. Do I need to register?*

    A user must have an account [registered](https://identity.ncsa.illinois.edu/register/UUMK36FU2M) with NCSA IN-CORE service. User credentials are required 
    in accessing repositories such as hazard, fragility, restoration, geographic and other data sets. 
    They are also used for accessing documentation server and Jupyter Notebook files.

    The username/password you chose during registration process in IN-CORE system is called 
    LDAP password, based on specific Lightweight Directory Access Protocol authentication. 
    You can test your registration credentials by accessing the [documentation server](http://incore.ncsa.illinois.edu/).

### pyIncore


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
    
- *How do I check what version of Python and Anaconda are installed?*

    The versions can be checked by running `python --version` and/or `import sys;sys.executable` in Python console.

- *I would like to use pip. I have Python 3 installed but the pip3 command does not work.*

    We prefer **conda** installation over **pip** mainly because it handles Python packages dependencies and even library outside of 
    the Python. Conda is a packaging tool and installer that handles library dependencies as well as the Python packages themselves. 
    User can install **pyIncore** with pip however some of the underlying libraries have to be installed separatelly and present globally (GDAL).
    In any case make sure you are running the correct version of Python (you can check by running `python3 --version`). Following links will help you navigate 
    through various installations; [Python 3 Installation & Setup Guide](https://realpython.com/installing-python/), 
    [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/#the-hitchhiker-s-guide-to-python), 
    OS specific [downloads](https://www.python.org/downloads/).

    **Installing pyIncore**

- *How do I check the installed version of pyIncore?*

    In your conda virtual environment type `conda list` and the output is a list of all installed Python packages including **pyIncore**.
    
- *How do I update pyIncore?*

    - Open a terminal window
    - Activate the environment where you installed pyIncore (for example, `conda activate pyincore`)
    - Run the following command: 
      ```
        conda update -c in-core pyincore
      ```
    
- *Should I use virtual environment for running the pyIncore?*

    We recommend using environment manager [Anaconda](https://www.anaconda.com/distribution/) 
    or [Miniconda](https://docs.conda.io/en/latest/miniconda.html); tools that help keep dependencies 
    separate for different Python projects. If you decide to use virtual environment or manager you must do it 
    at the beginning of the installation, in the prerequisite step. Some of the underlying libraries, 
    however have to be present globally (e.g. gdal on Windows OS). Therefore pyIncore installation 
    slightly differs for virtual environments and we will be happy to help you. Contact us at 
    <incore-dev@lists.illinois.edu>. 

    **Running pyIncore**

- *I am getting “Module not Found" when I run pyIncore* 

    This can be caused by many factors. You need to make sure the module is installed for your versions of Python.
    Run ``conda list`` to obtain the packages installed using conda in the active environment.

- *I am trying to run building_dmg.ipynb on my computer but nothing happens.*

    We assume that you are running Jupyter Notebook in your browser. Run each individual cell 
    by clicking >|Run. The cursor (box) will highlight the next cell. The actual calculation is called 
    in the last cell with the `bldg_dmg.run_analysis()` command. When successful a Comma delimited 
    file (csv) appears in the Notebook and in the Jupyter tree under Files tab.
    
- *Can I run files locally?*

    Yes. Users can run datasets stored on their local computers. It is, however not possible to use certain resources  such as fragility locally. 
    These have to be uploaded to the IN-CORE services. For details see [Tutorials](https://incore.ncsa.illinois.edu/tutorials) 
    section of this documentation.
    
- *I cannot install/update Jypyter Notebook. I encountered a* **EnvironmentNotWritableError** *while installing Jypyter Notebook.*

- *I do not have full administrative privileges to my School/Company issued computer. The pyIncore or Jupyter Notebook does not work.*

    Users may encounter issues depending on the administrative privileges they have on their computer. 
    I downloaded [Miniconda](https://docs.conda.io/en/latest/miniconda.html) not having any reason to download [Anaconda](https://www.anaconda.com/distribution/) or miniconda. 
    When needing to install/update jupyter notebook I encountered a EnvironmentNotWritableError. I tried to continue using 
    the older version of conda. When I launched jupyter notebook and tried to run the building_dmg.ipynb file, I was unsuccessful. 
    The second try, after the recommendation of a colleague, I installed Anaconda3 rather than miniconda and proceeded through the steps 
    as instructed and had success.
    
- *How do I empty pyIncore's cache?*

### Creating and running analyses

- *What is a mapping and how do I create one?*

    We use mapping to associate each element of a given set such as Building inventory with one or more 
    elements of a second set of Fragility curves. For details see [Tutorials](https://incore.ncsa.illinois.edu/tutorials) 
    section of this documentation.

- *Is mapping related to a map?*

    We use noun mapping for *operation that associates each element of a given set with one or more elements 
    of a second set*. In *IN-CORE* and *pyIncore* specifically, for example a Building inventory (given set) 
    is mapped to a (second) set of Fragility curves.

- *What is dataset_id and how do I create it?*

    Each set being it a data, mapping, inventory, fragility or restoration set in IN-CORE system 
    has assigned ID, an identifier, which uniquely identifies it for the services and *pyIncore*. The unique ID 
    is assigned when the set is uploaded to the IN-CORE services. For details how to do it see technical 
    documentation or contact us at <incore-dev@lists.illinois.edu>.

- *How do I import datasets to IN-CORE service?*

    Have we decided where to answer it? 
    1) Notebook example with other Notebooks, linked from FAQ, 
    2) Start editing Technical documentation page (we have it ready but no content yet), 
    3) Somewhere else? (edited) 
    
    @Gowtham @Chris Navarro I added Milad’s question and your answer here: https://opensource.ncsa.illinois.edu/confluence/display/INCORE1/questions/160860190/can-i-simulate-and-upload-earthquakes-to-incore
opensource.ncsa.illinois.eduopensource.ncsa.illinois.edu
Can I simulate and upload earthquakes to incore? - IN-CORE - Confluence
I used an earthquake from hazard service for my analysis. The magnitude of this earthquake is large (magnitude = 7.9) and we got issues in econ. anal

Right now, I have flood fragility curves and surfaces developed for 15 building archetypes. Also, Hazard Model (Raster Map) for Lumberton, NC is already developed. Building Exposure data are fully included in a shapefile. So, the three-stage model (Hazard, Exposure, and vulnerability) is ready to be integrated into IN-CORE. Also, I learned some Python basics and I keep learning. I wonder if you could tell me how to start to integrate all of these data and do the analysis into IN CORE. If you have templates to read and analyze data it would be helpful. Also, is there a way to read 3D fragility. FYI, my fragility functions are based on raw data and not lognormally fitted.

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
 
### INCORE Lab and running analyses  
    
- *How do I empty cache in INCORE Lab?*

    Downloaded datasets in INCORE Lab are being cached for faster access later on. The data is stored in user's home 
    directory in folder `~/.incore/cache_data`. To delete content of the cache folder add following command in your Notebook:
    ```
        client = IncoreClient()
        client.clear_cache()
    ```

### Working with Jupyter Notebooks

-*How to access metadata of the loaded shapefiles inside the Jupyter Notebook?*
   
   A user can display all matadata associated with a shapefile by invoking inventory reader and running a loop 
   through **properties** key:
   ```
        # load shapefile dataset with building inventory
        bldg_dmg.load_remote_input_dataset("buildings", "5a284f0bc7d30d13bc081a28")
        bldg_dataset = bldg_dmg.input_datasets['buildings']['value']

        rdr = bldg_dataset.get_inventory_reader()
        for row in rdr:
            print(row['properties']['year_built'])
   ```



You can also post your questions at [https://opensource.ncsa.illinois.edu/confluence/display/INCORE1/questions/all](https://opensource.ncsa.illinois.edu/confluence/display/INCORE1/questions/all)

