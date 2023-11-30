# Population dislocation

**Description**

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

**Contributors**

- Science: Walter Gillis Peacock, Nathanael Rosenheim
- Implementation: Nathanael Rosenheim, Yong Wook Kim, Gowtham Naraharisetty, Michal Ondrejcek, Chen Wang , and NCSA IN-CORE Dev Team

**Related publications**

* Lin, Y.S., Peacock, W.G., Lu, J.C., and Zhang, Y. (2008). Household dislocation algorithm 3: A logistic regression approach 08-05R. 
Retrieved from [hrrc.arch.tamu.edu/publications/research reports/08-05R Dislocation Algorithm 3.pdf](https://hrrc.arch.tamu.edu/publications/research%20reports/08-05R%20Dislocation%20Algorithm%203.pdf)
* Rosenheim, N., Guidotti, R., Gardoni, P., and Peacock, W.G. (2019). Integration of detailed household and housing unit characteristic data with critical infrastructure for post-hazard resilience modeling. *Sustainable and Resilient Infrastructure* DOI: [10.1080/23789689.2019.1681821](https://doi.org/10.1080/23789689.2019.1681821)
* Bai, J., Hueste, M.B.D. and Gardoni, P. (2009), Probabilistic Assessment of Structural Damage due to Earthquakes for Buildings in Mid-America *Journal of Structural Engineering* **135(10)** DOI: [10.1061/(ASCE)0733-9445(2009)135:10(1155)](https://doi.org/10.1061/%28ASCE%290733-9445%282009%29135%3A10%281155%29)

**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` | `str` | Result name |  Name of the result dataset.
`seed` <sup>*</sup> | `int` | Seed | Initial value to seed the random number generator.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`building_dmg` <sup>*</sup> | [`ergo:buildingDamageVer4`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingDamageVer4)<br>[`ergo:buildingDamageVer5`](https://incore.ncsa.illinois.edu/semantics/api/types/ergo:buildingDamageVer5) | Building damage | A building damage dataset.
`housing_unit_allocation` <sup>*</sup> | [`incore:housingUnitAllocation`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:housingUnitAllocation) | Housing allocation | A housing unit allocation dataset.
`block_group_data` <sup>*</sup> | [`incore:blockGroupData`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:blockGroupData) | Block group data | A block group racial distribution dataset.
`value_loss_param` <sup>*</sup> | [`incore:valueLossParam`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:valueLossParam) | Loss parameters | A table with value loss beta distribution parameters.
                    
**Output Datasets** 

key name | type | name | description
--- | --- | --- | ---
`result` <sup>*</sup> | [`incore:popDislocation`](https://incore.ncsa.illinois.edu/semantics/api/types/incore:popDislocation) | Results | A dataset containing results (format: CSV).

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

Jupyter notebook: [populationdislocation.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/populationdislocation.ipynb)