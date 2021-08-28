Data transformations
====================

When analyzing quantitative data, it is important to consider the
scale that is used to use to represent the data.  Sometimes the scale
that is most familiar, or easiest to measure, is not the scale that is
most informative when it comes to analyzing and interpreting the data.
In such situations, applying a _transformation_ to the data helps to
make it more informative.  Here we discuss this topic, using several
examples to illustrate.

Transforming data point-wise
----------------------------

### Reciprocal transformations

In the United States, the fuel efficiency of vehicles is usually
quantified in "MPG" (Miles per Gallon) -- the number of miles that can
be driven using one gallon of fuel.  These numbers typically range
from around 20 up to 40 or more for cars and light trucks, but are
lower for heavier vehicles.  Suppose that a shipping company would
like to reduce its fuel consumption.  Such a company would tend to use
heavier vehicles that consume more fuel.  Imagine that the shipping
company has 1000 older trucks with an 8 MPG rating, and 1000 newer
trucks with a 16 MPG rating.  For simplicity, imagine that the older
and newer trucks can carry the same amount of goods, and that each of
these 2000 trucks is driven 100 miles per day.  The average MPG rating
for this fleet of trucks is 12 MPG (the average of 8 and 16), but is
this the right way to summarize these data?  The total fuel consumed
per day by one of the heavier trucks is 100/8 = 12.5 gallons, and the
total fuel consumed per day by one of the lighter trucks is 100/16 =
6.25 gallons. Thus, the average amount of fuel consumed per day is
9.375 gallons, which corresponds to 100/9.375 ~ 10.7 miles per
gallon.  Note that we have obtained two different average values, 12
and 10.7, using the same data, but calculating the average on two
different scales.

Since the shipping company will likely not change the number of miles
traveled if they change the vehicles in their fleet, and a gallon of
fuel costs the same whether you put it in an efficient truck or an
inefficient truck, arguably, the most relevant statistic for
summarizing the fuel efficiency of the shipping company's fleet is
10.7 (the average gallons per mile), not 12 (the average miles per gallon).
This reflects the amount of money that the company will
spend on fuel.  Both of these summary statistics are averages, but
they are averages taken on different scales.  It turns out in this
case that although we may collect the data on fuel economy using units
of miles per gallon, units of "gallons per mile" is a more appropriate
scale for analysis.  Thus, we should take the reciprocal (1/x) of each
data value prior to averaging, and then, if we wish, take the
reciprocal of this average in order to present our results on the
familiar MPG scale.  This is exactly what was done above to obtain the
10.7 MPG value.

### Logarithm transformations

The reciprocal transformation is just one of many different
mathematical transformations that may be usefully applied to data
prior to analysis.  It is not the most common such transformation --
that would be the logarithm.  The logarithm is a very powerful tool
that dramatically simplifies many mathematical operations.  The key
property of a logarithm is that it converts multiplication into
addition: {{<katex>}}\log(a\cdot b) = \log(a) + \log(b){{</katex>}}.
This turns out to be very useful when analyzing data.

Suppose we are interested in state-level income in the United States.
For the sake of illustration, imagine that we have two states, A and
B, that have the same number of residents.  Income varies within state
A and within state B, but imagine that every person in state A has a
counterpart in state B with the same occupation, whose income is
exactly {{<katex>}}f{{</katex>}} times different, for some constant
{{<katex>}}f > 0{{</katex>}}.  This would imply that a barber in state
B earns {{<katex>}}f{{</katex>}} times the income of a barber in state
A, a teacher in state B earns {{<katex>}}f{{</katex>}} times the
income of a teacher in state A, and so on.

Let {{<katex>}}x_i{{</katex>}} denote the income of the i'th resident
of state A, and let {{<katex>}}y_i{{</katex>}} denote the income of
their counterpart in state B.  Then {{<katex>}}y_i = f
x_i{{</katex>}}, and hence {{<katex>}}\log(y_i) = \log(f) +
\log(x_i){{</katex>}}.  Thus, the average log-scale income in state B
will be {{<katex>}}\log(f){{</katex>}} units different (in an additive
sense) than the average log-scale income in state A.  Since
{{<katex>}}\log(1) = 0{{</katex>}}, if {{<katex>}}f=1{{</katex>}} then
the average log-scale incomes in the two states are equal.  Similarly,
{{<katex>}}\log(f){{</katex>}} is greater than 0 or less than 0 when
when {{<katex>}}f{{</katex>}} is greater than 1, or less than 1,
respectively.  Thus the sign of {{<katex>}}\log(f){{</katex>}} is
negative, zero, or positive based on whether the income in state B
tends to be less than, equal to, or greater than the income in state
A.

