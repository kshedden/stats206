% Data summaries
% Kerby Shedden
% September 3, 2020

A __data summary__ is any technique that takes a large amount of data,
and reduces it to a smaller and more interpretable form.

Basic data summaries are usually numeric.  Collections of data
summaries are often presented as tables or plots to makes them easier
to interpret.

Summaries can involve a single variable, in which case they are
__univariate__, or they can involve more than one variable, in which
case they are __multivariate__.

At this point in the class, we will focus on univariate summaries.

---

Different types of univariate summaries are used with different
statistical types of variables.

The most common summary for a nominal or ordinal variable is a
_frequency table_.

Suppose we ask people about their relationship status.  We may obtain
a frequency table such as follows:

| Status     | Never-married | Divorced | Separated | Widowed | Married |
|  :--       | :--           | :--      | :--       | :--     | :--     |
| Count      | 385           |  198     |  246      |  79     | 311     |
| Proportion | 0.39          | 0.20     | 0.02      | 0.08    | 0.31    |

(Note: Divorced, Separated, Widowed refer to the most recent
relationship of people who are currently unmarried but were once
married)

The raw dataset is a list of 997 responses.  The five counts and five
proportions given above are a summary because they constitute a more
interpretable reduction of the data, compared to a listing of all 997
responses.

The __modal__ label for a nominal or ordinal variable is the label
with the greatest frequency, e.g. above the modal relationship status
is "never married".

---

Quantitative variables allow a much greater variety of data summaries
than ordinal or nominal variables.

We are all familiar with using the mean and median to summarize a
collection of (quantitative) observations.

These are both _measures of location_, also known as _measures of
central tendency_, or _measures of centrality_.

A measure of location aims to identify the most typical or representative
value in a dataset (this is not something that has a clear-cut definition).

But there are many other important features of a dataset to capture,
beyond just the "location".

---

Mathematically and algorithmically, there are two main classes of
summary measures: those based on __moments__, and those based on
__quantiles__.

Moments are formed through averaging.  The mean is a moment.

Quantiles are formed through sorting.  The median is a quantile.

For most features of a dataset, there is both a moment and a quantile
that captures that feature.

---

In our discussion here, we will focus on using moments and quantiles
of a dataset to capture its main features.

___Remember:___
The goal of a statistical analysis is almost always to learn about the
population that the data represent, not only about the data that we
have in-hand.

This maxim applies when forming summary measures as well.

The median can be calculated from a sample of data.  This is properly
called the __sample median__.  The population that these data
represent also has a median, called the __population median__.

The sample and population medians will generally be close, but usually
are not equal.

Uncertainty analysis tells us how far the sample and population
medians are likely to fall from each other.

---

The sample median is obtained by sorting the data, and selecting the
value in the middle of the sorted list.

If the sample size is odd, there is a clear proper choice for
"middle", e.g. if the sample size is 11, we take the value in position
6 of the sorted list (counting from 1).

If the sample size is even, there is no value that falls exactly in
the middle.  There are various conventions for dealing with this, we
will let the software handle this issue for us.

---

The __order statistics__ of a dataset are obtained by taking the
values of the dataset and sorting them.

If our data are 9, 2, 11, then the first order statistic of our data
is 2, the second is 9, and the third is 11.

If we denote the data as $x_i$, so that $x_1=9$, $x_2=2$, and
$x_3=11$, then the order statistics are denoted $x_{(i)}$, so that
$x_{(1)} = 2$, $x_{(2)} = 9$, and $x_{(3)} = 11$.

---

The __left tail proportions__ of our data are obtained by calculating
the proportion of the data that fall below a given value $x$.

Suppose we are considering the incomes of people in Brazil.  Using USD
equivalents as the currency unit, we can ask:

* What proportion of workers in Brazil earn less than or equal to USD
500 per month?

* What proportion of workers in Brazil earn less than or equal to USD
1000 per month?

These are both left tail proportions.

---

For any "probability point" $p$ between 0 and 1, we can
define the $p^{th}$ __sample quantile__ to be the order statistic
$x_{(i)}$ such that $i$ is the least integer that is greater than
or equal to $np$, where $n$ is the sample size.

The $p^{th}$ quantile may be denoted $Q_p$.

Quantitative variables have measurement units -- quantiles always have
the same measurement units as the data from which they were derived.

---

As an example, suppose that $p=0.75$ and the sample size is $n=243$.
The $0.75$ sample quantile, also known as the 75th percentile, is
approximately equal to the order statistic $x_{(183)}$, since
$0.75*243 = 182.25$, and 183 is the least integer that is greater
than or equal to 182.25.

