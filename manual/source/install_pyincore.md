## Installation
 
These steps guides you on how to install both pyIncore and Jupyter Notebooks on **All platforms** so you can develop your code.

1. From the Terminal (Mac/Linux) or Command Prompt (Windows) add [conda-forge](https://conda-forge.org/) package repository/channel to your environment:
    ```
    conda config --add channels conda-forge
    ```

2. To install pyIncore, navigate to the directory you want to use for running Jupyter Notebooks and run the following command:
    ```
    conda install -c in-core pyincore
    ```
To check that the package is installed.  run 
```
conda list pyincore
```
or `conda list` for all packages currently installed. You can check if pyincore exists in the list.

To update pyIncore run 
```
conda update -c in-core pyincore
```
