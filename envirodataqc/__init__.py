'''
EnviroData QC - 
Quality control and assurance of
environmental data.

API
- Uses config.yaml to define QC settings for different variables
- Check Values
    Input
    -- pandas dataframe with datetimes and values
    -- variable type matching a variable listed in QC file
    Output
    -- Dataframe with original data plus flags
- Check Gaps
    Input
    -- pandas dataframe with datetimes and values
    -- ??

General Algorithm
- import yaml configuration
    -- Possible definition of config object
- define check_vals
- define check_gaps



check_gaps Algorithm
-- ?

'''
#Load required libraries
import yaml

#Load QC settings
configpath = 'config.yaml'  #****This might not work when package is imported
with open(config,'rt') as yin:
    configyaml = yin.read()

config = yaml.safe_load(configyaml) 

#Check Values function
def check_vals(data,vartype):
    '''
    Evaluate range, step change, and flatlining
    of input data.
    Inputs
     - Pandas dataframe with datetimes (col 0), values (col 1)
     - variable type matching one of the variables in configuration file
    Output - Pandas dataframe of original input plus flag columns 

    check_vals Algorithm
    - Load setting for input variable type
    - Check for range
    - Check for step change
    - Check for flatlining
    '''
    #Copy input data frame
    **might need to rename data column
    **Initialize bdpts
    
    #Load QC Settings for this variable type
    qc = qcsettings(config[vartype])

    #Create flag columns
    data['flags...'] = 0

    #Check range
    data['flags_range'] = qc.range(data.values[])

    #Remove any bad values from dataframe
    bdpts = bdpts.join(data[data.flags == 2])
    data = data[data.flags != 2]

    #Check step change
    data['flags_step'] = qc.step(data.values[])

    ##Remove any bad values from dataframe
    bdpts = bdpts.join(data[data.flags == 2])
    data = data[data.flags != 2]

    #Check flatlining
    data['flags_flat'] = qc.flat(data.values[])

    #Put bad points back in dataset
    if not bdpts.empty:
        data = data.append(bdpts)
        data.sort_index(inplace=True)

    return data
