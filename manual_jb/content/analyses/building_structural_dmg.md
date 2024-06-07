# Building structural damage

**Description**

This analysis computes building structural damage based on a particular hazard. Currently supported hazards are: **earthquake**, 
**tsunami**, **tornado**, **hurricane** and **flood**.

The process for computing the structural damage is similar to other parts of the built environment. First, a fragility
is obtained based on the hazard type and attributes of the building. Based on the fragility, the hazard intensity at the 
location of the building is computed. Using this information, the probability of exceeding each limit state is computed, 
along with the probability of damage. For the case of an earthquake hazard, soil information can be used to
modify the damage probabilities to include damage due to liquefaction.  

The outputs of this analysis are CSV file with probabilities of damage and JSON file with information about hazard and fragilities.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`hazard_type` <sup>*</sup> | `str` | Hazard type | Hazard type (earthquake, tsunami, tornado, hurricaneWindfields).
`hazard_id` <sup>*</sup> | `str` | Hazard id | ID of the hazard from the Hazard service.
`fragility_key` | `str` | Fragility key | Fragility key used in mapping dataset.
`use_liquefaction` | `bool` | Liquefaction | Use liquefaction, if applicable to the hazard. <br>Default is *False*.
`use_hazard_uncertainty` | `bool` | Uncertainty | Use hazard uncertainty. <br>Default is *False*.
`seed` <sup>*</sup> | `int` | Seed | Initial value to seed the random number generator.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computation. <br>Default is *1*.
`liquefaction_geology_dataset_id` | `str` | Liquefaction id | Liquefaction geology/susceptibility dataset id. <br>If not provided, liquefaction will be ignored.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`buildings` <sup>*</sup> | [`ergo:buildingInventoryVer4`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingInventoryVer4)<br>[`ergo:buildingInventoryVer5`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingInventoryVer5)<br>[`ergo:buildingInventoryVer6`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingInventoryVer6)<br>[`ergo:buildingInventoryVer7`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingInventoryVer7) | Building dataset |  A building dataset.
`dfr3_mapping_set` <sup>*</sup> | [`incore:dfr3MappingSet`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:dfr3MappingSet) | DFR3 Mapping Set | DFR3 Mapping Set.
`retrofit_strategy` | [`incore:retrofitStrategy`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:retrofitStrategy) | Retrofit Strategy | Building retrofit strategy that contains guid and retrofit method.

**Input Hazards**

key name | type                                                             | name          | description
--- |------------------------------------------------------------------|---------------| ---
`hazard` | `earthquake`<br>`tornado`<br>`hurricane`<br>`flood`<br>`tsunami` | Hazard | Supported hazard object for using local and remote hazards.


**Output datasets**

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`ds_result` <sup>*</sup> | [`ergo:buildingDamageVer5`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingDamageVer5) | `buildings` | Results | A dataset containing results <br>(format: CSV).
`damage_result` <sup>*</sup> | [`incore:buildingDamageSupplement`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:buildingDamageSupplement) | `buildings` | Results | Information about applied hazard value and fragility<br>(format: JSON).

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create building structural damage
    bldg_dmg = BuildingStructuralDamage(client)

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

    # Run building structural damage analysis
    bldg_dmg.run_analysis()
```

full analysis: [building_structural_dmg.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/building_structural_dmg.ipynb)
