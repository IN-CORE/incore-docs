# Interdependent Network Design Problem (INDP)

**Description**

This analysis takes a decentralized approach to solve the Interdependent Network Design Problem (INDP), a family of
centralized Mixed-Integer Programming (MIP) models, which find the optimal restoration strategy of disrupted networked
systems subject to budget and operational constraints.

**Contributors**

- Implementation: Hesam Talebiyan, Chen Wang, and NCSA IN-CORE Dev Team

**Input parameters**

 key name                       | type    | name                  | description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
--------------------------------|---------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 `network_type` <sup>*</sup>    | `str`   | Network Type          | Type of the network, which is set to `from_csv` for Seaside networks. e.g. *from_csv*, *incore*.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
 `MAGS` <sup>*</sup>            | `list`  | MAGS                  | The earthquake return period.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
 `sample_range` <sup>*</sup>    | `range` | Sample Range          | The range of sample scenarios to be analyzed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
 `dislocation_data_type`        | `str`   | Dislocation Data Type | Dislocation Data Type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
 `return_model`                 | `str`   | Return Model          | Type of the model for the return of the dislocated population. Options: *step_function* and *linear*.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
 `testbed_name`                 | `str`   | Testbed Name          | Sets the name of the testbed in analysis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
 `extra_commodity` <sup>*</sup> | `dict`  | Extra Commodity       | Multi-commodity parameters dictionary.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
 `RC` <sup>*</sup>              | `list`  | Resource Caps         | List of resource caps or the number of available resources in each step of the analysis. Each item of the list is a dictionary whose items show the type of resource and the available number of that type of resource. For example: * If `network_type`=*from_csv*, you have two options:* if, for example, `R_c`= [{"budget": 3}, {"budget": 6}], then the analysis is done for the cases when there are 3 and 6 resources available of type "budget" (total resource assignment).* if, for example, `R_c`= [{"budget": {1:1, 2:1}}, {"budget": {1:1, 2:2}}, {"budget": {1:3, 2:3}}] and given there are 2 layers, then the analysis is done for the case where each layer gets 1 resource of type "budget", AND the case where layer 1 gets 1 and layer 2 gets 2 resources of type "budget", AND the case where each layer gets 3 resources of type "budget" (Prescribed resource for each layer). 
 `layers` <sup>*</sup>          | `list`  | Layers                | List of layers in the analysis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
 `method` <sup>*</sup>          | `str`   | Method                | There are two choices of method: 1. `INDP`: runs Interdependent Network Restoration Problem (INDP). 2. `TDINDP`: runs time-dependent INDP (td-INDP).  In both cases, if "time_resource" is True, then the repair time for each element is considered in devising the restoration plans.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
 `t_steps`                      | `int`   | Time steps            | Number of time steps of the analysis.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
 `time_resource`                | `bool`  | Time Resource         | If time resource is True, then the repair time for each element is considered in devising the restoration plans.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
 `save_model`                   | `bool`  | Save Model            | If the optimization model should be saved to file. The default is False.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
 `solver_engine`                | `str`   | Solver Engine         | Solver to use for optimization model. Default to use SCIP solver.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
 `solver_path`                  | `str`   | Solver Engine Path    | Executable Path to the Solver to use for optimization model. Default to SCIP solver.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
 `solver_time_limit`            | `int`   | Solve Time Limit      | Solving time limit in seconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                

**Input datasets**

 key name                                    | type                                   | name                                       | description                                                                   
---------------------------------------------|----------------------------------------|--------------------------------------------|-------------------------------------------------------------------------------
 `wf_repair_cost` <sup>*</sup>               | `incore:repairCost`                    | Water Facility Repair Cost                 | Repair cost for each water facility.                                          
 `wf_restoration_time` <sup>*</sup>          | `incore:waterFacilityRepairTime`       | Water Facility Repair Time                 | Repair time at certain functionality recovery for each class and limit state. 
 `epf_repair_cost` <sup>*</sup>              | `incore:repairCost`                    | Electric Power Facility Repair Cost        | Repair cost for each electric power facility.                                 
 `epf_restoration_time` <sup>*</sup>         | `incore:epfRepairTime`                 | Electric Power Facility Repair Time        | Repair time at certain functionality recovery for each class and limit state. 
 `pipeline_repair_cost` <sup>*</sup>         | `incore:pipelineRepairCost`            | Water Pipeline Repair Cost                 | Repair cost for each water pipeline.                                          
 `pipeline_restoration_time` <sup>*</sup>    | `incore:pipelineRestorationVer1`       | Water Pipeline Resotarting Time            | Pipeline restoration times.                                                   
 `power_network` <sup>*</sup>                | `incore:epnNetwork`                    | Electric Power Network Dataset             | Electric power network dataset.                                               
 `water_network` <sup>*</sup>                | `incore:waterNetwork`                  | Water Network Dataset                      | Water network dataset.                                                        
 `powerline_supply_demand_info` <sup>*</sup> | `incore:powerLineSupplyDemandInfo`     | Powerline Supply Demand Info               | Supply and demand information for powerlines.                                 
 `epf_supply_demand_info` <sup>*</sup>       | `incore:epfSupplyDemandInfo`           | Electric Power Facility Supply Demand Info | Supply and demand information for electric power facilities.                  
 `wf_supply_demand_info` <sup>*</sup>        | `incore:waterFacilitySupplyDemandInfo` | Water Facility Supply Demand Info          | Supply and demand information for water facilities.                           
 `pipeline_supply_demand_info` <sup>*</sup>  | `incore:pipelineSupplyDemandInfo`      | Water Pipeline Supply Demand Info          | Supply and demand information for water pipelines.                            
 `interdep` <sup>*</sup>                     | `incore:interdep`                      | Interdependency                            | Interdepenency between water and electric power facilities.                   
 `wf_failure_state` <sup>*</sup>             | `incore:sampleFailureState`            | Water Facility Failure State               | MCS failure state of water facilities.                                        
 `wf_damage_state` <sup>*</sup>              | `incore:sampleDamageState`             | Water Facility Damage State                | MCS damage state of water facilities.                                         
 `pipeline_failure_state` <sup>*</sup>       | `incore:sampleFailureState`            | Water Pipeline Failure State               | Failure state of pipeline from pipeline functionality analysis.               
 `epf_failure_state` <sup>*</sup>            | `incore:sampleFailureState`            | Electric Power Facility Failure State      | MCS failure state of electric power facilities.                               
 `epf_damage_state` <sup>*</sup>             | `incore:sampleDamageState`             | Electric Power Facility Damage State       | MCS damage state of electric power facilities                                 
 `pop_dislocation` <sup>*</sup>              | `incore:popDislocation`                | Population Dislocation                     | Population dislocation.                                                       
 `bldgs2elec`                                | `incore:bldgs2elec`                    | Building To Electric Power Facility        | Relation between building and electric power facility.                        
 `bldgs2wter`                                | `incore:bldgs2wter`                    | Building To Water Facility                 | Relation between building and water facility.                                 

