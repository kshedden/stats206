% Information and sample size
% Kerby Shedden
% October 28, 2020

Statistical estimation and population parameters
================================================

In a general framework for statistical estimation, we have
two related but different quantities:

__Statistic__: a numerical summary calculated from data

__Population parameter__: a numerical summary of a population

The process of collecting data is random -- we can at least
in principle replicate our data collection, and every time
we do so we get a different dataset.

Since the data are random, anything derived from the data is
random, so in particular a statistic derived from the data
is random.

Population parameters, in contrast, are fixed values.

---

Estimation and population parameters
====================================

Most statistics _estimate_ or "target" a population parameter, called
the _population analogue_ of the statistic.

Most population parameters can be estimated by one or
more (often many) statistics.

In most cases, the goal of calculating a statistic is to estimate
its corresponding population parameter.

For example:

* The sample mean (average) of the data estimates the population mean.

* The sample variance (average of squared deviations from the mean)
estimates the population variance.

* The proportion of the data values that are less than or equal
to 2 (a left tail probability) estimates the probability (according
to the population) of observing a value that is less than or equal
to 2.

* The sample 90th percentile estimates the population 90th percentile.

---

Sampling distributions
======================

Since the statistic (i.e. the estimate) is random, it has its own probability
distribution.  For example, if the data $x_1, \ldots, x_n$ have a
distribution, then the sample mean $\bar{x}$ also has a distribution.

If we have an identically distributed sample of data, we can
(approximately) see the distribution of the data directly
(e.g. by making a histogram
of the data values).  We cannot see the distribution of a statistic,
since we only observe a single value of the statistic.

In general, we can only learn about the distribution of a statistic
by considering its properties from a theoretical perspective.

The probability distribution of a statistic is called its _sampling distribution_,
since this distribution reflects the behavior of the statistic when
repeatedly sampling datasets from the population.

---

Bias and the mean of the sampling distribution
==============================================

Since a statistic is random, it follows a probability
distribution.  Like any other distribution, the distribution
of a statistic has a location, a dispersion, and other characteristics.

In particular, the probability distribution of a statistic has
an expected value.  For example, if the statistic is
the sample mean, the expected value of its sampling
distribution can be denoted $E\bar{x}$.

Suppose that the data are independent and identically
distributed, and have mean $\mu$, that is, $Ex_i = \mu$
for every index $i$.  In this case, the statistic also
has mean $\mu$.  In words, $E\bar{x} = \mu$.

When the expected value of the statistic is equal to
the population parameter that it aims to estimate,
the statistic is said to be _unbiased_.

Here we see that the sample mean is an unbiased estimate
of the population mean, as long as the data are IID.

Many, but not all commonly-used statistics are unbiased,
at least if the data are IID.

---

Bias in estimation
==================

Some estimators are unbiased as long as the data are IID.
This is true of the mean and all quantiles.

However these estimators can become biased if the data
are not IID.  Also, sometimes the data are sampled in
such a way that they are IID and have an expected value
$\mu$ that is not the value of interest.  In this case,
we may get bias.

For example, suppose that we wish to know the average number of steps
walked per day by American adults, and we sample in a
way such that young people are systematically under-represented.
If young people take more steps per day than older people,
then our statistic will be biased (downward) due to the way that the
data were collected.

---

Bias in estimation
==================

Some statistics are biased even if the data are IID and are
representative of the population of interest.

For example, suppose we wish to estimate the ratio of
the expected income $\mu_c$ for college graduates
to the expected income $\mu_h$ for high
school graduates.

That is, our parameter of interest is $\mu_c/\mu_h$.

We collect IID data for college graduates $x_1, \ldots, x_n$,
and IID data for an independent set of high school
graduates $y_1, \ldots, y_n$.  Then it is natural to
estimate the parameter of interest using $\bar{x}/\bar{y}$.

However this estimate is biased -- even though $\bar{x}$
is unbiased for $\mu_c$ and $\bar{y}$ is unbiased for
$\mu_h$, $\bar{x}/\bar{y}$ is not unbiased for $\mu_c/\mu_h$.

---

Dispersion in sampling distributions
====================================

In most cases, the distribution of a statistic derived from many
data points is less dispersed than the data values themselves.

That is, the sampling distribution is less dispersed than the distribution
of the data.

A special case of this fact is that when we have an independent and
identically distributed (IID) sample, the dispersion of the sample mean,
measured using the variance, can be directly related to the dispersion
of the data.

If the data $x_1, \ldots, x_n$ have variance $\sigma^2$, then the sample mean $\bar{x}$
has variance $\sigma^2/n$.

* The more dispersed the data are, the more dispersed is the sampling distribution
of the sample mean (since both have a factor of $\sigma^2$).

* The larger the sample size, the less dispersed is the sampling distribution of
the sample mean (since it has a factor of $n$ in its denominator).

