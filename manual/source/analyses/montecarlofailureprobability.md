 ### Monte Carlo failure probability

**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset, usually in CSV format which contains <br>the infrastructure damage information.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. Default *1*.
`num_samples` <sup>*</sup> | `int` | Number of MC samples | Number of Monte Carlo samples.
`damage_interval_keys` <sup>*</sup> | `list` | Damage interval keys | Column names of the damage intervals.
`failure_state_keys` <sup>*</sup> | `list` | Failure state keys | Column names of damager intervals that are considered damaged.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`damage` <sup>*</sup> | `ergo:buildingDamageVer4`, <br>`bridge-damage`, <br>`ergo:waterFacilityDamageVer4` | Damage | Damage results that has damage intervals in it.

**Output Datasets**

key name | type | name | description
--- | --- | --- | ---
`result` | `incore:failureProbability` | Results | A CSV file of failure probability.

<small>(* required)</small>

**Execution**

code snipet:

```
    # Create instance
    mc = MonteCarloFailureProbability(client)

    # Load remote datasets
    mc.load_remote_input_dataset("damage", damage_id)

    # Set analysis parameters
    mc.set_parameter("result_name", "mc_failure_probability")
    mc.set_parameter("num_samples", 10)
    mc.set_parameter("damage_interval_keys", ["insignific", "moderate", "heavy", "complete"])
    mc.set_parameter("failure_state_keys", ["moderate", "heavy", "complete"])

    mc.run_analysis()
```

**Chaining**

code snipet:

```
    # chaining with building damage
    bldg_dmg = BuildingDamage(client)
    bldg_dmg.load_remote_input_dataset("buildings", building_inventory_id)
    bldg_dmg.set_parameter("mapping_id", mapping_id)
    bldg_dmg.set_parameter("hazard_type", hazard_type)
    bldg_dmg.set_parameter("hazard_id", hazard_id)
    bldg_dmg.set_parameter("result_name", "building_damage")

    bldg_dmg.run_analysis()

    mc = MonteCarloFailureProbability(client)

    # This loads a local dataset from a file
    damage = Dataset.from_file("building_damage.csv", "ergo:buildingDamageVer4")
    mc.set_input_dataset("damage", damage)
    # If your data has been uploaded to the service, you can still use the load_remote_input_dataset with a damage id

    mc.set_parameter("result_name", "bldg_mc_failure_probability")
    mc.set_parameter("num_cpu", 8)
    mc.set_parameter("num_samples", 10)
    mc.set_parameter("damage_interval_keys", ["insignific", "moderate", "heavy", "complete"])
    mc.set_parameter("failure_state_keys", ["moderate", "heavy", "complete"])

    mc.run_analysis()
```

full analysis: [montecarlofailureprobability.ipynb](https://incore2.ncsa.illinois.edu/doc/examples/montecarlofailureprobability.ipynb)
