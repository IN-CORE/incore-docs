Prerequisites
=============

A user must have an account recognized by the **Incore** service. Please `register <https://identity.ncsa.illinois.edu/register/UUMK36FU2M>`_ and use your credentials later on.

`Python 3.5 <https://www.python.org/>`_ or greater

`GDAL <www.gdal.org/>`_ - Geospatial Data Abstraction Library

* Linux

    **Pyincore** uses GDAL library which has to be installed separately for example by using ``apt-get`` package utility
    on Debian, Ubuntu, and related Linux distributions.

    .. code-block:: bash

        apt-get gdal


    Additonal information can be found  at the wiki page `How to install GDAL <https://github.com/domlysz/BlenderGIS/wiki/How-to-install-GDAL>`_.

* Windows

    GDAL for Windows can be difficult to build, requiring a number of prerequisite software, libraries, and header files.
    If you are comfortable building Windows software then building GDAL from source as a develop build is preferred.

    If you are not comfortable building GDAL then you may want to download the ``gdal`` binaries
    from `Windows Binaries for Python <https://www.lfd.uci.edu/~gohlke/pythonlibs/>`_.
    The problem with this is that GDAL header files
    are not included, so you cannot do a ``pip install`` of packages that want to utilize
    the GDAL headers. Fiona and Rasterio will need binaries installed from this page as well,
    and if you run into failed dependancies during the setup process you may want to revisit
    the page and install the binaries for the Python extensions that are causing problems.
    Additional information can be found at the wiki page `How to install GDAL <https://github.com/domlysz/BlenderGIS/wiki/How-to-install-GDAL>`_.


**Optional**: A `virtual environment <[virtual environment](https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv/)>`_, a tool that helps to keep dependencies required by different projects separate
by creating isolated Python virtual environments for them. A module named ``virtualenv`` is available by running ``pip3 install virtualenv``
(``pip3`` command is pip for Python3, you could also run ``pip3 install --upgrade pip`` first), or an environment manager called `Anaconda <https://www.anaconda.com/distribution/>`_ by downloading OS specific `installer <https://docs.anaconda.com/anaconda/install/>`_.
Note that a full Anaconda distribution will include Python (and a collection of over 1,500+ open source packages), so installing Python first isn't needed if you use Anaconda.

`Jupyter <https://jupyter.org/>`_ notebook

We recommend using Jupyter notebook for running the **pyincore** projects. It as an open-source application that allows you to create projects (documents) that contain live Python code, visualizations and documentation.
`Installing Jupyter <https://jupyter.org/install.html>`_ can be done again with pip by running ``pip3 install jupyter``.
With **Anaconda** you already have installed Jupyter notebook.

----

:doc:`Pyincore home <index>`