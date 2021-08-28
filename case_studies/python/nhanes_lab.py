# # Workbook for NHANES data

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

np.random.seed(34324)

base = "/scratch/stats206w21_class_root/stats206w21_class/shared_data/datasets"
df = pd.read_csv(os.path.join(base, "nhanes.csv.gz"))
df = df.loc[df["RIDAGEYR"] >= 18, :]
df = df.dropna()

# Restrict the dataset to females between the ages of 18 and 70.
# Calculate the mean height (BMXHT), the variance of the height, and
# the sample size for this subset of the data.  Then calculate the
# standard error of the mean for the mean height in this subsample.

0

# Use the method `round(-1)` to create a variable that indicates a
# person's decade of age.  Then use `groupby` to calculate the sample
# size, standard deviation, and standard error of the mean (SEM) for
# height (BMXHT) within each decade.  Note which decade has the
# largest SEM, and consider whether this SEM being large is due to the
# standard deviation (SD) or the sample size.

0

# Use a loop to generate 100 subsets of size 50 from the height data
# selected above.  Calculate the sample mean and sample variance of
# each subset.  Then take the variance of the sample mean, the
# variance of the sample variances, and the mean of the sample
# variances.  How are these values related?  Then repeat the exercise
# using samples of size 200 and consider how the results change.

0

# Use a loop to calculate the sample correlation coefficient between
# BMI (BMXBMI) and blood pressure (BPXSY1), for the first `k`
# observations in the dataset.  The loop should run over values of `k`
# from 10 to the total sample size.  Plot these correlations against
# `k` and consider what result from probability theory is being
# illustrated here.

0

# Generate a set of 100,000 values by forming `0.1 + z^2`, where `z`
# follows a standard normal distribution.  Calculate the mean and
# variance of these 100,000 values.  Then, within each iteration of a
# loop, generate 20 values in this same way.  Retain the sample mean
# and sample standard deviation of each set of 20 values. Then,
# calculate the standard deviation of these sample means, and the mean
# of the sample standard deviations.  Use these findings to validate
# the SEM in this setting.

0

# Sample 50 females at random and 50 males at random, then calculate
# the sample mean and sample standard deviation for systolic blood
# pressure within each of these two samples.  Calculate the difference
# between these two means, and calculate the standard error for this
# difference.  Place this all into a loop that iterates 200 times.
# Once the loop has completed, calculate the standard deviation of the
# 200 mean differences, and the mean of the 200 standard errors.  Use
# these results to assess the validity of your standard error
# calculation.

0
