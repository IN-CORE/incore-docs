### Joplin Computable General Equilibrium (CGE)

A computable general equilibrium (CGE) model is based on fundamental economic principles. A CGE model uses multiple 
data sources to reflect the interactions of households, firms and relevant government entities as they contribute 
to economic activity. The model is based on (1) utility-maximizing households that supply labor and capital, 
using the proceeds to pay for goods and services (both locally produced and imported) and taxes; (2) the production 
sector, with perfectly competitive, profit-maximizing firms using intermediate inputs, capital, land and labor 
to produce goods and services for both domestic consumption and export; (3) the government sector that collects 
taxes and uses tax revenues in order to finance the provision of public services; and (4) the rest of the world. 

The output of this analysis are CSV files with domestic supply, gross income, ore- and post-disaster factor demand 
and household count.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`model_iterations` <sup>*</sup> | `int` | Iterations | Number of dynamic model iterations.
`solver_path` <sup>*</sup> | `str` | Solver path | Path to **ipopt** package.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`SAM` <sup>*</sup> | `incore:joplinCGEsam` | Social matrix | A social accounting matrix.
`BB` <sup>*</sup> | `incore:JoplinCGEbb` | Capital composition | A matrix of functioning capital.
`IOUT` <sup>*</sup> | `incore:JoplinCGEiout` | Government parameters | A matrix tax revenue transfer.
`MISC` <sup>*</sup> | `incore:joplinCGEmisc` | Parameters | Data of employment, capital and households <br>in the economy.
`MISCH` <sup>*</sup> | `incore:joplinCGEmisch` | Supply elasticity | Elasticities for the supply of labor.
`LANDCAP` <sup>*</sup> | `incore:JoplinCGElandcap` | Land capital | Changes in the price of physical capital.
`EMPLOY` <sup>*</sup> | `incore:JoplinCGEemploy` | Employment | Commercial sector employment data
`IGTD` <sup>*</sup> | `incore:JoplinCGEigtd` | Exogenous payment | A matrix of exogenous transfer payment.
`TAUFF` <sup>*</sup> | `incore:joplinCGEtauff` | Tax rates | Social security tax rates.
`JOBCR` <sup>*</sup> | `incore:JoplinCGEjobcr` | Labor | A matrix of workers groups in the economy.
`OUTCR` <sup>*</sup> | `incore:JoplinCGEoutcr` | Commuter laborers | A matrix of Joplin commuting workers.
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

code snipet:

```
    # Create Joplin CGE Model
    joplin_cge = JoplinCGEModel(client)

    # Set analysis input datasets
    joplin_cge.load_remote_input_dataset("SAM", SAM)
    joplin_cge.load_remote_input_dataset("BB", BB)
    joplin_cge.load_remote_input_dataset("IOUT", IOUT)
    joplin_cge.load_remote_input_dataset("MISC", MISC)
    joplin_cge.load_remote_input_dataset("MISCH", MISCH)
    joplin_cge.load_remote_input_dataset("LANDCAP", LANDCAP)
    joplin_cge.load_remote_input_dataset("EMPLOY", EMPLOY)
    joplin_cge.load_remote_input_dataset("IGTD", IGTD)
    joplin_cge.load_remote_input_dataset("TAUFF", TAUFF)
    joplin_cge.load_remote_input_dataset("JOBCR", JOBCR)
    joplin_cge.load_remote_input_dataset("OUTCR", OUTCR)
    joplin_cge.load_remote_input_dataset("sector_shocks", sector_shocks)

    # Set analysis parameters
    joplin_cge.set_parameter("solver_path", "ipopt")
    joplin_cge.set_parameter("model_iterations", 1)

    # Run Joplin CGE model analysis
    joplin_cge.run_analysis()
```

full analysis: [joplin_cge.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/joplin_cge.ipynb)