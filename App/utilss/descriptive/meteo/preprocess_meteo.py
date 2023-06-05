import pandas as pd
from utilss import paths

def gather_data(folder_path):
    meteor_data_path = [folder_path + '/LC_2022Q1_chunk_1.csv',
                        folder_path + '/LC_2022Q2_chunk_1.csv',
                        folder_path + '/LC_2022Q3_chunk_1.csv',
                        folder_path + '/LC_2022Q4_chunk_1.csv',
                        folder_path + '/LC_2022Q1_chunk_2.csv',
                        folder_path + '/LC_2022Q2_chunk_2.csv',
                        folder_path + '/LC_2022Q3_chunk_2.csv',
                        folder_path + '/LC_2022Q4_chunk_2.csv',
                        folder_path + '/LC_2022Q1_chunk_3.csv',
                        folder_path + '/LC_2022Q2_chunk_3.csv',
                        folder_path + '/LC_2022Q3_chunk_3.csv',
                        folder_path + '/LC_2022Q4_chunk_3.csv',
                        folder_path + '/LC_2022Q1_chunk_4.csv',
                        folder_path + '/LC_2022Q2_chunk_4.csv',
                        folder_path + '/LC_2022Q3_chunk_4.csv',
                        folder_path + '/LC_2022Q4_chunk_4.csv',
                        folder_path + '/LC_2022Q1_chunk_5.csv',
                        folder_path + '/LC_2022Q2_chunk_5.csv',
                        folder_path + '/LC_2022Q3_chunk_5.csv',
                        folder_path + '/LC_2022Q4_chunk_5.csv',
                        folder_path + '/LC_2022Q1_chunk_6.csv',
                        folder_path + '/LC_2022Q2_chunk_6.csv',
                        folder_path + '/LC_2022Q3_chunk_6.csv',
                        folder_path + '/LC_2022Q4_chunk_6.csv',
                        folder_path + '/LC_2022Q1_chunk_7.csv',
                        folder_path + '/LC_2022Q2_chunk_7.csv',
                        folder_path + '/LC_2022Q3_chunk_7.csv',
                        folder_path + '/LC_2022Q4_chunk_7.csv',
                        folder_path + '/LC_2022Q1_chunk_8.csv',
                        folder_path + '/LC_2022Q2_chunk_8.csv',
                        folder_path + '/LC_2022Q3_chunk_8.csv',
                        folder_path + '/LC_2022Q4_chunk_8.csv']

    df1_1 = pd.read_csv(meteor_data_path[0])
    df1_2 = pd.read_csv(meteor_data_path[1])
    df1_3 = pd.read_csv(meteor_data_path[2])
    df1_4 = pd.read_csv(meteor_data_path[3])
    df1_5 = pd.read_csv(meteor_data_path[4])
    df1_6 = pd.read_csv(meteor_data_path[5])
    df1_7 = pd.read_csv(meteor_data_path[6])
    df1_8 = pd.read_csv(meteor_data_path[7])

    df1 = pd.concat([df1_1, df1_2, df1_3, df1_4, df1_5, df1_6, df1_7, df1_8])

    df2_1 = pd.read_csv(meteor_data_path[8])
    df2_2 = pd.read_csv(meteor_data_path[9])
    df2_3 = pd.read_csv(meteor_data_path[10])
    df2_4 = pd.read_csv(meteor_data_path[11])
    df2_5 = pd.read_csv(meteor_data_path[12])
    df2_6 = pd.read_csv(meteor_data_path[13])
    df2_7 = pd.read_csv(meteor_data_path[14])
    df2_8 = pd.read_csv(meteor_data_path[15])

    df2 = pd.concat([df2_1, df2_2, df2_3, df2_4, df2_5, df2_6, df2_7, df2_8])               

    df3_1 = pd.read_csv(meteor_data_path[16])
    df3_2 = pd.read_csv(meteor_data_path[17])
    df3_3 = pd.read_csv(meteor_data_path[18])
    df3_4 = pd.read_csv(meteor_data_path[19])
    df3_5 = pd.read_csv(meteor_data_path[20])
    df3_6 = pd.read_csv(meteor_data_path[21])
    df3_7 = pd.read_csv(meteor_data_path[22])
    df3_8 = pd.read_csv(meteor_data_path[23])

    df3 = pd.concat([df3_1, df3_2, df3_3, df3_4, df3_5, df3_6, df3_7, df3_8])


    df4_1 = pd.read_csv(meteor_data_path[24])
    df4_2 = pd.read_csv(meteor_data_path[25])
    df4_3 = pd.read_csv(meteor_data_path[26])
    df4_4 = pd.read_csv(meteor_data_path[27])
    df4_5 = pd.read_csv(meteor_data_path[28])
    df4_6 = pd.read_csv(meteor_data_path[29])
    df4_7 = pd.read_csv(meteor_data_path[30])
    df4_8 = pd.read_csv(meteor_data_path[31])

    df4 = pd.concat([df4_1, df4_2, df4_3, df4_4, df4_5, df4_6, df4_7, df4_8])

    df = pd.concat([df1, df2, df3, df4],ignore_index=True)
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
