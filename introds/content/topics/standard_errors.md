Standard errors
===============

One of the primary goals of data analysis is to estimate a
characteristic of a population using a sample of data taken from that
population.  For example, we may wish to estimate the expected value
(or population mean) using the sample mean.  Or, we may wish to
estimate the population value of the 0.75 quantile using the 0.75
quantile of the data.

An estimate of a population parameter is almost never exact.  Thus,
all estimates can be considered to have "error".  The _error_ of an
estimate is the value of the estimate minus the value being estimated
(the value being estimated is often called the _estimand_, the
"population parameter", or the "target" of the estimate).  In a very
generic setting, the estimate may be denoted
{{<katex>}}\hat{\theta}{{</katex>}} (read "theta hat") with the
estimand denoted {{<katex>}}\theta{{</katex>}}.  The "hat" notation
denotes that something is an estimate.

It is important to distinguish the error of an estimate from the
"errors" in the data.  For example, suppose we are studying the lung
capacity of smokers.  We may use a quantity called "Forced Expiratory
Volume" (FEV) to quantify this trait.  Suppose a person's true FEV is
83, but we measure their FEV as 86.  Then there is an error in the
measured FEV value of +3 units.  If we measure the FEV for 100 smokers
and obtain a mean FEV for the sample of 79 units, and if the
population mean FEV for all smokers is 80, then the estimation error
for the population mean is -1 unit.

We can almost never know the estimation error exactly.  If we knew the
estimation error, we could subtract it from our estimate to recover
the population value without any uncertainty.  In the example above,
if we knew that the estimation error for the mean FEV of smokers was
-1 unit, with an estimated value of 79 units, then we could recover
the population mean without uncertainty by subtracting the error from
the estimate, 79 - (-1) = 80.

Since we can't actually know the estimation error, we have to settle
for something less specific than this.  The _standard error_ is,
roughly speaking, the typical magnitude of the estimation error.  By
"typical", we mean the magnitude of the estimation error that we would
generally observe in a study like ours.  The standard error is not the
actual estimation error in our study, but instead tells us for studies
using the methods that we are using and with a similar population as
we are studying, what would the magnitude of the estimation error
typically be.  It is tempting to refer to the standard error as the
"average" or "expected" estimation error, but this is not quite right,
for reasons discussed further below.

In the above example of estimating the FEV of smokers, the standard
error might be, say 1.5.  That is, on average for the sample size and
population under consideration, the estimated mean FEV tends to be off
by around 1.5 units in one direction or the other.  The specific
estimation error of -1 units is not knowable, but it is not surprising
that if the typical error has magnitude 1.5 units, then the error in
one specific instance could be -1 unit.

In many data analysis settings, it is sufficient to report the
estimate and its standard error.  This is often written in the form 79
(1.5).  That is, we write the estimate first, then the standard error
next to it in parentheses.  This tells the reader that the data
supports a FEV value of 79 units, but this value has an error that can
be either positive or negative, and tends to have magnitude of around
1.5 units.

We should point out that while the standard error is often described
as the "average magnitude of the estimation error", this is not quite
correct.  More exactly, the standard error is the square root of the
average squared magnitude of the estimation error.  The average of the
square root of a random quantity X is not the same as the square root
of the average of X.

Standard error of the mean
--------------------------

The most commonly encountered standard error arises in the setting
where the population parameter of interest is the expected value, and
the statistic we are using for estimation is the sample mean.  If we
have an independent and identically distributed sample, then the
standard error in this setting is equal to the standard deviation of
the measurements (often denoted {{<katex>}}\sigma{{</katex>}}) divided
by the square root of the sample size (often denoted n).  Thus the
standard error of the mean (for IID data), often denoted _SEM_, is
{{<katex>}}\sigma/\sqrt{n}{{</katex>}}.

The expression for the standard error of the mean,
{{<katex>}}\sigma/\sqrt{n}{{</katex>}},
tells a great deal about what factors of the
population and sample influence the precision of our estimate.  To
have a precise estimate, we want the standard error to be small.
Thus, we see that we have a small standard error when either
{{<katex>}}\sigma{{</katex>}} is small, {{<katex>}}n{{</katex>}} is
large, or both.  It is natural that having more data
(a larger value of {{<katex>}}n{{</katex>}})
leads to a more
precise estimate of the population mean.  The fact that the sample size enters via its square
root implies that we need to increase the sample size by a factor of
four to reduce the standard error by a factor of two.  Thus, small
increases in the sample size do not bring a substantial improvement in
precision.  The value of {{<katex>}}\sigma{{</katex>}} describes the
variation in the individual values that we are studying.  It should
not be surprising that if these values are more dispersed, the
estimated value will be less precise.  We usually do not have control
over the value of {{<katex>}}\sigma{{</katex>}}, but it is important
to understand how its value influences the uncertainty in our estimates
of the population parameters of interest.

## Estimated standard errors and nuisance parameters

The exact value of the SEM depends on the standard deviation of the
measurements, {{<katex>}}\sigma{{</katex>}}, but this value is almost
never known.  We can estimate it using the sample standard deviation,
{{<katex>}}\hat{\sigma}{{</katex>}} of the data values, and use the
estimated standard deviation to produce an estimated standard error
{{<katex>}}\hat{\sigma}/\sqrt{n}{{</katex>}}.  But this introduces yet
more uncertainty into the analysis.  A quantity like
{{<katex>}}\sigma{{</katex>}} that is not of direct interest, but that
is needed to conduct uncertainty analysis on our quantity of direct
interest (i.e. the mean), is called a _nuisance parameter_.

Nuisance parameters can complicate statistical analyses.  The most
common way of dealing with a nuisance parameter is to estimate it, and
"plug-in" the estimated nuisance parameter to any formula that we are
working with.  This is sometimes called a "plug-in approach".

