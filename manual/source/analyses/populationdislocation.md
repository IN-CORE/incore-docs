### Population dislocation

This analysis computes population dislocation based on a particular hazard. First, housing units, with detailed characteristics 
(tenure, household size, occupied, or vacant) are allocated to the address points (buildings). This is done by calling the Housing unit allocation analysis.
After the housing units are allocated, the hazard event defined by calling Fragility and Hazard services would determine 
the value loss for each structure which would be the input for the dislocation calculation. The dislocation is calculated 
from four probabilities of dislocation based on a random beta distribution of the four damage factors presented by Bai et al. 2009. 
These four damage factors correspond to value loss. The sum of the four probabilities multiplied by the four probabilities 
of damage states is used as the probability for dislocation. Since the process to determine which households are dislocated 
is probabilistic an integer value being imported to seed the random number generator determines if a household dislocates.

Additionally, the Block Group characteristics, percentages of African-American and Hispanic population are taken into account. 

The output is a CSV file with dislocated households and related variables.

**Related publications**

* Probabilistic Assessment of Structural Damage due to Earthquakes for Buildings in Mid-America, J. Bai; M.B.D. Hueste and P. Gardoni, *Journal of Structural Engineering* **135(10)** 2009, doi: [10.1061/(ASCE)0733-9445(2009)135%3A10(1155)](https://ascelibrary.org/doi/10.1061/%28ASCE%290733-9445%282009%29135%3A10%281155%29)
* Integration of Physical Infrastructure and Social Systems in Communities Reliability and Resilience Analysis, R. Guidotti, P. Gardoni and N. Rosenheim, *Reliability Engineering & System Safety*, 2019: DOI [10.1016/j.ress.2019.01.008](https://app.dimensions.ai/details/publication/pub.1111322263?and_facet_journal=jour.1158471)

**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` | `str` | Result name |  Name of the result dataset.
`seed` <sup>*</sup> | `int` | Seed | Initial value to seed the random number generator.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`building_dmg` <sup>*</sup> | `ergo:buildingDamageVer4` | Building damage | A building damage dataset.
`housing_unit_allocation` <sup>*</sup> | `incore:housingUnitAllocation` | Housing allocation | A housing unit allocation dataset.
`block_group_data` <sup>*</sup> | `incore:blockGroupData` | Block group data | A racial distribution dataset.
`value_loss_param` <sup>*</sup> | `incore:valueLossParam` | Loss parameters | A table with value loss beta distribution parameters.
                    
**Output Datasets** 

key name | type | name | description
--- | --- | --- | ---
`result` | `incore:popDislocation` | Results | A dataset containing results (format: CSV).

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create population dislocatin
    pop_dis = PopulationDislocation(client)

    # Load input dataset
    pop_dis.load_remote_input_dataset("building_dmg", building_dmg)
    pop_dis.load_remote_input_dataset("housing_unit_allocation", housing_unit_alloc)
    pop_dis.load_remote_input_dataset("block_group_data", bg_data)
    pop_dis.load_remote_input_dataset("value_loss_param", value_loss)

    # Specify the result name
    result_name = "IN-CORE_1bv6_population_dislocation"

    seed = 1111

    # Set analysis parameters
    pop_dis.set_parameter("result_name", result_name)
    pop_dis.set_parameter("seed", seed)

    # Run Population dislocation analysis
    pop_dis.run_analysis()
```

Jupyter notebook: [populationdislocation.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/populationdislocation.ipynb)