## Getting Started

This page is an overview of the **IN-CORE** and **pyIncore** documentation and related resources.

**IN-CORE** is a platform that enables quantitative comparisons of alternative resilience strategies.
On the platform, data from the community can be seamlessly integrated which allows users to optimize
community disaster resilience planning and post-disaster recovery strategies intelligently using physics-based
models of inter-dependent physical systems combined with socio-economic systems.

**pyIncore** is a Python project and module to analyze and visualize various hazard (earthquake, tornado, hurricane etc.) 
scenarios. Python framework accesses underlying data and interacts with them through remote services and facilitates 
moving and synthesizing results, it can also be used to develop scientific analysis and algorithm.

### Introduction to IN-CORE platform

On the IN-CORE platform, users can run analysis that model the impact of natural hazards and community resilience 
and recovery. The platform includes among others IN-CORE Lab, pyIncore, Web tools and services. Resources such as Inventory datasets, Fragilities, 
Hazard files etc. provided by the research community are stored on NCSA's IN-CORE 
servers, and they can be seamlessly integrated to allow users to optimize community disaster resilience planning and 
post-disaster recovery strategies.

IN-CORE platform utilizes the Jupyter Notebook as a workspace to allow users to develop scripts in Python and  
allowing them to call hazard and community resilience analyses modules embedded in **pyIncore** library. Available is **IN-CORE Lab**, 
an interactive environment with tabbed work area for working with code and data which is based on 
[Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/#), and with pyIncore pre-installed on the IN-CORE Lab.

In this Tutorial we will create a script for Building damage of specific testbed by calling pyIncore's 
core analysis module **BuildingDamage**. We will be running the Notebook interactively, first in NCSA's [IN-CORE Lab](incore_lab)
and then on user's local computer.

A user must have an IN-CORE account recognized by the IN-CORE service. This account gives you access to all of the public data on
the system and allows you to create data that is only accessible by you. See [IN-CORE Account](account) section for setting one.

IN-CORE Lab can be accessed from [https://incore.ncsa.illinois.edu](https://incore.ncsa.illinois.edu) home page. 
Log in with your new credentials and click on IN-CORE Lab link in the **upper left** pull down menu. 
A new tab with `Start My Server` button appears followed by a progress bar.

![IN-CORE Lab progress bar.](images/tutorials/tut1_1_start.jpg "IN-CORE Server progress bar.")

Main Incore Lab's dashboard tab appears shortly:

![IN-CORE Lab dashboard tab.](images/tutorials/tut1_2_dash.jpg "IN-CORE Lab dashboard tab.").

### Using pyIncore in IN-CORE Lab

In this section we will create and run our first analysis using Jupyter Notebook and pyIncore library, both running on remote server. 
We will re-create Building Damage analysis and run it in IN-CORE Lab. 

A user needs only IN-CORE account and Internet browser to finish 
the analysis. The result will be a comma-delimited (csv) text file with Building inventory and Damage states for each individual building.

1. Create an empty Jupyter Notebook by clicking the `Notebook > Python 3` tile. A new `.ipynb` file appears in the left panel. Rename it 
(Rigth Mouse click and Rename) to, for example **Tutorial_1.ipynb**  

2. In the Notebook's upper cell type, or copy and paste following code:
    ```
    from pyincore import IncoreClient
    from pyincore.analyses.buildingdamage import BuildingDamage
    ```
    With these two lines, by importing the `IncoreClient` and `BuildingDamage` classes you just get "access" to codebase in **pyIncore** module. 
    
    You can already run the Notebook by clicking `Run the selected cells` arrow button. If pyIncore imports correctly a second, empty cell appears. 
    Otherwise <span style="color:red">ImportError</span> error message is shown.

3. Connect to IN-CORE services by typing in the empty cell (or insert a new one by clicking the `+` button first):
    ```
    client = IncoreClient()
    ```
    Prompts `Enter username` and `Enter password` appear. Enter your account credentials for service authentication.
    
4. In the next cell we are going to select Hazard, Building inventory and Fragility curves for the buildings.
    ```
    # New madrid earthquake using Atkinson Boore 1995
    hazard_type = "earthquake"
    hazard_id = "5b902cb273c3371e1236b36b"

    # Building inventory in Shelby county, TN
    bldg_dataset_id = "5a284f0bc7d30d13bc081a28"

    # Default Building Fragility mapping
    mapping_id = "5b47b350337d4a3629076f2c"
    ```
   For this Tutorial we chose a **New madrid earthquake using Atkinson Boore 1995** as hazard, 
   **Building inventory in Shelby county, TN** and **Default Building Fragility mapping**
   
   The files are referenced by their ID numbers and they are being accessed from IN-CORE services; Hazard service, 
   Data service, and DFR3 (Damage, Functionality, Repair, Restoration, Recovery) service located on the IN-CORE servers.
   Users can see the files in [IN-CORE Web Tools](webtools) or in IN-CORE Lab under `INCORE Apps menu`.
   
    
5. Create an instance of Building damage object specific to this Tutorial; your Notebook code. Load datasets and specify parameters necessary for running the analysis.
    ```
    # Create building damage
    bldg_dmg = BuildingDamage(client)

    # Load input dataset
    bldg_dmg.load_remote_input_dataset("buildings", bldg_dataset_id)

   # Specify the result name
    result_name = "memphis_bldg_dmg_result"

    # Set analysis parameters
    bldg_dmg.set_parameter("result_name", result_name)
    bldg_dmg.set_parameter("mapping_id", mapping_id)
    bldg_dmg.set_parameter("hazard_type", hazard_type)
    bldg_dmg.set_parameter("hazard_id", hazard_id)
    bldg_dmg.set_parameter("num_cpu", 4)
    ```
   Note that the `load_remote_input_dataset` and `set_parameter` are functions of pyIncore's module. The parameter 
   Number of central processing units (num_cpu) is used for paralel computations.

6. Call your Building damage analysis run function.
    ```
    bldg_dmg.run_analysis()
    ```
    ![uilding damage Jupyter notebook cells in IN-CORE Lab..](images/tutorials/tut1_3_juplab_build_dmg.jpg "Building damage Jupyter notebook cells in IN-CORE Lab.")


7. Save your Tutorial notebook by clicking `Save` button in the top bar. Your web page now shows multiple cells of code. 
    
    You are not actually running a notebook yet. Running a cell means that you will execute the cells' content. 
    To execute cells one by one you can just select the first cell and click the **Run** button/command at the top, or from the menu 
    `Run > Run All Cells command`.
    
    A **memphis_bldg_dmg_result.csv** file will appear after a short time in the left panel.

    There is little indication that analysis is running except by either looking at the Notebook file and seeing the [*] for the  
    cell where that block of code is being executed.

8. You can view the resulting datataset directly in IN-CORE Lab by double clicking the csv file in the left panel 
    or by converting csv to Pandas DataFrame in the Notebook itself:
    ```
    # Retrieve result dataset
    result = bldg_dmg.get_output_dataset("result")

    # Convert dataset to Pandas DataFrame
    df = result.get_dataframe_from_csv()

    # Display top 5 rows of output data
    df.head()
    ```

### Using pyIncore locally

In this section we use the same Building Damage analysis but this time we run it locally, on user's computer. 
Apart from already set IN-CORE Account we need

* Python virtual environment called **Anaconda** and
* **pyIncore** library

Please note that for this **Getting started** example we recommend Python environment manager Anaconda because it  
includes Python and Jypyter Notebook (and many other open source packages), both needed locally. For details see [prerequisits](prerequisites.md) 
page. 

#### Install Anaconda manager

1. Download the latest Anaconda3 installer for your operating system from the [Anaconda](https://www.anaconda.com/distribution/) web page. 
Choose Python 3.7 version.

    Following three steps might differ slightly on your system. For up-to-date installation follow 
    Anaconda's documentation, chapters [Installing on Windows](https://docs.anaconda.com/anaconda/install/windows/), [Installing on macOS](https://docs.anaconda.com/anaconda/install/mac-os/) and 
    [Installing on Linux](https://docs.anaconda.com/anaconda/install/linux/).
    Various installation options are summarized in Anaconda's [Frequently asked questions](https://docs.anaconda.com/anaconda/user-guide/faq/#distribution-faq-windows-folder).

2. Run the installer setup locally if asked (select *Just Me* choice on Windows OS or *Install for me only* on Mac/Linux OS) 
to avoid the need for administrator privileges. 

3. Leave the **default** folder path. For your information, the default path is `C:\Users\<username>\anaconda3` on Windows, 
`/Users/<username>/opt/anaconda3` on Mac (or `~/opt` for the graphical install) and `/home/<username>/anaconda3` on Linux.

4. Do not add Anaconda to the PATH. Do, however, register Anaconda as the default Python environment.

5. Activate the environment:
    * On Windows, open up an Anaconda prompt from the Windows Start menu. The `base` environment is being activated and the prompt changes to: `(base) C:\Users\<user>`:

        ![Windows Menu.](images/tutorials/tut1_4_win_prompt.jpg)

    * On Mac/Linux, open up a Terminal. The `base` environment is being activated and the prompt changes to: `(base)/Users/<username>` or `(base)/home/<username>`:

        ![Environment prompt.](images/tutorials/tut1_5_env_prompt.jpg "Environment prompt")

6. Create the Python environment (for this example we choose `mypyincore`) and activate it:
    ```
    conda create -n mypyincore python=3.7
    conda activate mypyincore
    ```
    You should see `mypyincore` in parenthesis before the command prompt, meaning you set up the new virtual environment and are now using it.

7. Add [conda-forge](https://conda-forge.org/) package repository to your environment:
    ```
    conda config --add channels conda-forge
    ```

#### Install pyIncore package

1. Navigate to the directory you want to use for developing your code in Jupyter Notebooks and run the following command in your **activated** environment:
	```
	conda install -c in-core pyincore
	```

	To check that the package is installed, run
	```
	conda list pyincore
	```
 
2. Start local Jupyter Notebook by running the following command in the terminal or command prompt, from your **Project folder**. Jupyter Notebook is already installed 
with Anaconda distribution:
	```
	jupyter notebook
	```
   
	A message *The Jupyter Notebook is running* appears in the terminal/prompt and you should see the notebook open in your browser. 
	If a web browser doesn't open automatically, you can copy/paste a token into browser's navigation bar.
    
	![Jupyter Notebook token, running for the first time.](images/tutorials/tut1_6_juploc_token.jpg "Jupyter Notebook token, running for the first time.")

	If you see an error message *jupyter: command not found** launch Notebook through **Anaconda Navigator**, a desktop graphical user interface (GUI) 
	which lets you launch Anaconda applications.
	
	Find Anaconda Navigator using `Start Menu - Anaconda Navigator` or Search bar on Windows, or directly in the Applications folder on Mac. 
	Choose your environment (**mypyincore** in this example) from the `Applications On` pull down menu in the Navigator's dashboard, install 
    Jupyter Notebook and start it by clicking a **Launch** button.
    
 	![Anaconda Navigator dashboard.](images/tutorials/tut1_7_anaconda_nav.jpg "Anaconda Navigator dashboard.")
   
3. Create an new Jupyter Notebook (with Python 3), name it **Tutorial_1.ipynb** 

	![A new Jupyter Notebook.](images/tutorials/tut1_8_juploc_start.jpg "A new Jupyter Notebook..")

4. Add codebase of the analysis by following steps **1 through 8** from previous section [Using pyIncore in IN-CORE Lab](#pyincorelab).

	![Building damage Jupyter notebook cells.](images/tutorials/tut1_9_juploc_build_dmg.jpg "Building damage Jupyter notebook cells.")

5. Again, your web page should show multiple cells of code. To execute cells one by one select the first cell and click the **Run** button at the top.

	Please note, you might get warning *Matplotlib is building the font cache using fc-list. This may take a moment.*

    A **memphis_bldg_dmg_result.csv** file will appear after a short time in the file tab.	

	![Building damage files.](images/tutorials/tut1_10_juploc_build_files.jpg "Building damage files.")

	
### Useful links

* Anaconda: [Installing on Windows](https://docs.anaconda.com/anaconda/install/windows/), [Installing on macOS](https://docs.anaconda.com/anaconda/install/mac-os/) and 
[Installing on Linux](https://docs.anaconda.com/anaconda/install/linux/), and [Frequently asked questions](https://docs.anaconda.com/anaconda/user-guide/faq/#distribution-faq-windows-folder)

* A [Beginner’s Guide](https://medium.com/@neuralnets/beginners-quick-guide-for-handling-issues-launching-jupyter-notebook-for-python-using-anaconda-8be3d57a209b) to installing Jupyter Notebook using Anaconda distribution. 
Opening a Jupyter [Notebook on Windows](https://problemsolvingwithpython.com/02-Jupyter-Notebooks/02.04-Opening-a-Jupyter-Notebook/).

* For details on running and manipulating `ipynb` files refer to [Jupyter documentation](https://jupyter.readthedocs.io/en/latest/running.html#running). 
If you have problems running Notebooks, check our [WIKI questions](https://opensource.ncsa.illinois.edu/confluence/display/INCORE1/questions/all) page or contact us at [incore-dev@lists.illinois.edu](mailto:incore-dev@lists.illinois.edu).

* IN-CORE Lab extends Jupyter Lab. See [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/) and [blog](https://blog.jupyter.org/jupyterlab-is-ready-for-users-5a6f039b8906) for more information.

* IN-CORE's Frequently Asked Questions ([FAQ](faq)) and [WIKI Questions](https://opensource.ncsa.illinois.edu/confluence/display/INCORE1/questions/all)) for detail information. 

* The Building analysis Jupyter Notebook is also available at [IN-CORE project](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/bridge_dmg.ipynb) on GitHub.