Standard errors for differences
-------------------------------

Differences, or _contrasts_ arise very frequently in data analysis.
For example, suppose we are interested in comparing the FEV values
between smokers and non-smokers.  A natural way to do this would be to
obtain samples of {{<katex>}}n_{\rm s}{{</katex>}} smokers and
{{<katex>}}n_{\rm ns}{{</katex>}} non-smokers.  Then we calculate the
sample means {{<katex>}}\overline{\rm FEV}_{\rm s}{{</katex>}} and
{{<katex>}}\overline{\rm FEV}_{\rm ns}{{</katex>}} for each group, and
then calculate their difference {{<katex>}}\overline{\rm FEV}_{\rm s}
- \overline{\rm FEV}_{\rm ns}{{</katex>}}.  This is an estimate of the
population contrast {{<katex>}}E[{\rm FEV}_{\rm s}] - E[{\rm FEV}_{\rm
ns}]{{</katex>}}.

Like any estimate, {{<katex>}}\overline{\rm FEV}_{\rm s} -
\overline{\rm FEV}_{\rm ns}{{</katex>}} is not equal to the
corresponding estimand {{<katex>}}E[{\rm FEV}_{\rm s}] - E[{\rm
FEV}_{\rm ns}]{{</katex>}}.  A standard error can be used to quantify
the typical error in this setting.  The standard error for
{{<katex>}}\overline{\rm FEV}_{\rm s}{{</katex>}} alone is
{{<katex>}}\sigma_{\rm s}/\sqrt{\rm n_s}{{</katex>}}, where
{{<katex>}}\sigma_s{{</katex>}} is the standard deviation of FEV
values for smokers.  Similarly, the standard error for
{{<katex>}}\overline{\rm FEV}_{\rm ns}{{</katex>}} alone is
{{<katex>}}\sigma_{\rm ns}/\sqrt{n_{\rm ns}}{{</katex>}}, where
{{<katex>}}\sigma_{\rm s}{{</katex>}} is the standard deviation of FEV
values for non-smokers.

A very general result from probability tells us how to combine the
uncertainty in two independent estimates when we subtract them.  If
{{<katex>}}s_1{{</katex>}} and {{<katex>}}s_2{{</katex>}} are two
standard deviations, say for independent estimates
{{<katex>}}A{{</katex>}} and {{<katex>}}B{{</katex>}}, then the
standard deviation for {{<katex>}}A-B{{</katex>}} is
{{<katex>}}\sqrt{s_1^2+s_2^2}{{</katex>}}.  Thus, the standard error
for {{<katex>}}\overline{\rm FEV}_{\rm s} - \overline{\rm FEV}_{\rm
ns}{{</katex>}} is

{{<katex>}}
\sqrt{\sigma_{\rm s}^2/n_{\rm s} + \sigma_{\rm ns}^2/n_{\rm ns}}.
{{</katex>}}

Note that this standard error contains two nuisance parameters,
{{<katex>}}\sigma_{\rm s}{{</katex>}} and {{<katex>}}\sigma_{\rm
ns}{{</katex>}}.  We can get an estimated standard error by plugging
their estimated values into the exact standard error:

{{<katex>}}
\sqrt{\hat{\sigma}_{\rm s}^2/n_{\rm s} + \hat{\sigma}_{\rm ns}^2/n_{\rm ns}}.
{{</katex>}}

Standard errors for proportions
-------------------------------

A proportion is actually a mean, but proportions arise so often that
their standard error is usually calculated in a special way.  The
proportion is the number of times that something happens, out of a
given set of opportunities for it to happen.  Suppose we ask four
people whether they have consumed alcohol in the past week, and the
responses are "yes", "no", "no", and "yes".  The proportion of people
responding "yes" is 1/2.  If we code "yes" as 1 and "no" as zero, then
the data can be represented as 1, 0, 0, 1, and the proportion of "yes"
responses is (1 + 0 + 0 + 1) / 4 = 1/2.  This example illustrates why
proportions are actually equivalent to means.

Suppose that {{<katex>}}X{{</katex>}} is a random variable
representing a binary outcome, say {{<katex>}}X=1{{</katex>}}
corresponds to a respondent stating that they drank alcohol in the
last week, and {{<katex>}}X=0{{</katex>}} corresponds to the
respondent stating that they have not had any alcohol in the past
week. The "event probability" is denoted {{<katex>}}p{{</katex>}} and
defined to be {{<katex>}}P(X=1){{</katex>}}.  A fact that we will not
prove here is that the variance of {{<katex>}}X{{</katex>}} is
{{<katex>}}p(1-p){{</katex>}}.  Therefore the standard error for the
sample proportion based on {{<katex>}}n{{</katex>}} independent and
identically distributed observations of {{<katex>}}X{{</katex>}} is
{{<katex>}}\sqrt{p(1-p)/n}{{</katex>}}.

Standard errors for other statistics
------------------------------------

Every statistic has a standard error, but in many cases the exact form
of the standard error is difficult to derive.  More advanced
statistics courses develop methods for calculating and approximating
standard errors for more difficult settings than we consider here.  We
will provide one more standard error here because it is quite useful
and extremely simple.  If we calculate the sample correlation
coefficient for paired values {{<katex>}}(x_1, y_1), \ldots, (x_n,
y_n){{</katex>}}, an iid sample from a bivariate distribution
{{<katex>}}(X, Y){{</katex>}}, then the approximate standard deviation
(or standard error) for the sample correlation coefficient is simply
{{<katex>}}1/\sqrt{n}{{</katex>}}.  This is an approximate standard
error, but works well in many settings.
