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
from envirodataqc.dataqc import dataqc
from envirodataqc.QCconfig import qcsettings
import numpy as np
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
    qcranges = qcsettings[vartype]
    qc = dataqc(vartype,qcranges['good'],qcranges['suspicious'])

    #Check range
    data['flags_range'] = qc.check_range(data)

    #Check step change
    #data['flags_step'] = qc.step(data.values[])

    #Check flatlining
    #data['flags_flat'] = qc.flat(data.values[])

    return data

def check_gaps(dataindex):
    '''
    Check gaps between data
    Output total of gaps > 1hr
    Input:
    - Pandas datetime index
    Output: total gaps in hours
    **Currently returns np float64
    '''
    #Calculate gaps between points in minutes
    timediff = np.diff(dataindex)
    timediff = timediff.astype(float)/(60*(10**9)) #60 x 10^9 to convert from nanosec

    #Find total of gaps over 1hr
    tot = round(timediff[timediff > 60].sum()/60,1)

    return tot



     

