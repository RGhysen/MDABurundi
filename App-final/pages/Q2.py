# Import necessary libraries 
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
from app import app
from datetime import date

df_iris = px.data.iris()

dropdown1 = dcc.Dropdown(
    id='id_selection_first',
    options=[{"label":'Sepal Width','value':'sepal_width'},
             {"label":'Sepal Length','value':'sepal_length'},
             ],
    value='sepal_width')

dropdown2 = dcc.Dropdown(
    id='id_selection_second',
    options=[{"label":'Sepal Width','value':'sepal_width'},
             {"label":'Sepal Length','value':'sepal_length'},
             ],
    value='sepal_length')

datepicker1 = dcc.DatePickerSingle(
    id='my-date-picker-single',
    min_date_allowed=date(2022, 1, 1),
    max_date_allowed=date(2022, 12, 31),
    initial_visible_month=date(2022, 1, 1),
    date=date(2022, 1, 1),
    display_format= 'YYYY-MM-DD')
    
datepicker2 = dcc.DatePickerRange(
        id='date-picker-range',
        min_date_allowed=date(2022, 1, 1),
        max_date_allowed=date(2022, 12, 31),
        initial_visible_month=date(2022, 1, 1),
        show_outside_days=True,
        day_size=32,
        display_format='DD/MM/YYYY',
        clearable=True,
        style={'zIndex': 10}
    )

parameters = dbc.Row(dbc.Col(
    html.Div([
        html.P('Select Parameter for X axis'),
        dropdown1,
        html.Br(),
        html.P('Select Parameter for Y axis'),
        dropdown2,
        html.Br(),
        html.P("Select Time Period: #1"),
        datepicker2,
        html.Br(),
        html.Br(),
        html.P("Select Time Period: #2"),
        dbc.InputGroup([
            dbc.Input(id='id_start_date',value="2020-01-01", type="text")],className="mb-3",),
        dbc.InputGroup([
            dbc.Input(id='id_end_date',value="2021-01-01",type="text")],className="mb-3",),
            ])
    ))

# Define the final page layout
layout = dbc.Container([
    html.Br(),
    dbc.Row([
        html.Center(html.H1("Research Question 2")),
        html.Br(),
        html.Hr(),        
        dbc.Col([
            html.P("This is for parameter selection for Q1."), 
            parameters,
            html.Br(),
            dbc.Button("Plot", id = "example-button", color="primary", className="me-1")
            ], width=3), 

        dbc.Col([
            html.P("This is for output"), 
            dcc.Graph(id = "example-output", figure = {})
        ]),
    ])
])

@app.callback(
    Output("example-output", "figure"),
    Input("example-button", 'n_clicks'),
    State("id_selection_first", "value"),
    State("id_selection_second", "value"),
)

def plot_figure(click, id_selection_first_value, id_selection_second_value):
    fig = px.scatter(df_iris, x = id_selection_first_value, y = id_selection_second_value)
    return fig