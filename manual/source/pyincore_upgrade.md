## pyIncore Upgrade Guide

This page will help you to upgrade/refactor your python code to be compatible with the latest version of pyIncore/pyIncore-viz API changes.
 
### Previous versions to pyIncore 0.6.4 (or beyond)

From pyIncore 0.6.4 (and beyond), a local fragility mapping class and a local fragility class are introduced. In order to support this addition, how to input a fragility mapping to an analysis has changed. Instead of using the ID of the mapping, a mapping Set object is used. If you are using an analysis with a fragility mapping as an input, please upgrade your code using the example below:

- Before
    ```
    mapping_id = "5b48fb1f337d4a478e7bd54d"
    bldg_dmg.set_parameter(‘mapping_id', mapping_id
    ```
- After (pyIncore 0.6.4)
    ```
    fragility_service = FragilityService(client)
    mapping_id = "5b48fb1f337d4a478e7bd54d"
    mapping_set = MappingSet(fragility_service.get_mapping(mapping_id))
    
    bldg_dmg.set_input_dataset('dfr3_mapping_set', mapping_set)
    ```

