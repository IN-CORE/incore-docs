### Pipeline damage

This analysis computes the damage to pipelines based on a particular hazard such as earthquake, tsunami
and tornado by calling fragility and hazard services.

The process is similar to evaluating other structural damages. The probabilities for pipeline damage
state are obtained using fragility curves and a hazard definition, each pipeline will have
a specific PGA (Peak Ground Acceleration), a measurement of an earthquake hazard for each scenario.
Liquefaction effect, which is defined as a change in stress condition, in which material that is ordinarily
a solid behaves like a liquid can be considered as well. The LMF (Liquefaction Modification Factor)
values are implemented as multiplication factors to the median fragility values and they must be present
in the dataset.

The code covers Normal and LogNormal fragilities with 4 limit states (slight, moderate, extensive
and complete) and creates an output CSV file.

**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset, usually in CSV format which contains <br>the infrastructure damage information.
`mapping_id` <sup>*</sup> | `str` | Mapping ID | Fragility mapping on Incore-service. It defines the fragilities to be used in the calculation.
`hazard_type` <sup>*</sup> | `str` | Hazard type | Hazard type for calculating pipeline damage (earthquake, tornado, tsunami, etc.).
`hazard_id` <sup>*</sup> | `str` | Hazard ID | Hazard ID for calculating pipeline damage.
`fragility_key` | `str` | Fragility key | Fragility key to use in mapping dataset. Default **.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. Default *1*.
`liquefaction_geology_dataset_id` | `str` | Geology dataset ID | Liquefaction geology/susceptibility dataset ID. <br>If not provided, liquefaction will be ignored.

**Input Datasets** 

key name | type | name | description
--- | --- | --- | ---
`pipeline` <sup>*</sup> | `ergo:buriedPipelineTopology`, <br>`ergo:pipeline` | Pipeline inventory | A pipeline dataset, usually a shape file <br>for which the damage is calculated.

**Output Datasets**

key name | type | name | description
--- | --- | --- | ---
`result` | `incore:pipelineDamage` | Results | A CSV file of bridge structural damage.

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

full analysis: [pipeline_dmg.ipynb](https://incore2.ncsa.illinois.edu/doc/examples/pipeline_dmg.ipynb)
