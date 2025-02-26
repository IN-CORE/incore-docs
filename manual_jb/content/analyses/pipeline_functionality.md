# Pipeline functionality analysis

**Description**

This analysis computes pipeline functionality using repair rate calculations from pipeline damage analysis. 
The computation operates by computing Monte Carlo samples derived from Poisson sample deviates from the damage analysis as input to Bernoulli experiments, later used to determine average functionality.

The output of this analysis are two CSV files; a failure proability *base_name*_failure_probability.csv
and *base_name*_failure_state.csv.
    
**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`num_samples` <sup>*</sup> | `int` | Samples | Number of samples for Bernoulli distribution.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`pipeline_repair_rate_damage` <sup>*</sup> | [`ergo:pipelineDamageVer3`](https://tools.in-core.org/semantics/api/types/ergo:pipelineDamageVer3) | pipeline Damage | Output of the pipeline damage repair rate analysis

**Output Datasets**

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`failure_probability` <sup>*</sup> | [`incore:failureProbability`](https://tools.in-core.org/semantics/api/types/incore:failureProbability) | Results | A dataset containing failure probability results <br>(format: CSV).
`sample_failure_state` <sup>*</sup> | [`incore:sampleFailureState`](https://tools.in-core.org/semantics/api/types/incore:sampleFailureState) | Results | A dataset containing failure state for each sample <br>(format: CSV).
                    
<small>(* required)</small>

**Execution** 

code snippet:

```
    # Create pipeline functionality
    pipline_func = PipelineFunctionality(client)

    # Load input datasets
    pipline_func.load_remote_input_dataset("pipeline_repair_rate_damage", pipeline_damage_id)
    # Load fragility mapping

    # Set analysis parameters
    pipline_func.set_parameter("result_name", result_name)
    pipline_func.set_parameter("num_samples", 100)

    # Run pipeline analysis
    result = pipline_func.run_analysis()
```

full analysis: [pipeline_functionality.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/pipeline_functionality.ipynb)