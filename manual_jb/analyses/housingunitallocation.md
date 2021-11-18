# Housing unit allocation

**Description**

This analysis sets up a detailed critical infrastructure inventory with housing unit level characteristics.
The process aligns the housing unit inventory with physical systems, such as the inventory of buildings
and the demand nodes of a potable water network. The allocation of housing units to the address points
(buildings) provides a framework to account for uncertainty in community structure that allows
for the hazard impacts to be analyzed statistically.

The output of this analysis is a CSV file with detailed household and housing unit characteristics 
(number of persons, race, tenure, vacancy) allocated to individual house units assigned to individual buildings.

**Contributors**

- Science: Nathanael Rosenheim
- Implementation: Nathanael Rosenheim, Michal Ondrejcek, and NCSA IN-CORE Dev Team

**Related publications**

* Rosenheim, N., Guidotti, R., Gardoni, P. and Peacock, W.G. (2019). Integration of detailed household and housing unit characteristic data with critical infrastructure for post-hazard resilience modeling. *Sustainable and Resilient Infrastructure* DOI: [10.1080/23789689.2019.1681821](http://doi.org/10.1080/23789689.2019.1681821)
* Rosenheim, Nathanael (2021). Detailed Household and Housing Unit Characteristics: Alpha Release of Housing Unit Inventories. *DesignSafe-CI* DOI: [10.17603/ds2-jwf6-s535](https://doi.org/10.17603/ds2-jwf6-s535)

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`seed` <sup>*</sup> | `int` | Seed | Initial value to seed the random number generator.
`iterations` <sup>*</sup> | `int` | Iterations | Number of iterations of running the probabilistic model.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`building_inventory` <sup>*</sup> | `ergo:buildingInventoryVer4`<br>`ergo:buildingInventoryVer5`<br>`ergo:buildingInventoryVer6`<br>`ergo:buildingInventoryVer7` | Building inventory | A building inventory dataset.
`housing_unit_inventory` <sup>*</sup> | `incore:housingUnitInventory` | Housing inventory | A housing unit inventory dataset.
`address_point_inventory` <sup>*</sup> | `incore:addressPoints` | Address inventory | An address locations dataset.

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`result` <sup>*</sup> | `incore:housingUnitAllocation` | Results | A dataset containing results <br>(format: CSV).

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create housing allocation
    hua = HousingUnitAllocation(client)

    # Load input dataset
    hua.load_remote_input_dataset("housing_unit_inventory", housing_unit_inv)
    hua.load_remote_input_dataset("address_point_inventory", address_point_inv)
    hua.load_remote_input_dataset("building_inventory", building_inv)

    # Specify the result name
    result_name = "IN-CORE_1bv6_housingunitallocation"

    seed = 1238
    iterations = 1

    # Set analysis parameters
    hua.set_parameter("result_name", result_name)
    hua.set_parameter("seed", seed)
    hua.set_parameter("iterations", iterations)

    # Run Housing unit allocation analysis
    hua.run_analysis()
```

full analysis: [housingunitallocation.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/housingunitallocation.ipynb) <br />
Galveston, TX housing unit allocation: [HUA_Galveston_2020-12-04.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/HUA_Galveston_2020-12-04.ipynb) <br />
Visualization of Total Population by various categories: [pyincore-viz-analysis-example.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/pyincore-viz-analysis-example.ipynb)