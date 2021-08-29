% Standard errors
% Kerby Shedden
% November 1, 2020

Review of terms
===============

In statistics, our goal is usually to estimate a characteristic or
parameter of the population, which may be called the _estimand_.  To
achieve this goal, we use a statistic that is derived from our sample
of data.

If $\alpha$ is the estimand, then a statistic that estimates $\alpha$
will generally be denoted $\hat{\alpha}$ (the "hat" indicates that it
is an estimate).

The estimate is a function of the data $x_1, \ldots, x_n$.  To
emphasize this, we may write the estimate as $\hat{\alpha}(x_1,
\ldots, x_n)$.

The _estimation error_ is $\hat{\alpha} - \alpha$, the _bias_ is
$E\hat{\alpha} - \alpha$, and the _standard error_ is
$\textrm{SD}(\hat{\alpha})$.

---

Estimation of the population mean
=================================

If our goal is to estimate the population mean, then the estimand is
denoted $\mu$, and the estimator is $\bar{x}$, the average or sample
mean of the data.

The standard error in this case is also known as the standard error of
the mean, $\sigma/n^{1/2}$, where $\sigma$ is the sample size.

Since $\bar{x}$ is unbiased for $\mu$, the estimation errors have
expected value zero, and standard deviation $\sigma/n^{1/2}$.

By the central limit theorem (CLT), the sample mean is approximately
Gaussian.  Therefore, the estimation errors $\bar{x} - \mu$ are
approximately Gaussian and follow the "empirical rule".  Thus,
$\bar{x}$ will fall within $2\sigma/n^{1/2}$ of the estimand $\mu$ at
least 95% of the time, and will fall within $3\sigma/n^{1/2}$ of $\mu$
at least 99% of the time.

---

Estimated standard errors
=========================

The standard error of the mean is $\sigma/n^{1/2}$.  When conducting a
data analysis involving estimation of a population mean, it would be
useful to know this value in order to help us assess how precise our
estimate $\bar{x}$ is.

We almost always know the value of $n$ (the number of data values),
but we almost never know the value of $\sigma$ (the standard deviation
of the data).

A statistic that is not our primary value of interest, but that is
needed to assess the uncertainty in our estimate of a primary value of
interest, is called a _nuisance parameter_.  Thus, $\sigma$ is a
nuisance parameter.

We have an estimate $\hat{\sigma}$ of $\sigma$ (the sample standard
deviation of the data).  If we use $\hat{\sigma}$ in place of $\sigma$
to estimate the SEM as $\hat{\sigma}/n^{1/2}$, we are "plugging in" an
estimate of the nuisance parameter.  This is a very common strategy in
statistical inference.

---

Analyses involving single estimands
===================================

Some statistical analyses involve a single parameter that is of direct
interest:

* The proportion of the public that support a particular policy

* The proportion of people receiving a vaccine who nevertheless get
the disease that the vaccine is intended to prevent

* The physical force that can be applied to a sheet of glass before it
breaks

---

Analyses involving comparisons
==============================

However many statistical analyses involve comparisons between two
quantities, each of which must be estimated.  Some examples of this
situation are

* The difference between the proportions of people over 50 and under
50 who support a particular policy

* The difference between the proportions of people receiving two
different vaccines who nevertheless get the disease that the vaccines
are intended to prevent

* The difference between the force that can be applied to sheets of
two different types of glass before they break

---

Analyses involving comparisons
==============================

When conducting an analysis involving a difference, we must estimate
two quantities.  For now these estimates will be independent (later we
will consider the setting where they are not independent).

Suppose we test 10 pieces of glass of type A, and obtain the force (in
pounds per square inch, PSI), under which each piece breaks.  Denote
these data $x_1, \ldots, x_{10}$, and suppose that $\bar{x} = 73$.

Then we test 20 pieces of glass type B, and obtain the same results
for these pieces, which we denote $y_1, \ldots, y_{20}$.  Suppose that
$\bar{y} = 64$.

The population parameter of interest is $\mu_x - \mu_y$, where $\mu_x$
and $\mu_y$, respectively, are the population means for glass type A
and glass type B.

The difference between the two sample means is $73 - 64 = 9$.  It
appears that glass of type A is able to withstand 9 PSI more force
than glass of type B.

But there is uncertainty in both sample means (73 and 64) that are
being subtracted.  Our goal is to obtain an estimate of the "total
error" in this difference.

---

Analyses involving comparisons
==============================

