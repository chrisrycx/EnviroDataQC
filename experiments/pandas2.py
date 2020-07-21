'''
Just a script for testing pandas concepts
'''
import pandas as pd 

data = pd.read_csv('../tests/data/tphdata.csv',index_col=0,parse_dates=True)