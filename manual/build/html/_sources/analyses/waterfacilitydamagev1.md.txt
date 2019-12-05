### Water facility damage

This analysis computes the damage to water facilities, tanks, pumping stations etc. based on a particular hazard
such as earthquake, tsunami, and tornado by calling fragility and hazard services.

The process is similar to evaluating other structural damages. The probabilities for water facilities damage
state are obtained using fragility curves and a hazard definition, each water facility will have
a specific PGA (Peak Ground Acceleration), a measurement of an earthquake hazard.
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
`mapping_id` <sup>*</sup> | `str` | Mapping id | Fragility mapping dataset. It defines which fragility curves are to be <br>used in each calculation.
`hazard_type` <sup>*</sup> | `str` | Hazard type | Hazard type for calculating damage (earthquake, tornado, tsunami, etc.).
`hazard_id` <sup>*</sup> | `str` | Hazard id | Hazard ID for calculating damage.
`fragility_key` | `str` | Fragility key | Fragility key used in mapping dataset.
`use_liquefaction` | `bool` | Liquefaction | Use liquefaction to modify fragility curve. Default *False*.
`use_hazard_uncertainty` | `bool` | Uncertainty | Use hazard uncertainty for computing damage. Default *False*.
`liquefaction_geology_dataset_id` | `str` | Liquefaction dataset id | Liquefaction geology/susceptibility dataset id. <br>If not provided, liquefaction will be ignored.
`liquefaction_fragility_key` | `str` | Fragility key for liquefaction | Fragility key used in liquefaction mapping dataset.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. Default *1*.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`water_facilities` <sup>*</sup> | `ergo:waterFacilityTopo` | Water facility inventory | A water facility dataset, usually a shape <br>file for which the damage is calculated.

**Output datasets** 

key name | type | name | description
--- | --- | --- | ---
`result` | `ergo:waterFacilityDamageVer4` | Results | A csv file of damage.

<small>(* required)</small>

**Execution**

code snipet:

```
    # Create water facility damage instance
    waterfac_dmg = WaterFacilityDamage(client)

    # Load input dataset
    waterfac_dmg.load_remote_input_dataset("water_facilities", water_facilities_id)

    # Set analysis parameters
    waterfac_dmg.set_parameter("result_name", "Results.csv")
    waterfac_dmg.set_parameter("mapping_id", mapping_id)
    waterfac_dmg.set_parameter("hazard_type", "earthquake")
    waterfac_dmg.set_parameter("hazard_id", hazard_id)
    waterfac_dmg.set_parameter("num_cpu", 4)

    # Run water facility damage analysis
    waterfac_dmg.run_analysis()
```

full analysis: [waterfacilitydamagev1.ipynb](https://incore2.ncsa.illinois.edu/doc/examples/waterfacilitydamagev1.ipynb)
