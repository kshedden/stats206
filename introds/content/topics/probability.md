Basic probability
=================

Probability is the branch of mathematics that studies randomness in a
formal and rigorous way.  Probability is also part of the foundation
of statistics and data science, largely because it provides us with a
way to link a sample to its population, and a way to make precise
statements about uncertainty in data analysis.  Probability also
provides us with many tools for describing variation in a collection
of measurements.

Recall that we view the sample of data that we collect and analyze as
a selection from a larger population, and our goal in data analysis is
to make statements about the population, not only about the sample.
In a probability-based approach to statistics, the sample is viewed as
a random "draw" from the population.  In this context, we can
view the population as something called a
_probability distribution_, which is a precise
description of all the possible observations that can be made, and how
likely we are to observe each of them.

As a concrete example of a probability distribution, suppose we select
a person of age 18 or older at random from a city, say Cairo, Egypt,
and ask that person how many times they have been married.  The
possible outcomes are 0, 1, 2, ... (in principle it is unbounded).
There is a certain probability that the person responds with 0,
another probability that the person responds with 1, and so on.  These
probabilities, taken together, constitute a probability distribution.

A random draw from a population can always be repeated, at least in
theory.  That is, if we are interested in sampling 10 people from the
UM student population, and we randomly contact 10 people today to
construct a sample, we can do this again tomorrow.  The 10 people
sampled tomorrow will almost certainly be different than the 10 people
sampled today.  However in some sense the two samples are equivalent
because the same process was used to obtain them.

In situations where you have a sample, but you can't imagine obtaining
a replicate of your sample, then the sample that you have is likely
not a random sample.  For example, sometimes the sample is actually
the entire population.  Such a sample is known as a _census_.  If you
were to repeat a census, you would get back exactly the same results.
In other cases, we have a _convenience sample_ that was generated in
such a haphazard way that there is no natural way to view it as a
proper random draw from a population.

A probability distribution is formally defined by two entities, one of
which, the _sample space_, is the collection of values that can be
drawn.  The sample space can be either finite of infinite.  Starting
with the finite case, the other entity that defines the probability
distribution is its _probability mass function_, or _pmf_.  The pmf is
a function on the sample space that tells us the probability of
observing each point when we take a draw.

For example if we have a box containing one red ball, two orange
balls, and one green ball, then the sample space can be viewed as the
set {red, orange, green}.  If we reach into the box and draw a ball,
the pmf can be denoted with the function
{{<katex>}}p(\cdot){{</katex>}}, where {{<katex>}}p({\rm red}) =
1/4{{</katex>}}, {{<katex>}}p({\rm orange}) = 1/2{{</katex>}}, and
{{<katex>}}p({\rm green}) = 1/4{{</katex>}}.  The probability for the
orange point is twice that of the other colors since there are two
orange balls in the box.

Based on the above example, we see that a probability distribution
with a finite sample space can always be represented through a table:

x    | red  | orange | green |
-----|------|--------|-------|
p(x) | 1/4  |  1/2   |  1/4  |

There are certain properties satisfied by all probability
distributions.  The most important of these are (i) every probability
is a real number between 0 and 1, and (ii) the sum of probabilities
over all points in the sample space is 1.  We see this in the example
above, since 1/4 + 1/2 + 1/4 = 1, and each of these probabilities
falls between 0 and 1.

An _event_ is a subset of the sample space. We say that the event
"occurs" if the value we draw is in the event.  For example, {orange,
green} is an event that occurs if the ball that we draw is either
orange or green.  The probability of an event is the sum of all
probabilities in the event, which is 3/4 in this example.  An event
can be _complemented_, by forming the set of all points that are not
in the event.  This yields a simple but important identity.  If E is
any event, the the probability that E does not occur is equal to 1
minus the probability that E does occur.  Thus, the probability of not
drawing an orange or a green ball is 1 - 3/4 = 1/4.  We can write this
fact mathematically as {{<katex>}}P({\rm not}\; E) = 1 -
P(E){{</katex>}}.

