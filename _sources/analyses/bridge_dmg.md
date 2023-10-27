# Bridge damage

**Description**

This analysis computes bridge damage based on a particular hazard. Currently supported hazards are: **earthquake**, 
**tsunami**, **tornado** and **hurricane**.

The process for computing the structural damage is similar to other parts of the built environment. First, a fragility
is obtained based on the hazard type and attributes of the bridge. Based on the fragility, the hazard intensity at the 
location of the bridge is computed. Using this information, the probability of exceeding each limit state is computed, 
along with the probability of damage. For the case of an earthquake hazard, if the bridge dataset contains soil 
information, the median value of the associated fragility can be modified to account for liquefaction in the damage. 

The outputs of this analysis are CSV file with probabilities of damage and JSON file with information about hazard and fragilities.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`hazard_type` | `str` | Hazard type | Hazard type (earthquake, tsunami, tornado, hurricaneWindfields). 
`hazard_id` | `str` | Hazard id | ID of the hazard from the Hazard service. 
`fragility_key` | `str` | Fragility key | Fragility key used in mapping dataset.
`use_liquefaction` | `bool` | Liquefaction | Use liquefaction, if applicable to the hazard. <br>Default is *False*.
`use_hazard_uncertainty` | `bool` | Uncertainty | Use hazard uncertainty.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computation. <br>Default is *1*.
`liquefaction_geology_dataset_id` | `str` | Liquefaction id | Liquefaction geology/susceptibility dataset id. <br>If not provided, liquefaction will be ignored.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`bridges` <sup>*</sup> | `ergo:bridges` | Bridge dataset | A bridge dataset.
`dfr3_mapping_set` <sup>*</sup> | `incore:dfr3MappingSet` | DFR3 Mapping Set | DFR3 Mapping Set.

**Input Hazards**

key name | type                                                             | name          | description
--- |------------------------------------------------------------------|---------------| ---
`hazard` | `earthquake`<br>`tornado`<br>`hurricane`<br>`flood`<br>`tsunami` | Hazard | Supported hazard object for using local and remote hazards.

**Output datasets**

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`result` <sup>*</sup> | `ergo:bridgeDamageVer2` | `bridges` | Results | A dataset containing results <br>(format: CSV).
`damage_result` <sup>*</sup> | `incore:bridgeDamageSupplement` | `bridges` | Results | Information about applied hazard value and fragility<br>(format: JSON).

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create bridge damage
    bridge_dmg = BridgeDamage(client)

    # Load input dataset
    bridge_dmg.load_remote_input_dataset("bridges", bridge_dataset_id)

    # Load fragility mapping
    fragility_service = FragilityService(client)
    mapping_set = MappingSet(fragility_service.get_mapping(mapping_id))
    bridge_dmg.set_input_dataset('dfr3_mapping_set', mapping_set)

    # Specify the result name
    result_name = "bridge_result"

    # Set analysis parameters
    bridge_dmg.set_parameter("result_name", result_name)
    bridge_dmg.set_parameter("hazard_type", hazard_type)
    bridge_dmg.set_parameter("hazard_id", hazard_id)
    bridge_dmg.set_parameter("num_cpu", 4)

    # Run bridge damage analysis
    bridge_dmg.run_analysis()
```

full analysis: [bridge_dmg.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/bridge_dmg.ipynb)
