# Electric power facility damage

**Description**

This analysis computes electric power facility damage based on a particular hazard. 
Currently supported hazards are: **earthquake**, **tsunami**, **tornado** and **hurricane**.

The process for computing the structural damage is similar to other parts of the built environment. First, a fragility
is obtained based on the hazard type and attributes of the electric power facility. Based on the fragility, the hazard intensity at the 
location of the electric power facility is computed. Using this information, the probability of exceeding each limit state is computed, 
along with the probability of damage. For the case of an earthquake hazard, soil information can be used to
modify the damage probabilities to include damage due to liquefaction.  

The outputs of this analysis are CSV file with probabilities of damage and JSON file with information about hazard and fragilities.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`hazard_type` | `str` | Hazard type | Hazard type (earthquake, tsunami, tornado, hurricaneWindfields). 
`hazard_id` | `str` | Hazard id | Hazard ID which defines the particular hazard (e.g. New Madrid <br>earthquake using Atkinson Boore 1995).
`fragility_key` | `str` | Fragility key | Fragility key used in mapping dataset.
`use_liquefaction` | `bool` | Liquefaction | Use liquefaction, if applicable to the hazard. <br>Default is *False*. Use a ground liquefaction to modify damage interval.
`liquefaction_fragility_key` | `str` | Liquefaction key | Fragility key to use in liquefaction mapping dataset.
`liquefaction_geology_dataset_id` | `str` | Liquefaction id | Liquefaction geology/susceptibility dataset id. <br>If not provided, liquefaction will be ignored.
`use_hazard_uncertainty` | `bool` | Uncertainty | Use hazard uncertainty. <br>Default is *False*.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. <br>Default *1*.

**Input Hazards**

key name | type                                                             | name          | description
--- |------------------------------------------------------------------|---------------| ---
`hazard` | `earthquake`<br>`tornado`<br>`hurricane`<br>`flood`<br>`tsunami` | Hazard | Supported hazard object for using local and remote hazards.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`epfs` <sup>*</sup> | `incore:epf`<br>`ergo:epf` | Electric power dataset | An electric power facility dataset.
`dfr3_mapping_set` <sup>*</sup> | `incore:dfr3MappingSet` | DFR3 Mapping Set | DFR3 Mapping Set.

**Output datasets**

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`result` <sup>*</sup> | `incore:epfDamageVer3` |`epfs` | Results | A dataset containing results <br>(format: CSV).
`damage_result` <sup>*</sup> | `epfDamageSupplement` | `epfs` | Results | Information about applied hazard value and fragility<br>(format: JSON).

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create epf damage instance
    epf_dmg = EpfDamage(client)

    # Load input datasets
    epf_dmg.load_remote_input_dataset("epfs", epf_dataset_id)

    # Load fragility mapping
    fragility_service = FragilityService(client)
    mapping_set = MappingSet(fragility_service.get_mapping(mapping_id))
    epf_dmg.set_input_dataset('dfr3_mapping_set', mapping_set)

    # Specify the result name
    result_name = "hazus_epf_dmg_result"

    # Set analysis parameters
    epf_dmg.set_parameter("result_name", result_name)
    epf_dmg.set_parameter("hazard_type", hazard_type)
    epf_dmg.set_parameter("hazard_id", hazard_id)
    epf_dmg.set_parameter("use_liquefaction", True)
    epf_dmg.set_parameter("liquefaction_geology_dataset_id", liquefaction_dataset_id)
    epf_dmg.set_parameter("use_hazard_uncertainty", False)
    epf_dmg.set_parameter("num_cpu", num_cpu)

    # Run epf damage analysis
    epf_dmg.run_analysis()
```

full analysis: [epf_dmg.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/epf_dmg.ipynb)
