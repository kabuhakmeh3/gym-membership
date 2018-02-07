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

# only 2500 allowed per day
num_members = len(addresses)
folds = 6
foldsize = 2400

a = 0
b = 1
while a<=num_members:
    if (a+foldsize) < num_members:
        addresses[a:a+foldsize].to_csv('addresses_' + str(b) + '.csv')
    else:
        addresses[a:].to_csv('addresses_' + str(b) + '.csv')
    a+=foldsize
    b+=1
