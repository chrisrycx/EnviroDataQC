'''
Test pandas bug
in v1.3.2 this fails in 1.2.5 this works

'''

import pandas as pd
import datetime
import pytz

tmzn = pytz.timezone('America/Denver')

i = pd.DatetimeIndex([
    datetime.datetime(2021,8,20,12,30),
    datetime.datetime(2021,8,20,12,40),
    datetime.datetime(2021,8,20,12,50),
    datetime.datetime(2021,8,21,12,30),
    datetime.datetime(2021,8,21,12,40),
    datetime.datetime(2021,8,21,12,50)
    ],
    tz=tmzn
)

t = pd.Series([0,2,3,0,5,6],index=i)

print(t[t>3].size)

print(t.resample('1D').agg(lambda x: x[x==0].size/x.size))