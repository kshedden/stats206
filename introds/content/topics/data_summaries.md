Data summaries
==============

Many approaches to data analysis may be viewed as data
"summarization".  The most immediate effect of summarizing data is to
take data that may be overwhelming to work with, and reduce it to a
few key summary values that can be viewed, often in a table or plot.

As we have emphasized before, data analysis should always aim to
address specific and explicit research questions.  This principle continues to hold when
working with data summaries.  There are many data summaries in common
use, and new approaches to summarizing data continue to be developed.
However not all data summaries are equally relevant for addressing a
particular question.  When conducting a data analysis, it is important
to identify data summaries that are informative for addressing the
question at hand.

[Previously]({{<ref
"what_is_statistics.md#samples-and-populations">}}), we have
introduced the key notions of _samples_ and _populations_. Our data
(the "sample") are reflective of a population that we cannot
completely observe.  The goal of a data analysis is always to learn
about the population, not only about the sample.  When performing a
data analysis involving data summaries, we will calculate the
summaries using the data for our sample (since that is all we have to work with), but
draw conclusions (with appropriate uncertainty quantification) about
the population.

There does not exist (and probably never will exist) a recipe or
algorithm that automatically tells us which data summaries can be used
to address a particular question.  Therefore, it is important to
understand the motivation and theoretical properties behind a number of different
summarization approaches.  With experience, you can develop the
ability to effectively summarize data in a way that brings insight
regarding your research aims.

One meaning of the term _statistic_ is equivalent to the idea of a
data summary.  That is, a statistic is a value derived from data that
tells us something in summary form about the data.  Here we will
introduce some of the main types of data summaries, or statistics.  We
will continue to learn about many more types of data summaries later
in the course.  As noted above, many data summaries are best viewed in
graphical form, but here we will focus on simple numerical data
summaries that can be appreciated without graphing.  We will consider
graphical summaries later.

Data summaries based on frequencies
-----------------------------------

We have learned that a nominal variable takes on a finite set of
unordered values.  The most basic summarization of a nominal variable
is its _frequency table_.  For example, suppose we are interested in
the employment status of working-age adults, and we categorize
people's employment status as follows: (i) employed full time, (ii)
employed part time, looking for full time work, (iii) employed part
time, not looking for full time work, (iv) not employed, looking for
work, and (v) not employed, not looking for work.  If we obtain the
employment status for 1000 people, then our "raw data" is a list of
1000 values.  The frequency table summarizes this data as five counts,
the number of people who give each of the possible responses, and the
corresponding proportions (which must sum to 1).

|                | i     | ii    | iii   | iv    |   v   |
|    :--         |  --:  | --:   |   --: | --:   |  --:  |
| __Count__      | 367   | 253   | 47    | 51    | 282   |
| __Proportion__ | 0.367 | 0.252 | 0.047 | 0.051 | 0.282 |

Data summaries based on quantiles and tail proportions
--------------------------------------------------------

For ordinal and quantitative data, a _tail proportion_ is defined to
be the proportion of the data that falls at or below a given value.
For example, suppose we ask "what proportion of the days in August
does the daily maximum temperature exceed 35C?", or "what proportion
of workers in Mexico earn 1000 USD or less per month?".  The first of
these examples can be called a _right tail proportion_, because it
refers to the proportion of observations that are greater than a given
value (35C), and the second of these examples can be called a _left
tail proportion_, because it refers to the proportion of observations
that are less than or equal to a given value (1000 USD).

Tail proportions are calculated from a sample of data.  The analogous
characteristic of a population is called a _tail probability_.  We
will not emphasize this distinction here, but will return to it later
in the course.

