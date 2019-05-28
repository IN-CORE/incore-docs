Prerequisites
=============

- **IN-CORE account**
    A user must have an **IN-CORE** account. If you don’t have an account, see IN-CORE `account <account.html>`_ section.

- `Python 3.5+ <https://www.python.org/>`_
    It is common to have more than one Python version installed on your computer. Make sure you are running the correct version of Python (you can check by running ``python --version``) with corresponding path added to the PATH system variable. The following links will help you navigate through various installations guides:

    - https://realpython.com/installing-python/
    - https://docs.python-guide.org/#the-hitchhiker-s-guide-to-python
    - OS specific downloads: https://www.python.org/downloads/

- **Virtual environment**
    We recommend that users get familiar with `virtual environments <https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv/>`_ or `environment manager <https://www.anaconda.com/distribution/>`_:

    * These are tools that help keep dependencies separate for different projects. If you decide, however, to use a virtual environment or manager you must do it now, in this prerequisite step.

    * A module named ``virtualenv``  is available by running ``pip3 install virtualenv`` (``pip3`` command is pip for Python3, you could also run ``pip3 install --upgrade pip`` first),

      **or**

    * An environment manager called `Anaconda <https://docs.anaconda.com/anaconda/install/>`_ is available by downloading OS specific installer. A full Anaconda distribution (with a collection of over 1,500+ open source packages), as well as its lightweight version called `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_ will include **Python 3.x**, so installing Python first isn't needed.  The ``conda`` is the preferred interface for managing package installations and environments with the Anaconda/Miniconda Python distribution (For using ``pip`` inside conda environments check `Understanding conda and pip <https://www.anaconda.com/understanding-conda-and-pip/>`_).



- `Jupyter <https://jupyter.org/>`_
    We recommend using Jupyter Notebook for running the **pyIncore** projects. It as an open-source application that allows you to create projects (documents) that contain live Python code, visualizations and documentation. With Anaconda (but not Miniconda!) you already have installed Jupyter notebook.

    `Installing Jupyter <https://jupyter.org/install.html>`_ can be done again with ``pip`` (on Miniconda; in your virtual environment) or ``pip3`` in virtualenv or globally:

    .. code-block:: bash

        pip3 install jupyter



----

`IN-CORE home <index.html>`_
