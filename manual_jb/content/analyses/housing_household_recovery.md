# Household-level housing sequential recovery

**Description**

This analysis computes the series of household recovery states given a population 
dislocation dataset, a transition probability matrix (TPM) and an initial state vector.

The computation operates by segregating household units into five zones as a way of 
assigning social vulnerability. Using this vulnerability in conjunction with the TPM 
and the initial state vector, a Markov chain computation simulates most probable 
states to generate a stage history of housing recovery changes for each household.

The output of the computation is the history of housing recovery changes for each household unit in CSV format.

**Contributors**

- Science: Elaina Sutley, Sara Hamideh
- Implementation: Nathanael Rosenheim, Santiago Núñez-Corrales, and NCSA IN-CORE Dev Team

**Related publications**

* Sutley, E.J. and Hamideh, S., 2020. Postdisaster housing stages: a Markov chain approach to model sequences and duration based on social vulnerability. *Risk Analysis*, **40(12)**, pp.2675-2695.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`seed` <sup>*</sup> | `int` | Seed | Initial value to seed the random number generator to ensure replication of the Markov Chain path'<br>in connection with Population Dislocation.
`t_delta` <sup>*</sup> | `float` | Time step | A size of the analysis time step.
`t_final` <sup>*</sup> | `float` | Time duration | Total duration.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`population_dislocation_block` <sup>*</sup> | `incore:popDislocation` | Population dislocation | Population dislocation result aggregated to the block group level.
`tpm` <sup>*</sup> | `incore:houseRecTransitionProbMatrix` | Probability matrix | A transition probability matrix that specifies<br>the corresponding Markov chain per social vulnerability level.
`initial_stage_probability` <sup>*</sup> | `incore:houseRecInitialStageFactors` | Mass probability | Initial mass probability function for stage 0 of the Markov Chain.

**Output datasets**

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`result` <sup>*</sup> | `incore:housingRecoveryHistory` | `housing_recovery_block` | Results | A dataset containing results (format: CSV)<br>with housing recovery sequences at the individual household level.

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create Housing recovery sequential analysis instance
    hrs = HousingRecoverySequential(client)

    # Load input dataset
    hrs.load_remote_input_dataset("population_dislocation_block", population_dislocation_block)
    hrs.load_remote_input_dataset("tpm", tpm)
    hrs.load_remote_input_dataset("initial_stage_probability", initial_stage_probability)

    # Specify the result name
    result_name = "IN-CORE_housingrecovery"

    # Set analysis parameters
    hrs.set_parameter("result_name", result_name)
    hrs.set_parameter("seed", 1238)
    hrs.set_parameter("t_delta", t_delta)
    hrs.set_parameter("t_final", t_final)

    # Run Housing recovery analysis
    hrs.run_analysis()
```

full analysis: [housing_household_recovery.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/housing_household_recovery.ipynb)