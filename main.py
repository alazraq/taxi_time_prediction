# 1. Loading the necessary packages
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from preprocessing import AirportPreprocessingPipeline, GeoPreprocessingPipeline, WeatherPreprocessingPipeline, TrainPreprocessingPipeline
from scipy import stats

print("1. Imports done")

# 2. Loading the datasets and creating pipelines
df_airport_initial = pd.read_csv("Raw_data/training_set_airport_data.csv")
df_geographic_initial = pd.read_csv("Prepared_data/new_geographic_data.csv", sep = ";")
df_weather_initial = pd.read_csv("Raw_data/Weather_data/weather_data_train_set.csv")
df_aircraft = pd.read_csv("Prepared_data/ACchar.csv", sep = ";")

app = AirportPreprocessingPipeline()
gpp = GeoPreprocessingPipeline()
wpp = WeatherPreprocessingPipeline()
tpp = TrainPreprocessingPipeline()
print("2. Loading datasets done")

# 3. Preprocessing

df_airport = app.fit(df_airport_initial)
df_airport = app.transform(df_airport_initial)
print("- Airport data preprocessed")
df_geographic = gpp.fit(df_geographic_initial)
df_geographic = gpp.transform(df_geographic_initial)
print("- Geo data preprocessed")
df_weather = wpp.fit(df_weather_initial)
df_weather = wpp.transform(df_weather_initial)
print("- Weather data preprocessed")
print('3. Preprocessing done')

# 4.Combining datasets

## Let's combine our training set with the geographic dataset (the key is the runway & the stand)
df_train_initial = pd.merge(df_airport, df_geographic ,on='runway_stand',how='left')

## Let's combine our training set with the weather dataset (the key is the datetime)
df_train_initial = pd.merge(df_train_initial, df_weather ,on = 'AOBT_hourly', how='left')
df_train_initial = pd.merge(df_train_initial, df_aircraft ,on = 'aircraft_model', how='left')

# TAKES A LOT OF TIME
# df_train_initial.to_csv("Preprocessed_airport_data.csv", index= False)

print('4. Combining datasets done')

# 5. Cleaning the dataset
df_train = tpp.fit(df_train_initial)
df_train = tpp.transform(df_train_initial)

print('5. Cleaning the dataset done\n')

print(f"Training dataset shape is {df_train.shape}")
print('\n')
print(df_train.head())

# Save the dataset TAKES A LOT OF TIME
# df_train_initial.to_csv("Preprocessed_airport_data.csv", index= False)

# 6. Splitting into training and validation datasets
#Split the dataset into X & y (where y is the variable to predict)
df_y = df_train['taxitime']
df_X = df_train.drop(['taxitime'], axis=1)

# Split test & train randomly
X_train, X_test, y_train, y_test = train_test_split(
     df_X, df_y, test_size=0.2, random_state=42)

# 7. Models definition
'''
# Linear regression baseline
reg = LinearRegression().fit(X_train, y_train)
print(reg.score(X_train, y_train))
print(reg.coef_)
print(reg.intercept_)
print(reg.predict(X_test))
'''