% Measures of association
% Kerby Shedden
% October 23, 2020

The term _association_ refers to a relationship between
two observed variables that are measured on the same units of analysis,
e.g. BMI and blood pressure measured on the same people.

Associations can take many forms, such as:

* The more nickel a steel alloy contains, the less it tends to corrode --
nickel content of steel alloys is inversely associated with corrosion.

* Fruits with higher levels of calcium last longer before spoiling --
calcium content of fruits is positively associated with shelf life.

* Air temperatures are more variable when the humidity is lower --
variation in air temperatures is inversely associated with humidity.

As the population level, two random variables $X$ and $Y$ are
__associated__ if they
are not independent (in the sense of probability).

---

Measures of association
=======================

Suppose we have paired data $(x_i, y_i)$.
For example, $x_i$ might be temperature and $y_i$ might be
humidity (at a particular location and time).

In this example, $x_i$ and $y_i$ are quantitative variables
that can be visualized with a scatterplot.
We may be able to detect an association between $x$ and $y$
"by eye", based on the scatterplot.  We may also wish to quantify
the manner in which these variables
are associated using a numerical summary statistic.

On the next slide, three of the four plots illustrate
settings where $x$ and $y$ are associated.  There is
no association in the lower right plot.

---

Association in scatterplots
===========================

![](/~kshedden/introds/images/assoc1.svg)

---

Measures of association
=======================

There are many ways that two variables can be associated.
No single summary measure is sensitive to all forms of association.

Every measure of association is a statistic that can be
calculated with data, and that also has a corresponding population analogue
(a population parameter).
The value of interest is the population parameter, but we
cannot obtain this value exactly.  However
using our data we can obtain the value of the association
statistic.

---

Product moment correlation
==========================

The most widely-used measure of correlation is the _product-moment
correlation coefficient_, sometimes called "Pearson's correlation",
or the _correlation coefficient_.

Pearson's correlation starts with the Z-scores
$\tilde{x}_i = (x_i - \bar{x})/\hat{\sigma}_x$ and
$\tilde{y}_i = (y_i - \bar{y})/\hat{\sigma}_y$, where
$\hat{\sigma}_x$ and $\hat{\sigma}_y$ are the standard
deviations of the $x_i$ and the $y_i$, respectively,
and $\bar{x}$, $\bar{y}$ are their means.

The product-moment correlation statistic is
$\sum_i \tilde{x}_i\tilde{y}_i/n$.

Note that this statistic is a moment, because we are averaging
a function of the data (the function that we are averaging is
$f(x, y) = x\cdot y$).

Since this statistic is formed from the Z-scores of the data,
it is both _translation invariant_ and _scale invariant_ --
we can add a constant to all data and multiply all data by
a constant without changing the correlation coefficient.  The
correlation coefficient is dimensionless and has no units.

---

Product moment correlation
==========================

The product moment correlation is a real number between -1 and 1.

If the data $x_i, y_i$ follow a perfect linear relationship
$y_i = a + bx_i$ with slope $b$, then the correlation coefficient is equal to 1
if $b>0$, and is equal to -1 if $b<0$.

If either $x_i$ or $y_i$ has no variation ($\hat{\sigma}_x=0$ or
$\hat{\sigma}_y=0$), then the correlation coefficient is undefined.

---

Product moment correlation
==========================

![](/~kshedden/introds/images/corr3.svg)

---

Product moment correlation
==========================

The product of Z-scores $\tilde{x}_i\tilde{y}_i$ is positive if $\tilde{x}_i$ and
$\tilde{y}_i$ have the same sign, and is negative if they have opposite
signs.

Therefore, $\tilde{x}_i\tilde{y}_i$ is positive if and only if
$\tilde{x}_i$ and $\tilde{y}_i$ both fall on the same side of their
mean.

Thus, the product moment correlation $\sum_i \tilde{x}_i\tilde{y}_i/n$
is positive if $\tilde{x}_i$ and $\tilde{y}_i$ tend to fall on the
same sides of their means (i.e. they fall in quadrants I and III of
the plane), and is negative if $\tilde{x}_i$ and $\tilde{y}_i$ tend to fall on
opposite sides of their means (they fall in quadrants II and IV
of the plane).

The product moment correlation is not only based on the
number of times that $\tilde{x}_i$ and $\tilde{y}_i$
fall on the same sides of their mean values.  When
$\tilde{x}$ and $\tilde{y}$ are both large, their product is
very large.  Therefore the largest Z-scores have an especially large
influence on this correlation measure.

---

Product moment correlation
==========================

Suppose we have data on education and income, with education having
mean 13.5 and income having mean 40 (on appropriate scales).
These values are positively correlated.

The
orange points in the plot below correspond to the people whose education and
income fall on the same sides of their means, and the purple points
below are the people whose education and income fall on opposite
sides of their means.

