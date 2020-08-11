'''
Quick test of check_flat
'''
from envirodataqc import dataqc
import pandas as pd
import numpy as np
import datetime

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

#Test parameters
testgood = {
    'range':[(0,16),(20,100)],
    'rate':[(-0.27,0.27)],
    'flat':[(0,40)]}
testsusp = {
    'range':[(-1,0),(16,20)],
    'rate':[(0.27,0.34),(-0.34,-0.27)],
    'flat':[(45,55)]}
        
#Load class
qc = dataqc('test',testgood,testsusp)

test = qc.check_flat(data)

