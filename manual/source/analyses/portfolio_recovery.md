### Portfolio recovery
   
The code creates two output files *building-recovery.csv* and *portfolio-recovery.csv*
   
**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` | `str` | Result name | Name of the result dataset, usually in CSV format which contains <br>the infrastructure damage information.
`uncertainty` <sup>*</sup> | `bool` | Uncertainty | True if you want to use some randomness, false otherwise.
`sample_size` | `int` | Sample Size | Number of buildings to be considered from input buildings.
`random_sample_size` <sup>*</sup> | `int` | Random sample size | Number of iterations for the Monte Carlo Simulation.
`no_of_weeks` <sup>*</sup> | `int` | Number of weeks | Number of weeks to run the recovery model.
`num_cpu` | `int` | Number of CPUs | Number of CPUs used for parallel computations. Default *1*.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`building_data` <sup>*</sup> | `incore:portfolioBuildingInventory` | Building data | Building dataset.
`occupancy_mapping` <sup>*</sup> | `incore:portfolioOccupancyMapping` | Occupancy code mapping | Dataset of occupancy of buildings.
`building_damage` <sup>*</sup> | `incore:portfolioBuildingDamage` | Building damage | Results of damage done to buildings.
`dmg_ratios` <sup>*</sup> | `incore:portfolioDamageRatios` | Damage ratios | Percentage of mean repair by occupancy / building type.
`utility` <sup>*</sup> | `incore:portfolioUtilityAvailability` | Utility availability | Full utility availability at each utility service area - joint area of <br>power and water (row), at each week (column).
`utility_partial` <sup>*</sup> | `incore:portfolioUtilityAvailability` | Utility partial availability | Partial utility availability at each utility service area.
`coefFL` <sup>*</sup> | `incore:portfolioCoefficients` | Coefficients of initial functionality | Correlation coefficient of initial functionality states.

**Output Datasets**

key name | type | name | description
--- | --- | --- | ---
`result` | `incore:portfolioRecovery` | Results | A CSV file of the building portfolio recovery.

<small>(* required)</small>

**Execution**

code snipet:

```
    # Create instance
    bldg_portfolio_recovery = BuildingPortfolioRecoveryAnalysis(client)

    # Load input datasets
    bldg_portfolio_recovery.load_remote_input_dataset("building_data", bldg_data_dataset) 
    bldg_portfolio_recovery.load_remote_input_dataset("occupancy_mapping", occupancy_dataset) 
    bldg_portfolio_recovery.load_remote_input_dataset("building_damage", bldg_damage_dataset) 
    bldg_portfolio_recovery.load_remote_input_dataset("dmg_ratios", mean_repair_dataset) 
    bldg_portfolio_recovery.load_remote_input_dataset("utility", utility_dataset) 
    bldg_portfolio_recovery.load_remote_input_dataset("utility_partial", utility_partial_dataset) 
    bldg_portfolio_recovery.load_remote_input_dataset("coefFL", coefFL_dataset) 

    # Set parameters
    bldg_portfolio_recovery.set_parameter("uncertainty", True)
    bldg_portfolio_recovery.set_parameter("sample_size", 35)
    bldg_portfolio_recovery.set_parameter("random_sample_size", 50)
    bldg_portfolio_recovery.set_parameter("no_of_weeks", 100)

    bldg_portfolio_recovery.run_analysis()
```

full analysis: [portfolio_recovery.ipynb](https://incore2.ncsa.illinois.edu/doc/examples/portfolio_recovery.ipynb)
