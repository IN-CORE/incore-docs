### Electric power network recovery model

This analysis computes the damage to electric power network caused by hurricane hazard by calling fragility
and hazard services. It also deals with network recovery. The analysis is based on research of Vulnerability
and Robustness of Civil Infrastructure Systems to Hurricanes by Prof. Shuoqi Wang, Department of Civil and
Environmental Engineering, University of Washington.

The analysis calculates wind hazard, storm surge and rainfall levels within each zip code boundary. There are
multiple models based upon the three hazards of wind speed, storm surge inundation and rainfall.
The user has the option of making the selection of the fragility function.

The code creates an output CSV file.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset, usually in CSV format which contains <br>the electric power network recovery information.
`use_hazard_wind` | `bool` | Wind | Include wind hazard in analysis. Default *False*.
`use_hazard_surge` | `bool` | Surge | Include surge hazard in analysis. Default *False*.
`use_hazard_rain` | `bool` | Rain | Include rain hazard in analysis. Default *False*.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. Default *1*.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`boundary` <sup>*</sup> | `incore:boundaries` | A boundary dataset id | A parcel and zip code bounday dataset, usually <br>a shape file for which the recovery is calculated.
`wind` <sup>*</sup> | `incore:wind` | Wind dataset id | A hurricane hazard raster dataset. Maximum sustained wind speed,<br>the 1-minute wind speed at 10m above ground (in meters per second).<br>Not the 3-second gust used in ASCE7
`surge` <sup>*</sup> | `incore:surge` | Surge dataset id | A surge dataset id with inland inundation level above ground (in meters).
`rain` <sup>*</sup> | `incore:rain` | Rain dataset id | A rain dataset id with maximum daily total rainfall (in millimeters).

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`result` <sup>*</sup> | `incore:EPNRecoveryVer1` | Results | A csv file of electric power network recovery.

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