Tail proportions can be very useful if there is a good reason for
choosing a particular threshold from which to define the tail.  For
example, a temperature of 35 C may be considered dangerously warm, or
a monthly income of 1000 USD may be just above the poverty level
in Mexico.  While such thresholds can often be stated, in some
settings any choice of a threshold seems arbitrary.
To circumvent this, we may use a closely related
summary statistic called a _quantile_.  A quantile is essentially
the inverse of a tail proportion.  Instead of starting with a
threshold (say 1000 USD for monthly income), we start with the
proportion of the sample (say 0.25), and find a value X such that the
given proportion (e.g. 0.25) of the data is less than or equal to X.
Note that quantiles are always defined in terms of left tail
proportions.
These proportions may be called _probability points_ in this context.

In principle, a quantile exists for every probability point between 0 and 1.
But technical difficulties can arise when the sample size is small,
or when the number of distinct observable values is small.  Suppose
we only observe four values {1, 3, 7, 9}.  Half of the data are less
than or equal to 3, but it is also true that half of the data are less
than or equal to 6.99.  Any value in the interval [3, 7) could be
taken as the median.  There are several conventions for resolving this
difficulty.  However in this course, we will generally be working with
fairly large data sets, where the minor differences between various
approaches for calculating quantiles are not consequential.

In common parlance, people refer to "percentiles" more often than
"quantiles".  But these two notions are equivalent -- the 65th
percentile is the same as the 0.65 quantile (for example).  In most
settings, it is fine to use either term.

Certain quantiles have special names.  The _median_ is the quantile
corresponding to a proportion of 0.5.  The _deciles_ are the quantiles
for proportions 0.1, 0.2, ..., 0.9.  The _quartiles_ are the quantiles
for proportions 0.25, 0.5, and 0.75.  _Tertiles_ are the quantiles for
proportions 1/3 and 2/3, and _quintiles_ are the quantiles for
proportions 0.2, 0.4, 0.6, and 0.8.  Note that to divide the real line
into n parts requires n-1 points.  So there are 9 deciles, 3
quartiles, etc.

People may also state that a
value "falls into" a quartile (or a tertile, etc.).  A value that falls
into, say, the second quartile of a dataset (or distribution) is a
value that falls between the 25th and 50th percentiles.

### Order statistics

A closely related concept to a quantile is an _order statistic_.  If
we sort our data and take the i'th element of the sorted list, then this
value is
called the i'th _order statistic_.  If our data are {7, 3, 1, 9}, then
the first order statistic is 1, the second order statistic is 3, the
third order statistic is 7, and the fourth order statistic is 9.  If
we denote our data {{<katex>}}x_1=7{{</katex>}}, {{<katex>}}x_2=3{{</katex>}},
{{<katex>}}x_3=1{{</katex>}}, and {{<katex>}}x_4=9{{</katex>}}, then
the order statistics are denoted
{{<katex>}}x_{(1)}=1{{</katex>}}, {{<katex>}}x_{(2)}=3{{</katex>}},
{{<katex>}}x_{(3)}=7{{</katex>}}, and {{<katex>}}x_{(4)}=9{{</katex>}}.

Order statistics and quantiles are related in the following manner.
If {{<katex>}}n{{</katex>}} is the sample size, and we wish to estimate
the quantile for proibability point {{<katex>}}p{{</katex>}}, one
convention is to take the order statistic {{<katex>}}x_{(j)}{{</katex>}},
where {{<katex>}}j{{</katex>}} is the least integer greater than or equal to
{{<katex>}}p\cdot n{{</katex>}}, where {{<katex>}}n{{</katex>}} is the
sample size.

The most important
thing to keep in mind about quantiles is that the {{<katex>}}p^\textrm{th}{{</katex>}}
quantile {{<katex>}}Q_p{{</katex>}} has the property that approximately
a fraction of {{<katex>}}p{{</katex>}} of the data falls at or
below {{<katex>}}Q_p{{</katex>}}, and approximately a fraction of
{{<katex>}}1-p{{</katex>}} of the data falls at or above
{{<katex>}}Q_p{{</katex>}}.

### The median as a measure of central tendency

