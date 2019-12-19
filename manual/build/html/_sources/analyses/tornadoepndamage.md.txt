### Tornado Electric Power Network (EPN) damage

This analysis computes electric power network (EPN) damage based on tornado hazard.  

The process for computing the structural damage is similar to other parts of the built environment. 
First, fragilities are obtained based on the hazard type and attributes of the network tower and network pole. Based on the fragility, 
the hazard intensity at the location of the infrastructure is computed. Using this information, the probability of exceeding 
each limit state is computed, along with the probability of damage. 

The output of this analysis is a CSV file. Depending on the input data the analysis this analysis also provides information on the number of damaged poles for each node, 
repair cost for each node, total repair cost for the network and total repair time for the network.

**Related publications**

* Probabilistic framework for performance assessment of electrical power networks to tornadoes, Vipin U. Unnikrishnan & John W. van de Lindt, *Sustainable and Resilient Infrastructure*, **1:3-4**, 137-152, 2016, DOI: [10.1080/23789689.2016.1254998](https://www.tandfonline.com/doi/full/10.1080/23789689.2016.1254998)
* Hindcasting Community-Level Damage to the Interdependent Buildings and Electric Power Network after the 2011 Joplin, Missouri, Tornado, Navid Attary, John W. van de Lindt, Hussam Mahmoud, and Steve Smith, *Natural Hazards Review*, **20(1)**, 2019, DOI [10.1061/(ASCE)NH.1527-6996.0000317](https://ascelibrary.org/doi/10.1061/%28ASCE%29NH.1527-6996.0000317)

**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`tornado_id` <sup>*</sup> | `str` | Tornado id | ID of the tornado dataset from the Hazard service.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`epn_node` <sup>*</sup> | `incore:epnNodeVer1` | EPN node | A dataset with nodes of the electric power network.
`epn_link` <sup>*</sup> | `incore:epnLinkeVer1` | EPN link | A dataset with links of the electric power network.
`tornado` | `tornadowindfield` | Tornado dataset | A tornado winds dataset.

**Output Datasets** 

key name | type | name | description
--- | --- | --- | ---
`result` <sup>*</sup> | `incore:tornadoEPNDamageVer1` | Results | A dataset containing results (format: CSV).

<small>(* required)</small>

**Execution**

code snipet:

```
    # Create instance
    ted = TornadoEpnDamage(client)

    # Load datasets
    ted.load_remote_input_dataset("epn_node", epn_node_id)
    ted.load_remote_input_dataset("epn_link", epn_link_id)

    # Set analysis parameters
    ted.set_parameter("result_name", "tornadoEPNresults.csv")
    ted.set_parameter("tornado_id", tornado_id)

    ted.run_analysis()
```

full analysis: [TornadoEpnDamage.ipynb](https://github.com/IN-CORE/pyincore/blob/master/pyincore/analyses/tornadoepndamage/TornadoEpnDamage.ipynb)