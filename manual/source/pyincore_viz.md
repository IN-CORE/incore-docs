## pyIncore viz

Visualization package associated with pyIncore is called **pyIncore-viz**. It contains Python packages 
required for visualizing and disseminating the IN-CORE results, mainly via the Jupyter Notebooks.
 
### Prerequisites

- **pyIncore**: A user must have a pyIncore package installed. See [pyIncore section](pyincore) for details.

- **Virtual environment**: We recommend that users work with virtual environment managers called [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

- Mac OS specific notes: There is a Mac specific `matplotlib` installation issue addressed 
  at StackOverflow [link 1](https://stackoverflow.com/questions/4130355/python-matplotlib-framework-under-macosx) and [link 2](https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python). In a nutshell, insert line:
    ```
        backend : Agg
    ```
    
    into `~/.matplotlib/matplotlibrc` file. You must create the file (`matplotlibrc`) if it does not exist.

### Installation

1. To install pyIncore-viz, navigate to the directory you want to use for running Jupyter Notebooks and run the following command:
    ```
    conda install -c in-core pyincore-viz
    ```
   
   For update replace `install` with `update`.
   
2. To check that the package is installed run 
    ```
    conda list
    ```
    It will again list all packages currently installed. You can check if pyincore-viz exists in the list.
