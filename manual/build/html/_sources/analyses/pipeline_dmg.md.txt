### Pipeline damage

This analysis computes pipeline damage based on earthquake hazard.

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
`hazard_type` <sup>*</sup> | `str` | Hazard type | Eearthquake hazard type.
`hazard_id` <sup>*</sup> | `str` | Hazard id | ID of the earthquake hazard from the Hazard service
`fragility_key` | `str` | Fragility key | Fragility key used in mapping dataset.
`liquefaction_geology_dataset_id` | `str` | Geology id | A geology dataset for liquefaction adjustment.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. <br>Default *1*.

**Input Datasets** 

key name | type | name | description
--- | --- | --- | ---
`pipeline` <sup>*</sup> | `ergo:buriedPipelineTopology`, <br>`ergo:pipeline` | Pipeline  dataset | A pipeline dataset.

**Output Datasets**

key name | type | name | description
--- | --- | --- | ---
`result` | `incore:pipelineDamage` | Results | A dataset containing results (format: CSV).

<small>(* required)</small>

**Execution**

code snipet:

```
    # Create instance
    pipeline_dmg = PipelineDamage(client)

    # Load input datasets
    pipeline_dmg.load_remote_input_dataset("pipeline", pipeline_id)

    # Set analysis parameters
    pipeline_dmg.set_parameter("result_name", "pipeline_damage_result")
    pipeline_dmg.set_parameter("mapping_id", mapping_id)
    pipeline_dmg.set_parameter("hazard_type", "earthquake")
    pipeline_dmg.set_parameter("fragility_key", "Non-Retrofit inundationDepth Fragility ID Code")
    pipeline_dmg.set_parameter("hazard_id", hazard_id)

    result = pipeline_dmg.run_analysis()
```

full analysis: [pipeline_dmg.ipynb](https://github.com/IN-CORE/pyincore/blob/master/pyincore/analyses/pipelinedamage/pipeline_dmg.ipynb)