# Building Economic Loss

**Description**

This analysis calculates the building loss based on building appraisal value, mean damage, 
and an inflation multiplier. A user must supply the inflation rate (as a percentage) 
between building appraisal year and year of interest (current, date of hazard, etc.) and optional Occupancy multiplier.
The analysis can be used for with building mean damage results for either Structural, Drift-Sensitive Nonstructural, 
Acceleration-Sensitive Nonstructural or Contents Damage component.

The output of this analysis is a CSV file with structural losses based on damage.

**Contributors**

- Science: Ported from Ergo/MAEviz implementation
- Implementation: Michal Ondrejcek, Gowtham Naraharisetty, Chris Navarro and NCSA IN-CORE Dev Team

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`inflation_factor`| `float` | Inflation factor | A factor to adjust the appraisal values of buildings. <br>Default is *0.0*.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`buildings` <sup>*</sup> | [`ergo:buildingInventoryVer4`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingInventoryVer4)<br>[`ergo:buildingInventoryVer5`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingInventoryVer5)<br>[`ergo:buildingInventoryVer6`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingInventoryVer6)<br>[`ergo:buildingInventoryVer7`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingInventoryVer7) | Building dataset |  A building inventory dataset.
`building_mean_dmg` <sup>*</sup> | [`ergo:meanDamage`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:meanDamage)<br>[`ergo:buildingDamage`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingDamage) | Building mean damage | A CSV file with building mean damage results for either Structural, Drift-Sensitive Nonstructural, Acceleration-Sensitive Nonstructural or Contents Damage component.
`occupancy_multiplier` | [`incore:buildingOccupancyMultiplier`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:buildingOccupancyMultiplier) | Occupancy multiplier | Building occupancy damage multipliers. These multipliers account for the value associated with different types of components (structural, acceleration-sensitive nonstructural, drift-sensitive nonstructural, contents).

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`result` <sup>*</sup> | [`ergo:buildingEconomicLoss`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingEconomicLoss) | Results | A CSV file with building economy losses.

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create building economic loss
    bldg_econ_dmg = BuildingEconLoss(client)

    # Load input dataset
    bldg_econ_dmg.load_remote_input_dataset("buildings", bldg_dataset_id)
    bldg_econ_dmg.load_remote_input_dataset("building_mean_dmg", bldg_dmg_id)
    bldg_econ_dmg.load_remote_input_dataset("occupancy_multiplier", bldg_occupancy_mult_id)

    # Specify the result name
    result_name = "seaside_bldg_econ_loss"

    # Set analysis parameters
    bldg_econ_dmg.set_parameter("result_name", result_name)
    bldg_econ_dmg.set_parameter("inflation_factor", 2.5)

    # Run building economic loss analysis
    bldg_econ_dmg.run_analysis()
```

full analysis: [building_loss.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/building_loss.ipynb)