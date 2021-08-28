The Central Limit Theorem and Gaussianity
=========================================

The Central Limit Theorem, or CLT, may be the most celebrated theorem
in the field of probability.  In order to state the CLT, we must first discuss a
specific probability distribution called the _Gaussian distribution_,
often referred to as the _normal distribution_.  The normal
distribution is a probability distribution on the real line, which
means that it cannot be described by a probability mass function
(pmf).  Instead, the normal distribution is described by a
_probability density function_.  The density function for a normal
distribution is depicted below (the density is positive at all
real values, but is very small outside the range that is shown in
the graph):

![normdist-1](/~kshedden/introds/images/norm1.svg)

Calculus is required to work mathematically with density functions, so
in this course we will only discuss density functions at a high level.
The main idea behind a density function is that it tells us how likely
we are to observe values near any given point.  We are more likely to
observe values where the density is large, and less likely to observe
values where the density is small.  For this type of distribution, we
should not try to define the probability of observing any specific
value.  Instead, we can obtain the probabilities of intervals, say,
the probability of observing a value between 2 and 3.  Such
probabilities are directly encoded in the density function, since they
are the area under the graph of the density function over the interval
(e.g. between 2 and 3).

The Gaussian distribution is actually a family of distributions,
defined by (or parameterized by) the mean {{<katex>}}\mu{{</katex>}}
and variance {{<katex>}}\sigma^2{{</katex>}}.  That is, for any real
number {{<katex>}}\mu{{</katex>}}, and any non-negative real number
{{<katex>}}\sigma^2{{</katex>}}, there is a Gaussian distribution with
mean {{<katex>}}\mu{{</katex>}} and variance
{{<katex>}}\sigma^2{{</katex>}}.  These are all different probability
distributions, but they have the same basic form, which can be
translated and scaled to emphasize different parts of the real line.
The Gaussian distribution with expected value
{{<katex>}}\mu=0{{</katex>}} and variance
{{<katex>}}\sigma^2=1{{</katex>}} is especially common and is referred
to as the _standard Gaussian_ or _standard normal_ distribution.  This
is the density function that is depicted above.

Density functions for three different Gaussian distributions are shown
below. In each case, the maximum density occurs at the mean
{{<katex>}}\mu{{</katex>}}.  Note that while the Gaussian distribution
has the property that the maximum density coincides with the mean,
this is not true of all distributions.  Also note that the density
functions are wider when the standard deviation
{{<katex>}}\sigma{{</katex>}} is greater.

![normdist-2](/~kshedden/introds/images/norm2.svg)

Symmetry and shape
------------------

The Gaussian distribution is sometimes referred to as the "bell
curve", since the bell shape describes how likely you are to see
points at various distances from the mean.  One important property of
the Gaussian distribution is that it is _symmetric_.  Symmetry can be
defined in various ways, but we will use a definition here in terms of
tail probabilities.  If Z follows a Gaussian distribution with mean
{{<katex>}}\mu{{</katex>}} and any variance, then {{<katex>}}P(Z < \mu
- t) = P(Z > \mu + t){{</katex>}}.  This means that we are equally
likely to observe a value that falls {{<katex>}}t{{</katex>}} or more
units below the mean as we are to observe a value that falls
{{<katex>}}t{{</katex>}} or more units above the mean.

Empirical rule
--------------

Another important property of the Gaussian distribution is the
so-called _empirical rule_, which states that (i) the probability of
observing a value within one standard deviation of the mean is
approximately 0.68, (ii) the probability of observing a value within
two standard deviations of the mean is approximately 0.95, and (iii)
the probability of observing a value that is within three standard
deviations of the mean is approximately 0.997 (sometimes roughly
approximated as 0.99 or 0.995).

For example, if we have data that follows a Gaussian distribution with
mean {{<katex>}}\mu=130{{</katex>}} and standard deviation
{{<katex>}}\sigma=12{{</katex>}}, then we are very unlikely to observe
a value smaller than {{<katex>}}94 = \mu-3\sigma{{</katex>}} or larger
than {{<katex>}}166 = \mu+3\sigma{{</katex>}}.  Specifically, only
around 3 out of 1000 values would be expected to fall in these
regions.  The empirical rule reflects the fact that the Gaussian
distribution has thin tails, so most of its mass falls within 3
standard deviations of its expected value.  Extreme values are very
seldom seen for the Gaussian distribution.  Other distributions such
as the Student-t and exponential distributions have heavier tails, and
a greater tendency to produce values that fall far from the expected
value.

Tail probabilities
------------------

The empirical rule describes the probability that a value drawn from
a Gaussian distribution falls a certain distance (or further) from
the mean.  When the standardard deviation {{<katex>}}\sigma{{</katex>}}
is larger, the probability of an observation falling a given distance
from the mean increases.  Therefore, it usually
makes sense to think of "distance from the mean" in terms of
multiples of the standard deviation.  For example, we may ask
how likely we are to observe a value that is at least 2 standard
deviations ({{<katex>}}2\sigma{{</katex>}}) from the mean.  Expressed
in probability notation, this can be written
{{<katex>}}P(|X-\mu|>2\sigma){{</katex>}}.  More generally, we
have _tail probabilities_, which are the probabilities that
a value falls {{<katex>}}c{{</katex>}} or more standard deviations
from the mean, i.e.
{{<katex>}}P(|X-\mu|>c\sigma){{</katex>}}.

