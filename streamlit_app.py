from collections import namedtuple
import altair as alt
import math
import pandas as pd
import plotly
import folium
import json
from streamlit_folium import folium_static
import streamlit as st

"""
# Film Tax Credit Incentive Analysis Tool

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
# st.write(" ## This map was created using Folium in Streamlit")
# st.write(" ### Film Tax Credit Map 1")

# # Create a basic map
# map = folium.Map(location=[45.5236, -122.6750])

# # Add a marker
# folium.Marker([45.5244, -122.6699], popup='Mt. Hood Meadows').add_to(map)  

# # Display map using Streamlit
# folium_static(map)

# --------------------------------------------------------
# Plot2

# Add some text 
st.write(" ## This map was created using Folium in Streamlit")
st.write(" ### Film Tax Credit Map 2")
state_data = pd.read_csv('US_Film_Tax_Credit_Minimum_July2023.csv')

map2 = folium.Map(location=[48, -102], zoom_start=3)

folium.Choropleth(
    geo_data='us-states.json',
    name="choropleth",
    data=state_data,
    columns=["State", "Film Tax Credit Minimum Rate"],
    key_on="feature.id",
    fill_color="YlGn",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Film Tax Credit Minimum Rate (%)",
).add_to(map2)

folium_static(map2)