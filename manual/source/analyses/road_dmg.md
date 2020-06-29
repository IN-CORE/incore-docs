### Road damage

This analysis computes road damage based on earthquake or tsunami hazard.

The process for computing the structural damage is similar to other parts of the built environment. First, a fragility
is obtained based on the hazard type and attributes of the roads. Based on the fragility, the hazard intensity is computed. 
Using this information, the probability of exceeding each limit state is computed, 
along with the probability of damage. If the road dataset contains soil information, the median value of the associated 
fragility can be modified to account for liquefaction in the damage. 

The output of this analysis is a CSV file with probabilities of damage.

**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`hazard_type` <sup>*</sup> | `str` | Hazard type | Hazard type, earthquake or tsunami.
`hazard_id` <sup>*</sup> | `str` | Hazard id | ID of the hazard from the Hazard service
`fragility_key` | `str` | Fragility key | Fragility key used in mapping dataset.
`liquefaction_geology_dataset_id` | `str` | Geology id | A geology dataset for liquefaction adjustment.
`use_hazard_uncertainty` | `bool` | Hazard uncertainty | Use hazard uncertainty.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. <br>Default *1*.

**Input Datasets** 

key name | type | name | description
--- | --- | --- | ---
`roads` <sup>*</sup> | `ergo:roadLinkTopo`, <br>`incore:roads` | Road  dataset | A road dataset.
`dfr3_mapping_set` <sup>*</sup> | `incore:dfr3MappingSet` | DFR3 Mapping Set | DFR3 Mapping Set.

**Output Datasets**

key name | type | name | description
--- | --- | --- | ---
`result` | `ergo:roadDamage` | Results | A dataset containing results (format: CSV).

<small>(* required)</small>

**Execution**

code snipet:

```
    # Create Road damage analysis
    road_dmg = RoadDamage(client)

    # Load road inventory for Seaside, OR
    road_dmg.load_remote_input_dataset("roads", road_dataset_id)

    # Load fragility mapping
    fragility_service = FragilityService(client)
    mapping_set = MappingSet(fragility_service.get_mapping(mapping_id))
    road_dmg.set_input_dataset('dfr3_mapping_set', mapping_set)

    # Set result name
    road_dmg.set_parameter("result_name", "seaside_earthquake_road_result")

    # Set a hazard: Seaside Earthquake
    road_dmg.set_parameter("hazard_type", "earthquake")
    road_dmg.set_parameter("hazard_id", hazard_id)
    if fragility_key is not None:
         road_dmg.set_parameter("fragility_key", fragility_key)
    road_dmg.set_parameter("use_liquefaction", liquefaction)

    road_dmg.set_parameter("use_hazard_uncertainty", uncertainty)

    # Set number of CPU for computation
    road_dmg.set_parameter("num_cpu", 4)

    # Run eoad damage analysis
    result = road_dmg.run_analysis()
```
    
full analysis: [road_dmg.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/road_dmg.ipynb)