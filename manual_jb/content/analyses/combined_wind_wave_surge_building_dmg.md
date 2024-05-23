# Combined wind, wave, surge building damage

**Description**

This analysis determines overall building maximum damage state from wind, flood and surge-wave damage 

The outputs of this analysis are a CSV file with maximum damage state from each hazard and the overall maximum damage and a CSV with the combined damage probabilities from the three hazards

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`wind_damage` <sup>*</sup> | [`ergo:buildingDamageVer6`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingDamageVer6) | Building wind damage |  A building wind damage dataset.
`surge_wave_damage` <sup>*</sup> | [`ergo:buildingDamageVer6`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingDamageVer6) | Building surge-wave damage |  A building surge-wave damage dataset.
`flood_damage` <sup>*</sup> | [`ergo:nsBuildingInventoryDamageVer4`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:nsBuildingInventoryDamageVer4) | Building flood damage |  A building flood damage dataset.

**Output datasets**

key name | type | parent key | name| description
--- | --- | --- |---| ---
`result` <sup>*</sup> | [`incore:maxDamageState`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:maxDamageState) | `buildings` | Results| A dataset containing maximum damage state for each building<br>(format: CSV).
`ds_result` <sup>*</sup> | [`ergo:buildingDamageVer6`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingDamageVer6) | `buildings` | Damage State Results | A dataset containing damage states for building structural damage<br>(format: CSV).
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
    f_bldg_dmg = NonStructBuildingDamage(client)

    # Run building damage analysis
    f_bldg_dmg.run_analysis()    

    surge_wave_damage = sw_bldg_dmg.get_output_dataset("ds_result")
    wind_damage = w_bldg_dmg.get_output_dataset("ds_result")
    flood_damage = f_bldg_dmg.get_output_dataset("ds_result")

    combined_bldg_dmg = CombinedWindWaveSurgeBuildingDamage(client)
    result_name = "combined_dmg_result"
    combined_bldg_dmg.set_input_dataset("surge_wave_damage", surge_wave_damage)
    combined_bldg_dmg.set_input_dataset("wind_damage", wind_damage)
    combined_bldg_dmg.set_input_dataset("flood_damage", flood_damage)
    combined_bldg_dmg.set_parameter("result_name", result_name)
    combined_bldg_dmg.run_analysis()
```

full analysis: [combined_wind_wave_surge_building_dmg.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/combined_wind_wave_surge_building_dmg.ipynb)
