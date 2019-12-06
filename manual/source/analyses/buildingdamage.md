### Building damage

This analysis computes the damage to buildings based on a particular hazard such as earthquake, tsunami
and tornado by calling fragility and hazard services.

The process is similar to evaluating other structural damages. The probabilities for building damage
state are obtained using fragility curves and a hazard definition, each building site will have
a specific PGA (Peak Ground Acceleration), a measurement of an earthquake hazard for each scenario.
Liquefaction effect, which is defined as a change in stress condition, in which material that is ordinarily
a solid behaves like a liquid can be considered as well. The LMF (Liquefaction Modification Factor)
values are implemented as multiplication factors to the median fragility values and they must be present
in the dataset.

The code covers Normal and LogNormal fragilities with 4 limit states (slight, moderate, extensive
and complete) and creates an output CSV file.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset, usually in CSV format which contains <br>the infrastructure damage information.
`mapping_id` <sup>*</sup> | `str` | Mapping id | Default building fragility mapping on Incore-service. It implicitly <br>defines the fragilities to be used in the calculation.
`hazard_type` <sup>*</sup> | `str` | Hazard type | Hazard type for calculating bridge damage, e.g earthquake, <br>tornado etc.
`hazard_id` <sup>*</sup> | `str` | Hazard id | Hazard ID for calculating building damage.  Generally, hazards <br>with PGA values are used to calculate building damages.
`fragility_key` | `str` | Fragility key | Fragility key used in mapping dataset.
`use_liquefaction` | `bool` | Liquefaction | Use liquefaction to modify fragility curve. Default *False*.
`use_hazard_uncertainty` | `bool` | Uncertainty | Use hazard uncertainty for computing damage.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. Default *1*.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`buildings` <sup>*</sup> | `ergo:buildingInventoryVer4`<br>`ergo:buildingInventoryVer5`<br>`ergo:buildingInventoryVer6` | Building dataset id | A building (infrastructure) dataset, usually <br>a shape file for which the damage is calculated.
`dmg_ratios` |  | Damage ratios id | A dataset that contains the damage ratios for buildings. It includes <br>weights to compute mean damage.

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`result` <sup>*</sup> | `ergo:buildingDamageVer4` | Results | A csv file of building structural damage.

<small>(* required)</small>

**Execution**

code snipet:

```
    # Create building damage instance
    bldg_dmg = BuildingDamage(client)

    # Load input datasets
    bldg_dmg.load_remote_input_dataset("buildings", bldg_dataset_id)

    # Specify the result name
    result_name = "result_name"

    # Set analysis parameters
    bldg_dmg.set_parameter("result_name", result_name)
    bldg_dmg.set_parameter("mapping_id", mapping_id)
    bldg_dmg.set_parameter("hazard_type", hazard_type)
    bldg_dmg.set_parameter("hazard_id", hazard_id)
    bldg_dmg.set_parameter("num_cpu", num_cpu)

    # Run building damage analysis
    bldg_dmg.run_analysis()
```

full analysis: [buildingdamage.ipynb](https://incore2.ncsa.illinois.edu/doc/examples/buildingdamage.ipynb)