The 75th percentile (0.75 quantile) gives us a value such that
approximately 75% of the values in the sample fall at or below this
number, and approximately 25% of the values fall at or above it.

Some sets of quantiles are very commonly used and have special
names:

* Deciles: $0.1, 0.2, \ldots, 0.8, 0.9$

* Quintiles: $0.2, 0.4, 0.6, 0.8$

* Quartiles: $0.25, 0.5, 0.75$

* Tertiles: $0.33, 0.66$

---

Quantiles other than the median tell us about the full range of values
in the data, not just about the most typical value.

The table below shows a series of quantiles of the household incomes
for residents of three US states:

State\Percentile   |  10    |  25    |  50    |   75    |   90     |
 :--               |  --:   | --:    | --:    |--:      | --:      |
__MI__             | 13,200 | 29,000 | 55,500 |  98,000 | 153,150  |
__TX__             | 14,000 | 30,000 | 60,000 | 106,700 | 171,100  |
__MD__             | 18,900 | 42,000 | 82,080 | 140,200 | 220,000  |

(source: ACS/PUMS)

The units of these quantiles are US dollars (USD).

As the proportion $p$ grows within a row, the quantiles are
non-decreasing.

All quantiles for Texas are greater than the corresponding quantiles
for Michigan, and all quantiles for Maryland are greater than the
corresponding quantiles for Texas.  The three states appear to be
_stochastically ordered_.  This is much stronger than knowing only
that the means or medians are ordered.

---

The central value (location) of a dataset only scratches the surface
of what that dataset may tell us.

Another important notion is that of __dispersion__ -- how spread out
are the data values?

One way to quantify dispersion is through the __interquartile range__
 (IQR).  This is the difference between the 75th and 25th percentiles.

The IQR for Michigan is 98,000 - 29,000 = 69,000.  The IQR for
Maryland is 140,200 - 42,000 = 98,200.  Incomes in Maryland are more
dispersed than incomes in Michigan.

The IQR is an __L-statistic__ because it is a linear function of
quantiles.

---

__Residuals__ are a modified version of our data in which the data
have been transformed to have location equal to zero.

__Median residuals__ are formed by subtracting the median from each
data value.  The median of the median residuals is zero.

__Mean residuals__ are formed by subtracting the mean from each data
value.  The mean of the mean residuals is zero.

When people say "residuals" without qualification they are probably
referring to mean residuals.

The __median absolute deviation__ (MAD) is the median of the absolute
values of the median residuals:

$$
\textrm{med}(|x_1 - m|, \ldots, |x_n - m|) \;\;\textrm{where}\;\; m = \textrm{med}(x_1, \ldots, x_n)
$$

The MAD is an alternative measure of dispersion to the IQR.  The MAD
and IQR are different, but both reflect the dispersion of the data.

---

The mean (average) of the data is a moment.  It is the prototypical
example of a moment, but many other summaries are also moments.

The mean, like the median, is a measure of location.

One of the important differences between moment-based summaries and
quantile-based summaries is captured through the notion of
__resistance__.  We won't give a complete definition of this term
here.  For our purposes, a statistic is resistant if by changing a small
fraction of the data by a large amount, the value of the statistic
shows little to no change.

The median is very resistant.  The median of {1, 3, 7} is 3, but the
median of {1, 3, 7000} is also 3.  We can make any change to the data
values above the median, or below the median, and the median will not
change.  On the other hand, the mean of {1, 3, 7}, is approximately
3.7, while the mean of {1, 3, 7000} is 2335.  Thus, the mean is not a
resistant statistic.

In general, statistics (summaries) derived from quantiles are resistant,
and statistics derived from moments are not resistant.

This does not mean that quantile-based or other resistant data summaries
are better than moment-based summaries.  There are additional
trade-offs that we will consider later.

---

Next we will construct a moment-based measure of dispersion.

Above we discussed the concept of "mean residual".  If $x_i$ is a data
value and $\bar{x} = (x_1 + \cdots + x_n) / n$ is the average of our
data, then $x_i - \bar{x}$ is the residual (mean residual).

The average of the squared mean residuals is:

$$ \hat{\sigma}^2 = ((x_1 - \bar{x})^2 + \cdots + (x_n - \bar{x})^2) /
n.  $$

This is one version of the _sample variance_.  Another common version
of the sample variance divides by $n-1$ instead of dividing by $n$.
We will discuss the rationale for this later.

The sample variance is the "average squared residual" or "average
squared deviation from the mean".  The units of the sample variance is
the square of the units of the data.  So if our data are kilograms
(kg), then the sample variance has units kg^2.

