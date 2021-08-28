# # Workbook for American Community Survey data

import pandas as pd
import numpy as np
import os

# Load the data from the filesystem into a dataframe.

base = "/scratch/stats206w21_class_root/stats206w21_class/shared_data/datasets"
df = pd.read_csv(os.path.join(base, "pums_short.csv.gz"))

# The variable named `VALP` contains the value of a property owned by
# members of a household which is also their residence (this includes
# properties held with a mortgage).  The variable named `RNTP`
# contains the amount of rent paid per month.  According to ACS
# definitions, each household can be a renter or an owner, but not
# both.  Also, some households are neither renters nor owners.
# Therefore, each row of the dataframe may contain a non-NaN value for
# `RNTP` or for `VALP`, but never for both.  Some rows of the
# dataframe may have NaN values for both `RNTP` and for `VALP`.  The
# following steps confirm these expectations.  You can complete these
# exercises using combinations of `dropna`, `shape`, and `size`, along
# with selecting one or more columns of data using syntax like
# `df["x"]` and `df[["x", "y"]]`.

# How many rows are in the dataframe?

0

# How many rows in the dataframe have a non-NaN value of `VALP`?

0

# How many rows in the dataframe have a non-NaN value of `RNTP`?

0

# Confirm that no row in the dataframe has a non-NaN value for both
# `VALP` and `RNTP`.

0

# The numbers for `VALP` tend to be large.  Create a new version of
# `VALP` called `VALPx` which contains the property values in units of
# thousands of dollars.

0

# What are the deciles of VALPx?

0

# Calculate the median and MAD of `VALPx` within levels of the family
# structure/employment type variable `FES`.  Is there a
# location/dispersion relationship between the median and MAD such
# that when comparing two levels of FES, if the median is greater in
# one level then the MAD is also greater in that level?

0

# Use `groupby` and `transform` to construct median residuals for
# `VALPx` around the FES-specific medians, and around the
# REGION-specific medians.  Calculate the IQR of each set of residuals
# and compare them.  What can you conclude by observing that one set
# of residuals has a smaller IQR than the other?

0

# Calculate the median rent (`RNTP`) and the median property value
# (`VALPx`) for each state (using groupby/aggregate).  Then take the
# ratio between these values (for each state).  Which state has the
# greatest and smallest ratio?  What is the ratio between the greatest
# and smallest ratio?

0

# Using the data in the `FPARC` variable, create a new binary
# (False/True) variable that indicates whether the household has
# "related children" (i.e. children related to the household heads)
# living at home.  You might want to use the `isin` method to
# accomplish this.

0

# Compare the property values for households with and without related
# children at home.

0

# Use `groupby/describe` to obtain summary statistics for every
# combination of the `DIVISION` variable and the variable that you
# created above indicating whether the household has related children
# at home.  Do these summary statistics suggest a consistent
# stochastic ordering within every DIVISION level between the property
# values for households with and without children?

0

# Calculate the log property values, then calculate the mean value for
# each `DIVISION` of `VALP` and its log transformed version.  If you
# sort the means for `VALP`, are they also sorted for the means of the
# log-transformed data?

0

# Create a dataframe containing the 25th, 50th, and 75th percentiles
# for the values of the log-transformed `VALP` within each `DIVISION`.
# You can do this using `groupby` then `quantile`.  The result will be
# in long form.  Use "unstack" to convert it to wide form.

0

# Take what you did in the previous cell, then extend it to obtain the
# quantile skew of log property value within every `DIVISION`.

0
