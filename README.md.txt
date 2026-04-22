eudr-carbon-passport-ethiopia
# EUDR Carbon Passport: Geospatial Audit & Biomass Quantification

## Project Overview
**Title:** Automated EUDR Compliance & Carbon Asset Valuation Pipeline  
**Sector:** AgTech / Sustainability / Remote Sensing  
**Target Region:** Jimma Zone, Ethiopia (Smallholder Coffee)

This project is a production-grade geospatial analytical tool designed to align with the **European Union Deforestation Regulation (EUDR)**. It automates the verification of smallholder farm plots by integrating multi-spectral satellite imagery (Sentinel-2) with global forest boundary datasets to quantify environmental impact and legal compliance.

## The Problem
Smallholder farmers are often invisible to global supply chains. With the enforcement of EUDR, coffee and cocoa exporters must prove that their products:
1.  **Do not originate from deforested land** (Cut-off date: Dec 31, 2020).
2.  **Are legally situated** outside of protected forest reserves.

Manually auditing millions of smallholder plots is logistically impossible and prone to error. Without automated "Data Passports," these farmers risk being excluded from the European market, threatening their livelihoods.

## The Solution
I developed a 5-phase end-to-end pipeline that transforms raw satellite "pixels" into "Verified Carbon Assets."

### Satellite Ingestion & Baseline
* **Technology:** Python, Sentinel-2 (L2A) API Simulation.
* **Action:** Established a 7-year NDVI (Normalized Difference Vegetation Index) time-series (2019–2025).
* **Impact:** Verified the stability of the forest canopy before and after the 2020 EUDR deadline.

### Spatial Compliance Audit
* **Technology:** Geopandas, Fiona, Shapely, UTM Projections (EPSG:32637).
* **Action:** Performed a topological intersection between farm polygons and Protected Forest Reserve layers.
* **Impact:** Identified a **Spatial Risk** for plot `ETH-JIM-001` due to its 0.00m proximity/overlap with a restricted zone.

### Biomass & Carbon Modeling
* **Technology:** IPCC Tier 1 Coefficients, NumPy.
* **Action:** Converted mean NDVI signatures into Above Ground Biomass (AGB) and subsequently into Carbon Sequestration ($tCO_2e$).
* **Impact:** Quantified a carbon stock of **1,010.78 Tonnes CO2e** with a market value of **~$25,269.55 USD**.

### Trend & Anomaly Detection
* **Technology:** SciPy (Linear Regression), Statistics (Z-Scores).
* **Action:** Calculated a **Stability Score (CV: 4.61%)** and a long-term growth trend of **+0.0021 NDVI/year**.
* **Impact:** Proved the "Permanence" of the carbon asset through rigorous statistical validation.

## Key Results
* **Compliance Status:** RISK DETECTED (Encroachment on Protected Zone).
* **Vegetation Health:** 95.39% Stability (High-Forest Agroforestry).
* **Asset Value:** $25,269.55 Carbon Credit Potential.

## Recommendations
Based on the audit findings for the Jimma region, the following interventions are recommended:
1.  **Ground-Truth Survey:** Due to the 0.00m buffer detected, a high-precision GPS field visit is required to verify the exact farm boundary vs. the forest reserve.
2.  **Carbon Monetization:** If boundaries are cleared, the high canopy stability (95%+) makes this plot an ideal candidate for voluntary carbon market enrollment to provide a "Sustainability Premium" to the farmer.
3.  **Expansion:** Scale the automated Z-Score anomaly detection across the entire Jimma cooperative to provide real-time alerts for illegal logging.

## Tech Stack
* **Language:** Python 3.13
* **Geospatial:** Geopandas, Fiona, Shapely, Rasterio (Simulation).
* **Analytics:** Pandas, NumPy, SciPy.
* **Deployment:** Streamlit, Plotly.

---
*Developed as a proof-of-concept for the Senior Impact Analyst role at Enveritas.*