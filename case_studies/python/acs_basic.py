# # American Community Survey

# The American Community Survey (ACS) is a large survey of households
# and individuals in the United States, carried out by the US
# government on a continuous basis (around 3.5 million people are
# contacted per year).  It is arguably the most authoritative source
# of information about the demographic composition of the US
# population, and is used for many purposes in academic research,
# government, public policy, and in private industry.

# Some of the questions in the ACS are about sensitive topics, and
# therefore are only released in aggregate form.  The "public use
# microsample" (PUMS) is a set of individual ACS responses that only
# includes information that has been deemed safe for public release at
# the individual level.  Here we will work with a subset of the
# ACS/PUMS data.

# You will need to refer to the documentation to know what the ACS
# variable names mean.  The documentation is available
# [here](https://www.census.gov/programs-surveys/acs/technical-documentation/pums/documentation.html).
# We are using the 2018 "1-year" ACS/PUMS.  The file that contains the
# variable names is called a "data dictionary".  You can download it
# in various formats from the documentation link above.

# For this course, we are providing a simplified version of the
# ACS/PUMS data from 2018.  It contains a random subset of the
# cases and a selected subset of variables.

# Note that many PUMS variables are described as being "household" or
# "individual" variables.  These refer to characteristics of
# households (one or more people living at the same address) or to
# characteristics of individual people, respectively.

# These are the libraries that we will need.

import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as sps
import os

# Modify this string according to your section number (001 or 002):

f = "stats206s002f21"

# Next we load the data from the filesystem into a dataframe.

base = "/scratch/%s_class_root/%s_class/shared_data/datasets" % (f, f)
df = pd.read_csv(os.path.join(base, "pums_short.csv.gz"))

# ## Missing values

# Most datasets in the real world have missing values.  There are many
# reasons that a value may be missing.  For example, in some cases it
# makes no sense to calculate a number (e.g. income for a young
# child); or a person may refuse to answer a question in a survey; or
# a value may have inadvertently not been collected.

# In Pandas, missing values are represented using the symbol `NaN`,
# which means "not a number".  The method `isnull` tells us which
# values in a Pandas data structure (a dataframe or series) are null.
# If we want to know the proportion of observations for each variable
# that are missing, we can use the following:

df.isnull().mean()

# The above results shows us that a few variables, e.g. RNTP, have
# many missing values, while others, e.g. DIVISION, have no missing
# values.  The RNTP variable contains information about the amount of
# rent someone pays, so is always missing if a person does not rent
# the place where they live.  DIVISION indicates where in the US the
# person lives.  DIVISION can never be missing because the census
# bureau always has this information about each respondent.

# If you want to drop all cases (rows) of a variable that are missing,
# you can use the `dropna` method.  For example, suppose we want the
# non-missing values for the amount of money that households pay for
# rent (RNTP).  As noted above, these values are missing for
# households that do not rent their place of residence.  We can use
# the following code to obtain the non-missing values and store them
# in a series called x:

x = df["RNTP"].dropna()

# Note that an equivalent syntax to what is shown above is:

x = df.loc[:, "RNTP"].dropna()

# If is often useful to "chain" `dropna` with other methods or
# attributes of a series.  For example, if we want to know how many
# people have a non-missing rent value (i.e. are renters), we can use

df["RNTP"].dropna().size

# The treatment of missing values in a statistical analysis is a
# complex topic.  Here we are simply demonstrating how to drop the
# missing values from the dataset.  Sometimes this is the correct
# thing to do, but often it is not.

# ## Summary statistics of income

# We will turn now to the variable "HINCP" which is the household
# income -- the combined income of everyone living in one household.
# Note that income is not the same thing as wealth.  Many people have
# far more wealth than income, and their financial standing is largely
# a function of their wealth, not of their income.
#
# Overall, the United States has the following income characteristics:

df["HINCP"].describe()

# The summary statistics above are computed using the non-missing
# values of HINCP.  Most Pandas dataframe methods, like `describe`,
# automatically drop missing values, but functions and methods from
# other Python packages generally do not, so in some settings you will
# need to drop the missing values explicitly using `dropna`, like
# this:

df["HINCP"].dropna().describe()

# Here are the deciles of the household income in the US:

