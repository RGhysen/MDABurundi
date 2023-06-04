import pandas as pd
import datetime 
import numpy as np

def filter_df(df, day, hour):
    df.columns = ['location', 'date', 'hour', 'long', 'lat', 'voi']

    selected_df1 = df[df['location'] == 'Naamsestraat 62']
    selected_df1_date = selected_df1[selected_df1['date'] == day]
    selected_df1_hour = selected_df1_date[selected_df1_date['hour'] == hour]

    selected_df2 = df[df['location'] == 'Naamsestraat 81']
    selected_df2_date = selected_df2[selected_df2['date'] == day]
    selected_df2_hour = selected_df2_date[selected_df2_date['hour'] == hour]
    
    selected_df3 = df[df['location'] == 'Calveriekapel']
    selected_df3_date = selected_df3[selected_df3['date'] == day]
    selected_df3_hour = selected_df3_date[selected_df3_date['hour'] == hour]
    
    selected_df4 = df[df['location'] == 'Parkstraat 2']
    selected_df4_date = selected_df4[selected_df4['date'] == day]
    selected_df4_hour = selected_df4_date[selected_df4_date['hour'] == hour]
    
    return [df, selected_df1_hour, selected_df2_hour, selected_df3_hour, selected_df4_hour]