### API Design ###

envirodataqc.checkvals(data,data_type)
* Inputs
    * data: pandas dataframe with col0=timestamp, col1=value
    * data_type: One of the data types listed in configuration file
* Returns - pandas dataframe with 5 new columns corresponding to data flags
    * New columns: 'flag_bad','flag_special','flag_flat','flag_step','flag_range'

envirodataqc.checkgaps()...undefined

envirodataqc.checkconsistancy()... undefined
envirodataqc.checkspecial(data1,data2... type)... not sure how to support this
* Probably have a separate wind check


### Algorithms ###
checkvals
1. Load configuration settings for datatype
2. Check that values are in range, flag
3. Remove bad values and check remaining values for step change, flag
4. Remove bad values and check remaining values for flatlining, flag
5. Return final dataframe including all bad values

### Objects ###
qcsettings
* Attributes - different ranges
* Methods - check a particular value

#### Check