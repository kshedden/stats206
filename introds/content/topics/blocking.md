Blocking, matching, and paired comparisons
==========================================

In research that aims to rigorously attribute mechanisms to one or
more explanatory factors, it is difficult yet very important to
attempt to isolate the roles of factors of primary interest from the
roles of other factors that are of lesser interest.

As an example, suppose we are interested in the relationship between
regular exercise and cognitive function in older adults.  A very
simple study design would be to recruit, say, 200 subjects, interview
them about their physical activity, administer a cognitive assessment,
then compare the cognitive scores between people with high and low
levels of physical activity.

This design could yield misleading results for a number of reasons.
One issue is that there could be confounders that affect both physical
activity and cognitive level.  For example, perhaps people with full
time jobs have higher cognitive scores but lower physical activity.
In this case, having a full time job is a confounder of the
relationship between physical activity and cognitive ability.

Another issue is that there could be variables that strongly influence
only one of the variables of interest, for example, perhaps physical
activity differs by sex but cognitive ability does not.  In this case,
sex is not a confounder, but heterogeneity due to sex differences will
reduce the statistical power to understand the relationship between
physical activity and cognitive level.

One way to address these issues is by _blocking_ the data prior to
analysis.  Essentially, this means that we put the units into groups
that are similar in terms of factors that are of lesser interest, so
that we can more clearly see the roles of the factors that are of
primary interest.

Blocking is a very general and broadly-applicable strategy.  It can be
implemented in many ways, but in this course we will only consider one
type of blocking, which is a paired test of means.  This test is best
known as the _paired t-test_, but we will be considering only the
approximate large sample version of this test which we will call the
_paired Z-test_.

Continuing with the example above, suppose we recruit only identical
twin sisters into our study, selecting only twins for which one sister
has high physical activity and the other sister has low physical
activity.  Even though twin sisters tend to be alike in many ways,
physical activity is not completely heritable, so it should be
possible to identify twin sisters who are different in this particular
way.

Identical twins are genetically identical, and usually experience a
shared environment during childhood.  This diminishes or eliminates
many potential confounders and removes a great deal of heterogeneity.

The data for this analysis can be denoted {{<katex>}}(x_i,
y_i){{</katex>}}, where {{<katex>}}x_i{{</katex>}} is the cognitive
score for the sister with high physical activity and
{{<katex>}}y_i{{</katex>}} is the cognitive score for the sister with
low physical activity.  In a conventional unpaired Z-test, we would
use the following test statistic:

{{<katex>}}
(\bar{x}-\bar{y})/\sqrt{\hat{\sigma}_x^2/n + \hat{\sigma}_y^2/n}
{{</katex>}}

Note that here, the sample sizes for the two groups
({{<katex>}}x_i{{</katex>}} and {{<katex>}}y_i{{</katex>}}) are the
same, so there is only one sample size {{<katex>}}n{{</katex>}}.

A paired Z-test works with the differenced data {{<katex>}}z_i = x_i -
y_i{{</katex>}}.  As a result, we are only comparing each individual
with high physical activity to her sister with low physical activity,
rather than comparing every individual with high activity to every
other individual with low physical activity.  By comparing only within
same-sex siblings, we eliminate the roles of many confounders and many
variables of secondary interest.

The null hypothesis for this analysis is that the expected value of
the {{<katex>}}x_i{{</katex>}} is equal to the expected value of the
{{<katex>}}y_i{{</katex>}}.  This null hypothesis implies that the
expected value of the {{<katex>}}z_i{{</katex>}} is zero.  We
therefore need an appropriate test statistic for this hypothesis.

To construct this test statistic, we start with the sample mean
{{<katex>}}\bar{z}{{</katex>}}, and standardize it by dividing it by
its standard error.  As we know, the standard error of the mean, or
SEM, is {{<katex>}}\sigma^2/n{{</katex>}} which we can estimate in
this setting with {{<katex>}}\hat{\sigma}_z^2/n{{</katex>}}, where
{{<katex>}}\hat{\sigma}_z{{</katex>}} is the sample standard deviation
of the {{<katex>}}z_i{{</katex>}}.  Finally, invoking the CLT, we
compare the test statistic to a standard normal reference
distribution.

As an example, suppose we found that {{<katex>}}\bar{z} =
0.8{{</katex>}} and {{<katex>}}\hat{\sigma}_z = 3.9{{</katex>}} with a
sample size of {{<katex>}}n=150{{</katex>}}.  The test statistic in
this case will be around 2.51, which yields a p-value of around 0.01.
Thus, we can declare that there is a statistically significant
difference between the cognitive scores of active and less-active
women, with the active women having higher cognitive scores.

It is instructive to consider what might happen in this setting if we
ignored the pairing, and conducted an unpaired two sample Z-test.  By
rearranging terms, we can see that {{<katex>}}\bar{z} = \bar{x} -
\bar{y}{{</katex>}}.  Thus, the numerators of the paired and unpaired
test statistics are identical.  In this example, both are equal to
0.8.  However the denominators of the test statistics can be quite
different, and in general, the denominator of the unpaired statistic
will be larger.  Suppose, for example, that
{{<katex>}}\hat{\sigma}_x=5.2{{</katex>}} and
{{<katex>}}\hat{\sigma}_y=6.1{{</katex>}}.  In this case, the unpaired
test statistic will be equal to 1.22, which provides no evidence for a
significant difference.  Thus, in this case we reject the null
hypothesis under the paired test, but not under the unpaired test.

The reason that the paired test usually has more power than the
unpaired test is that we select the pairs to be similar in terms of
many characteristics that are not of interest.  By doing so, the
effects of these uninteresting characteristics cancel out when we
subtract the data within pairs.  Note that there is no "free lunch"
here.  If we do not have a natural way to pair the data, e.g. if in
the study of cognitive level we pair people at random rather than
pairing people who are similar, there will be no gain in power, and
the paired and unpaired tests will almost always agree.
