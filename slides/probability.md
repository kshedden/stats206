% Probability
% Kerby Shedden
% October 10, 2020

Probability is the branch of mathematics that studies randomness in a
formal and rigorous way.

Probability is part of the foundation of statistics and data science.

Probability provides us with:

* A way to link a sample to its population

* A way to make precise statements about uncertainty in data analysis

* Tools for describing variation in a collection of measurements.

---

Data sampling and probability
=============================

In any statistical analysis, the sample is derived
from a population.

Some samples are _probability samples_, meaning that they
can be mathematically described using the language of probability
theory.

Other samples are collected so haphazardly that they are not
amenable to this type of formal description.  These are
usually called _convenience samples_.

Another situation where probability doesn't add much insight
is when we have a census, so that our sample is the entire
population.

In some cases, a sample is literally a selection from a finite
population -- for example, we contact 1000 people living in
one country.

In other cases, a sample consists of measurements that
are impacted by numerous _sources of variation_ along with
_measurement error_.  An example of this type of sample would
be a study of the yield of an agricultural crop,
in which we grow the crop on a plot of land and
measure the yield.  The sources of variation could include soil chemistry
and weather.

---

Probability distributions
=========================

When we have a probability sample, its population can be
described using a _probability distribution_.  This
is a formal way of defining what can be observed, and how likely
we are to observe individual observations and combinations of
observations.

The _sample space_ is the set of all values that can be observed.
It may be finite or infinite.

Suppose we have a process for drawing colored balls at random,
and the balls can be either red, orange, or green.  In this
case, we have a finite sample space containing three elements.
The probability distribution
can be defined by a _probability mass function_ (PMF), which is a
function that takes an element of the sample space as input,
and returns the probability of observing that value as the
result.

A PMF can be represented as a table, such as:

x        | red  | orange | green |
---------|------|--------|-------|
__p(x)__ | 1/4  |  1/2   |  1/4  |

---

Events
======

An _event_ is a subset of the sample space, e.g.
$\{\textrm{red}, \textrm{green}\}$ is an event for the
sample space
$\{\textrm{red}, \textrm{green}, \textrm{orange}\}$.

The probability of an event is the sum of probabilities
for all elements in the event, e.g.

$$
P(\{\textrm{red}, \textrm{green}\}) = 1/4 + 1/4 = 1/2.
$$

Every event $E$ has a complement event $E^c$, which is defined
to be the event consisting of all points in the sample
space that are not in $E$.  If $E = \{\textrm{red}, \textrm{green}\}$
then $E^c = \{\textrm{orange}\}$.

---

Axioms of probability
=====================

Every probability distribution respects the axioms
of probability.  Two key consequences of these axioms
are:

* Every probability is a real number between 0 and 1

* The sum of probabilities over all points in the sample
space is 1

---

Random variables
================

A _random variable_ is a term that is often used to refer
to the result of drawing a value from a probability distribution.

A random variable is usually denoted by a capital letter, e.g. $X$.

A random variable has no fixed value, but there are fixed probabilities
that the random variable is observed to take on each value in its sample space.

If $x$ (lower case) is a fixed point in the sample space, then we
can write $P(X=x)$ to denote "the probability that $X$ takes on the
value $x$".

In the example seen earlier, $P(X = \textrm{orange}) = 1/2$.

---

Transformations
===============

We will often need to obtain the probability distribution
for a random variable that has been derived from another
random variable by applying a transformation to it.

For example, this is the distribution for a random
variable $X$:

x          | 1    | 2   | 4   | 7   |
-----------|------|-----|-----|-----|
__p(X=x)__ | 0.1  | 0.3 | 0.4 | 0.2 |

If we define $Y=X^2$, then $Y$ is a transformation
of $X$, and we can obtain the distribution of $Y$
as follows:

y          | 1    | 4   | 16  | 49  |
-----------|------|-----|-----|-----|
__p(Y=y)__ | 0.1  | 0.3 | 0.4 | 0.2 |

---

Transformations
===============

