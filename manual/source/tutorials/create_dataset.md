# Create and Use Dataset Object
Any analysis in pyIncore, by default uses Dataset Object, DFR3 CurveSet Object and DFR3 MappingSet Object. This
 tutorial introduces users to the basic concept of creating and using **Dataset Object** via either loading from local
  files, or connecting to remote IN-CORE Data Services.

```python
import pandas as pd
from pyincore import IncoreClient, DataService, SpaceService, Dataset, FragilityService, MappingSet
from pyincore.analyses.buildingdamage import BuildingDamage
from pyincore.analyses.meandamage import MeanDamage
```


```python
client = IncoreClient()
data_services = DataService(client)
space_services = SpaceService(client)
```

# 0. Upload Dataset to Data Services
Note that this is completely optional. You can work with local datasets and we will cover that in section 2.

## Write Metadata
- **Metadata** is a string describing the dataset. 
- **dataType** needs to be align with the analyses in pyincore.
- **format** is the file format of the dataset. Currently we support "shapefile", "table", "Network", "textFiles
", "raster", "geotiff" and etc. Please consult with development team if you intend to post a new format.

```python
# note you have to put the correct dataType as well as format
dataset_metadata = {
    "title":"ERGO Memphis Hospitals",
    "description": "ERGO Memphis Hospitals",
    "dataType": "ergo:buildingInventoryVer5",
    "format": "shapefile"
}
```

## Upload Metadata
This will create the dataset in the service.

```python
created_dataset = data_services.create_dataset(dataset_metadata)
dataset_id = created_dataset['id']
print('dataset is created with id ' + dataset_id)
```

    dataset is created with id 5f1ef1c32fab4d660a9c32b2


## Attach Files to the Dataset Created
Using the dataset id we attach the files that contain the data for the dataset.

```python
files = ['all_bldgs_ver5_WGS1984.shp',
         'all_bldgs_ver5_WGS1984.shx',
         'all_bldgs_ver5_WGS1984.prj',
         'all_bldgs_ver5_WGS1984.dbf',
         'all_bldgs_ver5_WGS1984.fix',
         'all_bldgs_ver5_WGS1984.qix']
full_dataset = data_services.add_files_to_dataset(dataset_id, files)
```


```python
full_dataset
```




    {'id': '5f1ef1c32fab4d660a9c32b2',
     'deleted': False,
     'title': 'ERGO Memphis Hospitals',
     'description': 'ERGO Memphis Hospitals',
     'date': '2020-07-27T15:24:51+0000',
     'creator': 'cwang138',
     'contributors': [],
     'fileDescriptors': [{'id': '5f1ef1c753587c306ede0785',
       'deleted': False,
       'filename': 'all_bldgs_ver5_WGS1984.shp',
       'mimeType': 'application/octet-stream',
       'size': 716,
       'dataURL': '5f/1e/5f1ef1c753587c306ede0785/all_bldgs_ver5_WGS1984.shp',
       'md5sum': '6e1e96c4a6cf5762317054fe813d82bf'},
      {'id': '5f1ef1c753587c306ede0788',
       'deleted': False,
       'filename': 'all_bldgs_ver5_WGS1984.shx',
       'mimeType': 'application/octet-stream',
       'size': 276,
       'dataURL': '5f/1e/5f1ef1c753587c306ede0788/all_bldgs_ver5_WGS1984.shx',
       'md5sum': '799965579a991f1f45afeb22c07c5ece'},
      {'id': '5f1ef1c753587c306ede078b',
       'deleted': False,
       'filename': 'all_bldgs_ver5_WGS1984.prj',
       'mimeType': 'application/octet-stream',
       'size': 205,
       'dataURL': '5f/1e/5f1ef1c753587c306ede078b/all_bldgs_ver5_WGS1984.prj',
       'md5sum': '30e5566d68356bfc059d296c42c0480e'},
      {'id': '5f1ef1c753587c306ede078e',
       'deleted': False,
       'filename': 'all_bldgs_ver5_WGS1984.dbf',
       'mimeType': 'application/octet-stream',
       'size': 10859,
       'dataURL': '5f/1e/5f1ef1c753587c306ede078e/all_bldgs_ver5_WGS1984.dbf',
       'md5sum': '7ea0a4c769ca254a6b4821f2e737eb35'},
      {'id': '5f1ef1c753587c306ede0791',
       'deleted': False,
       'filename': 'all_bldgs_ver5_WGS1984.fix',
       'mimeType': 'application/octet-stream',
       'size': 277,
       'dataURL': '5f/1e/5f1ef1c753587c306ede0791/all_bldgs_ver5_WGS1984.fix',
       'md5sum': '15c08cc1fac086265cb57ceac0785acb'},
      {'id': '5f1ef1c753587c306ede0794',
       'deleted': False,
       'filename': 'all_bldgs_ver5_WGS1984.qix',
       'mimeType': 'application/octet-stream',
       'size': 632,
       'dataURL': '5f/1e/5f1ef1c753587c306ede0794/all_bldgs_ver5_WGS1984.qix',
       'md5sum': 'a1cba745192516c7e1cd0e4d4d13497c'}],
     'dataType': 'ergo:buildingInventoryVer5',
     'storedUrl': '',
     'format': 'shapefile',
     'sourceDataset': '',
     'boundingBox': [-90.07376669874641,
      35.03298062856903,
      -89.71464767735003,
      35.207753220358086],
     'networkDataset': None}



