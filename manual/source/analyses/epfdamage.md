### Electric power facility damage

This analysis computes electric power facilities damage based on a particular hazard such as earthquake, tsunami, tornado, etc.

The process for computing the structural damage is similar to other parts of the built environment. First, a fragility
is obtained based on the hazard type and attributes of the electric power facility. Based on the fragility, the hazard intensity at the 
location of the electric power facility is computed. Using this information, the probability of exceeding each limit state is computed, 
along with the probability of damage. For the case of an earthquake hazard, soil information can be used to
modify the damage probabilities to include damage due to liquefaction.  

The output of this analysis is a CSV file with probabilities of damage.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`mapping_id` <sup>*</sup> | `str` | Mapping id | ID of the mapping dataset from the DFR3 service.
`hazard_type` <sup>*</sup> | `str` | Hazard type | Hazard type (earthquake, tsunami, tornado, hurricaneWindfields). 
`hazard_id` <sup>*</sup> | `str` | Hazard id | ID of the hazard from the Hazard service.
`fragility_key` | `str` | Fragility key | Fragility key used in mapping dataset.
`use_liquefaction` | `bool` | Liquefaction | Use liquefaction, if applicable to the hazard. <br>Default is *False*.
`use_hazard_uncertainty` | `bool` | Uncertainty | Use hazard uncertainty. <br>Default is *False*.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. <br>Default *1*.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`epfs` <sup>*</sup> | `incore:epf`<br>`ergo:epf` | Electric power dataset | An electric power facility dataset.

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`result` <sup>*</sup> | `incore:epfVer1` | Results | A dataset containing results <br>(format: CSV).

<small>(* required)</small>

**Execution**

code snipet:

```
    # Create epf damage instance
    epf_dmg = EpfDamage(client)

    # Load input datasets
    epf_dmg.load_remote_input_dataset("epfs", epf_dataset_id)

    # Specify the result name
    result_name = "hazus_epf_dmg_result"

    # Set analysis parameters
    epf_dmg.set_parameter("result_name", result_name)
    epf_dmg.set_parameter("mapping_id", mapping_id)
    epf_dmg.set_parameter("hazard_type", hazard_type)
    epf_dmg.set_parameter("hazard_id", hazard_id)
    epf_dmg.set_parameter("num_cpu", num_cpu)

    # Run epf damage analysis
    epf_dmg.run_analysis()
```

full analysis: [epfdamage.ipynb](../notebooks/epfdamage)