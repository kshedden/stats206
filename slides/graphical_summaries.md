% Graphical summaries
% Kerby Shedden
% September 8, 2020

A statistical graph or plot is any approach to
summarizing data that presents its results visually
rather than through numbers, text, or tables.

Statistical graphs are data summaries, and are subject
to the same principles as any other data summary:

* Every graph should aim to address a specific question or
support a specific argument.

* A graph is almost always constructed from a sample of
data.  But the purpose of the graph is to allow us
to make inferences about the population that the data
represent.

* A graph is almost always based on a collection of
numerical summaries.  The theoretical properties
of these numerical summaries determine the theoretical
properties of the graph.

* A graph can be misleading or informative, based on
the theoretical properties on which it is based.

---

The main challenge with constructing an informative
graph is to compress as much relevant information
as possible onto a page, while remaining legible.

Many graphing procedures suffer from "overplotting"
when used with large or complex datasets,
meaning that the graph elements crowd and fall on
top of each other, making the graph difficult
to read.

Most graphs are 2-dimensional, but there are some
approaches for presenting higher-dimensional data.

---

A __boxplot__ is based on a collection of quantiles.
Its purpose is to show a minimal amount of information
to convey the location, dispersion, and skew of the data
(and indirectly, of the population that it represents).

![](/~kshedden/introds/images/bp1.svg)

The central box has three parallel lines defined by
quantiles: the 25th percentile, the median, and the
75th percentile.

The "whiskers" fall at the 75th percentile plus
1.5 times the IQR, and the 25th percentile minus
1.5 times the IQR (the whiskers may be drawn
at the largest/smallest data values that are
less/greater than these points).

The "fliers" (dots) are any points that fall
outside of the whiskers.

---

Boxplots for several samples that we wish to
compare can be plotted side-by-side:

![](/~kshedden/introds/images/bp2.svg)

---

A __histogram__ aims to depict the data in more
detail.  It shows the _density_ of data near
each value within its range.  The "density" at a point
$x$ roughly
means the frequency at which we observe values
close to $x$.

![](/~kshedden/introds/images/hist0.svg)

A histogram is constructed by dividing the
range of the data into _bins_.  We then count
the number of observations that fall into each bin.
This is the height of the bar for that bin.

---

The number of bins in a histogram is a _parameter_ of the method
and must be set.  A common rule of thumb is to
use bins with width equal to $2\cdot \textrm{IQR}/n^{1/3}$,
where $n$ is the sample size.

In order to be informative, histograms require more data than boxplots (based on quantiles).
This is a mathematical fact that can be proven.

Roughly speaking, to double the accuracy of a quantile estimate,
we need to increase our sample size by a factor of 4.  To
double the accuracy of a density estimate (e.g. a histogram),
we need to increase our sample size by a factor of 8.

For large datasets, histograms
may be more informative than boxplots, but as a result of this theoretical
fact, for small datasets histograms
may be very unstable compared to boxplots (i.e. the appearance
changes dramatically for different samples from the same
population).

---

For quantities that are measured on a continuous scale, it is
natural to imagine that the density also varies continuously.

However the histogram is a _step function_, meaning that it is
discontinuous.

There are techniques that smooth a histogram, in order to estimate
the density as a continuous function.  We will not discuss the
details of how this smoothing takes place.

Like a regular histogram, a smoothed histogram requires quite
a bit of data to give a meaningful result.

![](/~kshedden/introds/images/hist1.svg)

---

Just as we can compare two datasets with side-by-side
boxplots, we can also compare two datasets (and by extension,
their corresponding populations) by plotting
their smoothed densities on a common axis:

![](/~kshedden/introds/images/hist2.svg)

---

A boxplot only shows three key quantiles of a dataset
(the 25th, 50th, and 75th percentiles).  To obtain a more
fine-scale representation of the data, we can plot
the _quantile function_, which is essentially a graph
of every quantile $Q_p$ plotted against the corresponding
probability point $p$.  Below we plot two quantile functions
on the same axes to allow a comparison to be made:

![](/~kshedden/introds/images/qp1.svg)

---

Plotting multiple quantile functions in the same graph can
be a very effective way of comparing two collections of
data.

If we have two samples $A$ and $B$, and if every quantile
for sample $A$ is greater than the corresponding quantile
for sample $B$, then we say that $A$ is _stochastically
greater_ than $B$.

This is much stronger than knowing that $A$ has a greater
mean or median than $B$.

See the previous slide for an example of two quantile
functions that show a stochastic ordering.

---

If the two plotted quantile functions cross, as below, there is no
stochastic ordering.  But it is informative to know where
they cross, and how far apart the quantile functions are.

![](/~kshedden/introds/images/qp2.svg)

---

A powerful way to compare two samples (or populations)
is using a _quantile-quantile plot_ (or QQ plot).  This plot appears
simple, but requires some experience to interpret.

Suppose we have two samples with quantile functions
$Q_1(p)$ and $Q_2(p)$.  Earlier we showed
a plot of $Q_1(p)$ against $p$ overlaid with a plot of
$Q_2(p)$ against $p$.

