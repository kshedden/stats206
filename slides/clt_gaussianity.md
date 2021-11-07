% Large sample approximations
% Kerby Shedden
% October 12, 2020

The _Gaussian_ or _normal_ distribution is a probability distribution
on the real line.

It is not described by a probability mass function, instead
it is described by a _probability density function_ (pdf)
as depicted below:

![](/~kshedden/introds/images/norm1.svg)

The density function is higher at a point $x$ when it
is more likely to observe values near $x$.

---

Gaussian distribution
=====================

The Gaussian distribution is not a single distribution.
It is a family of distributions indexed by the mean $\mu$
and the variance $\sigma^2$.  There exists a Gaussian
distribution for every $\mu$ and for every $\sigma^2>0$.

Several Gaussian distributions are shown below:

![](/~kshedden/introds/images/norm2.svg)

All Gaussian distributions share the same shape.  There is a
single point where the density is greatest, and the density
diminishes in the same way on either side of this peak,
giving a symmetric "bell curve".

---

Empirical rule
==============

The Gaussian distribution satisfies the "68-95-99" empirical
rule, stated more precisely as follows:

* The probability of
observing a value within one standard deviation of the mean is
approximately 0.68

* The probability of observing a value within
two standard deviations of the mean is approximately 0.95

* The probability of observing a value that is within three standard
deviations of the mean is approximately 0.997.

The empirical rule links moments (mean and standard deviation) to
probabilities.

---

Tail probabilities
==================

For any distribution, the probability of observing
a value falling $c$ or more standard deviations ($\sigma$) away from
the mean ($\mu$)
is called a _tail probability_, and can be denoted $P(|X-\mu| > c\sigma)$.

The tail probabilities diminish as $c$ increases.
But the exact tail probabilities
depend on the distribution.  The Gaussian distribution
is "light tailed" so the tail probabilities diminish quite
quickly with increasing $c$.

---

Empirical rule example
======================

Suppose we have data that follow a Gaussian distribution with
mean $\mu=130$ and standard deviation
$\sigma=12$.  We are very unlikely to observe
a value smaller than $94 = \mu-3\sigma$ or larger
than $166 = \mu+3\sigma$.

Specifically, only
around 3 out of 1000 values would be expected to fall in these
regions.

The empirical rule reflects the fact that the Gaussian
distribution has thin tails, so most of its mass falls within 3
standard deviations of its expected value.  Extreme values are very
seldom seen for the Gaussian distribution.

---

Tail probabilities for non-Gaussian distributions
=================================================

The empirical rule only holds for the Gaussian distribution.  For
other distributions, these probabilities may be smaller, or larger.

_Chebyshev's inequality_ states that for a large class of
distributions, $P(|X-\mu| > c\sigma) \le 1/c^2$.  This is an inequality
rather than an exact value, since the exact value depends on
the distribution.

Setting $c=3$
we get $1/c^2 = 1/9 \approx 0.11$.  Thus, for a non-Gaussian distribution,
up to 11% of the values can fall more than 3 standard deviations
from the mean, while in a Gaussian distribution only $1 - 0.997 = 0.003$,
or 0.3% of the values can fall more than 3 standard deviations
from the mean.

---

Uses of the Gaussian distribution
=================================

Most data do not follow the Gaussian distribution.  It is
generally not a good model for data.

Many variables of interest such as household income
and blood pressure values are skewed.  Since the Gaussian
distribution is not skewed, it cannot fit these types
of data very well.

Even measurements that have an approximate symmetric distribution
often do not fit a Gaussian distribution very well.

The Gaussian distribution is mainly of interest because
it describes the "errors" that result when using the sample
to estimate a parameter of the population.

It is not necessary or important that the measured data
values being analyzed fit a Gaussian distribution.

---

Central limit theorem
=====================

The central limit theorem (CLT) describes the probability distribution
of the sample mean.

The sample mean is a random quantity, because it is constructured using
data that are themselves random.  If we draw a new sample and recompute the sample
mean, we will get a new sample mean.

The CLT states that the distribution of the sample mean will be approximately
Gaussian, even if the individual data values are not Gaussian.

There are some unusual situations where the CLT does not apply.  We will not
consider this further in this course.

---

Distribution of the sample mean
===============================

In practice, we observe a sample consisting of
many data values, and can observe
the distribution of these values directly (in approximate form), e.g.
through a histogram or boxplot.

In general we only observe one value of the sample mean.  There
is no way to even approximately visualize the distribution
of the sample mean from the data alone.

The CLT provides us with theory-based insight into the
distribution of the sample mean (namely that it is
approximately Gaussian).

---

Distribution of the sample mean
===============================

Knowing that the distribution of the sample mean
is Gaussian allows us to infer how likely it is
for the sample mean to fall close to the population
mean.

Suppose we are interested in the
population mean of blood glucose levels
for people with BMI greater than 30.
To accomplish this, we obtain a sample of people with BMI over 30,
measure their blood glucose levels, and
obtain a sample mean value of 31.  By the CLT,
this sample mean approximately follows a
Gaussian distribution.

Note that we only obtain one value for the sample mean -- 31.
Given this one number, there is no way to assess what its
distribution looks like.  The CLT tells us that its distribution
is approximately Gaussian.

The CLT does not tell us which Gaussian distribution our
sample mean follows.  However based on the way in which the
data were collected, we can usually infer the value of
$\sigma$, the standard deviation of the Gaussian distribution that
describes our sample mean.

For example, if we knew that
the Gaussian distribution describing the behavior of our sample
mean has a standard deviation
of 1.3, then it is very unlikely that the population
mean and sample mean are more than $3\cdot 1.3 = 3.9$
units apart.

---

Aggregation and asymptotic normality
====================================

The CLT applies directly to the sample mean.  However similar
results apply to many other statistics.

The key to the CLT is that when we aggregate (combine) a lot of data,
the aggregated value behaves more Gaussian than the individual values
do.

Many other statistics, such as the sample median and sample standard deviation,
behave approximately like Gaussian random variables, as long as the
sample size is sufficiently large.  This is called _asymptotic normality_.

Many formal procedures in statistics are based on asymptotic normality.
As we will soon see, we often need to know how far a statistic
may fall from its population analogue.  Knowing that the distribution
of the statistic is approximately Gaussian makes it possible to do this.