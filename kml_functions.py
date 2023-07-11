import pandas as pd
import geopandas as gpd
from fiona.drvsupport import supported_drivers
from shapely.geometry import Polygon


# Create Bounding Box - North and South Carolina coastal region
box = {'geometry': [Polygon([(-77.121369, 36.541466),
                             (-70.760165, 36.541466),
                             (-71.511922, 32.087495),
                             (-79.317663, 31.036502)])]}
bbox_gdf = gpd.GeoDataFrame(box, crs='EPSG:4326')
bbox_gdf.bounds

# Read in the KML and trim it to north and south carolina
def read_kml(kml_fp: str):
    """
    Read in a KML file to a geopandas dataframe.
    Trim it to North and South Carolina.

    Inputs
    -------
    kml_fp: str
        filepath where KML is located
    Outputs:
    --------
    gdf: gpd.GeoDataFrame
    """

    supported_drivers['KML'] = 'rw'
    gdf = gpd.read_file(kml_fp, driver='KML', bbox=bbox_gdf)
    return gdf


# Turn geometry into Latitude and longitude, create desired format
def create_refined_df(gdf: gpd.GeoDataFrame):
    """
    Build dataframe with desired columns.

    Input
    -----
    gdf: GeoDataFrame

    Output:
    -------
    df: DataFrame
    """
    df = pd.DataFrame(
        columns=['lat', 'lon', 'size', 'description'])
    df['lon'] = gdf.geometry.x
    df['lat'] = gdf.geometry.y
    return df