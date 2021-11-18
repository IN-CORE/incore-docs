# IN-CORE Jupyter Book documents

Main IN-Core documentation which is built using Python [Jupyter Book](https://jupyterbook.org/intro.html) package.

## Installation

Clone the code from INCORE docs [GitHub](https://github.com/IN-CORE/incore-docs.git) repository.

### Running directly in your environment

1. Install `jupyter-book` package.

2. We recommend using virtual environments, `conda` (preferred) or `virtualenv` for Python 3.6-3.8. 
for managing Python environments.  
In case of `conda`, the package management and deployment tool 
is called `anaconda`. Create the environment from the terminal at the project 
folder (called `incore_docs` here) and activate it:
    ```
    conda create -n incore_docs python=3.8 anaconda
    source activate incore_docs
    ```
    or  
    ```
    virtualenv --python=python3.8 incore_docs
    source venv/bin/activate
    ```
   
3. Use `conda` again or you can also use `pip`:

    ```
    conda install -c conda-forge jupyter-book
    ```
    or
    ```
    python3 -m pip install -U jupyter-book
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

 
