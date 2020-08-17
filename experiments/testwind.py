'''
Quick script for testing wind algorithms
'''
from envirodataqc import wind
import pandas as pd
import numpy as np
import datetime

#Load data
data = [
    (datetime.datetime(2020,8,7,0,0),0,0),
    (datetime.datetime(2020,8,7,0,30),2,1),
    (datetime.datetime(2020,8,7,0,45),2,1),
    (datetime.datetime(2020,8,7,1,15),2,0),
    (datetime.datetime(2020,8,7,1,30),0,0),
    (datetime.datetime(2020,8,7,1,45),2,-2),
    (datetime.datetime(2020,8,7,2,0),2,0),
    (datetime.datetime(2020,8,7,2,15),3,-2),
    (datetime.datetime(2020,8,7,2,30),2,-2),
    (datetime.datetime(2020,8,7,2,45),5,-2),
    (datetime.datetime(2020,8,7,3,15),0,0),
    (datetime.datetime(2020,8,7,3,30),0,0)
    ]

#Create dataframe
dtstamp = []
spvals = []
dirvals = []
for val in data:
    dtstamp.append(val[0])
    spvals.append(val[1])
    dirvals.append(val[2])

data = pd.DataFrame({'spvals':spvals,'dirvals':dirvals},index=dtstamp)

test = wind.check_winddir(data)