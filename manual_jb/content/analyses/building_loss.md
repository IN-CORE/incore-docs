# Building structural loss

**Description**

This analysis calculates the building loss based on building appraisal value, mean damage, 
and an inflation multiplier. A user must supply the inflation rate (as a percentage) 
between building appraisal year and year of interest (current, date of hazard, etc.)

The output of this analysis is a CSV file with structural losses based on damage.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`component_type`| `str` | Component type | Type of building component. This variable defines the structural and non-structural components of an inventory item (building) and the choice of corresponding occupancy multipliers. Values of the string are<br /> STR: structural,<br /> DS: drift-sensitive nonstructural,<br />AS: acceleration-sensitive nonstructural,<br /> CONTENT: contents,<br />default is STR.
`inflation_factor`| `float` | Inflation factor | A factor to adjust the appraisal values of buildings. <br>Default is *0.0*.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`buildings` <sup>*</sup> | `ergo:buildingInventoryVer4`<br>`ergo:buildingInventoryVer5`<br>`ergo:buildingInventoryVer6`<br>`ergo:buildingInventoryVer7` | Building dataset |  A building inventory dataset.
`building_mean_dmg` <sup>*</sup> | `ergo:meanDamage`<br>`ergo:buildingDamage` | Building mean damage | A CSV file with building mean damage results for either Structural, Drift-Sensitive Nonstructural, Acceleration-Sensitive Nonstructural or Contents Damage component.
`occupancy_multiplier` | `incore:buildingOccupancyMultiplier` | Occupancy multiplier | Building occupancy damage multipliers. These multipliers account for the value associated with different types of components (structural, acceleration-sensitive nonstructural, drift-sensitive nonstructural, contents).

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`result` <sup>*</sup> | `ergo:buildingEconomicLoss` | Results | A CSV file with building economy losses <br>(format: CSV).

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create building economic loss
    bldg_econ_dmg = BuildingEconLoss(client)

    # Load input dataset
    bldg_econ_dmg.load_remote_input_dataset("buildings", bldg_dataset_id)
    bldg_econ_dmg.load_remote_input_dataset("building_mean_dmg", bldg_dmg_id)

    # Specify the result name
    result_name = "seaside_bldg_econ_loss"

    # Set analysis parameters
    bldg_econ_dmg.set_parameter("result_name", result_name)
    bldg_econ_dmg.set_parameter("inflation_factor", 2.5)

    # Run building economic loss analysis
    bldg_econ_dmg.run_analysis()
```

full analysis: [building_loss.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/building_loss.ipynb)