For the Gaussian distribution, the tail probabilities are universal --
they do not depend on {{<katex>}}\mu{{</katex>}} and {{<katex>}}\sigma{{</katex>}}.
This is the reason that we can obtain the constant values stated in the
empirical rule.

Distributions that are not Gaussian do not follow the empirical rule.
This may lead us to wonder how likely it is, in some non-Gaussian
distribution, to observe a value that is at least {{<katex>}}c{{</katex>}}
standard deviations from the mean.  This question is partially answered
by _Chebyshev's inequality_, which tells us that for a very large
class of distributions, {{<katex>}}P(|X-\mu|>c\sigma) < 1/c^2{{</katex>}}.
For example, if {{<katex>}}c=3{{</katex>}}, then for some distributions,
a value can
have as much as {{<katex>}}1/c^2 \approx 0.11{{</katex>}} probability
of falling 3 standard deviations from mean.  Contrast this to the
setting of a Gaussian distribution, where the probability of falling
3 standard deviations from the mean is less than 1%.

Uses of the Gaussian distribution
---------------------------------

The Gaussian distribution is sometimes used to directly model measured
data values.  But in many cases, the Gaussian distribution is not a
good fit for a particular population of interest.  For example, the
distribution of incomes within a country would almost never follow a
Gaussian distribution, since income distributions are right skewed and
the Gaussian distribution is symmetric.  Our reason for discussing the
Gaussian distribution here is not to use it as a model for data.
Instead, the Gaussian distribution will turn out to describe the
statistical "errors" in many estimation processes.  The reason for
this is the Central Limit Theorem, which we discuss next.

Central Limit Theorem
---------------------

The Central Limit Theorem (CLT) describes the distribution of the
sample mean, (the average value) of n independent and identically
distributed (iid) data values.  The sample mean, like the individual
data values, is a random variable, so it follows a probability
distribution (in contrast, the population mean is constant).  The
probability distribution of the sample mean describes the tendency for
it to fall at different points relative to the population mean.

The CLT states that the sample mean will approximately have a Gaussian
distribution, even if the individual data values have a distribution
that is non-Gaussian.  The Gaussian approximation provided by the CLT
becomes more accurate as the sample size becomes larger.  People often
ask how large the sample size needs to be in order for the sample mean
to have a distribution that is approximately Gaussian.  Unfortunately,
this question does not have a good universal answer.  If the data
values themselves are Gaussian, then the statement of the CLT holds
exactly for all sample sizes n.  If the data values are very far from
being Gaussian, it takes a larger sample size for the "Gaussian
approximation" to begin to hold well.  Except in extreme cases, a
sample size of around 100 or more produces sample means that are
reasonably close to being Gaussian.  In the case of data that are not
too far from being Gaussian themselves, sample sizes in the range of
30-50 are usually sufficient.

The CLT is somewhat intangible, because it describes the distribution
of something that we only observe once.  Suppose we have a sample of
n=75 observations.  Taking the sample mean reduces these 75 values to
one average value.  This single number is random, but you cannot learn
very much about the distribution of something that you only see one
time.  We could learn about the distribution of the data by making a
histogram of their values, but a histogram of the sample mean would
convey very little, because we only observe a single sample mean.
Thus, the CLT is telling us something that, while true, cannot be seen
directly in our data.

Why do we care that the sample mean has an approximately normal
distribution?  The reason is that in many situations we want to
compute the probability that the sample mean falls at a certain
distance from the expected value.  This comes up in the two core
statistical inference procedures -- confidence intervals, and
hypothesis testing.  We will cover both of these topics soon.  For
now, we can use the CLT directly in the following example.

Suppose we are interested in the average systolic blood pressure (SBP)
of all African American men of age 60.  If we have a representative
sample of 50 such men, we can compute their mean blood pressure,
suppose this yields a value of 155 mm/Hg (the units of blood
pressure).  If we knew that the standard deviation of the SBP for 60
year-old African American men was 33, then the standard error of the
mean would be {{<katex>}}33/\sqrt{50} \approx 4.67{{</katex>}}.  Now
we can apply the empirical rule which states that 95% of the time, the
sample mean falls within two standard deviations of the true mean.
Thus, we have here that the sample mean has 95% probability of falling
within {{<katex>}}2\cdot 4.67 \approx 9.34{{</katex>}} of the truth.
In plain language, we can be quite confident (but not completely
certain) that the estimated mean SBP of 155 is within 10 mm/Hg of the
true population mean (or expected value) for African American men of
age 60.

Note that this analysis relies on the CLT, because we are invoking the
empirical rule, which only applies for the Gaussian distribution.
Note as well that this analysis takes the standard deviation of the
data (33) to be known, which in fact it is not.  This is an important
issue that we will return to later.
