# IN-CORE Jupyter Book documents

Main IN-Core documentation which is built using Python [Jupyter Book](https://jupyterbook.org/intro.html) package.

## Installation

Clone the code from INCORE docs [GitHub](https://github.com/IN-CORE/incore-docs.git) repository.

### Running directly in your environment

1. Install `jupyter-book` package.

2. We recommend using virtual environment `conda` with Python 3.6-3.8. The package management and deployment tool 
is called `miniconda` or `anaconda`. Create the environment from the terminal at the project 
folder (called `incore_docs` here) and activate it:
    
   ```
    conda create -n incore_docs python=3.8 anaconda
    source activate incore_docs
    ```
   
3. Use `conda` again for Jupyter book installation:

    ```
    conda install -c conda-forge jupyter-book
    ``` 

4. From the terminal at the project folder (**incore-docs/**) run: 
    ```
    jupyter-book build manual_jb
    ```
    after that you should be able to run (`clean` deletes content of the `build` folder) :
    ```
    jupyter-book clean manual_jb
    ```
5. Locate folder with html files (**incore-docs/_build**) and view **index.html** in a browser.

