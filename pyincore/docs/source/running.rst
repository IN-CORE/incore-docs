Running
=======

Testing pyIncore Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- For these instructions we assume that users develop their python script by using pyIncore in their own **project folder** (create folder if you don’t have one)

- Download the Jupyter Notebook file for **Building damage analysis** (`<https://incore2.ncsa.illinois.edu/doc/examples/buildingdamage.ipynb>`_) to your **project folder**. We will verify your installation of pyIncore by running this file.

Running locally
^^^^^^^^^^^^^^^

* Start a local **Jupyter notebook** by running the following command in the terminal or command prompt from your **project folder** (change directories to the particular project folder at the command prompt):

    .. code-block:: bash

        jupyter notebook


    or if Jupyter Notebook is not recognized in Anaconda:

    .. code-block:: bash

        python -m notebook


  A message *The Jupyter Notebook is running* appears in the terminal/prompt and you should see the notebook dashboard open in your browser.
  Note that you might be asked to copy/paste a URL into your browser when you connect for the first time.

* Click on the ``buildingdamage.ipynb`` in the Jupyter Notebook browser. Your web page should now show multiple cells of code

Right now you are not actually running a notebook yet. Running a cell means that you will execute the cell’s contents. To execute cells in order you can just select the first cell and click the **Run** button at the top.
Note that **Building damage** is a long running analysis and there is little indication that it's running except by either looking at the Jupyter Notebook file and seeing the [*] for the notebook cell where that block of code is being executed or by looking at the Task Manager in the Notebook dashboard to see there is a python process running. Alternatively, you can look at the Jupyter Notebook dashboard to see if the ``csv`` file with results has been created yet.

For details of running and manipulating ipynb files refer to `Jupyter documentation <https://jupyter.readthedocs.io/en/latest/running.html#running>`_.


Using IN-CORE Lab
^^^^^^^^^^^^^^^^^

A user can run Jupyter notebook interactively in NCSA's (`IN-CORE Lab <https://incore-lab.ncsa.illinois.edu>`_). IN-CORE Lab is a customized `Jupyter Lab <https://jupyterlab.readthedocs.io/en/stable/#>`_ for running and editing Notebooks.

- Login to IN-CORE Lab with you IN-CORE account info.

**Running Jupyter Notebook in IN-CORE Lab**

We described how to run Building damage Notebook locally. This section focuses on step-by-step instructions of running Notebooks on the IN-CORE Lab.

1. Create a credential file with IN-CORE username/password (same information you used to login to IN-CORE Lab) in order to use IN-CORE services. This is similar to the local authentication step except the authentication file ``.incorepw`` is being created on the IN-CORE Lab server running Linux OS:

    a. Open the terminal on IN-CORE lab Launcher page

    b. In the terminal, make sure you are in your HOME directory. Type:

        .. code-block:: bash

            pwd

        to see the current path and

        .. code-block:: bash

            cd ~

        to get into your home directory (``/home/<username>``).

    c. Create a hidden (therefore dot prefix) folder:

        .. code-block:: bash

            mkdir .incore

    d. Create a hidden credential file in the folder you just created and type IN-CORE username and password using for example nano text editor:

        .. code-block:: bash

            cd .incore
            nano .incorepw

    e. Save the file with ``Ctrl+O`` and ``Enter`` commands

    f. Close the text editor and return to your shell with ``Ctrl+X`` command

2. Upload the **Building Damage Notebook** from your local machine to IN-CORE lab by clicking the Upload icon in the left panel and select buildingdamage.ipybn.

3. The Notebook shows up in the left panel after a successful upload.

4. Double click to open the Notebook in the main area and run it. Instructions on how to run building damage analysis, please refer to previous section **Running a Building Damage Analysis**.


----

:doc:`pyIncore home <index>`
