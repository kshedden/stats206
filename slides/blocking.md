% Blocking, power, and hypothesis testing
% Kerby Shedden
% December 1, 2020

Power
=====

In formal statistical testing, there are two types of mistaken
conclusions that can be made:

* We can reject the null hypothesis when the null hypothesis is
correct.  This is called a _false positive_.

* We can accept the null hypothesis when the null hypothesis is
incorrect.  This is called a _false negative_.

The primary goal of formal hypothesis testing is to limit false
positives.  Usually we wish to limit the probability of a false
positive to 5% (in settings where the null hypothesis is true).

---

Power
=====

If the null hypothesis is false, we want to reject it.  The
probability of rejecting the null hypothesis when it is false is
called the _power_.

Power and false positives are in tension with each other.  It is easy
to have high power if we are willing to have a high rate of false
positives.  Limiting the false positive rate, say to 5%, imposes
limits on the power.  These limits can be overcome by collecting more
data, by collecting more informative data, or by analyzing the data
more efficiently.

---

Review of testing to compare two means
======================================

Many hypothesis tests involve comparisons.  For example, we have
previously considered a comparison of means between two populations.
The population means $\mu_1$ and $\mu_2$ may represent, for example,
the mean incomes for people with and without a 4-year college degree.

If we choose to formally test the null hypothesis $\mu_1 = \mu_2$, one
strategy that we may employ is to obtain the incomes for a sample of
people who completed college, denoted $x_1, \ldots, x_m$, and for a
sample of people who did not complete college, denoted $y_1, \ldots,
y_n$.

We can then use the Z-score $T = (\bar{x} - \bar{y}) /
(\hat{\sigma}_x^2/m + \hat{\sigma}_y^2/n)^{1/2}$ as a test statistic.
If $T > 2$ we can reject the null hypothesis that $\mu_1 = \mu_2$.

---

Blocking
========

When comparing two groups, e.g. people with and without college
degrees, there are many other sources of variation besides the primary
factor of interest.  This can include confounders, e.g. people with
college-educated parents are more likely to go to college, as well as
factors that influence the outcome but that do not associate with
group membership.

One strategy for improving statistical power is to reduce the
influence of such "extraneous" variables by optimizing the manner in
which we collect the data.  "Blocking" is a way to achieve this.

---

Paired testing
==============

A concrete example of blocking is to collect data from "discordant
pairs".  For example, when considering the relationship between
college education and adult income, we may try to locate siblings
where one individual attends college and one does not.

Let $x_i, y_i$ denote the adult incomes for the $i^\textrm{th}$
discordant sibling pair, with $x_i$ denoting the income for the
sibling who completed college, and $y_i$ denoting the income for the
sibling who did not.

These data can be reduced to the differences $d_i = x_i - y_i$.  The
null hypothesis that there is no difference in adult incomes between
the two groups can be expressed $E[d] = 0$.

By directly comparing siblings, we are "controlling" for factors such
as parental education and income that are potential confounders,
and that are shared by both siblings.

To obtain a test statistic for this hypothesis, we can start with the
sample mean $\bar{d}$.  The standard error for $\bar{d}$ is the SEM
$\hat{\sigma}/n^{1/2}$.  The test statistic is the Z-score
$\bar{d}/\textrm{SEM}$ $= n^{1/2}\bar{d}/\hat{\sigma}$.

---

Paired testing
==============

Paired testing is an approach that is available whenever discordant
pairs can be obtained.  Another example would be an agricultural
experiment where we are comparing the yields of two varieties of a
crop, call them types A and B.

Factors such as soil quality, sunlight, and moisture vary by location.
To reduce these effects, we can divide the study area into plots,
subdivide each plot in half, and randomly plant crop A in one of the
half plots and crop B in the other half plot.

Here we let $x_i$ and $y_i$ denote the yield for plants, with $x_i$
denoting the yield for a plant of type A and $y_i$ denoting the yield
for a plant of type B, with the subscript $i$ denoting the plot
consisting of two adjacent sub-plots.

As above, we set $d_i = x_i - y_i$ and conduct a test using the test
statistics $T = n^{1/2}\bar{d} / \hat{\sigma}$.

---

Stable confounders
==================

One way to understand why blocking may improve performance is to
consider a possible "model" for the data.

Suppose that $c = E[d]$ is the true difference between incomes of
people who attend and who do not attend college.

A _stable confounder_ is a variable, denoted $u_i$ below, that effects
the incomes of two siblings, but is shared between them.  We also
introduce variables $e_{i1}$ and $e_{i2}$ that influence the incomes
of each individual uniquely.

A model for the data could be:

$x_i = c + u_i + e_{i1}$

$y_i = u_i + e_{i2}$

Note that when we form the difference $d_i = x_i - y_i$, the $u_i$
cancel out and we get $d_i = c + e_{i1} - e_{i2}$.

The fact that the $u_i$ cancel out of the difference here is what
improves our power.

---

Paired versus unpaired testing
==============================

When data appear to have a discordant pairs structure, we have
the option to analyze it using the pairs, or ignoring the pairs.

If ignoring the pairs, we use the unpaired test statistic $(\bar{x} -
\bar{y})/(\hat{\sigma}_x^2/n + \hat{\sigma}_y^2/n)^{1/2}$.

If using the pairs, we use the paired test statistic
$\bar{d}/(\hat{\sigma}/n^{1/2})$.

The numerator of these two statistics is the same, since $\bar{d} =
\bar{x} - \bar{y}$.  However the denominators are different.

In most cases in practice, $\hat{\sigma}/n^{1/2} < (\hat{\sigma}_x^2/n
+ \hat{\sigma}_y^2/n)^{1/2}$, i.e. the standard error for the paired
statistic is smaller than the standard error for the unpaired
statistic.

This means that the paired statistic will be larger than the unpaired
statistic.  A larger statistic is more like to reach a threshold for
"statistical significance", e.g. to achieve $T>2$.