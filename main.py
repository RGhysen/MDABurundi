
import pandas as pd
import plotly.graph_objs as go
import numpy as np
import plotly.express as px



events_hishears = "/Users/leendersmira/Downloads/export_41/csv_results_41_303910_mp-04-his-hears.csv"
events_vrijthof = "/Users/leendersmira/Downloads/export_41/csv_results_41_280324_mp08bis---vrijthof.csv"
events_stadspark = "/Users/leendersmira/Downloads/export_41/csv_results_41_255445_mp-08-kiosk-stadspark.csv"
events_naamsestraat = "/Users/leendersmira/Downloads/export_41/csv_results_41_255444_mp-07-naamsestraat-81.csv"
events_parkstraat = "/Users/leendersmira/Downloads/export_41/csv_results_41_255443_mp-06-parkstraat-2-la-filosovia.csv"
events_kapel = "/Users/leendersmira/Downloads/export_41/csv_results_41_255442_mp-05-calvariekapel-ku-leuven.csv"
events_taste = "/Users/leendersmira/Downloads/export_41/csv_results_41_255441_mp-03-naamsestraat-62-taste.csv"
events_xior = "/Users/leendersmira/Downloads/export_41/csv_results_41_255440_mp-02-naamsestraat-57-xior.csv"
events_maxim = "/Users/leendersmira/Downloads/export_41/csv_results_41_255439_mp-01-naamsestraat-35-maxim.csv"

df1 = pd.read_csv(events_hishears,delimiter=';')
df2 = pd.read_csv(events_vrijthof,delimiter=';')
df3 = pd.read_csv(events_stadspark,delimiter=';')
df4 = pd.read_csv(events_naamsestraat,delimiter=';')
df5 = pd.read_csv(events_parkstraat,delimiter=';')
df6 = pd.read_csv(events_kapel,delimiter=';')
df7 = pd.read_csv(events_taste,delimiter=';')
df8 = pd.read_csv(events_xior,delimiter=';')
df9 = pd.read_csv(events_maxim,delimiter=';')

noiselevels_hishears = "/Users/leendersmira/Downloads/export_42/csv_results_42_303910_mp-04-his-hears.csv"
noiselevels_vrijthof = "/Users/leendersmira/Downloads/export_42/csv_results_42_280324_mp08bis---vrijthof.csv"
noiselevels_stadspark = "/Users/leendersmira/Downloads/export_42/csv_results_42_255445_mp-08-kiosk-stadspark.csv"
noiselevels_naamsestraat = "/Users/leendersmira/Downloads/export_42/csv_results_42_255444_mp-07-naamsestraat-81.csv"
noiselevels_parkstraat = "/Users/leendersmira/Downloads/export_42/csv_results_42_255443_mp-06-parkstraat-2-la-filosovia.csv"
noiselevels_kapel = "/Users/leendersmira/Downloads/export_42/csv_results_42_255442_mp-05-calvariekapel-ku-leuven.csv"
noiselevels_taste = "/Users/leendersmira/Downloads/export_42/csv_results_42_255441_mp-03-naamsestraat-62-taste.csv"
noiselevels_xior = "/Users/leendersmira/Downloads/export_42/csv_results_42_255440_mp-02-naamsestraat-57-xior.csv"
noiselevels_maxim = "/Users/leendersmira/Downloads/export_42/csv_results_42_255439_mp-01-naamsestraat-35-maxim.csv"

df11 = pd.read_csv(noiselevels_hishears, delimiter=';')
df22 = pd.read_csv(noiselevels_vrijthof, delimiter=';')
df33 = pd.read_csv(noiselevels_stadspark, delimiter=';')
df44 = pd.read_csv(noiselevels_naamsestraat, delimiter=';')
df55 = pd.read_csv(noiselevels_parkstraat, delimiter=';')
df66 = pd.read_csv(noiselevels_kapel, delimiter=';')
df77 = pd.read_csv(noiselevels_taste, delimiter=';')
df88 = pd.read_csv(noiselevels_xior, delimiter=';')
df99 = pd.read_csv(noiselevels_maxim, delimiter=';')


