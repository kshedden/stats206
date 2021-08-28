Graphical summaries of data
===========================

Many powerful approaches to data analysis communicate their findings
via graphs. These are an important counterpart to data analysis
approaches that communicate their findings via numbers or tabless.

Here we will illustrate some of the most common approaches for
graphical data analysis.  Throughout this discussion, it is important
to remember that graphical data analysis methods are subject to the
same principles as non-graphical methods.  A graph can be either
informative or misleading, just like any other type of statistical
result.  To understand whether a graph is informative, we should
consider the following:

* Every graph should provide insight into the specific research question that
is the overall goal of the data analysis.

* The graph is constructed using a sample of data, but the purpose of the graph is to
learn about the population that the sample represents.

* What statistical principal or concept is the graph based on?

* What are the theoretical properties of any numerical summaries
that are shown in the graph?

Almost every statistical graphic conveys a statistical concept that
can be defined in a non-graphical manner.  Graphs may show
associations, location, dispersion, tails, conditioning, or almost any
other statistical feature of the data or population.  Graphs make it
easier for the viewer to digest such information, but when
interpreting a graph it is always important to keep in mind the
specific statistical concept on which the graph is based.

Statistical graphics have an aesthetic dimension that is usually not
evident when presenting findings through, say, tables.  Our goal here
is to focus on the content of graphs, not their aesthetic properties.
Very crude graphs that have deep content are much more informative
than beautiful graphs that convey only superficial content.  In recent
years, the field of _infographics_ has grown rapidly.  There is no
sharp line dividing infographics from statistical graphs, however in
general, the former tend to convey relatively simple insights in an
aesthetically engaging way, while the latter aim to convey deeper and
more subtle insight, with less focus on presentation.


Challenges and limitations of graphs
------------------------------------

One of the main challenges in statistical graphics is to fit the
greatest amount of useful information into a single graph, while
allowing the graph to remain interpretable.  More complex graphs
can suffer from _overplotting_, in which the
plot elements are so crowded on the page that they fall on top of each
other.  This can limit the legibility of plots formed from large
datasets unless a great deal of preliminary summarization of the data
is performed.

Another challenge that arises in graphing complex datasets is that
most graphs are two-dimensional, so that they can be viewed on a screen (or
printed on paper).  Some graphing techniques extend to three
dimensions, but many datasets have a natural dimensionality that is
much greater than 2 or 3.  A few methods for graphing work around this,
but require more effort from the person viewing the graph.

Boxplots
--------

Boxplots are a graphical representation of the distribution of a
single quantitative variable.  A boxplot is based on a set of
quantiles calculated using a sample of data.  Below is an example of a
single boxplot, drawn horizontally, showing the distribution of income
values based on a sample of 100 individuals.

![Boxplot-1](/~kshedden/introds/images/bp1.svg)

The "box" in a boxplot (shaded blue above) spans from the 25th to the
75th percentiles of the data, with an additional line drawn cross-wise
through the box at the median.  "Whiskers" extend from either end of
the box, and are intended to cover the range of the data, excluding
"outliers".

The concept of an outlier is extremely problematic and no generically
useful definition of outliers has been proposed.  For the purpose of
drawing a boxplot, the most common convention is to plot the upper
(right-most) whisker at the 75th percentile plus 1.5 times the IQR, or
to the greatest data value less than this quantity.  Analogously, the
lower (left-most) whisker is drawn at the 25th percentile minus 1.5
times the IQR, or to the least data value greater than this quantity.
Finally, individual points sometimes called "fliers" are drawn
corresponding to any value that falls outside the range spanned by the
whiskers.  A single box-plot, as above, is often drawn horizontally,
but may also be drawn vertically.

There are many alternative ways of defining the locations of the
whiskers in a boxplot.  The approach described above is most common,
and is chosen so that with "light tailed" distributions, well under 1%
of the data will fall outside of of the whiskers.

The boxplot above shows a right-skewed distribution.  This is evident
because the upper whisker is further from the box than the lower
whisker.  Also, within the box, the median is closer to the lower side
of the box than to the upper side of the box.  Overall, the lower
quantiles are more compressed, and the upper quantiles are more spread
out, which is a feature of right-skewed distributions.

Side-by-side boxplots
---------------------

Boxplots are commonly used to compare distributions.  A "side-by-side"
or "grouped" boxplot is a collection of boxplots drawn for different
subsets of data, plotted on the same axes.  These subsets usually
result from a stratification of the data, according to some
stratifying factor that partially accounts for the heterogeneity
within the population of interest.  For example, below we consider
boxplots showing the distribution of income, stratified by sex.

