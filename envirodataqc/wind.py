'''
Special QC Algorithms for wind
'''
#------------ Wind specific algorithms -----------------#
def windspchk(datasp):
    '''
    Evaluate speeds for internal consistency
    - Calculate daily average and maximum wind speed
    - Assesses ratio of max/ave winds
    Input - Dataframe of wind speed values, flags
    '''
    #Output dataframe
    daydata = pd.DataFrame()
    
    #Resample to daily values and calculate
    daydata['avgwinds'] = datasp.resample('1D').apply(dataAvg) #Returns a series
    daydata['maxwinds'] = datasp.wind_speed.resample('1D').max()

    #Ratio
    daydata['max_avg'] = daydata.avgwinds/daydata.maxwinds

    #Flag data where avg/max ratio < 0.1
    daydata.dropna(inplace=True) #Drop any nans associated with endpoints
    counter = 0
    for day in daydata.index:
        if daydata.max_avg[counter]<0.1:
            #Flag all point associated with a given day
            datasp.loc[day.to_pydatetime():,'flags']=1 #Colon needed for datetime...see help
        counter = counter+1

    return datasp, daydata

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
