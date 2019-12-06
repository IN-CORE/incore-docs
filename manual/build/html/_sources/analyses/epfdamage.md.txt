### Electric power facility damage

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset, usually in CSV format which contains <br>the infrastructure damage information.
`mapping_id` <sup>*</sup> | `str` | Mapping id | Default electric power facility fragility mapping on Incore-service. <br>It implicitly <br>defines the fragilities to be used in the calculation.
`hazard_type` <sup>*</sup> | `str` | Hazard type | Hazard type for calculating epf damage, e.g earthquake, <br>tornado etc.
`hazard_id` <sup>*</sup> | `str` | Hazard id | Hazard ID for calculating epf damage.  Generally, hazards <br>with PGA values are used to calculate epf damages.
`fragility_key` | `str` | Fragility key | Fragility key used in mapping dataset.
`use_liquefaction` | `bool` | Liquefaction | Use liquefaction to modify fragility curve. Default *False*.
`use_hazard_uncertainty` | `bool` | Uncertainty | Use hazard uncertainty for computing damage.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. Default *1*.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`epfs` <sup>*</sup> | `incore:epf`<br>`ergo:epf` | Epf dataset id | An Electric power facility (infrastructure) dataset, usually <br>a shape file for which the damage is calculated.

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`result` <sup>*</sup> | `incore:epfVer1` | Results | A csv file of bridge structural damage.

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

full analysis: [epfdamage.ipynb](https://incore2.ncsa.illinois.edu/doc/examples/epfdamage.ipynb)