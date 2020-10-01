#Loading the necessary packages
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from preprocessing import AirportPreprocessingPipeline, GeoPreprocessingPipeline, WeatherPreprocessingPipeline

# Loading the datasets
df_airport_initial = pd.read_csv("Raw_data/training_set_airport_data.csv")
df_geographic_initial = pd.read_csv("Prepared_data/new_geographic_data.csv", sep = ";")
df_weather_initial = pd.read_csv("Raw_data/Weather_data/weather_data_train_set.csv")
df_aircraft = pd.read_csv("Raw_data/AC_characteristics/ACchar.csv", sep = ";")

app = AirportPreprocessingPipeline()
gpp = GeoPreprocessingPipeline()
wpp = WeatherPreprocessingPipeline()

# Preprocessing
print('Start transforms')
df_airport = app.fit(df_airport_initial)
df_airport = app.transform(df_airport_initial)
df_geographic = gpp.fit(df_geographic_initial)
df_geographic = gpp.transform(df_geographic_initial)
df_weather = wpp.fit(df_weather_initial)
df_weather = wpp.transform(df_weather_initial)
print('End transforms')

# Combining datasets

## Let's combine our training set with the geographic dataset (the key is the runway & the stand)
df_train = pd.merge(df_airport, df_geographic ,on='runway_stand',how='left')

## Let's combine our training set with the weather dataset (the key is the datetime)
df_train = pd.merge(df_train, df_weather ,on = 'AOBT_hourly', how='left')
df_train = pd.merge(df_train, df_aircraft ,on = 'aircraft_model', how='left')

# TAKES A LOT OF TIME
# df_train.to_csv("Preprocessed_airport_data.csv", index= False)

print(f"Training dataset shape is {df_train.shape}")

print('\n')
print(df_train.head())

# Splitting into training and validation datasets
X_train, X_test, y_train, y_test = train_test_split(df_train[df_train.columns - ["taxitime"]], df_train["taxitime"], test_size=0.33, random_state=42)

# Models definition

## Linear regression baseline
reg = LinearRegression().fit(X_train, y_train)
print(reg.score(X_train, y_train))
print(reg.coef_)
print(reg.intercept_)
print(reg.predict(X_test))

