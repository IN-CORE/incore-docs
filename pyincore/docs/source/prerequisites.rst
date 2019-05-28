Prerequisites
=============

IN-CORE account

    * A user must have an account recognized by the **IN-CORE** service. Please `register <https://identity.ncsa.illinois.edu/register/UUMK36FU2M>`_, your credentials (Username and Password) will be required in later steps.

`Python 3.5+ <https://www.python.org/>`_

    * If you are on Windows, go to Windows 64 bit section under GDAL section.

    * It is common to have more than one Python version installed on your computer. Make sure you are running the correct version of Python (you can check by running ``python --version``) with corresponding path added to the PATH system variable. The following links will help you navigate through various installations guides:

        - https://realpython.com/installing-python/
        - https://docs.python-guide.org/#the-hitchhiker-s-guide-to-python
        - OS specific downloads: https://www.python.org/downloads/

    * We recommend that users get familiar with `virtual environments <https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv/>`_ or `environment manager <https://www.anaconda.com/distribution/>`_:

        - These are tools that help keep dependencies separate for different projects. If you decide, however, to use a virtual environment or manager you must do it now, in this prerequisite step.
        - Note that GDAL installation is global on Windows and Linux, even if you use virtual environments (see next step).

`GDAL <https://www.gdal.org/>`_ - Geospatial Data Abstraction Library

    **pyIncore** uses ``GDAL`` library which has to be installed separately. The followings are instruction for each operating system.

    * Linux
        Additional information can be found at the wiki page `How to install GDAL <https://github.com/domlysz/BlenderGIS/wiki/How-to-install-GDAL>`_.

        - Install **gdal-bin**

            .. code-block:: bash

                sudo apt-get install gdal-bin

        - Install **libspatialindex-dev**

            .. code-block:: bash

                apt-get install libspatialindex-dev

        - Also, update your Pip Python package manager

            .. code-block:: bash

                pip3 install --upgrade pip


    * Windows 64bit

        We provide installation instructions for `Anaconda <https://www.anaconda.com/distribution/>`_ environment manager using `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_. **Python 3.x** and **GDAL** library will be installed with Anaconda/Miniconda. The following instructions were tested for Win 64bit:

        - Download the latest Miniconda3 installer for Windows from `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_ web page.

        - Run the installer setup locally (select the *Just Me* choice) to avoid the need for administrator privileges.

        - Leave the default folder path (``C:\Users\<user>\..\miniconda3``).

        - Do not add Anaconda to the PATH. Do, however, register Anaconda as the default Python environment.

        - Open up an Anaconda prompt from the Windows Start menu.

        - Create Python environment (required for the ``pyincore`` example) and activate it.

            .. code-block:: bash

                conda create -n pyincore python=3
                conda activate pyincore

        - Install dependency packages in the following order:

            .. code-block:: bash

                conda install rasterio
                conda install fiona
                conda install rtree


    * MacOS

        Use `Homebrew <https://brew.sh/>`_, a MacOS package manager. If you don’t have Homebrew, please install it. Additional information about installing GDAL can be found at an `Install link <https://medium.com/@vascofernandes_13322/how-to-install-gdal-on-macos-6a76fb5e24a4>`_.

        - Install **gdal**

            .. code-block:: bash

                brew install gdal

        - Install **spatialindex** library

            .. code-block:: bash

                brew install spatialindex

        - Also, update the ``pip`` Python package manager

            .. code-block:: bash

                pip3 install --upgrade pip


`Jupyter <https://jupyter.org/>`_

    We recommend using Jupyter Notebook for running the **pyIncore** projects. It as an open-source application that allows you to create projects (documents) that contain live Python code, visualizations and documentation.

        - `Installing Jupyter <https://jupyter.org/install.html>`_ can be done again with ``pip`` (on Miniconda; in your virtual environment) or ``pip3`` as indicated below:

            .. code-block:: bash

                pip3 install jupyter

**Optional**: We recommend to use `virtual <https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv/>`_ environment
or environment `manager <https://www.anaconda.com/distribution/>`_; tools that help keep dependencies separate for different projects.


----

:doc:`pyIncore home <index>`
