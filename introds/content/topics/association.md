Measures of association
=======================

Many data analyses involve multiple variables, and are therefore said
to be _multivariate_.  To perform a multivariate analysis, we need a
dataset in which several variables are measured for each "unit of
analysis" (e.g. for each person in a study).  For example, if we
measure the income and number of years of education for each of 200
people, we can perform a multivariate (or specifically a _bivariate_)
analysis with these data.  It is important to note that the variables
in a multivariate analysis must be measured on the same individuals.
If we had, say 100 people and obtained their income, and a different
set of 100 people and obtained their education level, this would not permit
us to perform a multivariate analysis. In contrast to a multivariate
analysis, a _univariate analysis_ is one in which all analysis
involves a only single variable.

Multivariate analyses open up many analytic possibilities that are not
present when working with a single variable.  Here we will focus on
one such possibilty, which is the identification of _associations_ in
bivariate data.

The term _association_, loosely speaking, describes a "relationship"
beween two variables.  More formally, at the population level, we say
that two random variables {{<katex>}}X{{</katex>}} and
{{<katex>}}Y{{</katex>}} are associated if they are not statistically independent,
in the sense defined in our discussion of probability.  The question
we address here is whether we can estimate the manner in which the
random variables {{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}}
are associated, using data from a sample of values {{<katex>}}(x_1,
y_1), (x_2, x_2), \ldots, (x_n, y_n){{</katex>}} comprising an independent and
identically distributed (iid) sample from the distribution of
{{<katex>}}X, Y{{</katex>}}.

There are many ways to assess associations.  Here we will discuss two
of the most well-known measures of association, which are applicable
in two complementary situations.

Product-moment correlation
--------------------------

The product-moment correlation, also known as the _correlation
coefficient_, or the Pearson correlation, is generally used with
quantitative data, although it can used with ordinal or even binary
data.  The correlation coefficient is a standardized version of the
_covariance_, so we will begin with a discussion about covariances.

The covariance between two random variables {{<katex>}}X{{</katex>}}
and {{<katex>}}Y{{</katex>}} is defined to be the expectation of a
function involving {{<katex>}}X{{</katex>}} and
{{<katex>}}Y{{</katex>}}; it is
{{<katex>}}E[(X-EX)(Y-EY)]{{</katex>}}.  Here,
{{<katex>}}X-EX{{</katex>}} and {{<katex>}}Y-EY{{</katex>}} are
_centered_ versions of {{<katex>}}X{{</katex>}} and
{{<katex>}}Y{{</katex>}}.  If {{<katex>}}X-EX{{</katex>}} is positive,
then {{<katex>}}X{{</katex>}} is greater than its mean, and if
{{<katex>}}X-EX{{</katex>}} is negative, then {{<katex>}}X{{</katex>}}
is less than its mean; analogous statements can be made for
{{<katex>}}Y{{</katex>}}.  Now note that the product
{{<katex>}}(X-EX)(Y-EY){{</katex>}} is positive if and only if
{{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}} are both on the
same sides of their respective means, i.e.
{{<katex>}}X > EX{{</katex>}} and {{<katex>}}Y > EY{{</katex>}}, or
{{<katex>}}X < EX{{</katex>}} and {{<katex>}}Y < EY{{</katex>}}.
If {{<katex>}}(X-EX)(Y-EY){{</katex>}} is positive on average, this
means that in a random draw of {{<katex>}}(X, Y){{</katex>}}, the
values of {{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}} tend
to fall on the same sides of their respective means.  If
{{<katex>}}(X-EX)(Y-EY){{</katex>}} is negative on average, this means
that {{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}} tend to
fall on opposite sides of their respective means.  If
{{<katex>}}(X-EX)(Y-EY){{</katex>}} is zero on average, then there is
no tendency for {{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}}
to fall either on the same or opposite sides of their respective
means.

