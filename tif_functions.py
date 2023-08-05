import pandas as pd
import rioxarray as rxr


def read_tifs(path):
    """Read in tif files and get information from them.
    
     Inputs
    ------
    path: str
        filepath where TIF is located.

    Outputs: 
    ------
    None: None
    """
    test = rxr.open_rasterio(path, masked=True)
    print("The crs of your data is:", test.rio.crs)
    print("The nodatavalue of your data is:", test.rio.nodata)
    print("The shape of your data is:", test.shape)
    print("The spatial resolution for your data is:", test.rio.resolution())
    print("The metadata for your data is:", test.attrs)
    return None

def night_lights_tif_to_df(filepath, name):
    """Open night lights data and trasnform to a dataframe."""
    # Open TIF and read it in array
    step1 = rxr.open_rasterio(filepath, masked=True).squeeze()
    step2 = step1.where(step1>0)
    # turn array into dataframe
    df = step2.to_dataframe(name).dropna()
    return df


def open_tif_to_df(tif_fp, name):
    """

    Read in a TIF file to a data frame and drop NA values.

    Inputs
    ------
    tif_fp: str
        filepath where TIF is located.
    name: str
        Name of dataframe. 
    Outputs: 
    ------
    df = pd.DataFrame

    """
    
    df = tif_fp.to_dataframe(name).dropna()
    return df