A very commonly-encountered quantile is the _median_, which is the
quantile corresponding to a proportion of 0.5.  That is, the median is
a point {{<katex>}}Q_{0.5}{{</katex>}} such that approximately half of the data are less than or equal to
{{<katex>}}Q_{0.5}{{</katex>}},
and approximately half of the data are greater than or equal to {{<katex>}}Q_{0.5}{{</katex>}}.
For a large dataset, the median can be computed by sorting the data,
and taking the value in the middle of the sorted list.

The median is the most commonly-encountered quantile, and is the
easiest to interpret.  It is sometimes said to be a measure of
_location_ or _central tendency_.  These terms mean that the median is
used to reflect the "most typical", "most representative" or "most central"
value in a dataset.  However there
are many other measures of central tendency besides the median, and in
some cases different measures of central tendency can give very
different results.  This is a topic that we will return to later.

### Example: Quantiles of household income

Suppose we are looking at the distribution of income for households in
the United States.  This median is currently around 59,000 USD per
year.  The 10th percentile and 90th percentile of US household income
are currently around 14,600 USD, and 184,000 USD, respectively.  These
values tell us about the living standard of the middle 80% of the
United States population.  We can take this a step further by looking
at a series of income quantiles within three US states in 2018
(Michigan, Texas, and Maryland).

State\Percentile   |  10    |  25    |  50    |   75    |   90     |
 :--               |  --:   | --:    | --:    |--:      | --:      |
__MI__             | 13,200 | 29,000 | 55,500 |  98,000 | 153,150  |
__TX__             | 14,000 | 30,000 | 60,000 | 106,700 | 171,100  |
__MD__             | 18,900 | 42,000 | 82,080 | 140,200 | 220,000  |

(source: ACS/PUMS)

There are several interesting observations that can be made from the
above table.  One is that the differences between the states grow
larger as we move from the lower quantiles to the upper quantiles.
Another is that the states are always ordered in the same way --
every quantile for Texas is greater than the corresponding
quantile for Michigan, and every quantile for Maryland is greater
than the corresponding quantile for Texas.  If this is true
for every possible quantile given by a probability point
{{<katex>}}0 \le p \le 1{{</katex>}}, then we could say
that incomes in Texas are _stochastically greater_ than incomes in Michigan,
and incomes in Michigan are stochastically greater than incomes in Texas.
Since the table above only shows five quantiles, we can only say that the
table is consistent with these "stochastic ordering" relationships
holding.

We have learned that quantitative data typically have measurement
units.  The quantiles based on a sample of quantitative data always have the
same measurement units as the data themselves.  The quantiles in the
above table have United States dollars (USD) as their units, since
that is the units of the data.

### Extreme quantiles

The term _extreme quantile_ refers to any quantile that represents a
point that is far into the tail of a distribution.  Extreme quantiles
play an important role in assessing risk.  For example, if someone is
debating whether to build an expensive house next to a river, they
should be concerned about whether the house will be destroyed by a
flood. The flood stage for an average year, or the median flood stage,
is not relevant in such a setting.  Since a house should last for 100
years or more under normal conditions, in order to assess the risk of
loosing the house due to flooding one should consider an upper
quantile such as the 99th percentile of the flood stage.

The most extreme quantiles are the maximum (the 100th percentile) and
the minimum (the 0th percentile).  However these two quantiles are
seldom used in statistical data analysis, because they are very
unstable when calculated using a sample of data.  We will define this
notion of "instability" more precisely later, but intuitively, if you
have incomes for 1000 households in a state with 5 million households,
the maximum income in your data will generally be far less than the
maximum income in the state (since it is unlikely that your sample
includes the richest person in the state).  Moreover, if two people
obtain distinct datasets containing 1000 households from the state,
the maximum values in these two samples are likely to be quite
different.  This instability makes it hard to interpret the minimum
and maximum of the sample, since their values are likely to be quite
different from the corresponding minimum and maximum values in the
population.  With large samples it may be useful to examine the 99th
or even 99.9th percentile, but for a small sample, it is uncommon to
examine quantiles corresponding to proportions greater than 0.9, or
less than 0.1.

