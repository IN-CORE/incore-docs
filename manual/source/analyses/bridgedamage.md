### Bridge damage

This analysis computes bridge damage based on a particular hazard such as earthquake, tsunami, tornado, etc.

The process for computing the structural damage is similar to other parts of the built environment. First, a fragility
is obtained based on the hazard type and attributes of the bridge. Based on the fragility, the hazard intensity at the 
location of the bridge is computed. Using this information, the probability of exceeding each limit state is computed, 
along with the probability of damage. For the case of an earthquake hazard, if the bridge dataset contains soil 
information, the median value of the associated fragility can be modified to account for liquefaction in the damage. 

The output of this analysis is a CSV file with probabilities of damage.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`mapping_id` <sup>*</sup> | `str` | Mapping id | ID of the mapping dataset from the DFR3 service.
`hazard_type` <sup>*</sup> | `str` | Hazard type | Hazard type (earthquake, tsunami, tornado, hurricaneWindfields). 
`hazard_id` <sup>*</sup> | `str` | Hazard id | ID of the hazard from the Hazard service 
`fragility_key` | `str` | Fragility key | Fragility key used in mapping dataset.
`use_liquefaction` | `bool` | Liquefaction | Use liquefaction, if applicable to the hazard. <br>Default is *False*.
`use_hazard_uncertainty` | `bool` | Uncertainty | Use hazard uncertainty.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computation. <br>Default is *1*.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`bridges` <sup>*</sup> | `ergo:bridges` | Bridge dataset | A bridge dataset.

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`result` <sup>*</sup> | `ergo:bridgeDamage` | Results | A dataset containing results <br>(format: CSV).

<small>(* required)</small>

**Execution**

code snipet:

```
    # Create bridge damage instance
    bridge_dmg = BridgeDamage(client)

    # Load input datasets
    bridge_dmg.load_remote_input_dataset("bridges", bridge_dataset_id)
    bridge_dmg.load_remote_input_dataset("dmg_ratios", dmg_ratio_id)

    # Specify the result name
    result_name = "result_name"

    # Set analysis parameters
    bridge_dmg.set_parameter("result_name", result_name)
    bridge_dmg.set_parameter("mapping_id", mapping_id)
    bridge_dmg.set_parameter("hazard_type", hazard_type)
    bridge_dmg.set_parameter("hazard_id", hazard_id)
    bridge_dmg.set_parameter("num_cpu", num_cpu)

    # Run bridge damage analysis
    bridge_dmg.run_analysis()
```

full analysis: [bridgedamage.ipynb](https://github.com/IN-CORE/pyincore/blob/master/pyincore/analyses/bridgedamage/bridge_dmg.ipynb)
