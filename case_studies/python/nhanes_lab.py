# # Workbook for NHANES data

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

np.random.seed(34324)

f = "stats206s002f21"
base = "/scratch/%s_class_root/%s_class/shared_data/datasets" % (f, f)
df = pd.read_csv(os.path.join(base, "nhanes.csv.gz"))
df = df.loc[df["RIDAGEYR"] >= 18, :]
df = df.dropna()

# BMI is defined to be the ratio of weight in kilograms to the
# square of height in meters.  With this in mind, what would
# you expect to see for the correlation coefficient between
# BMI and weight, and the correlation coefficient between BMI
# and height?  Just think qualitatively, e.g. "a big positive
# number" or "a small negative number" or "something close to
# zero".

0

# Calculate the correlation coefficients between BMI and weight,
# and between BMI and height, over all subjects.

0

# Log transform height, weight, and BMI, and calculate the same
# correlation coefficients as in the previous cell.

0

# Stratify the dataset into four age groups (using qcut).  Then, 
# determine the correlation coefficient between weight and BMI 
# within each age group.  Which age group has the strongest 
# correlation?

0

# Create three BMI groups of approximately equal size using qcut.
# Then construct a 4 x 3 contingency table between age group (as 
# calculated above) and BMI group.

0

# Calculate the probabilities (proportions) corresponding to the
# counts in the previous cell.

0

# Calculate the closest independent distribution to the probabilities
# calculated in the previous cell.

0

# Calculate the Pearson residuals for the age group by BMI group
# cross classification.

0

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

# Use a loop to generate 100 random subsets of size 50 from the height data
# selected above.  Calculate the sample mean and sample variance of
# each subset.  Then take the variance of the sample mean, the
# variance of the sample variances, and the mean of the sample
# variances.  How are these values related?  

0

# Repeate the exercise from the previous cell using samples of size 200 
# and consider how the results change.

0

# Use a loop to calculate the sample correlation coefficient between
# BMI (BMXBMI) and blood pressure (BPXSY1), for the first `k`
# observations in the dataset.  The loop should run over values of `k`
# from 10 to the total sample size.  Plot these correlations against
# `k` and consider what result from probability theory is being
# illustrated here.

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
