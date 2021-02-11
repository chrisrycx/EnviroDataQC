'''
Test dataqc class
- Uses unittest
'''

import unittest
import datetime
import pandas as pd
import numpy as np
import pytz
from envirodataqc.dataqc import dataqc

class Testdataqc(unittest.TestCase):

    def setUp(self):
        '''
        Create a pandas dataframe for tests
        This dataset is somewhat arbitrary but meant to 
        be useful in a variety of ways.
        '''
        testdata = [
            (datetime.datetime(2020,8,7,0,0),1),
            (datetime.datetime(2020,8,7,0,15),1),
            (datetime.datetime(2020,8,7,0,30),1),
            (datetime.datetime(2020,8,7,0,45),6),
            (datetime.datetime(2020,8,7,1,0),1),
            (datetime.datetime(2020,8,7,1,15),2),
            (datetime.datetime(2020,8,7,1,30),-4),
            (datetime.datetime(2020,8,7,2,0),-3),
            (datetime.datetime(2020,8,7,2,30),-6),
            (datetime.datetime(2020,8,7,2,45),14),
            (datetime.datetime(2020,8,7,3,0),8),
            (datetime.datetime(2020,8,7,3,15),6),
            (datetime.datetime(2020,8,7,3,30),6)
            ]
        
        #Create dataframe
        dtstamp = []
        dvals = []
        for val in testdata:
            dtstamp.append(val[0])
            dvals.append(val[1])

        self.data = pd.DataFrame({'testvals':dvals},index=dtstamp)

    def tearDown(self):
        pass

    def test_range_multiple(self):
        '''
        Test check_ranges method with multiple good
        and suspicious ranges of values
        '''
        #Test parameters
        testgood = {'range':[(-2,4),(8,12)],'rate':[],'flat':[]}
        testsusp = {'range':[(-10,-2)],'rate':[],'flat':[]}
        testignore = {'range':[],'rate':[],'flat':[]}
        flags = [0,0,0,2,0,0,1,1,1,2,0,2,2]

        #Load class
        qc = dataqc('test',testgood,testsusp,testignore)

        #Test output
        testflags = qc.check_range(self.data).tolist()
        self.assertEqual(testflags,flags)

    def test_range_empty(self):
        '''
        Test check_ranges with an empty range
        for suspicious values
        '''
        #Test parameters
        testgood = {'range':[],'rate':[],'flat':[]}
        testsusp = {'range':[],'rate':[],'flat':[]}
        testignore = {'range':[],'rate':[],'flat':[]}
        flags = [2,2,2,2,2,2,2,2,2,2,2,2,2]

        #Load class
        qc = dataqc('test',testgood,testsusp,testignore)

        #Test output
        testflags = qc.check_range(self.data).tolist()
        self.assertEqual(testflags,flags)

    def test_range_overlap(self):
        '''
        Test check_ranges where there is an
        overlap in good and suspicious ranges
        '''
        pass

    def test_rate(self):
        '''
        Basic check of the check check_rate method
        '''
        #Test parameters
        testgood = {'range':[(-1,2),(4,6)],'rate':[(-0.27,0.27)],'flat':[]}
        testsusp = {'range':[(-5,-1)],'rate':[(0.27,0.34),(-0.34,-0.27)],'flat':[]}
        testignore = {'range':[],'rate':[],'flat':[]}
        flags = [0,0,1,1,1,1,1,0,1,2,1,0,0]

        #Load class
        qc = dataqc('test',testgood,testsusp,testignore)

        #Test output
        testflags = qc.check_rate(self.data).tolist()
        self.assertEqual(testflags,flags)

    def test_rate_empty(self):
        '''
        Test that all data flagged bad
        when no good, suspicious ranges given.
        '''
        #Test parameters
        testgood = {'range':[],'rate':[],'flat':[]}
        testsusp = {'range':[],'rate':[],'flat':[]}
        testignore = {'range':[],'rate':[],'flat':[]}
        flags = [2,2,2,2,2,2,2,2,2,2,2,2,2]

        #Load class
        qc = dataqc('test',testgood,testsusp,testignore)

        #Test output
        testflags = qc.check_rate(self.data).tolist()
        self.assertEqual(testflags,flags)

    def test_flat(self):
        '''
        Test check_flat algorithm
        '''
        #Create new test data specific to flat check
        testdata = [
            (datetime.datetime(2020,8,7,0,0),0),
            (datetime.datetime(2020,8,7,0,30),2),
            (datetime.datetime(2020,8,7,0,45),2),
            (datetime.datetime(2020,8,7,1,15),2),
            (datetime.datetime(2020,8,7,1,30),0),
            (datetime.datetime(2020,8,7,1,45),2),
            (datetime.datetime(2020,8,7,2,0),2),
            (datetime.datetime(2020,8,7,2,15),0),
            (datetime.datetime(2020,8,7,2,30),2),
            (datetime.datetime(2020,8,7,2,45),2),
            (datetime.datetime(2020,8,7,3,15),2),
            (datetime.datetime(2020,8,7,3,30),2),
            (datetime.datetime(2020,8,7,3,45),4),
            (datetime.datetime(2020,8,7,4,0),4),
            (datetime.datetime(2020,8,7,4,15),4)
            ]

        #Create dataframe
        dtstamp = []
        dvals = []
        for val in testdata:
            dtstamp.append(val[0])
            dvals.append(val[1])

        data = pd.DataFrame({'testvals':dvals},index=dtstamp)

        #Test parameters
        testgood = {
            'range':[(0,16),(20,100)],
            'rate':[(-0.27,0.27)],
            'flat':[(0,15)]}
        testsusp = {
            'range':[(-1,0),(16,20)],
            'rate':[(0.27,0.34),(-0.34,-0.27)],
            'flat':[(15,55)]}
        testignore = {'range':[],'rate':[],'flat':[4]}
        
        #Load class
        qc = dataqc('test',testgood,testsusp,testignore)

        #Check output
        flags = [0,1,1,1,0,0,0,0,2,2,2,2,0,0,0]
        testflags = qc.check_flat(data).tolist()
        self.assertEqual(testflags,flags)

    def test_rate_tz(self):
        '''
        Re-run rate test but make dataframe timezone aware
        '''
        #Test parameters
        testgood = {'range':[(-1,2),(4,6)],'rate':[(-0.27,0.27)],'flat':[]}
        testsusp = {'range':[(-5,-1)],'rate':[(0.27,0.34),(-0.34,-0.27)],'flat':[]}
        flags = [0,0,1,1,1,1,1,0,1,2,1,0,0]

        #Load class
        qc = dataqc('test',testgood,testsusp)

        #Localize dataframe
        tz = pytz.timezone('America/Denver')
        datatz = self.data.tz_localize(tz)

        #Test output
        testflags = qc.check_rate(datatz)
        self.assertEqual(testflags,flags)




if __name__=='__main__':
    unittest.main()