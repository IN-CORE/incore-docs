# Quick Reference


1. A user must have an **IN-CORE** account. If you do not have it, see [IN-CORE Account](../account.md) section for setting one.
    <br />
    <br />
2. Install Miniconda or Anaconda virtual environment. Download the latest Miniconda3 installer from 
    the [Miniconda](https://docs.conda.io/en/latest/miniconda.html) web page or Anaconda3 installer from [Anaconda](https://www.anaconda.com/distribution/) page. 
    <br />
    <br />
3. From the Terminal (Mac/Linux) or Command Prompt (Windows) add [conda-forge](https://conda-forge.org/) package repository/channel to your environment:
    ```
    conda config --add channels conda-forge
    ```
   
4. Create the python environment (for this example we choose `pyincoreEnv`):
    ```
    conda create -n pyincoreEnv python=3.9
    ```
   
5. Activate the environment:
    ```
    conda activate pyincoreEnv
    ``` 
   
6. To install pyIncore, navigate to the directory you want to use for running Jupyter Notebooks and run the following command. This will install both, **pyIncore-viz** and **pyIncore** as a dependency.
    ```
    conda install -c in-core pyincore-viz
    ```

   If you have trouble installing pyincore and pyincore-viz or it is taking a long time to resolve the dependencies,
   try using the libmamba solver by running the following command:

    ```
    conda install -c in-core pyincore-viz --solver=libmamba
    ```

   If the installed pyincore or pyincore-viz version is not the latest or lower than the desired one, specify the version number in installation command.
    ```
    conda install -c in-core pyincore-viz=1.8.3 (or your version of choice)
    ```
   Version information for pyincore and pyincore-viz can be found in
    - https://anaconda.org/IN-CORE/pyincore
    - https://anaconda.org/IN-CORE/pyincore-viz
    
   
7. Install Jupyter Notebook. Jupyter Notebook is already installed with Anaconda distribution; it has to be installed separately in your virtual environment on Miniconda:
    ```
    conda install jupyter
    ```
