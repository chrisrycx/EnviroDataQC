'''
Quick tests of rate check
'''
from envirodataqc import dataqc
import pandas as pd
import datetime

testdata = [
    (datetime.datetime(2020,8,7,0,0),1),
    (datetime.datetime(2020,8,7,0,15),1),
    (datetime.datetime(2020,8,7,0,30),1),
    (datetime.datetime(2020,8,7,0,45),6),
    (datetime.datetime(2020,8,7,1,0),1),
    (datetime.datetime(2020,8,7,1,15),2),
    (datetime.datetime(2020,8,7,1,30),-4),
    (datetime.datetime(2020,8,7,2,0),-3),
    (datetime.datetime(2020,8,7,2,30),-6),
    (datetime.datetime(2020,8,7,2,45),14),
    (datetime.datetime(2020,8,7,3,0),8),
    (datetime.datetime(2020,8,7,3,15),6),
    (datetime.datetime(2020,8,7,3,30),6)
    ]

#Create dataframe
dtstamp = []
dvals = []
for val in testdata:
    dtstamp.append(val[0])
    dvals.append(val[1])

data = pd.DataFrame({'testvals':dvals},index=dtstamp)

#Test parameters
testgood = {'range':[(0,16),(20,100)],'rate':[(-0.27,0.27)],'flat':[]}
testsusp = {'range':[(-1,0),(16,20)],'rate':[(0.27,0.34),(-0.34,-0.27)],'flat':[]}
        
#Load class
qc = dataqc('test',testgood,testsusp)

flags = qc.check_rate(data)

