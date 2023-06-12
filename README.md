# Where do objects go on the sea floor?
Repo for earth lab capstone project. 
### Questions
Where do objects go on the ocean floor? 
Hazardous objects are unidentified all over the sea floor. What are the spatial patterns that we might see when using machine learning and artificial intelligence to identify such objects? Furthermore, will these objects be buried in sediment or will they move over time? 

### Goal
The goal of this project is to create a heat map of where objects are off the coast of North and South Carolina in the United States and to predict where they may move. 

This notebook will combine data from various different sources to gather information on where sea floor objects are located. Some of these objects may be hazardous and the hope is that this codebase can predict movement patterns and be used to mitigate risk of hazardous chemicals being released. 

The functions and work created here will display data for the region we've discussed. A user could use the functions here to load in data from sources for different regions/locations.

## Requirements

Python(Jupyter notebook) + Conda

## Usage

1. Download Artifical Reef KMZ [here](https://deq.nc.gov/marine-fisheries/coastal-fishing-information/artificial-reefs/reef-kmz-file/open)
2. Change the extention to `.zip`
3. Unzip the file - it will return a `.kml` and a `.xsl`. Rename the KML to `Reef_Material.kml` and move it to `earth-analytics/data/earthpy-downloads/`

All images are held in the `img` directory.

### Data
This repository uses these types of input data:
- KML
- TIF
- ASC

This can be run by selecting `run all` at the top of the jupyter notebook as long as the conda environment is activated.

## License
See [License](https://github.com/rmarowitz/seafloor-objects/blob/main/LICENSE)

## Credit
This software was developed by Robyn Marowitz and Allison Buchanan
[![DOI](https://zenodo.org/badge/627546755.svg)](https://zenodo.org/badge/latestdoi/627546755)

