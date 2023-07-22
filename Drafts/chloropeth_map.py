import plotly
import pandas as pd
import streamlit as st

# this map uses plotly library
# Read data 
df = pd.read_csv('simple tax credit sheet.csv')

# Read values of axes 
tax_credits = df['Tax Credit']
# health_exp= df.iloc[:,3]

# Define the data to be visualised and some of the parameters of the visualisation
data = [ dict(
        type = 'choropleth',
        colorscale = 'Rainbow',
        locations = df['Code'],
        z = tax_credits,
        text = df['Country'],

        colorbar = dict(
            title = 'minimum percentage rate', 
            titlefont=dict(size=12),
            tickfont=dict(size=12))
      ) ]

# Define layout
layout = dict(
    title = 'Film Tax Credits Global Chloropeth Map',
    titlefont = dict(size=40),
    geo = dict(
        showframe = True,
        showcoastlines = True,
        projection = dict(type = 'equirectangular')
              )
             )
