 ### Monte Carlo failure probability

**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`num_samples` <sup>*</sup> | `int` | Samples | Number of Monte Carlo samples.
`damage_interval_keys` <sup>*</sup> | `list` | Damage keys | Column names of the damage intervals.
`failure_state_keys` <sup>*</sup> | `list` | Failure keys | Column names of damage intervals.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. <br>Default *1*.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`damage` <sup>*</sup> | `ergo:buildingDamageVer4`, <br>`bridge-damage`, <br>`ergo:waterFacilityDamageVer4` | Infrastructure damage | A file with infrastructure damage intervals.

**Output Datasets**

key name | type | name | description
--- | --- | --- | ---
`result` | `incore:failureProbability` | Results | A dataset containing results <br>(format: CSV).

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
    mc.set_parameter("num_cpu", 8)
    mc.set_parameter("num_samples", 10)
    mc.set_parameter("damage_interval_keys", ["insignific", "moderate", "heavy", "complete"])
    mc.set_parameter("failure_state_keys", ["moderate", "heavy", "complete"])

    # Run Monte Carlo failure
    mc.run_analysis()
```

full analysis: [montecarlofailureprobability.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/montecarlofailureprobability.ipynb)