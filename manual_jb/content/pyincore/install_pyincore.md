# Installation
 
These steps guides you on how to install both pyIncore and Jupyter Notebooks on **All platforms** so you can develop your code.

1. From the Terminal (Mac/Linux) or Command Prompt (Windows) add [conda-forge](https://conda-forge.org/) package repository/channel to your environment:
    ```
    conda config --add channels conda-forge
    ```

2. To install pyIncore, navigate to the directory you want to use for running Jupyter Notebooks and run the following command:
    ```
    conda install -c in-core pyincore
    ```
   A user can also install **pyIncore-viz** module for which **pyIncore** installs as a dependency:
    ```
    conda install -c in-core pyincore-viz
    ```
   If the installed pyincore version is not the latest or lower than the desired one, specify the version number in installation command.
    ```
    conda install -c in-core pyincore=1.5.0 (or your version of choice)
    ```
   Version information for pyincore and pyincore-viz can be found in
   - https://anaconda.org/IN-CORE/pyincore
   

To check that the package is installed run 
```
conda list pyincore
```
or `conda list` for all packages currently installed. You can check if pyincore exists in the list.

To update pyIncore run 
```
conda update -c in-core pyincore
```
