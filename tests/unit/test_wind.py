'''
Unit tests for wind.py
'''

import unittest
import datetime
import pytz
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
        dts = [
            datetime.datetime(2021,3,18,0,0),
            datetime.datetime(2021,3,18,0,10),
            datetime.datetime(2021,3,18,0,20),
            datetime.datetime(2021,3,18,0,30),
            datetime.datetime(2021,3,18,0,40),
            datetime.datetime(2021,3,18,0,50),
            datetime.datetime(2021,3,18,1,0),
            datetime.datetime(2021,3,18,1,10)
        ]

        #Test wind speeds and directions
        #Consists of: 
        # One section of zero winds associated with changing
        # One section of zero winds with unchanging direction
        # One section of non-zero winds with flatlined direction
        spvals = [1,0,0,1,2,3,0,0]
        dirvals = [30,55,65,60,60,65,22,22]

        self.data = pd.DataFrame({'spvals':spvals,'dirvals':dirvals},index=dts)

    def tearDown(self):
        pass

    def test_windsp_ratio(self):
        testratio = wind.check_windsp_ratio(self.data)
        trueratio = 0.31

        self.assertAlmostEqual(testratio,trueratio,3)

    def test_windsp_withdir(self):
        trueflags = [0,1,1,0,0,0,0,0]
        testflags = wind.check_windsp_withdir(
            self.data['spvals'].to_numpy(),
            self.data['dirvals'].to_numpy()
            )

        self.assertEqual(testflags,trueflags)
    
    def test_winddir_withsp(self):
        trueflags = [0,0,0,1,1,0,0,0]
        testflags = wind.check_winddir_withsp(
            self.data['spvals'].to_numpy(),
            self.data['dirvals'].to_numpy()
            )


        self.assertEqual(testflags,trueflags)

    def test_windsp_ratio_tz(self):
        '''
        Test windsp ratio using TZ aware dataframe
        '''
        tmzn = pytz.timezone('America/Denver')
        datatz = self.data.tz_localize(tmzn)
        testratio = wind.check_windsp_ratio(datatz)
        trueratio = 0.31

        self.assertAlmostEqual(testratio,trueratio,3)



if __name__=='__main__':
    unittest.main()
