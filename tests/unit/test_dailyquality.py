'''
Test daily_quality function
'''

import unittest
import datetime
import pandas as pd
import numpy as np
import pytz
import envirodataqc as envqc

def make_dataset(datadate,percent_good,gaps):
    '''
    Create a pandas dataframe for testing with
    the input characteristics.

    Inputs:
    - datadate = string 'YYYY-MM-DD'
    - percent_good = int 0-100
    - gaps (hours) = int 1 - 12

    Return:
    - Pandas df

    Keep it simple
    - flags are only in flags_range
    - gaps created by flagging a group of points to 2
    '''
    #Create 15m datetimeindex
    enddate = datadate + ' 23:59'
    dts = pd.date_range(datadate,enddate,freq='15T')

    #Determine number of good points
    #15 min data for a date is 96 points
    goodpts = int(np.ceil(percent_good*96/100))
    badpts = 96 - goodpts

    #Create data frame
    data = pd.DataFrame(
        {
            'values':[999]*96,
            'flags_range':[0]*goodpts + [1]*badpts,
            'flags_rate':[0]*96,
            'flags_flat':[0]*96
        },
        index = dts
    )

    #Delete a range of values to create a gap
    if (gaps >= 1) and (gaps <=12):
        removedt = datadate + ' {}:00'.format(gaps + 12)
        data = data.loc[
            (data.index <= datadate + ' 12:00') | (data.index >= removedt)
        ]

    return data

class Testdataqc(unittest.TestCase):

    def setUp(self):
        '''
        Create a pandas dataframe for tests consisting of:
        Day 1 - all good data
        Day 2 - 90% good
        Day 3 - 80% good
        Day 4 - 90% good, gaps <=2hr
        Day 5 - 80% good, gaps <=2hr
        Day 6 - 90% good, gaps > 2hr
        Day 7 - 50% good, gaps > 2hr
        '''
        #Create dataframes
        #Some caution is warranted as removing data later changes
        #percent_good requiring 81% as an input below
        day1 = make_dataset('2021-03-20', 100, 0)
        day2 = make_dataset('2021-03-21', 90, 0)
        day3 = make_dataset('2021-03-22', 80, 0)
        day4 = make_dataset('2021-03-23', 90, 2)
        day5 = make_dataset('2021-03-24', 81, 1)
        day6 = make_dataset('2021-03-25', 90, 3)
        day7 = make_dataset('2021-03-26', 50, 3)
        
        #Concatenate dataframes
        self.testdf = pd.concat([day1,day2,day3,day4,day5,day6,day7])

    def test_alldata(self):
        '''
        Test daily_quality with testdf
        Expect:
        Day 1 - all good data = data quality 1
        Day 2 - 90% good = data quality 1
        Day 3 - 80% good = data quality 2
        Day 4 - 90% good, gaps 2hr = data quality 2
        Day 5 - 80% good, gaps 1hr = data quality 2
        Day 6 - 90% good, gaps > 2hr = data quality 3
        Day 7 - 50% good, gaps > 2hr = data quality 3

        '''
        #Create anticipated output
        dts = pd.date_range('2021-03-20','2021-03-26',freq='1D')
        true_quality = pd.DataFrame(
            {
            'quality':[1,1,2,2,2,3,3]
            },
            index = dts
        )

        #Calculate data quality
        dailyq = envqc.daily_quality(self.testdf)

        #Assert equal
        pd.testing.assert_frame_equal(true_quality,dailyq)
    
    def test_alldata_tz(self):
        '''
        Same test as above but data is now timezone aware
        '''
        tmzn = pytz.timezone('America/Denver')
        testdf = self.testdf.tz_localize(tmzn)

        #Create anticipated output
        dts = pd.date_range('2021-03-20','2021-03-26',freq='1D',tz=tmzn)
        true_quality = pd.DataFrame(
            {
            'quality':[1,1,2,2,2,3,3]
            },
            index = dts
        )

        #Calculate data quality
        dailyq = envqc.daily_quality(testdf)

        #Assert equal
        pd.testing.assert_frame_equal(true_quality,dailyq)
        


if __name__=='__main__':

    unittest.main()
    