The importance of the log transformation is that it captures a
multiplicative, rather than an additive relationship when comparing
two data sets.  This is often (but not always) more informative when
dealing with _heterogeneous_ populations.  The notion of heterogeneity
is extremely important and will arise throughout this course.  The key
point here is that in the United States at this time, certain
professions earn much greater income than others, and these
differences tend to exist in every state.  Every state has barbers,
teachers, lawyers, and heart surgeons, and all do essential work, but
heart surgeons earn more than barbers in nearly every case.  When
comparing two states, the overall state incomes can differ for two
reasons.  One is that one state may have a higher fraction of people
in high-earning jobs than another state.  The other is that people in
the same job types may earn different incomes in different states.
Comparing incomes on the log scale is arguably the most natural
analytic approach, especially if the latter effect dominates.

Another setting where log transformations play an important role is
when working with data from systems that exhibit exponential growth.
Many real-world processes can exhibit exponential growth, including
pandemics and investment returns.  In the real world, exponential
growth cannot persist for long, but in some regimes, an exponential
growth model is a good way to describe the behavior of a system.  If a
system exhibits exponential growth, in many cases log transforming the
data induces linear behavior.  Thus, log transformations can be very
useful when working with data from systems of this type.

Yet another situation where log transforms can be effective is if we
are looking at relationships within or between quantities that vary
over multiple orders of magnitude.  For example, if we look at the
population size and gross domestic product of each country in the
world, it is natural to consider these quantities on a logarithmic
scale.  If country A has twice as many people as country B, then
country A would be expected to have twice the economic activity of
country B (assuming their economic structures are similar).  This is
because production and consumption by humans is the driver of economic
activity.  As a result of this relationship, countries with similar
levels of economic activity will appear along the same line through
the origin when considering a scatterplot of log GDP versus log
population size.

A final reason that we might log-transform data is to induce symmetry
in the distribution of the data.  We have discussed the concept of a
distribution being skewed.  Many variables, such as household income,
are quite skewed on their natural scale (units of money), but
reasonably symmetric after log transforming the income values.  Skewed
distributions are not bad, and it is not necessary to always seek to
symmetrize every skewed distribution that you encounter.  However, in
some cases that we will discuss later in the course, it can be
valuable to work with symmetrically-distributed values, and in many
cases log transforming the data will achieve this goal.

### Geometric and harmonic means

Suppose we calculate mean of log-transformed data, and then
exponentiate this mean value to return the result to the original
scale.  This turns out to be exactly equivalent to calculating the
product of the n data values, and then taking the n'th root of this
product.  For example, if we have three data values {{<katex>}}x_1,
x_2, x_3{{</katex>}}, then we would get

{{<katex>}}\exp((\log(x_1) +\log(x_2) + \log(x_3))/3) = (x_1\cdot
x_2\cdot x_3)^{1/3}{{</katex>}}.

This is in contrast to the usual mean in which we take {{<katex>}}(x_1
+ x_2 + x_3)/3{{</katex>}}.  These two "mean values" are referred to
as the _geometric mean_ and the _arithmetic mean_, respectively.
There is a third such "classical mean" called the _harmonic mean_,
which for three data values would be

{{<katex>}}1/((1/x_1 + 1/x_2 + 1/x_3)/3){{</katex>}}.

The harmonic mean is the reciprocal of the arithmetic mean of the
reciprocals of the data values --
exactly what we did above when considering the fuel economies of
vehicles.

We see here that the three "classical means" -- arithmetic, geometric,
and harmonic, can be obtained by taking the arithmetic mean of
transformed data, then transforming this result.  In this course, we
will take the perspective that there is really only one mean -- the
arithmetic mean (i.e. the simple average), and we will call it simply
the "mean".  The geometric mean and harmonic mean can be obtained from
the arithmetic mean by calculating the arithmetic mean using
transformed data -- log transformed data for the geometric mean, and
reciprocal transformed data for the harmonic mean.


Centering, scaling, and normalizing transformations
---------------------------------------------------

