# Mean damage

**Description**

The process for computing the structural damage uses mean damage and standard deviation values from damage ratios tables. 
The four damage state probabilities are multiplied by the mean damage and aggregated to get the Mean damage for 
each individual structure (building, bridge, waterfacility etc.). 

The output of this analysis is a CSV file with probabilities of damage.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`damage_interval_keys` <sup>*</sup> | `list` | Damage ratio | Names of the four damage intervals.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computation. <br>Default is *1*.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`damage` <sup>*</sup> | `ergo:buildingDamageVer4`<br>`ergo:buildingDamageVer5`<br>`ergo:nsBuildingInventoryDamage`<br>`ergo:nsBuildingInventoryDamageVer2`<br>`ergo:bridgeDamage`<br>`ergo:bridgeDamageVer2`<br>`ergo:waterFacilityDamageVer4`<br>`ergo:waterFacilityDamageVer5`<br>`ergo:roadDamage`<br>`ergo:roadDamageVer2`<br>`incore:epfDamage`<br>`incore:epfDamageVer2`<br>`incore:pipelineDamage`<br>`incore:pipelineDamageVer2`| Infrastructure dataset |  An infrastructure dataset.
`dmg_ratios` <sup>*</sup> | `ergo:buildingDamageRatios`<br>`ergo:bridgeDamageRatios`<br>`ergo:buildingContentDamageRatios`<br>`ergo:buildingASDamageRatios`<br>`ergo:buildingDSDamageRatios`<br>`ergo:roadDamageRatios` | Damage ratios |  A damage ratios dataset.
 
**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`result` <sup>*</sup> | `ergo:meanDamage` | Results | A dataset containing results <br>(format: CSV).

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create mean damage instance
    md = MeanDamage(client)

    # Load input datasets
    md.set_input_dataset("damage", bridge_damage_result)
    md.load_remote_input_dataset("dmg_ratios", dmg_ratios_id)

    # Specify the result name
    result_name = "result_name"

    # Set analysis parameters
    md.set_parameter("result_name", "bridge_mean_damage")
    md.set_parameter("damage_interval_keys",["DS_0", "DS_1", "DS_2", "DS_3", "DS_4"])
    md.set_parameter("num_cpu", 1)

    # Run mean damage analysis
    md.run_analysis()
```

full analysis: [mean_dmg.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/mean_dmg.ipynb)