A QQ plot plots $Q_2(p)$ against $Q_1(p)$.  The
value of $p$ is not explicitly shown.

![QQplot-1](/~kshedden/introds/images/qqp1.svg)

---

Each point on a QQ plot plots a quantile for one dataset
(corresponding to some probability $p$) against the same quantile
for a different dataset.

For example, one point on the QQ plot shows the median
of the second data set plotted against the median of the first dataset.

A different point on the QQ plot shows the 25th percentile
of the second dataset plotted against the 25th perentile of the first
dataset.

However we do not know which point on the QQ plot corresponds
to the median, the 25th percentile, etc.

---

Here are some key conclusions that can be made from a QQ plot:

* If the QQ plot is linear, the populations are linearly related,
i.e. there are constants $a$ and $b$ such that the second population
can be obtained by drawing a value $x$ from the first population,
and transforming it using $a + bx$.

* If the QQ plot tends to have a slope exceeding 1, then the
data or population depicted on the vertical axis is more
dispersed than the data or population depicted on the horizontal
axis,.

* If the QQ plot lies entirely above the line $y=x$, then the data
or population depicted on the vertical axis is stochastically greater
than the data or population depicted on the horizontal axis.

---

A __dotplot__ is a good way to convert a simple table
into a graph.  There are many ways to do this, we will
only show one example here.

Imagine we had this table showing the average age by
sex within 11 countries:

| Country   | Female | Male | Country   | Female | Male |
| :--       | :--    | :--  | :--       | :--    | :--  |
| Canada    | 43.5   | 40.9 | Nigeria   | 18.5   | 18.3 |
| Ethiopia  | 18.1   | 17.7 | Brazil    | 32.8   | 31.1 |
| France    | 43.1   | 39.6 | China     | 38.4   | 36.5 |
| Japan     | 48.7   | 46.0 | S. Africa | 27.3   | 26.9 |
| India     | 28.6   | 27.2 | USA       | 39.4   | 36.8 |
| Russia    | 42.5   | 36.6 |

---

Here is a dotplot corresponding to the table on the
previous slide:

![](/~kshedden/introds/images/dp1.svg)

Note that the countries are sorted by the overall
average age.

---

__Scatterplots__ are one of the most commonly encountered
graphs, but many people have not considered them
carefully from a statistical perspective.

Here is a scatterplot showing the daily maximum versus
the daily minimum temperature at multiple locations:

![](/~kshedden/introds/images/sp0.svg)

---

Scatterplots reflect the _joint distribution_ between
two quantitative variables.  Inspecting a scatterplot reveals
many features of the data, including location, scale,
skew, density, trends, associations, conditional properties,
and more.  It takes some skill to
learn to recognize these features in a scatterplot.

Like any statistical graph based on data, in almost
all cases, the more data we have, the more informative
the graph will be.  A scatterplot based on a small
amount of data may be misleading, because it may
differ substantially from the population that the
data represent.

If our goal is to understand the "trend" or association
between two quantitative variables, we can use
"scatterplot smoothing" to estimate the _conditional
mean function_.  Suppose we are plotting a variable
$y$ on the vertical axis against a variable $x$ on
the horizontal axis.  The conditional mean of
$y$ given $x$, at a given point $x_0$, is the average value of $y$ for
all observations $x$ that fall close to $x_0$.

---

There are several algorithms for doing this, a notable
one is called _LOWESS_.  We won't get into the details
of this algorithm here.  It produces the orange line
in the plot below:

![](/~kshedden/introds/images/sp1.svg)

---

A _parallel coordinates plot_ is a technique for plotting
higher-dimensional data in two-dimensions.

sInstead of
using the horizontal and vertical axes to each represent
one dimension of information (which limits us to two
dimensions if we want our plot to lie in a plane),
we place the "coordinates" as parallel (rather than
perpendicular) lines.

The values on different axes for one observation are
connected by lines.

This allows us to have arbitrarily
many dimensions in a 2-dimensional graph.

A drawback of this plot is that it suffers
from overplotting with larger datasets, and it
takes some experience to interpret.

---

Here is a parallel coordinates plot showing four characteristics
of ten countries (the data are simulated):

![](/~kshedden/introds/images/pc1.svg)

It is common in a parallel coordinate plot to Z-score
the variables, as we have done here.

---

Most or all of the plots we have considered so far are
appropriate for quantitative data.  Here we consider a plot
that is appropriate for nominal data, specifically for bivariate
nominal data (pairs of nominal values observed on the same
units).

In the plot displayed on the next slide, each subject
in the dataset to be depicted has cancer.  We
record their sex, and what type of cancer they have.

A __mosaic plot__ takes data of this form, and represents
it such a way that every combination of the variables
corresponding to the horizontal and vertial axes is represented
with a box.  The size of this box approximately corresponds
to the number of individuals in the sample (or population)
with this pair of characteristics.)

---

![](/~kshedden/introds/images/mp1.svg)
