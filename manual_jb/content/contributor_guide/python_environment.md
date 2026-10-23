# 2. Working with Python

Prerequisite for pyIncore, pyIncore-viz, pyIncore-data and pyIncore-incubator.

## Create an environment

Install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) (or [mamba](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html)), then:

```bash
conda config --add channels conda-forge
conda create -n incore python=3.11
conda activate incore
```

pyIncore requires Python 3.11 or newer.

## Install released packages

```bash
conda install -c in-core pyincore pyincore-viz pyincore-data pyincore-incubator
```

Install only what you need. Slow or stuck dependency resolution? Add `--solver=libmamba`.

## Install from source (editable)

For contributors, or to try an unreleased fix. Changes to the source take effect without reinstalling.

```bash
git clone https://github.com/IN-CORE/pyincore.git
cd pyincore
conda env create -f environment.yml
conda activate pyincore
pip install -e .
```

Same pattern for [pyincore-viz](https://github.com/IN-CORE/pyincore-viz), [pyincore-incubator](https://github.com/IN-CORE/pyincore-incubator) and [pyincore-data](https://github.com/IN-CORE/pyincore-data) (which uses `environment.yaml`). Per-repo details: [IN-CORE Developer Setup](https://github.com/IN-CORE/IN-CORE/wiki/IN%E2%80%90CORE-Developer-Setup) (wiki).

## Run notebooks

- Local: `conda install jupyter`, then `jupyter lab` from your project folder. See [Testing and Running](../pyincore/running.md).
- No install: [IN-CORE Lab](../incore_lab.md) has pyIncore preinstalled.

## Connect to IN-CORE

```python
from pyincore import IncoreClient

client = IncoreClient()                            # prod: https://tools.in-core.org
client = IncoreClient("https://dev.in-core.org")   # dev (requires dev access)
client = IncoreClient(offline=True)                # local data only, no services
```

- Dev access: ask via the channels in [Before you start](../contributor_guide.md).
- Login tokens are cached in `~/.incore`, one per service URL.
- Downloaded datasets are cached too. Stale data? `client.clear_cache()`.

## Troubleshooting

- **Fiona error after installing Jupyter:** Jupyter can downgrade fiona. Install Jupyter first, then pyIncore, or run `conda update fiona`.
- **macOS matplotlib backend error:** add `backend : Agg` to `~/.matplotlib/matplotlibrc` (create the file if missing).
