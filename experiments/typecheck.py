'''
Checking output type
'''

import pandas as pd
from envirodataqc import check_gaps

dpath = '../tests/data/tphdata.csv'
data = pd.read_csv(dpath,index_col=0,parse_dates=True)

tot = check_gaps(data.index)