### Measures of dispersion derived from quantiles

Some useful summary statistics are formed by taking "linear
combinations" of quantiles.  These are sometimes referred to as
_L-statistics_.  The most common statistic of this type is the
_interquartile range_, or _IQR_.  The IQR is simply the difference
between the 75th percentile and the 25th percentile.  The _interdecile
range_ (_IDR_) is the difference between the 90th percentile and the
10th percentile.  The IQR and the IDR are both _measures of dispersion_,
also known as _measures of scale_.  Recall by contrast that the
median (which is also an L-statistic) is a "measure of location".
Measures of location and measures of scale are highly complementary to
each other and describe very different aspects of the data and
population.

Measures of dispersion describe the degree of variation or spread in
the data.  Roughly speaking, "dispersion" tells us whether
observations tend to fall far from each other, and far from the
central value of the dataset (this would be a highly dispersed
dataset), or whether they tend to fall close to each other, and close
to the central value of the dataset (this would be a dataset with low
dispersion).

As an example, suppose that we sample people from three locations and
determine each person's age.  In each location, we calculate the 10th,
25th, 50th, 75th, and 90th percentiles, and the IQR and IDR of the
ages.  The three locations are an elementary school, a nursing home,
and a grocery store.  We may obtain results like this:

| Location\Percentile      | 10   | 25  | 50  | 75  | 90  | IQR | IDR |
|   :--                    | --:  | --: | --: | --: | --: | --: | --: |
| __Elementary school__    |  4   | 6   | 7   | 8   | 39  |  2  | 35  |
| __Nursing home__         | 22   | 67  | 72  | 81  | 93  | 14  | 71  |
| __Grocery store__        | 11   | 24  | 39  | 51  | 71  | 27  | 60  |

The elementary school has a small median and a small IQR -- the
central half of the people in this elementary school are children
between the ages of 6 and 8.  At least 10 percent but not more than
25 percent of the people in this elementary school are much older,
these could be teachers and other adult workers.  The presence of
these older people impacts the
90th percentile, but not the 75th percentile of the data.  Thus the
IQR is not impacted by the presence of adults in the school (as long
as they comprise less than 25% of the school population), but the
IDR is affected, as long as at least 10% of the school population
consists of adults.
As a result, the IDR in this elementary school is much greater than the IQR.

The
residents of a nursing home are mostly rather old, but will generally
have a greater dispersion of ages compared to the students in an
elementary school, as reflected in the greater IQR for the nursing
home compared to the elementary school.  The nursing home staff likely
consists of people who are much younger
than the nursing home residents.  This leads to the 10th
percentile of the ages of people in the nursing home being much less than the
other reported quantiles.

Compared to the elementary school and the nursing home, the grocery store has an
intermediate median age.  It also has a very wide dispersion of ages, which
is evident from the reported measures of dispersion of ages as measured
by the IQR.

This example shows us that the median and the IQR are distinct
characteristics -- they can be similar or different, there is no
linkage between them.  On the other hand, the IQR and IDR are somewhat
related -- in particular the IDR cannot be smaller than the IQR.  Data
samples with a high IQR will tend to have a high IDR, and data samples
with a low IQR will tend to have a low IDR.  But these measures still
capture distinct information, and it is possible to have a sample with
an IDR that is much greater than its IQR, or to have a data sample in
which the IDR is equal to the IQR.

Yet another measure of dispersion that has a form that is similar to
the IQR and the IDR would be the _range_ of the data, defined to be
the maximum value minus the minimum value.  This statistic has the
advantage of being very easy to explain, and superficially is easy to
interpret.  However it is generally not a good measure of dispersion
for the same reasons that the maximum and minimum are somewhat
problematic quantiles to interpret, as discussed above.

The IQR and IDR are linear combinations of quantiles (L-statistics),
and hence have the same units as the quantiles that they are derived
from.  If we measure the income of US households in dollars, then the
IQR and IDR also have US dollars as their units.

### Median residuals and the MAD

