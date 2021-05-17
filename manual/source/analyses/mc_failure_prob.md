 ### Monte Carlo failure probability

This analysis calculates a probability of failure using a stochastic process. Failure probability and Failure state are derived 
using the dictionary of failed damage states in the input infrastructure dataset. Failure probability is calculated from all
stochastic runs, failure state shows all infrastructure standings as a string of *failed* (0) and *not failed* (1) states 
of each individual run.

The output of this analysis are two CSV files; a failure proability *base_name*_failure_probability.csv with allocated house units
and  *base_name*_failure_state.csv.
                                
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
`damage` <sup>*</sup> | `ergo:buildingDamageVer4`<br>`ergo:buildingDamageVer5`<br>`ergo:bridgeDamage`<br>`incore:epfDamage`<br>`ergo:nsBuildingInventoryDamage`<br>`ergo:nsBuildingInventoryDamageVer2`<br>`incore:pipelineDamage`<br>`ergo:roadDamage`<br>`ergo:waterFacilityDamageVer4` | Infrastructure damage | A file with infrastructure damage intervals.
                        
**Output Datasets**

key name | type | name | description
--- | --- | --- | ---
`failure_probability` | `incore:failureProbability` | Results | A dataset containing failure probability results <br>(format: CSV).
`sample_failure_state` | `incore:sampleFailureState` | Results | A dataset containing failure state for each sample <br>(format: CSV).
                    
<small>(* required)</small>

**Execution**

code snippet:

```
    # Create instance
    mc = MonteCarloFailureProbability(client)

    # Load remote datasets
    mc.load_remote_input_dataset("damage", damage_id)

    # Set analysis parameters
    mc.set_parameter("result_name", "mc_failure_probability")
    mc.set_parameter("num_cpu", 8)
    mc.set_parameter("num_samples", 10)
    mc.set_parameter("damage_interval_keys", ["DS_0", "DS_1", "DS_2", "DS_3"])
    mc.set_parameter("failure_state_keys", ["moderate", "heavy", "complete"])

    # Run Monte Carlo failure
    mc.run_analysis()
```

full analysis: [mc_failure_prob.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/mc_failure_prob.ipynb)