#  Frequently asked questions

## IN-CORE

*   *I want to try your IN-CORE services. Do I need to register?*

    A user must have an account [registered](https://identity.ncsa.illinois.edu/register/BSKC2UKQPU) with NCSA IN-CORE service. User credentials are required 
    in accessing repositories such as hazard, fragility, restoration, geographic and other data sets. 
    They are also used for accessing documentation server and Jupyter Notebook files.

    The username/password you chose during registration process in IN-CORE system is called 
    LDAP password, based on specific Lightweight Directory Access Protocol authentication. 
    You can test your registration credentials by accessing the [documentation server](http://incore.ncsa.illinois.edu/).
    <br />
    <br />
    
*   *What does dfr3 (DFR3 service) refer to?*

    The acronym **dfr3** (DFR3) stands for **D**amage, **F**unctionality, **R**epair, **R**estoration and **R**ecovery. For example 
    fragility curves can be viewed in a Viewer which interacts with DFR3 service.
    

## pyIncore


*   *What’s the difference between Anaconda, conda, and Miniconda?*
    
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
    <br />
    <br />
    
*   *How do I check what version of Python and Anaconda are installed?*

    The versions can be checked by running `python --version` and/or `import sys;sys.executable` in Python console. If you have 
    already installed Anaconda you need to use conda, Anaconda’s package manager to check the version by running `conda list anaconda`.
    <br />
    <br />
    
*   *Anaconda/Miniconda downgraded my Python version.*

    Conda can downgrade Python to a lower version when it finds incompatible libraries in a specific environment. For example fresh conda 
    environment created with command `conda create -n pyincoreEnv python=3`
    
    installs latest Python version supported by Anaconda which gets downgraded to `3.7.x` with `pyincore` installation. This is an expected behavior which can be remedied 
    by using particular Python version
    ```
        conda create -n pyincoreEnv python=3.7
    ```
    General note for installing new packages or updating old ones, if you get notified that there will be downgrade or upgrade, 
    you might consider creating a new environment to preview the change.
    <br />
    <br />    
        
*   *I would like to use pip. I have Python 3 installed but the pip3 command does not work.*

    We prefer **conda** installation over **pip** mainly because it handles Python packages dependencies and even library outside of 
    the Python. Conda is a packaging tool and installer that handles library dependencies as well as the Python packages themselves. 
    User can install **pyIncore** with pip however some of the underlying libraries have to be installed separatelly and present globally (GDAL).
    In any case make sure you are running the correct version of Python (you can check by running `python3 --version`). Following links will help you navigate 
    through various installations; [Python 3 Installation & Setup Guide](https://realpython.com/installing-python/), 
    [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/#the-hitchhiker-s-guide-to-python), 
    OS specific [downloads](https://www.python.org/downloads/).
    
    
### Installing pyIncore

*   *How do I check the installed version of pyIncore?*

    In your conda virtual environment type `conda list` and the output is a list of all installed Python packages including **pyIncore**.
    <br />
    <br />
    
*   *How do I update pyIncore?*

    - Open a terminal window
    - Activate the environment where you installed pyIncore (for example, `conda activate pyincore`)
    - Run the following command: 
        ```
        conda update -c in-core pyincore
        ```
    <br />

*   *pyIncore update failed or pyIncore cannot be updated to the latest version.*

    - PyIncore update does not work for versions 0.5.3 and earlier. These versions were installed from 
    the NCSA conda private channel. Unfortunately, a user must delete the corresponding environment and re-install 
    pyIncore again from the official Anaconda `in-core` channel.
    - It is possible that there are dependency conflicts in your environment which prevent a further upgrade. Conda usually warns 
    very explicitly if they occur e.g. package X requires package Y version <5.0. We make sure that pyIncore works with 
    fresh environment and in this case we recommend re-installing pyIncore.
    <br />
       
*   *Should I use virtual environment for running the pyIncore?*

    We recommend using environment manager [Anaconda](https://www.anaconda.com/distribution/) 
    or [Miniconda](https://docs.conda.io/en/latest/miniconda.html); tools that help keep dependencies 
    separate for different Python projects. If you decide to use virtual environment or manager you must do it 
    at the beginning of the installation, in the prerequisite step. Some of the underlying libraries, 
    however have to be present globally (e.g. gdal on Windows OS). Therefore pyIncore installation 
    slightly differs for virtual environments and we will be happy to help you. Contact us at 
    <incore-dev@lists.illinois.edu>. 
    Note: Use Anaconda if you do not have full administrative privileges on your computer. It has been reported that 
    Jupyter Notebook can't be subsequently installed in Miniconda environment. With Anaconda **Jupyter Notebook** is already 
    pre-installed.
    

### Running pyIncore

*   *I am getting “Module not Found" when I run pyIncore* 

    This can be caused by many factors. You need to make sure the module is installed for your versions of Python.
    Run ``conda list`` to obtain the packages installed using conda in the active environment.
    <br />
    <br />
    
*   *I am trying to use building_dmg.ipynb on my computer but nothing happens.*

    We assume that you are running Jupyter Notebook in your browser. Run each individual cell 
    by clicking >|Run. The cursor (box) will highlight the next cell. The actual calculation is called 
    in the last cell with the `bldg_dmg.run_analysis()` command. When successful a Comma delimited 
    file (csv) appears in the Notebook and in the Jupyter tree under Files tab.
    <br />
    <br />
    
*   *Can I use files locally?*

    Yes. Users can use datasets stored on their local computers. It is, however not possible to use certain resources such as dfr3 curves locally.
    These have to be uploaded to the IN-CORE services. For details see [Tutorials](tutorials) section of this documentation.
    <br />
    <br />
    
*   *I cannot install/update Jypyter Notebook. I encountered a* **EnvironmentNotWritableError** *while installing Jypyter Notebook.*

    This error has been reported if you 1) use Miniconda and 2) do not have full administrative privileges on your computer. 
    Jupyter Notebook is not included in Miniconda and it has to be installed separately. The Environment error reflects lack of installation 
    privileges causes. Remove Miniconda and install **Anaconda** instead. The latter comes with pre-installed Jupyter Notebook.
    <br />
    <br />
    
*   *I do not have full administrative privileges to my School/Company issued computer. The pyIncore or Jupyter Notebook does not work.*

    Check what version of Python (3.6-3.8) and Miniconda/Anaconda are installed. Try to install Anaconda rather than Miniconda. 
    If none of the above helps contact your System administrator and Contact us at <incore-dev@lists.illinois.edu>.
    <br />
    <br />
    
*   *How do I empty pyIncore's local cache?*

    The installation of pyIncore creates an **.incore** folder in your HOME directory to store cached files. The typical location 
    of a HOME directory is `C:\Users\<username>` on WindowsOS, `/Users/<username>` on MacOS and `/home/<username>` on Linux based 
    machines. Locate the folder in your HOME directory and delete the content of `cache_data` sub-folder.
    
    **Note**: The folders and files starting with "." (dot prefix) are hidden in Operating systems with Unix roots. 
    There are few ways ([link1](https://nektony.com/how-to/show-hidden-files-on-mac) 
    and [link2](https://macpaw.com/how-to/show-hidden-files-on-mac)) to view hidden files on your Mac. 
    You can also use a command line tool to locate home directory and hidden files:
    Open the Terminal application from Launchpad and use following commands 1) to change the current working directory to your **home** directory,
    2) get the full path of Present Working Directory (pwd) on your OS and 3) list all files including the hidden ones.
    ```
    1) cd ~
    2) pwd
    3) ls -a
    ```


## Creating and running analyses

*   *What is a mapping and how do I create one?*

    We use mapping to associate each element of a given set such as Building inventory with one or more 
    elements of a second set of Fragility curves. For details see [Tutorials](tutorials) section of this documentation.
    <br />
    <br />

*   *Is mapping related to a map?*

    We use noun mapping for *operation that associates each element of a given set with one or more elements 
    of a second set*. In *IN-CORE* and *pyIncore* specifically, for example a Building inventory (given set) 
    is mapped to a (second) set of Fragility curves.
    <br />
    <br />
    
*   *What is dataset_id and how do I create it?*

    Each set being it a data, mapping, inventory, fragility or restoration set in IN-CORE system 
    has assigned ID, an identifier, which uniquely identifies it for the services and *pyIncore*. The unique ID 
    is assigned when the set is uploaded to the IN-CORE services. For details how to do it see technical 
    documentation or contact us at <incore-dev@lists.illinois.edu>.
    <br />
    <br />

*   *How do I upload files to IN-CORE datasets service?*

    There are two ways of importing files such as inventory datasets to IN-CORE service. The first uses Python script calling 
    **pyIncore* for file upload, and the second describes how to use a web application (Postmen, RESTer) to send POST 
    request with "attached" files directly to the service. For details see [Tutorials](tutorials).
    <br />
    <br />   
    
*   *Can I create and use my own earthquakes? I used an earthquake from hazard service for my analysis but I need different intensities. Do I need to upload simulated earthquakes to hazard service and then use it?*

    Earthquakes and other hazards can be defined in various ways, there are data based earthquakes that actually require user to 
    provide the shapefiles in order to create an earthquake or tehre are simulated earthquakes. Yes, you can define your own simulated earthquake 
    by creating the (hazard) json file through [pyIncore](https://github.com/IN-CORE/pyincore/blob/main/tests/pyincore/test_hazardservice.py#L117), 
    similar to the one provided in the [example](https://github.com/IN-CORE/pyincore/blob/main/tests/data/eq-model.json). 
    Currently you either run that pyincore method do need to upload your file to hazard service. For additional information 
    see IN-CORE [wiki](https://opensource.ncsa.illinois.edu/confluence/display/INCORE1/questions/all) page.
    <br />
    <br />

*   *Is Geopandas (package x) part of pyIncore?*

    The full set of Python packages available in *pyIncore* is listed in the *setup.py* file. The basic set of 
    packages is as follows: `fiona`, `jsonpickle`, `matplotlib`, `networkx`, `numpy`, `owslib`, 
    `pandas`, `geopandas`, `plotly`, `pyproj`, `pyyaml`, `rasterio`, `requests`, `rtree`, `scipy`, `shapely`, `wntr`, 
    `seaborn`, `pyomo`. We are currently working on creating visualization package so some packages such as 
    `ipyleaflet`, `matplotlib`, `plotly` will be removed from future version of **pyIncore** core and they will 
    be moved to **pyIncore viz**.
    <br />
    <br />    
    
*   *What is the best Image processing library for Python.*

    The most common Image manipulation and processing packages are [Pillow](https://pillow.readthedocs.io/en/stable/) 
    which is a continuation of the PIL (Python Imaging Library), [scikit-image](https://scikit-image.org/), 
    a collection of algorithms for image processing, 
    [scipy](https://docs.scipy.org/doc/scipy/reference/) which is already a dependency 
    of *pyIncore* and which provides a various image processing functions that can be operated with arrays 
    of any dimensionality.   
    <br />

*   *My tornado analysis is returning 0 for each inventory. When I put them together in QGIS, I can see that 
   the inventories fall within the tornado’s path.*

    The dataset is probably using different projection than WGS84. QGIS converts the projections behind the scene 
    putting the inventory and tornado paths in the same place.  
    <br />
    
*   *Warning: Boto3 is not present.*

    Boto3 is a package for connectivity with Amazon AWS. **pyIncore** does not use it however the warning comes 
    from the package build. We beleive that certain combination of conda channels causes the warning to appear. 
    A user can ignore the warning or additionally install **boto3**.
 
 
## INCORE Lab and running analyses  
    
*   *How do I empty cache in INCORE Lab?*

    Downloaded datasets in INCORE Lab are being cached for faster access later on. The data is stored in user's home 
    directory in folder `~/.incore/cache_data`. To delete content of the cache folder add following command in your Notebook:
    ```
    client = IncoreClient()
    client.clear_cache()
    ```

## Working with Jupyter Notebooks

*   *Can I see information, tags, columns associated with an infrastructure inventory file? How do I access metadata of the loaded shapefiles inside the Jupyter Notebook?*
   
    A user can display information data (matadata) columns associated with a shapefile by invoking Python inventory reader 
    to show what columns are available in the **properties**, and running a loop through a key (`year_built` here):
    ```
    # load shapefile dataset with building inventory
    bldg_dmg.load_remote_input_dataset("buildings", "5a284f0bc7d30d13bc081a28")
    bldg_dataset = bldg_dmg.input_datasets['buildings']['value']

    rdr = bldg_dataset.get_inventory_reader()

    print(rdr[0]['properties'].keys())
    for row in rdr:
        print(row['properties']['year_built'])
    ```


You can also post your questions 
at [https://opensource.ncsa.illinois.edu/confluence/display/INCORE1/questions/all](https://opensource.ncsa.illinois.edu/confluence/display/INCORE1/questions/all)

