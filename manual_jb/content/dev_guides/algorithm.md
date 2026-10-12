# 2. Scientist: develop a new pyincore / pyincore-viz algorithm

## Setup (all cases)

```bash
conda create -n incore -c conda-forge python=3.11
conda activate incore
conda install -c in-core pyincore pyincore-viz jupyter
```

To modify pyincore itself instead of using the release:

```bash
git clone https://github.com/IN-CORE/pyincore.git
cd pyincore
conda env update -n incore -f environment.yml
pip install -e .
```

New analysis = subclass `BaseAnalysis`, implement `get_spec()` and `run()`.
Copy an existing analysis as a template (e.g. `pyincore/analyses/buildingdamage/`).

- Analysis pattern + example: [pyIncore Incubator](../pyincore_incubator.md)
- API reference: https://tools.in-core.org/doc/pyincore/index.html

---

## 2a. Use existing resources on IN-CORE services

Inputs (inventory, hazard, DFR3, mapping) are referenced by ID from prod.

```python
from pyincore import IncoreClient, FragilityService, MappingSet
client = IncoreClient()  # prompts for IN-CORE login, defaults to https://tools.in-core.org

analysis = MyAnalysis(client)
analysis.load_remote_input_dataset("buildings", "<dataset_id>")
analysis.set_input_dataset("dfr3_mapping_set",
    MappingSet(FragilityService(client).get_mapping("<mapping_id>")))
analysis.set_parameter("hazard_type", "earthquake")
analysis.set_parameter("hazard_id", "<hazard_id>")
analysis.run_analysis()
```

Find IDs: Web tools (Data/Hazard/DFR3 viewers) [IN-CORE Web Tools](../webtools.md)

- Walkthrough: [Getting Started](../getting_started.md)
- Per-analysis inputs/IDs: [Analyses](../analyses.md)

(dev-guides-local-data)=
## 2b. Use local datasets / hazard / fragility / mapping

No upload needed. Use `offline=True` if nothing is remote.

```python
from pyincore import IncoreClient, Dataset, FragilityCurveSet, MappingSet, Earthquake

client = IncoreClient(offline=True)

bldgs   = Dataset.from_file("bldgs.shp", data_type="ergo:buildingInventoryVer7")
mapping = MappingSet.from_json_file("mapping.json")          # references local fragility IDs
eq      = Earthquake.from_json_file("eq.json")
eq.hazardDatasets[0].from_file("pga.tif", data_type="ergo:probabilisticEarthquakeRaster")

analysis = MyAnalysis(client)
analysis.set_input_dataset("buildings", bldgs)
analysis.set_input_dataset("dfr3_mapping_set", mapping)
analysis.set_input_hazard("hazard", eq)
analysis.run_analysis()
```

| Need | Tutorial |
|------|----------|
| Local hazard (EQ, tornado, flood, hurricane, tsunami) | [Create Local Hazards](../notebooks/create_local_hazard/create_local_hazard.ipynb) |
| Local dataset | [Create and Use Dataset Object](../notebooks/create_dataset/create_dataset.ipynb) |
| Local fragility + mapping | [Create  DFR3 and Mapping Objects](../notebooks/create_dfr3_object/create_dfr3_object.ipynb) |
| Local network dataset | [Create Network Dataset](../notebooks/create_network_dataset/create_network_dataset.ipynb) |
| Full local-data workflow | [Session 4: Building Damage and Recovery Analyses with Local Data](../workshops/20231115/session4/session4-building-dmg-recovery-local-data.ipynb) |
| Remote vs local hazards | [Session 2: How to Work with Remote and Local Hazards](../workshops/20231115/session2/session2-remote-and-local-hazards.ipynb) |

Data types (`data_type=`): listed on each analysis page, or `SemanticService(client).get_all_semantic_types()` (login required).

## 2c. Upload to IN-CORE services

Requires a logged-in client (not offline). Uploads are private to your account by default.

| Resource | pyincore call | Tutorial |
|----------|---------------|----------|
| Dataset | `DataService.create_dataset(props)` → `add_files_to_dataset(id, files)` | [create_dataset](../notebooks/create_dataset/create_dataset.ipynb) |
| Network dataset | `DataService.add_files_to_network_dataset(...)` | [create_network_dataset](../notebooks/create_network_dataset/create_network_dataset.ipynb) |
| Fragility / mapping | `FragilityService.create_dfr3_set(json)` / `create_mapping(json)` | [create_dfr3_object](../notebooks/create_dfr3_object/create_dfr3_object.ipynb) |
| Earthquake | `HazardService.create_earthquake(json, files)` | [create_earthquake](../notebooks/create_earthquake/create_earthquake.ipynb) |
| Tornado | `HazardService.create_tornado_scenario(json, files)` | [create_tornado](../notebooks/create_tornado/create_tornado.ipynb) |
| Flood / hurricane / tsunami | `create_flood` / `create_hurricane` / `create_tsunami_hazard` | [API ref](https://tools.in-core.org/doc/pyincore/index.html) |

Tip: develop against **dev** first (`IncoreClient("https://dev.in-core.org")`) so test uploads don't clutter prod.
To share with a group (space), contact incore-dev@lists.illinois.edu.

---

## Getting it into a release

- New analysis for community use → **pyincore-incubator** (see {ref}`Contribute to pyincore-incubator <dev-guides-incubator>`).
- Core analysis → PR to https://github.com/IN-CORE/pyincore with tests under `tests/pyincore/analyses/<name>/`.
- Visualization → PR to https://github.com/IN-CORE/pyincore-viz.
