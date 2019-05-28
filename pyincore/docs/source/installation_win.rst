Windows 64-bit installation
===========================

- `GDAL <https://www.gdal.org/>`_ - Geospatial Data Abstraction Library

    We provide installation instructions for Anaconda environment manager using `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_. The following instructions were tested for Windows 64-bit (The 32-bit has not been tested yet):

    1. Download the latest Miniconda3 installer for Windows from `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_ web page.

    2. Run the installer setup locally (select the *Just Me* choice) to avoid the need for administrator privileges.

    3. Leave the default folder path (``C:\Users\<user>\..\miniconda3``).

    4. Do not add Anaconda to the PATH. Do, however, register Anaconda as the default Python environment.

    5. Open up an Anaconda prompt from the Windows Start menu. The ``base`` environment is being activated and the prompt changes to: ``(base) C:\Users\<user>``:

    .. image:: images/win_prompt1.jpg
        :height: 324px
        :width: 346px
        :scale: 100 %
        :alt: Windows Menu
        :align: center

    |

    6. Create the python environment (``pyincore`` for example) and activate it (or stay in the ``base``):

        .. code-block:: bash

            conda create -n pyincore python=3
            conda activate pyincore

    7. Install dependency packages in the following order:

        .. code-block:: bash

            conda install rasterio
            conda install fiona
            conda install rtree

- **pyIncore package**

    These steps will guide you on how to install **pyIncore**.

    1. Download **pyIncore** (``pyincore_<version>.tar.gz``) as an archive file from `NCSA's server <https://incore2.ncsa.illinois.edu/>`_ to a directory on your computer.

    2. To install **pyIncore**, navigate to the directory you used on step 1 and:

        From the Anaconda prompt run:

        * If you are using a virtual environment, you will need to activate it if it has not been done yet.
        * Run the following command:

            .. code-block:: bash

                pip3 install --user pyincore_<version>.tar.gz

- **pyIncore credentials**

    The installation installs **pyIncore** and creates an ``.incore`` folder in your HOME directory to store cached files. A message *pyIncore credentials file has been created at <HOME directory>/.incore/.incorepw appears* in the prompt. The typical location of a HOME directory is ``C:\Users\<username>`` on Windows OS.

    1. Locate a file called **.incorepw** in the ``.incore`` folder in your HOME directory.
    2. Write your LDAP credentials in it; the first line contains your username and the second password. This information is used for communicating with IN-CORE web service.


----

`IN-CORE home <index.html>`_