Suppose that the measurements for glass type A have an estimated
standard deviation ($\hat{\sigma}$) of 9 PSI, and the measurements for
glass type B have an estimated standard deviation of 7 PSI.

Then the estimated standard error of $\bar{x}$ (its SEM), is
$9/10^{1/2} = 2.85$.

The estimated standard error of $\bar{y}$ is $7/20^{1/2} = 1.57$.

The estimated standard error for the difference $\bar{x} - \bar{y}$ is

$(2.85^2 + 1.57^2)^{1/2} = 3.25$.

We can now apply the empirical rule to the difference $\bar{x} -
\bar{y}$, and conclude that the observed difference is very likely
(more than 95% likely) to be within $2\cdot 3.25 = 6.5$ of its target,
$\mu_x - \mu_y$.

---

Analyses involving proportions
==============================

As noted earlier, proportions are means of indicators that are coded
as 0 and 1.  Suppose we are interested in the proportion of people who
support a tax on sugary drinks.  We obtain a sample of people and ask
them about this issue.  If person $i$ supports the tax then $x_i=1$,
otherwise $x_i=0$.

The proportion of people in the sample who support the tax is
$\bar{x}$, and the standard error for this proportion is
$(p(1-p)/n)^{1/2}$, where $p$ is the true proportion of people who
support the tax in the population.

We don't know $p$, so we can estimate the standard error for the
proportion as $(\bar{x}(1-\bar{x})/n)^{1/2}$.

Now suppose that the people in the sample of $x_i$ are all from
California, and we ask the same question for a sample of people $y_1,
\ldots, y_m$ from New York.  The proportion of the New York sample who
support the tax is estimated by $\bar{y}$, the corresponding true
proportion can be denoted $q$, and the standard error is
$(q(1-q)/m)^{1/2}$.

The estimated standard error for the California sample is
$(\bar{y}(1-\bar{y})/m)^{1/2}$.

---

Analyses involving proportions
==============================

If we are interested in the difference between the proportions in
California and New York, the estimated value of this difference is
given by $\bar{x} - \bar{y}$.

Suppose we observe $\bar{x} = 0.48$ and $\bar{y} = 0.41$, and the
sample sizes are $n=100$ and $m=200$.  The estimated difference in
support for the tax between the two states is $0.48 - 0.41 = 0.07$.
The standard error for this difference is estimated to be

$(0.48\cdot 0.52/100 + 0.41\cdot 0.59/200)^{1/2} \approx 0.06$

Thus, the observed difference 0.07 is unlikely to be more than
$2\cdot 0.06 = 0.12$ different from the true difference.

---

Z-scores of statistics
======================

The standard error $s$ of a statistic $\hat{\alpha}$ tells us about
the typical size of the estimation error $\hat{\alpha} - \alpha$.

In some settings, we have a reference point $\alpha_0$ to which we
want to compare the statistic.  In this case, it is helpful to know
how far the estimate $\hat{\alpha}$ falls from the reference point
$\alpha_0$ in units of standard errors.

This quantity is given by the Z-score $(\hat{\alpha} - \alpha_0) / s$.

This is related to, but different than the Z-score of the data, which
is obtained by subtracting an estimate of location from each data
value and then dividing by an estimate of dispersion.

---

Z-scores of statistics
======================

__Example__: Suppose we are assessing whether a coin is fair, meaining
that when flipped it is equally likely to produce a head or a tail.
The statistic $\hat{\alpha}$ here can be the proportion of heads
obtained in $n$ independent flips, the reference point is
$\alpha_0=1/2$, and the standard error is
$s=(\hat{\alpha}(1-\hat{\alpha})/n)^{1/2}$.  The Z-score is
$(\hat{\alpha} - \alpha_0)/(\hat{\alpha}(1-\hat{\alpha})/n)^{1/2}$.

__Example__: Suppose we are comparing the exected number of minutes of
nightly sleep betweeen two populations.  We obtain IID data from each
population and form sample means $\bar{x}$ and $\bar{y}$.  The
statistic of interest is the difference $\bar{x}-\bar{y}$, and the
reference point is zero.  The standard error is $(\hat{\sigma}_x/n_x +
\hat{\sigma}_y/n_y)^{1/2}$, where $n_x$ $n_y$, $\hat{\sigma}_x$,
$\hat{\sigma}_y$, are the sample sizes and estimated standard
deviations for the two populations.  The Z-score is
$(\bar{x}-\bar{y})/(\hat{\sigma}_x/n_x + \hat{\sigma}_y/n_y)^{1/2}$.