---

The __sample standard deviation__ is $(\hat{\sigma}^2)^{1/2}$.
It has the same units as the data.

Both the sample variance and the sample standard deviation are
moment-based measures of dispersion.  The sample standard deviation is
usually easier to interpret, because it has the same units as the
data.

It is not correct to say that the standard deviation is the "average
distance of the data to the mean value".  It is the "square root
of the average squared distance of the data to the mean value".

Note the similarity and difference between the standard deviation
and the MAD.  The MAD is based on absolute median residuals
(which are equivalent to distances to the median).

---

Another important property of a dataset that can be approached using
either moments or quantiles is __skew__.  Roughly speaking, the skew
refers to whether the data extend further on the high side of the
central value, or on the low side of the central value.

A quantity that is very commonly found to be strongly skewed is
income.  In the US, the median household income is around 60K
USD/year.  Although technically incomes can be negative, most incomes
are positive, so the lower half of the income distribution
predominantly falls between 0 and 60K USD.  The upper half of the
income distribution extends well into the millions of dollars.  This
assymetry is indicative of strong right skew, which is a property that
is almost always found for incomes.

---

We can construct a quantile-based measure of skew as follows.  First,
form the L-statistic

$$ (Q_{0.75} - Q_{0.5}) - (Q_{0.5} - Q_{0.25}) = Q_{0.75} - 2\cdot
Q_{0.5} + Q_{0.25}.  $$

This directly reflects the gap between the middle and upper quantiles,
and the gap between the lower and middle quantiles.

A desirable measure of skew should be scale-invariant.  The skew
should not change if we measure incomes in USD, in thousands of USD,
or in pennies.

To make the skew scale-invariant, we divide the above L-statistic by
the IQR.  This gives us the following expression for the quantile-based
skew:

$$ (Q_{0.75} - 2\cdot Q_{0.5} + Q_{0.25}) / (Q_{0.75} - Q_{0.25}).  $$

---

A moment-based measure of skew can be obtained using third moments.
The third central moment is denoted $m_3$:

$$ m_3 = ((x_1 - \bar{x})^3 + \cdots + (x_n - \bar{x})^3) / n $$

Note that some versions of the third central moment are divided by
$n-1$ rather than $n$.  For purposes of assessing the skew, this does
not impact the results at all.

Note the following:

* Raising the data to the third power preserves the sign (positive or
  negative)

* Raising the data to the third power exaggerates the largest values
(in magnitude) relative to the values with smaller magnitudes

If there are more positive residuals with large magnitude, $m_3$ will
be positive.  If there are more negative residuals with large
magnitude, $m_3$ will be negative.
Thus, $m_3$ reflects whether the residuals with the largest magnitude
tend to be positive, or tend to be negative.

---

As a simple example, suppose that our data are {0, 1, 10}.

The mean residuals are {-3.7, -2.7, 6.3}.

The cubes of the mean residuals are {-49.3, -19.0, 254}.

The average of these cubes is 61.9.

We can see that the more extreme upper value of the data (10) dominates
the less extreme lower value of the data (0), in terms of distance to
the mean.  This leads to a positive
value for the third central moment.

---

The quantile-based measure of skew is scale-invariant. We would like
the moment-based version of the skew to also be scale invariant.

To do this, we calculate the third moment using Z-scores, not using
the raw data.  A Z-score is a normalized version of a data value,
defined as

$$ z_i = (x_i - \bar{x}) / \hat{\sigma}.  $$

The moment-based skew is:

$$ ((z_1 - \bar{z})^3 + \cdots + (z_n - \bar{z})^3) / n $$

---

Often we can choose to summarize data using either a quantile-based
or moment-based measure.

There are some trade-offs in this choice.

As noted earlier, quantile-based measures are usually resistant to
contamination and outliers.  In some cases, they are easier to
explain than moment-based measures (e.g. the IQR may be easier
to explain than the standard deviation).

However quantile-based measures may, in some cases, be slightly
more difficult to estimate (we will return to this point later
in the course).

---

Moment-based measures are easier to work with mathematically, mainly
because we can expand them algebraically:

$$(x_i - \bar{x})^2= x_i^2 - 2x_i\bar{x} + \bar{x}^2$$

Ths gives rise to some useful identities, such as that:

$$\hat{\sigma}^2 = (x_1^2 + \cdots + x_n^2) / n - \bar{x}^2.$$

In words, the variance is "the mean of the squares minus the
square of the mean".

Quantile based measures are difficult to work with mathematically.
They often involve sorting and absolute values, which cannot
be manipulated algebraically.
