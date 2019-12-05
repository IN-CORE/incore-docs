### Tornado epn damage

This analysis computes the damage to electric power network (EPN) caused by tornado hazard by calling fragility
and hazard services.  The probabilities for EPN damage state are obtained using network tower and network pole
fragility curves. Depending on the input data the analysis also provide information about the number of damaged
poles for each node, repair cost for each node, total repair cost for the network and total repair time for the network.

The code creates an output CSV file.

**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset, usually in CSV format which contains <br>the infrastructure damage information.
`tornado_id` <sup>*</sup> | `str` | Tornado ID | Tornado ID for calculating EPN damage.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`epn_node` <sup>*</sup> | `incore:epnNodeVer1` | EPN node | Nodes for the electric power network.
`epn_link` <sup>*</sup> | `incore:epnLinkeVer1` | EPN link | Links for the electric power network.
`tornado` | `tornadowindfield` | Tornado dataset | Winds for the tornado.

**Output Datasets** 

key name | type | name | description
--- | --- | --- | ---
`result` <sup>*</sup> | `incore:tornadoEPNDamageVer1` | Results | A CSV file of EPN damage and repair costs.

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

full analysis: [TornadoEpnDamage.ipynb](https://incore2.ncsa.illinois.edu/doc/examples/TornadoEpnDamage.ipynb)
