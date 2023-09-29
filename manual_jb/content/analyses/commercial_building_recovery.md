# Commerical building recovery

**Description**

This analysis computes the recovery time needed for each commercial building from any damage states to receive the
full restoration. Currently, supported hazards are tornadoes.

The methodology incorporates the multi-layer Monte Carlo simulation approach and determines the two-step recovery
time that includes delay and repair. The delay model was modified based on the REDi framework and calculated the
end-result outcomes resulted from delay impeding factors such as post-disaster inspection, insurance claim,
financing and government permit. The repair model followed the FEMA P-58 approach and was controlled by fragility
functions.

The outputs of this analysis is a CSV file with time-stepping recovery probabilities at the building level.

**Contributors**

- Science: Wanting Lisa Wang, John W. van de Lindt
- Implementation: Wanting Lisa Wang and NCSA IN-CORE Dev Team

**Related publications**

- Wang, W.L., Watson, M., van de Lindt, J.W. and Xiao, Y., 2023. Commercial Building Recovery Methodology for Use
        in Community Resilience Modeling. Natural Hazards Review, 24(4), p.04023031.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`num_samples` <sup>*</sup> | `int` | Samples number | Number of sample scenarios.
`seed` | `int` | Seed | Initial seed for the probabilistic model.
`repair_key` | `str` | Repair key | A repair key to use in mapping dataset.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`buildings` <sup>*</sup> | `ergo:buildingInventoryVer4`<br>`ergo:buildingInventoryVer5`<br>`ergo:buildingInventoryVer6`<br>`ergo:buildingInventoryVer7` | Building dataset |  A building dataset.
`dfr3_mapping_set` <sup>*</sup> | `incore:dfr3MappingSet` | DFR3 Mapping Set | DFR3 Mapping Set.
`sample_damage_states` <sup>*</sup> | `incore:sampleDamageState` | Damage states | Sample damage states.
`mcs_failure` <sup>*</sup> | `incore:failureProbability` | MCS failure | mcs_failure.
`delay_factors` <sup>*</sup> | `incore:buildingRecoveryFactors` | Delay factors | Delay impeding factors such as post-disaster inspection, insurance claim,<br>and government permit based on building's damage state. Provided by REDi framework.

**Output datasets**

key name | type | parent key              | name | description
--- | --- |-------------------------| --- | ---
`time_stepping_recovery` <sup>*</sup> | `incore:buildingRecovery` | Results                 | A dataset containing results (format: CSV)<br>with percentages of commerical building recovery.
`recovery` <sup>*</sup> | `incore:buildingRecoveryTime` | Building Recovery Time  | A dataset containing results (format: CSV)<br>with commerical building recovery time.
`total_delay` <sup>*</sup> | `incore:buildingRecoveryDelay` | Building Recovery Delay | A dataset containing results (format: CSV)<br>with commerical building delay time.

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create Commerical building recovery instance
    comm_recovery = CommericalBuildingRecovery(client)
    
    # Load input building infrastructure dataset
    comm_recovery.load_remote_input_dataset("buildings", buildings)

    # Load repair mapping
    repair_service = RepairService(client)
    mapping_set = MappingSet(repair_service.get_mapping(mapping_id))
    comm_recovery.set_input_dataset('dfr3_mapping_set', mapping_set)
    
    # Load input datasets
    com_recovery.load_remote_input_dataset("sample_damage_states", sample_damage_states)
    com_recovery.load_remote_input_dataset("mcs_failure", mcs_failure)
    com_recovery.load_remote_input_dataset("delay_factors", delay_factors)

    # Specify the result name
    result_name = "joplin_recovery"

    # Set analysis parameters
    comm_recovery.set_parameter("result_name", result_name)
    comm_recovery.set_parameter("seed", seed)
    comm_recovery.set_parameter("num_samples", 10)

    # Run commerical recovery analysis
    comm_recovery.run_analysis()
```

full analysis: [commerical_building_recovery.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/commerical_building_recovery.ipynb)