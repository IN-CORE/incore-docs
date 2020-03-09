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



Running a Building Damage Analysis

We assume that users develop python script by using pyIncore in their own Project folder.
Locate a file called .incorepw  in your HOME directory and write your credentials in it; the first line contains your username and the second password. The information is used for communicating with IN-CORE services such as hazard, data and fragility. The file is located in the .incore folder created during installation in your HOME directory. The typical path is C:\Users\<username> on Windows OS, /Users/<username> on MacOS and /home/<username> on Linux based machines.

Download the Building damage analysis Jupyter notebook (https://incore2.ncsa.illinois.edu/doc/examples/buildingdamage.ipynb) and verify the installation by running it from your project folder. For details of running and manipulating ipynb files refer to Jupyter documentation. If you have problems running notebooks, contact us at incore-dev@lists.illinois.edu.

Start local Jupyter notebook by running the following command at the terminal or command prompt from a Project folder:
jupyter notebook

A message The Jupyter Notebook is running appears in the terminal/prompt and you should see the notebook open in your browser. Note that you will be asked to copy/paste a token into your browser when you connect for the first time. 
Additionally, a user can run Jupyter notebook interactively in NCSA's IN-CORE Lab. (coming soon)



Running a Building Damage Analysis

We assume that users develop python script by using pyIncore in their own Project folder.
Locate a file called .incorepw  in your HOME directory and write your credentials in it; the first line contains your username and the second password. The information is used for communicating with IN-CORE services such as hazard, data and fragility. The file is located in the .incore folder created during installation in your HOME directory. The typical path is C:\Users\<username> on Windows OS, /Users/<username> on MacOS and /home/<username> on Linux based machines.

Download the Building damage analysis Jupyter notebook (https://incore2.ncsa.illinois.edu/doc/examples/buildingdamage.ipynb) and verify the installation by running it from your project folder. For details of running and manipulating ipynb files refer to Jupyter documentation. If you have problems running notebooks, contact us at incore-dev@lists.illinois.edu.

Start local Jupyter notebook by running the following command at the terminal or command prompt from a Project folder:
jupyter notebook

A message The Jupyter Notebook is running appears in the terminal/prompt and you should see the notebook open in your browser. Note that you will be asked to copy/paste a token into your browser when you connect for the first time. 

Additionally, a user can run Jupyter notebook interactively in NCSA's IN-CORE Lab. (coming soon)

IN-CORE Lab
IN-CORE Lab is an extended Jupyter Lab dashboard for running and editing Notebooks. We added IN-CORE specific top menus, INCORE apps and INCORE docs as well as INCORE login tile under the Launcher pane. INCORE login uses username and LDAP password created during the NCSA’s IN-CORE Registration process. Fragility, Data and Hazard Explorers under INCORE apps menu become enabled after pressing LOGIN button AND reloading the current page in the browser. A file named user.json appears in the File list manager on the left side. The file contains an authentication token required for advanced development of new analyses using IN-CORE Application programming interface (API). NOTE: A user must reload the whole Jupyter dashboard page using the Reload button of the browser, not the Refresh File List (which is part of Jupyter’s file navigation).

The second IN-CORE menu (INCORE docs) allows user to see pyIncore documentation and API endpoints definitions for accessing Fragility, Data and Hazard server(s). Another login window opens up at the top of the browser’s main window. In this case the user enters Documentation server credentials provided in NCSA’s invitational e-mail (username incore2). Documentation that appears in the frame mirrors the IN-CORE web pages and it is shown for convenience in IN-CORE Lab.

###<a name="learnpyincore"></a>Learn pyIncore

###Installing an official release

**pyIncore** and its dependency, **pyincore-viz** are available as conda packages for macOS, 
Windows and Linux distributions.

From the Terminal (Mac/Linux) or Command Prompt (Windows) add [conda-forge](https://conda-forge.org/) package repository/channel to your environment
and instal pyIncore:

```
conda config --add channels conda-forge
conda install -c in-core pyincore
conda install -c in-core pyincore-viz
```
   
Although not required, we suggest also installing [Jupyter Notebook](https://jupyter.org/install) for running interactive Notebooks.

```
conda install -c conda-forge notebook
```

####Test data

The installation does not contain test data. The easiest way to start learning pyIncore is by running 
the **Building damage analysis** Jupyter Notebook. Download (<https://github.com/IN-CORE/incore-docs/blob/master/notebooks/building_dmg.ipynb>)
and verify the installation by running it from your project folder.

