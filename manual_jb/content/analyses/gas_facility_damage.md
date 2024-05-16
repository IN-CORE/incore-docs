# Gas facility damage

**Description**

This analysis computes gas facility damage based on a particular hazard. Currently supported hazards are: 
**earthquake**.

The process for computing the structural damage is similar to other parts of the built environment. First, a fragility
is obtained based on the hazard type and attributes of the building. Based on the fragility, the hazard intensity at the 
location of the building is computed. Using this information, the probability of exceeding each limit state is computed, 
along with the probability of damage. For the case of an earthquake hazard, soil information can be used to
modify the damage probabilities to include damage due to liquefaction.  

The outputs of this analysis are CSV file with probabilities of damage and JSON file with information about hazard and fragilities.

**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`hazard_type` | `str` | Hazard type | Hazard type (earthquake). 
`hazard_id` | `str` | Hazard id | ID of the hazard from the Hazard service.
`fragility_key` | `str` | Fragility key | Fragility key used in mapping dataset.
`use_liquefaction` | `bool` | Liquefaction | Use liquefaction, if applicable to the hazard. Default is <br>*False*.
`use_hazard_uncertainty` | `bool` | Uncertainty | Use hazard uncertainty.
`liquefaction_geology_dataset_id` | `str` | Liquefaction id | Liquefaction susceptibility dataset.
`liquefaction_fragility_key` | `str` | Fragility key | Fragility key used in mapping dataset.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. <br>Default *1*.

**Input Hazards**

key name | type | name | description
--- |-------|---------------| ---
`hazard` | `earthquake` | Hazard | Supported hazard object for using local and remote hazards.

**Input Datasets**

key name | type                                                                                                          | name | description
--- |---------------------------------------------------------------------------------------------------------------| --- | ---
`gas_facilities` <sup>*</sup> | [`ergo:gasFacilityInventory`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:gasFacilityInventory) | Facility dataset |  A gas facility dataset.
`dfr3_mapping_set` <sup>*</sup> | [`incore:dfr3MappingSet`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:dfr3MappingSet)         | DFR3 Mapping Set | DFR3 Mapping Set.

**Output datasets** 

key name | type                                                                                                                            | parent key       | name | description
--- |---------------------------------------------------------------------------------------------------------------------------------|------------------| --- | ---
`result` <sup>*</sup> | [`ergo:gasFacilityInventoryDamage`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:gasFacilityInventoryDamage)       | `gas_facilities` | Results | A dataset containing limit state and damage state probabilities <br>(format: CSV).
`metadata` <sup>*</sup> | [`incore:gasFacilityDamageSupplement`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:gasFacilityDamageSupplement) | `gas_facilities` | Results | Information about applied hazard value and fragility for each facility<br>(format: JSON).

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create gas facility damage analysis
    gf_dmg = GasFacilityDamage(client)

    # Load gas facility inventory dataset
    gf_dmg.load_remote_input_dataset("gas_facilities", facility_dataset_id)

    # Load fragility mapping
    fragility_service = FragilityService(client)
    mapping_set = MappingSet(fragility_service.get_mapping(mapping_id))
    gf_dmg.set_input_dataset('dfr3_mapping_set', mapping_set)

    # Specify result name
    result_name = "gf-dmg-results"

    # Set analysis parameters
    gf_dmg.set_parameter("result_name", result_name)
    gf_dmg.set_parameter("hazard_type", hazard_type)
    gf_dmg.set_parameter("hazard_id", hazard_id)
    gf_dmg.set_parameter("fragility_key", fragility_key)
    gf_dmg.set_parameter("use_liquefaction", liquefaction)
    gf_dmg.set_parameter("liquefaction_geology_dataset_id", liq_geology_dataset_id)
    gf_dmg.set_parameter("liquefaction_fragility_key", liq_fragility_key)
    gf_dmg.set_parameter("use_hazard_uncertainty", uncertainty)
    gf_dmg.set_parameter("num_cpu", 4)

    # Run gas facility damage analysis
    gf_dmg.run_analysis()
```

full analysis: [gas_facility_dmg.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/gas_facility_dmg.ipynb)
