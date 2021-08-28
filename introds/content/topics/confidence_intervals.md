Confidence intervals
====================

The core goal of statistics is to answer questions about the real
world using data.  Often, our question can be stated in terms of an
unknown numerical characteristic of a population of interest.  For
example, suppose we are studying unemployment and how it relates to
demographic characteristics.  As part of this research, we may wish to
estimate the unemployment rate in a specific demographic subgroup,
say, men living in Ohio who are between the ages of 20 and 30 and who
do not have a college degree.

We can never recover the exact value of a population characteristic
from our data.  We can only estimate it, and estimates are always
wrong to some degree.  Thus, we will usually also want to quantify the
uncertainty in our estimate, which means that we wish to express how
large the error in our estimate might be.  One way to do this is using
_confidence intervals_.

A confidence interval is a form of _interval estimate_, meaning that
instead of presenting our findings as a single number, which we know
is not exactly correct, we present our findings as an interval.  For
example, we may report an interval of (5.3, 7.1) for the unemployment
percentage in a particular population.  This interval is constructed
so that it has a high chance (probability) of containing the true
value of interest, e.g.  the true unemployment rate in the population.

In most settings, the estimation error can be arbitrarily large --
there is no limit to how large the estimation error can be (although
very large errors may occur quite rarely).  Therefore, the only
interval that is guaranteed to contain the value of interest is an
interval that covers the entire real number line,
i.e. {{<katex>}}(-\infty, \infty){{</katex>}}.  But clearly this is
not a helpful way to report our results.

Instead of producing an interval that is guaranteed to contain the
value of interest, we may aim to construct an interval that has a
defined probability of containing this value.  This probability is
called the _coverage probability_, and is most often taken to be 95%.
Thus, we aim to construct an interval that is just wide enough so that
95% of the time, the interval contains the value of interest.
Occasionally we may see people using a 90% or 99% confidence interval,
which are intervals that either 90% of the time or 99% of the time
cover the value of interest.

Note that when we talk about coverage probabilities, the probabilities
are taken with respect to repetitions of our entire study, including
all steps from data collection to data analysis.  In reality, we will
never carry out such a repetition.  Instead, we will only ever carry
out our research study one time.  In this one study, any confidence
interval that we construct will either contain its target value or not
(although we do not know which is the case).  The idea of coverage
probability is based on an imagined set of replications of our study,
such that over all of these imagined replications, the intervals that
would be constructed cover the target value a defined fraction of the
time (usually 95%).

The coverage probability is chosen by the researcher.  Most of the
time, a coverage probability of 95% is chosen, but this is only a
convention.  Note that a confidence interval with a higher coverage
probability must be wider than a confidence interval with a lower
coverage probability.  For example, if (5.3, 7.1) is an interval with
95% coverage probability, then (5.5, 6.9) may be an interval with 90%
coverage probability.  The former interval has width 1.8, the latter
has width 1.4.

To construct a confidence interval it is usually sufficient to have
three pieces of information in-hand: (i) an estimate, (ii) the
estimate's standard error, and (iii) some understanding of the
sampling distribution of the estimate.  In many cases, we will invoke
the central limit theorem to argue that the sampling distribution in
(iii) is a normal distribution.

The most conventional form for a confidence interval is
{{<katex>}}(\hat{\theta} - q\cdot{\rm SE}, \hat{\theta} + q\cdot{\rm
SE}){{</katex>}}, where {{<katex>}}\hat{\theta}{{</katex>}} is the
estimate and {{<katex>}}{\rm SE}{{</katex>}} denotes the standard
error of this estimate.  The value {{<katex>}}q{{</katex>}} is a
positive constant that we will discuss shortly.  If our goal is to
estimate the population mean using the sample mean, then
{{<katex>}}\hat{\theta} = \bar{x}{{</katex>}}, the average of the
data, and {{<katex>}}{\rm SE} = \sigma/\sqrt{n}{{</katex>}}, where
{{<katex>}}n{{</katex>}} is the sample size and
{{<katex>}}\sigma{{</katex>}} is the standard deviation of the
measurements.  As discussed above, we generally do not know
{{<katex>}}\sigma{{</katex>}}, but can plug-in the estimate
{{<katex>}}\hat{\sigma}{{</katex>}}.  This yields the form for the
confidence interval for the population mean that is most encountered
in practice, which is {{<katex>}}(\bar{x} - q\hat{\sigma}/\sqrt{n},
\bar{x} + q\hat{\sigma}/\sqrt{n}){{</katex>}}.

The value of {{<katex>}}q{{</katex>}} in the confidence interval
depends on the desired coverage probability (most often 95%), and the
distribution of the data values.  If we wish to have a confidence
interval that covers with probability {{<katex>}}1 -
\alpha{{</katex>}} (so {{<katex>}}\alpha = 0.05{{</katex>}} to have
95% coverage probability), then {{<katex>}}q{{</katex>}} should be set
to the {{<katex>}}1-\alpha/2{{</katex>}} quantile of the standardized
estimate, where {{<katex>}}1-\alpha/2 = 0.975{{</katex>}} for a 95%
confidence interval.  The standardized estimate is
{{<katex>}}(\hat{\theta} - \theta) / \widehat{\rm SE}{{</katex>}} in
general, and {{<katex>}}\sqrt{n}(\bar{x} - \mu) /
\hat{\sigma}{{</katex>}} in the case of mean estimation.  Due to the
CLT, this distribution is approximately normal in many cases, unless
the sample size is small.  In this course, we will primarily focus on
the case where this distribution can be taken to be normal, but we
will comment briefly on some other possibilities.

Conveniently, when we take the distribution of the standardized
estimate to be normal, and if we are constructing a 95% confidence
interval, then the 0.975 quantile of the standard normal distribution
happens to be 1.96, which can be rounded to 2.  Thus, one way to get
an approximate 95% confidence interval for the mean is simply to take
the sample mean {{<katex>}}\bar{x}{{</katex>}}, then add and subtract
two standard errors from it.  This approach works fine for larger
sample sizes.

If the data are far from following a normal distribution and the
sample size is small, the distribution of the standardized estimate
may not be well approximated by a normal distribution.  In such cases,
the actual distribution may have heavier tails than the normal
distribution, which means that the 97.5 percentile of the actual
sampling distribution will be somewhat greater than 2.  In some cases,
people use the quantiles of a Student-t distribution rather than a
normal distribution to remedy this.  The 0.975 quantile of the
Student-t distribution falls between 2 and 2.25 as long as the sample
size is greater than 10.  However the Student-t distribution isn't
always the right distribution to use either.  Constructing a
confidence interval for small samples from an unknown distribution and
achieving a good approximation to the desired coverage probability may
be impossible in some cases.

In this course, we will generally use the "large sample" approach to
confidence intervals, using the estimate plus/minus two standard
deviations in most cases to form a 95% confidence interval.  It is
important to note that this interval only has approximately 95%
coverage.  However this construction is intuitive and easy to
remember.  For very small samples or heavy-tailed data distributions,
it is important to note that the interval may not actually have the
intended coverage level.
