Installation
============

All Platforms
-------------

1. Download **pyincore** as an archive file from NCSA's server.
2. Change into the ``pyincore`` directory (or prepend the path to the directory onto files reference from here on out)
3. **Optional**: Activate your virtual (``source virtual_env_name/bin/activate``) or conda (``source activate virtual_env_name``) environment. The conda is the preferred interface for managing installations and virtual environments with the Anaconda Python distribution.
4. From the terminal, in the project folder (``pyincore``) run:

    .. code-block:: bash

        python setup.py install


Windows specific installation notes
-----------------------------------

* Open the ``Anaconda`` prompt, or ``cmd`` depending on if you are using Anaconda or not before you activate virtual environment (step 3 above)



Mac specific installation notes
-------------------------------

* ``spacialindex`` library is needed, but appears to be included on other platforms. The easy way to install is to use `Homebrew <https://brew.sh/>`_ , and run:

    .. code-block:: bash

        brew install spacialindex

* We use ``matplotlib`` library to create graphs. There is a Mac specific installation issue addressed at StackOverflow `link1 <https://stackoverflow.com/questions/4130355/python-matplotlib-framework-under-macosx>`_ and `link2 <https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python>`_. In a nutshell, insert line:

    .. code-block:: bash

        backend : Agg


into ``~/.matplotlib/matplotlibrc`` file.


----

:doc:`Pyincore home <index>`