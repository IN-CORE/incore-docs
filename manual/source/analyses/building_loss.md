### Building structural loss

This analysis computes building structural loss based on mean damage of the building.

The economic loss damage uses building appraisal value as a base price and adjusts it based
 on the consumer price index reflecting inflation.  

The output of this analysis is a CSV file with structural losses based on damage.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computation. <br>Default is *1*.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`buildings` <sup>*</sup> | `ergo:buildingInventoryVer4`<br>`ergo:buildingInventoryVer5`<br>`ergo:buildingInventoryVer6`<br>`ergo:buildingInventory` | Building dataset |  A building inventory dataset.
`building_mean_dmg` <sup>*</sup> | `ergo:meanDamage`<br>`ergo:buildingDamage` | Building mean damage | Building mean damage results CSV file.
`consumer_price_index` <sup>*</sup> | `incore:consumerPriceIndexUS` | Consumer price index | US Consumer Price Index 1913-2020, text file.

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`result` <sup>*</sup> | `ergo:buildingEconomicLoss` | Results | A CSV file with building economy losses <br>(format: CSV).

<small>(* required)</small>

**Execution**

code snipet:

```
    # Create building economic loss
    bldg_econ_dmg = BuildingEconLoss(client)

    # Load input dataset
    bldg_econ_dmg.load_remote_input_dataset("buildings", bldg_dataset_id)
    bldg_econ_dmg.load_remote_input_dataset("building_mean_dmg", bldg_dmg_id)
    bldg_econ_dmg.load_remote_input_dataset("consumer_price_index", consumer_price_idx)

    # Specify the result name
    result_name = "seaside_bldg_econ_loss""

    # Set analysis parameters
    bldg_econ_dmg.set_parameter("result_name", result_name)
    bldg_econ_dmg.set_parameter("num_cpu", 4)

    # Run building economic loss analysis
    bldg_econ_dmg.run_analysis()
```

full analysis: [building_loss.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/building_loss.ipynb)