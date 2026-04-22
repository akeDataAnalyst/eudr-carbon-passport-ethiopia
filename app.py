import streamlit as st
import pandas as pd
import geopandas as gpd
import plotly.express as px
import plotly.graph_objects as go
import json

# 1. Page Configuration
st.set_page_config(page_title="EUDR Carbon Passport", layout="wide", page_icon="🌲")

st.title("EUDR Compliance & Carbon Asset Passport")
st.markdown("### Regional Smallholder Audit: Jimma, Ethiopia")
st.divider()

# 2. Data Ingestion (Bypassing environment hurdles)
@st.cache_data
def load_data():
    # Load NDVI Time-series
    df = pd.read_csv('data/processed/ndvi_baseline_2019_2025.csv')
    df['observation_date'] = pd.to_datetime(df['observation_date'])

    # Load Spatial Results (Native JSON for stability)
    with open('data/processed/final_carbon_passport.geojson', 'r') as f:
        geo_data = json.load(f)
    gdf = gpd.GeoDataFrame.from_features(geo_data['features'])

    return df, gdf

try:
    ts_df, farm_gdf = load_data()
    farm = farm_gdf.iloc[0]

    # 3. Top-Level Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Compliance Status", farm['spatial_compliance'], delta="EUDR 2020 Valid")
    col2.metric("Total Carbon Stock", f"{farm['total_carbon_stock']:.1f} tCO2e")
    col3.metric("Asset Value (USD)", f"${farm['carbon_asset_value_usd']:,.2f}")
    col4.metric("Canopy Stability", "95.39%", delta="High")

    st.divider()

    # 4. Visualization Rows
    left_col, right_col = st.columns([1, 1])

    with left_col:
            st.subheader("Vegetation Stability Trend")
            
            # Ensure date is strictly datetime (Fixes potential math errors)
            ts_df['observation_date'] = pd.to_datetime(ts_df['observation_date'])
            
            fig_ts = px.line(ts_df, x='observation_date', y='ndvi_value', 
                             title="NDVI Time-Series (Sentinel-2)",
                             line_shape='spline')
            
            # FIXED: Use a clean pd.Timestamp without arithmetic
            cutoff_date = pd.Timestamp('2020-12-31')
            
            fig_ts.add_vline(
                x=cutoff_date.timestamp() * 1000, # Convert to milliseconds for Plotly
                line_dash="dash", 
                line_color="red"
            )
            
            # Add a separate annotation if the vline text causes issues
            fig_ts.add_annotation(
                x=cutoff_date,
                y=0.9,
                text="EUDR Cutoff",
                showarrow=False,
                font=dict(color="red")
            )
    
            fig_ts.update_layout(
                template="plotly_dark", 
                hovermode="x unified",
                xaxis_title="Audit Timeline",
                yaxis_title="NDVI Index"
            )
            st.plotly_chart(fig_ts, use_container_width=True)
    with right_col:
        st.subheader("Geolocation & Risk Audit")
        # Simple coordinate display as fallback if mapbox token isn't set
        st.write(f"**Farm ID:** {farm['farm_id']}")
        st.write(f"**Center Lat/Lon:** 7.673, 36.835")
        st.write(f"**Buffer to Protected Zone:** {farm['forest_buffer_m']:.2f} meters")

        # Risk Indicator
        if farm['forest_buffer_m'] < 10:
            st.error("SPATIAL RISK: Farm boundary touches protected forest reserve.")
        else:
            st.success("SPATIAL SAFE: Farm is outside protected forest boundaries.")

    # 5. Auditor's Ledger
    st.subheader("Technical Audit Log")
    st.dataframe(ts_df.tail(10), use_container_width=True)

except Exception as e:
    st.error(f"Please ensure Phase 1-4 notebooks are run and data is saved. Error: {e}")
