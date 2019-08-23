IN-CORE Lab
===========

.. image:: images/juplab_login.jpg
    :height: 118px
    :width: 164px
    :scale: 100%
    :alt: IN-CORE Lab login.
    :align: right

A user can run and edit Jupyter Notebooks interactively in NCSA's IN-CORE Lab running at https://incore-lab.ncsa.illinois.edu. The IN-CORE Lab is a customized `Jupyter Lab <https://jupyterlab.readthedocs.io/en/stable/#>`_ with **pyIncore** installed on the server running Linux OS.

Login to IN-CORE Lab with your IN-CORE `account <account.html>`_ info.


.. image:: images/juplab0.jpg
    :height: 256px
    :width: 610px
    :scale: 100%
    :alt: Default IN-CORE Lab dashboard tab.
    :align: center


Authentication
^^^^^^^^^^^^^^

Create a credential file with IN-CORE username/password (same information you used to login to IN-CORE Lab) in order to use IN-CORE services. This is similar to the local authentication step except the authentication file ``.incorepw`` is being created on the server:

1. Open the terminal on IN-CORE lab Launcher page (arrow):

.. image:: images/juplab0_terminal.jpg
    :height: 256px
    :width: 610px
    :scale: 100%
    :alt: IN-CORE Lab launcher page.
    :align: center

2. In the terminal, make sure you are in your HOME directory. Type ``pwd`` to see the current path and ``cd ~`` to get into your home directory (``/home/<username>``).

3. Create a hidden (therefore dot prefix) folder using ``mkdir .incore`` command.

.. image:: images/nano_usr_pswd.jpg
    :height: 160px
    :width: 300px
    :scale: 75%
    :alt: Nano text editor.
    :align: right

4. Create a hidden credential file in the folder you just created (``cd .incore`` followed by ``nano .incorepw``) and type IN-CORE username and password using `Nano <https://www.howtogeek.com/howto/42980/the-beginners-guide-to-nano-the-linux-command-line-text-editor/>`_, the Linux command-line text editor. nano text editor. Write your username in the first line and the password in the second:

5. Save the file with ``Ctrl+O`` and ``Enter`` commands

6. Close the text editor and return to your shell with ``Ctrl+X`` command

A chain of terminal commands 2) through 4) above.

.. code-block:: bash

    pwd
    cd ~
    ($/home/<username>)
    mkdir .incore
    cd .incore
    nano .incorepw


Running Notebook in the Lab
^^^^^^^^^^^^^^^^^^^^^^^^^^^

In `Running Notebook locally <running.html>`_ section we described how to run Building damage Notebook locally. The following section focuses on **step-by-step instructions** of running Notebooks on the IN-CORE Lab.

1. Create a credential file with IN-CORE username/password if you haven't done it yet. See `IN-CORE Lab`_ section.

2. Upload the Building Damage Analysis notebook from your local machine to IN-CORE lab by clicking the ``Upload`` icon in the left panel and select **buildingdamage.ipybn**.

.. image:: images/juplab9_nbook.jpg
    :height: 256px
    :width: 610px
    :scale: 100%
    :alt: IN-CORE Lab upload panel.
    :align: center

3. The Notebook shows up in the left panel after a successful upload.

4. Double click to open the Notebook in the main area and run it. Instructions on how to run a **Building Damage Analysis**, please refer to previous section `Running Notebook locally <running.html>`_.

.. image:: images/juplab9_run_nbook.jpg
    :height: 256px
    :width: 610px
    :scale: 100%
    :alt: Building damage Jupyter notebook cells in IN-CORE Lab.
    :align: center

Accessing IN-CORE Web Tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section shows how to access `IN-CORE Web Tools <incore_webtools.html>`_ on IN-CORE Lab. The IN-CORE Lab is a customized Jupyter Lab with ``INCORE Login`` button in the main window and two IN-CORE-related menus, ``INCORE apps`` and ``INCORE docs``.

.. image:: images/juplab0_arrows.jpg
    :height: 256px
    :width: 610px
    :scale: 100%
    :alt: IN-CORE Lab with custom icon and menus.
    :align: center

1. Click on ``INCORE Login`` button in the main window. For login use the same username and password.

.. image:: images/juplab1.jpg
    :height: 256px
    :width: 610px
    :scale: 100%
    :alt: Web Tools on the IN-CORE Lab login.
    :align: center

2. This login process generates a file named **user.json**. It appears in the **File list manager** on the left side. The file contains an authentication token required for development of new analyses using IN-CORE’s Application programming interface (`API <https://en.wikipedia.org/wiki/Application_programming_interface>`_).

.. image:: images/juplab2.jpg
    :height: 256px
    :width: 610px
    :scale: 100%
    :alt: Web Tools on the IN-CORE Lab token file.
    :align: center

.. image:: images/juplab2_json.jpg
    :height: 116px
    :width: 610px
    :scale: 100%
    :alt: Web Tools on the IN-CORE Lab, details of the token file.
    :align: center

3. Fragility, Data and Hazard Explorers under ``INCORE apps`` menu become enabled after pressing ``LOGIN`` button AND reloading the current page in the browser. **NOTE**: A user must reload the whole Jupyter dashboard page (above) using the ``Reload`` button of the browser, not the Refresh File List (part of Jupyter’s file navigation) otherwise a following Warning appears:

.. image:: images/juplab3_no_reload.jpg
    :height: 256px
    :width: 610px
    :scale: 100%
    :alt: Web Tools on the IN-CORE Lab warning.
    :align: center

The `IN-CORE Web Tools <incore_webtools.html>`_ Viewers become part of INCORE Lab as shown below for Fragility viewer..

.. image:: images/juplab4_fragility.jpg
    :height: 362px
    :width: 610px
    :scale: 100%
    :alt: Fragility viewer on the IN-CORE Lab.
    :align: center


IN-CORE documentation
^^^^^^^^^^^^^^^^^^^^^

For ease of access - documentation is easily accessible from IN-CORE Lab.

The second IN-CORE menu, ``INCORE docs`` allows user to see **pyIncore** documentation and API endpoints definitions for accessing Fragility, Data and Hazard server(s).

.. image:: images/juplab5_doc.jpg
    :height: 362px
    :width: 610px
    :scale: 100%
    :alt: pyIncore documentation on the IN-CORE Lab.
    :align: center

.. image:: images/juplab8_swagger.jpg
    :height: 362px
    :width: 610px
    :scale: 100%
    :alt: API viewer on the IN-CORE Lab with endpoint definitions.
    :align: center



----

`IN-CORE home <index.html>`_
