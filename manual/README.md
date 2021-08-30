## IN-CORE documents

Main IN-Core documentation which is built using Python [Sphinx](http://www.sphinx-doc.org/en/master/) package.

### Installation

Clone the code from INCORE docs [git](https://opensource.ncsa.illinois.edu/bitbucket/scm/incore1/incore-docs.git) 
repository.

### Building and running Sphinx in Docker container

Install [Docker Desktop](https://www.docker.com/) for your OS and change directory to your local branch incore-docs/manual folder (one with Dockerfile).

1. Build container
    ```
    docker build -t doc_test .
    ```
    The container's name is **doc_test** in this example.
    
2. Run docker
    ```
    docker run --rm -p 80:80 --name doctest doc_test:latest
    ```
    Optional flag, `-name` sets container's name to **doctest** under which it appears in Docker Desktop.
   
3. Run html pages in your local browser (you might see the nginx main page first)
    ```
    http://localhost/doc/incore/
    ```  

### Running Sphinx directly in your environment

1. Install required packages. Currently `sphinx`, a Python package for building documentation and `sphinx_rtd_theme`, 
a theme used in this documentation and other packages. See section 4. for the full list.

2. We recommend using virtual environments, `conda` (preferred) or `virtualenv` for Python 3.6+. 
for managing Python environments.  
In case of `conda`, the package management and deployment tool 
is called `anaconda`. Create the environment from the terminal at the project 
folder (called `incore_docs` here) and activate it:
    ```
    conda create -n incore_docs python=3.7 anaconda
    source activate incore_docs
    ```
    or  
    ```
    virtualenv --python=python3.7 incore_docs
    source venv/bin/activate
    ```
   
3. Install required packages individually if necessary. Use `conda` again or you can also use `pip`. Packages `myst-parser` 
and `sphinx-markdown-tables` are for correct 
rendering of the tables and `nbsphinx` and `ipythony` installs extension that provides a source parser for Jupyter Notebook **ipynb files**:

    ```
    conda install sphinx
    conda install sphinx_rtd_theme
    conda install -c conda-forge myst-parser
    pip install sphinx-markdown-tables
    conda install -c conda-forge nbsphinx
    conda install -c conda-forge ipython
    ```
    or (global install for all users drop the --user flag)
    ```
    python3 -m pip install sphinx --user
    python3 -m pip install sphinx_rtd_theme --user
    python3 -m pip install myst-parser --user
    python3 -m pip install sphinx-markdown-tables --user
    python3 -m pip install nbsphinx --user
    python3 -m pip install IPython --user
    ```   

4. From the terminal at the project folder (**incore-docs/manual**) run: 
    ```
    sphinx-build -b html source build
    ```
    after that you should be able to run (`clean` deletes content of the `build` folder) :
    ```
    make clean
    make html
    ```
 