The quantity $\sigma^2/n$ is called the _sampling variance of the sample mean_.

---

Dispersion in sampling distributions
====================================

Just as the standard deviation $\sigma$ is the square root of the variance
of the data ($\sigma^2$), the
_standard error_ of a statistic is the square root of its sampling variance.

Thus, if the statistic we are working with is the mean $\bar{x}$, then the standard
error of the mean (SEM) is $\sigma/n^{1/2}$.

* The standard error of the mean is directly proportional to the standard deviation
of the data (both include a factor of $\sigma$).

* The standard error of the mean scales as "root n" of the sample size, i.e. it
has a factor of $n^{1/2}$ in its denominator.

A key consequence of these observations is that if we want to reduce the standard
error of the mean by a factor of 2, we need to increase the sample size $n$
by a factor of 4, or decrease $\sigma$ by a factor of 2 (but usually it
is not possible to change $\sigma$).

---

Estimation error
================

The _estimation error_ is the difference between the value of a statistic
and the population parameter that it estimates.

For the sample mean, the estimation error is $\bar{x} - \mu$, since the
sample mean is (usually) taken to be an estimate of the population mean
$\mu$.

The estimation error is random, since it depends on the statistic, which
is random.

We always want the estimation error to be small.  But in practice,
the estimation error will never be zero, and in rare cases it may
be quite large.

In order to quantify the
uncertainty in our estimates, we need to have an understanding of
how large the estimation errors tend to be.

---

Standard errors and the empirical rule
======================================

Due to the CLT, the sample mean (as well as many other statistics obtained
by aggregating data) approximately follows a normal distribution.

If the data are IID, we know that this distribution has mean $\mu$ (the
mean of the data values), and it has standard deviation $\sigma/n^{1/2}$.

It follows that the estimation error $\bar{x} - \mu$ has mean zero, and
also has standard deviation $\sigma/n^{1/2}$.

Since the sample mean is approximately Gaussian, it (approximately)
follows the empirical rule.

Therefore there is a 95% probability that the estimation error is
within two standard deviations of its mean value.  That is, 95% of the time
the estimation error is smaller than $2\sigma/n^{1/2}$, and more than 99%
of the time the estimation error is smaller than $3\sigma/n^{1/2}$.

---

Statistics other than the mean
==============================

The basic version of the CLT only applies to the sample mean,
but many other statistics besides the sample mean also
(approximately) behave in a Gaussian manner.

However, there is often no simple formula that gives us
the sampling distribution of a statistic (except for the sample mean).

Next we consider a few other statistics where exact or approximate standard
errors are available.

---

Proportions
===========

A proportion is actually just a mean.  For example, suppose we are interested
in the proportion of values from a particular distribution that are less
than 1, which we can write $p = P(X < 1)$. This is equivalent to taking the mean of the
_indicator function_ $Y$, which
which is defined to be equal to 1 if the value that we observe is less than 1,
and is defined to be equal to 0 otherwise.

The indicator function is sometimes written $Y = I(X<1)$.

Analogously, if we have data $x_1, \ldots, x_n$, then
we can create new data $y_i = I(x_i < 1)$ (so that $y_i=1$ if $x_i<1$ and $y_i=0$
if $x_i\ge 1$).  The average value $\bar{y}$ is a statistic that estimates $P(X < 1$).

The variance of each $y_i$ is $p(1-p)$, where $p=P(X<1)$ is the population
parameter (we won't derive this fact in this class).

Thus the standard error of the estimated proportion is
$(\sigma^2/n)^{1/2} = (p(1-p)/n)^{1/2}$.

---

Other statistics
================

Some statistics, such as quantiles, have standard errors that
are quite difficult to obtain.  This is one of the reasons
that quantiles are used less extensively in some parts of
statistics compared to moments.

Sometimes, a complex statistic has a surprisingly simple
standard error (at least in approximate form).  The sample
correlation coefficient has standard error that is roughly
equal to $1/n^{1/2}$ (there are better approximations than
this one, but they are more complicated).

Many statistics, even those that do not have an easily-obtained
standard error, continue to exhibit the same "root n" scaling
as the sample mean.  That is, we know that the standard error
is reduced by a factor of 2 when the sample size is increased
by a factor of 4, even though we cannot calculate the
standard errors.

---

Law of large numbers
====================

The _law of large numbers_ (LLN) is a theorem that characterizes
what happens to a statistic when it is calculated with
increasingly large datasets.

We will not state the theorem precisely here, but will
consider it in intuitive terms.

The LLN essentially says that for most statistics that are
based on IID data, the value of the statistic converges
to its expected value as the sample size grows.

Thus, if the statistic is unbiased, the value of the statistic
is guaranteed to become arbitrarily close to the population
parameter, as long as enough data is collected.