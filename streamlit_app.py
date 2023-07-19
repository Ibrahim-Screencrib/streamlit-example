# from collections import namedtuple
# import altair as alt
# import math
# import pandas as pd
# import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


# with st.echo(code_location='below'):
#     total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
#     num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

#     Point = namedtuple('Point', 'x y')
#     data = []

#     points_per_turn = total_points / num_turns

#     for curr_point_num in range(total_points):
#         curr_turn, i = divmod(curr_point_num, points_per_turn)
#         angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
#         radius = curr_point_num / total_points
#         x = radius * math.cos(angle)
#         y = radius * math.sin(angle)
#         data.append(Point(x, y))

#     st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
#         .mark_circle(color='#0068c9', opacity=0.5)
#         .encode(x='x:Q', y='y:Q'))

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import geoplot as gplt
import folium
import streamlit as st
from streamlit_folium import folium_static
from shapely.geometry import Point

# # List of tuples containing movie script data
# movie_scripts_data = [('USA', 100), ('France', 80)]  # Replace with your actual data

# # Convert the list of tuples to a DataFrame
# df_movie_scripts = pd.DataFrame(movie_scripts_data, columns=['Country', 'Count'])

# # Load the tax credit data
# df_tax_credits = pd.read_csv('tax_credits.csv')  # 'Country', 'TaxCreditsRate', 'Eligibility', 'Description', 'Link'

# # Merge the dataframes
# df = pd.merge(df_movie_scripts, df_tax_credits, on='Country')

# # Load the world map
# world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# # Merge with world map
# world['Country'] = world['name']
# df_world = pd.merge(world, df, on='Country', how='left')
# df_world['Count'] = df_world['Count'].fillna(0)  # Replace NaN counts with 0

# # Generate the basic world map using geoplot
# plt.figure(figsize=(15, 10))
# gplt.choropleth(df_world, hue='Count', cmap='Greys', figsize=(10, 5))

# # Generate the interactive world map with folium
# map = folium.Map(location=[0, 0], zoom_start=2)

# Add the countries to the map with pop-up info
# for i in range(len(df_world)):
#     try:
#         location = [df_world.at[i, 'geometry'].centroid.y, df_world.at[i, 'geometry'].centroid.x]
#         popup = folium.Popup(
#             f"Country: {df_world.at[i, 'Country']}<br>"
#             f"Count: {df_world.at[i, 'Count']}<br>"
#             f"Tax credit rate: {df_world.at[i, 'TaxCreditsRate']}<br>"
#             f"Eligibility: {df_world.at[i, 'Eligibility']}<br>"
#             f"Description: {df_world.at[i, 'Description']}<br>"
#             f"<a href='{df_world.at[i, 'Link']}'>Link</a>",
#             max_width=300
#         )
#         folium.Marker(location, popup=popup).add_to(map)
#     except:
#         pass

# Use Streamlit to show the interactive map
st.title('World Map with Movie Scripts and Tax Credits Data')
# folium_static(map)
