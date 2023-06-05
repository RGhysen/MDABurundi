from utils.descriptive.meteo import preprocess_meteo
from dash import dash_table
import pandas as pd

def create_table(value):
    df_initial = preprocess_meteo.df[value]
    df_head = df_initial.head(n=5)
    df_tail = df_initial.tail(n=5)
    df_combine = pd.concat([df_head, df_tail])
    df_combine['LC_HUMIDITY'] = df_combine['LC_HUMIDITY'].round(2)
    df_combine['LC_DWPTEMP'] = df_combine['LC_DWPTEMP'].round(2)
    df_combine['LC_RAD'] = df_combine['LC_RAD'].round(2)
    df_combine['LC_RAININ'] = df_combine['LC_RAININ'].round(2)
    df_combine['LC_DAILYRAIN'] = df_combine['LC_DAILYRAIN'].round(2)
    df_combine['LC_WINDDIR'] = df_combine['LC_WINDDIR'].round(2)
    df_combine['LC_WINDSPEED'] = df_combine['LC_WINDSPEED'].round(2)
    df_combine['LC_RAD60'] = df_combine['LC_RAD60'].round(2)
    df_combine['LC_TEMP_QCL3'] = df_combine['LC_TEMP_QCL3'].round(2)



    dashtable = dash_table.DataTable(
        df_combine.to_dict('records'), [{"name": i, "id": i} for i in df_combine.columns],
        style_cell={
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
        'maxWidth': 0,
        },
        tooltip_data=[{
            column: {'value': str(value), 'type': 'markdown'}
            for column, value in row.items()
        } for row in df_combine.to_dict('records')
        ],
        tooltip_duration=None
    )
    return dashtable


