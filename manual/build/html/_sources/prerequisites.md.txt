## Prerequisites

- **IN-CORE Account**
    A user must have an **IN-CORE** account. If you do not have it, see [IN-CORE Account](account) section for setting one.

- **Virtual environment**
    We recommend that users get familiar with Python virtual environment managers called [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

    * These are tools that help keep dependencies separate for different projects. If you decide, however, to use 
    a virtual environment or manager you must do it now, in this prerequisite step.

    * Environment managers are available by downloading OS specific installers. Note that Anaconda/Miniconda 
    distribution will include Python (Anaconda also includes a collection of over 1,500+ open source packages), so installing Python first is not needed if you use Anaconda/Miniconda. With Anaconda you already have installed Jupyter Notebook. The `conda` is the preferred interface for managing installations and virtual environments with the Anaconda/Miniconda Python distribution.

- `Python 3.5+` <https://www.python.org/>
    It is common to have more than one Python version installed on your computer. Make sure you are running 
    the correct, Anaconda version of Python.

- `Jupyter Notebook` <https://jupyter.org/>
    We recommend using Jupyter Notebook for running the **pyIncore** projects. It as an open-source application 
    that allows you to create projects (documents) that contain live Python code, visualizations and documentation. 
    Jupyter Notebook is already installed with Anaconda distribution; it has to be installed separately 
    in your virtual environment on Miniconda distribution.

In the Installation section we provide instructions for environment manager using [Miniconda](https://docs.conda.io/en/latest/miniconda.html). Similar instructions apply to full [Anaconda](https://docs.anaconda.com/anaconda/install/) manager. Python 3.x is installed with both versions. The following instructions were tested for Mac, Windows and Linux 64-bit OS.

### Windows 64-bit

1. Download the latest Miniconda3 installer for Windows from the [Miniconda](https://docs.conda.io/en/latest/miniconda.html) web page.

2. Run the installer setup locally (select the *Just Me* choice) to avoid the need for administrator privileges.

3. Leave the default folder path (`C:\Users\<user>\..\miniconda3`).

4. Do not add Anaconda to the PATH. Do, however, register Anaconda as the default Python environment.

5. Open up an Anaconda prompt from the Windows Start menu. The `base` environment is being activated and the prompt changes to: `(base) C:\Users\<user>`:

    ![Windows Menu.](images/win_prompt1.jpg)


6. Create the python environment (`pyincoreEnv` for example) and activate it (or stay in the `base`):
    ```
    conda create -n pyincoreEnv python=3
    conda activate pyincoreEnv
    ```

7. Add [conda-forge](https://conda-forge.org/) package repository to your environment:
    ```
    conda config --add channels conda-forge
    ```

### Mac and Linux OS

1. Download the latest Miniconda3 installer from the [Miniconda](https://docs.conda.io/en/latest/miniconda.html) web page.

2. Run the installer setup locally (select the *Install for me only* on Mac/Linux) to avoid the need for administrator privileges.

3. Leave the default folder path (`/Users/<username>/miniconda3` or `/home/<username>/miniconda3`).

4. Do not add Anaconda to the PATH. Do, however, register Anaconda as the default Python environment.

5. Open up a Terminal. The `base` environment is being activated and the prompt changes to: `(base)/Users/<username>` or `(base)/home/<username>`:

6. Create the python environment (`pyincoreEnv` for example) and activate it (or stay in the `base`):
    ```
    conda create -n pyincoreEnv python=3
    conda activate pyincoreEnv
    ```

7. Add [conda-forge](https://conda-forge.org/) package repository to your environment:
    ```
    conda config --add channels conda-forge
    ```
   
   


