from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np
import math
from utils import DatetimeToTaxitime, distanceInKmBetweenCoordinates


class AirportDataAugmenter(BaseEstimator, TransformerMixin):

    def __init__(self):
        pass
    
    def fit(self, x, y=None):
        return self

    def transform(self, x, y=None):
        x['taxitime'] = x.apply(lambda l: DatetimeToTaxitime(l.AOBT, l.ATOT), axis =1)
        x = x[x["taxitime"] > 0]
        x['runway_stand'] = x['Runway'] + x['Stand']
        return x

class GeoDataAugmenter(BaseEstimator, TransformerMixin):

    def __init__(self):
        pass
    
    def fit(self, x, y=None):
        return self

    def transform(self, x, y=None):
        # Compute the distance in the aircraft dataframe
        x['distance'] = x.apply(lambda x: distanceInKmBetweenCoordinates(x.Lat_runway, x.Lng_runway, x.Lat_stand, x.Lng_stand), axis =1)
        return x