The covariance is ultimately determined not only by the signs of
{{<katex>}}X-EX{{</katex>}} and {{<katex>}}Y-EY{{</katex>}}, but also
by their magnitudes.  If a specific draw of
{{<katex>}}X-EX{{</katex>}} or {{<katex>}}Y-EY{{</katex>}} is only
slightly different from zero, then {{<katex>}}(X-EX)(Y-EX){{</katex>}}
will be small and not have a strong impact on the covariance.  When
{{<katex>}}X-EX{{</katex>}} and {{<katex>}}Y-EX{{</katex>}} both have
large magnitudes, then their product will have a very large magnitude.
Thus, the covariance is especially influenced by the pairs
{{<katex>}}X, Y{{</katex>}} that fall furthest from their means.

As a concrete example, let's consider the relationship between
education and income, where education is measured in years of
schooling, and income is personal income per year.  Let's also suppose
that the mean income is 40,000 USD, and the mean years of schooling is
13.5.  We observe pairs {{<katex>}}(X, Y){{</katex>}} consisting of the
number of years of schooling ({{<katex>}}X{{</katex>}}) and the income
({{<katex>}}Y{{</katex>}}).  A scatterplot of such data is shown below.
The years of schooling variable might in reality be integer-valued,
but can be "jittered" with noise to make the plot easier to interpret.

![correlation-1](/~kshedden/introds/images/corr1.svg)

If a person has more than 13.5 years of
schooling and has an income that is greater than 40K USD, or if a
person has less than 13.5 years of schooling and has an income that is
less than 40K USD, that person contributes positively to the
covariance (these are the orange points above).
A person contributes negatively to the covariance (purple points above) if they
either have more than 13.5 years of schooling and earn less than 40K
USD, or if they have less than 13.5 years of schooling and earn more
than 40K USD per year.  The stronger the relationship between
education and income, the larger the covariance will be.  For this
particular pair of variables the covariance will be
positive in almost any human society.

The units of the covariance is the product of the units of
{{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}}.  Thus, the
covariance between education and income has units of "years x USD".
This isn't easy to interpret, thus it is more common to work with the
correlation coefficient, which is a standardized version of the
covariance that is dimension-free (it has no units).  There are two
ways to think about this standardization.  One is that we convert the
random variables {{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}}
to _Z-scores_.  A Z-score is obtained by taking a random variable
{{<katex>}}X{{</katex>}}, and transforming it to {{<katex>}}(X -
EX)/\sigma_X{{</katex>}}, where {{<katex>}}EX{{</katex>}} is the expected
value of {{<katex>}}X{{</katex>}} and {{<katex>}}\sigma_X{{</katex>}} is
the standard deviation of {{<katex>}}X{{</katex>}}.  Note that
{{<katex>}}X-EX{{</katex>}} is the centered version of
{{<katex>}}X{{</katex>}}, so the Z-score is obtained by dividing the
centered version of X by its standard deviation.  Similarly,
{{<katex>}}Y{{</katex>}} is transformed to its Z-score which is
{{<katex>}}(Y-EY)/\sigma_Y{{</katex>}}.  These "standardized" or "Z-scored" versions of
{{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}} have mean zero
and standard deviation equal to 1.  The covariance between two
variables that have been standardized to Z-scores is the product-moment,
or Pearson correlation coefficient.  The scatterplot below shows the Z-scores
for education and income as discussed above.

![correlation-2](/~kshedden/introds/images/corr2.svg)

Another way to obtain the correlation coefficient is to calculate
{{<katex>}}{\rm Cov}(X, Y)/(\sigma_X\cdot \sigma_Y){{</katex>}},
where {{<katex>}}\sigma_X{{</katex>}} and {{<katex>}}\sigma_Y{{</katex>}}
are the standard deviations of {{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}},
respectively.  Thus, rather than
standardizing {{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}} to
Z-scores, we calculate the covariance of {{<katex>}}X{{</katex>}} and
{{<katex>}}Y{{</katex>}} in unstandardized form, then standardize the
covariance by dividing by the product of the standard deviations of
{{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}}.  It turns out
that these two ways of obtaining the correlation coefficient always
yield identical results.

