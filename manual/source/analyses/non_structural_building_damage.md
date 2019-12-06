### Nonstructural building damage

This analysis computes the non-structural damage to buildings based on earthquake hazard by calling fragility and
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
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset, usually in CSV format which contains <br>the infrastructure damage information.
`mapping_id` <sup>*</sup> | `str` | Mapping ID | Fragility mapping on Incore-service. It implicitly <br>defines the fragilities to be used in the calculation.
`hazard_type` <sup>*</sup> | `str` | Hazard type | Hazard type for calculating bridge damage (earthquake, tornado, tsunami, etc.).
`hazard_id` <sup>*</sup> | `str` | Hazard ID | Hazard ID for calculating damage.
`fragility_key_as` | `str` | AS Fragility | AS fragility key to use in mapping dataset.
`fragility_key_ds` | `str` | DS Fragility | DS Fragility key to use in mapping dataset.
`use_liquefation` | `bool` | Liquefaction | Use liquefaction to modify fragility curve. Default *False*.
`liq_geology_dataset_id` | `str` | Liquefaction dataset ID | Liquefaction geology/susceptibility dataset ID. <br>If not provided, liquefaction will be ignored.
`use_hazard_uncertainty` | `bool` | Uncertainty | Use hazard uncertainty for computing damage. Default *False*.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. Default *1*.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`buildings` <sup>*</sup> | `ergo:buildingInventoryVer4` | Building inventory | Building dataset, usually a shape file for which the damage is calculated.

**Output Datasets**

key name | type | name | description
--- | --- | --- | ---
`result` | `ergo:nsBuildingInventoryDamage` | Results | A CSV file of building non-structural damage.

**Execution**

code snipet:

```
    # Create an instance
    non_structural_building_dmg = NonStructBuildingDamage(client)

    # Load input datasets
    non_structural_building_dmg.load_remote_input_dataset("buildings", building_dataset_id)

    # Set analysis parameters
    non_structural_building_dmg.set_parameter("result_name", "non_structural_building_dmg_result")
    non_structural_building_dmg.set_parameter("mapping_id", mapping_id)
    non_structural_building_dmg.set_parameter("hazard_type", "earthquake")
    non_structural_building_dmg.set_parameter("hazard_id", hazard_id)
    
    non_structural_building_dmg.run_analysis()
```

full analysis: [non_structural_building_damage.ipynb](https://incore2.ncsa.illinois.edu/doc/examples/non_structural_building_damage.ipynb)
