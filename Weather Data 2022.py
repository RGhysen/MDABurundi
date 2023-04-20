#!/usr/bin/env python
# coding: utf-8

# # Weather Data

# # Libraries

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Dataset

# In[14]:


weather_Q1 = pd.read_csv("C:\Alhamd\Belgium Study Material\Modern Data Analytics\Weather Data\dataverse_files (1)\LC_2022Q1.csv")
weather_Q1.head()
weather_Q1.shape


# In[15]:


weather_Q2 = pd.read_csv("C:\Alhamd\Belgium Study Material\Modern Data Analytics\Weather Data\dataverse_files (1)\LC_2022Q2.csv")
weather_Q2.head()
weather_Q2.shape


# In[13]:


weather_Q3 = pd.read_csv("C:\Alhamd\Belgium Study Material\Modern Data Analytics\Weather Data\dataverse_files (1)\LC_2022Q3.csv")
weather_Q3.head()
weather_Q3.shape


# In[29]:


weather_Q4 = pd.read_csv("C:\Alhamd\Belgium Study Material\Modern Data Analytics\Weather Data\dataverse_files (1)\LC_2022Q4.csv")
weather_Q4.head()
weather_Q4.shape
weather_Q4.tail()


# # Joining the Data 

# In[28]:


full_data_weather = pd.concat([weather_Q1, weather_Q2, weather_Q3, weather_Q4],ignore_index=False, keys=['Q1','Q2','Q3', 'Q4'])
full_data_weather_2022 = full_data_weather.drop(full_data_weather.index[-1])
full_data_weather_2022.shape
full_data_weather_2022.head()
full_data_weather_2022.tail()


# In[16]:


1430784 + 1430784 + 1415232 + 1270080


# In[ ]:




