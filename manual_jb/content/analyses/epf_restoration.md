# Electric power facility restoration

**Description**

This analysis computes the repair time and the percentage of functionality change with time for an electric power 
facility based on input restoration curves.

The restoration curves are obtained based on the hazard type and class of the power facility, e.g. Low 
Voltage Substation, Large Power Plant, etc. Based on the restoration curve applicable, we can obtain the 
percentage of the functionality change by varying the time; we can also compute the repair time at different 
level of percentage of functionality change by inversing the restoration function.

**Input Parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.
`restoration_key` | `str` | Restoration key | Restoration key used in mapping dataset. Default to "Restoration ID Code"
`end_time` | `float` | End time | End repair time in days. Default to 365 days
`time_interval` | `float` | Time interval | Incremental interval for time in days. Default to 1
`pf_interval` | `float` | Percentage of functionality interval | Incremental interval for percentage of functionality. Default to 0.1
`discretized_days` | `List[int]`  | Discretized Days | Discretized days to compute functionality. Defaults to 1, 3, 7, 30, 90

**Input Datasets**

key name | type | name | description
--- | --- | --- | ---
`dfr3_mapping_set` <sup>*</sup> | [`incore:dfr3MappingSet`](https://tools.in-core.org/semantics/api/types/incore:dfr3MappingSet) | DFR3 Mapping Set | DFR3 Mapping Set.
`epfs` <sup>*</sup> | [`incore:epf`](https://tools.in-core.org/semantics/api/types/incore:epf) <br> [`ergo:epf`](https://tools.in-core.org/semantics/api/types/ergo:epf) | Electric Power Facilities | Electric Power Facilities.

**Output datasets** 

key name | type | name | description
--- | --- | --- | ---
`pf_results` <sup>*</sup> | [`incore:epfRestorationFunc`](https://tools.in-core.org/semantics/api/types/incore:epfRestorationFunc) | Percentage of functionality results | A csv file recording functionality change with time for each class and limit state
`time_results` <sup>*</sup> | [`incore:epfRestorationTime`](https://tools.in-core.org/semantics/api/types/incore:epfRestorationTime) | Time results | A csv file recording repair time at certain functionality recovery for each class and limit state.
`inventory_restoration_map` <sup>*</sup> | [`incore:inventoryRestorationMap`](https://tools.in-core.org/semantics/api/types/incore:inventoryRestorationMap) | Mapping of inventory and restoration | A csv file recording the mapping relationship between GUID and restoration id applicable.
`func_results` <sup>*</sup> | [`incore:epfDiscretizedRestorationFunc`](https://tools.in-core.org/semantics/api/types/incore:epfDiscretizedRestorationFunc) | Discretized restoration functionality | A csv file recording discretized functionality over time.

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create electric power facility restoration analysis
    client = IncoreClient()
    epf_rest = ElectricPowerFacilityRestoration(client)

    # Load restoration mapping
    restorationsvc = RestorationService(client)
    mapping_set = MappingSet(restorationsvc.get_mapping("61f302e6e3a03e465500b3eb"))  # new format of mapping
    epf_rest.load_remote_input_dataset('epfs', '5d92355bb9219c06ae7e386a')
    epf_rest.set_input_dataset('dfr3_mapping_set', mapping_set)
    epf_rest.set_parameter("result_name", "epf_restoration.csv")
    epf_rest.set_parameter("discretized_days", [1, 3, 7, 30, 90])
    epf_rest.set_parameter("restoration_key", "Restoration ID Code")
    epf_rest.set_parameter("end_time", 100.0)
    epf_rest.set_parameter("time_interval", 1.0)
    epf_rest.set_parameter("pf_interval", 0.01) 
    
    # run restoration analysis
    epf_rest.run_analysis()
```

full analysis: [power_facility_restoration.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/power_facility_restoration.ipynb)

