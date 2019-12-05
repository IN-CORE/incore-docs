# IN-CORE documents

Main IN-Core documentation which is built using Python [Sphinx](http://www.sphinx-doc.org/en/master/) package.

# Installation

1. Clone the code from INCORE docs [git](https://opensource.ncsa.illinois.edu/bitbucket/scm/incore1/incore-docs.git) 
repository.
2. Install required packages. Currently `sphinx`, a Python package for building documentation and `sphinx_rtd_theme`, 
a theme used in this documentation. 
3. We recommend using virtual environments, `conda` (preferred) or `virtualenv` for Python 3.6+. 
for managing Python environments.  
In case of `conda`, the package management and deployment tool 
is called `anaconda`. Create the environment from the terminal at the project 
folder (called `incore_docs` here) and activate it:

    ```
    conda create -n incore_docs python=3.6 anaconda
    source activate incore_docs
    ```
    or  
    ```
    virtualenv --python=python3.6 incore_docs
    source venv/bin/activate
    ```
4. Install required packages individually if necessary. use `conda` again or  
you can also use `pip` for installing packages:

    ```
    conda install sphinx
    conda install sphinx_rtd_theme
    conda install recommonmark
    pip install sphinx-markdown-tables
    ```
    or
    ```
    pip install sphinx
    pip install sphinx_rtd_theme
    pip install recommonmark
    pip install sphinx-markdown-tables
    ```   

# Running

From the terminal at the project folder (incore-docs/incore-docs) run: 

```
sphinx-build -b html source build
```

after that you should be able to run (`clean` deletes content of the `build` folder) :

```
make clean
make html
```
            
# Testing
    NA
