# Cumulative building damage

**Description**

This analysis computes building damage based on a particular hazard. The process for computing the structural damage 
is done externally and the results for earthquake and tsunami are imported to the analysis. The damage intervals are then calculated from combined limit states.

The output of this analysis is a CSV file with probabilities of damage.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. <br>Default *1*.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`eq_bldg_dmg` <sup>*</sup> | `ergo:buildingDamageVer5` | Building dataset | A building dataset with earthquake damage.
`tsunami_bldg_dmg` <sup>*</sup> | `ergo:buildingDamageVer5` | Building dataset | A building dataset with tsunami damage.

**Output datasets**

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`combined-result` <sup>*</sup> | `ergo:buildingDamageVer5` | `buildings` | Results | A dataset containing results <br>(format: CSV).

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create cumulative Building Damage
    cumulative_bldg_dmg = CumulativeBuildingDamage(client)

    # Load input datasets
    cumulative_bldg_dmg.load_remote_input_dataset("eq_bldg_dmg", eq_bldg_dmg_id)
    cumulative_bldg_dmg.load_remote_input_dataset("tsunami_bldg_dmg", tsunami_bldg_dmg_id)

    # Specify the result name
    result_name = "cumulative_bldg_dmg_result"

    # Set analysis parameters
    cumulative_bldg_dmg.set_parameter("result_name", result_name)
    cumulative_bldg_dmg.set_parameter("num_cpu", 4)

    # Run Cumulative Building Damage Analysis
    cumulative_bldg_dmg.run_analysis()
```

full analysis: [cumulative_building_dmg.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/cumulative_building_dmg.ipynb)