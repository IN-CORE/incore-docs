## pyIncore Upgrade Guide

This page will help you to upgrade/refactor your python code to be compatible with the latest version of pyIncore/pyIncore-viz API changes.
 
### Previous versions to pyIncore 0.6.4 (or beyond)

From pyIncore 0.6.4 (and beyond), a local fragility mapping class and a local fragility class are introduced. In order to support this addition, how to input a fragility mapping to an analysis has changed. Instead of using the ID of the mapping, a mapping Set object is used. If you are using an analysis with a fragility mapping as an input, please upgrade your code using the example below:

- Before
    ```
    mapping_id = "5b48fb1f337d4a478e7bd54d"
    bldg_dmg.set_parameter(‘mapping_id', mapping_id)
    ```
- After (pyIncore 0.6.4)
    ```
    fragility_service = FragilityService(client)
    mapping_id = "5b48fb1f337d4a478e7bd54d"
    mapping_set = MappingSet(fragility_service.get_mapping(mapping_id))
    
    bldg_dmg.set_input_dataset('dfr3_mapping_set', mapping_set)
    ```

### pyIncore 0.9.3

1. Split analysis output into JSON and CSV for all analyses. JSON contains supplemental information (e.g. which demand type 
and unit was used). 
2. Rename limit states and damage states to LS_0, LS_1, LS2 and DS_0, DS_1, DS_2, DS_3 where applicable

- Before

  **csv file**

  guid | LS_0 | LS_1 | LS_2 | insignific | moderate | heavy | complete
  --- | --- | --- | --- | --- | --- | --- | ---
  a41e7dcc-3b82-42f2-9dbd-a2ebdf39d453 | 0.8481 | 0.3273 | 0.0272 | 0.1519 | 0.5208 | 0.3001 | 0.0272
  254d1dd8-5d2f-4737-909b-59cc64ca72d4 | 0.8443 | 0.3283 | 0.0286 | 0.1557 | 0.5160 | 0.2997 | 0.0286
  4253802e-b3e5-4ed3-93b0-dda9ef6362b0 | 0.8968 | 0.4809 | 0.0876 | 0.1032 | 0.4158 | 0.3934 | 0.0876

- After (pyIncore 0.9.3)
  
  **csv file**

  guid | LS_0 | LS_1 | LS_2 | DS_0 | DS_1 | DS_2 | DS_3 | haz_expose
  --- | --- | --- | --- | --- | --- | --- | --- | ---
  a41e7dcc-3b82-42f2-9dbd-a2ebdf39d453 | 0.8481 | 0.3273 | 0.0272 | 0.1519 | 0.5208 | 0.3001 | 0.0272 | yes
  254d1dd8-5d2f-4737-909b-59cc64ca72d4 | 0.8443 | 0.3283 | 0.0286 | 0.1557 | 0.5160 | 0.2997 | 0.0286 | yes
  4253802e-b3e5-4ed3-93b0-dda9ef6362b0 | 0.8968 | 0.4809 | 0.0876 | 0.1032 | 0.4158 | 0.3934 | 0.0876 | yes```

  **json file**

  ```
  [
     {
        "guid": "a41e7dcc-3b82-42f2-9dbd-a2ebdf39d453",
        "fragility_id": "5b47b350337d4a36290769c7",
        "demandtype": ["PGA"],
        "demandunits": ["g"],
        "hazardval": [0.3099964301]
     },
     {
        "guid": "254d1dd8-5d2f-4737-909b-59cc64ca72d4",
        "fragility_id": "5b47b350337d4a36290769cd",
        "demandtype": ["PGA"],
        "demandunits": ["g"],
        "hazardval": [0.3099964301]
     },
     {
        "guid": "4253802e-b3e5-4ed3-93b0-dda9ef6362b0",
        "fragility_id": "5b47b34e337d4a3629075420",
        "demandtype": ["PGA"],
        "demandunits": ["g"],
        "hazardval": [0.3084251268]
    },
  ```

### pyIncore 0.9.5

We ended support for legacy fragility curve formats (e.g. standard,  period standard, period building, conditional, 
custom expression, parametric). All your existing fragilities in both public and personal spaces have already been 
reformatted to the new format so no change is required on your part. However, creating new fragilities is only 
supported in the new format. Please clear browser cache.

- After (pyIncore 0.9.5)

  ```
  {
     "className": "FragilitySet",
     "legacyId": "SF_S1_212",
     "hazardType": "earthquake",
     "inventoryType": "building",
     "authors": ["Elnashai and Jeong"],
     "description": "Mid-Rise Steel Moment Frame",
     "resultType": "Limit State",
     "demandTypes": ["0.2 sec Sa"],
     "demandUnits": ["g"],
     "fragilityCurves": [
        {
           "description": "legacy - PeriodStandardFragilityCurve",
           "className": "FragilityCurveRefactored",
           "returnType": {
              "type": "Limit State",
              "unit": "",
              "description": "Moderate"
           },
           "rules": [{
              "expression": "scipy.stats.norm.cdf((math.log(point_two_sec_SA) - (-0.576))/(0.836))"
           }]
        },
        {
           "description": "legacy - PeriodStandardFragilityCurve",
           "className": "FragilityCurveRefactored",
           "returnType": {
           "type": "Limit State",
           "unit": "",
           "description": "Extensive"
           },
           "rules": [{
              "expression": "scipy.stats.norm.cdf((math.log(point_two_sec_SA) - (0.23))/(0.911))"
           }]
        },
        {
           "description": "legacy - PeriodStandardFragilityCurve",
           "className": "FragilityCurveRefactored",
           "returnType": {
              "type": "Limit State",
              "unit": "",
              "description": "Complete"
           },
           "rules": [{
              "expression": "scipy.stats.norm.cdf((math.log(point_two_sec_SA) - (1.197))/(1.05))"
           }]
        }
     ],
     "creator": "incore",
     "fragilityCurveParameters": [
        {
           "name": "point_two_sec_SA",
           "fullName": "0.2 sec Sa",
           "unit": "g",
           "description": "0.2 sec Sa value from hazard services"
        },
        {
            "name": "num_stories",
            "unit": "",
            "description": "number of stories in building inventory",
            "expression": "1"
        },
        {
            "name": "period",
            "unit": "",
            "description": "default building period",
            "expression": "1.08"
        }
     ],
     "id": "5b47b2d7337d4a36187c61c9"
   }
  ```