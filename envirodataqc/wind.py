'''
Special QC Algorithms for wind
'''
import numpy as np
import pandas as pd

def check_windspeed(data):
    '''
    Evaluate wind speeds for internal consistency
    - Calculate ratio of max/ave values (typically for 24hr period)
    Input
     - Dataframe of wind speed values

    Algorithm:
    Calculate average (numerical integral) of values
    Calculate the max value
    Return ratio of values
    '''
    #Calculate the max
    maxval = data.iloc[:,0].max()

    #Calculate the average using numerical integration
    dvals = data.iloc[:,0].to_numpy()
    timediff = np.diff(data.index)
    timediff = timediff.astype(float)/(60*(10**9)) #60 x 10^9 to convert from nanosec
    dmins = np.cumsum(timediff) #Minutes past starting time
    dmins = np.insert(dmins,0,0)
    dataintegral = np.trapz(dvals,dmins)
    dave = dataintegral/dmins[-1] #Last value should be total time period
    
    #Return the ratio
    return dave/maxval
    

def check_winddir(data):
    '''
    Evaluate direction data
    Assess flatlining in context of windspeed.
    Flatlining associated with wind > 0 is suspicious.
    Input
    - dataframe: index (datetime),speedvals,dirvals
    Return
    - list of flags associated with each value (0 good, 1 suspicious)
    '''
    spvals = data.iloc[:,0].to_numpy()
    dirvals = data.iloc[:,1].to_numpy()

    #Check flatlining against wind speed
    slopeflags = []
    for n in range(len(spvals)-1):
        #Flag where direction change is zero but wind > 0
        dirdiff = dirvals[n+1] - dirvals[n]
        spsum = spvals[n+1] + spvals[n]
        if (dirdiff == 0) and (spsum > 0):
            slopeflags.append(1)
        else:
            slopeflags.append(0)

    #Finally: assign point flags based on slope flags
    flags = []
    for n in range(len(slopeflags)-1):
        flags.append(max(slopeflags[n],slopeflags[n+1]))
    #Endpoints
    flags.insert(0,slopeflags[0])
    flags.append(slopeflags[-1])

    return flags

    