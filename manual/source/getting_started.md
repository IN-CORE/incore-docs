##Getting Started with pyIncore - An Overview and the first walk through Tutorial

This page is an overview of the **IN-CORE** and **pyIncore** documentation and related resources.

**IN-CORE** is a platform that enables quantitative comparisons of alternative resilience strategies.
On the platform, data from the community can be seamlessly integrated which allows users to optimize
community disaster resilience planning and post-disaster recovery strategies intelligently using physics-based
models of inter-dependent physical systems combined with socio-economic systems.

**pyIncore** is a Python project and module to analyze and visualize various hazard (earthquake, tornado, hurricane etc.) 
scenarios. Python framework accesses underlying data through remote services and facilitates moving 
and synthesizing results, it can also be used to develop scientific analysis and algorithm.

- [Try pyIncore](#trypyincore)
- [Learn pyIncore](#learnpyincore)
- Staying Informed
- Documentation
- Something Missing?

###<a name="trypyincore"></a>Try pyIncore

A user must have an IN-CORE account recognized by the IN-CORE service. This account gives you access to all of the public data on
the system and allows you to create data that is only accessible by you. See [IN-CORE Account](account) section for setting one.

We will be running a tutorial Jupyter notebook interactively in NCSA's [IN-CORE Lab](incore_lab) 
at [https://incore.ncsa.illinois.edu](https://incore.ncsa.illinois.edu). 
The IN-CORE Lab is a customized [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/#) with **pyIncore** pre-installed on the server.
Let us explore the IN-CORE Lab first.

###IN-CORE Lab

We added IN-CORE specific top menus, INCORE apps and INCORE docs as well as INCORE login tile under the Launcher pane. 
INCORE login uses username and LDAP password created during the NCSA’s IN-CORE Registration process. Fragility, Data and Hazard Explorers 
under INCORE apps menu become enabled after pressing LOGIN button AND reloading the current page in the browser. A file named user.json appears 
in the File list manager on the left side. The file contains an authentication token required for advanced development of new analyses 
using IN-CORE Application programming interface (API). NOTE: A user must reload the whole Jupyter dashboard page using the Reload button of the browser, 
not the Refresh File List (which is part of Jupyter’s file navigation).
Running a Building Damage Analysis


###Running a Building Damage Analysis

We assume that users develop python script by using pyIncore in their own Project folder.
Locate a file called .incorepw  in your HOME directory and write your credentials in it; the first line contains your username and the second password. 
The information is used for communicating with IN-CORE services such as hazard, data and fragility. The file is located in the .incore folder created 
during installation in your HOME directory. The typical path is C:\Users\<username> on Windows OS, /Users/<username> on MacOS and /home/<username> 
on Linux based machines.

Download the Building damage analysis Jupyter notebook (https://incore2.ncsa.illinois.edu/doc/examples/buildingdamage.ipynb) and verify the installation 
by running it from your project folder. For details of running and manipulating ipynb files refer to Jupyter documentation. 
If you have problems running notebooks, contact us at incore-dev@lists.illinois.edu.

Start local Jupyter notebook by running the following command at the terminal or command prompt from a Project folder:
jupyter notebook

A message The Jupyter Notebook is running appears in the terminal/prompt and you should see the notebook open in your browser. Note that you will be asked to copy/paste a token into your browser when you connect for the first time. 

####Test data

The installation does not contain test data. The easiest way to start learning pyIncore is by running 
the **Building damage analysis** Jupyter Notebook. Download (<https://github.com/IN-CORE/incore-docs/blob/master/notebooks/building_dmg.ipynb>)
and verify the installation by running it from your project folder.
