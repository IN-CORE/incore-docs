##  Frequently asked questions

### IN-CORE account

- *I want to try your IN-CORE services. Do I need to register?*

    A user must have an account [registered](https://identity.ncsa.illinois.edu/register/UUMK36FU2M) with NCSA IN-CORE service. User credentials are required 
    in accessing repositories with hazard, fragility, restoration, geographic and other data sets. 
    They are also used for accessing documentation server and Jupyter notebook files.

    The username/password you chose during registration process in NCSA IN-CORE system is called 
    LDAP password, based on specific Lightweight Directory Access Protocol authentication. 
    You can test your registration credentials by accessing the [documentation server](http://incore2.ncsa.illinois.edu/docs).

### pyIncore

- *What is pyIncore? How is it different from pyincore?*

    **pyIncore** is a Python module that can be used to develop scientific hazard analysis and algorithm. 
    We recommend using Jupyter notebook for running the pyIncore projects, either locally or in 
    NCSA's [IN-CORE Lab](https://incore-lab.ncsa.illinois.edu/).

    **Insatalling pyincore**
    
- *Should I use virtual environment for running the pyIncore?*

    We recommend using environment manager [Anaconda](https://www.anaconda.com/distribution/) 
    or [Miniconda](https://docs.conda.io/en/latest/miniconda.html); tools that help keep dependencies 
    separate for different Python projects. If you decide to use virtual environment or manager you must do it 
    at the beginning of the installation, in the prerequisite step. Some of the underlying libraries, 
    however have to be present globally (e.g. gdal on Windows OS). Therefore pyIncore installation 
    slightly differs for virtual environments and we will be happy to help you. Contact us at 
    incore-dev@lists.illinois.edu.

- *I have Python 3 installed but pip3 command does not work.*

    Try installing additional packages via `conda`, use `pip` only if conda installer is not avilable. 
    All required Python packages should be installed or updated using `conda install pyincore` or `conda update pyincore`.
    If you still need `pip3` command make sure you are running the correct version of Python (you can check 
    by running `python3 --version`) with corresponding path added to the PATH system variable. 
    Following links will help you navigate 
    through various installations; [Python 3 Installation & Setup Guide](https://realpython.com/installing-python/), 
    [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org/#the-hitchhiker-s-guide-to-python), 
    OS specific [downloads](https://www.python.org/downloads/).

    **Running pyincore**

- *I am trying to run buildingdamage.ipynb on my computer but nothing happens.*

    We assume that you are running Jupyter Notebook in your browser. Run each individual cell 
    by clicking >|Run. The cursor (box) will highlight the next cell. The actual calculation is called 
    in the last cell with the `bldg_dmg.run_analysis()` command. When successful a Comma delimited 
    file (csv) appears in the Notebook and in the Jupyter tree under Files tab.