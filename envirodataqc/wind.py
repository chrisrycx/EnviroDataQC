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
    return maxval/dave
    

def winddirchk(datasp,datadir):
    '''
    Evaluate direction data
    Assess flatlining in context of windspeed.
    Flatlining associated with wind > 0 is suspicious.
    '''
    #Set bad speed values to np.nan
    datasp[datasp['flags'] == 2] = np.nan
    
    #Extract flags to avoid data warning
    myflags = datadir.flags.values

    #Calculate slope between input data points
    #Ignore time, every point should be different when wind > 0
    slopes = np.diff(datadir.wind_direction.values)

    #Assess slopes and flag
    counter = 1 #Keep track of index
    for slope in slopes:
        if slope == 0:
            index1 = counter - 1
            index2 = counter
            speed1 = datasp.wind_speed[index1]
            speed2 = datasp.wind_speed[index2]
            spflag1 = datasp.flags[index1]
            spflag2 = datasp.flags[index2]
            #Flag points associated with 0 slope if speed != 0
            if (speed1!=0)and(speed2!=0):
                myflags[index1] = 1
                myflags[index2] = 1
            #Flag points associated with 0 slope if speed is suspect
            if(spflag1==1)and(spflag2==1):
                myflags[index1] = 1
                myflags[index2] = 1
        counter = counter + 1

    #Set flags again
    datadir.flags = myflags

    return datadir
