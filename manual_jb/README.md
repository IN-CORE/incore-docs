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

4. From the terminal at the project folder (**incore-docs/manual_jb**) run: 
    ```
    jupyter-book build content
    ```
    after that you should be able to run (`clean` deletes content of the `build` folder) :
    ```
    jupyter-book clean content
    ```
5. Locate folder with html files (**incore-docs/content/_build**) and view **index.html** in a browser.


## Building and running Jupyter Book in Docker container

Install [Docker Desktop](https://www.docker.com/) for your OS and change directory to your local branch 
incore-docs/manual_jb folder (one with Dockerfile).

1. Build container
   ```
   docker build -t doc_test .
   ```
   or for fresh build
   ```
   docker build --no-cache -t doc_test .
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
