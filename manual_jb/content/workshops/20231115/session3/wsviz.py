from pyincore import Dataset, DataService, HazardService
import geopandas as gpd
import folium
from folium.plugins import MousePosition
from pathlib import Path
import rasterio
from rasterio.plot import show_hist

def show_tornado(client, tornado_model_metadata):
    tornado_dataset_id = tornado_model_metadata['datasetId']
    tornado_dataset = Dataset.from_data_service(tornado_dataset_id, DataService(client))
    tornado_gdf = gpd.read_file(tornado_dataset.local_file_path)
    map = tornado_gdf.explore(
        column="ef_rating", 
        tooltip="ef_rating",  
        popup=True,  
        cmap="Set1"  # use "Set1" matplotlib colormap)
    )
    
    MousePosition().add_to(map)
    return map

def show_tornado_by_id(client, id):
    hazardsvc = HazardService(client)
    metadata = hazardsvc.get_tornado_hazard_metadata(id)
    return show_tornado(client, metadata)

def show_eq_hist(client, eq_metadata):
    eq_dataset_id=eq_metadata['rasterDataset']['datasetId']
    eq_dataset = Dataset.from_data_service(eq_dataset_id, DataService(client))
    raster_file_path = Path(eq_dataset.local_file_path).joinpath(eq_dataset.metadata['fileDescriptors'][0]['filename'])
    src = rasterio.open(raster_file_path)
    show_hist(
        src, bins=50, lw=0.0, stacked=False, alpha=0.3,
        histtype='stepfilled', title="Histogram")