Another term for a probability distribution is a _random variable_.  A
random variable is usually denoted with a capital letter, such as
{{<katex>}}X{{</katex>}}.  When we write
{{<katex>}}P(X=x){{</katex>}}, this means "the probability that the
random variable {{<katex>}}X{{</katex>}} takes on the value
{{<katex>}}x{{</katex>}}".  In this expression,
{{<katex>}}x{{</katex>}} is a fixed constant and
{{<katex>}}X{{</katex>}} represents a draw from a probability
distribution, and therefore has no fixed value.  If
{{<katex>}}X{{</katex>}} follows the distribution for sampling colored
balls discussed above, then we could write {{<katex>}}P(X={\rm red}) =
1/4{{</katex>}}.  We can also write things like {{<katex>}}P(X \in
\{{\rm orange, green}\}) = 3/4{{</katex>}} to denote the probability
that the event {orange, green} occurs.

Summary statistics of quantitative probability distributions
------------------------------------------------------------

Quantitative distributions have numeric sample spaces.  For example,
if {{<katex>}}X{{</katex>}} represents a quantitative distribution,
say the annual household income in the United States, then we can
write {{<katex>}}P(X \le 30000){{</katex>}} to denote the probability
that a household's income is 30,000 USD or less, or {{<katex>}}P(X >
100000){{</katex>}} to denote the probability that the household's
income is greater than 100,000 USD.

Earlier in the course we studied summary statistics.  Many of the
summary statistics we discussed such as moments and quantiles are
mainly used with quantitative data.  Now that we have some basic
definitions from probability, we can define analogous summary measures
for probability distributions.  We will work with the following
example:

x      | 1    | 2   | 4   | 7   |
-------|------|-----|-----|-----|
p(X=x) | 0.1  | 0.3 | 0.4 | 0.2 |

This is a quantitative distribution whose sample space contains the
four points {1, 2, 4, 7}.  Note that the probabilities in the table
sum to 1.  The _expected value_ of this distribution is obtained by
taking each point in the sample space, multiplying by its
corresponding probability, and summing.  In this case, we get 0.1·1 +
0.3·2 + 0.4·4 + 0.2·7 = 3.7, and this value may be denoted
{{<katex>}}E[X]{{</katex>}} or {{<katex>}}EX{{</katex>}}, where
{{<katex>}}E{{</katex>}} stands for "expectation".  Recall that the
expected value is a moment, so this example shows how a moment can be
defined for a probability distribution.

The expected value is the _population analogue_ of the average of the
data, and may also be called the _population mean_.  The notion of a
population analogue of a statistic is very important.  The expected
value represents the exact, true mean of a distribution.  When we
conduct a study, we collect data, but never observe the population.
Thus, we would never know that 3.7 is the population mean.  We can
calculate the mean of our data (often called the _sample mean_ to
distinguish it from the population mean).  For reasons to be discussed
later, the sample mean will generally be close to the population mean,
thus it is reasonable to argue that we have learned something about
the population mean by calculating the sample mean.  This is the
process of _generalization_ (generalizing from sample to population),
which is central to all statistical data analyses.

Previously we have discussed the role of transformations in data
analysis.  Transformations can also be applied to populations.  If we
have a probability distribution for a random variable X, it is very
easy to calculate the probability distribution for a transformation of
X.  For example, the probability distribution of
{{<katex>}}Y=X^2{{</katex>}} is

y      | 1    | 4   | 16  | 49  |
-------|------|-----|-----|-----|
p(Y=y) | 0.1  | 0.3 | 0.4 | 0.2 |

Note that we have applied the transformation (squaring) to each point
in the sample space, and left the probabilities unchanged.  In some
cases, transforming a random variable may decrease the size of its
sample space.  For example, the distribution of the random variable
{{<katex>}}Y=(X-3)^2{{</katex>}} is

x      | 1    | 4   | 16  |
-------|------|-----|-----|
p(X=x) | 0.7  | 0.1 | 0.2 |


A very important transformation is the _centering transformation_, which
subtracts the population mean from each point in the sample space.
The distribution of {{<katex>}}Z = X - EX{{</katex>}}, the centered
version of X, is

