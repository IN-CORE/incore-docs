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

###<a name="trypyincore"></a>Try pyIncore

A user must have an IN-CORE account recognized by the IN-CORE service. This account gives you access to all of the public data on
the system and allows you to create data that is only accessible by you. See [IN-CORE Account](account) section for setting one.

We will be running a tutorial Jupyter notebook interactively in NCSA's [IN-CORE Lab](incore_lab). 
The IN-CORE Lab is a customized [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/#) with **pyIncore** pre-installed on the server.

Let us explore the IN-CORE Lab first.

IN-CORE Lab can be accessed from [https://incore.ncsa.illinois.edu](https://incore.ncsa.illinois.edu) home page. 
Log in with your new credentials and click on IN-CORE Lab link in the **upper left** pull down menu. 
A new tab with `Start My Server` button appears followed by a progress bar.

![IN-CORE Lab progress bar.](images/juplab0_start.jpg "IN-CORE Server progress bar.")

Main Incore Lab's dashboard tab appears shortly:

![IN-CORE Lab dashboard tab.](images/juplab0.jpg "IN-CORE Lab dashboard tab.").

We added IN-CORE specific top menus, **INCORE apps** and **INCORE docs** as well as **INCORE Authenticator** tile under 
the Launcher pane.

###<a name="learnpyincore"></a>Learn pyIncore

In this section we will create our first Notebook using **pyIncore** library. We will re-create Building Damage analysis and Run it.
The result will be a csv file with Building inventory and Damage states for each individual building.

1. Create an empty Jupyter Notebook by clicking on the `Notebook > Python 3` tile. A new `.ipynb` file appears in the in the left panel. Rename it (Rigth Mouse click and Rename) to 
for example **Tutorial_1.ipynb**  

2. In the Notebook's upper cell type, or copy and paste:
    ```
    from pyincore import IncoreClient
    from pyincore.analyses.buildingdamage import BuildingDamage
    ```
    We just got access to code from **pyIncore** module by importing the `IncoreClient` and `BuildingDamage` classes and 
    their functions using import. You can already run the Notebook by clicking `Run the selected cells` Arrow button. A second, empty cell appears if pyIncore imports 
    correctly, otherwise <span style="color:red">ImportError</span> error message is shown.

3. Insert a new cell by clicking the `+` button and type:
    ```
    client = IncoreClient()
    ```
    to connect to IN-CORE service. Prompts `Enter username` and `Enter password` appear. Enter your account credentials for service authentication.
    
4. In the next cell we are going to select a hazard, building inventory and fragility curves for the buildings.
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
   Data service, and 3) DFR3 (Damage, Functionality, Repair, Restoration, Recovery) service located on the IN-CORE servers.
   
   We refer user to Documentation and Frequently Asked Questions ([FAQ](faq) and [WIKI Questions](https://opensource.ncsa.illinois.edu/confluence/display/INCORE1/questions/all)) for detail information. 
    
5. Create an instance of Building damage object specific to this Tutorial (your Notebook code), load dataset and 
    files and specify parameters necessary for running the analysis.
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
   Note that the `load_remote_input_dataset` and `set_parameter` are functions of pyIncore's module. The only Runtime parameter 
   here is Number of central processing units (num_cpu) for paralel computations.

6. Call your Building damage analysis run function.
    ```
    bldg_dmg.run_analysis()
    ```

    [Building damage Jupyter notebook cells in IN-CORE Lab.](images/juplab9_run_nbook.jpg "Building damage Jupyter notebook cells in IN-CORE Lab.")


7. Save your Tutorial notebook by clicking `Save` button in the top bar and Run the analyses by using command 
`Run > Run All Cells command`. A **memphis_bldg_dmg_result.csv** file will appear after a short time in the left pane. 

8. You can view the resulting csv datataset directly in your Notebook by converting it into Pandas DataFrame:
    ```
    # Retrieve result dataset
    result = bldg_dmg.get_output_dataset("result")

    # Convert dataset to Pandas DataFrame
    df = result.get_dataframe_from_csv()

    # Display top 5 rows of output data
    df.head()
    ```

The Building analysis Jupyter Notebook is also available at IN-CORE's [GitHub](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/bridge_dmg.ipynb).