'''
Initial testing of envirodataqc
Loads some data from csv for test
'''

import envirodataqc as envqc
import pandas as pd #Initially used for importing csv data

#Load data from CSV
data = pd.read_csv('basicdata.csv',index_col=0,parse_dates=True)

#print(data.head())

#Extract air temperature
dataT = data[['air_temp']]
dataT['flags'] = 0

print(dataT.head())

#Run checks
dataTqc = envqc.checkall(dataT)