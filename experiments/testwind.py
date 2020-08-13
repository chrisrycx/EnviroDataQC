'''
Quick script for testing wind algorithms
'''
from envirodataqc import wind
import pandas as pd
import numpy as np
import datetime

#Load data
testdata = [
    (datetime.datetime(2020,8,7,0,0),0),
    (datetime.datetime(2020,8,7,0,30),2),
    (datetime.datetime(2020,8,7,0,45),2),
    (datetime.datetime(2020,8,7,1,15),2),
    (datetime.datetime(2020,8,7,1,30),0),
    (datetime.datetime(2020,8,7,1,45),2),
    (datetime.datetime(2020,8,7,2,0),2),
    (datetime.datetime(2020,8,7,2,15),0),
    (datetime.datetime(2020,8,7,2,30),2),
    (datetime.datetime(2020,8,7,2,45),2),
    (datetime.datetime(2020,8,7,3,15),2),
    (datetime.datetime(2020,8,7,3,30),2)
    ]

#Create dataframe
dtstamp = []
dvals = []
for val in testdata:
    dtstamp.append(val[0])
    dvals.append(val[1])

data = pd.DataFrame({'testvals':dvals},index=dtstamp)


test = wind.check_windspeed(data)