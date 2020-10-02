from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np
import math
from scipy import stats
from utils import DatetimeToTaxitime, distanceInKmBetweenCoordinates, ComputeQandN,date_transfo


class AirportDataAugmenter(BaseEstimator, TransformerMixin):

    def __init__(self):
        pass
    
    def fit(self, x, y=None):
        return self

    def transform(self, x, y=None):
        x['taxitime'] = x.apply(lambda l: DatetimeToTaxitime(l.AOBT, l.ATOT), axis =1)
        x = x[x["taxitime"] > 0]
        x['runway_stand'] = x['Runway'] + x['Stand']
        N_list, Q_list = ComputeQandN(x)
        x['N'] = N_list        
        x['Q'] = Q_list
        return x

class GeoDataAugmenter(BaseEstimator, TransformerMixin):

    def __init__(self):
        pass
    
    def fit(self, x, y=None):
        return self

    def transform(self, x, y=None):
        # Compute the distance in the aircraft dataframe
        x['distance'] = x.apply(lambda x: distanceInKmBetweenCoordinates(x.Lat_runway, x.Lng_runway, x.Lat_stand, x.Lng_stand), axis =1)
        x['log_distance'] = np.log(x['distance'])
        x = x[['runway_stand', 'distance', 'log_distance']]
        return x

class TrainDataAugmenter(BaseEstimator, TransformerMixin):

    def __init__(self):
        pass
    
    def fit(self, x, y=None):
        return self

    def transform(self, df_train, y=None):
        #We can drop the missing values for all the column where they correspond to delete (because less than 1% of the huge dataset)
        subset_delete = ['Manufacturer', 'Engines', 'Wingspan__ft', 'Length__ft', 'Tail_Height__ft', 
                        'Wheelbase__ft', 'Wake_Category', 'temperature', 'apparentTemperature', 'dewPoint', 'humidity',
                        'windSpeed', 'visibility', 'precipType', 'precipAccumulation', 'ozone']
        df_train = df_train.dropna(subset = subset_delete) 

        #For the remaining NAs value (weather data), 
        #we are going to use the method fillna assuming that the weather does not change as much from one hour to another
        df_train = df_train.fillna(method='ffill')

        #From the EDA and the Outliers search for the variable to predict - there seems to be some outliers 
        # For some outiliers the ATOT is before the AOBT: there is a mistake so we should delete them

        #Delete the taxitime < 0 (we assume that there is a mistake)
        df_train = df_train[df_train["taxitime"] > 0]


        # For the others, we will use Z-score strategy to identify Data point that falls outside of 3 standard deviations 
        z_score = np.abs(stats.zscore(df_train.taxitime))
        threshold = 3
        print(len(np.where(z_score > 3)[0]))

        df_train = df_train[(z_score< 3)]

        df_train = date_transfo(df_train)
        df_train = df_train.drop(['flight_dt', 'aircraft_model', 'ATOT', 'AOBT_hourly', 'Manufacturer'], axis = 1)
        return df_train
