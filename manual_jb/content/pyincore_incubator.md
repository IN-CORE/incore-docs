# pyIncore Incubator

**pyIncore-incubator** is a component of IN-CORE that allows users to extend
the core set of analyses provided by pyincore. New analyses in
pyincore-incubator extend the pyincore BaseAnalysis class and can be chained
with existing pyincore analyses to add new functionality. The incubator gives
the community around the IN-CORE project a forum and set of resources for
innovation and investigation of new ideas and alternative ideas.

## Features
1. Example analysis showing how to extend pyincore functionality
 
## Prerequisites

- **pyIncore**: A user must have pyIncore package installed. See [pyIncore section](pyincore) for details.

- **Virtual environment**: We recommend that users work with virtual environment managers called [Anaconda](https://www.anaconda.com/) 
or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

- Mac OS specific notes: There is a Mac specific `matplotlib` installation issue addressed 
  at StackOverflow [link 1](https://stackoverflow.com/questions/4130355/python-matplotlib-framework-under-macosx) and [link 2](https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python). In a nutshell, insert line:
    ```
        backend : Agg
    ```
    
    into `~/.matplotlib/matplotlibrc` file. You must create the file (`matplotlibrc`) if it does not exist.

## Installation

1. To install pyIncore-incubator, navigate to the directory you want to use for running Jupyter Notebooks and run the 
   following command:
    ```
    conda install -c in-core pyincore-incubator
    ```
   If you have trouble installing pyincore-incubator or it is taking a long time to resolve the dependencies, try 
   using the libmamba solver by running the following command:

    ```
    conda install -c in-core pyincore-incubator --solver=libmamba
    ```

   If the installed pyincore-incubator version is not the latest or lower than the desired one, specify the version 
   number in installation command.
    ```
    conda install -c in-core pyincore-incubator=0.1.0 (or your version of choice)
    ```
   Version information for pyincore-incubator can be found in
    - [https://anaconda.org/IN-CORE/pyincore-incubator](https://anaconda.org/IN-CORE/pyincore-incubator)
    
   For update replace `install` with `update`.

   
2. To check that the package is installed run 
    ```
    conda list
    ```
   It will again list all packages currently installed. You can check if **pyincore** and **pyincore-incubator** 
   exist in the list.

## Examples

Below are a few example Jupyter notebooks of community contributions to IN-CORE. 

Examples: <br />
