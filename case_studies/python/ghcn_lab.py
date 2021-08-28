# # Workbook for GHCN data

# The following code will get you set up to work with this dataset.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import os

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

base = "/scratch/stats206w21_class_root/stats206w21_class/shared_data/datasets"
df = pd.read_csv(os.path.join(base, "ghcnd_gsn.csv.gz"))

df["date"] = pd.to_datetime(df["date"])

# Take the daily minimum temperature values (tmin) from the month of
# January, and consider whether within each station the values are
# predominantly left skewed or predominantly right skewed.

0

# Perform the same analysis for another month, and for the daily
# maximum temperature values.  How would you describe and interpret
# these findings?

0

# The conditional standard deviation of $Y$ given $X$ is the standard
# deviation of $Y$ calculated for a subset of the sample in which $X$
# is close to a specified reference value.  For our purposes, $Y$ will
# be the daily maximum temperature, and $X$ will be the latitude,
# elevation, and month.  What is the conditional standard deviation
# for latitude 20, elevation 0, and month January?  You will have to
# use your judgment to decide which data values are "close" to the
# reference point.

0

# Repeat the previous exercise for elevation 1500 and month April,
# ignoring latitude.

0

# Calculate the interdecile range (IDR) of daily maximum temperature
# values for each station within each year.  Then calculate the median
# IDR for each year (over the stations).  Display these median IDR
# values from year 1970 onward and comment about any trends that may
# be evident.

0

# Use loess to estimate the conditional mean of the daily maximum
# temperature as a function of latitude, using data from January.
# Then form residuals from the observed daily maximum temperature
# values with respect to these conditional means.  What are the
# average residuals for stations in the northern and southern
# hemispheres, respectively?

0