![](/~kshedden/introds/images/corr1.svg)

---

Product moment correlation
==========================

The correlation coefficient for the education and income data
is based on their Z-scores, plotted below.

![](/~kshedden/introds/images/corr2.svg)

---

Product moment correlation
==========================

Correlations closer to 1 (or -1) correspond to stronger associations:

![](/~kshedden/introds/images/corr4.svg)

---

Product moment correlation
==========================

No single number can capture all aspects of a scatterplot.  In particular,
two variables may have the same product moment correlation, but appear
very different in scatterplots.  "Anscombe's quartet" below shows four
datasets all of which have exactly they same correlation coefficient:

![](/~kshedden/introds/images/anscombe.svg)

---

Association and transformations
===============================

If we have an invertible transformation $f$, e.g. the log
transform $f(x) = \log(x)$, then random variables $X$ and $Y$ are independent if
and only if $f(X)$ and $f(Y)$ are independent.

However the form of the association can change upon transformation,
and it can be
much more informative in some cases to interpret an association
after applying transformations to the variables.

The product-moment correlation coefficient can change and even
move from zero to non-zero (or from non-zero to zero)
after applying a transformation.

---

Association and transformations
===============================

These scatterplots show exactly the same data, but the scatterplot
on the right is a log/log plot and the scatterplot on the left
shows the data on their original scale.

The correlation on the left is 0.7 and the correlation on the
right is 0.82.

![](/~kshedden/introds/images/assoc2.svg)

---

Association among nominal variables
===================================

We now consider a setting where the two variables that we
observe are nominal.

The joint distribution among two nominal variables
can be shown in a contingency table, such as below:


|           |  Insured | Uninsured |  Total  |
| :--       |   --:    |   --:     |  --:    |
| __VA__    |   3025   |    433    |  3458   |
| __MI__    |   4053   |    332    |  4385   |
| __CA__    |   6341   |    801    |  7142   |
| __Total__ |  13419   |   1566    | 14985   |

The rows are people's states of residence and the columns
are their insurance status.

---

Association among nominal variables
===================================

The contingency table can be converted into a
table of probabilities, by dividing the counts
by the total count:

|              |  Insured   | Uninsured |  Marginal  |
| :--          |   --:      |   --:     |  --:       |
| __VA__       |   0.2019   |  0.0289   |  0.2308    |
| __MI__       |   0.2705   |  0.0222   |  0.2926    |
| __CA__       |   0.4232   |  0.0535   |  0.4766    |
| __Marginal__ |   0.8955   |  0.1045   |  1         |

---

Association among nominal variables
===================================

The following table is formed by multiplying the
marginal probabilities from the previous slide, e.g.
$0.2067 = 0.8955\cdot 0.2308$:

|              |  Insured   | Uninsured |  Marginal  |
| :--          |   --:      |   --:     |  --:       |
| __VA__       |   0.2067   |  0.0241   |  0.2308    |
| __MI__       |   0.2620   |  0.0306   |  0.2926    |
| __CA__       |   0.4268   |  0.0498   |  0.4766    |
| __Marginal__ |   0.8955   |  0.1045   |  1         |

This is the closest joint distribution to our
observed distribution that is
exactly independent.

---

Association among nominal variables
===================================

Now we multiply each cell probability from the
previous slide by the total sample size (14,985)
to get a table of counts:

|          |  Insured  | Uninsured |
|----------|-----------|-----------|
| __VA__   |   3097.6  |  361.4    |
| __MI__   |   3926.7  |  458.3    |
| __CA__   |   6395.6  |  746.4    |

These counts are the closest counts to
our observed counts that reflect perfect
independence.

---

Association among nominal variables
===================================

Next we obtain residuals by subtracting the
"fitted values" from the previous slide
from the original data:

|          |  Insured  | Uninsured |
|----------|-----------|-----------|
| __VA__   |    -71.6  |  71.6     |
| __MI__   |    126.3  |  -126.3   |
| __CA__   |     -54.6 |   54.6    |

From this we see that, for example, Michigan
has more insured people than would be expected
if the state that a person lives in is independent
of their chance of being insured.  Virginia
has fewer insured people than would be expected
if this independence were to hold.

---

Association among nominal variables
===================================

The remaining issue is that the residuals
above do not follow a meaningful scale.
To put the residuals on a meaningful
scale, we divide each cell by the square
root of the fitted value.  For example,
we divide $-71.6$ by $3097.6^{1/2}$ to
obtain $-1.3$.


|        |  Insured  | Uninsured |
|--------|-----------|-----------|
| __VA__ |    -1.3   |   3.8     |
| __MI__ |     2.0   |  -5.9     |
| __CA__ |    -0.7   |   2.0     |

The values in the table above are sometimes called
"Pearson residuals" or "standardized residuals".
Standardized residuals greater than 2-3 in magnitude
are "large" and suggestive of non-independence.
