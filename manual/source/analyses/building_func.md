### Building functionality

The building functionality analysis can be used to calculate building functionality probabilities considering 
two situations: buildings are in at least a damage state 2 or greater or buildings are not damaged but electric
power is not available to the building. Whether buildings can receive electrical power is assumed to depend on 
the interdependency between buildings and substations, and between buildings and poles in close proximity.

If both the nearest pole to the building and the substation where buildings belong to its service area are 
functional, buildings are considered to be able to receive electric power.

The output of this analysis is a CSV file with probabilities of functionality.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computation. <br>Default is *1*.
`num_samples` | `int` | Number of CPUs | Number of iterations of running the probabilistic model.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`building_damage_mcs_samples` <sup>*</sup> | `incore:buildingDamageMcSamples` | Building dataset |  Buildings damage dataset.
`substations_damage_mcs_samples` <sup>*</sup> | `incore:substationsDamageMcSamples` | Substation dataset |  Substations damage dataset.
`poles_damage_mcs_samples` <sup>*</sup> | `incore:polesDamageMcSamples` | Pole dataset |  Electric poles dataset.
`interdependency_dictionary` <sup>*</sup> | `incore:buildingInterdependencyDict` | Interdependency dataset |  A dataset of interdependency between buildings and substations and poles.

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`result` <sup>*</sup> | `incore:funcProbability` | Results | A dataset containing results <br>(format: CSV).

<small>(* required)</small>

**Execution**

code snipet:

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
full analysis: [building_func.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/building_func.ipynb)