Another useful data summary that can be derived using quantiles is the
_MAD_, or _median absolute deviation_.  The MAD, like the IQR and IDR,
is a measure of dispersion.  The MAD is calculated in two steps, and
is not directly a function of the quantiles.  To calculate the MAD, we
first _median center_ the data.  "Centering operations", including the
median centering operation that we discuss here, arise very commonly
in data science.  To median center the data, we simply calculate the
median of the data, then subtract this median from each data value.
The median centered data values are sometimes called _median
residuals_.

The median residuals have an important property, which is that if we
calculate the median of the median residuals, we are guaranteed to get
a result of zero.  That is, median centering removes the median from
the data, and recenters the data around zero.  Note also that the
median centering operation does not reduce or summarize the data -- if
we have 138 data points to begin with, we still have 138 data points
after median centering.

After calculating the median residuals, the second step in calculating
the MAD is to take the absolute value of each median residual.  These
are called, not surprisingly, the _absolute median residuals_.  The
third and final step of calculating the MAD is to take the median of
the absolute median residuals.  This third step is where the
summarization takes place, as we end up with only one number after
taking the median of the absolute median residuals.

The MAD, like the IQR and IDR, is a measure of dispersion. It tells us
how far a typical data value falls from the median of the data.  Note
that the word "far" implies distance, and distances are not signed
(i.e. they are always non-negative).  That is the reason that we take
the absolute value in the second step of computing the MAD.  In fact,
if we skipped this step, we would always get a value of zero following
the third step.

The MAD is a measure of dispersion, but it is not equal to the IQR or
IDR in general.  However data sets with large values for the IQR
and/or IDR will tend to have larger values for the MAD.  In practice, the
IQR, IDR, and MAD are all useful measures of dispersion.

### Measures of skew derived from quantiles

Another important statistic that can be derived from quantiles is the
_quantile skewness_, which is defined to be: ((Q3 - Q2) - (Q2 - Q1)) /
(Q3 - Q1), which simplifies to (Q3 - 2*Q2 + Q1) / (Q3 - Q1).  Note
that this is a ratio of two L-statistics, but is not an L-statistic
itself.  Here, Q2 is always the median, and Q1, Q3 are two quantiles
representing symmetric proportions around the median.  Most commonly,
Q1 is the 25th percentile and Q3 is the 75th percentile.  But
alternatively, we could specify Q1 to be the 10th percentile and Q3 to
be the 90th percentile.  For example, the quantile skew for household
income in Michigan using the 25th and 75th percentiles, based on the
data given above, is

(98000 - 2*55500 + 29000) / (98000 - 29000) = 0.231

The skewness tells us whether the p'th quantile and the (1-p)'th
quantile are equally far from the median.  In a _right skewed_
distribution, like that of income in most places, the upper quantiles
are much further from the median than the lower quantiles.  That is,
the difference between the 50th and 75th percentiles is much greater
than the difference between the 25th and 50th percentiles.  A right
skewed data set has a positive value for its quantile skewness, as
seen above for the Michigan household income data.

In a _left skewed_ distribution, the difference between the lower
quantiles and the median is greater than the difference between the
upper quantiles and the median.  Left skewed distributions are less
commonly encountered than right skewed distributions, but they do
occur.  A left skewed data set will have a negative value for its
quantile skewness.

The quantile skewness has another property that is common to many
statistics, namely that it is _scale invariant_.  If we multiply all
our data by a positive constant factor, say 100, then the numerator
and denominator of the quantile skewness will both change by a factor
of 100, and since the statistic is a ratio, this constant factor will
cancel out.  Thus, the quantile skewness is not impacted by scaling
the data by a positive constant.  If we report income in dollars, in
hundreds of dollars, or in pennies, we will get the same value when
calculating the quantile skew.  This property of being scale invariant
is sometimes referred to as being "dimension-free" or "dimensionless".

Data summaries based on moments
-------------------------------

