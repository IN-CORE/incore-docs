### Transportation recovery

This analysis computes the damage to bridges, first calling the bridge damage analysis. It then uses nodes and
links in transportation path and average daily traffic (ADT) data of bridges to calculate a Transportation
network post-disaster recovery.

Additionally, the analysis can be used in stochastic calculations with an integer value being imported to seed the random number generator.

The code creates an output CSV file with recovery trajectory timelines and data.

**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. Default *1*.
`pm` <sup>*</sup> | `int` | Performance metrics | Transportation performance metrics: <br>0: Weighted independent pathways <br>1: Free flow travel time.
`ini_num_population` <sup>*</sup> | `int` | Initial population number | The initial population number.
`population_size` <sup>*</sup> | `int` | Population size | The population size.
`num_generation` <sup*</sup> | `int` | Number Generation | Iterations per scenario.
`mutation_rate` <sup>*</sup> | `float` | Mutation rate | Mutation rate for the NSGA-II algorithm used to determine optimal recovery rate.
`crossover_rate` <sup>*</sup> | `float` | Crossover rate | Crossover rate for the NSGA-II algorithm used to determine optimal recovery rate.

**Input Datasets** 

key name | type | name | description
--- | --- | --- | ---
`nodes` <sup>*</sup> | `ergo:roadNetwork` | Road nodes network | A road network dataset, a CSV <br>file for which recovery is calculated.
`links` <sup>*</sup> | `ergo:roadNetwork` | Road links network | A road network dataset, a CSV <br>file for which recovery is calculated.
`bridges` <sup>*</sup> | `ergo:bridges` | Bridges network | A bridges dataset, usually a shape <br>file for which recovery is calculated.
`bridge_damage_value` <sup>*</sup> | `incore:bridgeDamageValue` | Bridge damages | A dataset of damages to bridges, a CSV <br>file for which recovery can be calculated.
`unrepaired_bridge` <sup>*</sup> | `incore:unrepairedBridge` | Unrepaired bridges | A dataset of unrepaired bridges, a CSV <br>file for which recovery can be calculated.
`ADT` <sup>*</sup> | `incore:ADT` | Average daily traffic | A dataset of the average daily traffic of bridges, with the assumption that <br>attached roads have the same average daily traffic.

**Output Datasets**

key name | type | name | description
--- | --- | --- | ---
`optimal_solution_of_bridge_repair_schedule` | `incore:transportationRepairSchedule` | Optimal bridge repair schedule | A CSV that lists each bridge and its ending repair time.
`overall_transportation_recovery_trajectory` | `incore:transportationRecovery` | Recovery trajectory | A CSV that lists the ending time and travel efficiency for the whole network.

<small>(* required)</small>

**Execution**

code snipet:

```
    # Create transportation recovery instance
    transportation_recovery = TransportationRecovery(client)

    # Load input datasets
    transportation_recovery.load_remote_input_dataset("nodes", nodes)
    transportation_recovery.load_remote_input_dataset("links", links)
    transportation_recovery.load_remote_input_dataset('bridges', bridges)
    transportation_recovery.load_remote_input_dataset('bridge_damage_value', bridge_damage)
    transportation_recovery.load_remote_input_dataset('unrepaired_bridge', unrepaired)
    transportation_recovery.load_remote_input_dataset('ADT', ADT_data)

    # Set analysis parameters
    transportation_recovery.set_parameter("num_cpu", 4)
    transportation_recovery.set_parameter("pm", 1)
    transportation_recovery.set_parameter('ini_num_population', 5)
    transportation_recovery.set_parameter("population_size", 3)
    transportation_recovery.set_parameter("num_generation", 2)
    transportation_recovery.set_parameter("mutation_rate", 0.1)
    transportation_recovery.set_parameter("crossover_rate", 1.0)

    # Run transportation recovery analysis
    transportation_recovery.run_analysis()
```

full analysis: [transportation_recovery.ipynb](https://incore2.ncsa.illinois.edu/doc/examples/transportation_recovery.ipynb)
full analysis: [complete_transportation_recovery.ipynb](https://incore2.ncsa.illinois.edu/doc/examples/complete_transportation_recovery.ipynb)
