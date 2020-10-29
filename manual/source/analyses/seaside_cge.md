### Seaside Computable General Equilibrium (CGE)

A computable general equilibrium (CGE) model is based on fundamental economic principles. A CGE model uses multiple 
data sources to reflect the interactions of households, firms, and relevant government entities as they contribute 
to economic activity. The model is based on (1) utility-maximizing households that supply labor and capital, 
using the proceeds to pay for goods and services (both locally produced and imported) and taxes; (2) the production 
sector, with perfectly competitive, profit-maximizing firms using intermediate inputs, capital, land, and labor 
to produce goods and services for both domestic consumption and export; (3) the government sector that collects 
taxes and uses tax revenues in order to finance the provision of public services; and (4) the rest of the world. 
The output of this analysis are CSV files with cge simulations, domestic supply and employment.

**Related publications**

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`print_solver_output` | `bool` | Solver output | Print solver output.
`solver_path` | `str` | Solver path | Path to **ipopt** package.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`SAM` <sup>*</sup> | `incore:SeasideCGEsam` | Social matrix | A social accounting matrix.
`BB` <sup>*</sup> | `incore:SeasideCGEbb` | Capital composition | A matrix of functioning capital.
`HHTABLE` <sup>*</sup> | `incore:SeasideCGEhhtable` | HH Table | HH Table.
`EMPLOY` <sup>*</sup> | `incore:SeasideCGEemploy` | Employment | Commercial sector employment data.
`JOBCR` <sup>*</sup> | `incore:SeasideCGEjobcr` | Labor | A matrix of workers groups in the economy.
`SIMS` <sup>*</sup> | `incore:SeasideCGEsim` | Capitol shocks random number | Random numbers for the change of capital stocks.
`sector_shocks` <sup>*</sup> | `incore:SeasideCGEshocks` | Capital shocks | Building states to capital <br>shocks per sector.

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`Seaside_Sims` <sup>*</sup> | `incore:SeasideCGEsims` | Cge simulations | A dataset containing Seaside cge simulations (format: CSV).
`Seaside_output` <sup>*</sup> | `incore:SeasideCGEEmployDS` | Employment supply results | A dataset  of changes in employment and supply. <br>(format: CSV).

<small>(* required)</small>

**Execution**

code snipet:

```
    # Create Seaside CGE Model
    seaside_cge = SeasideCGEModel(client)

    # Set analysis input parameters (both optional)
    seaside_cge.set_parameter("print_solver_output", False)
    seaside_cge.set_parameter("solver_path", "ipopt")

    # Set analysis input datasets
    seaside_cge.load_remote_input_dataset("SAM", sam)
    seaside_cge.load_remote_input_dataset("BB", bb)
    seaside_cge.load_remote_input_dataset("EMPLOY", employ)
    seaside_cge.load_remote_input_dataset("JOBCR", jobcr)
    seaside_cge.load_remote_input_dataset("HHTABLE", hhtable)
    seaside_cge.load_remote_input_dataset("SIMS", sims)
    seaside_cge.load_remote_input_dataset("sector_shocks", sector_shocks)

    # Set analysis parameters
    seaside_cge.set_parameter("solver_path", "ipopt")
    seaside_cge.set_parameter("model_iterations", 1)

    # Run Seaside CGE model analysis
    seaside_cge.run_analysis()
```

full analysis: [seaside_cge.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/seaside_cge.ipynb)