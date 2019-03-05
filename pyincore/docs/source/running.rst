Running
=======

* Create a file called ``.incorepw``  with credentials; the first line contains your username and the second password. The information is used for communicating with pyincore services such as hazard, data and fragility. Move the file to the top-level folder of the pyincore package.

* Start local Jupyter notebook by running the following command at the Terminal (Mac/Linux) or Command Prompt (Windows) **from the top-level pyincore folder**:

  .. code-block:: bash

      jupyter notebook


  A message *The Jupyter Notebook is running* appears in the terminal/prompt and you should see the notebook open in your browser.
  Note that you will be asked to copy/paste a token into your browser when you connect for the first time.

* Verify the installation by running the **building damage analysis** in Jupyter. Navigate to the `buildingdamage.ipynb` file using Notebook's dashboard. The file is located in the analyses folder of the pyincore package (full path ``pyincore/analyses/buildingdamage/``). For details of running and manipulating ``ipynb`` files refer to `Jupyter documentation <https://jupyter.readthedocs.io/en/latest/running.html#running>`_.


  Additionally, a user can run Jupyter notebook interactively in NCSA's (`Incore Lab <https://incore-jupyter.ncsa.illinois.edu/hub/login>`_).


----

:doc:`Pyincore home <index>`