Sometimes a transformation reduces the size
of the sample space, here we have the PMF of
$Y = (X-3)^2$:

x          | 1    | 4   | 16  |
-----------|------|-----|-----|
__p(X=x)__ | 0.7  | 0.1 | 0.2 |

---

Summary statistics of populations and samples
=============================================

We have considered many summary statstics for samples
of data,
all of which can be derived either from moments or
from quantiles.

For every summary statistic that we can compute using
a sample, there is an analogous summary value
for the population from which the sample was obtained.
This may be called the _population analogue_ of the
summary statistic.

We have calculated the mean (average) for a sample
of data.  The corresponding population statistic
is sometimes called the _expectation_, or the
_population mean_.  When needed, we refer to the
mean of the sample as the _sample mean_ to distinguish
it from the population mean.

---

Summary statistics of populations and samples
=============================================

The expectation for a probability distribution on
a finite sample space is obtained by taking each
point in the sample space, multiplying by its
probability, and summing these values.

The expected value for the probability distribution

x          | 1    | 2   | 4   | 7   |
-----------|------|-----|-----|-----|
__p(X=x)__ | 0.1  | 0.3 | 0.4 | 0.2 |

is $0.1\cdot 1 + 0.3\cdot 2 + 0.4\cdot 4 + 0.2\cdot 7 = 3.7$

The expectation, like the sample mean, is a measure of
location or centrality.  In this example, we see that
the expectation lies roughly at the center of the distribution.

A _population quantile_ of a random variable $X$ corresponding
to probability point
$p$ is any point $q$ in the sample space such that $P(X \le q) = p$.

In the distribution above, 3 is a population 0.4 quantile, as is any number
in the interval [2, 4).

---

Population variance
===================

The _centering transformation_
subtracts the population mean from each point in the sample space.
The distribution of $Z = X - EX$, the centered
version of $X$, is

z          | -2.7 | -0.7 | 1.3 | 3.3 |
-----------|------|------|-----|-----|
__p(Z=z)__ | 0.1  | 0.3  | 0.4 | 0.2 |

The distribution of the squared deviations from the mean,
$V = Z^2$, is

v          | 7.29 | 0.49 | 1.69 | 10.89 |
-----------|------|------|------|-------|
__p(V=v)__ | 0.1  | 0.3  | 0.4  | 0.2   |

The population variance is the expected value of this distribution,
which is

$0.1\cdot 7.29 + 0.3\cdot 0.49 + 0.4\cdot 1.69 + 0.2\cdot 10.89 = 3.73$.

---

Cumulative Distribution Function
================================

Another representation of a probability
distribution that is useful for quantitative data is the _cumulative
distribution function_ (CDF).

The CDF tabulates all of the left tail
probabilities $P(X \le x)$.

Given this distribution:

x          | 1    | 2   | 4   | 7   |
-----------|------|-----|-----|-----|
__p(X=x)__ | 0.1  | 0.3 | 0.4 | 0.2 |

The CDF is:

x           | 1    | 2   | 4   | 7 |
------------|------|-----|-----|---|
__p(X<=x)__ | 0.1  | 0.4 | 0.8 | 1 |

---

Non-finite sample spaces
========================

All of the examples we have seen so far involve finite sample
spaces.  In practice, we often want to work with an infinite
sample space.

An infinite sample space does not have a probability mass
function.  There may (or may not) be a _probability density
function_ (PDF) for a random variable $X$ with an infinite sample space.
The PDF for $X$ evaluated at $x$ describes how likely we are
to observe points near (not exactly at) $x$.

Working mathematically with infinite sample spaces involves
calculus so is not considered further in this course.

---

Joint distributions
===================

Two random variables have a joint distribution if
we can place a probability on every combined pair
of values that the two variables can take on.

For example, below $X$ has sample space $\{1, 3\}$
and $Y$ has sample space $\{2, 4, 5\}$.  The joint
probabilities for $X$ and $Y$ are in this table:

X\\Y   | 2   |  4  |  5  |
-------|-----|-----|-----|
__1__  | 0.3 | 0.3 | 0.2 |
__3__  | 0.1 | 0   | 0.1 |

Note that all six probabilities in the table
sum to 1.

---

Joint distributions
===================

We can calculate the
marginal distribution for every variable in a joint
distribution.

For this joint distribution:

X\\Y   | 2   |  4  |  5  |
-------|-----|-----|-----|
__1__  | 0.3 | 0.3 | 0.2 |
__3__  | 0.1 | 0   | 0.1 |

the marginal distribution for $X$ is

| x          |  1  |   3  |
| :--        | :-- | :--  |
| __P(X=x)__ | 0.8 |  0.2 |

This marginal distribution is obtained by summing within the rows
of the joint distribution.

---

Joint distributions
===================

The marginal distribution for $Y$
is obtained by summing within the columns of the joint distribution:

|  y          |  2  |   4  |  5  |
|  :--        | :-- | :--  | :-- |
| __P(Y=y)__  | 0.4 |  0.3 | 0.3 |

---

Independence
============

A joint distribution exhibits independence
if every probability in the joint table is the product
of the corresponding marginal probabilities.

For this joint distribution:

X\\Y   | 2   |  4  |  5  |
-------|-----|-----|-----|
__1__  | 0.3 | 0.3 | 0.2 |
__3__  | 0.1 | 0   | 0.1 |

the marginal probability of observing $X=3$ is 0.2,
and the marginal probability of observing $Y=4$ is
0.3.  But the joint probability of observing
$X=3$ and $Y=4$ is zero, which is not equal to $0.2\cdot 0.3$.

Therefore $X$ and $Y$ are not independent in this joint
distribution.

---

Independence
============

Here is another joint distribution:

X\\Y   | 2    |  4   |  5   |
-------|------|------|------|
__1__  | 0.32 | 0.24 | 0.24 |
__3__  | 0.08 | 0.06 | 0.06 |

It has the same marginal distributions for $X$ and for $Y$ as this
joint distribution:

X\\Y   | 2   |  4  |  5  |
-------|-----|-----|-----|
__1__  | 0.3 | 0.3 | 0.2 |
__3__  | 0.1 | 0   | 0.1 |

However the first joint distribution above exhibits independence,
while the second one does not.

---

Conditional distributions
=========================

Starting with this joint distribution

X\\Y  | 2   |  4  |  5  |
------|-----|-----|-----|
__1__ | 0.3 | 0.3 | 0.2 |
__3__ | 0.1 | 0   | 0.1 |

we can divide each row by its total and obtain the _conditional
distributions of $Y$ given $X$_:

X\\Y   | 2   |  4  |  5  |
-------|-----|-----|-----|
__1__  | 3/8 | 3/8 | 1/4 |
__3__  | 1/2 | 0   | 1/2 |

Note that each row sums to 1 and is a distribution in its own
right.

---

Conditional distributions
=========================

If we knew that, say, $X=3$, then the second row
of this table would tell us how likely we are to observe
each possible value of $Y$.

These conditional probabilities are denoted,
e.g., $P(Y=2 \;|\; X=1) = 3/8$.  The "|" symbol is
read "given".

---

Conditional distributions
=========================

Recall that in the table below, $X$ and $Y$ are independent:

X\\Y   | 2    |  4   |  5   |
-------|------|------|------|
__1__  | 0.32 | 0.24 | 0.24 |
__3__  | 0.08 | 0.06 | 0.06 |

The conditional distributions of $Y$ given $X$ are:

X\\Y   | 2    |  4   |  5  |
-------|------|------|-----|
__1__  | 0.4  | 0.3  | 0.3 |
__3__  | 0.4  | 0.3  | 0.3 |

Note that the rows are identical -- the conditional
distribution of $Y$ given $X$ does not depend on $X$.
This always happens when $X$ and $Y$ are independent.

---

Conditional distributions
=========================

The conditional distributions of $X$ given
$Y$ are:

