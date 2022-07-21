# Water facility network functionality

**Description**

This analysis computes the functionality of water facility networks.

The computation uses inputs from Monte Carlo failure analysis using water facility damage information, as well as 
pipeline functionality data to determine the functionality probability and failure states for a corresponding water 
facility network by performing a reachability analysis.

The output of the analysis consists of a CSV with functionality probabilities for water facilities, and a CSV 
with functionality failure states.

**Contributors**

- Science: Neetesh Sharma, Armin Tabandeh, Paolo Gardoni
- Implementation: Neetesh Sharma, Armin Tabandeh, Santiago Núñez-Corrales, and NCSA IN-CORE Dev Team

**Related publications**

* Sharma, N., Tabandeh, A., & Gardoni, P. (2019). Regional resilience analysis: A multi-scale approach to model the 
  recovery of interdependent infrastructure. In P. Gardoni (Ed.), *Handbook of sustainable and resilient 
  infrastructure* (pp. 521–544). New York, NY: Routledge.
* Sharma, N., Tabandeh, A., & Gardoni, P. (2020). Regional resilience analysis: A multi-scale approach to optimize 
  the resilience of interdependent infrastructure. *Computer‐Aided Civil and Infrastructure Engineering*, **35(12)**, 
  1315-1330.
* harma, N., & Gardoni, P. (2022). Mathematical modeling of interdependent infrastructure: An object-oriented 
  approach for generalized network-system analysis. *Reliability Engineering & System Safety*, **217**, 108042.

**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`tank_node_list` <sup>*</sup> | `list` | Tank node list | List of tank nodes within the network.
`pumpstation_node_list` <sup>*</sup> | `list` | Pump station list | List of pump station nodes within the network.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`wfn_network` <sup>*</sup> | `incore:waterNetwork` | Water Facility Network | Water Facility Network Dataset.
`wf_sample_failure_state` <sup>*</sup> | `incore:sampleFailureState` | Water Facilities Failure Sample States | Water Facilities Failure Sample States.
`pp_sample_failure_state` <sup>*</sup> | `incore:sampleFailureState` | Pipeline Functionality Failure Sample States | Pipeline Functionality Failure Sample States.

**Output datasets** 

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`failure_probability` <sup>*</sup> | `incore:failureProbability` | `water_facilities` | Probability of functionality results | A csv file recording the probability of functionality for water facilities.
`sample_failure_state` <sup>*</sup> | `incore:sampleFailureState` | `water_facilities` | Sample failure state results | A csv file recording sample failure states for water facilities.

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create water facility restoration analysis
    client = IncoreClient()
    wf_rest = WaterFacilityRestoration(client)

    # Run Water Facility Functionality analysis
    wfn_func = WfnFunctionality(client)

    wfn_func.load_remote_input_dataset("wfn_network", wfn_dataset_id)
    wfn_func.set_input_dataset("wf_sample_failure_state", wf_dmg_fs)
    wfn_func.set_input_dataset("pp_sample_failure_state", pp_dmg_fs)
    wfn_func.set_parameter("result_name", "mmsa_wfn_functionality")
    wfn_func.set_parameter("tank_node_list", [1, 7, 10, 13, 14, 15])
    wfn_func.set_parameter("pumpstation_node_list", [2, 3, 4, 5, 6, 8, 9, 11, 12])

    # Run Analysis
    wfn_func.run_analysis()
```

full analysis: [wfn_functionality.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/wfn_functionality.ipynb)