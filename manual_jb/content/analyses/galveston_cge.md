# Galveston Computable General Equilibrium (CGE)

**Description**

A computable general equilibrium (CGE) model is based on fundamental economic principles. A CGE model uses multiple 
data sources to reflect the interactions of households, firms, and relevant government entities as they contribute 
to economic activity. The model is based on (1) utility-maximizing households that supply labor and capital, 
using the proceeds to pay for goods and services (both locally produced and imported) and taxes; (2) the production 
sector, with perfectly competitive, profit-maximizing firms using intermediate inputs, capital, land, and labor 
to produce goods and services for both domestic consumption and export; (3) the government sector that collects 
taxes and uses tax revenues in order to finance the provision of public services; and (4) the rest of the world. 

The output of this analysis are CSV files with domestic supply, gross income, ore- and post-disaster factor demand 
and household count.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`model_iterations` <sup>*</sup> | `int` | Iterations | Number of dynamic model iterations.
`solver_path` | `str` | Solver path | Path to **ipopt** package.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`SAM` <sup>*</sup> | `incore:CGEsam` | Social matrix | A social accounting matrix.
`BB` <sup>*</sup> | `incore:CGEbb` | Capital composition | A matrix of functioning capital.
`IOUT` | `incore:CGEiout` | Government parameters | A matrix tax revenue transfer.
`MISC` | `incore:CGEmisc` | Parameters | Data of employment, capital and households <br>in the economy.
`MISCH` <sup>*</sup> | `incore:CGEmisch` | Supply elasticity | Elasticities for the supply of labor.
`EMPLOY` <sup>*</sup> | `incore:CGEemploy` | Employment | Commercial sector employment data
`JOBCR` <sup>*</sup> | `incore:CGEjobcr` | Labor | A matrix of workers groups in the economy.
`OUTCR` <sup>*</sup> | `incore:CGEoutcr` | Commuter laborers | A matrix of Galveston commuting workers.
`sector_shocks` <sup>*</sup> | `incore:capitalShocks` | Capital shocks | Building states to capital <br>shocks per sector.

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`domestic-supply` <sup>*</sup> | `incore:Employment` | Supply results | A dataset containing domestic supply results (format: CSV).
`gross-income` <sup>*</sup> | `incore:Employment` | Gross income | A dataset of resulting gross income (format: CSV).
`pre-disaster-factor-demand` <sup>*</sup> | `incore:FactorDemand` | Factor demand | A dataset of factor demand before disaster (format: CSV).
`post-disaster-factor-demand` <sup>*</sup> | `incore:FactorDemand` | Factor demand | A dataset of factor demand after disaster (format: CSV).
`household-count` <sup>*</sup> | `incore:HouseholdCount` | Household count | A dataset of household count (format: CSV).

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create Galveston CGE Model
    galveston_cge = SaltLakeCGEModel(client)
    
    # Set analysis input datasets
    galveston_cge.set_parameter("model_iterations", 1)
    galveston_cge.load_remote_input_dataset("SAM", SAM)
    galveston_cge.load_remote_input_dataset("BB", BB)
    galveston_cge.load_remote_input_dataset("MISCH", MISCH)
    galveston_cge.load_remote_input_dataset("EMPLOY", EMPLOY)
    galveston_cge.load_remote_input_dataset("JOBCR", JOBCR)
    galveston_cge.load_remote_input_dataset("OUTCR", OUTCR)
    galveston_cge.load_remote_input_dataset("sector_shocks", sector_shocks)

    # Set analysis parameters
    galveston_cge.set_parameter("solver_path", "ipopt")
    galveston_cge.set_parameter("model_iterations", 1)

    # Run Galveston CGE model analysis
    galveston_cge.run_analysis()
```

full analysis: [galveston_cge.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/galveston_cge.ipynb)
