# Traffic flow recovery

**Description**

This analysis computes the damage to bridges, first calling the bridge damage analysis. It then uses nodes and links 
in traffic flow path and Average Daily Traffic (ADT) data of bridges to calculate a traffic flow network post-disaster recovery.
Additionally, the analysis can be used in stochastic calculations with an integer value being imported 
to seed the random number generator.

The output of this analysis is a CSV file with recovery trajectory timelines and data.

**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`pm` <sup>*</sup> | `int` | Performance metrics | Name of the result dataset.
`ini_num_population` <sup>*</sup> | `int` | Population number | An initial population number.
`population_size` <sup>*</sup> | `int` | Population size | A population size.
`num_generation` <sup>*</sup> | `int` | Number generation | Number of iterations per scenario.
`mutation_rate` <sup>*</sup> | `float` | Mutation rate | Mutation rate for the NSGA-II algorithm used for recovery rate.
`crossover_rate` <sup>*</sup> | `float` | Crossover rate | Crossover rate for the NSGA-II algorithm used for recovery rate.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. <br>Default *1*.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`bridges` <sup>*</sup> | [`ergo:bridges`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:bridges) | Bridge dataset | A bridge dataset.
`nodes` <sup>*</sup> | [`ergo:roadNetwork`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:roadNetwork) | Rad nodes | A road network dataset.
`links` <sup>*</sup> | [`ergo:roadNetwork`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:roadNetwork) | Road links | A road network dataset.
`bridge_damage_value` <sup>*</sup> | [`incore:bridgeDamageValue`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:bridgeDamageValue) | Bridge damages | A bridge dataset.
`unrepaired_bridge` <sup>*</sup> | [`incore:unrepairedBridge`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:unrepairedBridge) | Unrepaired bridges | An unrepaired bridge dataset.
`ADT` <sup>*</sup> | [`incore:ADT`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:ADT) | Bridge traffic | A dataset of daily traffic.

**Output Datasets**

key name | type                                                                                                                              | name | description
--- |-----------------------------------------------------------------------------------------------------------------------------------| --- | ---
`optimal_solution_of_bridge_repair_schedule` <sup>*</sup> | [`incore:transportationRepairSchedule`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:transportationRepairSchedule) | Repair schedule | A dataset containing results (format: CSV).
`overall_traffic_flow_recovery_trajectory` <sup>*</sup> | [`incore:trafficFlowRecovery`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:trafficFlowRecovery)                   | Recovery trajectory | A dataset containing results (format: CSV).

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create traffic flow recovery instance
    traffic_flow_recovery = TrafficFlowRecovery(client)

    # Load input datasets
    traffic_flow_recovery.load_remote_input_dataset("nodes", nodes)
    traffic_flow_recovery.load_remote_input_dataset("links", links)
    traffic_flow_recovery.load_remote_input_dataset('bridges', bridges)
    traffic_flow_recovery.load_remote_input_dataset('bridge_damage_value', bridge_damage)
    traffic_flow_recovery.load_remote_input_dataset('unrepaired_bridge', unrepaired)
    traffic_flow_recovery.load_remote_input_dataset('ADT', ADT_data)

    # Set analysis parameters
    traffic_flow_recovery.set_parameter("num_cpu", 4)
    traffic_flow_recovery.set_parameter("pm", 1)
    traffic_flow_recovery.set_parameter('ini_num_population', 5)
    traffic_flow_recovery.set_parameter("population_size", 3)
    traffic_flow_recovery.set_parameter("num_generation", 2)
    traffic_flow_recovery.set_parameter("mutation_rate", 0.1)
    traffic_flow_recovery.set_parameter("crossover_rate", 1.0)

    # Run traffic flow recovery analysis
    traffic_flow_recovery.run_analysis()
```

full analysis: [traffic_flow_recovery.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/traffic_flow_recovery.ipynb)