### Business closure model

**Description**

The analysis predicts operation closure days of a business based on a number of predictors, including damage state of the building, 
content, and machinery of the business, as well as disruptions in the utilities. This model is developed using a stepwise modeling 
approach based on Bayesian linear regression which was proposed by Aghababaei et al. (2020)

The model uses the empirical data collected from businesses in Lumberton, NC, after 2016 Hurricane Matthew.

The output of the model are values for the predicted closure operation days of the businesses  in CSV format.

**Contributors**

- Science: Mohammad Aghababaei, Maria Koliou
- Implementation: Mohammad Aghababaei, Michal Ondrejcek, and NCSA IN-CORE Dev Team

**Related publications**

* Aghababaei, M., Koliou, M., Watson, M. and Xiao, Y., 2021. Quantifying post-disaster business recovery through Bayesian methods. *Structure and Infrastructure Engineering*, **17(6)**, pp.838-856.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`seed` | `int` | Seed | Initial value to seed the random number generator.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`predictors` <sup>*</sup> | `incore:businessPredictorsVer1` | Damage and Loss Predictors | Damage to the buildings, content and machinery, and utilities losses

**Output datasets**

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`result` <sup>*</sup> | `incore:businessClosureOperation` |  | Results | A dataset containing results (format: CSV)<br>with values for the predicted operation closure days of the businesses.

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create Business Operation Closure analysis instance
    bco = `BusinessClosureOperation`(client)

    # Load input dataset
    bco.load_remote_input_dataset("predictors", business_predictors)

    # Specify the result name
    result_name = "IN-CORE_BusinessClosureOperation"

    # Set analysis parameters
    bco.set_parameter("result_name", result_name)
    bco.set_parameter("seed", 1238)

    # Run Business Operation Closure analysis
    bco.run_analysis()
```

full analysis: [business_closure.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/business_closure.ipynb)