'''
Define dataQC class
- Objects can have multiple ranges describing good, suspicious values
- Where suspicious and good ranges overlap, data will be classified as good
- **rates and flat must be in units of min (for now)
- **each method takes a pandas df with values of interest in col 1 and datetimes col 0
- **each method returns an numpy array of flags for each value
'''

import numpy as np
import pandas as pd

class dataqc:
    '''
    dataqc class:
    Contains QC settings and methods
    '''
    def __init__(self,typename,goodvals,susvals):
        '''
        Create a new data QC object
        Input
        - typename: type of data
        - goodvals: a list with different good range settings
        - susvals: a list with different suspicious range settings 
        '''
        #Load inputs
        self.datatype = typename
        
        self.goodrange = goodvals['range']   #[(x,y),(x2,y2)...]
        self.goodrate = goodvals['rate']   #Units/min
        self.goodflat = goodvals['flat']   #Minutes
        self.susprange = susvals['range']
        self.susprate = susvals['rate']
        self.suspflat = susvals['flat']

    def _check_range_(self,datavals,flags,minval,maxval,rangetype):
        '''
        "Private" method to check values for a given range
        Inputs
            - datavals: numpy array of data values
            - flags: current numpy array of flags
            - max and min values for range
            - rangetype = 'good' or 'suspicious' 
        Returns
            - np array of flags for each value
        '''
        ranges = {'good':0,'suspicious':1}
        flags[(datavals >= minval) & (datavals <= maxval)] = ranges[rangetype] 

        return flags
        
    
    def check_ranges(self,data):
        '''
        Check data against all good and suspicious ranges
        Input
        - data: pandas df with first column values
        Returns
        Numpy array of flags associated data values
        '''

        dvals = data.iloc[:,0].values
        flags = np.ones(len(dvals),dtype=np.int8)*2 #Set all flags to 2 (bad)

        #Check suspicious first so that good range will override
        for valrange in self.susprange:
            flags = self._check_range_(dvals,flags,valrange[0],valrange[1],'suspicious')
        
        for valrange in self.goodrange:
            flags = self._check_range_(dvals,flags,valrange[0],valrange[1],'good')

        return flags

    '''
    def check_rate():
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

    def check_flat():
            pass
    '''



if __name__=='__main__':

    #Testing...
    data = pd.read_csv('../tests/data/basicdata.csv',index_col=0,parse_dates=True)
    data = data[['air_temp']]
    print(data.head())

    #Test data
    testgood = {
    'range':[(0,5),(6,10)],
    'rate':[(0,10)],
    'flat':[(0,15)]
    }

    #Create object
    airTqc = dataqc('air_temperature',testgood,{})

    #Check range
    data['flags'] = airTqc.check_ranges(data)

