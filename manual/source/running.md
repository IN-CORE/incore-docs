## Testing and Running

- We assume that users develop Python script by using pyIncore in their own **Project folder**.


- Install Jupyter Notebook. Jupyter Notebook is already installed with Anaconda distribution; it has to be installed separately in your virtual environment on Miniconda:
    ```
    conda install jupyter
    ```
  
- Download the **Building damage analysis** Jupyter Notebook (<https://github.com/IN-CORE/incore-docs/blob/master/notebooks/building_dmg.ipynb>)
and verify the installation by running it from your project folder. For details on running and manipulating `ipynb` files refer 
to [Jupyter documentation](https://jupyter.readthedocs.io/en/latest/running.html#running). If you have problems running Notebooks, contact us at [incore-dev@lists.illinois.edu](mailto:incore-dev@lists.illinois.edu).

- Start local **Jupyter Notebook** by running the following command at the terminal or command prompt from a **Project folder**. if you are using anaconda. If you are using Miniconda, please refer to the useful links section to install Jupyter Notebook:
    ```
    jupyter notebook
    ```
    
    or if Jupyter Notebook is not recognized in Anaconda
    ```
    jupyter -m notebook
    ```     
    A message *The Jupyter Notebook is running* appears in the terminal/prompt and you should see the notebook open in your browser. 
    If the web browser doesn't open automatically, you can copy/paste the whole url with token into browser's navigation bar.
    
    ![Jupyter Notebook token, running for the first time.](images/jupyter_token2.jpg "Jupyter Notebook token, running for the first time.")

	If you use Anaconda and see an error message *jupyter: command not found** launch Notebook through **Anaconda Navigator**, a desktop graphical user interface (GUI) 
	which lets you launch Anaconda applications.
	
	Find Anaconda Navigator using `Start Menu - Anaconda Navigator` or Search bar on Windows, or directly in the Applications folder on Mac. 
	Choose your environment (**mypyincore** in this example) from the `Applications On` pull down menu in the Navigator's dashboard, install 
    Jupyter Notebook and start it by clicking a **Launch** button.
    
 	![Anaconda Navigator dashboard.](images/tutorials/tut1_9_anaconda_nav.jpg "Anaconda Navigator dashboard.")


- Click on the `building_dmg.ipynb` in the Jupyter Notebook browser.

    ![Jupyter Notebook dashboard.](images/juplocal1_file.jpg "Jupyter Notebook dashboard.")


- Your web page should now show multiple cells of code. However, you are not actually running a notebook yet. Running 
a cell means that you will execute its content. To execute cells in order you can just select the first 
cell and click the **Run** button at the top.

    ![Building damage Jupyter notebook cells.](images/juplocal2_notebook.jpg "Building damage Jupyter notebook cells.")

    The **Building damage** is a long running analysis and there is little indication that it's running except 
    by either looking at the Jupyter Notebook file and seeing the [*] for the notebook cell where that block 
    of code is being executed or by looking at the Task Manager in the Notebook dashboard to see there is 
    a python process running. Alternatively, you can look at the Jupyter Notebook dashboard to see if the `csv` file 
    with results has been created yet.

For details of running and manipulating ipynb files refer to [Jupyter documentation](https://jupyter.readthedocs.io/en/latest/running.html#running).

- Additionally, a user can run Jupyter Notebook interactively in NCSA's [IN-CORE Lab](https://incore.ncsa.illinois.edu/lab).
