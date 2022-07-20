# EPN functionality analysis

**Description**
    
**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`gate_station_node_list` <sup>*</sup> | `list` | Gate Station Node list | List of node IDs that represents the gate station.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`epn_network` <sup>*</sup> | `incore:epnNetwork` | EPN Network | EPN network dataset
`epf_sample_failure_state` <sup>*</sup> | `incore:sampleFailureState` | EPF sample failure state | CSV file of failure state for each sample. Output from MCS analysis.

**Output Datasets**

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`failure_probability` <sup>*</sup> | `incore:failureProbability` | Results | A dataset containing failure probability results <br>(format: CSV).
`sample_failure_state` <sup>*</sup> | `incore:sampleFailureState` | Results | A dataset containing failure state for each sample <br>(format: CSV).
                    
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

full analysis: [epn_functionality.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/epn_functionality.ipynb)