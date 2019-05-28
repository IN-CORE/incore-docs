Installation
============

All Platforms
-------------

These steps will guide you on how to install **pyIncore**.

1. Download **pyIncore** (``pyincore_0.3.0.tar.gz``) as an archive file from `NCSA's server <https://incore2.ncsa.illinois.edu/>`_ to a directory on your computer.

2. To install **pyIncore**, navigate to the directory you used on step 1 and:

    * From the Terminal (Mac/Linux) run:

        .. code-block:: bash

            pip3 install --user pyincore_0.3.0.tar.gz


    Note: If you are using a virtual environment, you will need to activate it and then run the installation command.

    * From the Anaconda prompt (Windows):

        a. Activate the ``pyincore`` environment created on the Prerequisite section

            .. code-block:: bash

                conda activate pyincore


        b. Run the following command:

            .. code-block:: bash

                pip install --user pyincore_0.3.0.tar.gz


3. The installation installs **pyIncore** and creates a ``.incore`` folder in your HOME directory to store cached files. A message *pyIncore credentials file has been created at <HOME directory>/.incore/.incorepw* appears in the terminal/prompt. The typical location of a HOME directory is

    - ``C:\Users\<username>`` on Windows OS
    - ``/Users/<username>`` on MacOS
    - ``/home/<username>`` on Linux based machines


**Linux specific notes**

* If you see following error, make sure that you installed ``libspatialindex-dev`` (see GDAL section above):

    .. code-block:: bash

        OSError: Could not find libspatialindex_c library file


**MacOS specific notes**

* We use ``matplotlib`` library to create graphs. There is a Mac specific installation issue addressed at StackOverflow `link1 <https://stackoverflow.com/questions/4130355/python-matplotlib-framework-under-macosx>`_ and `link2 <https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python>`_. In a nutshell, insert line:

    .. code-block:: bash

        backend : Agg


into ``~/.matplotlib/matplotlibrc`` file.

**Add credentials to .incorepw file**

Locate a file called ``.incorepw`` in your HOME directory and write your LDAP credentials in it; the first line contains your username and the second password.

* This information is used for communicating with IN-CORE web service.

* The file is located in the ``.incore`` folder created during installation in your HOME directory.

* The typical path is ``C:\Users\<username>`` on Windows OS, ``/Users/<username>`` on MacOS and ``/home/<username>`` on Linux based machines.


----

:doc:`pyIncore home <index>`
