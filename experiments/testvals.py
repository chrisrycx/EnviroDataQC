'''
Quick test of check vals
'''
import pandas as pd
import envirodataqc

dpath = '../tests/data/tphdata.csv'
data = pd.read_csv(dpath,index_col=0,parse_dates=True)

#Run check_vals
testdata = envirodataqc.check_vals(
    data.loc[:,['airT']],
    'air_temperature'
    )