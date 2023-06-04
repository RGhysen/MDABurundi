# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc

# Define the navbar structure
def Navbar():

    layout = html.Div([
        dbc.NavbarSimple(
            children=[
                dbc.NavItem(dbc.NavLink("Home", href="/home")),
<<<<<<< HEAD
                dbc.NavItem(dbc.NavLink("Data Explorations - Exploratory Visualisations", href="/visuals")),
                dbc.NavItem(dbc.NavLink("Noise Prediction Model", href="/predictions"))
=======
                dbc.NavItem(dbc.NavLink("Descriptive Analysis 1", href="/A1")),
                dbc.NavItem(dbc.NavLink("RQ 1", href="/Q1")),
                dbc.NavItem(dbc.NavLink("RQ 2", href="/Q2")),
                dbc.NavItem(dbc.NavLink("RQ 3", href="/Q3")),
>>>>>>> 780801e9ed38dc89b7de1f3b1f1fab026bb97be3
            ] ,
            brand="MDA App",
            brand_href="/",
            color="dark",
            dark=True,
        ), 
    ])

    return layout