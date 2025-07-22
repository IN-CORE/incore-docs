# Pipeline repair cost

**Description**

This analysis estimates the repair costs of water pipeline for different simulation scenarios based on 
their damage states, replacement costs, and damage ratios.

**Contributors**

- Implementation: Hesam Talebiyan, Chen Wang, and NCSA IN-CORE Dev Team


**Input Parameters**

| key name                   | type  | name           | description                                                                            |
|----------------------------|-------|----------------|----------------------------------------------------------------------------------------|
| `result_name` <sup>*</sup> | `str` | Result name    | Name of the result dataset.                                                            |
| `num_cpu`                  | `int` | Number of CPUs | If using parallel execution, the number of cpus to request.                            |
| `diameter`                 | `int` | Diameter       | Pipeline diameter cutoff assumption for different damage ratios. Default is 20 inches. |
| `segment_length`           | `int` | Segment length | Segment length assumption. Default is 20 feet                                          |


**Input Datasets**

| key name                           | type                                              | name                                                    | description                                                                |
|------------------------------------|---------------------------------------------------|---------------------------------------------------------|----------------------------------------------------------------------------|
| `pipeline` <sup>*</sup>            | [`ergo:buriedPipelineTopology`](https://tools.in-core.org/semantics/api/types/ergo:buriedPipelineTopology)<br/>[`ergo:pipeline`](https://tools.in-core.org/semantics/api/types/ergo:pipeline) | Water Pipeline                                          | Water Pipeline.                                                            |
| `replacement_cost` <sup>*</sup>    | [`incore:replacementCost`](https://tools.in-core.org/semantics/api/types/incore:replacementCost)                          | Replacement Cost                                        | Repair cost of the node in the complete damage state (= Replacement cost). |
| `pipeline_dmg` <sup>*</sup>        | [`ergo:pipelineDamageVer3`](https://tools.in-core.org/semantics/api/types/ergo:pipelineDamageVer3)                         | Pipeline damage from PipelineDamageRepairRate Analysis. |
| `pipeline_dmg_ratios` <sup>*</sup> | [`incore:pipelineDamageRatios`](https://tools.in-core.org/semantics/api/types/incore:pipelineDamageRatios)                     | Damage Ratios Table                                     | Damage Ratios Table.                                                       |

**Output datasets** 

| key name              | type                        | name        | description                                                     |
|-----------------------|-----------------------------|-------------|-----------------------------------------------------------------|
| `result` <sup>*</sup> | [`incore:pipelineRepairCost`](https://tools.in-core.org/semantics/api/types/incore:pipelineRepairCost) | Repair Cost | A csv file with repair cost and budget for each water pipeline. |

<small>(* required)</small>

**Execution**

code snippet:

```
    client = IncoreClient()
    
    pipeline_repair_cost = PipelineRepairCost(client)

    pipeline_repair_cost.load_remote_input_dataset("pipeline_dmg", pipeline_dmg_id)
    pipeline_repair_cost.load_remote_input_dataset("pipeline_dmg_ratios", pipeline_dmg_ratios_id)
    pipeline_repair_cost.set_parameter("result_name", "pipeline")
    pipeline_repair_cost.set_parameter("num_cpu", 4)

    # Run Analysis
    pipeline_repair_cost.run_analysis()

```

full analysis: [pipeline_repair_cost.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/pipeline_repair_cost.ipynb)
