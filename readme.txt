# EUDR Carbon Passport: Geospatial Compliance & Carbon Valuation

## Description
This project is a geospatial analytics pipeline designed to support compliance with the European Union Deforestation Regulation (EUDR) while enabling carbon asset valuation for smallholder farmers.

## Problem
Smallholder farmers risk exclusion from international markets due to:
- Lack of verifiable geospatial data
- Inability to prove compliance with deforestation regulations
- Limited access to carbon market opportunities

## Solution
We developed an automated geospatial audit system:

- Analyzed satellite imagery to track vegetation changes over time
- Performed spatial intersection with protected forest boundaries
- Estimated biomass and carbon stock using standard coefficients
- Evaluated vegetation stability and anomaly trends

## Recommendation
- Use satellite-based screening combined with targeted field verification
- Enable compliant farms to access carbon markets for additional income
- Deploy monitoring systems to detect and prevent deforestation risks

## Tech Stack
- Python (Pandas, NumPy, SciPy)
- Geospatial Analysis: Geopandas, Shapely, Fiona, Rasterio
- Remote Sensing (NDVI, Sentinel-2)
- Visualization: Plotly
- Deployment: Streamlit