One additional point that is important to note about the covariance is
that it only partially captures the state of independence between
variables {{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}}.  If
{{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}} have a non-zero
covariance, then they are not independent.  But if the covariance
between {{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}} is zero,
then it is possible that {{<katex>}}X{{</katex>}} and
{{<katex>}}Y{{</katex>}} are either independent or dependent.

Now that we have discussed the population versions of the covariance
and correlation coefficients, we will discuss how to estimate these
quantities from data.  Suppose we have data pairs {{<katex>}}(x_1,
y_1), (x_2, y_2), \ldots, (x_n, y_n){{</katex>}}.  The _sample
covariance_ between these data pairs is based on the products
{{<katex>}}(x_i-\bar{x})(y_i-\bar{y}){{</katex>}}.  These are
directly analogous to the products of centered random variables that
appear in the definition of the population covariance.  When working
with data, instead of taking the expectation over a distribution, we
take the average over the data:

{{<katex>}}
[(x_i-\bar{x})(y_i-\bar{y}) + \cdots + (x_n-\bar{x})(y_n-\bar{y})]/(n-1).
{{</katex>}}

The sample covariance is an estimate of the population covariance.  As
with the sample variance, the denominator of the sample covariance is
n-1, but the difference between using n and n-1 in the denominator is
usually non-consequential.

The sample Z-scores for the {{<katex>}}x_i{{</katex>}} can be defined
as {{<katex>}}(x_i - \bar{x})/\hat{\sigma}_X{{</katex>}}, where {{<katex>}}\hat{\sigma}_X{{</katex>}}
is the sample standard deviation of {{<katex>}}x_1, \ldots,
x_n{{</katex>}}.  Note that all values used to compute this Z-score
are statistics that can be calculated from data (we don't need to know
anything about the population to calculate the Z-scores).  If we
calculate the sample covariance using the Z-scores for the
{{<katex>}}x_i{{</katex>}} and {{<katex>}}y_i{{</katex>}}, we obtain
the _sample correlation coefficient_.

The sample correlation coefficient, like the population correlation
coefficient, is a real number that falls between -1 and 1 (inclusive).
It is undefined if the standard deviation of the
{{<katex>}}x_i{{</katex>}}, and/or the {{<katex>}}y_i{{</katex>}} is
zero (since then we would be dividing by zero).  The population and
sample correlation coefficients are dimensionless, which means that
they are invariant to linearly rescaling the data.  In the example above,
whether we measure income in dollars, thousands of dollars, or even in
Euros, and whether we measure education level in years, months, or
decades of schooling, we will get exactly the same correlation
coefficient.

Association among nominal variables
-----------------------------------

The joint distribution of two variables which we will denote here X
and Y, both of which are nominal, can be represented in tabular form.
A sample of data from such a distribution can be represented through a
_contingency table_, which counts the number of observations with each
possible combination of X and Y. For example, if we have data on
people under the age of 65 in three states (X), recording whether each
person has or does not have health insurance (Y), we might see a
contingency table like this:

|       |  Insured | Uninsured |  Total  |
| :--   |   --:    |   --:     |  --:    |
| VA    |   3025   |    433    |  3458   |
| MI    |   4053   |    332    |  4385   |
| CA    |   6341   |    801    |  7142   |
| Total |  13419   |   1566    | 14985   |


Recall that an association is present between two variables X and Y if
when we observe (X, Y) jointly, knowing X tells us something about Y,
and knowing Y tells us something about X.  An association in the above
table means that if we select a person at random from all 14,985
subjects, if we know what state they are in, we can predict (better
than guessing) whether they have insurance.  Equivalently, if we know
whether a person has insurance, we can predict (better than guessing)
what state they live in.  Put another way, under independence, the
probability of a randomly-selected person being insured is the same
whether they live in Virginia or in California, and the probability of
a randomly-selected person living in Michigan is the same whether they
are insured or uninsured.  Yet another way to express this is that
under independence, the conditional probability of being insured (or
the "conditional insurance rate") is the same in all three states.
Lack of independence requires the conditional insurance rate to differ
among at least two states.

