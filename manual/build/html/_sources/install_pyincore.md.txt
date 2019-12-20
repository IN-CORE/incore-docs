## Installation
 
These steps guides you on how to install both pyIncore and Jupyter Notebooks on **All platforms** so you can develop your code.

1. From the Terminal (Mac/Linux) or Command Prompt (Windows) add [conda-forge](https://conda-forge.org/) package repository/channel to your environment:
    ```
    conda config -add channels conda-forge
    ```

2. To install pyIncore, navigate to the directory you want to use for running Jupyter Notebooks and run the following command:
    ```
    conda install -c in-core pyincore
    ```

To check that the package is installed run `conda list` command.

Replace `install` command above with `update` to update pyIncore to the latest version that is compatible with all other packages in the environment.