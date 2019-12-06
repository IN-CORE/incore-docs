### Housing unit allocation

This analysis sets up a detailed critical infrastructure inventory with housing unit level characteristics.
The process aligns the housing unit inventory with physical systems, such as the inventory of buildings
and the demand nodes of a potable water network. The allocation of housing units to the address points
(buildings) provides a framework to account for uncertainty in community structure that allows
for the hazard impacts to be analyzed statistically.

Additionally, the code can be used as a MCS analysis with n runs  or as a single allocation run with an integer
value being used as a random number generator seed and passed to the other analyses. Output is a tabulated
Housing Unit Allocation dataset.

**Related publications**

* Integration of Detailed Household Characteristic Data with Critical Infrastructure and Its Implementation to Post-Hazard Resilience Modeling, N. Rosenheim, R. Guidotti and P. Gardoni, [pdf](https://www.researchgate.net/profile/Jose_Rodriguez-Llanes/publication/328233484_Food_security_resilience_to_shocks_in_Niger_preliminary_findings_on_potential_measurement_and_challenges_from_LSMS-ISA_data/links/5bc07b2fa6fdcc2c91f72ca2/Food-security-resilience-to-shocks-in-Niger-preliminary-findings-on-potential-measurement-and-challenges-from-LSMS-ISA-data.pdf#page=166)
* Integration of Physical Infrastructure and Social Systems in Communities Reliability and Resilience Analysis, R. Guidotti, P. Gardoni and N. Rosenheim, *Reliability Engineering & System Safety*, 2019, doi: [10.1016/j.ress.2019.01.008](https://app.dimensions.ai/details/publication/pub.1111322263?and_facet_journal=jour.1158471)

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset, usually in CSV format which contains <br>the allocation information.
`seed` <sup>*</sup> | `int` | Seed | Initial seed for the probabilistic model. <br>An integer value imported to seed the random <br>number generator.
`iterations` <sup>*</sup> | `int` | Iterations | Number of iterations of running <br>the probabilistic model.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`housing_unit_inventory` <sup>*</sup> | `incore:housingUnitInventory` | Housing unit inventory id | A housing unit inventory dataset, <br>aka Census block data. Corresponds to a possible <br>occupied housing unit, vacant housing unit, <br>or a group quarters.
`address_point_inventory` <sup>*</sup> | `incore:addressPoints` | Address inventory id | An address locations dataset. Corresponds <br>to a specific address where a housing unit or group quarters <br>could be assigned.
`building_inventory` <sup>*</sup> | `ergo:buildingInventory` | Building inventory id | A building Inventory csv dataset for each <br>building/structure. A structure can have multiple <br>addresses.

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`result` <sup>*</sup> | `incore:housingUnitAllocation` | Results | A csv file with the merged dataset of the inputs,<br>aka Probabilistic Housing Unit Allocation.

<small>(* required)</small>

**Execution**

code snipet:

```
    # Create bridge damage instance
    hua = HousingUnitAllocation(client)

    # Load input datasets
    hua.load_remote_input_dataset("housing_unit_inventory", housing_unit_inv)
    hua.load_remote_input_dataset("address_point_inv", address_point_inv)
    hua.load_remote_input_dataset("building_inventory", building_inv)

    # Specify the result name
    result_name = "housing_unit_allocation"

    # Set analysis parameters
    hua.set_parameter("result_name", result_name)
    hua.set_parameter("seed", seed)
    hua.set_parameter("iterations", iterations)

    # Run bridge damage analysis
    hua.run_analysis()
```

full analysis: [housingunitallocation.ipynb](https://incore2.ncsa.illinois.edu/doc/examples/housingunitallocation.ipynb)