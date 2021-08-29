% Confidence intervals
% Kerby Shedden
% November 16, 2020

Review of notation and terminology
==================================

An _estimate_ in statistics is a value calculated from the data that
is intended to fall close to a particular value of interest called the
_estimand_, _population parameter_, or _population target_.

Since estimates are calculated from data, they are random, just as the
data are.  Recall that something is "random" in this sense if it
changes every time we repeat the collection of our data.

The estimate is written with a "hat" over it, so if $\alpha$
represents a population target, then $\hat{\alpha}$ denotes an
estimate of $\alpha$.

The _estimation error_ $\hat{\alpha} - \alpha$ is a random quantity
and occasionally can be quite large (we never know how big the
estimation error is because although we observe $\hat{\alpha}$, we
never know $\alpha$).

We commonly are interested in estimating the expected value $\mu$
using the sample mean $\bar{x}$.  In this case, the population
parameter is $\alpha = \mu$, and the estimator is $\hat{\alpha} =
\bar{x}$.

---

Review of notation and terminology
==================================

There are two sources of statistical uncertainty -- _bias_ and
_variance_.  Bias represents the systematic part of the estimation
error, and variance represents the random part of the estimation
error.

The bias is the expected value of the estimation error.  Often (but
not always) the bias is zero.  For example, if our data are
independent and identically distributed, and they represent the
population of interest, then the sample mean $\bar{x}$ is unbiased for
the expected value $\mu$.

The variance is most often represented through the standard error,
which is the standard deviation of the estimate $\hat{\alpha}$.

Most estimates are approximately Gaussian and therefore approximately
follow the empirical rule.  Thus, the estimation error has 68%, 95%,
and over 99% probabiilty of being less than one, two, and three
standard errors in magnitude, respectively.

---

Confidence intervals
====================

A confidence interval (CI) is a way of expressing what the empirical
rule and standard error tell us about random estimation error.

A confidence interval is an interval $(a, b)$, with lower and upper
confidence limits $a$ and $b$ respectively.  It is constructed based
on the data, and thus has a certain probability of containing the
estimand.  This probability is called the _coverage probability_.

The coverage probability is a value under our control that we can set
to any number between 0 and 1.  The width of the confidence interval
$b-a$ will become larger if you choose a greater value for the
coverage probability, and will be smaller if you choose a smaller
value for the coverage probability.

While it is desirable to have a high coverage probability, achieving
very high coverage probability requires using very wide intervals.  At
the extreme, a coverage probability of 1 can only be obtained with an
interval that is infinitely wide: $(-\infty, \infty)$.

---

Constructing confidence intervals based on the empirical rule
=============================================================

If our statistic is approximately Gaussian, the empirical rule gives
us a way to construct confidence intervals with coverage probabilities
equal to 68%, 95%, and 99%.

The estimate plus or minus one estimated standard error constitutes a
68% confidence interval.  For the sample mean, this interval has the
form $(\bar{x}-\hat{\sigma}/n^{1/2}, \bar{x}+\hat{\sigma}/n^{1/2})$.

The estimate plus or minus two estimated standard errors constitutes a
95% confidence interval.  For the sample mean, this interval has the
form $(\bar{x}-2\hat{\sigma}/n^{1/2}, \bar{x}+2\hat{\sigma}/n^{1/2})$.

A 99% confidence interval can be constructed using multiples of three
standard errors.

In all of these intervals, the sample mean $\bar{x}$ sits at the
center of the interval.

For historical reasons, 95% confidence intervals are most commonly
used, but this convention is arbitrary.

---

Interpretation of confidence intervals
======================================

A confidence interval is a way to communicate about the uncertainty in
a statistical estimate.  If we report that the average household
income in a given US county is 71 (thousand USD), with a 95%
confidence interval $(69, 73)$, this tells us something about the
limits of the precision in our knowledge about the population mean.

The confidence interval is likely to contain the population mean, and
any value within the confidence interval represents a possible value
for the population mean that is consistent with ("fits") the observed
data.  Values outside the confidence interval are less consistent with
the observed data, but still may possibly be the true value of the
population mean.

---

Interpretation of confidence intervals
======================================

Three important points to note:

* The 95% confidence interval for the mean does not contain 95% of
the data (it contains a much lower fraction of the data than 95%).

* The confidence interval is not guaranteed to contain the population
mean.

* The population mean is not equally likely to be any value within the
confidence interval.  It is more likely to be near the center of the
interval.

* The "fitness" of a possible value for the population mean does not
suddenly drop once it crosses the edge of the CI.  Values near the
center of the interval are the most fit, and the fitness drops
continuously as a value moves away from the center.

---

