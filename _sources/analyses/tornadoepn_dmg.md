# Tornado electric power network (EPN) damage

**Description**

This analysis computes electric power network (EPN) based on a particular hazard. Currently, supported hazard is: **tornado**.

The process for computing the structural damage is similar to other parts of the built environment. 
First, fragilities are obtained based on the hazard type and attributes of the network tower and network pole. Based on the fragility, 
the hazard intensity at the location of the infrastructure is computed. Using this information, the probability of exceeding 
each limit state is computed, along with the probability of damage. 

The outputs of this analysis are CSV file with probabilities of damage and JSON file with information about hazard and fragilities. Depending on the input data the analysis this analysis also provides information on the number of damaged poles for each node, 
repair cost for each node, total repair cost for the network and total repair time for the network.

**Related publications**

* Probabilistic framework for performance assessment of electrical power networks to tornadoes, Vipin U. Unnikrishnan & John W. van de Lindt, *Sustainable and Resilient Infrastructure*, **1:3-4**, 137-152, 2016, DOI: [10.1080/23789689.2016.1254998](https://www.tandfonline.com/doi/full/10.1080/23789689.2016.1254998)
* Hindcasting Community-Level Damage to the Interdependent Buildings and Electric Power Network after the 2011 Joplin, Missouri, Tornado, Navid Attary, John W. van de Lindt, Hussam Mahmoud, and Steve Smith, *Natural Hazards Review*, **20(1)**, 2019, DOI [10.1061/(ASCE)NH.1527-6996.0000317](https://ascelibrary.org/doi/10.1061/%28ASCE%29NH.1527-6996.0000317)

**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`tornado_id` | `str` | Tornado id | ID of the tornado dataset from the Hazard service.

**Input Hazards**

key name | type | name  | description
--- |-------|--------| ---
`hazard` | `tornado` | Hazard  | Supported hazard object for using local and remote hazards.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`epn_network` <sup>*</sup> | `incore:epnNetwork` | EPN network dataset | A network dataset of the electric power network.
`seed` <sup>*</sup> | `int` | Seed | Initial value to seed the random number generator.
`tornado` <sup>*</sup>| `incore:tornadoWindfield` | Tornado dataset | A tornado winds dataset.

**Output Datasets** 

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`result` <sup>*</sup> | `incore:tornadoEPNDamageVer3` | `epn_network` | Results | A dataset containing results <br>(format: CSV).
`metadata` <sup>*</sup> | `incore:tornadoEPNDamageSupplement` | `epn_network` | Results | Information about applied hazard value and fragility<br>(format: JSON).

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create instance
    ted = TornadoEpnDamage(client)

    # Specify the result name
    result_name = "tornado_dmg_result"

    # Load datasets
    ted.load_remote_input_dataset("epn_network", epn_network_id)

    # Set analysis parameters
    ted.set_parameter("result_name", result_name)
    ted.set_parameter('tornado_id', tornado_id)
    ted.set_parameter('seed', 1001)

    ted.run_analysis()
```

full analysis: [tornadoepn_dmg.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/tornadoepn_dmg.ipynb)
