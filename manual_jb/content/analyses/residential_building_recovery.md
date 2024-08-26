# Residential building recovery

**Description**

This analysis computes the recovery time needed for each residential building from any damage states 
to achieve full restoration. Currently, supported hazards are **tornadoes**.

The methodology incorporates a multi-layer Monte Carlo simulation approach and 
determines the two-step recovery time which includes both the delay period and repair 
period. The delay model was modified based on the REDi framework and calculated 
the end-result outcomes resulting from delay impeding factors such as post-disaster 
inspection, insurance claims, and building permit issuance. The repair model followed 
the FEMA P-58 approach and ultimately utilized fragility functions from Koliou and 
van de Lindt (2020).

The outputs of this analysis is a CSV file with time-stepping recovery probabilities at the building level.

**Contributors**

- Science: Wanting Lisa Wang, John W. van de Lindt
- Implementation: Wanting Lisa Wang, Gowtham Naraharisetty, and NCSA IN-CORE Dev Team

**Related publications**

- Wang, Wanting Lisa, and John W. van de Lindt. "Quantitative Modeling of Residential Building Disaster Recovery and Effects of Pre-and Post-event Policies." *International Journal of Disaster Risk Reduction* (2021): 102259.
- Koliou, M. and J.W. van de Lindt. (2020). “Development of Building Restoration Functions for use in Community Recovery Planning to Tornadoes.”, *ASCE Natural Hazards Review*, Vol **21 (2)** doi.org10.1061/(ASCE)NH.1527-6996.0000361.

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
`buildings` <sup>*</sup> | [`ergo:buildingInventoryVer4`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingInventoryVer4)<br>[`ergo:buildingInventoryVer5`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingInventoryVer5)<br>[`ergo:buildingInventoryVer6`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingInventoryVer6)<br>[`ergo:buildingInventoryVer7`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingInventoryVer7) | Building dataset |  A building dataset.
`dfr3_mapping_set` <sup>*</sup> | [`incore:dfr3MappingSet`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:dfr3MappingSet) | DFR3 Mapping Set | DFR3 Mapping Set.
`sample_damage_states` <sup>*</sup> | [`incore:sampleDamageState`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:sampleDamageState) | Damage states | Sample damage states.
`socio_demographic_data` <sup>*</sup> | [`incore:socioDemograhicData`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:socioDemograhicData) | Socio demographic | Socio-demographic data with household income group predictions.
`financial_resources` <sup>*</sup> | [`incore:householdFinancialResources`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:householdFinancialResources) | Financial resources | Financial resources by household income groups.
`delay_factors` <sup>*</sup> | [`incore:buildingRecoveryFactors`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:buildingRecoveryFactors) | Delay factors | Delay impeding factors such as post-disaster inspection, insurance claim,<br>and government permit based on building's damage state. Provided by REDi framework.

**Output datasets**

key name | type | parent key | name                   | description
--- | --- | --- |------------------------| ---
`time_stepping_recovery` <sup>*</sup> | [`incore:buildingRecovery`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:buildingRecovery) | Results | Time Stepping Recovery | A dataset containing results (format: CSV)<br>with percentages of residential building recovery.
`total_delay` <sup>*</sup> | [`incore:buildingRecoveryDelay`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:buildingRecovery) | Results | Total Delay            | A dataset containing results (format: CSV)<br>with delay time of residential building recovery. 
`recovery` <sup>*</sup> | [`incore:buildingRecoveryTime`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:buildingRecovery) | Results | Recovery               | A dataset containing results (format: CSV)<br>with delay time of residential building recovery. 

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create Residential building recovery instance
    res_recovery = ResidentialBuildingRecovery(client)
    
    # Load input building infrastructure dataset
    res_recovery.load_remote_input_dataset("buildings", buildings)

    # Load repair mapping
    repair_service = RepairService(client)
    mapping_set = MappingSet(repair_service.get_mapping(mapping_id))
    res_recovery.set_input_dataset('dfr3_mapping_set', mapping_set)
    
    # Load input datasets  
    res_recovery.load_remote_input_dataset("sample_damage_states", sample_damage_states)
    res_recovery.load_remote_input_dataset("socio_demographic_data", socio_demographic_data)
    res_recovery.load_remote_input_dataset("financial_resources", financial_resources)
    res_recovery.load_remote_input_dataset("delay_factors", delay_factors)

    # Specify the result name
    result_name = "joplin_recovery"

    # Set analysis parameters
    res_recovery.set_parameter("result_name", result_name)
    res_recovery.set_parameter("seed", seed)
    res_recovery.set_parameter("num_samples", 10)

    # Run residential recovery analysis
    res_recovery.run_analysis()
```

full analysis: [residential_building_recovery.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/residential_building_recovery.ipynb)