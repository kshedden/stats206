% Hypothesis tests
% Kerby Shedden
% November 16, 2020

Scientific and statistical hypotheses
=====================================

Along with standard errors and confidence intervals, _hypothesis
testing_ is one of the most widely-used techniques in formal
statistical inference.

Statistical hypothesis testing is inspired by the _empirical approach_
to scientific research in which theories are proposed that may be
_falsified_ by certain observations.  For example, the theory that
cancer is always caused by damage to the DNA would be falsified if a
form of cancer were identified in individuals with no DNA damage.

Statistical hypothesis testing often starts with a hypothesis that we
wish to falsify (or _reject_) called the _null hypothesis_.  The null
hypothesis usually states that a certain relationship is absent in the
population.  If we then observe data that contradicts the null
hypothesis, we have provided evidence that this relationship is in
fact present.

Example: if we suspect that poor sleep is associated with high blood
pressure, we may conduct a study in which data on sleep habits and
blood pressure are collected.  The null hypothesis may be that the
correlation coefficient between sleep and blood pressure is zero.

---

Comparing two expected values
=============================

Many interesting statistical hypotheses involve comparisons.  In
particular, it is extremely common that we wish to compare two
expected values.

Suppose for example that we wish to assess whether people who take
daily aspirin have lower levels of C-reactive protein (CRP), a
biomarker for poor cardiac health, compared to people who do not take
daily aspirin.

The population mean level of CRP among people who take daily aspirin
may be denoted $\mu_1$.  The population mean level of CRP among people
who do not take daily aspirin may be denoted $\mu_2$.  An appropriate
null hypothesis here is that $\mu_1 = \mu_2$.

To assess this hypothesis, we can collect data (ideally in an iid
manner) from people who take daily aspirin, yielding CRP values $x_1,
\ldots, x_m$.  Similarly, we can collect data from people who do not
take daily aspirin, yielding CRP values $y_1, \ldots, y_n$.

---

Comparing two expected values
=============================

We can form sample means $\bar{x}$ and $\bar{y}$ from the data that we
have collected.  Since $\bar{x} \approx \mu_1$ and $\bar{y} \approx
\mu_2$, it is natural to use $\bar{x} - \bar{y}$ to estimate $\mu_1 -
\mu_2$, and in turn use this to assess whether the data are compatible
with the null hypothesis $\mu_1 - \mu_2 = 0$.

It is natural to compare $\bar{x}$ to $\bar{y}$, since we observe
these values but do not observe $\mu_1$ and $\mu_2$.  However
$\bar{x}$ will almost never be exactly equal to $\bar{y}$, even when
$\mu_1=\mu_2$.

Note that a statistical hypothesis (such as a null hypothesis) is
always a statement about the population, it involves population
parameters such as $\mu_1$ and $\mu_2$. The statement of a null
hypothesis never directly involves the data (e.g. $\bar{x}$,
$\bar{y}$).

The data provide evidence against a hypothesis, but never are
explicitly referred to in the statement of the hypothesis itself.

---

Data reductions for hypothesis testing
======================================

We usually approach a hypothesis test by reducing the data to one
number that best summarizes the evidence in the data related to the
hypothesis.  In the CRP example, the total sample size is $m+n$.  This
may be quite a large number of data points, so reducing the data from
$m+n$ values to one value is a substantial reduction.

As an initial approach, we may consider using $\bar{x} - \bar{y}$ as
our data reduction.  This statistic is an unbiased estimate of the
quantity $\mu_1 - \mu_2$, which determines our null hypothesis.
The greater the value of $\bar{x} - \bar{y}$ (in magnitude), the
greater the evidence in the data against the null hypothesis.

However $\bar{x} - \bar{y}$ turns out not to be ideal as a data
reduction for hypothesis testing.  As noted above, $\bar{x} - \bar{y}$
will not be exactly zero even if the null hypothesis is true.  If we
observe a value, say $\bar{x} - \bar{y} = 10$, how much evidence
against the null hypothesis do we have?

The issue here is that $\bar{x} - \bar{y}$ has units that are not
statistical in nature, but instead relate to the scale on which the
data were measured. CRP is conventionally measured in units of mg/L,
but if we instead measured CRP in units of mg/mL, the values of
$\bar{x} - \bar{y}$ would become 1000 times smaller.  However the
evidence against the null hypothesis doesn't change just because we
change measurement units.

---

Test statistics in statistical units
====================================

To obtain a data reduction that has statistical units, rather than
having units derived from the measurement units of the data, we divide
$\bar{x} - \bar{y}$ by its estimated standard error, yielding
$(\bar{x} - \bar{y}) / (\hat{\sigma}_1^2/m +
\hat{\sigma}_2^2/n)^{1/2}$.

This should look familiar as the Z-score of the mean difference
$\bar{x} - \bar{y}$.

This data reduction, or _test statistic_ is denoted $T$. It measures
evidence against the null hypothesis.

Values of $T$ close to zero constitute the least possible evidence
against the null hypothesis.  The greater the value of $T$ (in
magnitude), the stronger the evidence against the null hypothesis.