z      | -2.7 | -0.7 | 1.3 | 3.3 |
-------|------|------|-----|-----|
p(Z=z) | 0.1  | 0.3  | 0.4 | 0.2 |

The values of {{<katex>}}X - EX{{</katex>}} are _deviations from the
mean_, which play a very important role in many statistical analyses.
Note that the expected value of the deviations from the mean is zero:
EZ = 0.1·(-2.7) +0.3·(-0.7) +0.3·0.4 + 0.2·3.3 = 0.

We have previously discussed the variance and standard deviation as
summary statistics of data, used to measure dispersion.  The
population analogue of the variance is {{<katex>}}E[(X -
EX)^2]{{</katex>}}.  This value tells us the expected squared
deviation from the mean.  It is a population-level measure of
dispersion, since it will be large for distributions whose values
often fall quite far from the expected value.  Above we constructed
the distribution of {{<katex>}}X - EX{{</katex>}}, now we can
construct the distribution of {{<katex>}}Q=(X - EX)^2{{</katex>}}:

q      | 7.29 | 0.49 | 1.69 | 10.89 |
-------|------|------|------|-------|
p(Q=q) | 0.1  | 0.3  | 0.4  | 0.2   |

Finally, we can calculate the variance of X, denoted Var[X], by taking
the expected value of the above distribution: 0.1·7.29 + 0.3·0.49 +
0.4·1.69 + 0.2·10.89 = 3.73.

All of the above calculations were based on the probability mass
function (pmf).  An alternative representation of a probability
distribution that is useful for quantitative data is the _cumulative
distribution function_ (CDF).  The CDF tabulates all of the left tail
probabilities, {{<katex>}}P(X \le x){{</katex>}}.  Note that we have
earlier discussed the notion of the left tail proportion based on
data.  The left tail probabilities are the population analogues of the
left tail proportions.  For the example we have been using here, the CDF is

x       | 1    | 2   | 4   | 7 |
--------|------|-----|-----|---|
p(X<=x) | 0.1  | 0.4 | 0.8 | 1 |

If we sort the sample space of {{<katex>}}X{{</katex>}}, the left tail
probabilities {{<katex>}}P(X\le x){{</katex>}} are obtained by
cumulatively summing the probabilities from the left.  These
cumulative probabilities will be non-negative, non-decreasing, and the
final cumulative probability will always be equal to 1.

Another summary statistic we discussed earlier in the course is the
quantile (or percentile).  Certain quantiles can be obtained directly
from the CDF.  In the example above, the 0.1 quantile is 1, the 0.4
quantile is 2, the 0.8 quantile is 4, and the 1 quantile is 7.  There
are various conventions about how to define other quantiles for this
population, but in practice, it is not very
useful to consider quantiles for probability distributions with very small sample
spaces such as these.

Many distributions are best thought of as having a sample space that
is infinite, possibly consisting of all or part of the real number
line.  Suppose that {{<katex>}}X{{</katex>}} is a random variable
representing such a distribution, then the left tail probability
{{<katex>}}P(X \le x){{</katex>}}, which is the CDF,
has a natural definition and interpretation.  Taking a
probability p between 0 and 1, the p'th quantile is the point q such
that {{<katex>}}P(X \le q) = p{{</katex>}}.

The probabilities of specific points {{<katex>}}P(X = x){{</katex>}}
do not have a natural definition for many random variables with
infinite sample spaces, and while paradoxical, these probabilities
may be equal to zero for every
value of x.  A proper treatment of random variables with infinite sample
spaces requires calculus, and will not be developed further here.

Joint distributions
-------------------

So far we have only considered a single random variable.  In practice,
we often want to consider multiple random variables that are observed
together.  A probability distribution in this setting is called a
_joint distribution_.  As above, we will focus on the case where the
sample spaces are finite.  Suppose we have two random variables
{{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}} that we observe
together.  Suppose further that the sample space of
{{<katex>}}X{{</katex>}} is {1, 3} and the sample space of
{{<katex>}}Y{{</katex>}} is {2, 4, 5}.  Then the joint distribution of
{{<katex>}}(X, Y){{</katex>}} takes the form of a table:

