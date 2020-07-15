### Nonstructural building damage

This analysis computes the non-structural damage to buildings based on **earthquake** hazard by calling fragility and
hazard services.

The process is similar to evaluating other structural damages. The probabilities for building damage
state are obtained using fragility curves and a hazard definition, each building site will have
a specific PGA (Peak Ground Acceleration), a measurement of an earthquake hazard for each scenario.
Liquefaction effect, which is defined as a change in stress condition, in which material that is ordinarily
a solid behaves like a liquid can be considered as well. The LMF (Liquefaction Modification Factor)
values are implemented as multiplication factors to the median fragility values and they must be present
in the dataset.

The code covers Normal and LogNormal fragilities with 4 limit states (slight, moderate, extensive
and complete) and creates an output CSV file.

**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`hazard_type` <sup>*</sup> | `str` | Hazard type | Hazard type (earthquake).
`hazard_id` <sup>*</sup> | `str` | Hazard id | ID of the hazard from the Hazard service.
`fragility_key_as` | `str` | AS fragility | Fragility key used in mapping dataset.
`fragility_key_ds` | `str` | DS fragility | Fragility key used in mapping dataset.
`use_liquefation` | `bool` | Liquefaction | Use liquefaction, if applicable to the hazard. <br>Default *False*.
`liq_geology_dataset_id` | `str` | Liquefaction id | A liquefaction susceptibility dataset.
`use_hazard_uncertainty` | `bool` | Uncertainty | Use hazard uncertainty. Default is <br>*False*.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. <br>Default *1*.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`buildings` <sup>*</sup> | `ergo:buildingInventoryVer4` | Building dataset |  A building dataset.
`dfr3_mapping_set` <sup>*</sup> | `incore:dfr3MappingSet` | DFR3 Mapping Set | DFR3 Mapping Set.

**Output Datasets**

key name | type | name | description
--- | --- | --- | ---
`result` | `ergo:nsBuildingInventoryDamage` | Results | A dataset containing results <br>(format: CSV).

**Execution**

code snipet:

```
    # Create an instance
    non_structural_building_dmg = NonStructBuildingDamage(client)

    # Load input datasets
    non_structural_building_dmg.load_remote_input_dataset("buildings", building_dataset_id)

    # Load fragility mapping
    fragility_service = FragilityService(client)
    mapping_set = MappingSet(fragility_service.get_mapping(mapping_id))
    non_structural_building_dmg.set_input_dataset('dfr3_mapping_set', mapping_set)

    # Specify the result name
    result_name = "non_structural_building_dmg_result"

    # Set analysis parameters
    non_structural_building_dmg.set_parameter("result_name", result_name)
    non_structural_building_dmg.set_parameter("hazard_type", hazard_type)
    non_structural_building_dmg.set_parameter("hazard_id", hazard_id)
    non_structural_building_dmg.set_parameter("num_cpu", 4)

    # Shelby County Liquefaction Susceptibility
    use_liquefaction = True
    liq_geology_dataset_id = "5a284f55c7d30d13bc0824ba"

    non_structural_building_dmg.set_parameter("use_liquefaction", use_liquefaction)
    non_structural_building_dmg.set_parameter("liq_geology_dataset_id", liq_geology_dataset_id)

    non_structural_building_dmg.run_analysis()
```

full analysis: [non_structural_building_dmg.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/non_structural_building_dmg.ipynb)