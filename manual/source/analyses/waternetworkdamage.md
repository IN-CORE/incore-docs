### Water network damage

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`water_facility_mapping_id` <sup>*</sup> | `str` | Water mapping id | Default water facility fragility mapping <br>on Incore-service. It implicitly defines the fragilities to be used in the calculation.
`water_pipeline_mapping_id` <sup>*</sup> | `str` | Pipeline mapping id | Default pipeline fragility mapping <br>on Incore-service. It implicitly defines the fragilities to be used in the calculation.
`earthquake_id` <sup>*</sup> | `str` | Hazard id | Hazard ID for calculating water network damage.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. Default *1*.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`water_network` <sup>*</sup> | `incore:waternetwork` | Water dataset id | Water network dataset.

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`pipeline_dmg` <sup>*</sup> | `ergo:pipelineDamage` | Pipeline results | A csv file of pipeline structural damage.
`tank_dmg` <sup>*</sup> | `ergo:pumpDamage` | Tank results | A csv file of tank structural damage.
`pump_dmg` <sup>*</sup> | `ergo:lifelineWaterTankInventoryDamage` | Pump results | A csv file of pump structural damage.

<small>(* required)</small>

**Execution**

code snipet:

```
    # Create water network damage instance
    wn_dmg = WaterNetworkDamage(client)

    # Load input datasets
    wn_dmg.load_remote_input_dataset("water_facilities", water_facilities)

    # Set analysis parameters
    wn_dmg.set_parameter("earthquake_id", 'earthquake_id')
    wn_dmg.set_parameter("water_facility_mapping_id", 'water_facility_mapping_id')
    wn_dmg.set_parameter("water_pipeline_mapping_id",'water_pipeline_mapping_id')
    wn_dmg.set_parameter("num_cpu", 4)

    # Run water network damage analysis
    wn_dmg.run_analysis()
```

full analysis: [Water_Network_Analysis.ipynb](https://incore2.ncsa.illinois.edu/doc/examples/Water_Network_Analysis.ipynb)
full analysis: [Complete_Water_Network_Analysis.ipynb](https://incore2.ncsa.illinois.edu/doc/examples/Complete_Water_Network_Analysis.ipynb)