# Combined wind, wave, surge building loss

**Description**

This analysis determines overall building loss from wind, flood and surge-wave damage 

The output of this analysis is a CSV file with individual components of structural and content loss as well as total 
loss. 

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.

**Input datasets**

key name | type | name                           | description
--- | --- |--------------------------------| ---
`buildings` <sup>*</sup> | [`ergo:buildingInventoryVer4`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingInventoryVer4)<br>[`ergo:buildingInventoryVer5`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingInventoryVer5)<br>[`ergo:buildingInventoryVer6`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingInventoryVer6)<br>[`ergo:buildingInventoryVer7`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingInventoryVer7) | Building dataset |  A building dataset.
`wind_damage` <sup>*</sup> | [`ergo:buildingDamageVer6`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingDamageVer6) | Building wind damage | A building wind damage dataset.
`surge_wave_damage` <sup>*</sup> | [`ergo:buildingDamageVer6`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingDamageVer6) | Building surge-wave damage | A building surge-wave damage dataset.
`flood_damage` <sup>*</sup> | [`ergo:nsBuildingInventoryDamageVer4`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:nsBuildingInventoryDamageVer4) | Building flood damage | A building flood damage dataset.
`structural_cost` <sup>*</sup> | [`incore:structuralCostRatio`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:structuralCostRatio) | Building structural cost ratios | A dataset with building structural cost ratios for each archetype.
`content_cost` <sup>*</sup> | [`incore:contentCostRatio`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:contentCostRatio) | Building content cost ratios | A dataset with building content cost ratios for each damage state.

**Output datasets**

key name | type | parent key | name | description
--- | --- | --- |---------| ---
`result` <sup>*</sup> | [`incore:buildingLoss`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:buildingLoss) | `buildings` | Results | A dataset containing structural, content and total loss for each building<br>(format: CSV).
<small>(* required)</small>

**Execution**

code snippet:

```
    # Create surge-wave building damage
    sw_bldg_dmg = BuildingDamage(client)

    # Run building damage analysis
    sw_bldg_dmg.run_analysis()    

    # Create wind building damage
    w_bldg_dmg = BuildingDamage(client)

    # Run building damage analysis
    w_bldg_dmg.run_analysis()    

    # Create flood building damage
    f_bldg_dmg = BuildingDamage(client)

    # Run building damage analysis
    f_bldg_dmg.run_analysis()    

    surge_wave_damage = sw_bldg_dmg.get_output_dataset("ds_result")
    wind_damage = w_bldg_dmg.get_output_dataset("ds_result")
    flood_damage = f_bldg_dmg.get_output_dataset("ds_result")

    # Combined building loss from each hazard
    combined_bldg_loss = CombinedWindWaveSurgeBuildingLoss(client)
    combined_bldg_loss.load_remote_input_dataset("buildings", bldg_dataset_id)
    combined_bldg_loss.set_input_dataset("surge_wave_damage", surge_wave_damage)
    combined_bldg_loss.set_input_dataset("wind_damage", wind_damage)
    combined_bldg_loss.set_input_dataset("flood_damage", flood_damage)
    combined_bldg_loss.load_remote_input_dataset("structural_cost", structural_cost_id)
    combined_bldg_loss.load_remote_input_dataset("content_cost", content_cost_id)
    combined_bldg_loss.set_parameter("result_name", "Galveston")
    combined_bldg_loss.run_analysis() 
```

full analysis: [combined_wind_wave_surge_building_loss.ipynb](https://github.
com/IN-CORE/incore-docs/blob/main/notebooks/combined_wind_wave_surge_building_loss.ipynb)