A completely different class of data summaries is that based on
moments, rather than on quantiles.  A _moment_ is a data summary
formed by averaging.  The most basic moment is the _mean_, which is
simply the average of the data.  The mean can be used as a measure of
location or central tendency (like the median).  If our data are
{{<katex>}}x_1, x_2, \ldots, x_n{{</katex>}}, then the mean may be
written {{<katex>}}\bar{x}{{</katex>}}.  The concept of a moment is
much more general than just the familiar average value.  We can
produce many other moments by transforming the data, and taking the
mean of the transformed data.  For example, {{<katex>}}(x_1^2 + \cdots + x_n^2)/n{{</katex>}}
is also a moment.  We will see several useful examples of moments
below.

### Resistance

Moments and quantiles have overlapping use-cases.  In many settings,
it is reasonable to use either a quantile-based or a moment-based
summary statistic.  But it is important to keep the differing
properties of quantile-based and moment-based statistics in mind when
deciding which to use, and when interpreting your findings.  A
prominent difference between quantile-based and moment-based
statistics is captured by the notion of _resistance_.  A resistant
statistic is one that is not impacted by changing a few values, even
if they are changed to an extreme degree.  For example, if we have the
incomes for 100 people, and change the greatest income to one billion
dollars, the mean will change dramatically, but the median will not
change at all.  In general, quantile-based statistics are more
resistant than moment-based statistics.

### Mean residuals, variance, and the standard deviation

Above we discussed median centering the data, and the concept of a
median residual.  Analogously, we can _mean center_ the data by
subtracting the mean value from each data value.  The resulting
centered values are called _mean residuals_, or just _residuals_.  The
mean residual is the most commonly used residual (it is more commonly
encountered than the median residual).

A very important measure of dispersion called the _variance_ can be
calculated from the mean residuals.  To calculate the variance, we
simply average the squares of the mean residuals.  In words, the
variance is the "average squared distance from each data value to the
mean value".  As with the MAD, here we want to summarize unsigned,
"distance-like" values.  That is why we square the residuals prior to
averaging.  It should be easy to see that if all the values in our
dataset are zero, the variance is zero (as would be the MAD). On the
other hand, if the data values are well spread out, the variance and
the MAD will both be large.

One key difference between the variance and the IQR, IDR, or MAD is
the units.  As noted above, the MAD has the same units as the data.
This is due to the fact that taking the absolute value does not change
the units.  However, squaring the data also results in the units
becoming squared.  If the data are measured in years, then the
variance has "years-squared" as units.  If the data are measured in
meters, the variance has "meters-squared" as units (even though it
does not represent an area).

Since it is often desirable to have our summary statistics be either
dimensionless, or have the same units as the data, it is very common
to work with a statistic called the _standard deviation_ rather than
working directly with the variance.  The standard deviation is simply
obtained by taking the square root of the variance.  The standard
deviation, like the IQR, IDR, and MAD, has the same units as the data.

The variance and standard deviation are often defined slightly
differently than we are doing here -- specifically, the variance is
scaled by a factor of n/(n-1) relative to what we define here, where n
is the number of data points.  This is sometimes an important
distinction, but often has little impact on the result.  At this point
in the course, we will ignore this minor difference.

### Properties of different measures of dispersion

Many people find the IQR or MAD to be more intuitive measures of
dispersion than the standard deviation.  The standard deviation is
sometimes incorrectly described as being the "average distance from a
data value to the mean" -- it is actually "the square root of the
average squared distance of a data value to the mean".  On the other hand,
the MAD can be correctly described as being "the median distance from
a data value to the median".  In this sense, the MAD can be described
more concisely in everyday language.  The IQR is also easy to define
and interpret, since it is directly obtained from the sorted data.