# Optional: Moving your dataset to INCORE space 
If you would like other people to access your data, you can move your dataset to a certain space. Otherwise it wil
 be in your own space and not public accessible.


```python
# for example, adding to incore space
response = space_services.add_dataset_to_space("5df8fd18b9219c068fb0257f", dataset_id)
```

# 1. Load Dataset from Data Services


```python
building_dataset_id = "5a284f0bc7d30d13bc081a28"
buildings = Dataset.from_data_service(building_dataset_id, data_services)
buildings
```

    Dataset already exists locally. Reading from local cached zip.
    Unzipped folder found in the local cache. Reading from it...





    <pyincore.dataset.Dataset at 0x1a233361d0>



# 2. Load Dataset from Local Files
- Note you have to make sure you pass the right **data_type** when constructing Dataset Object from scratch
- To look up what **data_type** it should be, please refer to the **source code** of the analyses
- You want to look take a look at the **spec** section -> **input_datasets** -> **type**


```python
buildings = Dataset.from_file("./5a284f0bc7d30d13bc081a28/all_bldgs_ver5_WGS1984.shp", data_type="ergo:buildingInventoryVer5")
buildings
```




    <pyincore.dataset.Dataset at 0x1a233a3978>



# 3. Input the Dataset Object in Analyses


```python
# for example: Building Damage Analyses
bldg_dmg = BuildingDamage(client)
bldg_dmg.set_input_dataset("buildings", buildings)  
```




    True




```python
# Memphis Earthquake damage
# New madrid earthquake using Atkinson Boore 1995
hazard_type = "earthquake"
hazard_id = "5b902cb273c3371e1236b36b"

# Earthquake mapping
mapping_id = "5b47b350337d4a3629076f2c"
fragility_service = FragilityService(client)
mapping_set = MappingSet(fragility_service.get_mapping(mapping_id))
bldg_dmg.set_input_dataset('dfr3_mapping_set', mapping_set)

result_name = "memphis_eq_bldg_dmg_result"
bldg_dmg.set_parameter("result_name", result_name)
bldg_dmg.set_parameter("hazard_type", hazard_type)
bldg_dmg.set_parameter("hazard_id", hazard_id)
bldg_dmg.set_parameter("num_cpu", 4)

# Run Analysis
bldg_dmg.run_analysis()
```




    True



# 4. Chaining the output Dataset Object in subsequent Analyses
Output is a dataset object as well, here is how to display


```python
print("output datasets:", bldg_dmg.get_output_datasets())
bldg_dmg.get_output_dataset('result').get_dataframe_from_csv().head()
```

    output datasets: {'result': <pyincore.dataset.Dataset object at 0x1a245c17b8>}