It is important to note that whether two variables are independent or
dependent does not relate in any way to their marginal distributions.
For example, based on the above table, we see that far more people in
our dataset are insured than are not, and more people in our dataset
live in California than in Michigan.  Neither of these facts has any
bearing on whether having insurance is associated with which state a
person lives in.

Next, let's take the above table of counts, and convert it to a table
of estimated probabilities. To do this, we simply divide all the
numbers in the table by the total (14985).

|          |  Insured   | Uninsured |  Marginal  |
| :--      |   --:      |   --:     |  --:       |
| VA       |   0.2019   |  0.0289   |  0.2308    |
| MI       |   0.2705   |  0.0222   |  0.2926    |
| CA       |   0.4232   |  0.0535   |  0.4766    |
| Marginal |   0.8955   |  0.1045   |  1         |

Recall that in a joint distribution for variables with probability mass functions, the
variables are independent if and only if the joint probabilities are equal to the products
of the marginal probabilities.  We can create a table of independent joint probabilities by
multiplying the above marginal probabilities.  This table has perfect independence between
the rows (states) and columns (insurance status):

|          |  Insured   | Uninsured |  Marginal  |
| :--      |   --:      |   --:     |  --:       |
| VA       |   0.2067   |  0.0241   |  0.2308    |
| MI       |   0.2620   |  0.0306   |  0.2926    |
| CA       |   0.4268   |  0.0498   |  0.4766    |
| Marginal |   0.8955   |  0.1045   |  1         |

The next step in our analysis is to multiply all proportions in the
above table by the total sample size (14,985).  These are the counts
that we would expect to see under perfect independence.  Since our
data are a random sample, it is very unlikely that we will see exactly
the expected value.  However the closer our data fall relative to
these expected values, the stronger the indication that our data come
from a distribution in which the two variables (X and Y) are
independent.

|          |  Insured  | Uninsured |
|----------|-----------|-----------|
| VA       |   3097.6  |  361.4    |
| MI       |   3926.7  |  458.3    |
| CA       |   6395.6  |  746.4    |

To better gauge how close our data fall to their expected values under
independence, we can take a residual by subtracting the above fitted
values from the data:

|          |  Insured  | Uninsured |
|----------|-----------|-----------|
| VA       |    -71.6  |  71.6     |
| MI       |    126.3  |  -126.3   |
| CA       |     -54.6 |   54.6    |

In this table of residuals, a positive value indicates that our
observed count is greater than what is expected under independence,
and a negative value indicates that our observed count is less than
what is expected under independence.  Thus, we see somewhat more
people in Michigan who were insured and somewhat fewer people who are
uninsured, compared to what we would expect to see under independence.

A limitation with interpreting the preceeding table is that we don't
know the scale of the residuals.  This makes it difficult to judge
whether the residuals are much bigger than we would generally see
under independence, or if they just represent the random fluctuations
that would be seen even under independence.  This issue can be
addressed by scaling the residuals using an estimate of their standard
deviation.  We won't give a full justification for this here, but the
standard deviations of the residuals are approximately equal to the
square roots of their expected values.  For example, we estimate the
expected number of insured people in Michigan to be 3097.6, so we
estimate the standard deviation for the residual of the
Michigan/insured cell to be sqrt(3097.6) ~ 55.7.  This gives rise to
the table of Pearson residuals below:

|        |  Insured  | Uninsured |
|--------|-----------|-----------|
| VA     |    -1.3   |   3.8     |
| MI     |     2.0   |  -5.9     |
| CA     |    -0.7   |   2.0     |

As a rule of thumb, Pearson residuals that are smaller than 2 in
magnitude are completely compatible with X and Y being independent.
Values between 2 are 3 are suggestive of non-independence, and values
above 3 are strongly suggestive of non-independence.  In addition, by
inspecting the table above to see where the large positive and
negative values fall, we can learn something about the form of the
independence.  Most notably, Michigan has more insured and
substantially fewer uninsured people than would be expected under
independence, with the other two states showing the opposite trend.
This provides evidence that Michigan has a different (higher) medical
insurance rate than do Virginia or California.
