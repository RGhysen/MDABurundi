# Import necessary libraries 
from dash import html, dcc
import dash_bootstrap_components as dbc
from utils.night_noise import figure_map

# Define the page layout
layout = dbc.Container([
    html.Br(),
    dbc.Row([
        html.Center(html.H1("Research Question 3")),
        html.Br(),
        html.Hr(),
        html.P('Noise is a sensitive topic in many places, especially in cities!'),
        html.P('Governments often have specific regulations to keep noise levels within certain limitsThe World Health Organization (WHO) recommends outdoor noise levels not exceeding 55 dB(A) during daytime and 40 dB(A) during nighttime for residential areas. Leuven is giving special attention to noise problems (mostly related to student life) They (City & KU Leuven) gathered noise data (for noise in The Naamsestraat in 2022), for the following locations: (see map)'),
        dcc.Graph(figure=figure_map.figure_map)
    ])
        
])