X\Y  | 2   |  4  |  5  |
-----|-----|-----|-----|
1    | 0.3 | 0.3 | 0.2 |
3    | 0.1 | 0   | 0.1 |

This table contains six probabilities which sum to 1.  Each cell in
the table tells us the probability of observing the given values of
{{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}} jointly.  For
example, the probability of observing {{<katex>}}X=1{{</katex>}} and
{{<katex>}}Y=4{{</katex>}} jointly is 0.3.  Some combinations may have
zero probability, for example the probability here of observing
{{<katex>}}X=3{{</katex>}} and {{<katex>}}Y=4{{</katex>}} jointly is
zero -- this combination can never happen.

Given a joint probability distribution, such as the one above, it is
possible to define _marginal distributions_ for the rows (X) and the
columns (Y) by summing the probabilities over the columns or rows,
respectively.  Thus, the marginal distribution of X is

| x      |  1  |   3  |
| :--    | :-- | :--  |
| P(X=x) | 0.8 |  0.2 |

The value 0.8 is obtained by calculating 0.3 + 0.3 + 0.2, the sum of
the first row of the joint distribution, and the value of 0.2 is
obtained by calculating 0.1 + 0 + 0.1 = 0.2, the sum of the second row
of the joint distribution.

The marginal distribution of Y is

|  y      |  2  |   4  |  5  |
|  :--    | :-- | :--  | :-- |
| P(Y=y)  | 0.4 |  0.3 | 0.3 |

which is obtained by summing the columns of the joint table.  Note
that the marginal distributions of X and Y are each probability
distributions in their own right, since their probabilities sum to 1.

Independence
------------

One of the most fundamental notions in probability is that of
_independence_.  Suppose we observe two random variables
{{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}} jointly.
Informally, {{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}} are
independent if knowing {{<katex>}}X{{</katex>}} does not tell us
anything about the value of {{<katex>}}Y{{</katex>}}, and vice versa.
In our example above, when {{<katex>}}X=4{{</katex>}},
{{<katex>}}Y{{</katex>}} must be equal to 1, since the
{{<katex>}}(X=4, Y=3){{</katex>}} cell of the table has probability
equal to zero.  Thus, {{<katex>}}X{{</katex>}} and
{{<katex>}}Y{{</katex>}} cannot be independent in that example.

When two variables are not independent, they are _dependent_.
In the real world, variables such as income and education would be
dependent, since people with more education tend to have higher
income, and vice versa.
It is very important to note that dependence does not imply causality.
Although income and education are statistically
dependent (i.e. not statistically independent), this does not
mean that having more education causes people to have a higher income,
or that having a higher income causes people to have more education.
Either, both, or neither of these statements could be true.

Mathematically, we have perfect independence if and only if every
joint probability is the product of the corresponding marginal
probabilities.  The following joint probability table has the same
marginal probabilities as in the previous example.  But unlike in the
previous example, in this example, we can confirm that the random
variables X and Y are independent.  All six of the cell probabilities
in the table below are equal to the product of their corresponding
marginal probabilities, e.g. 0.32 = 0.8·0.4, and 0.24 = 0.8·0.3.


X\Y  | 2    |  4   |  5   |
-----|------|------|------|
1    | 0.32 | 0.24 | 0.24 |
3    | 0.08 | 0.06 | 0.06 |


Conditional distributions
-------------------------

Previously we have discussed the idea of stratifying data to better
understand its properties.  For example, when considering household
incomes in the United States, we might stratify by state, or by
demographic variables such as sex and age.  A _conditional
distribution_ is a distribution obtained by starting with a joint
distribution, and renormalizing it so that each row or each column
sums to 1.  For example, starting with this joint distribution,

X\Y  | 2   |  4  |  5  |
-----|-----|-----|-----|
1    | 0.3 | 0.3 | 0.2 |
3    | 0.1 | 0   | 0.1 |

we can divide each row by its total and obtain the conditional
distributions of "{{<katex>}}Y{{</katex>}} given
{{<katex>}}X{{</katex>}}":