![Boxplot-2](/~kshedden/introds/images/bp2.svg)

Histograms
----------

A histogram is a very familiar way to visualize quantitative data.
A histogram is
constructed by breaking the range of the values into bins and counting
the number (or proportion) of observations that fall into each bin.
The shape of a histogram shows visually how likely we are to observe
data value in each part of the range.  We are more likely to observe
values where the histogram bars are higher, and less likely to observe
values where the histogram bars are lower.

Histograms closely resemble "bar charts", but with the added
statistical aspect that the goal is to capture the _density_
at each possible point in the population.
"Density" is a measure of how commonly we observe data
"near", rather than "at" a point.  For example, the density of
household incomes at 45,000 USD would not be the exact number
or frequency of households with this income.  Instead, it
reflects the frequency of households that have an income
near 45,000 USD.

The width of the histogram bars (or "bins") is a _parameter_ of the
method.  There are "rules of thumb" for setting the width of the bins,
but no single such rule is used universally.  Two such rules are
"Scott's rule", which uses bins of width
{{<katex>}}3.49\cdot\sigma/n^{1/3}{{</katex>}}, where
{{<katex>}}\sigma{{</katex>}} is the standard deviation, and
{{<katex>}}n{{</katex>}} is the sample size (number of observations),
and the "Freedman-Diaconis rule", which uses bins of width
{{<katex>}}2\cdot{\rm IQR}/n^{1/3}{{</katex>}}.  Note that in both
cases, the bins are narrower when the sample size is larger.  Narrower
bins allow us to see the finer scale structure of the distribution,
but if the sample size is small, narrow bins produce unstable results
because each bin contains only a very few observations.  The above
rules for calculating the bin width aim to compromise between these
two issues.

A histogram can be used to assess almost any property of a
distribution.  The common measures of location and dispersion can be
judged from visual inspection of the histogram.  As always, we should
remember that features of the histogram may not always reflect
features of the population from which the data were sampled.  For
example, a histogram may show two modes (i.e. is _bimodal_) even when
the underlying distribution only has one mode (i.e. is _unimodal_).
Moreover, the number of modes in a histogram can change as the bin
width is varied.

Histograms are easy to communicate about, but may not be
effective when working with small samples, where
they can accentuate non-generalizable features of the sample
(i.e. characteristics of the sample that are not present in the
population).  This is reflected in the following mathematical fact.
For many statistics, if we wish to reduce the error relative to
the population value of the statistic by a factor of two, we need
to increase the sample size by a factor of four.  In the case
where we are aiming to estimate a density, in order to reduce
the error by a factor of two, we need to increase the sample size
by a factor of eight.

![Histogram-0](/~kshedden/introds/images/hist0.svg)

With a sufficiently large collection of representative data, the
histogram should closely match the population's _probability density
function_ (PDF).  The PDF is
usually a smooth curve, rather than a series of steps as in a
histogram.  This fact inspired the development of a modified version of a
histogram that presents us with a smooth curve instead of a series of
steps.  This technique is
called _kernel density estimation_ (_KDE_).  It produces graphs such
as shown below.

![Histogram-1](/~kshedden/introds/images/hist1.svg)

Kernel density estimates may provide a somewhat more accurate
estimation of the underlying density function compared to a histogram.
But like a histogram, they can be unstable and produce artifacts.  For
example, the _KDE_ above shows positive density for negative income
values, even though all of the income values used to fit the KDE were
positive (in some cases, income can take a negative value, but in this
case no such values were present).  More advanced KDE methods not used
here can mitigate this issue.

One advantage of using a KDE rather than a histogram is that it is
easier to overlay multiple KDEs on the same axes for comparison
without too much overplotting.  This might allow us to compare, say,
the distributions of female and male incomes as follows.

![Histogram-2](/~kshedden/introds/images/hist2.svg)

Quantile plots
--------------

A _quantile plot_ is a plot of the pairs {{<katex>}}(p,
q_p){{</katex>}}, where {{<katex>}}q_p{{</katex>}} is the p'th
quantile of a collection of quantitative values.  Since
{{<katex>}}p{{</katex>}} can be any real number between 0 and 1, the
graph of these pairs constitutes a function.  By construction, this
must be a non-decreasing function.  A quantile plot contains essentially
the same information as a histogram, but is represented in a very
different way.  Note that unlike the histogram, for which the bin
width is a parameter that must be selected, there is no such parameter
in the quantile plot.  Arguably, the quantile plot is a more stable
and informative summary of a sample, especially if the sample size is
moderate.  However most people are more comfortable interpreting
histograms than quantile functions.

