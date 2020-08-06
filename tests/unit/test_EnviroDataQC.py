'''
Test EnviroDataQC main functions
- check_vals, check_gaps
- Uses unittest
- Checks function with data from tphdata.csv
- Change tphdata.csv via testdata.ods

'''

import unittest
import pandas as pd
import numpy as np
import envirodataqc

class TestEnviroDataQC(unittest.TestCase):

    def setUp(self):
        '''
        Load test data
        '''
        dpath = '../data/tphdata.csv'
        self.data = pd.read_csv(dpath,index_col=0,parse_dates=True)

    def tearDown(self):
        pass

    def test_airT(self):
        '''
        Check air temperature values from tphdata.csv
        '''
        airdata = self.data.loc[:,['airT','airT_flags_range']]
        airdata.columns = ['airT','flags_range']
        
        #Run check_vals
        testdata = envirodataqc.check_vals(
            self.data.loc[:,['airT']],
            'air_temperature'
            )

        #Test output
        pd.testing.assert_frame_equal(
            airdata,
            testdata,
            check_dtype = False,
            check_names = False
            )

    def test_humidity(self):
        '''
        Check humidity values from tphdata.csv
        '''
        airdata = self.data.loc[:,['humidity','humidity_flags_range']]
        airdata.columns = ['humidity','flags_range']
        
        #Run check_vals
        testdata = envirodataqc.check_vals(
            self.data.loc[:,['humidity']],
            'humidity'
            )

        #Test output
        pd.testing.assert_frame_equal(
            airdata,
            testdata,
            check_dtype = False,
            check_names = False
            )

    def test_pressure(self):
        '''
        Check air pressure values from tphdata.csv
        '''
        airdata = self.data.loc[:,['air_pressure','air_pressure_flags_range']]
        airdata.columns = ['air_pressure','flags_range']
        
        #Run check_vals
        testdata = envirodataqc.check_vals(
            self.data.loc[:,['air_pressure']],
            'air_pressure'
            )

        #Test output
        pd.testing.assert_frame_equal(
            airdata,
            testdata,
            check_dtype = False,
            check_names = False
            )

    def test_gaps(self):
        '''
        Verify that output from check_gaps is correct
        '''
        dtindex = self.data.index

        #Run function
        totgaps = envirodataqc.check_gaps(dtindex)

        #Test output
        self.assertEqual(totgaps,1.3)



if __name__=='__main__':

    unittest.main()

  