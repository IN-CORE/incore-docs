## Testing and Running

- We assume that users develop python script by using pyIncore in their own **Project folder**.


- Locate a file called `.incorepw` in your HOME directory and write your credentials in it; the first line contains your username and the second password. 
The information is used for communicating with **IN-CORE** services such as hazard, data and fragility. 
The file is located in the `.incore` folder created during installation in your HOME directory.


- Download the **Building damage analysis** Jupyter notebook (<https://incore2.ncsa.illinois.edu/doc/examples/buildingdamage.ipynb>) (right-click and choose "save link as") 
and verify the installation by running it from your project folder. For details of running and manipulating `ipynb` files refer 
to [Jupyter documentation](https://jupyter.readthedocs.io/en/latest/running.html#running). If you have problems running notebooks, contact us at [incore-dev@lists.illinois.edu](mailto:incore-dev@lists.illinois.edu).


- Start local **Jupyter notebook** by running the following command at the terminal or command prompt from a **Project folder**:
    ```
    jupyter notebook
    ```
    
    or if Jupyter Notebook is not recognized in Anaconda
    ```
    jupyter -m notebook
    ```     
   
    A message *The Jupyter Notebook is running* appears in the terminal/prompt 
    and you should see the notebook open in your browser. 
    You will be asked to copy/paste a token into your browser when you connect 
    for the first time.
    
    ![Jupyter Notebook token, running for the first time.](images/jupyter_token2.jpg "Jupyter Notebook token, running for the first time.")
    
    **Note** that the notebook is already installed with Anaconda 
    distribution however it has to be installed separately in your virtual environment 
    on Miniconda by running `conda install jupyter`.
    
    
- Click on the `buildingdamage.ipynb` in the Jupyter Notebook browser.

    ![Jupyter Notebook dashboard.](images/juplocal1_file.jpg "Jupyter Notebook dashboard.")


- Your web page should now show multiple cells of code. Right now you are not actually running a notebook yet. Running 
a cell means that you will execute the cellâ€™s contents. To execute cells in order you can just select the first 
cell and click the **Run** button at the top.

    ![Building damage Jupyter notebook cells.](images/juplocal2_notebook.jpg "Building damage Jupyter notebook cells.")

    The **Building damage** is a long running analysis and there is little indication that it's running except 
    by either looking at the Jupyter Notebook file and seeing the [*] for the notebook cell where that block 
    of code is being executed or by looking at the Task Manager in the Notebook dashboard to see there is 
    a python process running. Alternatively, you can look at the Jupyter Notebook dashboard to see if the `csv` file 
    with results has been created yet.

For details of running and manipulating ipynb files refer to [Jupyter documentation](https://jupyter.readthedocs.io/en/latest/running.html#running).

- Additionally, a user can run Jupyter notebook interactively in NCSA's [IN-CORE Lab](https://incore.ncsa.illinois.edu/lab).