df["HINCP"].quantile([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

# We have discussed that the median (the 0.5 quantile) is a measure of
# "location" or "central tendency".  In this sense, the most typical
# annual household income in the US in 2018 was 63,000 USD.

# You will notice that a very small fraction of the household income
# values are negative, as shown below.  This is not an error.  Using
# standard definitions for income, it is possible for a household (or
# an individual) to have negative income.  The proportion of
# households with negative income can be obtained as follows:

(df.HINCP < 0).mean()

# Many quantile-based measures of dispersion are defined by taking the
# difference between an upper and a lower quantile that are symmetric
# around 0.5.  The most widely-used quantile-based measure of
# dispersion is the "interquartile range", or IQR, which is the
# difference between the 0.75 and 0.25 quantiles.  We can calculate it
# as follows

q = df["HINCP"].quantile([0.25, 0.75])
iqr = q[0.75] - q[0.25]

# The skew of a distribution reflects the spacing between quantiles.
# The standard quantile-based measure of skew is based on the spacings
# among the 0.25, 0.5, and 0.75 quantiles.  Let's start by examining
# these quantiles:

q = df["HINCP"].quantile([0.25, 0.5, 0.75])

# We can see that the difference between the 0.25 and 0.5 quantiles is
# less than the difference between the 0.5 and 0.75 quantiles.  This
# is indicative of _right skew_.  If the difference between the 0.25
# and 0.5 quantiles were greater than the difference between the 0.5
# and 0.75 quantiles, this would be indicative of _left skew_.  In
# practice, right skew is more common than left skew, but either is
# possible.

# The standard quantitative measure for skew based on quantiles is
# calculated next:

(q[0.75] + q[0.25] - 2*q[0.5]) / (q[0.75] - q[0.25])

# Since this value is positive, it follows that household income is
# right-skewed.  Income measures are almost always right-skewed.  The
# statistical reason that income is skewed is that the lower half of
# the income distribution is distributed from around 0 to 63,000 USD,
# while the upper half of the income distribution is distributed from
# around 63,000 USD to the highest income in the population, which is
# in the millions of dollars.

# ## Summary statistics of log-transformed income

# When working with quantitative data such as incomes, it is very
# common to transform the data prior to doing any analysis.  Log
# transformations are particularly common because they are very easy
# to interpret, and capture multiplicative relationships well.  If we
# use the base 2 logarithm, then the key fact to keep in mind when
# interpreting log-scale data is that if person A has a 1 unit greater
# value of the log2 income than person B, then person A has twice as
# much income as person B.

# Next we create a log (base 2) transformed income variable.  Note
# that we "clip" the income to remove people whose income is less than
# 1 USD, since we don't want to take the logarithm of non-positive
# values.

loginc = np.log2(df["HINCP"].clip(1, np.inf))

# We can now calculate the IQR of the log-scale data

q = loginc.quantile([0.25, 0.5, 0.75])
q[0.75] - q[0.25]

# The IQR is around 1.8, which means that a person at the 75th
# percentile of the income distribution has around 2^1.8 ~ 3.5 times
# greater income compared to a person at the 25th percentile of the
# income distribution.  This complements what we learned from the IQR
# of the raw data which showed us that a person at the 75th percentile
# of the income distributions earns around 79,200 USD more income than
# a person at the 25th percentile.

# Note that the IQR for log-scale data is dimension-free whereas the
# IQR for the untransformed income has units of USD.  The reason for
# this is that the difference of log-transformed values, $\log(x) -
# \log(y)$ is mathematically equivalent to the logarithm of their
# ratios $\log(x/y)$.  When taking a ratio, the units cancel.
# Therefore the IQR of log transformed data is dimension-free.

# Now we can calculate the quantile skew of the log transformed income data

(q[0.75] + q[0.25] - 2*q[0.5]) / (q[0.75] - q[0.25])

# This value is slightly negative (-0.09) whereas the skew of the
# untransformed data was positive at around 0.21.  It is not our goal
# here to remove the skew, but it is essentially always the case that
# log-transforming right-skewed data will reduce the skew, as it has
# done here.

# ## Stratifying to explain heterogeneity

# When considering a population such as the United States, which is
# extremely heterogeneous, it is usually much more informative to
# analyze the data after stratifying the population according to the
# values of factors that explain some of the heterogeneity.  The ACS
# includes a variable called "FES" which partitions the population
# into 8 subgroups based on household structure.  See the data
# dictionary for the precise definitions of the groups (note that "LF"
# in the documentation stands for "labor force").  These groupings
# were defined many years ago, and are based on heterosexual family
# structures.  Other variables added more recently capture information
# about same-sex family structures.

# First we can look at the set of standard summary statistics captured
# by the `describe` method, but now restricting the calculations to
# the values within each stratum.

df.groupby("FES")["HINCP"].describe()

# From the table above, we see that the wealthiest households, based
# on the median income, are those including a married couple, with
# both members of the couple working (group 1).  The least wealthy
# households are those including a single female who is not working
# (group 8).

# It is often convenient to re-order the rows of the output in order
# to sort one of the values.  This can be accomplished as below, where
# we sort the values according to the median income.

df.groupby("FES")["HINCP"].describe().sort_values(by="50%")

# The output of the `describe` method does not include the IQR, but we
# can easily add it ourselves, as below.

t = df.groupby("FES")["HINCP"].describe()
t["iqr"] = t["75%"] - t["25%"]
t

# We see that the IQR and median are related -- when the IQR is small,
# the median tends to be small, and when the IQR is large, the median
# tends to be large.  This is called a _location/dispersion
# relationship_.  In absolute terms (using USD as the units), there is
# more dispersion in the higher income subgroups than in the lower
# income subgroups.

# ## Multiple explanatory factors

# In many cases we want to stratify on two or more factors that may
# "explain" the variation in a value of interest.  Above we considered
# household structure as one explanatory factor.  Now we will consider
# the geographic region where the respondent lives as well.  The
# Census Bureau has several ways of partitioning by geography, the
# variable `REGION` here uses four levels (see the data dictionary for
# what they correspond to).  We will conduct a "two-way"
# stratification, and determine the median income for people living in
# each combination of a FES level and a REGION level.

df.groupby(["FES", "REGION"])["HINCP"].aggregate(np.median)

# The result of a `groupby`/`aggregate` expression, such as above, is
# a new dataframe in which the distinct combinations of the grouping
# variables (here, "FES" and "REGION") form the dataframe's _index_.
# To view these results as a table, it is easier to "unstack" the
# results, which moves one level of the row index to the columns.
# This is also called "pivoting", and can be accomplished as follows:

df.groupby(["FES", "REGION"])["HINCP"].aggregate(np.median).unstack()

# It may be more informative to view these results with a parallel
# coordinates plot.  To make this plot, we need to move the `FES` and
# `REGION` variables from the index to regular columns of the
# dataframe.  This is done using the `reset_index` method.

dx = df.groupby(["FES", "REGION"])["HINCP"].aggregate(np.median)
dx = dx.reset_index()
sns.lineplot(x="FES", y="HINCP", hue="REGION", palette=sns.color_palette("husl", 4), data=dx)

# This plot shows us that for all household types, regions 1 and 4
# (northeast and west) have greater median incomes than regions 2 and
# 3 (midwest and south).  Region 1 has the highest median income for
# household type 1 (a married couple, both members of which are
# working), while household type 4 (a married couple, neither of whom
# is working) has slightly higher median income in the west (region
# 4).  Regions 2 and 3 are quite similar for all household types
# except for type 6 (single males not in the labor force), where the
# income is somewhat higher in the midwest than in the south.

# The FES variable is nominal, although there is a partial ordering to
# the categories.  Lower numbers are assigned to married couple
# families, and lower numbers are assigned to households in the labor
# force.  But certain pairs of categories cannot be ordered, for
# example, a married couple in which only the wife works cannot be
# ordered relative to a married couple in which only the husband
# works.

# Next we consider an analogous parallel coordinates plot using log
# scale data.

df["log_HINCP"] = np.log2(df["HINCP"].clip(1, np.inf))
dx = df.groupby(["FES", "REGION"]).log_HINCP.aggregate(np.median)
dx = dx.reset_index()
sns.lineplot(x="FES", y="log_HINCP", hue="REGION", palette=sns.color_palette("husl", 4), data=dx)

# The above plot may inspire us to consider a contrast (difference) of
# the log scale data between two regions, say regions 1 and 3.

df["log_HINCP"] = np.log2(df["HINCP"].clip(1, np.inf))
dx = df.groupby(["FES", "REGION"]).log_HINCP.aggregate(np.median)
dx = dx.unstack()
dy = dx[1] - dx[3]
dy.name = "Diff_1_3"
dy = dy.reset_index()
sns.lineplot(x="FES", y="Diff_1_3", data=dy)

# The fact that the differences plotted above are not constant over
# the FES categories indicates that the ratio between incomes in the
# northeast and the south are not the same for all household types.
# For example, the typical income for family type 4 (a married couple,
# neither of whom is working) is only slightly greater in the
# northeast compared to the south (2^0.12 ~ 9%).  But the typical
# income for family type 6 (a single non-working male) is over 30%
# greater in the northeast compared to the south.  It is likely that
# other demographic factors underly these differences.  For example,
# non-working married couples are often retired, and social security
# reduces the dispersion in incomes for such people.  On the other
# hand it is possible that a single non-working male in the northeast
# is more likely to be a divorced professional, while a single
# non-working male in the south is more likely to be a younger man who
# was never married and has low professional skills.  This is only
# speculation, additional analysis may help clarify these differences.

# This analysis shows that it is possible to gain insight about two
# explanatory factors by stratifying the data on the _cross product_
# consisting of all subgroups defined by pairs of levels of the two
# factors.  These subgroups are sometimes called _cells_.  It should
# be clear however that this approach will not "scale" very well --
# cross products for three or more factors will generally produce huge
# numbers of cells.  We may have too little data per cell to produce
# meaningful estimates of population quantities, and even if this is
# not an issue, there will be a huge number of combinations to
# consider.  The difficulty of _controlling_ for, or stratifying on
# multiple explanatory factors is one of the major challenges that
# arises in statistical data analysis.

# ## Quantiles and moments

# The most commonly encountered measures of location are the mean and
# the median.  For a perfectly symmetric distribution, the mean and
# the median are identical.  For a right-skewed distribution, the mean
# is greater than the median, and for a left-skewed distribution, the
# median is greater than the mean.  We can compare the mean and the
# median in the ACS data by calculating these two statistics within
# each household structure group.  Note that by providing two
# summarizing functions to `aggregate` in a list, we get a result in
# which both summarizing functions are calculated for each group.

df.groupby("FES")["HINCP"].aggregate([np.mean, np.median])

# Above we see that the mean is greater than the median in every case.
# This happens with right-skewed data, and as mentioned already,
# income values are almost always right-skewed.

# The most commonly encountered measures of scale are the standard
# deviation, median absolute deviation (MAD) and interquartile range
# (IQR).  These can all be calculated in Python, but unfortunately
# they are located in different packages.  This leads to the slightly
# awkward syntax below.

r = df.groupby("FES")["HINCP"].aggregate([np.std, "mad", sps.iqr])
print(r)

# Using `aggregate` with multiple summary functions produces a "wide"
# array of results.  For plotting and further analysis, we want our
# data to have "long" form.  We can do this as follows.

r = r.reset_index().melt(id_vars="FES", var_name="stat_name", value_name="stat_value")
print(r)

# Now we can make a parallel coordinates plot of the results, which
# makes it easier to compare the different measures of scale.

sns.lineplot(x="FES", y="stat_value", hue="stat_name", palette=sns.color_palette("husl", 3), data=r)

# ## Residuals and Z-scores

# Residuals are obtained by taking each observation, and subtracting
# from it a reference value.  Usually this reference value is a
# measure of location calculated on an appropriate group of related
# observations.  For example, in the United States (as in almost any
# country), income varies geographically.  Thus, an appropriate
# reference value for a household's income may be the median income
# for the state in which that household is located.  Below we
# calculate the median log-income values by state using the
# `transform` method with `groupby`, then subtract the state median
# log-income values from the individual household log-income levels to
# produce median residuals.

df["linc_resid_med"] = df["log_HINCP"] - df.groupby("ST")["log_HINCP"].transform(np.median)

# Using `groupby` with `transform` is related to using `groupby` with
# `aggregate`, but differs in one important way.  In the case of
# `aggregate`, the result is smaller in length than the source data,
# as it contains one value for each grouping level.  For example, if
# we are aggregating over the 50 US states, then the result of
# `aggregate` would have 50 rows.  When using `transform`, the summary
# results are calculated as with aggregate, but then they are "spread"
# back over the rows of the original dataframe.

# The median of the median residuals is zero:

df["linc_resid_med"].median()

# The mean of the median residuals is not zero in general:

df["linc_resid_med"].mean()

# We can also calculate the mean residuals

df["linc_resid_mean"] = df["log_HINCP"] - df.groupby("ST")["log_HINCP"].transform(np.mean)

# These residuals have mean zero but their median is not (in general)
# equal to zero:

print(df["linc_resid_med"].mean())
print(df["linc_resid_med"].median())

# To fully standardize the values to "Z-scores", we need to divide the
# residuals by a measure of scale.  Most commonly, the mean residuals
# are scaled by the standard deviation, and the median residuals are
# scaled by either the IQR or the MAD.  This gives us moment based
# Z-scores and quantile-based Z-scores:

df["linc_z_m"] = df["linc_resid_mean"] / df.groupby("ST")["log_HINCP"].transform(np.std)
df["linc_z_q"] = df["linc_resid_med"] / df.groupby("ST")["log_HINCP"].transform("mad")

# We can check the summary statistics of these Z-scores to confirm
# that they behave as expected.  Specifically, the moment-based
# residuals will have mean zero and standard deviation one, and the
# quantile-based residuals will have median zero and MAD one (the MAD
# is not shown in the table below).  Note that computers often exhibit
# small numerical errors since the standard representation of a real
# number on a computer has finite precision.  Therefore, the mean of
# the moment based residuals below may be expressed as something like
# "2e-14", which means $2\times 10^{-14}$.

df[["linc_z_m", "linc_z_q"]].describe()

# Overall, the Z-scores based on moments and quantiles look quite
# similar, as shown in the scatterplot below.

sns.scatterplot(x="linc_z_m", y="linc_z_q", data=df)

# Since log-income is approximately unskewed, this result is expected.
# If we were working with non-logged income, there would have been a
# greater discrepancy between the quantile-based and moment-based
# residuals.

# ## The quantile function

# The quantile of a dataset can be calculated for any probability
# point p.  Therefore, we can define the quantile function to be the
# set of all quantiles, indexed by p.  To plot the quantile function,
# we choose a finite set of probabilities that approximately cover the
# interval [0, 1], and calculate the quantile for each.  Below we plot
# the quantile function for household income in the United States.

p = np.linspace(0.01, 0.99, 99)
q = df["HINCP"].quantile(p)
sns.lineplot(x=p, y=q)

# Similarly, we can plot the quantile function for log income, but
# here we exclude the people whose income is less than 10,000 USD.

dx = df.loc[df["HINCP"] >= 10000, :]
q = dx["log_HINCP"].quantile(p)
sns.lineplot(x=p, y=q)

# The plot above tells us a great deal about income distribution in
# the US.  From the 20th to the 80th percentile, the difference is
# around 2, and since these data are on the log2 scale, this means
# that there is around a factor of 4 difference between these two
# points in the distribution. The quantile function drops sharply for
# p less than 0.2, and rises sharply for p greater than 0.8, and
# especially for p greater than 0.9.  The latter reflects the fact
# that incomes in the highest 10-20 percent of the distribution are
# much greater than incomes in the lower 80 percent of the
# distribution.

# It is often informative to compare two or more quantile functions.
# Below we calculate the quantile function of income within each
# state.  Then we reduce the dataset to contain only three states,
# California (6), Michigan (26), and Texas (48).  See the ACS/PUMS
# data documentation for the complete list of numeric state codes.

dz = dx.groupby("ST")["log_HINCP"].quantile(p)
dz = dz.reset_index()
dz = dz.loc[dz["ST"].isin([6, 26, 48]), :]
dz = dz.rename(columns={"level_1": "p"})

# Next we plot the quantile functions for the three states

sns.lineplot(x="p", y="log_HINCP", style="ST", data=dz)

# We can learn a lot by carefully considering this plot.  First, the
# medians are given by the heights of the graphs at p=0.5.  California
# has a substantially greater median than Michigan or Texas, and the
# median for Texas is slightly greater than the median for Michigan.
# In fact, California has a greater income at every quantile level
# than Michigan and Texas, although the difference is small at the
# lowest values of the probability parameter p.  When this happens, we
# say that the incomes in California are _stochastically greater_ than
# the incomes in Michigan and Texas.  The convergence of the quantile
# functions at the lowest values of p indicates that the poorest
# people in each state have around the same income, but it is notable
# that even by the 10th percentile, incomes in California are greater
# than in the other states.
