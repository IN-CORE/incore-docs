### Pipeline damage with repair rate

This analysis computes water pipeline (with topology dataset) damage for Memphis based on earthquake.

The process for computing the structural damage is similar to other parts of the built environment. First, a fragility
is obtained based on the hazard type and attributes of the pipeline. Based on the fragility, the hazard intensity at the 
location of the pipeline is computed. Using this information, the probability of exceeding each limit state is computed, 
along with the probability of damage. If the pipeline dataset contains soil information, the median value of the associated 
fragility can be modified to account for liquefaction in the damage. 

The output of this analysis is a CSV file with probabilities of damage.
    
**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`mapping_id` <sup>*</sup> | `str` | Mapping id | ID of the mapping dataset from the DFR3 service.
`hazard_type` <sup>*</sup> | `str` | Hazard type | Earthquake hazard type.
`hazard_id` <sup>*</sup> | `str` | Hazard ID | ID of the hazard from the Hazard service.
`fragility_key` | `str` | Fragility key | Fragility key used in mapping dataset.
`use_liquefaction` | `bool` | Liquefaction | Use liquefaction, if applicable to the hazard.<br>Default is *False*.
`liquefaction_fragility_key` | `str` | Liquefaction key | Fragility key used in mapping dataset.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations.<br>Default *1*.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`pipeline` <sup>*</sup> | `ergo:buriedPipelineTopology`, <br>`ergo:pipeline` | Pipeline  dataset | A pipeline dataset.

**Output Datasets**

key name | type | name | description
--- | --- | --- | ---
`result` | `ergo:pipelineDamage` | Results | A dataset containing results (format: CSV).
<small>(* required)</small>

**Execution** 

code snipet:

```
    # Create pipeline damage with repair rate
    pipeline_dmg_w_rr = PipelineDamageRepairRate(client)

    # Load pipeline inventory as input datasets
    pipeline_dmg_w_rr.load_remote_input_dataset("pipeline", pipeline_dataset_id)

    # Specify the result name
    result_name = "pipeline_result"

    # Set analysis parameters
    pipeline_dmg_w_rr.set_parameter("result_name", result_name)
    pipeline_dmg_w_rr.set_parameter("mapping_id", mapping_id)
    pipeline_dmg_w_rr.set_parameter("hazard_type", hazard_type)
    pipeline_dmg_w_rr.set_parameter("hazard_id", hazard_id)
    pipeline_dmg_w_rr.set_parameter("liquefaction_fragility_key", liq_fragility_key)
    pipeline_dmg_w_rr.set_parameter("liquefaction_geology_dataset_id",liq_geology_dataset_id)
    pipeline_dmg_w_rr.set_parameter("use_liquefaction", use_liq)
    pipeline_dmg_w_rr.set_parameter("num_cpu", 4)

    # Run pipeline  damage analysis
    result = pipeline_dmg_w_rr.run_analysis()
```

full analysis: [pipeline_dmg_w_repair_rate.ipynb](https://github.com/IN-CORE/incore-docs/blob/develop/notebooks/pipeline_dmg_w_repair_rate.ipynb)