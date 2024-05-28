# Building Cluster recovery

**Description**

The code creates two output files *building-recovery.csv* and *cluster-recovery.csv*
   
**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` | `str` | Result name | Name of the result dataset.
`uncertainty` <sup>*</sup> | `bool` | Uncertainty | Additional randomness.
`sample_size` | `int` | Sample size | Number of buildings to be considered from buildings dataset.
`random_sample_size` <sup>*</sup> | `int` | Sample size | Number of iterations for the Monte Carlo simulation.
`no_of_weeks` <sup>*</sup> | `int` | Number weeks | Number of weeks to run the recovery model.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. Default *1*.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`building_data` <sup>*</sup> | [`incore:portfolioBuildingInventory`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:portfolioBuildingInventory) | Building dataset | A building dataset.
`occupancy_mapping` <sup>*</sup> | [`incore:portfolioOccupancyMapping`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:portfolioOccupancyMapping) | Occupancy mapping | An occupancy of buildings dataset.
`building_damage` <sup>*</sup> | [`incore:portfolioBuildingDamage`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:portfolioBuildingDamage) | Building damage | A building damage.
`dmg_ratios` <sup>*</sup> | [`incore:portfolioDamageRatios`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:portfolioDamageRatios) | Damage ratios | Mean repair by occupancy and building type.
`utility` <sup>*</sup> | [`incore:portfolioUtilityAvailability`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:portfolioUtilityAvailability) | Utility availability | Utility availability at utility service area.
`utility_partial` <sup>*</sup> | [`incore:portfolioUtilityAvailability`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:portfolioUtilityAvailability) | Utility availability | Partial utility availability at utility service area.
`coefFL` <sup>*</sup> | [`incore:portfolioCoefficients`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:portfolioCoefficients) | Initial coefficients | Correlation coefficient of initial functionality.

**Output Datasets**

key name | type                                                                                                         | name | description
--- |--------------------------------------------------------------------------------------------------------------| --- | ---
`result` <sup>*</sup> | [`incore:clusterRecovery`](https://incore.ncsa.illinois.<br/>edu/semantics/api/types/incore:clusterRecovery) | Results | A dataset containing results (format: CSV).

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create instance
    bldg_cluster_recovery = BuildingClusterRecovery(client)

    # Load input datasets
    bldg_cluster_recovery.load_remote_input_dataset("building_data", bldg_data_dataset)
    bldg_cluster_recovery.load_remote_input_dataset("occupancy_mapping", occupancy_dataset)
    bldg_cluster_recovery.load_remote_input_dataset("building_damage", bldg_damage_dataset)
    bldg_cluster_recovery.load_remote_input_dataset("dmg_ratios", mean_repair_dataset)
    bldg_cluster_recovery.load_remote_input_dataset("utility", utility_dataset)
    bldg_cluster_recovery.load_remote_input_dataset("utility_partial", utility_partial_dataset)
    bldg_cluster_recovery.load_remote_input_dataset("coefFL", coefFL_dataset)

    # Set parameters
    bldg_cluster_recovery.set_parameter("uncertainty", True)
    bldg_cluster_recovery.set_parameter("sample_size", 35)  # default none. Gets size form input dataset
    bldg_cluster_recovery.set_parameter("random_sample_size", 50)  # default 10000
    bldg_cluster_recovery.set_parameter("no_of_weeks", 100)  # default 250

    # Creates two output files building-recovery.csv and cluster-recovery.csv
    bldg_cluster_recovery.run_analysis()
```

full analysis: [building_cluster_recovery.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/building_cluster_recovery.ipynb)
