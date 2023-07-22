from collections import namedtuple
import altair as alt
import math
import pandas as pd
import plotly
import folium
from streamlit_folium import folium_static
import streamlit as st

"""
# Film Tax Credit Incentive Analysis Tool

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

Upload your movie script and your overall budget to see how much you can save by filming in a certain state/country.
"""

movie_script = st.file_uploader("Upload your movie script", type="pdf")
overall_budget = st.file_uploader("Upload your overall budget", type="pdf")

st.write("## How much can you save by filming in a certain state/country?")

# list of tuples for the most common countries mentioned in the movie script with the amount of times they are mentioned
most_common_countries = [("United States", 20), ("United Kingdom", 15), ("Canada", 10)]

# grand total for budget
grand_total = 1000000

# Lets use langchain to find similar countries to the ones mentioned in the script

# Plot 1

# Add some text 
st.write(" ## This map was created using Folium in Streamlit")
st.write(" ### Film Tax Credit Map 1")

# Create a basic map
map = folium.Map(location=[45.5236, -122.6750])

# Add a marker
folium.Marker([45.5244, -122.6699], popup='Mt. Hood Meadows').add_to(map)  

# Display map using Streamlit
folium_static(map)

# --------------------------------------------------------
# Plot2

# Add some text 
st.write(" ## This map was created using Folium in Streamlit")
st.write(" ### Film Tax Credit Map 2")
url = (
    "https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us-states.json"
)
state_geo = f"{url}/us-states.json"
state_unemployment = f"{url}/US_Unemployment_Oct2012.csv"
state_data = pd.read_csv(state_unemployment)

map2 = folium.Map(location=[48, -102], zoom_start=3)

folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["State", "Unemployment"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Unemployment Rate (%)",
).add_to(map2)

folium.LayerControl().add_to(map2)