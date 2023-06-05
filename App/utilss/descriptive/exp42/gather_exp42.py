from utilss import paths
import pandas as pd 

path1 = paths.path_exp42_processed + '/aggregated_data_laeq_df.csv'
path2 = paths.path_exp42_processed + '/aggregated_data_lamax_df.csv'
path3 = paths.path_exp42_processed + '/aggregated_data_lceq_df.csv'
path4 = paths.path_exp42_processed + '/aggregated_data_lcpeak_df.csv'

df1 = pd.read_csv(path1)
df2 = pd.read_csv(path2)
df3 = pd.read_csv(path3)
df4 = pd.read_csv(path4)
