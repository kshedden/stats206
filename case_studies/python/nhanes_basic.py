# # NHANES

# The National Health and Nutrition Examination Survey (NHANES) is a
# cross sectional observational study run every 2-3 years by the
# United States Centers for Disease Control (CDC).  It collects
# extensive demographic and health-related data on a representative
# sample of the US population.

# In this notebook, we will use the NHANES data to illustrate some
# basic ideas relating to sampling distributions, including standard
# errors, the law of large numbers, and the central limit theorem.

# First we import the libraries that we will be using.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# We will be simulating data in this notebook.  To make the results
# reproducible, we will set the seed of the random number generator to
# a fixed value.

np.random.seed(34324)

# Modify this string according to your section number (001 or 002):

f = "stats206s002f21"

# Now we load the NHANES data from a file.

base = "/scratch/%s_class_root/%s_class/shared_data/datasets" % (f, f)
df = pd.read_csv(os.path.join(base, "nhanes.csv.gz"))

# Here we will be focusing on blood pressure, which is mostly relevant
# for adults.  Therefore we exclude people under the age of 18.

df = df.loc[df["RIDAGEYR"] >= 18, :]

# For this notebook, we only need three variables:

dx = df[["RIDAGEYR", "RIAGENDR", "BPXSY1"]].dropna()

# # Blood pressure means in sex by age strata

# To begin, we construct a stratified age variable, constructing five
# bins with roughly equal sample sizes.  The pandas method `qcut`
# stands for _quantile cut_, and is used to create a sequence of
# categories from a quantitative variable based on its quantiles.  In
# this case, we are using the quintiles of age to form five strata.

dx["Age_strat"] = pd.qcut(dx.RIDAGEYR, 5)

# There is no built-in function for calculating the standard error of
# the mean (SEM), so we provide that here:

def calc_sem(x):
    return x.std() / np.sqrt(len(x))

# Next we create a table showing the mean, standard error, sample
# size, and standard error of the mean (SEM) for 10 age x sex strata.
# In NHANES, females are coded as 2 and males are coded as 1.

r = dx.groupby(["RIAGENDR", "Age_strat"])["BPXSY1"].aggregate([np.mean, np.std, np.size, calc_sem])
r

# The table above shows, as expected, that older people tend to have
# higher blood pressure than younger people.  Also, except for the
# oldest age band, males of a given age tend to have higher blood
# pressure than females of the same age.  In the highest age band, the
# relationship between sex and blood pressure is reversed.  This could
# be due to "survivorship bias", which is a form of selection bias.
# Many of the males with very high blood pressure have died by this
# point, leaving behind only the relatively healthier males.

# The table also reveals substantial heteroscedasticity -- the
# standard deviations are larger in the strata for older people, which
# also happen to have greater means.  Thus, these data exhibit a
# _location/dispersion relationship_.  When the location (mean) is
# greater, then the dispersion (standard deviation) is also greater.
# Since the standard error of the mean depends on the standard
# deviation, the SEM is larger for the strata containing older people.
# Thus, we are estimating the population mean less precisely in the
# older age bands.

# # Simulation study for the standard error of the mean

# First we will perform a simulation study to illustrate how the
# standard error of the mean behaves as we vary the sample size, and
# when sampling from distributions with different levels of
# dispersion.  The simulation study will focus on the strata for the
# youngest and oldest bands of women in the population.  Below we
# extract the data for these subjects.

a1 = dx["Age_strat"].cat.categories[0] # youngest women
v1 = dx.loc[(dx["Age_strat"] == a1) & (dx["RIAGENDR"] == 2), "BPXSY1"]
a2 = dx["Age_strat"].cat.categories[-1] # oldest women
v2 = dx.loc[(dx["Age_strat"] == a2) & (dx["RIAGENDR"] == 2), "BPXSY1"]

# Since we are focusing on dispersion here, we will remove the means
# to make it easier to make comparisons.

v1 -= v1.mean()
v2 -= v2.mean()

# As intended, the data from older women (right side below) are more
# dispersed than the data for younger women (left side below).

sns.boxplot(data=[v1, v2])

# The following code generates sample means by randomly drawing
# subsets from the two NHANES strata selected above.  For each
# stratum, we sample 100 independent subsets of sizes ranging from 10
# to 160, then take the sample mean of each subset that we obtain.

ns = [10, 20, 40, 80, 160] # Sample sizes to generate
x, nl = [], []
for v in v1, v2:
    for n in ns:
        # Generate 100 datasets by sampling n values from either
        # v1 or v2, then take the mean of each sampled dataset.
        y = [np.mean(np.random.choice(v, n)) for _ in range(100)]
        x.append(y) # sample means
        nl.append(n) # sample size

# The plot below illustrates how the sample means taken from samples
# of different sizes, and from different populations, differ in terms
# of their level of dispersion.  There is evidently less dispersion as
# the sample size grows, reflecting the presence of the factor of
# $1/\sqrt{n}$ in the standard error of the mean.  Also, the sample
# means for the older stratum (right half of the plot), which is a
# parent population with greater dispersion, are themselves more
# dispersed.  This reflects that presence of the factor of $\sigma$ in
# the standard error of the mean.

plt.clf()
plt.boxplot(x)
plt.xticks(range(1, 11), nl)
plt.xlabel("Sample size")
plt.ylabel("Sample means")

# # Simulation study for the sampling distribution of the mean

# Next we will perform a simulation study to illustrate the sampling
# distribution of the mean.  The simulation study will focus on the
# stratum for the the first row of the table above (the youngest band
# of men).  First we extract the values from this row into separate
# variables:

m, s, n, sem = tuple(r.iloc[0, :])
n = int(n)

