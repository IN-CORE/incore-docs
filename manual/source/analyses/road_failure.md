### Road failure

This analysis computes road damage and failure caused by **hurricane** inundation.
This analysis computes road damage and failure based on a particular hazard. Currently supported hazard is: **hurricane**.

The process for computing the road damage is similar to other parts of the built environment. First, a fragility
is obtained based on the hazard type and attributes of the roads. Based on the fragility and road distance to shore, the hazard intensity is computed. 
Using this information, the failure probability is computed. 

The outputs of this analysis are CSV file with probabilities of damage and JSON file with information about hazard and fragilities.

**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`hazard_type` <sup>*</sup> | `str` | Hazard type | Hazard type, hurricane.
`hazard_id` <sup>*</sup> | `str` | Hazard id | ID of the hazard from the Hazard service
`fragility_key` | `str` | Fragility key | Fragility key used in mapping dataset.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. <br>Default *1*.

**Input Datasets** 

key name | type | name | description
--- | --- | --- | ---
`roads` <sup>*</sup> | `ergo:roadLinkTopo`, <br>`incore:roads` | Road  dataset | A road dataset.
`distance_table` <sup>*</sup> | `incore:distanceToShore` | Distance table | A distance to shore table.
`dfr3_mapping_set` <sup>*</sup> | `incore:dfr3MappingSet` | DFR3 Mapping Set | DFR3 Mapping Set.

**Output Datasets**

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`result` <sup>*</sup> | `incore:roadFailureVer2` | `roads` | Results | A dataset containing results <br>(format: CSV).
`damage_result` <sup>*</sup> | `incore:roadFailureSupplement` | `roads` | Results | Information about applied hazard value and fragility<br>(format: JSON).
                  
<small>(* required)</small>

**Execution**

code snippet:

```
    # Create road failure
    roadfailure = RoadFailure(client)

    # Load road inventory
    roadfailure.load_remote_input_dataset("roads", road_dataset_id)
    roadfailure.load_remote_input_dataset("distance_table", distance_dataset_id)

    # Load fragility mapping
    fragility_service = FragilityService(client)
    mapping_set = MappingSet(fragility_service.get_mapping(mapping_id))
    roadfailure.set_input_dataset('dfr3_mapping_set', mapping_set)

    # Set result name
    roadfailure.set_parameter("result_name", "road_result")

    # Set a hazard: Hurricane
    roadfailure.set_parameter("hazard_type", "hurricane")
    roadfailure.set_parameter("hazard_id", hazard_id)
    # Set number of CPU for computation
    roadfailure.set_parameter("num_cpu", 4)

    # Run eoad damage analysis
    result = roadfailure.run_analysis()
```
    
full analysis: [road_failure.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/road_failure.ipynb)