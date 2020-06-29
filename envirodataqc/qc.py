'''
Defines a class to hold QC settings and methods
'''

class dataqc:
    '''
    Defines all QC settings and methods
    '''
    def __init__(self,vartype):
        '''
        Create a new data QC object
        Input
        --
        '''
        #Check suspicious range first
    for susprange in airTsusp:
        minval = qc.susprange[0]
        maxval = qc.susprange[1]
        data.loc[(data['vals']>minval) | (data['vals']<maxval),'flags'] = 1

    #Check good range second... this will override if there was overlap
    for goodrange in airTgood:
        minval = qc.goodrange[0]
        maxval = qc.goodrange[1]
        data.loc[(data['vals']>minval) | (data['vals']<maxval),'flags'] = 0
    

    

    #Calculate absolute slope between input data points
    vdiff = np.absolute(np.diff(data[mtype].values))
    #Calculate time differences in minutes
    timediff = np.diff(data.index)
    timediff = timediff.astype(float)/(60*(10**9)) #60 x 10^9 to convert from nanosec
    dataslopes = vdiff/timediff

    #Flag points based on jumps. Also identify flatlined sections
    oldslopeflat = False #Keeps track of start of flatlined data
    sindex = 0
    counter = 0 #Keep track of index
    for slope in dataslopes:
        
        if (slope!=0) and (oldslopeflat):
            #Signifies the end of a section of flat data
            eindex = counter
            #Check amount of time flat
            flattime = (data.index[eindex] - data.index[sindex]).seconds/60 #Time in minutes
            #If exceeds maximum time flag all points
            if flattime > maxflat[mtype]:
                data.iloc[sindex:eindex+1,1]=1
            oldslopeflat = False

        if (slope==0) and (not oldslopeflat):
            #Signifies the start of a flat section
            sindex = counter
            oldslopeflat = True
        
        #Slope exceeds limits
        if abs(slope) > maxjump[mtype]:
            #Flag points adjacent as suspicious
            data.iloc[counter,1] = 1
            data.iloc[counter+1,1] = 1

        counter = counter+1