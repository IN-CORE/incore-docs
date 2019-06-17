Mac OS  installation
====================

- `GDAL <https://www.gdal.org/>`_ - Geospatial Data Abstraction Library

    Use `Homebrew <https://brew.sh/>`_, a MacOS package manager. If you don’t have Homebrew, please install it. Additional information about installing GDAL can be found at an `Install link <https://medium.com/@vascofernandes_13322/how-to-install-gdal-on-macos-6a76fb5e24a4>`_.

    1. Install **gdal**

        .. code-block:: bash

            brew install gdal

    2. Install **spatialindex** library

        .. code-block:: bash

            brew install spatialindex

    3. Also, update the ``pip`` Python package manager

        .. code-block:: bash

            pip3 install --upgrade pip

- **pyIncore package**

    These steps will guide you on how to install **pyIncore**.

    1. Download **pyIncore** (``pyincore_<version>.tar.gz``) as an archive file from `NCSA's server <https://incore2.ncsa.illinois.edu/>`_ to a directory on your computer.

    2. To install **pyIncore**, navigate to the directory you used on step 1 and:

        * If you are using a virtual environment, you will need to activate it if it has not been done yet.
        * Run the following command:

            .. code-block:: bash

                pip3 install --user pyincore_<version>.tar.gz

        * We use ``matplotlib`` library to create graphs. There is a Mac specific installation issue addressed at StackOverflow `link 1 <https://stackoverflow.com/questions/4130355/python-matplotlib-framework-under-macosx>`_ and `link 2 <https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python>`_. In a nutshell, insert line into ``~/.matplotlib/matplotlibrc`` file. **Note** You must create the file (``matplotlibrc``) if it does not exist:

            .. code-block:: bash

                backend : Agg


- **pyIncore credentials**

    The installation installs **pyIncore** and creates an ``.incore`` folder in your HOME directory to store cached files. A message *pyIncore credentials file has been created at <HOME directory>/.incore/.incorepw appears* in the prompt. The typical location of a HOME directory is ``/Users/<username>`` on Mac OS.

    **Note**: The folders and files starting with "." (dot prefix) are hidden in Operating systems with Unix roots. There are few ways (`link1 <https://nektony.com/how-to/show-hidden-files-on-mac>`_ and `link2 <https://macpaw.com/how-to/show-hidden-files-on-mac>`_) to view hidden files on your Mac.


    1. Locate a file called **.incorepw** in the ``.incore`` folder in your HOME directory.
    2. Write your LDAP credentials in it; the first line contains your username and the second password. This information is used for communicating with IN-CORE web service.


----

`IN-CORE home <index.html>`_






