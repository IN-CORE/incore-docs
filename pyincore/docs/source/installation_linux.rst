Linux  installation
===================

- `GDAL <https://www.gdal.org/>`_ - Geospatial Data Abstraction Library

    Additional information can be found at the wiki page `How to install GDAL <https://github.com/domlysz/BlenderGIS/wiki/How-to-install-GDAL>`_.

    1. Install **gdal-bin**

        .. code-block:: bash

            sudo apt-get install gdal-bin

    2. Install **libspatialindex-dev**

        .. code-block:: bash

            apt-get install libspatialindex-dev

    3. Also, update your Pip Python package manager

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

        * If you see the *OSError: Could not find libspatialindex_c library file* error, make sure that you installed ``libspatialindex-dev`` (see GDAL section above):


- **pyIncore credentials**

    The installation installs **pyIncore** and creates an ``.incore`` folder in your HOME directory to store cached files. A message *pyIncore credentials file has been created at <HOME directory>/.incore/.incorepw appears* in the prompt. The typical location of a HOME directory is ``/home/<username>`` on Linux based machines.

    **Note**: The folders and files starting with "." (dot prefix) are hidden in Operating systems with Unix roots. There are few ways (`link 1 <https://nektony.com/how-to/show-hidden-files-on-mac>`_ and `link 2 <https://macpaw.com/how-to/show-hidden-files-on-mac>`_) to view hidden files on your Mac.


    1. Locate a file called **.incorepw** in the ``.incore`` folder in your HOME directory.
    2. Write your LDAP credentials in it; the first line contains your username and the second password. This information is used for communicating with IN-CORE web service.

----

`IN-CORE home <index.html>`_
