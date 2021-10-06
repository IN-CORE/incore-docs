### Joplin empirical restoration model

**Description**

This code generates a random realization for the restoration time of a building damaged in a tornado event to be restored 
to a certain functionality level. Functionality levels in this model are defined according to Koliou and van de Lindt (2020) 
and range from Functionality Level 4 (FL4, the lowest functionality) to Functionality Level 0 (FL0, full functionality). 
The distributions used in this code were generated using an empirical dataset collected in a longitudinal field study 
after the 2011 Joplin tornado in the city of Joplin, MO. Distributions were developed using this dataset for the recovery time 
of a building from an initial functionality level to a higher target functionality level (e.g., from FL3 to FL0). 
This model can be used only for Archetypes T1 to T5, which include only residential buildings per Memari et al. (2018).

The output of the model are values for the predicted restoration time of the building in CSV format.

**Contributors**

- Science: Mohammad Aghababaei, Maria Koliou
- Implementation: Mohammad Aghababaei, Michal Ondrejcek, and NCSA IN-CORE Dev Team

**Related publications**

* Aghababaei, M., Koliou, M., Pilkington, S., Mahmoud, H., van de Lindt, J.W., Curtis, A., Smith, S., Ajayakumar, J. and Watson, M., 2020. *Validation of time-dependent repair recovery of the building stock following the 2011 Joplin Tornado. Natural Hazards Review*, **21(4)**, p.04020038.
* Koliou, M. and van de Lindt, J.W., 2020. *Development of building restoration functions for use in community recovery planning to tornadoes*. Natural Hazards Review, **21(2)**, p.04020004.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`target_functionality_level` | `int` | Target level | Target functionality level for all infrastructure.
`seed` | `int` | Seed | Initial value to seed the random number generator.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`building_dmg` <sup>*</sup> | `ergo:buildingDamageVer4`<br>`ergo:buildingDamageVer5`<br>`ergo:nsBuildingInventoryDamage`<br>`ergo:nsBuildingInventoryDamageVer2` | Building damage | A building damage dataset.

**Output datasets**

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`result` <sup>*</sup> | `incore:restorationTime` |  | Results | A dataset containing results (format: CSV) with values for the predicted restoration time of the building.

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create Joplin empirical restoration analysis instance
    restoration = `JoplinEmpiricalRestoration`(client)

    # Load input dataset
    restoration.load_remote_input_dataset("building_dmg", building_damage)

    # Specify the result name
    result_name = "IN-CORE_Joplin_empirical_restoration"

    # Set analysis parameters
    restoration.set_parameter("result_name", result_name)
    restoration.set_parameter("target_functionality_level", 0)
    restoration.set_parameter("seed", 1234)
    
    # Run Joplin empirical restoration analysis
    restoration.run_analysis()
```

full analysis: [joplin_empirical_restoration.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/joplin_empirical_restoration.ipynb) <br />
