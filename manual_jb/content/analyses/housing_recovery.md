# Housing recovery

**Description**

The analysis predicts building values and value changes over time following a disaster event. The model is calibrated 
with respect to demographics, parcel data, and building value trajectories following Hurricane Ike (2008) in 
Galveston, Texas. The model predicts building value at the parcel level for 8 years of observation. The models rely 
on Census (Decennial or American Community Survey, ACS) and parcel data immediately prior to the disaster event 
(year -1) as inputs for prediction.

The Galveston, TX example makes use of 2010 Decennial Census and Galveston County Appraisal District (GCAD) 
tax assessor data and outputs from other analysis (i.e., Building Damage, Housing Unit Allocation, 
Population Dislocation) . 

The CSV outputs of the building values for the 6 years following the disaster event (with year 0 being the impact year).

**Contributors**

- Science: Wayne Day, Sarah Hamideh
- Implementation: Michal Ondrejcek, Santiago Núñez-Corrales, and NCSA IN-CORE Dev Team

**Related publications**

- Hamideh, S., Peacock, W. G., & Van Zandt, S. (2018). Housing recovery after disasters: Primary versus seasonal/vacation housing markets in coastal communities. *Natural Hazards Review*.

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`base_year` | `int` | Base year | Base year is used to calculate improvement age. It needs to be set to the tax assessment year representing pre-disaster building values. For example for GCAD data which represents improvement valuation before Hurricane Ike impacts. Deafult 2008.
`result_name` <sup>*</sup> | `str` | Result name | Name of the result dataset.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`population_dislocation` <sup>*</sup> | [`incore:popDislocation`](https://tools.in-core.org/semantics/api/types/incore:popDislocation) | Population Dislocation | A csv file with Population Dislocation aggregated to the block group level.
`building_area` <sup>*</sup> | [`incore:buildingInventoryArea`](https://tools.in-core.org/semantics/api/types/incore:buildingInventoryArea) | Building inventory area |  A csv file with Building square footage and damage. Damage is the actual building value loss in percentage terms observed through the County Appraisal District (GCAD) data. If damage column (dmg) is not available value loss is calculated from Population dislocation's rplosses and damage state (DS) values.
`census_block_groups_data` <sup>*</sup> | [`incore:censusBlockGroupsData`](https://tools.in-core.org/semantics/api/types/incore:censusBlockGroupsData) | Census block groups data | Census ACS data, 2010 5yr data for block groups available at IPUMS NHGIS web site.
`census_appraisal_data` | [`incore:censusAppraisalData`](https://tools.in-core.org/semantics/api/types/incore:censusAppraisalData) | Census appraisal data | Census data, 2010 Decennial Census District (GCAD) Census data. The json file must contain categories B25002_001E, B25002_001M, B25004_006E and B25004_006M.

**Output datasets**

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`result` <sup>*</sup> | [`incore:buildingValues`](https://tools.in-core.org/semantics/api/types/incore:buildingValues) | | Results | A csv file with building values for the 6 years following the disaster event (with year 0 being the impact year). A csv file with the building values for the 6 years following the disaster event (year -1 denotes pre-impact conditions and 0 being the impact year). Index year values represent building values against a base, pre-impact value.

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create housing recovery
    housing_rec = HousingRecovery(client)
    
    # Load input datasets
    housing_rec.load_remote_input_dataset("population_dislocation", pop_disl_id)
    housing_rec.load_remote_input_dataset("building_area", bldg_area_id)
    housing_rec.load_remote_input_dataset("census_block_groups_data", census_bg_id)

    # Countty FIPS code
    # Specify the result name
    result_name = "building_values"
    
    # Set analysis parameters
    housing_rec.set_parameter("result_name", result_name)

    # Run Analysis
    housing_rec.run_analysis()

```

full analysis: [housing_recovery.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/housing_recovery.ipynb)
