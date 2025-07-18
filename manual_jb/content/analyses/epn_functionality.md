# Electric power network functionality

This analysis computes the functionality of electric power networks.

The computation uses inputs from Monte Carlo failure analysis using electric power facility damage information, as 
well as the network topology of electric power line to determine the functionality probability and failure states 
for a corresponding electric power facility network by performing a reachability analysis.

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
* Sharma, N., & Gardoni, P. (2022). Mathematical modeling of interdependent infrastructure: An object-oriented 
  approach for generalized network-system analysis. *Reliability Engineering & System Safety*, **217**, 108042.
    
**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`gate_station_node_list` <sup>*</sup> | `List[int]` | Gate Station Node list | List of node IDs that represents the gate station.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`epn_network` <sup>*</sup> | [`incore:epnNetwork`](https://tools.in-core.org/semantics/api/types/incore:epnNetwork) | EPN Network | EPN network dataset
`epf_sample_failure_state` <sup>*</sup> | [`incore:sampleFailureState`](https://tools.in-core.org/semantics/api/types/incore:sampleFailureState) | EPF sample failure state | CSV file of failure state for each sample. Output from MCS analysis.

**Output Datasets**

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`failure_probability` <sup>*</sup> | [`incore:failureProbability`](https://tools.in-core.org/semantics/api/types/incore:failureProbability) | Results | A dataset containing failure probability results <br>(format: CSV).
`sample_failure_state` <sup>*</sup> | [`incore:sampleFailureState`](https://tools.in-core.org/semantics/api/types/incore:sampleFailureState) | Results | A dataset containing failure state for each sample <br>(format: CSV).
                    
<small>(* required)</small>

**Execution** 

code snippet:

```
    # run epn functionality
    epn_func = EpnFunctionality(client)
    epn_func.load_remote_input_dataset("epn_network", epn_dataset_id)
    epn_func.load_remote_input_dataset("epf_sample_failure_state", epf_sample_failure_state_id)

    epn_func.set_parameter("result_name", result_name)
    epn_func.set_parameter("gate_station_node_list", [1, 2, 3, 4, 5, 6, 7, 8, 9])

    # Run Analysis
    epn_func.run_analysis()
```

full analysis: [epn_functionality.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/epn_functionality.ipynb)
