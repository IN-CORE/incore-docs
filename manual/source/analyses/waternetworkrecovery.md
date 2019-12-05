### Water network recovery

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset, usually in CSV format which contains <br>the infrastructure damage information.
`n_days` <sup>*</sup> | `int` | Recovery days | n days of recovery simulation.
`seed` <sup>*</sup> | `int` | Seed | Initial seed for the probabilistic model. <br>An integer value imported to seed the random <br>number generator.
`work_hour_day` | `int` | Work time | Hours a day that crew works on the water network.
`tzero` | `int` | Starting hour | Starting hour.
`prod_param` | `tuple` | Parameters | Analysis parameters.
`crew` | `list` | Crew | Crew.
`mincrew` | `list` | Min crew | Minimum crew requirement.
`intrp_day` | `int` | Start dislocation | Start (day) of additional dislocation.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`wn_inp_file` <sup>*</sup> | `incore:waterNetworkEpanetInp` | EPAnet dataset id | EPAnet input dataset.
`demand_initial` <sup>*</sup> | `incore:waterNetworkDemand` | Water demand id | Dataset with intial demand for water network.
`pipe_dmg` <sup>*</sup> | `ergo:pipelineDamage` | Pipeline damage id | Pipeline damage probability.
`pump_dmg` <sup>*</sup> | `ergo:pumpDamage` | Pump damage id | Pump damage probability.
`tank_dmg` <sup>*</sup> | `ergo:lifelineWaterTankInventoryDamage` | Tank damage id | Tank damage probability.
`demand` <sup>*</sup> | `incore:waterNetworkDemand` | Demand id | Demand after dislocation.
`pipe_zone` <sup>*</sup> | `incore:pipeZoning` | Pipe zone id | Pipezone to decide repair order.
`demand_additional` | `incore:waterNetworkDemand` | Dislocation demand id | Water network demand after additional dislocation.

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`pressure` <sup>*</sup> | `csv` | Results | A csv file of bridge structural damage.
`initial_water_network` <sup>*</sup> | `pickle` | Results | Initial water network.
`recovery_water_network` <sup>*</sup> | `pickle` | Results | Recovery water network.
`recovery_water_network_add` <sup>*</sup> | `pickle` | Results | Recovery water network additional.

<small>(* required)</small>

**Execution**

code snipet:

```
    # Create water network recovery instance
    wn_recovery = WaterNetworkRecovery(client)

    # Load input datasets
    wn_recovery.load_remote_input_dataset("wn_inp_file", wn_inp_file)
    wn_recovery.load_remote_input_dataset("demand_initial", demand_initial)
    wn_recovery.load_remote_input_dataset("pipe_dmg", pipe_dmg)
    wn_recovery.load_remote_input_dataset("pump_dmg", pump_dmg)
    wn_recovery.load_remote_input_dataset("tank_dmg", tank_dmg)
    wn_recovery.load_remote_input_dataset("demand", demand)
    wn_recovery.load_remote_input_dataset("pipe_zone", pipe_zone)

    # Specify the result name
    result_name = "3_day_recovery"

    # Set analysis parameters
    wn_recovery.set_parameter("result_name", "result_name")
    wn_recovery.set_parameter("n_days", 3)
    wn_recovery.set_parameter("seed", 2)

    # Run water network recovery analysis
    wn_recovery.run_analysis()
```

full analysis: [Water_Network_Analysis.ipynb](https://incore2.ncsa.illinois.edu/doc/examples/Water_Network_Analysis.ipynb)
full analysis: [Complete_Water_Network_Analysis.ipynb](https://incore2.ncsa.illinois.edu/doc/examples/Complete_Water_Network_Analysis.ipynb)