The transformations discussed in the previous section are _point-wise_
transformations, because they transform each element individually,
without reference to the other values.  The next class of
transformations that we consider do not have this property.

A large class of transformations has the goal of standardizing data in
some way.  We have already encountered "residuals" which are formed by
subtracting either the overall mean or the overall median from each
data value.  Forming residuals is a _centering_ transformation, in
that it results in the data being distributed around zero -- that is,
zero falls at some point within the range of data values.  If the
overall central value is not important for a given analysis, it may
make sense to center the data.  Note that since the mean or median are
calculated using all of the data, the process of forming residuals is
not a point-wise transformation as defined above.

Centering the data places zero within the range of the data, but two
centered data sets can have very different levels of dispersion.
Thus, in some cases it is valuable to go one step further and
transform the data to have a specific, reference level of dispersion.
This can be achieved by taking the centered data, and dividing it by
some measure of dispersion such as the standard deviation, the IQR, or
the MAD (note that it would not make sense to divide by the variance,
since this has different units from the the data).  If we divide the
data by a measure of dispersion, then the transformed data will have
"unit dispersion", i.e. a dispersion value of 1 with respect to that
measure.  For example, if we divide the data by the IQR, then the
transformed data will have an IQR of 1.  This type of transformation
is called a _scaling_ transformation.

Usually, a scaling transformation is applied after first applying a
centering transformation.  The combined effect of a centering and
scaling transformation may be called a _normalizing_ or
_standardizing_ transformation.  Note that these transformations have
a linear form, since they involve subtraction and division by
constants.  A linear transformation plays a different role than a
non-linear transformation, such as the log-transformation that we
discussed above.

When standardizing data by applying both a centering and a scaling
transformation, it is most common to use either a quantile-based
transformation for both centering and scaling, or a moment-based
transformation for both centering and scaling.  It is less common to
mix, say, a quantile-based transformation for centering with a
moment-based transformation for scaling.

Normalizing transformations are often said to convert the data to
_Z-scores_.  A Z-score is a linearly transformed version of a dataset
that has location equal to 0 and dispersion equal to 1.  The location
is typically quantified using either the mean or the median, and the
dispersion is typically quantified using the standard deviation, MAD,
or IQR.

Differencing transformations
----------------------------

In many settings, our research question focuses more on change than on
absolute levels.  For example, we may be interested in the difference
in the HIV infection rate between 2020 and 2015, not the absolute HIV
infection rates in either year.  Suppose we have data on the level of
HIV infection among adults in each US county, in 2020 and 2015.  A
simple transformation that would make sense in many contexts would be
to subtract the HIV infection rate in 2015 from the HIV infection rate
in 2020, for each county.  This reduces the data to "change scores",
which are more relevant for the stated research question.

Another setting where it might make sense to work with
difference-transformed data would be in the setting of a clinical trial of
a medical treatment.  Suppose we are investigating a drug that is intended
to lower blood pressure.  Each participants blood pressure prior to
the beginning of the trial was noted, then a second blood pressure
measurement was obtained after the subject took the drug for six
months.  For example, a given subject may have had systolic blood
pressure (SBP) equal to 155 before taking the drug, and 138 after
taking the drug for six months.  The change score for this subject is
155 - 138 = 17.

Occasionally it may be useful to think in terms of ratios rather than
differences.  Imagine that a chain of stores ran a
promotional campaign, and recorded the total sales within each store
before and after the campaign.  As examples, one store might have seen
its sales change from 800 to 1000 (USD/day) and another store might
have seen its sales change from 8000 to 9000 (USD/day).  The latter
store had a 1000 USD/day increase, and the former store had a 200 USD/day
increase.  However, the former store had a much lower volume of sales
prior to the promotion, and it would likely be unrealistic to imagine
it having a 1000 USD/day increase due only to one promotion.  A ratio
transformation of the data would represent the first store's sales
change as 1000/800 ~ 1.25, and the second store's sales change as
9000/8000 ~1.125.  The change scores based on ratios show that the
first store outperformed the second store, whereas the change scores
based on differences show the opposite.

In many cases, we can take advantage of the properties of the log
transformation, allowing us to avoid forming ratios from the data.
The logarithm of a ratio is simply the difference of the
log-transformed numerator and denominator: log(a/b) = log(a)- log(b).
Thus, if we log transform the sales data for each store, then an
analysis of differences applied to the log-scale data would be
equivalent to an analysis of ratios of the original data.