#merged per location
merged_hishears = pd.merge(df1, df11, on= 'result_timestamp')
merged_vrijthof = pd.merge(df2, df22, on= 'result_timestamp')
merged_stadspark = pd.merge(df3, df33, on= 'result_timestamp')
merged_naamsestraat = pd.merge(df4, df44, on= 'result_timestamp')
merged_parkstraat = pd.merge(df5, df55, on= 'result_timestamp')
merged_kapel = pd.merge(df6, df66, on= 'result_timestamp')
merged_taste = pd.merge(df7, df77, on= 'result_timestamp')
merged_xior = pd.merge(df8, df88, on= 'result_timestamp')
merged_maxim = pd.merge(df9, df99, on= 'result_timestamp')

#remove missing dates

merged_hishears.shape
merged_hishears.isna().sum()
merged_hishears_clean = merged_hishears.dropna()
merged_hishears_clean.shape
merged_hishears_clean.isna().sum()

merged_vrijthof.shape
merged_vrijthof.isna().sum()
merged_vrijthof_clean = merged_vrijthof.dropna()
merged_vrijthof_clean.shape
merged_vrijthof_clean.isna().sum()

merged_stadspark.shape
merged_stadspark.isna().sum()
merged_stadspark_clean = merged_stadspark.dropna()
merged_stadspark_clean.shape
merged_stadspark_clean.isna().sum()

merged_naamsestraat.shape
merged_naamsestraat.isna().sum()
merged_naamsestraat_clean = merged_naamsestraat.dropna()
merged_naamsestraat_clean.shape
merged_naamsestraat_clean.isna().sum()

merged_parkstraat.shape
merged_parkstraat.isna().sum()
merged_parkstraat_clean = merged_parkstraat.dropna()
merged_parkstraat_clean.shape
merged_parkstraat_clean.isna().sum()

merged_kapel.shape
merged_kapel.isna().sum()
merged_kapel_clean = merged_kapel.dropna()
merged_kapel_clean.shape
merged_kapel_clean.isna().sum()

merged_taste.shape
merged_taste.isna().sum()
merged_taste_clean = merged_taste.dropna()
merged_taste_clean.shape
merged_taste_clean.isna().sum()

merged_xior.shape
merged_xior.isna().sum()
merged_xior_clean = merged_xior.dropna()
merged_xior_clean.shape
merged_xior_clean.isna().sum()

merged_maxim.shape
merged_maxim.isna().sum()
merged_maxim_clean = merged_maxim.dropna()
merged_maxim_clean.shape
merged_maxim_clean.isna().sum()



print(merged_hishears_clean.columns)
print(merged_vrijthof_clean.columns)
print(merged_stadspark_clean.columns)
print(merged_naamsestraat_clean.columns)
print(merged_parkstraat_clean.columns)
print(merged_kapel_clean.columns)
print(merged_taste_clean.columns)
print(merged_xior_clean.columns)
print(merged_maxim_clean.columns)

df = pd.concat([merged_hishears_clean, merged_vrijthof_clean, merged_stadspark_clean, merged_naamsestraat_clean, merged_parkstraat_clean, merged_kapel_clean, merged_taste_clean, merged_xior_clean, merged_maxim_clean]).reset_index(drop=True)

print(df.columns)


threshold = 90 # define a threshold for outlying noise events
df['outlier'] = np.where(df['lcpeak'] > threshold, True, False)

fig = px.scatter(df, x='result_timestamp', y='lcpeak', color='noise_event_laeq_primary_detected_class', hover_name='noise_event_laeq_model_id',
                 hover_data=['lamax', 'laeq', 'lcpeak', 'noise_event_laeq_primary_detected_class', 'noise_event_laeq_primary_detected_certainty'],
                 facet_col='description_x',
                 range_x=[df['result_timestamp'].min(), df['result_timestamp'].max()],
                 range_y=[df['lcpeak'].min(), df['lcpeak'].max()])

fig.update_layout(
    sliders=[dict(
        active=0,
        steps=[dict(label=f'Threshold: {i}', method='update', args=[{'visible': [df['lcpeak'] < i]}]) for i in range(0,101,10)]
    )]
)

fig.update_traces(selected=dict(marker=dict(color='red')), unselected=dict(marker=dict(color='blue')), mode='markers')

bar_data = df.groupby(['description_x', 'noise_event_laeq_primary_detected_class'])['noise_event_laeq_model_id'].count().reset_index()
bar_fig = px.bar(bar_df, x='description_x', y='noise_event_laeq_model_id', color='noise_event_laeq_primary_detected_class')











