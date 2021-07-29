'''
A quick initial test of daily_quality
'''

import envirodataqc
import pandas as pd

#Create a series
dt = pd.DatetimeIndex([
    '2021-07-29 10:00',
    '2021-07-29 12:10',
    '2021-07-29 15:45',
    '2021-07-29 19:30',
])

q = [0,1,1,2]

testseries = pd.Series(q,index=dt)

dayq = envirodataqc.daily_quality(testseries)

print(dayq)
