'''
Testing some ideas using pandas
'''
import pandas as pd
import numpy as np

#Test range
airTgood = [(12,15),(16,20)]
airTsusp = [(11,12)]

def checkrange(data):
    '''
    Input data get back a column of flags
    Append flags on to dataframe
    Input dataframe 'vals'

    **Maybe just push a numpy array
    '''
    #Create column for flag values, initialize as all bad
    data['flags'] = 2

    #Check suspicious range first
    for susprange in airTsusp:
        minval = susprange[0]
        maxval = susprange[1]
        data.loc[(data['vals']>minval) | (data['vals']<maxval),'flags'] = 1

    #Check good range second... this will override if there was overlap
    for goodrange in airTgood:
        minval = goodrange[0]
        maxval = goodrange[1]
        data.loc[(data['vals']>minval) | (data['vals']<maxval),'flags'] = 0

    return data
    


data = pd.read_csv('../tests/data/testdata1.csv',index_col=0,parse_dates=True)

#print(data.head())

#Extract air temperature
dataT = data[['air_temp']]