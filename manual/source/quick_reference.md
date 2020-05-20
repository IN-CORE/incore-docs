## Quick reference


1. A user must have an **IN-CORE** account. If you do not have it, see [IN-CORE Account](account) section for setting one.
    <br />
    <br />
2. Install Miniconda or Anaconda virtual environment. Download the latest Miniconda3 installer for Windows from 
    the [Miniconda](https://docs.conda.io/en/latest/miniconda.html) web page or Anaconda3 installer from [Anaconda](https://www.anaconda.com/distribution/) page. 
    <br />
    <br />
3. From the Terminal (Mac/Linux) or Command Prompt (Windows) add [conda-forge](https://conda-forge.org/) package repository/channel to your environment:
    ```
    conda config --add channels conda-forge
    ```
   
4. Create the python environment (for this example we choose `pyincoreEnv`) and activate it:
    ```
    conda create -n pyincoreEnv python=3.7
    conda activate pyincoreEnv
    ```
  
5. To install pyIncore, navigate to the directory you want to use for running Jupyter Notebooks and run the following command:
    ```
    conda install -c in-core pyincore
    ```
6. Install Jupyter Notebook. Jupyter Notebook is already installed with Anaconda distribution; it has to be installed separately in your virtual environment on Miniconda:
    ```
    conda install jupyter
    ```
