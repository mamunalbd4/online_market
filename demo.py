#Import Python Libraries
import pandas as pd
import folium #to install folium using Anaconda: conda install -c conda-forge folium
import geopandas as gpd #to install geopandas, run this code in the conda terminal: conda install geopandas
from folium.features import GeoJsonTooltip
import streamlit as st #You can follow the instructions in the beginner tutorial to install Streamlit if you don't have it
from streamlit_folium import folium_static
import requests
from io import StringIO

# GitHub CSV file URL
github_csv_url = 'https://github.com/mamunalbd4/online_market/blob/main/Bangladesh_property_prices.csv'

# Fetch CSV data using requests
response = requests.get(github_csv_url)
csv_data = response.text

# Convert CSV data to pandas DataFrame
df = pd.read_csv(StringIO(csv_data))

# Display the DataFrame using Streamlit
st.title('CSV Data Display')
st.dataframe(df)
