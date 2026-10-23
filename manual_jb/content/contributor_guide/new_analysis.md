# 3. Write a new analysis

## Set up

Install pyIncore from source in editable mode (see [Working with Python → Install from source](python_environment.md)), so your new analysis runs against your local code. For an incubator analysis, do the same with [pyincore-incubator](https://github.com/IN-CORE/pyincore-incubator).

## Subclass BaseAnalysis

Implement `get_spec()` (inputs, parameters, outputs) and `run()` (the computation):

```python
from pyincore import BaseAnalysis


class MyAnalysis(BaseAnalysis):
    def __init__(self, incore_client):
        super(MyAnalysis, self).__init__(incore_client)

    def get_spec(self):
        return {
            "name": "my-analysis",
            "description": "what it computes",
            "input_parameters": [
                {"id": "result_name", "required": True, "description": "result dataset name", "type": str},
            ],
            "input_datasets": [
                {"id": "buildings", "required": True, "description": "Building Inventory",
                 "type": ["ergo:buildingInventoryVer7"]},
            ],
            "output_datasets": [
                {"id": "result", "parent_type": "buildings", "description": "CSV of results",
                 "type": "ergo:buildingDamageVer6"},
            ],
        }

    def run(self):
        buildings = self.get_input_dataset("buildings").get_inventory_reader()
        results = [{"guid": b["properties"]["guid"]} for b in buildings]
        self.set_result_csv_data("result", results, name=self.get_parameter("result_name"))
        return True
```

Working example: [`example.py`](https://github.com/IN-CORE/pyincore-incubator/blob/develop/pyincore_incubator/analyses/example/example.py) in pyincore-incubator. Existing analyses in [pyincore/analyses](https://github.com/IN-CORE/pyincore/tree/develop/pyincore/analyses) are good templates.

## Try it on existing data

Run it like any other analysis (`set_input_dataset`, `set_parameter`, `run_analysis`):

- Remote data by ID: [Getting Started](../getting_started.md), [Analyses](../analyses.md)
- Local or uploaded data: [Tutorials](../tutorials.md)

## Where it goes

| Destination | When | Include |
|-------------|------|---------|
| [pyincore-incubator](https://github.com/IN-CORE/pyincore-incubator) | New or experimental community analyses | Analysis under `pyincore_incubator/analyses/<name>/`, test under `tests/pyincore_incubator/analyses/<name>/`, example notebook |
| [pyincore](https://github.com/IN-CORE/pyincore) | Analyses for the core library, agreed with the IN-CORE team | Analysis under `pyincore/analyses/<name>/`, test under `tests/pyincore/analyses/<name>/`, example notebook |

Then open a PR (see [Fix bugs or change pyIncore](pyincore_changes.md)) and add the docs page (see [Docs and example notebooks](docs_notebooks.md)).