Due to the central limit theorem, $T$ approximately follows a standard
normal distribution as long as $E(\bar{x} - \bar{y}) = 0$.  That is,
$T$ is approximately standard normal as long as the null hypothesis is
true.  Thus, we can calibrate the evidence against the null hypothesis
by noting how large is the value of $T$ relative to a standard normal
distribution.

---

P-values
=========

The "Z-score" given by $T$ is a useful measure of evidence against the
null hypothesis. In most settings, values of $T$ greater than 2
constitute some evidence against the null hypothesis, and values of
$T$ greater than 3 constitute strong evidence against the null
hypothesis.

For presentation purposes, the Z-score is usually converted to a
_p-value_.  This quantity is a probability that is defined to be equal
to the probability of observing a value of $T$ that is greater than
the one we actually observed, when the null hypothesis is true.

The p-value may be written $P_0(|\tilde{T}| > |T|)$, where $\tilde{T}$
is an (imaginary) test statistic that we would obtain if we were to
independently replicate our experiment in a world where we know that
the null hypothesis holds true.  Here, $P_0$ represents probability
calculated under the null hypothesis.

Like $T$, the p-value has units that are independent of the units of
the data.  The p-value has "probability units".  If the p-value is
small, it is very unlikely that the null hypothesis is true.  If the
p-value is larger, there is minimal evidence in the data against the
null hypothesis.

---

P-values
=========

The p-value is not the probability that the null hypothesis is true
given our data.  It is essentially the opposite of this -- it is the
probability of observing our data given that the null hypothesis is
true.

More explicitly, the p-value is "the probability of observing at least
as much evidence against the null hypothesis as we actually
observed, given that the null hypothesis is true".

Essentially, the p-value is a measure of how well the data "fit" the
null hypothesis, or how likely it is that we would see a certain level
of "spurious evidence" against the null hypothesis.

Using the fact that our Z-score approximately follows a standard
normal distribution, we can easily calculate p-values on a computer.
For example if we observe $T=2.5$, the p-value is 0.0124.

---

P-values
=========

p-values are useful because they represent all relevant information in
a dataset about a hypothesis using just one number.  Moreover, this
number has a scale that can be interpreted without any other
information about the data or hypothesis, e.g. p-values for comparing
two means are on the same scale as p-values for comparing two
correlation coefficients.

By convention, if the p-value is smaller than 0.05, we reject the null
hypothesis, and if the p-value is larger than 0.05, we do not reject
the null hypothesis. This means that 1/20 of the time when the null
hypothesis is true, spurious evidence against the null hypothesis will
fool us into thinking that the null hypothesis is not true.

In many settings, the notion of rejecting a hypothesis is too formal,
and we can simply report the p-value as a standardized measure of
evidence, without stating explicitly whether the null hypothesis is
rejected.

---

P-values
=========

p-value thresholds encourage thinking about evidence "dichotomously",
e.g. $p < 0.05$ is "significant" but $p \ge 0.05$ is "not
significant".  In some settings this may be appropriate, but in
reality the underlying evidence is continuous.  There is no meaningful
difference between $p=0.04$ and $p=0.06$.

p-values and hypothesis testing are only one way to summarize and
communicate statistical evidence, and many people think that this
approach is over-utilized and often mis-used or abused.

---

Statistical decisions
=====================

Hypothesis testing can be seen as a way to formalize the
process of making a binary decision based on the evidence
in data.

We have two __actions__: we may reject the null hypothesis,
or we may accept the null hypothesis.

The state of reality may be either that the null hypothesis
is true, or that the null hypothesis is false.

This results in four possibilities, in two of which our action
is correct and in two of which our action is incorrect:

|                 | Null H is true | Null H is false |
| :--             | :--            | :--             |
| __Accept null__ | True negative  | False negative  |
| __Reject null__ | False positive | True positive   |

The primary goal of this framework is to limit the rate of false
positives, which are seen as being worse than false negatives.  If we
only reject the null hypothesis when the p-value is less than 0.05,
then we will only make a false positive decision 1 out of 20 times
when the null hypothesis is true.

---

Multiple testing
================

Formal hypothesis testing is traditionally used in settings where a
specific sequence of steps are followed: first a hypothesis is
proposed, then a study is designed to assess the hypothesis, then the
study is carried out, the data are collected and finally analyzed.

A lot of research is more informal and exploratory, or involves
re-analysis of data that were collected for a different purpose.
This leads open the possibility of taking a dataset and testing
different hypotheses until reaching one where $p < 0.05$.  A
p-value found in this way is not a valid one, and does not imply
any particular level of evidence against the null hypothesis.

There are many techniques that can be used for adjusting p-values
so that they become meaningful even when obtained in an exploratory
manner.  The most basic such approach is the Bonferroni adjustment,
which simply involves multiplying the p-value by the number of
tests.  For example, if we conduct 10 tests, and the smallest
observed p-value is 0.01, it would be adjusted up to 0.1.