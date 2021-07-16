### Residential recovery

**Contributors**

- Scientific: Lisa Wang and John W. van de Lindt (CSU)
- Implementation: Gowtham Naraharisetty and Chris Navarro, Jong Sung Lee (NCSA, UIUC)

**Description**

This analysis focuses on the residential recovery in the aftermath of hazard events. The methodology incorporates the multi-layer 
Monte Carlo simulation approach and determines the two-step recovery time: downtime due to delay and downtime due to repair. 
The recovery time results could provide the time-stepping (e.g., monthly, quarterly, yearly) probabilistic recovery performance 
throughout the entire community for hazard events and keep track of the recovery trajectory of a single building or a single sector 
(e.g., household, business, healthcare, education). The analysis also shows the probabilities of housing units financed by different resources 
using real-world socio-demographic data with household income groups. 

Several delays inevitably take place before the initiation of building repairs, which would consequently increase the time needed 
for damaged buildings to reach any recovery states. The delay model was modified based on the REDi framework and calculated 
the end-result outcomes resulted from delay impeding factors such as post-disaster inspection, insurance claim, and government permit. 

The Jupyter notebook study presents the illustrated example of the Joplin testbed to explain the proposed methodology for wind events, 
and quantitatively measure the residential recovery performance impacted by policies. 

The output of the computation shows the functionality levels of residential buildings over the time in CSV format.

**Related publications**

- Sutley, Elaina J., and Sara Hamideh. "An interdisciplinary system dynamics model for post-disaster housing recovery." Sustainable and Resilient Infrastructure 3, no. 3 (2018): 109-127.
- Smith, Daniel J., and Daniel Sutter. "Response and recovery after the Joplin tornado: Lessons applied and lessons learned." The Independent Review 18, no. 2 (2013): 165-188.
- Lindell, Michael K., and Carla S. Prater. "Assessing community impacts of natural disasters." Natural hazards review 4, no. 4 (2003): 176-185.

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
`socio_demographic_data` <sup>*</sup> | `incore:socioDemograhicData` | Socio demographic | Socio-demographic data with household income group predictions.
`financial_resources` <sup>*</sup> | `incore:householdFinancialResources` | Financial resources | Financial resources by household income groups.
`delay_factors` <sup>*</sup> | `incore:buildingRecoveryFactors` | Delay factors | Delay impeding factors such as post-disaster inspection, insurance claim,<br>and government permit based on building's damage state. Provided by REDi framework.

**Output datasets**

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`residential_building_recovery` <sup>*</sup> | `incore:buildingRecovery` | Results | A dataset containing results (format: CSV)<br>with percentages of residential building recovery.

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create Residential recovery instance
    res_recovery = ResidentialRecovery(client)
    
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

full analysis: [joplin_residential_recovery.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/joplin_residential_recovery.ipynb)