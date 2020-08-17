'''
Unit tests for wind.py
'''

import unittest
import datetime
import pandas as pd
import numpy as np
from envirodataqc import wind

class test_wind(unittest.TestCase):

    def setUp(self):
        '''
        Create a pandas dataframe for tests
        This dataset is somewhat arbitrary but meant to 
        be useful in a variety of ways.
        '''
        data = [
            (datetime.datetime(2020,8,7,0,0),0,0),
            (datetime.datetime(2020,8,7,0,30),2,1),
            (datetime.datetime(2020,8,7,0,45),2,1),
            (datetime.datetime(2020,8,7,1,15),2,0),
            (datetime.datetime(2020,8,7,1,30),0,0),
            (datetime.datetime(2020,8,7,1,45),2,-2),
            (datetime.datetime(2020,8,7,2,0),2,0),
            (datetime.datetime(2020,8,7,2,15),3,-2),
            (datetime.datetime(2020,8,7,2,30),2,-2),
            (datetime.datetime(2020,8,7,2,45),5,-2),
            (datetime.datetime(2020,8,7,3,15),0,0),
            (datetime.datetime(2020,8,7,3,30),0,0)
            ]

        #Create dataframe
        dtstamp = []
        spvals = []
        dirvals = []
        for val in data:
            dtstamp.append(val[0])
            spvals.append(val[1])
            dirvals.append(val[2])

        self.data = pd.DataFrame({'spvals':spvals,'dirvals':dirvals},index=dtstamp)

    def tearDown(self):
        pass

    def test_windspeed(self):
        testratio = wind.check_windspeed(self.data[['spvals']])
        trueratio = 2.745

        self.assertAlmostEqual(testratio,trueratio,3)

    def test_winddir(self):
        trueflags = [0,1,1,1,1,0,0,1,1,1,0,0]
        testflags = wind.check_winddir(self.data)

        self.assertEqual(testflags,trueflags)



if __name__=='__main__':
    unittest.main()
