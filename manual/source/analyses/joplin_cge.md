### Joplin CGE

This analysis sets up an estimate of economic impact of Joplin tornado using Computable general equilibrium (CGE)
models. A detailed analysis shows how an economy might react to economic shocks, such as changes in policy, technology,
or natural disasters. A CGE model consists of equations describing model variables and a detailed database consistent
with the model equations.

The resulting datasets are 1) Domestic Supply, 2) employment and 3) household income.

**Related publications**

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`model_iterations` <sup>*</sup> | `int` | Iterations | Number of dynamic model iterations.
`solver_path` <sup>*</sup> | `str` | Solver path | A filesystem path to ipopt executable.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`SAM` <sup>*</sup> | `incore:joplingCGEsam` | Social accounting matrix | Social accounting matrix.
`BB` <sup>*</sup> | `incore:joplinCGEKc` | Capital comp | Capital comp.
`IOUT` <sup>*</sup> | `incore:joplingCGEiout` | Government parameters | Government parameters and initial values.
`MISC` <sup>*</sup> | `incore:joplingCGEmisc` | Parameters | Parameters and initial values.
`MISCH` <sup>*</sup> | `incore:joplingCGEmisch` | Household parameters | Household parameters and initial values.
`LANDCAP` <sup>*</sup> | `incore:joplingCGElandK` | Land capital | Land capital.
`EMPLOY` <sup>*</sup> | `incore:joplinCGEemployment` | Employment | Employment.
`IGTD` <sup>*</sup> | `incore:joplingCGEigtd` | Exogenous Transfer PMT | Exogenous Transfer PMT.
`TAUFF` <sup>*</sup> | `incore:joplingCGEtauff` | Tax rates | Tax rates.
`JOBCR` <sup>*</sup> | `incore:joplingCGEjobcr` | Labor | Labor.
`OUTCR` <sup>*</sup> | `incore:joplingCGEoutcr` | Commuter Labor Groups | Commuter Labor Groups.
`TPC` | `incore:joplingCGEtpc` | Factor taxes | Factor taxes.

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`domestic-supply` <sup>*</sup> | `joplincgeanalysis` | Supply results | A csv file of domestic supply.
`employment` <sup>*</sup> | `joplincgeanalysis` | Employment results | A csv file of employment.
`household-income` <sup>*</sup> | `joplincgeanalysis` | Income results | A csv file of household income.

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
    joplin_cge.load_remote_input_dataset("TPC", TPC)
    joplin_cge.load_remote_input_dataset("JOBCR", JOBCR)
    joplin_cge.load_remote_input_dataset("OUTCR", OUTCR)

    # Set analysis parameters
    joplin_cge.set_parameter("solver_path", "")
    joplin_cge.set_parameter("model_iterations", 1)

    # Run Joplin CGE model analysis
    joplin_cge.run_analysis()
```

full analysis: [joplin_cge.ipynb](https://incore2.ncsa.illinois.edu/doc/examples/joplin_cge.ipynb)