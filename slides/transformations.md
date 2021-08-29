% Transformations
% Kerby Shedden
% September 23, 2020

Point-wise transformations
--------------------------

Apply a function to the data to make it easier to analyze
and interpret.

Commonly-encountered transformations are the logarithm,
square root, and reciprocal functions.

Reciprocals are useful if the common-use units for a variable
are backwards from what makes sense to answer a research
question, e.g. we measure fuel economy in miles/gallon but
it usually makes more sense to analyze the data in units of
gallons/mile

---

Concave transformations
----------------------

A _monotone_ function is one that is invertible, and always
changes in the same direction (usually increasing for our purposes).

A function $f$ is invertible if
$f(x) = f(y)$ only when $x=y$.

A _concave_ function is one whose secant lines always lie below the
function (a secant line is a line connecting two points on the
graph of the function).

Many useful transformations are monotone and concave: these functions
"shrink" large values relative to smaller values.  Thereby they reduce
skew.

Two important examples of monotone concave transformations are the
square root and logarithm functions.

---

Logarithm transformations
-------------------------

The logarithm has a mathematical property that makes it extremely
useful for data analysis.  This is the fact that
$\log(x\cdot y) = \log(x) + \log(y)$.  Logarithms
convert multiplication to addition.

By default, a logarithm has base $e=2.71828\ldots$
(Euler's or Napier's constant).  But for the moment, suppose we calculate
logarithms with base 2 instead of the default base $e$.

In this case, note that
$\log(2x) = \log(x) + 1$.  In words, if two
log-transformed data values differ by 1 (under subtraction), then
their original untransformed values differ by a factor of 2.

Many natural phenomna from physics, biology, and social science have
multiplicative behavior, and are often easier to understand when
analyzed on the log scale.

---

Logarithm transformations
-------------------------

Suppose we have the following log base 2 values for the
populations of Detroit, Michigan and Lagos, Nigeria
in three years spanning the 20th century:

|               | 1900  | 1950  | 2000  |
| :--           | --:   | --:   | --:   |
| __Detroit__   | 18.1  | 20.8  | 19.9  |
| __Lagos__     | 15.4  | 18.3  | 22.8  |

We can conclude the following:

* The population of Detroit increased by a factor of 6.5
between 1900 and 1950, and declined by almost half between 1950 and 2000.

* The population of Lagos increased by approximately a factor of
7.5 between 1900 and 1950, and increased by almost a factor of over twenty
between 1950 and 2000.

* The population of Detroit was around 6.5 times greater than the
population of Lagos in 1900, but the population of Lagos was around
fifteen times greater than the population of Detroit in 2000.

---

Transformed data and summary statistics
---------------------------------------

A linear transformation ($f(x) = a + bx$) can be useful
for changing units (e.g. from feet to meters) but does not
qualitatively impact
the findings of most statistical procedures (a qualitative
change is one the alters the findings and conclusions).

Nonlinear transformations, such as the log transformation, can
strongly impact the results of an analysis.  For example, the mean
of dataset A may be greater than the mean of dataset B, but after
log transforming the values, the mean of dataset B may become greater
than the mean of dataset A.  Similar results can happen with standard
deviations, but not with quantiles.

---

Log transformation and the geometric mean
-----------------------------------------

The _arithmetic mean_ $(x_1 + \cdots + x_n)/n$
has a multiplicative counterpart called the _geometric mean_, defined
to be $(x_1 \times \cdots \times x_n)^{1/n}$.

The geometric mean is a measure of location, like the (arithmetic) mean
and the median.

There is a close connection between the geometric mean and the arithmetic
mean of log-transformed data.  Specifically, if we exponentiate (antilog)
the arithmetic mean of log transformed data, we get the geometric mean.
The proof of this for a dataset of size 2 is:

$\exp((\log(x_1) + \log(x_2))/2) = [\exp(\log(x_1)) \cdot \exp(\log(x_2))]^{1/2} = (x_1\cdot x_2)^{1/2}.$

---

Normalizing and standardizing transformations
---------------------------------------------

We have discussed elsewhere many transformations that aim to put
data on a standardized scale:

* Mean residuals: $x_i \rightarrow x_i - \bar{x}$.

* Median residuals: $x_i \rightarrow x_i - m$,
where $m$ is the sample median.

* Z-scores: $x_i \rightarrow (x_i - \bar{x}) / \hat{\sigma}$,
where $\hat{\sigma}$ is the standard deviation.

* Quantile-standardized Z-scores: $x_i \rightarrow (x_i - m) / \textrm{mad}$,
where $m$ is the median and $\textrm{mad}$ is
the median absolute deviation.

---

Non point-wise transformations
------------------------------

Some transformations do not operate by applying a function to each data value.

One such example is the __differencing transformation__ for data that are
observed as a sequence.

If $x_1, x_2, \ldots, x_n$ is a sequence of values,
then $x_2-x_1, x_3-x_2, \ldots, x_n-x_{n-1}$ are the differenced
values.

For example, if we measure the height of a child in centimeters at ages 2, 3, 4, and
5, we may observe: 94, 100, 105, 109.  The difference transformed values are
6, 5, 4.  These reflect the growth in height, as opposed to the actual height,
and may be more appropriate for some analyses.
