import numpy as np
import math
from datetime import timedelta

# Create the functions that compute distance between runways & stands in kilometers
def degreesToRadians(degrees):
    return degrees * np.pi / 180

def distanceInKmBetweenCoordinates(lat1, lon1, lat2, lon2):
    earthRadiusKm = 6371
    dLat = degreesToRadians(lat2-lat1)
    dLon = degreesToRadians(lon2-lon1)

    lat1 = degreesToRadians(lat1)
    lat2 = degreesToRadians(lat2)

    calculation = np.sin(dLat/2) * np.sin(dLat/2) + np.sin(dLon/2) * np.sin(dLon/2) * np.cos(lat1) * np.cos(lat2) 
    distance = 2 * math.atan2(np.sqrt(calculation), np.sqrt(1-calculation))
    return earthRadiusKm * distance

def DatetimeToTaxitime(datetime1, datetime2):
        difference = datetime2 - datetime1
        taxitime = difference.value / 6e10
        return taxitime

def hour_rounder(t):
        # Rounds to nearest hour by adding a timedelta hour if minute >= 30
        return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
                +timedelta(hours=t.minute//30))