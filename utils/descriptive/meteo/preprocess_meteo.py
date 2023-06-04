import pandas as pd
from utils import paths

def gather_data(folder_path):
    meteor_data_path = [folder_path + '/LC_2022Q1_chunk_1.csv',
                        folder_path + '/LC_2022Q2_chunk_1.csv',
                        folder_path + '/LC_2022Q3_chunk_1.csv',
                        folder_path + '/LC_2022Q4_chunk_1.csv',
                        folder_path + '/LC_2022Q1_chunk_2.csv',
                        folder_path + '/LC_2022Q2_chunk_2.csv',
                        folder_path + '/LC_2022Q3_chunk_2.csv',
                        folder_path + '/LC_2022Q4_chunk_2.csv']
    df1_1 = pd.read_csv(meteor_data_path[0])
    df1_2 = pd.read_csv(meteor_data_path[4])
    df2_1 = pd.read_csv(meteor_data_path[1])
    df2_2 = pd.read_csv(meteor_data_path[5])
    df3_1 = pd.read_csv(meteor_data_path[2])
    df3_2 = pd.read_csv(meteor_data_path[6])
    df4_1 = pd.read_csv(meteor_data_path[3])
    df4_2 = pd.read_csv(meteor_data_path[7])
    df = pd.concat([df1_1, df1_2, df2_1, df2_2, df3_1, df3_2, df4_1, df4_2],ignore_index=True)
    return df
    
def create_season(df):
    df['season']= 0
    df.loc[(df['Month'] > 2) & (df['Month'] < 6), 'season'] = 1
    df.loc[(df['Month'] > 5) & (df['Month'] < 9), 'season'] = 2
    df.loc[(df['Month'] > 8) & (df['Month'] < 12), 'season'] = 3
    return df

def initial_preprocessing_meteor(folder_path):
    df = gather_data(folder_path)
    df_drop = df.drop(['ID', 'LC_n', 'LC_TEMP_QCL0', 'LC_TEMP_QCL1','LC_TEMP_QCL2'], axis=1)
    df_drop_nan = df_drop.dropna()
    df_final_no_season = df_drop_nan.groupby(['DATEUTC'], as_index = False).mean()
    df_final = create_season(df_final_no_season)
    
    df_groupby_hour = df_final.groupby(['Year', 'Month', 'Day', 'Hour'], as_index = False).mean()
    df_groupby_hour.drop(['Minute'], inplace = True, axis = 1)
    
    df_groupby_day = df_final.groupby(['Year', 'Month', 'Day'], as_index = False).mean()
    df_groupby_day.drop(['Hour', 'Minute'], inplace = True, axis = 1)
    
    return df_final, df_groupby_hour, df_groupby_day

df = [df_final, df_groupby_hour, df_groupby_day] = initial_preprocessing_meteor(paths.path_meteo)