X\Y  | 2   |  4  |  5  |
-----|-----|-----|-----|
1    | 3/8 | 3/8 | 1/4 |
3    | 1/2 | 0   | 1/2 |

We would write these probabilities as, e.g. {{<katex>}}P(Y=4 | X=1) =
3/8{{</katex>}}.  The symbol "|" is read "given", or "conditioned on".
The meaning of this probability is that if we know that
{{<katex>}}X{{</katex>}} is equal to 1, then the probability of
observing {{<katex>}}Y{{</katex>}} to be equal to 4 would be 3/8.
Note that each row of the above conditional probability table sums to
1, whereas the overall sum of all cells in the joint table is equal to
1.

We can also construct the conditional distributions of
{{<katex>}}X{{</katex>}} given {{<katex>}}Y{{</katex>}}, by
normalizing the columns:

X\Y  | 2   |  4  |  5  |
-----|-----|-----|-----|
1    | 3/4 | 1   | 2/3 |
3    | 1/4 | 0   | 1/3 |

These probabilities are denoted, e.g. {{<katex>}}P(X=1 | Y=2) =
3/4{{</katex>}}, and represent the probability of observing
{{<katex>}}X{{</katex>}} to be equal to 1, when
{{<katex>}}Y{{</katex>}} is known to be equal to 2.

The table considered above describes the joint distribution of two
random variables {{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}}
that are not independent.  Next let's consider the table

X\Y  | 2    |  4   |  5   |
-----|------|------|------|
1    | 0.32 | 0.24 | 0.24 |
3    | 0.08 | 0.06 | 0.06 |

for which the rows ({{<katex>}}X{{</katex>}}) and columns
({{<katex>}}Y{{</katex>}}) are independent.  The conditional
distributions of {{<katex>}}Y{{</katex>}} given
{{<katex>}}X{{</katex>}} are

X\Y  | 2    |  4   |  5  |
-----|------|------|-----|
1    | 0.4  | 0.3  | 0.3 |
3    | 0.4  | 0.3  | 0.3 |

and the conditional distributions of {{<katex>}}X{{</katex>}} given
{{<katex>}}Y{{</katex>}} are

X\Y  | 2   |  4  |  5  |
-----|-----|-----|-----|
1    | 0.8 | 0.8 | 0.8 |
3    | 0.2 | 0.2 | 0.2 |

Note that {{<katex>}}P(X=x | Y=y){{</katex>}} does not depend on
{{<katex>}}y{{</katex>}}, and {{<katex>}}P(Y=y | X=x){{</katex>}} does
not depend on {{<katex>}}X{{</katex>}}.  In other words, the
conditional distribution of {{<katex>}}X{{</katex>}} given
{{<katex>}}Y{{</katex>}} is the same regardless of what value of
{{<katex>}}Y{{</katex>}} we condition on, and the conditional
distribution of {{<katex>}}Y{{</katex>}} given
{{<katex>}}X{{</katex>}} is the same regardless of what value of
{{<katex>}}X{{</katex>}} we condition on.  This happens if and only if
{{<katex>}}X{{</katex>}} and {{<katex>}}Y{{</katex>}} are independent.

Conditional independence
------------------------

Many research questions hinge on the inter-relationship among three
variables, which we will denote generically here by
{{<katex>}}X{{</katex>}}, {{<katex>}}Y{{</katex>}}, and
{{<katex>}}Z{{</katex>}}. In this setting, we may wish to combine the
notions of conditioning and independence, leading to the concept of
_conditional independence_.  The basic idea of conditional
independence is that two variables, say {{<katex>}}X{{</katex>}} and
{{<katex>}}Y{{</katex>}}, may be dependent, but when we condition on a
third variable {{<katex>}}Z{{</katex>}}, then {{<katex>}}X{{</katex>}}
and {{<katex>}}Y{{</katex>}} may become independent.

As an example, consider the relationships among tea drinking, smoking,
and cancer.  Each of these variables can be considered to be a binary
trait of a person (i.e. a person either drinks tea or does not, etc.).
Since there are three variables, each with two levels, there are
{{<katex>}}2^3=8{{</katex>}} combinations.  The joint probabilities
associated with these variables are presented in the following joint
three-way table:

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