# Next we generate 1000 data sets, each with the same mean, standard
# deviation and sample size as the selected stratum of people from the
# actual NHANES data.  The data here are simulated using a normal
# distribution, but below we will consider other distributions.

x = [m + np.random.normal(size=n)*s for _ in range(1000)]

# Next we calculate the sample mean from each simulated data set:

y1 = [u.mean() for u in x]

# The following histogram shows how the simulated sample means are
# distributed.  The sample mean value that was actually obtained in
# the NHANES study could be any one value drawn from this
# distribution.

sns.distplot(y1)
plt.xlabel("Sample mean")

# A probability distribution called the _gamma distribution_ is skewed
# and produces only positive values.  Next we repeat the simulation
# above, using gamma-distributed rather than normally distributed
# values.  You do not need to know the details of how the gamma
# parameters are determined below.

a = (m / s)**2
b = s**2 / m
x = [np.random.gamma(a, b, size=n) for _ in range(1000)]
y2 = [u.mean() for u in x]
sns.distplot(y2)
plt.xlabel("Sample mean")

# A third way to do the simulation is to randomly select from the
# observed data.  Since we want to randomly select n values, and the
# observed data consist only of n values, we have to select "with
# replacement".  If we selected "without replacement" we would get
# exactly the same values in each sample, hence the means would be the
# same and the resulting distribution would have zero variance.

ax = dx["Age_strat"].cat.categories[0]
v = dx.loc[(dx["Age_strat"] == ax) & (dx["RIAGENDR"] == 1), "BPXSY1"]
x = [np.random.choice(v, n, replace=True) for _ in range(1000)]
y3 = [u.mean() for u in x]
sns.distplot(y3)
plt.xlabel("Sample mean")

# The above three plots illustrate central limit theorem (CLT).  In
# each case, we are calculating sample means of independent and
# identically distributed (iid) samples of size 539 (since this is the
# size of the first stratum shown in the table above).  In the first
# case, the data are sampled from a normal distribution, in the second
# case, the data are sampled from a gamma distribution, and in the
# third case, the data are sampled with replacement from the observed
# NHANES data.  The distributions of sample means in the three cases
# appear quite similar.  The CLT argues that the distribution of
# sample means has a distribution that does not depend on the
# distribution of the individual data values.  Moreover, this
# distribution, according to the CLT, is approximately normal.

# Recall that a quantile-quantile (QQ) plot aids in determining
# whether two samples of data follow distributions that are related by
# a linear transformation.  Thus, we can sample 1000 iid standard
# normal values, then construct QQ plots comparing these values to
# each of the three sets of sample means constructed above.  If these
# plots are approximately linear, this means that the sample means
# approximately follow normal distributions.

z = np.random.normal(size=1000)

plt.clf()
plt.plot(np.sort(z), np.sort(y1), 'o')
plt.grid(True)

plt.clf()
plt.plot(np.sort(z), np.sort(y2), 'o')
plt.grid(True)

plt.clf()
plt.plot(np.sort(z), np.sort(y3), 'o')
plt.grid(True)

# Although there are some small deviations in the tails, the three
# plots above show overwhelmingly linear patterns, supporting the
# argument that the sample means derived from normal or gamma
# distributions, or by resampling from the observed data, all produce
# sample means that are approximately normally distributed.

# ## Law of large numbers

# Now we will use simulation to illustrate the law of large numbers
# (LLN).  The LLN argues that if we take the sample mean of $n$ iid
# values, say $\bar{x}^{(n)} = (x_1 + \cdots + x_n)/n$, and then let
# $n$ grow, as if you were obtaining larger and larger data sets, then
# $\bar{x}^{(n)}$ will converge to the expected value $E[x]$ of the
# data that you are sampling.

# We will illustrate the LLN using data for the blood pressure values
# for the youngest band of females in NHANES.

ax = dx["Age_strat"].cat.categories[0]
v = dx.loc[(dx["Age_strat"] == ax) & (dx["RIAGENDR"] == 2), "BPXSY1"]

# The following code generates 20 permuted versions of the data in
# 'v', and "cumulatively averages" the data.  For example, if our data
# were [2, 4, 6], then the cumulative averages are [2, 3, 6] -- each
# cumulative average is the regular average of an initial sequence of
# the data values.

n = np.arange(1, len(v)+1)

# Plotting one cumulative average shows us what we might have obtained
# had we recalculated the sample mean each time we obtained data for
# one additional person.  We don't know what the population mean is
# for these data, but the sample mean is converging to a value of
# around 111 for the finite set of data that we have.  According to
# the LLN, if we continued this process with greater values of n, we
# would converge in the limit to the population mean blood pressure
# (for the subpopulation of subjects considered here).

y = np.cumsum(v) / n
plt.clf()
plt.figure(figsize=(8, 6))
plt.grid(True)
plt.plot(n, y, '-', color='black')
plt.xlabel("Sample size")
plt.ylabel("Average value")

# To see what we might have obtained had we sampled the people in our
# study in a different order, we can repeat this process, randomly
# permuting the values for each sample.  You do not need to understand
# the details of the code below.

x = [np.cumsum(np.random.choice(v, len(v), replace=False))/n for _ in range(20)]

# Next we plot each of these random "trajectories" of cumulative
# averages.

plt.clf()
plt.figure(figsize=(8, 6))
plt.grid(True)
for y in x:
    plt.plot(n, y, '-', color='grey', alpha=0.5)
plt.xlabel("Sample size")
plt.ylabel("Average value")

# In the above plot, you can see that all of the sequences of
# cumulative averages seem to be converging to the same limit (we
# cannot actually see the limit since we are working with finite
# samples).  Some "unlucky" trajectories are quite far off even when
# the sample size is 100, but even these unlucky trajectories
# eventually become similar to the others.
