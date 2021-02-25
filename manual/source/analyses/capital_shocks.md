### Capital shocks

This analysis aggregates building functionality states and calculates total capital shock losses per sector.

Capital stock shocks for an individual building is equal to the functionality probability multiplied by value
of the building. This gives the capital stock loss in the immediate aftermath of a natural disaster. The analysis aggregates 
each of these individual losses to their associated economic sector and calculates the total capital stock lost for that 
particular sector.

The output of this analysis is a CSV file with aggregated building losses per sector and calculated total capital stock loss.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`buildings` <sup>*</sup> | `ergo:buildingInventoryVer4`<br>`ergo:buildingInventoryVer5`<br>`ergo:buildingInventoryVer6`<br>`ergo:buildingInventoryVer7` | Building dataset | A building inventory dataset.
`buildings_to_sectors` <sup>*</sup> | `incore:buildingsToSectors` | Buildings to sectors | A file defining sectors of buildings.
`failure_probability` <sup>*</sup> | `incore:failureProbability` | Failure probability | Failure probability of buildings..

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`sector_shocks` <sup>*</sup> | `incore:capitalShocks` | Results | A dataset containing aggregated building functionality to capital shocks<br>(format: CSV).

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create capital shocks loss
    joplin_capital_shocks = CapitalShocks(client)

    # Specify the result name
    result_name = "Joplin capital losses"

    # Set analysis parameters
    joplin_capital_shocks.set_parameter("result_name", result_name)

    # Load input datasets
    joplin_capital_shocks.load_remote_input_dataset("buildings", building_inventory)
    joplin_capital_shocks.load_remote_input_dataset("buildings_to_sectors", building_to_sectors)
    joplin_capital_shocks.load_remote_input_dataset("failure_probability", failure_probability)

    # Run Joplin capital shocks analysis
    joplin_capital_shocks.run_analysis()
```

full analysis: [capital_shocks.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/capital_shocks.ipynb)
