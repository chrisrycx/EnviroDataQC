'''
Test dataqc class
- Uses unittest
'''

import unittest
import datetime
import pandas as pd
import numpy as np
from envirodataqc.dataqc import dataqc

class TestDataqc(unittest.TestCase):

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
            (datetime.datetime(2020,8,7,2,45),8),
            (datetime.datetime(2020,8,7,3,0),8),
            (datetime.datetime(2020,8,7,3,15),6),
            (datetime.datetime(2020,8,7,3,30),6)        ]
        ]

        
        self.data = pd.DataFrame({'data':datavals})

    def tearDown(self):
        pass

    def test_range_multiple(self):
        '''
        Test check_ranges method with multiple good
        and suspicious ranges of values
        '''
        #Test parameters
        testgood = {'range':[(0,16),(20,100)],'rate':[],'flat':[]}
        testsusp = {'range':[(-1,0),(16,20)],'rate':[],'flat':[]}
        flags = [0,1,0,2,0,1,2,0,0,0]

        #Load class
        qc = dataqc('test',testgood,testsusp)

        #Test output
        testflags = qc.check_ranges(self.data).tolist()
        self.assertEqual(testflags,flags)

    def test_range_empty(self):
        '''
        Test check_ranges with an empty range
        for suspicious values
        '''
        pass

    def test_ranges_overlap(self):
        '''
        Test check_ranges where there is an
        overlap in good and suspicious ranges
        '''
        pass


if __name__=='__main__':
    unittest.main()