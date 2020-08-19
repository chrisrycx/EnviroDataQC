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

### Basic Use
Pass data (Pandas dataframe) and measurement type to check_vals(). Dataframe is returned
with three new columns: 'flags_range', 'flags_rate', 'flags_flat'. Measurement types supported are defined in 'QCconfig.py'.

Flags:
* 0 : Good
* 1 : Suspicious
* 2 : Bad

### Configuration
Change and/or add dictionaries defined in 'QCconfig.py'. Dictionary entries define "good" ranges and "suspicious" ranges for each flag category. Configuration ranges can be non-continuous and any overlap between "good" and "suspicious" ranges will be flagged as "good".

