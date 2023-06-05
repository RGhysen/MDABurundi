import plotly.express as px
from utilss.descriptive.meteo import preprocess_meteo
from utilss.descriptive.exp41 import preprocess41
import pandas as pd
import numpy as np
import plotly.graph_objects as go


def create_line_plots(value):

    df_initial = preprocess_meteo.df[value]
    divider_meteo = ['Year', 'Month', 'Day', 'Hour', 'Minute']
    div_meteo = divider_meteo[:5-value]
    df_initial['date'] = pd.to_datetime(df_initial[div_meteo])

    fig1 = px.line(df_initial, y='LC_HUMIDITY', x = 'date', title='Humidity vs Time',
                    labels=dict(LC_HUMIDITY="Humidity", index="Time"))
    fig2 = px.line(df_initial, y='LC_RAININ', x = 'date', title='Raining Intensity (µ) vs Time',
                    labels=dict(LC_RAININ="Raining Intensity", index="Time"))
    fig3 = px.line(df_initial, y='LC_DAILYRAIN', x = 'date', title='Daily Rain vs Time',
                    labels=dict(LC_DAILYRAIN="Daily Rain", index="Time"))
    fig4 = px.line(df_initial, y='LC_WINDSPEED', x = 'date', title='Wind Speed vs Time',
                    labels=dict(LC_WINDSPEED="Wind Speed", index="Time"))
    fig5 = px.line(df_initial, y='LC_TEMP_QCL3', x = 'date', title='Temperature vs Time',
                    labels=dict(LC_TEMP_QCL3="Temperature(C)", index="Time"))
    
    if value == 2:

        divider_events = ['year', 'month', 'day', 'hour', 'minute']
        div_events = divider_events[:5-value]

        df_E = preprocess41.df_E

        df_E['date'] = pd.to_datetime(df_E[div_events])
        unique, counts = np.unique(df_E['date'], return_counts=True)
        counts_temp = counts/10
        counts_rain = counts/1000000
        date_count_temp = pd.DataFrame([unique, counts_temp]).transpose()
        date_count_temp.columns = ['date','counts(*0.1)']
        date_count_rain = pd.DataFrame([unique, counts_rain]).transpose()
        date_count_rain.columns = ['date','counts(*0.01)']


        fig2.add_trace(go.Scatter(y = date_count_rain['counts(*0.01)']*2, x = date_count_rain['date'], mode='markers'))
        fig2.update(layout_showlegend=False)
        fig3.add_trace(go.Scatter(y = date_count_rain['counts(*0.01)']*20, x = date_count_rain['date'], mode='markers'))
        fig3.update(layout_showlegend=False)
        fig5.add_trace(go.Scatter(y = date_count_temp['counts(*0.1)'], x = date_count_temp['date'], mode='markers'))
        fig5.update(layout_showlegend=False)

    return fig5, fig2, fig3, fig4, fig1
