### Housing unit allocation

This analysis sets up a detailed critical infrastructure inventory with housing unit level characteristics.
The process aligns the housing unit inventory with physical systems, such as the inventory of buildings
and the demand nodes of a potable water network. The allocation of housing units to the address points
(buildings) provides a framework to account for uncertainty in community structure that allows
for the hazard impacts to be analyzed statistically.

The output of this analysis is a CSV file with allocated house units.

**Related publications**

* Integration of Detailed Household Characteristic Data with Critical Infrastructure and Its Implementation to Post-Hazard Resilience Modeling, N. Rosenheim, R. Guidotti and P. Gardoni, [pdf](https://www.researchgate.net/profile/Jose_Rodriguez-Llanes/publication/328233484_Food_security_resilience_to_shocks_in_Niger_preliminary_findings_on_potential_measurement_and_challenges_from_LSMS-ISA_data/links/5bc07b2fa6fdcc2c91f72ca2/Food-security-resilience-to-shocks-in-Niger-preliminary-findings-on-potential-measurement-and-challenges-from-LSMS-ISA-data.pdf#page=166)
* Integration of Physical Infrastructure and Social Systems in Communities Reliability and Resilience Analysis, R. Guidotti, P. Gardoni and N. Rosenheim, *Reliability Engineering & System Safety*, 2019, doi: [10.1016/j.ress.2019.01.008](https://app.dimensions.ai/details/publication/pub.1111322263?and_facet_journal=jour.1158471)

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`seed` <sup>*</sup> | `int` | Seed | Initial value to seed the random number generator.
`iterations` <sup>*</sup> | `int` | Iterations | Number of iterations of running the probabilistic model.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`housing_unit_inventory` <sup>*</sup> | `incore:housingUnitInventory` | Housing inventory | A housing unit inventory dataset.
`address_point_inventory` <sup>*</sup> | `incore:addressPoints` | Address inventory | An address locations dataset.
`building_inventory` <sup>*</sup> | `ergo:buildingInventory` | Building inventory | A building inventory dataset.

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`result` <sup>*</sup> | `incore:housingUnitAllocation` | Results | A dataset containing results <br>(format: CSV).

<small>(* required)</small>

**Execution**

code snipet:

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

full analysis: [housingunitallocation.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/housingunitallocation.ipynb)
Galveston, TX housing unit allocation: [HUA_Galveston_2020-12-04.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/HUA_Galveston_2020-12-04.ipynb)