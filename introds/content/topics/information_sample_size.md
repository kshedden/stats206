Information and sample size
===========================

One of the fundamental premises of empirical research is that
as we collect more and more data, we should get a better understanding
of the evidence relating to our research question.
Here we will discuss some ways that
we can formalize how data contains "information", and how
this information accumulates with increasing sample sizes.

We will focus on the central statistical task of _estimation_.  In
statistics, an _estimate_ is a value, obtained from data, that is
used to learn something about the population.  In most cases, we
will use a statistic to estimate
its "population analogue".  The prototypical such setting is to use
the sample mean (average) to _estimate_ the population mean (expected value).

It is important to keep in mind that the sample mean
is a random quantity, since it generally will
change if we repeat our data collection.  On the other
hand, the population mean is not random, it is a constant.  A primary goal for collecting data
is often to use averaging to reduce the "noise" in the sample
statistic (e.g. the sample mean), so that it becomes a more _precise_
estimate of its population analogue.

As an example, suppose that we are interested in determining the boiling point of acetic acid,
which happens to be 117.9 C.  We use an experimental approach in which we heat liquid
acetic acid until it appears to boil, then record the temperature using a well-calibrated
centigrade thermometer.  Each "trial" of our experiment will yield one value,
and since this is a crude experimental approach, these values may deviate substantially
from the truth.  For example, the first five measurements might be 116, 129, 124,
118, and 118.  As noted above, it is very natural to use the average of multiple measurements
to improve the precision of the estimates.

Now imagine replicating our study at a fixed sample size n, say n=5.
If we were to replicate our study five times,
we would get five data sets, and five sample means, as shown below.


|       |     |     |     |     |     | Mean     |
|-------|-----|-----|-----|-----|-----|----------|
| Set 1 | 109 | 116 | 123 | 118 | 124 | 118      |
| Set 2 | 125 | 122 | 123 | 120 | 106 | 119      |
| Set 3 | 109 | 114 | 122 | 111 | 127 | 117      |
| Set 4 | 130 | 122 | 112 | 121 | 124 | 122      |
| Set 5 | 108 | 113 | 113 | 120 | 115 | 114      |

Without doing any calculations, we can see that the individual measurements are much more
dispersed than the sample means.  This illustrates how precision is improved
by collecting multiple data points and averaging.

Previously we have discussed the use of the variance (the average squared deviation
from the mean) to quantify the dispersion in
a collection of data values.  The variance of the 25 individual
boiling point measurements in the table above is around 43. Since the sample mean,
shown in the final column of the table, is a
statistic, it is random and hence has its own variance.  However the repeated values
of the sample mean will be less dispersed than the repeated values of the individual
measurements.  The five sample means shown above, each of which is the average of five
repeated observations of the boiling point of acetic acid, have a variance that is around 9.

There is an important theoretical fact that underlies the above discussion.
If we average n repeated observations of the same quantity, then the variance of
this average value is 1/n times the variance of the individual measurements.  In
the example above, this theoretical fact is approximately satisfied, since 43/9 ~ 5.
The relationship is
not satisfied exactly because we only took five data sets in our illustration.  For the
relationship to hold exactly, we would need to have infinitely many data
samples, each of size 5.  This "variance scaling relationship"
is an extremely useful indication of how and why we get more information from larger samples,
and arguably
is the single most important theoretical fact that underlies the practice
of statistics and data science.

It is important to keep in mind that in practice we never collect multiple data
sets as in the illustration above.  If we had 25 observations, we would treat
that as one data set of size 25, not 5 data sets of size 5.  However much of statistics
is based on the thought exercise of imagining how much your results might differ
if you were to repeat your data collection and data analysis.  The illustration
above pertains to a setting where we can only collect five observations.  The
numerical and theoretical results discussed here allow us to quantify how much
the results of our analysis would vary if we (hypothetically) were to replicate it, even though
in practice we would not do so.

Variance plays a central role in statistics, but it is important to note that in
different settings, we may benefit from variance, or it may challenge us by
making it more difficult to answer our research questions.  When
our goal is to estimate a population quantity, we always want the variance
of our estimate to be as small as possible.  Thus, dividing the variance of the individual
measurements by the sample size n is helpful to us, and shows that the variance can be made as small
as we like as long as we can acquire a sufficiently large sample size.
The variance of a statistic and the variance of the data values are both variances.
But their purpose and interpretation are quite different.  Sometimes, the variance
of a statistic is called the _sampling variance_, to clearly distinguish it from the
variance of the data.

When we introduced the variance earlier in the course, we noted that
it has different units than the data.  If the data are in degrees
centigrade, as is the case here, then the variance has units of degrees centigrade
squared.  This can make it difficult to interpret the variance in practice,
and motivates the use of the standard deviation, which is simply the square root
of the variance.  The standard deviation of
a statistic is often called the _standard error_, and in particular,
when our statistic is the mean, it may be referred to as the _standard error of
the mean_, or SEM.

The variance scaling relationship gives rise to an analogous
"standard error scaling relationship", which is that the standard error (or standard
deviation) of the sample mean, based on averaging n independent and identically
distributed observations, is {{<katex>}}1/\sqrt{n}{{</katex>}} times the
standard deviation of the individual data values.
The standard error scaling relationship gives a better sense of what is really
happening, since standard error, like standard deviation, is in the same units as the data.  To
reduce the standard error of an estimate by a factor of two, we need the factor
{{<katex>}}1/\sqrt{n}{{</katex>}}
to become smaller by a factor of at least 1/2, which means that we need to increase n by a factor of 4.
The standard error scaling relationship explains why modest increases in sample size don't always
lead to large gains in insight.  If a study aiming to address a research
question yields ambiguous
results because the confidence intervals are too wide to be informative,
the next study should generally have a substantially larger sample size
to have hope of clarifying things.  Repeating an ambiguous study using a similar
or slightly larger sample size is unlikely to improve our understanding.

Law of large numbers
--------------------

The law of large numbers is a mathematical theorem that justifies much
of the practice of data science and statistics.  Above we saw that the
precision of a statistic grows as we collect more data, with the standard error
scaling by a factor of {{<katex>}}1/\sqrt{n}{{</katex>}} relative to the sample size {{<katex>}}n{{</katex>}}.  The
law of large numbers provides further support for the notion that with
enough samples, we can learn anything we want to learn about the population,
with minimal uncertainty.

Roughly speaking, the law of large numbers says that as we collect more and more data, the value
of any given statistic will eventually become arbitrarily close to
its population analogue.  Our goal here is only to provide an intuitive
view on the meaning of the law of large numbers.  There are several
versions of the law of large numbers, and precise statements
involve limits, and will not be discussed further in this
course.

In the example discussed above, where we aim to estimate the boiling point
of acetic acid, we can imagine taking the average of larger and larger
numbers of trials.  The law of large numbers says, for example, that if
we wish to be accurate to within 1 degree C, for a large enough sample
we will reach that point.  Similarly, if we want to be accurate to
within 0.1 degrees C, for a large enough sample, we will reach that point
as well.  For any "tolerance" that is not exactly zero, the law of large
numbers gaurantees that the average of
sufficiently many points will fall within the tolerance relative to
the target value.
