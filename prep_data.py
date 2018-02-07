import pandas as pd
import math
import datetime as dt

# define a few functions
def get_apikey(apifile):
    with open(apifile,'r') as file:
        apikey = file.read().rstrip('\n')
        return apikey

# this may not be necessary later
def get_duration(join, cancel):
    join_date = dt.datetime.strptime(join, '%Y-%m-%d').date()
    cancel_date = dt.datetime.strptime(cancel, '%Y-%m-%d').date()
    elapsed = cancel_date - join_date
    days_passed = elapsed.days
    return days_passed

data = pd.read_excel('Membership_data.xls')
apikey = get_apikey('gmapsapikey.txt')

# prepare data for a few processing steps
# 1. Create a list of names to lookup missing gender data
# 2. Create full addresses to lookup geographical coordinates to plot locations

# NAMES
# Create a list of names to lookup
names = data['First Name'].dropna()
name_list = names.apply(lambda x: x.upper().rstrip()).unique()

# only 1000 lookups permitted per day, so split the list
num_names = len(names)
nfolds = math.ceil(len(names)/1000)
fold_size = 950

i = 0
j = 1
while i<=num_names:
    if (i+fold_size) < num_names:
        names[i:i+fold_size].to_csv('names_' + str(j) + '.csv')
    else:
        names[i:].to_csv('names_' + str(j) + '.csv')
    i+=fold_size
    j+=1

# LOCATIONS
addresses = data[['Address1','City','State','Zip']].dropna()
addresses['City'] = addresses['City'].apply(lambda x: x.lower())
addresses['Lookup'] = addresses['Address1'] + addresses['Zip'] 

addresses_01 = addresses[0:2400]
addresses_02 = addresses[2400:4800]
addresses_03 = addresses[4800:7200]
addresses_04 = addresses[7200:9600]
addresses_05 = addresses[9600:12000]
addresses_06 = addresses[12000:]

addresses_01.to_csv('addresses_01.csv')  
addresses_02.to_csv('addresses_02.csv') 
addresses_03.to_csv('addresses_03.csv')
addresses_04.to_csv('addresses_04.csv')
addresses_05.to_csv('addresses_05.csv')
addresses_06.to_csv('addresses_06.csv')
