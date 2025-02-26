# Water facility repair cost

**Description**

This analysis estimates the repair costs of water facilities for different simulation scenarios based on 
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
`water_facilities` <sup>*</sup> | [`ergo:waterFacilityTopo`](https://tools.in-core.org/semantics/api/types/ergo:waterFacilityTopo) | Water Facilities | Water Facilities.
`replacement_cost` <sup>*</sup> | [`incore:replacementCost`](https://tools.in-core.org/semantics/api/types/incore:replacementCost) | Replacement Cost | Repair cost of the node in the complete damage state (= Replacement cost).
`sample_damage_states` <sup>*</sup> | [`incore:sampleDamageState`](https://tools.in-core.org/semantics/api/types/incore:sampleDamageState) | Sample Damage States | Sample damage states from Monte Carlo Simulation.
`wf_dmg_ratios` <sup>*</sup> | [`incore:waterFacilityDamageRatios`](https://tools.in-core.org/semantics/api/types/incore:waterFacilityDamageRatios) | Damage Ratios Table | Damage Ratios Table.

**Output datasets** 

key name | type | name | description
---|---|---|---
`result` <sup>*</sup> | [`incore:repairCost`](https://tools.in-core.org/semantics/api/types/incore:repairCost) | Repair Cost | A csv file with repair cost and budget for each water facility.

<small>(* required)</small>

**Execution**

code snippet:

```
    client = IncoreClient()
    
    wf_repair_cost = WaterFacilityRepairCost(client)

    wf_repair_cost.load_remote_input_dataset("water_facilities", water_facility_id)
    wf_repair_cost.load_remote_input_dataset("replacement_cost", replacement_cost_id)

    # can be chained with MCS
    wf_repair_cost.load_remote_input_dataset("sample_damage_states", sample_damage_states_id)

    # dmg ratiose
    wf_repair_cost.load_remote_input_dataset("wf_dmg_ratios", wf_dmg_ratios_id)

    wf_repair_cost.set_parameter("result_name", "wf")
    wf_repair_cost.set_parameter("num_cpu", 4)

    # Run Analysis
    wf_repair_cost.run_analysis()
```

full analysis: [water_facility_repair_cost.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/water_facility_repair_cost.ipynb)
