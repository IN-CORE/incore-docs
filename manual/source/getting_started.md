##Getting Started with pyIncore - An Overview and the first walkthrough Tutorial

This page is an overview of the **IN-CORE** and **pyIncore** documentation and related resources.

Learn what pyIncore is all about on our homepage or in the tutorial.


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