X\\Y  | 2   |  4  |  5  |
------|-----|-----|-----|
__1__ | 0.8 | 0.8 | 0.8 |
__3__ | 0.2 | 0.2 | 0.2 |

The conditional distribution of $X$ given $Y$ does
not depend on $Y$.  This always happens when $X$
and $Y$ are independent.

---

Conditional independence
========================

Now lets consider a setting where we are exploring
the relationship among three factors --
tea drinking, smoking, and cancer.  The following
joint distribution is shown in "long form":

Tea     | Smoke   |  Cancer  |  Probability  |
--------|---------|----------|---------------|
Y       | Y       | Y        | 0.0033        |
Y       | Y       | N        | 0.1080        |
Y       | N       | Y        | 0.0049        |
Y       | N       | N        | 0.4838        |
N       | Y       | Y        | 0.0027        |
N       | Y       | N        | 0.0860        |
N       | N       | Y        | 0.0031        |
N       | N       | N        | 0.3082        |

---

Conditional independence
========================

We can derive several marginal distributions from this joint three-way
distribution.  For example, the marginal distribution of tea drinking
and cancer is

 &nbsp;    | Cancer | No cancer |
-----------|--------|-----------|
__Tea__    | 0.0082 | 0.5918    |
__No tea__ | 0.0058 | 0.3942    |

The values in this table are obtained by summing rows
in the complete table over the levels of smoking.  For
example,

$$
P(\textrm{Tea}, \textrm{Cancer}) =
P(\textrm{Tea}, \textrm{Cancer},\textrm{Smoking}=N) +
P(\textrm{Tea}, \textrm{Cancer},\textrm{Smoking}=Y)
= 0.0049 + 0.0033 = 0.0082.
$$

---

Conditional independence
========================

To see if tea drinking and cancer are independent,
we can look at the conditional distributions of
cancer given tea drinking:

 &nbsp;    | Cancer | No cancer |
-----------|--------|-----------|
__Tea__    | 0.0137 | 0.9863    |
__No tea__ | 0.0144 | 0.9856    |

Since the two rows of this table are different,
tea drinking and cancer are dependent -- people
who drink tea have a slightly lower cancer risk
(1.37%) compared to people who do not drink tea (1.44%).

---

Conditional independence
========================

The following is the conditional joint distribution
between cancer and tea drinking, given that
people do not smoke:

&nbsp;     | Cancer | No cancer |
-----------|--------|-----------|
__Tea__    | 0.0061 | 0.6047    |
__No tea__ | 0.0039 | 0.3853    |

This table is obtained by taking the four
probabilities for non-smokers in the original
table, and dividing them by their sum.

For example,

$$
P(\textrm{Tea}, \textrm{Cancer} | \textrm{Smoke=N}) = 0.0049 / (0.0049 + 0.4838 + 0.0031 + 0.3082)
= 0.0061.
$$

---

Conditional independence
========================

Next we take the table from the previous slide and condition on tea
drinking, by dividing each row by the row total.  The result shows that cancer
is independent of tea drinking, given that
people do not smoke:

&nbsp;     | Cancer | No cancer |
-----------|--------|-----------|
__Tea__    | 0.01   | 0.99      |
__No tea__ | 0.01   | 0.99      |

If we conditioned on people being smokers,
instead of conditioning on people being non-smokers,
we would also conclude that cancer is
(conditionally) independent of tea drinking.
Specifically, (rounding to two places)
we would get the table below:

&nbsp;     | Cancer | No cancer |
-----------|--------|-----------|
__Tea__    | 0.03   | 0.97      |
__No tea__ | 0.03   | 0.97      |

---

Conditional independence
========================

This example shows that we can have three variables,
$X$, $Y$, $Z$, where $X$ and $Y$ are dependent if
we ignore $Z$, but become independent if we
condition on $Z$.

The example suggests that tea drinking may not really
protect you from cancer.  The apparent protective
effect of tea drinking for cancer may be a result of
tea drinkers tending to be less likely to smoke.
In statistical terms, smoking may be a confounder
of the relationship between tea drinking and cancer.
