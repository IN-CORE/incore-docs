# Pipeline restoration

This analysis computes water pipeline restoration time after a particular hazard. The analysis itself is hazard agnostic, as it works
with the output of [Pipeline damage with repair rate analysis](pipeline_dmg_w_repair_rate.md) and restoration curves.

The restoration curves are obtained based on the hazard type and diameter-specific class of the pipeline. 
Based on the restoration curve applicable, we can obtain the time it takes to repair each of the pipelines. It considers
the leak rate, break rate, pipe length and the number of available workers to calculate the repair times. One of the inputs of
this analysis is the output of the [Pipeline damage with repair rate analysis](pipeline_dmg_w_repair_rate.md).

The output of this analysis is a CSV file with expected time taken to repair for each pipeline.
    
**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`num_available_workers` <sup>*</sup> | `str` | Number of available workers | Number of available workers to work on the repairs.
`restoration_key` <sup>*</sup> | `str` | Restoration Key | Restoration key to use in mapping dataset.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations.<br>Default 1.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`pipeline` <sup>*</sup> | [`ergo:buriedPipelineTopology`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buriedPipelineTopology)<br>[`ergo:pipeline`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:pipeline) | Pipeline  dataset | A pipeline dataset.
`pipeline_damage` <sup>*</sup> | [`ergo:pipelineDamageVer2`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:pipelineDamageVer2)<br>[`ergo:pipelineDamageVer3`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:pipelineDamageVer3) | Pipeline damage with repair rates dataset | A pipeline damage with repair rates dataset.
`dfr3_mapping_set` <sup>*</sup> | [`incore:dfr3MappingSet`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:dfr3MappingSet) | DFR3 Mapping Set | DFR3 Mapping Set.

**Output Datasets**

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`pipeline_restoration` <sup>*</sup> | [`incore:pipelineRestorationVer1`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:pipelineRestorationVer1) | `pipeline` | Results | Repair time for each pipeline<br>(format: CSV).

<small>(* required)</small>

**Execution** 

code snippet:

```
    # Create pipeline restoration
    pipeline_restoration = PipelineRestoration(client)

    # shelby county pipelines
    pipeline_restoration.load_remote_input_dataset("pipeline", pipeline_dataset_id)
    pipeline_restoration.load_remote_input_dataset("pipeline_damage", pipeline_dmg_dataset_id)

    # Load fragility mapping
    fragility_service = FragilityService(client)
    mapping_set = MappingSet(fragility_service.get_mapping(pipeline_restoration_mapping_id))
    pipeline_restoration.set_input_dataset('dfr3_mapping_set', mapping_set)

    pipeline_restoration.set_parameter("result_name", "pipeline_restoration_times")

    pipeline_restoration.set_parameter("restoration_key", "Restoration ID Code")
    pipeline_restoration.set_parameter("num_available_workers", 4)
    pipeline_restoration.set_parameter("num_cpu", 4)

    # Run pipeline restoration analysis
    pipeline_restoration.run_analysis()
```

full analysis: [pipeline_restoration.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/pipeline_restoration.ipynb)
