# Pipeline damage

**Description**

This analysis computes pipeline damage based on a particular hazard. Currently supported hazards are: **earthquake** and **tsunami**.

The process for computing the structural damage is similar to other parts of the built environment. First, a fragility
is obtained based on the hazard type and attributes of the pipeline. Based on the fragility, the hazard intensity at the 
location of the pipeline is computed. Using this information, the probability of exceeding each limit state is computed, 
along with the probability of damage. If the pipeline dataset contains soil information, the median value of the associated 
fragility can be modified to account for liquefaction in the damage. 

The outputs of this analysis are CSV file with probabilities of damage and JSON file with information about hazard and fragilities.

**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` | `str` | Result name | Name of the result dataset.
`hazard_type` | `str` | Hazard type (earthquake and tsunami).
`hazard_id` <sup>*</sup> | `str` | Hazard id | ID of the hazard from the Hazard service.
`fragility_key` | `str` | Fragility key | Fragility key used in mapping dataset.
`liquefaction_geology_dataset_id` | `str` | Geology id | A geology dataset for liquefaction adjustment.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. <br>Default *1*.

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
`result` <sup>*</sup> | `incore:pipelineDamageVer2` |`pipeline` | Results | A dataset containing results <br>(format: CSV).
`damage_result` <sup>*</sup> | `pipelineDamageSupplement` | `pipeline` | Results | Information about applied hazard value and fragility<br>(format: JSON).

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create Pipeline damage analysis
    pipeline_dmg = PipelineDamage(client)

    # Load pipeline inventory for Seaside, OR
    pipeline_dmg.load_remote_input_dataset("pipeline", pipeline_id)

    # Load fragility mapping
    fragility_service = FragilityService(client)
    mapping_set = MappingSet(fragility_service.get_mapping(mapping_id))
    pipeline_dmg.set_input_dataset('dfr3_mapping_set', mapping_set)

    # Set result name
    pipeline_dmg.set_parameter("result_name", "seaside_tsunami_pipeline_result")

    # Set a hazard: Seaside Tsunami
    pipeline_dmg.set_parameter("hazard_type", "tsunami")
    pipeline_dmg.set_parameter("hazard_id", hazard_id)

    # Set number of CPU for computation
    pipeline_dmg.set_parameter("num_cpu", 4)

    # Run pipeline damage analysis
    result = pipeline_dmg.run_analysis()
```

full analysis: [pipeline_dmg.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/pipeline_dmg.ipynb)