The preference for the standard deviation is partly for historical
reasons, but it is also easier to mathematically derive properties of
the standard deviation, and of the variance, compared to
quantile-based statistics.  The reason for this is that we can expand
the square: if {{<katex>}}x_i{{</katex>}} is a data value and
{{<katex>}}\bar{x}{{</katex>}} is the overall mean, then
{{<katex>}}(x_i - \bar{x})^2 = x_i^2 - 2\bar{x} x_i +
\bar{x}^2{{</katex>}}.  With some algebra that we will not cover here,
we can arrive at an identity for the variance: the variance is equal
to the "mean of the squares minus the square of the mean":
{{<katex>}}(x_1^2 + \cdots + x_n^2)/n - \bar{x}^2{{</katex>}}.

The "mean of the squares" is obtained by squaring each data value, and
averaging the results, i.e., {{<katex>}}(x_1^2 + x_2^2 + \cdots +
x_n^2)/n{{</katex>}}.  The "square of the mean" is obtained by
calculating the mean in the usual way, and squaring it,
i.e. {{<katex>}}\bar{x}^2 = ((x_1 + x_2 + \cdots +
x_n)/n)^2{{</katex>}}.
The "mean of the squares" is an example of an _uncentered moment_.  We
can take the mean of the squared data, as we do here, or the mean of
the cubed data, and so on.  These are all examples of uncentered
moments.  A _centered moment_ is calculated from residuals.  As stated
above, the variance is the mean of the squared residuals.  Thus, the
variance is the most prominent example of a centered moment.

The IQR and MAD do not have any algebraic identities such as we just
obtained for the variance.  There is no way to algebraically
"expand" an absolute
value in the same way that we can expand a square.  This lack of
algebraic tractability is what made quantile-based statistics less
popular historically.  With computers, it is just as easy to work with
quantile-based statistics as it is to work with moment-based
statistics.  Both types of data summaries are useful, and they have
somewhat complementary properties.  We will use both types of
statistics throughout this course.

The notion of "resistance" stated above in regard to the median also
applies to the IQR and the MAD (which like the median, are based on
quantiles).  If we include a few extreme values in our data, the IQR
and MAD will be minimally impacted, whereas the standard deviation and
variance may change dramatically.  Arguably, this resistance is a good
thing, because extreme _outliers_ (a term that is often used but
impossible to define in a meaningful way) may be measurement errors or
data anomalies that are not related to what we are trying to study.
However it is certainly possible to have too much resistance -- if a
statistic is resistant to almost any changes to the data, it cannot be
used to learn from the data.

### Assessing skew using moments

Above we discussed the "quantile skew".  Its moment-based counterpart,
simply the "skew" or _coefficient of skewness_ is obtained as follows.
First, "Z-score" the data, which means that we replace each value
{{<katex>}}x_i{{</katex>}} with {{<katex>}}z_i =
(x_i-\bar{x})/\hat{\sigma}{{</katex>}}.  Here,
{{<katex>}}\bar{x}{{</katex>}} is the mean of the data, and
{{<katex>}}\hat{\sigma}{{</katex>}} is the standard deviation of the
data.  We will be using Z-scores throughout the course and will
discuss them in more detail later.  Once the Z-scores are obtained,
the coefficient of skewness is simply their third moment:
{{<katex>}}(z_1^3 + \cdots + z_n^3)/n{{</katex>}}.  Note that this
is both the central and noncentral third moment, since the
{{<katex>}}z_i{{</katex>}} have mean equal to zero.

The logic behind this moment-based definition of skew is as follows:
first, raising data to a high power accentuates the largest values
over the values that are of moderate or small magnitude.  Also,
raising the residuals to an odd power retains the sign of each
residual.  Thus, cubing the residuals gives us a new data set that has
exactly the same signs as the original data set, but with the largest
values exaggerated (i.e. they become relatively larger in magnitude
while maintaining their sign).  The average of the cubed residuals will
therefore tell us whether the largest values in the data set tend to
be positive, tend to be negative, or are equally likely to be positive
or negative.  This corresponds to the average cubed residual being
positive, negative, or zero, respectively.

Moments are one of the most powerful tools in statistics, and there
are many other summary statistics beyond what we have discussed here
that can be derived using moments.  We will return to the notion of
using moments in data analysis throughout the course.