As an example, the following plot shows simulated systolic blood
pressure values for a sample of females and a sample of males.  In this case, at
every probability point {{<katex>}}p{{</katex>}}, the blood pressure quantile for males is
greater than the blood pressure quantile for females, indicating that
male blood pressure is "stochastically greater" than female blood pressure.

![Quantileplot-1](/~kshedden/introds/images/qp1.svg)

Below is another example that shows two quantile functions, but in this
case the quantile functions cross.  As a result, there is no
"stochastic ordering" between the data for females and for males.
Also note that the quantile curve for females is steeper than the
curve for males, indicating that the female blood pressure values are
more dispersed than those for the males.

![Quantileplot-1](/~kshedden/introds/images/qp2.svg)


Quantile-quantile plots
-----------------------

A _quantile-quantile plot_, or _QQ plot_, is a plot based on quantiles
that is used to compare two distributions.  Recall that a quantile
plot plots the pairs {{<katex>}}(p, q_p){{</katex>}} for one sample.
A QQ plot plots the pairs {{<katex>}}(q^{(1)}_p,
q^{(2)}_p){{</katex>}}, where {{<katex>}}q^{(1)}_p{{</katex>}} are the
quantiles for the first sample, and {{<katex>}}q^{(2)}_p{{</katex>}}
are the quantiles for the second sample.  In a QQ-plot, the value of p
is "implicit" -- each point on the graph corresponds to a specific
value of p, but you cannot see what this value is by inspecting the
graph.

As an example, suppose we are comparing the number of minutes of sleep
during one night for teenagers and adults.  This might give us the
following QQ-plot:

![QQplot-1](/~kshedden/introds/images/qqp1.svg)

The above QQ-plot shows us that teenagers tend to sleep longer than
adults, and this is especially true at the upper end of the range.
The QQ-plot approximately passes through the point (600, 800), meaning
that for some probability p, 600 is the p'th quantile for adults and
800 is the p'th quantile for teenagers.

