### Population dislocation

This analysis computes the population dislocation based on a particular hazard such as earthquake. First, Housing units, with detailed characteristics (tenure, household size, occupied, or vacant) are allocated to the address points (buildings). This is done by calling the Housing Unit Allocation analysis.

After the housing units are allocated, the hazard event defined by calling fragility and hazard services would determine the value loss for each structure which would be the input for the dislocation calculation. The dislocation is calculated from four probabilities of dislocation based on a random beta distribution of the four damage factors presented by Bai et al. 2009. These four damage factors correspond to value loss. The sum of the four probabilities multiplied by the four probabilities of damage states is used as the probability for dislocation. Since the process to determine which households are dislocated is probabilistic an integer value being imported to seed the random number generator determines if a household dislocates.

Additionally, the Block Group characteristics, percentages of African-American and Hispanic population are taken into account. The output is a CSV file with dislocated households and related variables.

**Related publications**

* Probabilistic Assessment of Structural Damage due to Earthquakes for Buildings in Mid-America, J. Bai; M.B.D. Hueste and P. Gardoni, *Journal of Structural Engineering* **135(10)** 2009, doi: [10.1061/(ASCE)0733-9445(2009)135%3A10(1155)](https://ascelibrary.org/doi/10.1061/%28ASCE%290733-9445%282009%29135%3A10%281155%29)
* Integration of Physical Infrastructure and Social Systems in Communities Reliability and Resilience Analysis, R. Guidotti, P. Gardoni and N. Rosenheim, *Reliability Engineering & System Safety*, 2019: DOI [10.1016/j.ress.2019.01.008](https://app.dimensions.ai/details/publication/pub.1111322263?and_facet_journal=jour.1158471)

**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` | `str` | Result name | Name of the result dataset, usually in CSV format which contains <br>the infrastructure damage information. Default *population-dislocation-result.csv*
`seed` <sup>*</sup> | `int` | Seed | Seed to ensure replication if run as part of a probabilistic analysis.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`building_dmg` <sup>*</sup> | `ergo:buildingDamageVer4` | Building damage | Building damage results CSV file from hazard service.
`housing_unit_allocation` <sup>*</sup> | `incore:housingUnitAllocation` | Housing unit allocation | Merged dataset, as a CSV file, of the inputs such as Probabilistic House Unit Allocation.
`block_group_data` <sup>*</sup> | `incore:blockGroupData` | Block group data | Racial distribution census CSV data.

**Output Datasets** 

key name | type | name | description
--- | --- | --- | ---
`result` | `incore:popDislocation` | Results | A CSV file of population dislocation.

<small>(* required)</small>

**Execution**

code snipet:

```
    # Create instance
    pop_dis = PopulationDislocation(client)

    # Load input datasets
    pop_dis.load_remote_input_dataset("building_dmg", building_dmg)
    pop_dis.load_remote_input_dataset("housing_unit_allocation", housing_unit_allocation)
    pop_dis.load_remote_input_dataset("block_group_data", bg_data)

    # Set analysis parameters
    pop_dis.set_parameter("seed", 1111)

    pop_dis.run_analysis()
```

Jupyter notebook: [populationdislocation.ipynb](https://incore2.ncsa.illinois.edu/doc/examples/populationdislocation.ipynb)
