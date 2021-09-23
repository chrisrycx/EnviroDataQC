'''
Initial testing of envirodataqc
Loads some data from csv for test
'''

import envirodataqc as envqc
import pandas as pd #Initially used for importing csv data

#Load data from CSV
data = pd.read_csv('tests/data/data.csv',index_col=0,parse_dates=True)

print(data.head())

#Extract air temperature
dataT = data['temperature_C']

print(dataT.head())

#Run checks
dataTqc = envqc.check_vals(dataT,'air_temperature')

print(dataTqc.head())