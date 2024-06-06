# Building functionality

**Description**

The building functionality analysis calculates building functionality probabilities considering 
two situations: buildings are in at least a damage state 2 or greater or buildings are not damaged but electric
power is not available to the building. Whether buildings can receive electrical power is assumed to depend on 
the interdependency between buildings and substations, and between buildings and poles in close proximity.

If both the nearest pole to the building and the substation where buildings belong to its service area are 
functional, buildings are considered to be able to receive electric power.

The outputs of this analysis are 1) a CSV file with probabilities of functionality samples 
for direct comparison with [MC limit state probability](mc_limit_state_prob) outputs and 
2) a CSV file with probabilities of functionality.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`building_damage_mcs_samples` <sup>*</sup> | [`incore:buildingDamageMcSamples`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:buildingDamageMcSamples) | Building dataset |  Buildings damage dataset.
`substations_damage_mcs_samples` <sup>*</sup> | [`incore:substationsDamageMcSamples`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:substationsDamageMcSamples) | Substation dataset |  Substations damage dataset.
`poles_damage_mcs_samples` <sup>*</sup> | [`incore:polesDamageMcSamples`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:polesDamageMcSamples) | Pole dataset |  Electric poles dataset.
`interdependency_dictionary` <sup>*</sup> | [`incore:buildingInterdependencyDict`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:buildingInterdependencyDict) | Interdependency dataset |  A dataset of interdependency between buildings and substations and poles.

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`functionality_samples` <sup>*</sup> | [`incore:funcSample`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:funcSample) | Results | A dataset containing results of functionality samples<br>(format: CSV).
`functionality_probability` <sup>*</sup> | [`incore:funcProbability`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:funcProbability) | Results | A dataset containing results of functionality probability<br>(format: CSV).

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create building functionality instance
    bldg_dmg = BuildingFunctionality(client)

    # Load input dataset
    bldg_func.load_remote_input_dataset("building_damage_mcs_samples", building_dmg_mcs_id)
    bldg_func.load_remote_input_dataset("substations_damage_mcs_samples", substation_dmg_mcs_id)
    bldg_func.load_remote_input_dataset("poles_damage_mcs_samples", poles_dmg_mcs_id)
    bldg_func.load_remote_input_dataset("interdependency_dictionary", interdependency_id)

    # Specify the result name
    result_name = "funcionality_result"

    # Set analysis parameters
    bldg_func.set_parameter("result_name", result_name)
    bldg_func.set_parameter("num_samples", 3)
    bldg_func.set_parameter("num_cpu", 10)

    # Run building functionality analysis
    bldg_func.run_analysis()
```
full analysis: [building_func.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/building_func.ipynb)