Confidence intervals are random
===============================

It is important to note that confidence intervals are random objects.
Every time we collect data, we get a different CI.

The target that these intervals are aiming to cover remains
fixed, and repeated samples of data result in intervals that
"bounce around" the target value.

Thus, when we say, "what is the probability that the expected value
$\mu$ falls in the confidence interval", the probability is describing
the random behavior of the interval, not of $\mu$.

If we are working with 95% confidence intervals, and if we were to
repeat our study 20 times for the same population, then we would
expect 19 of the 20 intervals to cover the target, and 1 of them to
miss the target.

---

Width of the confidence interval
================================

The 95% confidence interval has a width -- for any interval $(a, b)$,
the width is $b - a$.

Since our confidence intervals are random, their widths are random.
The width of a CI is related to the information in the data about the
population parameter of interest.

If we are forming an interval for the expected value:

* The confidence interval will tend to be narrower if it is based on a
larger sample size.

* The confidence interval will tend to be wider if the dispersion of
the data ($\sigma$) is greater.

* The confidence interval will tend to be wider if the coverage
probability is greater.

---

Designing a study for confidence interval width
===============================================

In some situations, a primary aim when desiging a study
is to have a sufficiently narrow CI.

The width of the 95% CI for the mean is $4\sigma/n^{1/2}$.

Suppose we anticipate that $\sigma \approx 2$, and wish
to have the width of the CI be 0.5.  Then we should solve
the equation

$8/n^{1/2} = 0.5$

to get a sample size of $n=256$.

---

Confidence intervals for parameters other than the mean
=======================================================

We can use the empirical rule to construct confidence intervals for
any statistic as long as we have a standard error, and the statistic
follows the empirical rule.

We can construct a 95% confidence interval for the proportion:

$(\bar{x} - 2(\bar{x}(1-\bar{x})/n)^{1/2},
\bar{x} + 2(\bar{x}(1-\bar{x})/n)^{1/2})$

and a 95% confidence interval for a correlation coefficient
$r$:

$(r - 2/n^{1/2}, r + 2/n^{1/2})$.

---

Confidence intervals for differences
====================================

In many cases the goal may be to estimate the difference between two
quantities, rather than estimating a single quantity.

As we have seen, if two quantities have standard errors $s_1$ and
$s_2$, then the standard error for the difference between the two
quantities is $(s_1^2 + s_2^2)^{1/2}$.

For example, if we wish to estimate the difference between the mean
household incomes in Michigan and Ohio, we can calculate these means
as $\bar{x}$ and $\bar{y}$, and take their difference $\bar{x} -
\bar{y}$.

The standard error for this difference is $(\sigma_m^2/n_m +
\sigma_o^2/n_o)^{1/2}$, where $\sigma_m$ and $n_m$ are the standard
deviation of the data for Michigan and the sample size for Michigan,
while $\sigma_o$ and $n_o$ are the corresponding values for Ohio.

The estimated standard error for the difference between the mean
Michigan and Ohio incomes is $\hat{s} = (\hat{\sigma}_m^2/n_m +
\hat{\sigma}_o^2/n_o)^{1/2}$, so a 95% confidence interval for the
difference between the two mean household incomes is

$(\bar{x} - \bar{y} - 2\hat{s}, \bar{x} - \bar{y} + 2\hat{s})$.

---

Confidence intervals and nuisance parameters
============================================

Many confidence intervals depend on nuisance parameters, i.e.  values
that we must estimate in order to estimate the standard error.  For
example, if comparing the household incomes in Michigan and Ohio,
we must estimate the standard deviations $\sigma_m$ and $\sigma_o$.

If we estimate and "plug-in" these standard deviations, the resulting
interval becomes approximate.  It will generally have slightly lower
coverage probability than what is given by the empirical rule.  For
large sample sizes, the reduction of the coverage probability is very
small, but for small sample sizes it is considerable.

There are ways to compensate for this, but we do not consider them
here.

---

Defective confidence intervals
==============================

Many confidence intervals are approximate in some way, for example:

* The confidence interval may use an approximate standard error (like
the approximate standard error $1/n^{1/2}$ for the correlation
coefficient).

* The confidence interval may use a standard error with a nuisance
  parameter.

* The sample size may be small so that the empirical rule is
  approximate.

* The data may have been collected in a way that makes them
independent and identically distributed.

In these cases, the coverage probability implied by the empirical rule
may not be the actual coverage probability.  For example, the
empirical rule may suggest that an interval will have 95% coverage
probability, but in reality it only has 88% coverage probability.

In this setting, the desired coverage probability is called the
"nominal" coverage probability, and is usually greater than the
"actual" coverage probability.