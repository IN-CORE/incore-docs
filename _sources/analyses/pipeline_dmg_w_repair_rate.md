# Pipeline damage with repair rate

**Description**

This analysis computes water pipeline damage based on a particular hazard. Currently supported hazards is: **earthquake**.

The process for computing the structural damage is similar to other parts of the built environment. First, a fragility
is obtained based on the hazard type and attributes of the pipeline. Based on the fragility, the hazard intensity at the 
location of the pipeline is computed. Using this information, the probability of exceeding each limit state is computed, 
along with the probability of damage. If the pipeline dataset contains soil information, the median value of the associated 
fragility can be modified to account for liquefaction in the damage. 

The outputs of this analysis are CSV file with probabilities of damage and JSON file with information about hazard and fragilities.
    
**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`hazard_type` | `str` | Hazard type | Earthquake hazard type.
`hazard_id` | `str` | Hazard ID | ID of the hazard from the Hazard service.
`fragility_key` | `str` | Fragility key | Fragility key used in mapping dataset.
`use_liquefaction` | `bool` | Liquefaction | Use liquefaction, if applicable to the hazard.<br>Default is *False*.
`liquefaction_fragility_key` | `str` | Liquefaction key | Fragility key used in mapping dataset.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations.<br>Default *1*.

**Input Hazards**

key name | type | name | description
--- |---|---| ---
`hazard` | `earthquake`<br>`tsunami` | Hazard | Supported hazard object for using local and remote hazards.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`pipeline` <sup>*</sup> | `ergo:buriedPipelineTopology`, <br>`ergo:pipeline` | Pipeline  dataset | A pipeline dataset.
`dfr3_mapping_set` <sup>*</sup> | `incore:dfr3MappingSet` | DFR3 Mapping Set | DFR3 Mapping Set.

**Output Datasets**

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`result` <sup>*</sup> | `ergo:pipelineDamageVer2` | `pipeline` | Results | A dataset containing results <br>(format: CSV).
`damage_result` <sup>*</sup> | `incore:pipelineDamageSupplement` | `pipeline` | Results | Information about applied hazard value and fragility<br>(format: JSON).

<small>(* required)</small>

**Execution** 

code snippet:

```
    # Create pipeline damage with repair rate
    pipeline_dmg_w_rr = PipelineDamageRepairRate(client)

    # Load pipeline inventory as input datasets
    pipeline_dmg_w_rr.load_remote_input_dataset("pipeline", pipeline_dataset_id)

    # Load fragility mapping
    fragility_service = FragilityService(client)
    mapping_set = MappingSet(fragility_service.get_mapping(mapping_id))
    pipeline_dmg_w_rr.set_input_dataset('dfr3_mapping_set', mapping_set)

    # Specify the result name
    result_name = "pipeline_result"

    # Set analysis parameters
    pipeline_dmg_w_rr.set_parameter("result_name", result_name)
    pipeline_dmg_w_rr.set_parameter("hazard_type", hazard_type)
    pipeline_dmg_w_rr.set_parameter("hazard_id", hazard_id)
    pipeline_dmg_w_rr.set_parameter("liquefaction_fragility_key", liq_fragility_key)
    pipeline_dmg_w_rr.set_parameter("liquefaction_geology_dataset_id",liq_geology_dataset_id)
    pipeline_dmg_w_rr.set_parameter("use_liquefaction", use_liq)
    pipeline_dmg_w_rr.set_parameter("num_cpu", 4)

    # Run pipeline  damage analysis
    result = pipeline_dmg_w_rr.run_analysis()
```

full analysis: [pipeline_dmg_w_repair_rate.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/pipeline_dmg_w_repair_rate.ipynb)
