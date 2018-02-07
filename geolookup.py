import time
import googlemaps as gmp
import numpy as np
import pandas as pd

### Edit Here ###

file_to_read = 'addresses_01.csv'
file_to_write = 'geo_addresses_01.csv'

# Progress
# [x] addresses_01.csv 
# [x] addresses_02.csv
# [x] addresses_03.csv
# [x] addresses_04.csv
# [x] addresses_05.csv
# [x] addresses_06.csv

### ### ### ### #

def get_apikey(apifile):
    with open(apifile,'r') as file:
        apikey = file.read().rstrip('\n')
        return apikey

geoapikey=get_apikey('gmapsapikey.txt')
geolookup=gmp.Client(key=geoapikey)

def get_lat_lng(address, delay=0.05):
    # 2500 free requests/day
    # 50 requests/second maxiumum
    try:
        geoad = geolookup.geocode(address)
        lat = geoad[0]['geometry']['location']['lat']
        lng = geoad[0]['geometry']['location']['lng']
    except:
        lat = np.NaN
        lng = np.NaN
    print(lat,lng)
    time.sleep(delay)
    return lat, lng

addresses = pd.read_csv(file_to_read)
addresses['GeoLoc'] = addresses['Lookup'].apply(get_lat_lng)
addresses.to_csv(file_to_write)