key name | type | name | description
--- | --- | --- | ---
`result` <sup>*</sup> | `ergo:buildingDamageVer4` | Results | A dataset containing results <br>(format: CSV).




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>guid</th>
      <th>immocc</th>
      <th>lifesfty</th>
      <th>collprev</th>
      <th>insignific</th>
      <th>moderate</th>
      <th>heavy</th>
      <th>complete</th>
      <th>demandtype</th>
      <th>demandunits</th>
      <th>hazardval</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a41e7dcc-3b82-42f2-9dbd-a2ebdf39d453</td>
      <td>0.848146</td>
      <td>0.327319</td>
      <td>2.722903e-02</td>
      <td>0.151854</td>
      <td>0.520828</td>
      <td>0.300089</td>
      <td>2.722903e-02</td>
      <td>pga</td>
      <td>g</td>
      <td>0.309996</td>
    </tr>
    <tr>
      <th>1</th>
      <td>254d1dd8-5d2f-4737-909b-59cc64ca72d4</td>
      <td>0.844340</td>
      <td>0.328296</td>
      <td>2.860487e-02</td>
      <td>0.155660</td>
      <td>0.516045</td>
      <td>0.299691</td>
      <td>2.860487e-02</td>
      <td>pga</td>
      <td>g</td>
      <td>0.309996</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4253802e-b3e5-4ed3-93b0-dda9ef6362b0</td>
      <td>0.896775</td>
      <td>0.480926</td>
      <td>8.756764e-02</td>
      <td>0.103225</td>
      <td>0.415849</td>
      <td>0.393358</td>
      <td>8.756764e-02</td>
      <td>pga</td>
      <td>g</td>
      <td>0.308425</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b185d5b6-5bc0-43a3-800a-c046017372ab</td>
      <td>0.810564</td>
      <td>0.331283</td>
      <td>4.895657e-02</td>
      <td>0.189436</td>
      <td>0.479281</td>
      <td>0.282327</td>
      <td>4.895657e-02</td>
      <td>pga</td>
      <td>g</td>
      <td>0.299533</td>
    </tr>
    <tr>
      <th>4</th>
      <td>7b5dc4f6-ef5e-4178-9836-f044b4b92f0d</td>
      <td>0.970342</td>
      <td>0.154675</td>
      <td>7.649816e-11</td>
      <td>0.029658</td>
      <td>0.815668</td>
      <td>0.154675</td>
      <td>7.649816e-11</td>
      <td>1.0 sa</td>
      <td>g</td>
      <td>0.237687</td>
    </tr>
  </tbody>
</table>
</div>



## Chaining with Mean Damage Analysis


```python
md = MeanDamage(client)

# use the output of road damage
building_damage_output = bldg_dmg.get_output_dataset('result')
md.set_input_dataset("damage", building_damage_output)

md.load_remote_input_dataset("dmg_ratios", "5a284f2ec7d30d13bc08209a")
md.set_parameter("result_name", "building_mean_damage")
md.set_parameter("damage_interval_keys",
                 ["insignific", "moderate", "heavy", "complete"])
md.set_parameter("num_cpu", 1)

# Run analysis
md.run_analysis()
```




    True




```python
print("output datasets:", md.get_output_datasets())
md.get_output_dataset('result').get_dataframe_from_csv().head()[['meandamage', 'mdamagedev']]
```

    output datasets: {'result': <pyincore.dataset.Dataset object at 0x1a24697518>}

key name | type | name | description
--- | --- | --- | ---
`result` <sup>*</sup> | `ergo:meanDamage` | Results | A dataset containing results <br>(format: CSV).



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>meandamage</th>
      <th>mdamagedev</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.271043</td>
      <td>0.238080</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.271340</td>
      <td>0.239546</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.360131</td>
      <td>0.275124</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.274576</td>
      <td>0.256321</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.211648</td>
      <td>0.160879</td>
    </tr>
  </tbody>
</table>
</div>



# Utility Methods


```python
buildings.get_inventory_reader()
```




    <open Collection './5a284f0bc7d30d13bc081a28/all_bldgs_ver5_WGS1984.shp:all_bldgs_ver5_WGS1984', mode 'r' at 0x1a2452b128>


