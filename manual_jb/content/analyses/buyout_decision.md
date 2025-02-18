# Buyout Decision

**Description**

This analysis helps identify candidate properties for buyout and allows practitioners and researchers to evaluate 
the potential equity outcomes of their selection under different scenario events.

The outputs of this analysis is a CSV file with buildings to consider for buyout based on the set criteria. This can assist local 
practitioners to identify candidate properties for buyout selection and allows practitioners and researchers to evaluate the potential equity 
outcomes of their selection 

**Input parameters**

key name | type | name | description
--- |-------------------------|-------------------------| ---
`result_name` <sup>*</sup> | `str`                   | Result name             | Name of the result dataset.
`residential_archetypes` <sup>*</sup> | `list`                  | Residential archtetypes | Residential archetypes to consider for buyout.
`fema_buyout_cap` <sup>*</sup> | `float`                 | FEMA buyout cap | FEMA buyout cap is the maximum appraised value considered for buyout. 

**Input datasets**

key name | type | name | description
--- |-------------------------|-------------------------| ---
`buildings` <sup>*</sup> | [`ergo:buildingInventoryVer4`](https://tools.in-core.org/semantics/api/types/ergo:buildingInventoryVer4)<br>[`ergo:buildingInventoryVer5`](https://tools.in-core.org/semantics/api/types/ergo:buildingInventoryVer5)<br>[`ergo:buildingInventoryVer6`](https://tools.in-core.org/semantics/api/types/ergo:buildingInventoryVer6)<br>[`ergo:buildingInventoryVer7`](https://tools.in-core.org/semantics/api/types/ergo:buildingInventoryVer7) | Building dataset         |  A building dataset.
`past_building_damage` <sup>*</sup> | [`ergo:buildingDamageVer6`](https://incore.ncsa.illinois.<br/>edu/semantics/api/types/ergo:buildingDamageVer6) | Previous Building damage |  Building damage from a previous event.
`future_building_damage` <sup>*</sup> | [`ergo:buildingDamageVer6`](https://incore.ncsa.illinois.<br/>edu/semantics/api/types/ergo:buildingDamageVer6) | Future/predicted Building damage |  Building damage from a future/predicted event.
`housing_unit_allocation` <sup>*</sup> | [`incore:housingUnitAllocation`](https://tools.in-core.org/semantics/api/types/incore:housingUnitAllocation) | Housing unit allocation | Housing unit allocation.
`population_dislocation` <sup>*</sup> | [`incore:popDislocation`](https://tools.in-core.org/semantics/api/types/incore:popDislocation) | Population dislocation   | Population dislocation results.


**Output datasets**

key name | type | parent key | name | description
--- |-------------------------------------------------------------------------------------------------------| --- | --- | ---
`result` <sup>*</sup> | [`incore:buyoutDecision`](https://tools.in-core.org/semantics/api/types/incore:buyoutDecision) | `buildings` | Results | A dataset containing buyout decision results <br>(format: CSV).

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create buyout analysis
    buyout_decision = BuyoutDecision(client)

    # Load input datasets
    buyout_decision.load_remote_input_dataset("buildings", buildings_id)
    buyout_decision.load_remote_input_dataset("housing_unit_allocation", hua_id)
    buyout_decision.load_remote_input_dataset("past_building_damage", past_building_damage_id)
    buyout_decision.load_remote_input_dataset("future_building_damage", future_building_damage_id)
    buyout_decision.load_remote_input_dataset("population_dislocation", past_pop_dislocation_id)


    # Specify the result name
    result_name = "galveston_buyout_result"
    
    # Set analysis parameters
    buyout_decision.set_parameter("fema_buyout_cap", fema_buyout_cap)
    buyout_decision.set_parameter("residential_archetypes", residential_archetypes)
    buyout_decision.set_parameter("result_name", result_name)

    # Run buyout analysis
    buyout_decision.run_analysis()
```

full analysis: [buyout_decision.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/buyout_decision.ipynb)
