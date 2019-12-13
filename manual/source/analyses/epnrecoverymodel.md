### Electric power network recovery model to hurricane

This analysis computes the damage to and recovery of an electric power network as a result of hurricane hazard 
by calling fragility and hazard services. It also deals with network recovery.  The analysis calculates wind hazard, 
storm surge and rainfall levels within each zip code boundary. There are multiple models based upon the three hazards 
of wind speed, storm surge inundation and rainfall. The user has the option of making the selection 
of the fragility function.  

The output of this analysis is a CSV file with probabilities of damage.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`use_hazard_wind` | `bool` | Wind hazard | A wind hazard included in the analysis. <br>Default *False*.
`use_hazard_surge` | `bool` | Surge hazard | A surge hazard included in the analysis. <br>Default *False*.
`use_hazard_rain` | `bool` | Rain hazard | A rain hazard included in the analysis. <br>Default *False*.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. <br>Default *1*.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`boundary` <sup>*</sup> | `incore:boundaries` | Boundary dataset | A boundary dataset.
`wind` <sup>*</sup> | `incore:wind` | Wind dataset | A hurricane hazard raster dataset.
`surge` <sup>*</sup> | `incore:surge` | Surge dataset | A surge dataset
`rain` <sup>*</sup> | `incore:rain` | Rain dataset | A rain dataset.

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`result` <sup>*</sup> | `incore:EPNRecoveryVer1` | Results | A dataset containing results <br>(format: CSV).

Note: Base analysis implementing these parameters and datasets has not been finalized yet. 
See Jupyter notebook below for examples.
<small>(* required)</small>

**Execution**

code snipet:

```
    # Create Epn recovery model instance
    epn_recovery = EpnRecoveryModel(client)

    # Load input datasets
    epn_recovery.load_remote_input_dataset("boundaries", boundary_id)
    epn_recovery.load_remote_input_dataset("wind", wind_id)
    epn_recovery.load_remote_input_dataset("surge", surge_id)
    epn_recovery.load_remote_input_dataset("rain", rain_id)

    # Specify the result name
    result_name = "epn_recovery"

    # Set analysis parameters
    epn_recovery.set_parameter("result_name", result_name)
    epn_recovery.set_parameter("num_cpu", num_cpu)

    # Run bridge damage analysis
    epn_recovery.run_analysis()
```

full analysis: [EpnRecoveryModel.ipynb](https://incore2.ncsa.illinois.edu/doc/examples/EpnRecoveryModel.ipynb)
