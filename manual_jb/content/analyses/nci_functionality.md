# Network cascading interdependency functionality

**Description**

This analysis computes cascading functionality based on the interdependencies between electric power facility (EPF)
networks and  water distribution (WDS) networks.

This analysis computes the output of the Leontief equation for functional dependencies between two
interdependent networks having functionality information per node. These dependencies capture cascading
dependencies on infrastructure functionality, expressed in terms of discretized times.

The output of the computation consists of a dataset with EPN cascading functionality accompanying the original 
discrete ones.


**Contributors**

- Science: Milad Roohi, John van de Lindt
- Implementation: Milad Roohi, Santiago Núñez-Corrales and NCSA IN-CORE Dev Team

**Related publications**

* Roohi M, van de Lindt JW, Rosenheim N, Hu Y, Cutler H. (2021) Implication of building inventory accuracy on 
  physical and socio-economic resilience metrics for informed decision-making in natural hazards. Structure and
  Infrastructure Engineering. 2020 Nov 20;17(4):534-54.
* Milad Roohi, Jiate Li, John van de Lindt. (2022) Seismic Functionality Analysis of Interdependent Buildings and 
  Lifeline Systems 12th National Conference on Earthquake Engineering (12NCEE), Salt Lake City, UT (June 27-July 1, 
  2022).

**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`discretized_days` <sup>*</sup> | `List[int]` | Discretized days | List of discretized days used across related analyses.

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`epf_network` <sup>*</sup> | `incore:epnNetwork` | Electric Power Facility Network | Electric Power Facility Network Dataset.
`wds_network` <sup>*</sup> | `incore:waterNetwork` | Water Distribution Facility Network | Water Distribution Facility Network Dataset.
`epf_wds_intdp_table` <sup>*</sup> | `incore:networkInterdependencyTable` | EPN-to-WDS Interdependency | EPN-to-WDS Interdependency Table.
`wds_epf_intdp_table` <sup>*</sup> | `incore:networkInterdependencyTable` | WDS-to-EPN Interdependency | WDS-to-EPN Interdependency Table.
`epf_subst_failure_results` <sup>*</sup> | `incore:failureProbability` | Substation failure probability | Substation failure probability Dataset.
`epf_inventory_rest_map` <sup>*</sup> | `incore:inventoryRestorationMap` | EPN inventory restoration map | EPN inventory restoration Map.
`epf_time_results` <sup>*</sup> | `incore:epfRestorationTime` | EP facility restoration time | EP facility  restoration time Dataset.
`wds_dmg_results` <sup>*</sup> | `ergo:waterFacilityDamageVer6` | Water facility damage | Water Facility Damage Dataset.
`wds_inventory_rest_map` <sup>*</sup> | `incore:inventoryRestorationMap` | WDS inventory restoration map | WDS inventory restoration Map.
`wds_time_results` <sup>*</sup> | `incore:waterFacilityRestorationTime` | Water facility restoration time | Water facility restoration time Dataset.

**Output datasets** 

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`epf_cascading_functionality` <sup>*</sup> | `incore:epfDiscretizedCascadingFunc` | `electric_power_facilities` | EPF network interdependency cascading functionality results | CSV file of interdependent cascading network functionality for EPF.

<small>(* required)</small>

**Execution**

code snippet:

```
    client = IncoreClient()

    nic_func = NciFunctionality(client)
    nic_func.set_parameter("result_name", "MMSA_nci_result")
    nic_func.set_parameter("discretized_days", [1, 3, 7, 30, 90])
    nic_func.load_remote_input_dataset("epf_network", epf_mmsa_network)
    nic_func.load_remote_input_dataset("wds_network", wds_mmsa_network)
    nic_func.set_input_dataset("epf_wds_intdp_table", epf_wds_interdependencies)
    nic_func.set_input_dataset("wds_epf_intdp_table", wds_epf_interdependencies.csv)
    nic_func.set_input_dataset("epf_subst_failure_results", epf_subst_failure_results)
    nic_func.set_input_dataset("epf_inventory_rest_map", epf_inventory_rest_map)
    nic_func.set_input_dataset("epf_time_results", epf_time_results)
    nic_func.set_input_dataset("wds_dmg_results", wds_dmg_results)
    nic_func.set_input_dataset("wds_inventory_rest_map", wds_inventory_rest_map)
    nic_func.set_input_dataset("wds_time_results", wds_time_results)

    # Run Analysis
    nic_func.run_analysis()
```

full analysis: [nci_functionality.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/nci_functionality.ipynb)