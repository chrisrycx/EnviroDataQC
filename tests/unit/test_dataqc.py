'''
Test dataqc class
- Uses unittest
'''

import unittest
import pandas as pd
import numpy as np
from envirodataqc.dataqc import dataqc

class TestDataqc(unittest.TestCase):

    def setUp(self):
        '''
        Create a pandas dataframe for tests
        '''
        datavals = [0,-1,15,300.4,16,17.33,-40.5,20,21.33,0]
        self.data = pd.DataFrame({'data':datavals})

    def tearDown(self):
        pass

    def test_ranges_multiple(self):
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

    def test_ranges_empty(self):
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