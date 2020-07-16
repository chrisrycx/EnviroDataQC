'''
EnviroData QC - 
Quality control and assurance of
environmental data.

API
- QC settings defined in QCconfig.py
- Check Values
    Input
    -- pandas dataframe with datetimes and values
    -- variable type matching a variable listed in QC file
    Output
    -- Dataframe with original data plus flags
- Check Gaps
    Input
    -- pandas dataframe with datetimes and values
    -- ??

'''
from dataqc import dataqc
import QCconfig
import pandas as pd

#Check Values function
def check_vals(data,vartype):
    '''
    Evaluate range, step change, and flatlining
    of input data.
    Inputs
     - Pandas dataframe with datetimeindex and one column of values
     - variable type matching one of the variables in configuration file
    Output - Pandas dataframe of original input plus flag columns 

    check_vals Algorithm
    - Load setting for input variable type
    - Check for range
    - Check for step change
    - Check for flatlining
    '''
    
    #Load QC Settings for this variable type
    qcranges = QCconfig.qcsettings[vartype]
    qc = dataqc(vartype,qcranges['good'],qcranges['suspicious'])

    #Check range
    data['flags_range'] = qc.check_ranges(data)

    #Check step change
    #data['flags_step'] = qc.step(data.values[])

    #Check flatlining
    #data['flags_flat'] = qc.flat(data.values[])

    return data

#Test with some data
if __name__ == "__main__":

    #Read in some test data
    dpath = '../tests/data/basicdata.csv'
    data = pd.read_csv(dpath,index_col=0,parse_dates=True)

    #Note that .loc is important here!
    dataflag = check_vals(data.loc[:,['air_temp']],'air_temperature')

    print(dataflag.head())
     