The slope of the curve in the QQ-plot reflects the relative levels of
dispersion in the two distributions being compared.  Since the slope
of the curve in the above QQ-plot is greater than that of the diagonal
reference line, it follows that the values plotted on the vertical
axis (teenager's values) are more dispersed than the values plotted on
the horizontal axis (adult's values).

An important property of a QQ-plot is that if the plot shows a linear
relationship between the quantiles, then the two distributions are
related via a _location/scale transformation_.  That is, there is a
linear function {{<katex>}}a + bx{{</katex>}} that maps one
distribution to the other.  In the example above, there is a
substantial amount of curvature in the graph, so it does not seem to
be the case that the sleep durations for adults and teenagers are
related via a location/scale transformation.

Dot plots
---------

Dot plots display quantitative data that are stratified into groups.
One axis of the plot is used to display the quantitative measure, and
the other axis is used to separate the results for different groups.
A series of parallel "guide lines" are used to show which points
belong to each group.  Dot plots are often used to display a
collection of numerical summary statistics in visual form.  Sometimes
people say that dot plots are used to "convert tables into graphs".
Due to overplotting, dot plots are less commonly used to show raw
data.  The example below shows how dot plots can be used to display
the median age stratified by sex, for people living in each of eleven
countries.

![Dotplot-1](/~kshedden/introds/images/dp1.svg)

The plot above shows that the median age for females is greater than
the median age for males in every country.  This is mainly due to
females having longer life expectancies than males.  We also see that
some countries have much lower median ages for both sexes compared to
other countries.  Countries that have recently had high birth rates,
such as Ethiopia and Nigeria, tend to have much lower median ages than
countries with lower birth rates, such as Japan.

Scatterplots
------------

A scatterplot is a very widely-used method for visualizing bivariate
data.  They have many uses, but the most relevant for us is to plot
the joint (empirical) distribution of two quantitative values.  As an
example, suppose that we observe paired data values giving the annual
minimum and annual maximum temperature at a location.  We could view
these data with a scatterplot, placing, say, the minimum temperature
value on the horizontal (x) axis, and the maximum temperature value on
the vertical (y) axis.  The number of points is the sample size, here
being the number of locations for which temperature data are
available.  A possible graph of this type is shown below.

![Scatterplot-0](/~kshedden/introds/images/sp0.svg)

Several characteristics of the relationship between minimum and
maximum temperature are evident from the plot above.  The maximum
temperature at each location is at least as large as the minimum
temperature.  There is a positive association in which locations with
a lower minimum temperature tend to have a lower maximum temperature
compared to places with a higher maximum temperature, but there is a
lot of scatter around this trend.  Warmer places tend to have a
smaller range between their minimum and maximum temperatures.
Concretely, locations on the equator and at low elevation, such as
Singapore, have relatively constant temperature throughout the year.
Locations near the center of large continents, like Winnipeg, Canada,
can have extremely cold winters and also rather hot summers.  Coastal
regions that are far from the equator, such as Dublin, Ireland, have
mild winters and cool summers.

To aid in interpreting a scatterplot, it is useful to plot a smooth
curve that runs through the center of the data.  This is called
_scatterplot smoothing_, and can be accomplished with several
algorithms, one of which is known as _lowess_.  The population
analogue of a scatterplot smooth is the _conditional mean_, or
_conditional expectation_, denoted {{<katex>}}E[Y|X=x]{{</katex>}},
for the conditional mean of {{<katex>}}Y{{</katex>}} given
{{<katex>}}X{{</katex>}}.  The conditional mean is a function
of {{<katex>}}x{{</katex>}}, and can be evaluated at any point
{{<katex>}}x{{</katex>}} in the domain of {{<katex>}}X{{</katex>}}.
The conditional mean is (roughly speaking), the average of all
values of {{<katex>}}Y{{</katex>}} whose corresponding value
of {{<katex>}}X{{</katex>}} is near {{<katex>}}x{{</katex>}}.

The plot below adds the estimated conditional mean (orange curve) to the
scatterplot of temperature data discussed above.  The conditional mean curve is increasing,
showing that, as noted above, a location with lower annual minimum
temperature tends on average to have a lower annual maximum temperature (relative
to other locations).

![Scatterplot-1](/~kshedden/introds/images/sp1.svg)

Time series plots
-----------------

Some data have a _serial_ structure, meaning that the values are observed
with an ordering. Very often, such observations are made over time, which
gives us _time series_ or _longitudinal_ data.  Sometimes we observe
a single time series over a long period of time, such as the value of
a commodity in a market recorded every day over many years.  Other times,
we observe many short time series recorded irregularly.  We may plot
these time series together, leading to what is sometimes called
a "spaghetti plot".  For
example, in a study of human growth, we may observe measurements of
the body weight of research subjects at various ages, giving us
the spaghetti plot below:

![Spaghetti-1](/~kshedden/introds/images/spag1.svg)

Parallel coordinate plots
-------------------------

Scatterplots in the plane are limited to two dimensions. Various
techniques have been developed to overcome this limitation, one of
which is the _parallel coordinate plot_.  A parallel coordinate plot
places the coordinate axes for the multiple dimensions as parallel
lines, rather than as perpendicular lines.  Using parallel lines means
that data for far more than two or three variables can be placed on a
single page.

Below is an example of a parallel coordinates plot, showing four
attributes of a set of ten countries.  A scatterplot of these points
would live in four-dimensional space, which is quite challenging to
visualize directly.  Note that the attributes are converted to
Z-scores, which is common in a parallel coordinates plot when the
variables being plotted fall in very different ranges.  The plot shows
us that the life expectancies for females and for males are quite
similar -- the country with the highest life expectancy for females
also has the highest life expectancy for males, and the country with
the lowest life expectancy for females also has the lowest life
expectancy for males.  There is also a substantial positive
relationship between the economic status of a country, as measured by
its gross domestic product (GDP) and life expectancy.  However no
relationship is evident between GDP and population, or between either of the
life expectancy variables and population.

![ParCoordPlot-1](/~kshedden/introds/images/pc1.svg)


Mosaic plots
------------

The graphs above primarily use quantitative data.  A _mosaic plot_ is
a plot that is used with nominal data.  Specifically mosaic plots are
used when the units of analysis are _cross-classified_ according to
two nominal factors.  In the example below, people with cancer are
cross-classified by their biological sex, and by the type of cancer
that they have:

![ParCoordPlot-1](/~kshedden/introds/images/mp1.svg)

The width of each box in the mosaic plot corresponds to the relative
overall prevalence of the corresponding cancer type.  The heights of
the boxes correspond to the sex-specific prevalences.  Based on this
graph, we see that digestive, lung, and breast cancers are much more
common than, say, oral and endocrine cancers.  The mosaic plot also
shows us that while breast and endocrine cancers are more common in
females, the other cancer types are more common in males.

An important property of a mosaic plot is that the area of each box is
proportional to the number of units that fall into the box.  Thus, we
can see that the area of the female breast cancer box is larger than
the the combined areas of the female and male lung cancer boxes.
Thus, there are more cases of breast cancer in females than the
combined cases of lung cancer for both sexes.
