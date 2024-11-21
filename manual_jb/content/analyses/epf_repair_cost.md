# Electric power facility repair cost

**Description**

This analysis estimates the repair costs of electric power facilities for different simulation scenarios based on 
their damage states, replacement costs, and damage ratios.

**Contributors**

- Implementation: Hesam Talebiyan, Chen Wang, and NCSA IN-CORE Dev Team


**Input Parameters**

key name | type  | name | description
--- |---|---|---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`num_cpu` | `int` | Number of CPUs | If using parallel execution, the number of cpus to request.

**Input Datasets**

key name | type | name | description
---|---|---|---
`epfs` <sup>*</sup> | [`incore:epf`](https://tools.in-core.org/semantics/api/types/incore:epf) <br> [`ergo:epf`](https://tools.in-core.org/semantics/api/types/ergo:epf) <br> [`incore:epfVer2`](https://tools.in-core.org/semantics/api/types/incore:epfVer2) | Electric Power Facilities | Electric Power Facilities.
`replacement_cost` <sup>*</sup> | [`incore:replacementCost`](https://tools.in-core.org/semantics/api/types/incore:replacementCost) | Replacement Cost | Repair cost of the node in the complete damage state (= Replacement cost).
`sample_damage_states` <sup>*</sup> | [`incore:sampleDamageState`](https://tools.in-core.org/semantics/api/types/incore:sampleDamageState) | Sample Damage States | Sample damage states from Monte Carlo Simulation.
`epf_dmg_ratios` <sup>*</sup> | [`incore:epfDamageRatios`](https://tools.in-core.org/semantics/api/types/incore:epfDamageRatios) | Damage Ratios Table | Damage Ratios Table.

**Output datasets** 

key name | type | name | description
---|---|---|---
`result` <sup>*</sup> | [`incore:repairCost`](https://tools.in-core.org/semantics/api/types/incore:repairCost) | Repair Cost | A csv file with repair cost and budget for each electric power facility.

<small>(* required)</small>

**Execution**

code snippet:

```
    client = IncoreClient()
    
    # Create electric power facility repair cost analysis
    epf_repair_cost = EpfRepairCost(client)

    epf_repair_cost.load_remote_input_dataset("epfs", epf_id)
    epf_repair_cost.load_remote_input_dataset("replacement_cost", replacement_cost_id)

    # Can be chained with MCS
    epf_repair_cost.load_remote_input_dataset("sample_damage_states", sample_damage_states_id)

    # damage ratios
    epf_repair_cost.load_remote_input_dataset("epf_dmg_ratios", epf_dmg_ratios_id)

    epf_repair_cost.set_parameter("result_name", "test_epf")
    epf_repair_cost.set_parameter("num_cpu", 4)

    # Run Analysis
    epf_repair_cost.run_analysis()
```

full analysis: [epf_repair_cost.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/epf_repair_cost.ipynb)