**Output datasets**

 key name               | type                 | parent key | name     | description                                                              
------------------------|----------------------|------------|----------|--------------------------------------------------------------------------
 `action` <sup>*</sup>  | `incore:indpAction`  |            | Action   | Restoration action plans.                                                
 `cost` <sup>*</sup>    | `incore:indpCost`    |            | Cost     | Restoration cost plans                                                   
 `runtime` <sup>*</sup> | `incore:indpRuntime` |            | Run Time | Run time duration (in second) to execute computations for each time step 

<small>(* required)</small>

**Execution**

code snippet:

```
    indp_analysis = INDP(client)
    indp_analysis.set_parameter("network_type", "from_csv")
    indp_analysis.set_parameter("MAGS", [1000])
    indp_analysis.set_parameter("sample_range", sample_range)
    indp_analysis.set_parameter("dislocation_data_type", "incore")
    indp_analysis.set_parameter("return_model", "step_function")
    indp_analysis.set_parameter("testbed_name", "seaside")
    indp_analysis.set_parameter("extra_commodity", {1: ["PW"], 3: []})
    indp_analysis.set_parameter("RC", [{"budget": 240000, "time": 700}, {"budget": 300000, "time": 600}])
    indp_analysis.set_parameter("layers", [1, 3])
    
    indp_analysis.set_parameter("method", "INDP")
    # indp_analysis.set_parameter("method", "TDINDP")
    
    indp_analysis.set_parameter("t_steps", 10)
    indp_analysis.set_parameter("time_resource", True)
    
    indp_analysis.set_parameter("save_model", False)
    # indp_analysis.set_parameter("save_model", True)
    
     # scip
    indp_analysis.set_parameter("solver_engine", "scip")
    indp_analysis.set_parameter("solver_path", "/usr/local/bin/scip")

    # glpk
    # indp_analysis.set_parameter("solver_engine", "glpk")
    # indp_analysis.set_parameter("solver_path", "/usr/local/bin/glpsol")

    # cbc
    # indp_analysis.set_parameter("solver_engine", "cbc")
    # indp_analysis.set_parameter("solver_path", "/usr/local/bin/cbc")

    # gurobi
    # indp_analysis.set_parameter("solver_engine", "gurobi")

    indp_analysis.set_parameter("solver_time_limit", 3600)  # if not set default to never timeout

    indp_analysis.set_input_dataset("wf_restoration_time", wf_restoration_time)
    indp_analysis.set_input_dataset("wf_repair_cost", wf_repair_cost_result)
    indp_analysis.set_input_dataset("epf_restoration_time", epf_restoration_time)
    indp_analysis.set_input_dataset("epf_repair_cost", epf_repair_cost_result)
    indp_analysis.set_input_dataset("pipeline_restoration_time", pipeline_restoration_time)
    indp_analysis.set_input_dataset("pipeline_repair_cost", pipeline_repair_cost_result)
    indp_analysis.set_input_dataset("power_network", power_network_dataset)
    indp_analysis.set_input_dataset("water_network", water_network_dataset)  # with distribution noes
    indp_analysis.load_remote_input_dataset("powerline_supply_demand_info", powerline_supply_demand_info_id)
    indp_analysis.load_remote_input_dataset("epf_supply_demand_info", epf_supply_demand_info_id)
    indp_analysis.load_remote_input_dataset("wf_supply_demand_info", wf_supply_demand_info_id)
    indp_analysis.load_remote_input_dataset("pipeline_supply_demand_info", pipeline_supply_demand_info_id)
    indp_analysis.load_remote_input_dataset("interdep", interdep_id)
    indp_analysis.set_input_dataset("wf_failure_state", wterfclty_sample_failure_state)
    indp_analysis.set_input_dataset("wf_damage_state", wterfclty_sample_damage_states)
    indp_analysis.set_input_dataset("pipeline_failure_state", pipeline_sample_failure_state)
    indp_analysis.set_input_dataset("epf_failure_state", epf_sample_failure_state)
    indp_analysis.set_input_dataset("epf_damage_state", epf_sample_damage_states)
    indp_analysis.set_input_dataset("pop_dislocation", pop_dislocation_result)

    # # optional inputs
    # indp_analysis.load_remote_input_dataset("bldgs2elec", bldgs2elec_id)
    # indp_analysis.load_remote_input_dataset("bldgs2wter", bldgs2wter_id)

    # Run Analysis
    indp_analysis.run_analysis()
```

full analysis: [indp.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/indp.ipynb)
