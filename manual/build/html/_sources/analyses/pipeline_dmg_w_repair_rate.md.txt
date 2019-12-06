### Pipeline damage with repair rate

Memphis water buried pipeline with topology dataset, the Ergo repository
    
**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset, usually in a CSV format which contains <br>the infrastructure damage and repair information.
`mapping_id` <sup>*</sup> | `str` | Fragility mapping dataset | Fragility mapping on Incore-service. It defines the fragilities to be used in the calculation.
`hazard_type` <sup>*</sup> | `str` | Hazard type | Hazard type for calculating damage (earthquake, tornado, tsunami, etc.).
`hazard_id` <sup>*</sup> | `str` | Hazard ID | Hazard ID for calculating damage.
`fragility_key` | `str` | Fragility key | The key to use in the mapping dataset. Default depends on the hazard type specified.
`use_liquefaction` | `bool` | Liquefaction | Whether to use liquefaction or not. Default is *False*.
`liquefaction_fragility_key` | `str` | Liquefaction Fragility key | Fragility key to use in liquefaction.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. Default *1*.
`liquefaction_geology_dataset_id` | `str` | Liquefaction geology dataset | Liquefaction geology/susceptibility dataset id. <br>If not provided, liquefaction will be ignored.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`pipeline` <sup>*</sup> | `ergo:buriedPipelineTopology`, <br>`ergo:pipeline` | Pipeline Inventory | An infrastructure dataset, usually a shape file for which the damage is calculated.

**Output Datasets**

key name | type | name | description
--- | --- | --- | ---
`result` | `ergo:pipelineDamage` | Pipeline damage | A CSV file of pipeline damage.

<small>(* required)</small>

**Execution** 

code snipet:

```
    # Create instance
    pipeline_dmg = PipelineDamageRepairRate(client)

    # Load input datasets
    pipeline_dmg.load_remote_input_dataset("pipeline", pipeline_dataset_id)

    # Set analysis parameters
    pipeline_dmg.set_parameter("result_name", "pipeline_result")
    pipeline_dmg.set_parameter("mapping_id", mapping_id)
    pipeline_dmg.set_parameter("hazard_type", "earthquake")
    pipeline_dmg.set_parameter("hazard_id", hazard_id)
    pipeline_dmg.set_parameter("num_cpu", 4)

    result = pipeline_dmg.run_analysis()
```

full analysis: [pipeline_dmg_w_repair_rate.ipynb](https://incore2.ncsa.illinois.edu/doc/examples/pipeline_dmg_w_repair_rate.ipynb)
