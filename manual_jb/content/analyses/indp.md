# Interdependent Network Design Problem (INDP)

**Description**

This analysis takes a decentralized approach to solve the Interdependent Network Design Problem (INDP), a family of 
centralized Mixed-Integer Programming (MIP) models, which find the optimal restoration strategy of disrupted networked
systems subject to budget and operational constraints.

**Contributors**

- Implementation: Hesam Talebiyan, Chen Wang, and NCSA IN-CORE Dev Team

**Input parameters**

key name | type    | name                  | description
--- |---------|-----------------------| ---
`network_type` <sup>*</sup> | `str`   | Network Type          | Type of the network, which is set to `from_csv` for Seaside networks. e.g. *from_csv*, *incore*.
`MAGS` <sup>*</sup> | `list`  | MAGS                  | The earthquake return period.
`sample_range` <sup>*</sup> | `range` | Sample Range          | The range of sample scenarios to be analyzed.
`dislocation_data_type` | `str`   | Dislocation Data Type | Dislocation Data Type.
`return_model` | `str`   | Return Model          | Type of the model for the return of the dislocated population. Options: *step_function* and *linear*.
`testbed_name` | `str`   | Testbed Name          | Sets the name of the testbed in analysis.
`extra_commodity` <sup>*</sup> | `dict`  | Extra Commodity       | Multi-commodity parameters dictionary.
`RC` <sup>*</sup> | `list`  | Resource Caps         | List of resource caps or the number of available resources in each step of the analysis. Each item of the list is a dictionary whose items show the type of resource and the available number of that type of resource. For example: * If `FAIL_SCE_PARAM[TYPE]`=*from_csv*, you have two options:* if, for example, `R_c`= [{"budget": 3}, {"budget": 6}], then the analysis is done for the cases when there are 3 and 6 resources available of type "budget" (total resource assignment).* if, for example, `R_c`= [{"budget": {1:1, 2:1}}, {"budget": {1:1, 2:2}}, {"budget": {1:3, 2:3}}] and given there are 2 layers, then the analysis is done for the case where each layer gets 1 resource of type "budget", AND the case where layer 1 gets 1 and layer 2 gets 2 resources of type "budget", AND the case where each layer gets 3 resources of type "budget" (Prescribed resource for each layer).
`layers` <sup>*</sup> | `list`  | Layers                | List of layers in the analysis.
`method` <sup>*</sup> | `str`   | Method                | There are two choices of method: 1. `INDP`: runs Interdependent Network Restoration Problem (INDP). 2. `TDINDP`: runs time-dependent INDP (td-INDP).  In both cases, if "TIME_RESOURCE" is True, then the repair time for each element is considered in devising the restoration plans.
`t_steps` | `int`   | Time steps            | Number of time steps of the analysis.
`time_resource` | `bool`  | Time Resource         | If time resource is True, then the repair time for each element is considered in devising the restoration plans.
`save_model` | `bool`  | Save Model            | If the optimization model should be saved to file. The default is False.
`solver_engine` | `str`   | Solver Engine         | Solver to use for optimization model. Default to use SCIP solver.
`solver_path` | `str`   | Solver Engine Path    | Executable Path to the Solver to use for optimization model. Default to SCIP solver.
`solver_time_limit` | `int`   | Solve Time Limit      | Solving time limit in seconds.


**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`buildings` <sup>*</sup> | `ergo:buildingInventoryVer4`<br>`ergo:buildingInventoryVer5`<br>`ergo:buildingInventoryVer6`<br>`ergo:buildingInventoryVer7` | Building dataset |  A building dataset.
`dfr3_mapping_set` <sup>*</sup> | `incore:dfr3MappingSet` | DFR3 Mapping Set | DFR3 Mapping Set.
`retrofit_strategy` | `incore:retrofitStrategy` | Retrofit Strategy | Building retrofit strategy that contains guid and retrofit method.

**Output datasets**

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`ds_result` <sup>*</sup> | `ergo:buildingDamageVer5` | `buildings` | Results | A dataset containing results <br>(format: CSV).
`damage_result` <sup>*</sup> | `incore:buildingDamageSupplement` | `buildings` | Results | Information about applied hazard value and fragility<br>(format: JSON).

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create building damage
    bldg_dmg = BuildingDamage(client)

    # Load input dataset
    bldg_dmg.load_remote_input_dataset("buildings", bldg_dataset_id)

    # Load fragility mapping
    fragility_service = FragilityService(client)
    mapping_set = MappingSet(fragility_service.get_mapping(mapping_id))
    bldg_dmg.set_input_dataset('dfr3_mapping_set', mapping_set)

    # Specify the result name
    result_name = "memphis_bldg_dmg_result"

    # Set analysis parameters
    bldg_dmg.set_parameter("result_name", result_name)
    bldg_dmg.set_parameter("hazard_type", hazard_type)
    bldg_dmg.set_parameter("hazard_id", hazard_id)
    bldg_dmg.set_parameter("num_cpu", 10)

    # Run building damage analysis
    bldg_dmg.run_analysis()
```

full analysis: [building_dmg.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/building_dmg.ipynb)
