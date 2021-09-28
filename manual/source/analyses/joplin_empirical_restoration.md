### Joplin empirical restoration model


**Description**

This code generates a random realization for the restoration time of a building damaged in a tornado event to be restored to a certain functionality level. Functionality levels in this model are defined according to Koliou and van de Lindt (2020) and range from Functionality Level 4 (FL4, the lowest functionality) to Functionality Level 0 (FL0, full functionality). The distributions used in this code were generated using an empirical dataset collected in a longitudinal field study after the 2011 Joplin tornado in the city of Joplin, MO. Distributions were developed using this dataset for the recovery time of a building from an initial functionality level to a higher target functionality level (e.g., from FL3 to FL0). This model can be used only for Archetypes T1 to T5, which include only residential buildings per Memari et al. (2018).

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
`seed` | `int` | Seed | Initial value to seed the random number generator.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`damage` <sup>*</sup> | ergo:buildingDamageVer4, ergo:buildingDamageVer5, ergo:nsBuildingInventoryDamage, ergo:nsBuildingInventoryDamageVer2 | Infrastructure dataset | An infrastructure dataset.
`functionality_level` <sup>*</sup> | `incore:TargetFunctionalityVer1` | Target functionality | Target functionality.

**Output datasets**

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`result` <sup>*</sup> | `incore:restorationTime` |  | Results | A dataset containing results (format: CSV) with values for the predicted restoration time of the building.

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create Business Operatio Cease analysis instance
    bco = `BusinessCeaseOperation`(client)

    # Load input dataset
    bco.load_remote_input_dataset("predictors", business_predictors)

    # Specify the result name
    result_name = "IN-CORE_BusinessCeaseOperation"

    # Set analysis parameters
    bco.set_parameter("result_name", result_name)
    bco.set_parameter("seed", 1238)

    # Run Business Operation Closure analysis
    bco.run_analysis()
```

full analysis: [joplin_empirical_restoration.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/joplin_empirical_restoration.ipynb) <br />
