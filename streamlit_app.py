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
import plotly.express as px 
import streamlit as st
import plotly.graph_objects as go

# # Load county mention data 
# mentions = [('United States', 100), ('Canada', 50), ('Mexico', 20)] 

# # Convert mentions to DataFrame
# mentions_df = pd.DataFrame([
#   ('United States', 10),
#   ('Canada', 20),
#   ('Mexico', 30)  
# ])

# # Load tax credit data
# tax_credits = pd.read_csv('ScreenCrib Tax Credit Sheet.csv')

# # Create figure
# fig = px.choropleth(mentions_df, 
#               locations='country',
#               scope='north america')

# # Create hover text from tax credit info                   
# def get_popup_text(country):

#   row = tax_credits[tax_credits['Country'] == country]
  
#   if len(row) == 0:
#     # No match found
#     return "No tax credit info available"

#   return f"""
#     Tax Credit Rate: {row['Tax credits'].values[0]}  
#     Eligibility: {row['Eligibility'].values[0]}
#     Description: {row['Country description'].values[0]}
#     Source: {row['Links'].values[0]}
#   """
                              
# # Generate hover text and assign to figure  
# hover_texts = []
# for country in mentions:
#   hover_texts.append(get_popup_text(country))
  
# hover_dict = dict(zip(mentions, hover_texts))

# # Generate list of hover strings
# hover_strings = []
# for country, text in hover_dict.items():
#   hover_strings.append(text) 

# # Pass list to hovertemplate
# fig.update_traces(hovertemplate=hover_strings)

# df = px.data.gapminder().query("year == 2007")
# fig = px.choropleth(df, locations="iso_alpha", 
#                     color="lifeExp", 
#                     hover_name="country",
#                     scope="world")

# fig = go.Figure(data=go.Choropleth(
#     locations=['CA', 'TX', 'NY'], # Spatial coordinates
#     z = [1.0, 2.0, 3.0], # Data to be color-coded
#     locationmode = 'USA-states', # set of locations match entries in `locations`
#     colorscale = 'Reds',
#     colorbar_title = "Colorbar Title Goes Here",
# ))

# fig.update_layout(
#     title_text = 'USA States Choropleth Map',
#     geo_scope='usa', # limit map scope to USA
# )

# st.plotly_chart(fig)

import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title='Film Tax Credits', page_icon=':clapper:')

# Load data
data = pd.read_csv('data.csv')

# Map plot
fig, ax = plt.subplots()
ax.scatter(data['Longitude'], data['Latitude'], s=data['Tax Credit']*2000, 
           c=data['Tax Credit'], cmap='Reds')

# Color bar
plt.colorbar() 

# Labels 
for i, country in data.iterrows():
    plt.text(country['Longitude']+5, country['Latitude'], country['Country'], size=12)

# Plot  
st.pyplot(fig)

# Info
st.markdown("""
This interactive map allows you to visualize the tax credit incentives offered to film production across different countries.
            
* Circle size correlates to the percentage tax credit  
* Color indicates the credit percentage, with darker red signifying higher percentages
* Rolling over circles shows the country name and tax credit percentage

Use this to help determine which countries offer the most favorable incentives!
""")