We can derive several marginal distributions from this joint three-way
distribution.  For example, the marginal distribution of tea drinking
and cancer is

 &nbsp;    | Cancer | No cancer |
-----------|--------|-----------|
__Tea__    | 0.0082 | 0.5918    |
__No tea__ | 0.0058 | 0.3942    |

Each value in this marginal tables is obtained by summing two values in
the joint three-way table above.  For example, the probability of
drinking tea and not having cancer is the sum of the probabilities of
drinking tea and not having cancer for smokers and for non-smokers,
i.e. 0.5918 = 0.1080 + 0.4838.

There are actually three marginal two-way tables that can be
constructed from the joint three-way table.  Besides the joint
distribution of tea drinking and cancer status presented here, there
are also marginal distributions for tea drinking and smoking, and for
smoking and cancer status, which is shown here:

 &nbsp;      | Cancer | No cancer |
-------------|--------|-----------|
__Smoke__    | 0.006  | 0.194     |
__No smoke__ | 0.008  | 0.792     |

We can take this a step further, and obtain the marginal distribution
for a single variable, say smoking.  The marginal probability of
smoking is the sum of the four cells in the joint three-way table
corresponding to smokers: 0.0033 + 0.1080 + 0.0027 + 0.0860 = 0.2.
This tells us that marginally (ignoring tea drinking and cancer), 20% of this
population smokes.  We could do the corresponding calculation for
non-smokers, but since there are only two possible states for smoking,
we immediately know that the probability of someone not smoking in
this population is 1 - 0.2 = 0.8.

Are tea drinking and cancer independent or dependent?  To assess this,
we can convert the joint distribution between tea drinking and cancer,
presented above, to a conditional distribution, conditioning on tea
drinking.  We do this by dividing the values in each row by the row
total:

 &nbsp;    | Cancer | No cancer |
-----------|--------|-----------|
__Tea__    | 0.0137 | 0.9863    |
__No tea__ | 0.0144 | 0.9856    |

Since the two rows of the above table are different, it follows that
tea drinking and cancer are dependent.  People who drink tea in this
population have a slightly lower risk of having cancer than people who
do not drink tea.  However this may not be the full story, as we see
next.

The idea of conditional independence is that when we hold one variable
fixed, two other variables that were marginally dependent may become
conditionally independent.  If we condition on people not smoking, we
get the following conditional distribution for tea drinking and
cancer:

 &nbsp;    | Cancer | No cancer |
-----------|--------|-----------|
__Tea__    | 0.0061 | 0.6047    |
__No tea__ | 0.0039 | 0.3853    |

The above distribution is obtained by taking the four probabilities in
the joint three-way table corresponding to non-smokers, and dividing
them by the marginal probability that someone does not smoke, which as
determined above is 0.8.  For example the conditional probability of a
non-smoker being a tea-drinker without cancer is 0.4838 / 0.8 ~ 0.6048
(the last digit deviates due to rounding).

Are tea drinking and cancer dependent in this conditional
distribution?  To assess this, we condition the above table on tea
drinking.  This amounts to dividing each row by the row total,
yielding

 &nbsp;     | Cancer | No cancer |
------------|--------|-----------|
__Tea__     | 0.01   | 0.99      |
__No tea__  | 0.01   | 0.99      |

This result shows us that among non-smokers, both tea drinkers and
people who do not drink tea have the same risk of having cancer.  If
we were to do this calculation conditioning on people smoking rather than
conditioning on people not smoking, then we would also find no dependence between tea
drinking and cancer.

The explanation for what we are seeing here is that smoking is a
confounder of the relationship between tea drinking and cancer.
People who smoke are substantially more likely to get cancer than
people who do not smoke, and people who smoke are somewhat less likely
to drink tea than people who do not smoke.  If we do not consider
smoking, then a relationship appears between tea drinking and smoking,
but when we then condition on smoking behavior, this relationship
disappears.  In other words, tea drinking and cancer are marginally
dependent, but conditionally (given smoking) they are independent.
