# EnviroDataQC
This library provides a framework for assessing quality of environmental data.

Data is assessed with respect to:
* Data Range
* Data rate of change
* Data flatlining

Additionally, special methods are provided for assessing wind speed and direction data.
Data is classified as either suspicious or bad based on either default or custom user settings.

### Installation
pip install envirodataqc

The configuration file is currently a python script in the package, so it may be
easier to clone the repository rather than install from PYPI if you want to change
the configuration.

### Basic Use
Pass data (Pandas series) and measurement type to check_vals(). A Pandas dataframe is returned with three new columns: 'flags_range', 'flags_rate', 'flags_flat'. Measurement types supported are defined in 'QCconfig.py'.

Flags:
* 0 : Good
* 1 : Suspicious
* 2 : Bad

### Configuration
Change and/or add dictionaries defined in 'QCconfig.py'. Dictionary entries define "good" ranges and "suspicious" ranges for each flag category. Configuration ranges can be non-continuous and any overlap between "good" and "suspicious" ranges will be flagged as "good".

### Wind specific checks
* check_windsp_ratio - Check ratio of mean windspeed to max
* check_windsp_withdir - Check if windspeed is consistent with direction
* check_winddir_withsp - Check if direction is consistent with windspeed

### Other Functions
* check_gaps(index) - Given a Pandas datetime index outputs total time where gaps between timestamps are > 1hr.
* daily_quality(data) - Given a Pandas series (index=timestamp, values=data flags), return a pandas series with a consolidated daily quality level (0,1,2) 

