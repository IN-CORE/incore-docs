# Monte Carlo failure probability

**Description**

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
`damage_interval_keys` <sup>*</sup> | `List[str]` | Damage keys | Column names of the damage intervals.
`failure_state_keys` <sup>*</sup> | `List[str]` | Failure keys | Column names of damage intervals.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. <br>Default *1*.
`seed` | `int` | Seed | Initial seed for the probabilistic model to ensure reproducibility.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`damage` <sup>*</sup> | [`ergo:buildingDamageVer4`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingDamageVer4)<br>[`ergo:buildingDamageVer5`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingDamageVer5)<br>[`ergo:bridgeDamage`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:bridgeDamage)<br>[`ergo:bridgeDamageVer2`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:bridgeDamageVer2)<br>[`incore:epfDamage`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:epfDamage)<br>[`incore:epfDamageVer2`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:epfDamageVer2)<br>[`ergo:nsBuildingInventoryDamage`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:nsBuildingInventoryDamage)<br>[`ergo:nsBuildingInventoryDamageVer2`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:nsBuildingInventoryDamageVer2)<br>[`incore:pipelineDamage`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:pipelineDamage)<br>[`incore:pipelineDamageVer2`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:pipelineDamageVer2)<br>[`ergo:roadDamage`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:roadDamage)<br>[`ergo:roadDamageVer2`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:roadDamageVer2)<br>[`ergo:waterFacilityDamageVer4`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:waterFacilityDamageVer4)<br>[`ergo:waterFacilityDamageVer5`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:waterFacilityDamageVer5) | Infrastructure damage | A file with infrastructure damage intervals.

**Output Datasets**

key name | type | name | description
--- | --- | --- | ---
`failure_probability` <sup>*</sup> | [`incore:failureProbability`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:failureProbability) | Results | A dataset containing failure probability results <br>(format: CSV).
`sample_failure_state` <sup>*</sup> | [`incore:sampleFailureState`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:sampleFailureState) | Results | A dataset containing failure state for each sample <br>(format: CSV).
                    
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
    mc.set_parameter("failure_state_keys", ["DS_1", "DS_2", "DS_3"])
    mc.set_parameter("seed", 1111)

    # Run Monte Carlo failure
    mc.run_analysis()
```

full analysis: [mc_failure_prob.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/mc_failure_prob.ipynb)
