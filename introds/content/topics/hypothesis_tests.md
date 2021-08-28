Hypothesis tests
================

Formal hypothesis testing is perhaps the most prominent and
widely-employed form of statistical analysis.  It is sometimes seen as
the most rigorous and definitive part of a statistical analysis, but
it is also the source of many statistical controversies.  The
currently-prevalent approach to hypothesis testing dates to
developments that took place between 1925 and 1940, especially the
work of [Ronald
Fisher](https://en.m.wikipedia.org/wiki/Ronald_Fisher), [Jerzy
Neyman](https://en.m.wikipedia.org/wiki/Jerzy_Neyman), and [Egon
Pearson](https://en.m.wikipedia.org/wiki/Egon_Pearson).

In recent years, many prominent statisticians have argued that less
emphasis should be placed on the formal hypothesis testing approaches
developed in the early twentieth century, with a correspondingly
greater emphasis on other forms of uncertainty analysis.  Our goal
here is to give an overview of some of the well-established and
widely-used approaches for hypothesis testing.  We will also provide
some perspectives on how these tools can be effectively used, and
discuss their limitations.  We will also discuss some new approaches
to hypothesis testing that may eventually come to be as prominent as
these classical approaches.

A _falsifiable hypothesis_ is a statement, or hypothesis, that can be
contradicted with evidence.  In empirical (data-driven) research, this
evidence will always be obtained through the data.  In statistical
hypothesis testing, the hypothesis that we formally test is called the
_null hypothesis_.  The _alternative hypothesis_ is a second
hypothesis that is our proposed explanation for what happens if the
null hypothesis is wrong.

Suppose for example that we are interested in whether newly-licensed
drivers have a higher risk of being in a serious accident than drivers
who have substantial driving experience.  In a formal hypothesis
testing analysis, we would state as our null hypothesis that
"newly-licensed drivers and experienced drivers are equally likely to
be in a severe accident".  The alternative hypothesis might be that
"newly-licensed drivers are more likely to be in a severe accident
than experienced drivers".  The null hypothesis is sometimes denoted
{{<katex>}}H_0{{</katex>}} and the alternative hypothesis is sometimes
denoted {{<katex>}}H_1{{</katex>}} or {{<katex>}}H_A{{</katex>}}.
Formal hypothesis testing provides us with a way to summarize the
evidence relating to these competing hypotheses in a concise way.  It
does not tell us which hypothesis is correct, and it does not even
tell use which hypothesis we should believe is correct.  But it does
summarize the evidence in a way that allows us to make this judgement
in a principled way.

Test statistics
---------------

The key element of a statistical hypothesis test is the _test
statistic_, which (like any statistic) is a function of the data.  A
test statistic takes our entire dataset, and reduces it to one number.
This one number ideally should contain all the information in the data
that is relevant for assessing the two hypotheses of interest, and
exclude any aspects of the data that are irrelevant for assessing the
two hypotheses.  The test statistic measures evidence against the null
hypothesis.  Most test statistics are constructed so that a value of
zero represents the lowest possible level of evidence against the null
hypothesis.  Test statistic values that deviate from zero represent
greater levels of evidence against the null hypothesis.  The larger
the magnitude of the test statistic, the stronger the evidence against
the null hypothesis.

A major theme of statistical research is to devise effective ways to
construct test statistics.  Many useful ways to do this have been
devised, and there is no single approach that is always the best.  In
this introductory course, we will focus on tests that starting with an
estimate of a quantity that is relevant for assessing the hypotheses,
then proceed by standardizing this estimate by dividing it by its
standard error.  This approach is sometimes referred to as "Wald
testing", after [Abraham
Wald](https://en.m.wikipedia.org/wiki/Abraham_Wald).

Testing the equality of two proportions
---------------------------------------

As a basic example, let's consider risk perception related to
COVID-19.  As you will see below, hypothesis testing can appear at
first to be a fairly elaborate exercise.  Using this example, we
describe each aspect of this exercise in detail below.

### The data and research question

The data shown below are simulated but are designed to reflect actual
surveys conducted in the United States in March of 2020.  Partipants
were asked whether they perceive that they have a substantial risk of
dying if they are infected with the novel coronavirus.  The number of
people stating each response, stratified on age, are shown below (only
two age groups are shown):

|            | High risk  | Not high risk |
| :--        |  ---:      | ---:          |
| Age < 30   |    25      |    202        |
| Age 60-69  |    30      |    124        |

Each subject's response is _binary_ -- they either perceive themselves
to be high risk, or not to be at high risk.  When working with this
type of data, we are usually interested in the proportion of people
who provide each response within each stratum (age group).  These are
conditional proportions, conditioning on the age group.  The numerical
values of the conditional proportions are given below:

|           | High risk | Not high risk |
| :--       |  ---:     | ---:          |
| Age < 30  |   0.110   |   0.890       |
| Age 60-69 |   0.195   |   0.805       |


There are four conditional proportions in the table above -- the
proportion of younger people who perceive themselves to be at higher
risk, 0.110=25/(25+202); the proportion of younger people who do not
perceive themselves to be at high risk, 0.890=202/(25+202); the
proportion of older people who perceive themselves to be at high risk
0.195=30/(30+124); and the proportion of older people who do not
perceive themselves to be at high risk, 0.805=124/(30+124).

The trend in the data is that younger people perceive themselves to be
at lower risk of dying than older people, by a difference of
0.195-0.110=0.085 (in terms of proportions).  But is this trend only
present in this sample, or is it generalizable to a broader population
(say the entire US population)?  That is the goal of conducting a
statistical hypothesis test in this setting.

### The population structure

Corresponding to our data above is the unobserved population
structure, which we can denote as follows

|           | High risk                  | Not high risk                 |
| :--       |  ---:                      | ---:                          |
| Age < 30  |   {{<katex>}}p{{</katex>}} |   {{<katex>}}1-p{{</katex>}}         |
| Age 60-69 |   {{<katex>}}q{{</katex>}} |   {{<katex>}}1-q{{</katex>}}         |

The symbols {{<katex>}}p{{</katex>}} and {{<katex>}}q{{</katex>}} in
the table above are _population parameters_.  These are quantitites
that we do not know, and wish to assess using the data.  In this case,
our null hypothesis can be expressed as the statement {{<katex>}}p =
q{{</katex>}}.  We can estimate {{<katex>}}p{{</katex>}} using the
sample proportion {{<katex>}}\hat{p} = 0.110{{</katex>}}, and
similarly estimate {{<katex>}}q{{</katex>}} using {{<katex>}}\hat{q} =
0.195{{</katex>}}.  However these estimates do not immediately provide
us with a way of expressing the evidence relating to the hypothesis
that {{<katex>}}p=q{{</katex>}}.  This is provided by the test
statistic.

### A test statistic

As noted above, a test statistic is a reduction of the data to one
number that captures all of the relevant information for assessing the
hypotheses.  A natural first choice for a test statistic here would be
the difference in sample proportions between the two age groups, which
is 0.195 - 0.110 = 0.085.  There is a difference of 0.085 between the
perceived risks of death in the younger and older age groups.

The difference in rates (0.085) does not on its own make a good test
statistic, although it is a good start toward obtaining one.  The
reason for this is that the evidence underlying this difference in
rates depends also on the absolute rates (0.110 and 0.195), and on the
sample sizes (227 and 154).  If we only know that the difference in
rates is 0.085, this is not sufficient to evaluate the hypothesis in a
statistical manner.  A given difference in rates is much stronger
evidence if it is obtained from a larger sample.  If we have a
difference of 0.085 with a very large sample, say one million people,
then we should be almost certain that the true rates differ (i.e. the
data are highly incompatiable with the hypothesis that
{{<katex>}}p=q{{</katex>}}).  If we have the same difference in rates
of 0.085, but with a small sample, say 50 people per age group, then
there would be almost no evidence for a true difference in the rates
(i.e.  the data are compatiable with the hypothesis
{{<katex>}}p=q{{</katex>}}).

To address this issue, we need to consider the uncertainty in the
estimated rate difference, which is 0.085.  Recall that the estimated
rate difference is obtained from the sample and therefore is almost
certain to deviate somewhat from the true rate difference in the
population (which is unknown).  Recall from our study of standard
errors that the standard error for an estimated proportion is
{{<katex>}}\sqrt{p(1-p)/n}{{</katex>}}, where {{<katex>}}p{{</katex>}}
is the outcome probability (here the outcome is that a person
perceives a high risk of dying), and {{<katex>}}n{{</katex>}} is the
sample size.

In the present analysis, we are comparing two proportions, so we have
two standard errors.  The estimated standard error for the younger
people is {{<katex>}}\sqrt{0.11\cdot 0.89/227} \approx
0.021{{</katex>}}.  The estimated standard error for the older people
is {{<katex>}}\sqrt{0.195\cdot 0.805/154} \approx 0.032{{</katex>}}.
Note that both standard errors are estimated, rather than exact,
because we are plugging in estimates of the rates (0.11 and 0.195).
Also note that the standard error for the rate among older people is
greater than that for younger people.  This is because the sample size
for older people is smaller, and also because the estimated rate for
older people is closer to 1/2.

In our previous discussion of standard errors, we saw how standard
errors for independent quantities {{<katex>}}A{{</katex>}} and
{{<katex>}}B{{</katex>}} can be used to obtain the standard error for
the difference {{<katex>}}A-B{{</katex>}}.  Applying that result here,
we see that the standard error for the estimated difference in rates
0.195-0.11=0.085 is {{<katex>}}\sqrt{0.021^2 + 0.032^2} \approx
0.038{{</katex>}}.

The final step in constructing our test statistic is to construct a
Z-score from the estimated difference in rates.  As with all Z-scores,
we proceed by taking the estimated difference in rates, and then
divide it by its standard error.  Thus, we get a test statistic value
of {{<katex>}}0.085 / 0.038 \approx 2.24{{</katex>}}.

A test statistic value of 2.24 is not very close to zero, so there is
some evidence against the null hypothesis.  But the strength of this
evidence remains unclear.  Thus, we must consider how to calibrate
this evidence in a way that makes it more interpretable.

### Calibrating the evidence in the test statistic

By the central limit theorem (CLT), a Z-score approximately follows a
normal distribution.  When the null hypothesis holds, the Z-score
approximately follows the standard normal distribution (recall that a
standard normal distribution is a normal distribution with expected
value equal to 0 and variance equal to 1).  If the null hypothesis
does not hold, then the test statistic continues to approximately
follow a normal distribution, but it is not the standard normal
distribution.

A test statistic of zero represents the least possible evidence
against the null hypothesis.  Here, we will obtain a test statistic of
zero when the two proportions being compared are identical,
i.e. exactly the same proportions of younger and older people perceive
a substantial risk of dying from a disease.  Even if the test
statistic is exactly zero, this does not guarantee that the null
hypothesis is true.  However it is the least amount of evidence that
the data can present against the null hypothesis.

In a hypothesis testing setting using normally-distrbuted Z-scores, as
is the case here (due to the CLT), the standard normal distribution is
the _reference distribution_ for our test statistic.  If the Z-score
falls in the center of the reference distribution, there is no
evidence against the null hypothesis.  If the Z-score falls into
either tail of the reference distribution, then there is evidence
against the null distribution, and the further into the tails of the
reference distribution the Z-score falls, the greater the evidence.

### P-values

The most conventional way to quantify the evidence in our test
statistic is through a probability called the _p-value_.  The p-value
has a somewhat complex definition that many people find difficult to
grasp.  It is the probability of observing as much or more evidence
against the null hypothesis as we actually observe, calculated when
the null hypothesis is assumed to be true. We will discuss some ways
to think about this more intuitively below.

For our purposes, "evidence against the null hypothesis" is reflected
in how far into the tails of the reference distribution the Z-score
(test statistic) falls.  We observed a test statistic of 2.24 in our
COVID risk perception analysis.  Recall that due to the "empirical
rule", 95% of the time, a draw from a standard normal distribution
falls between -2 and 2.  Thus, the p-value must be less than 0.05,
since 2.24 falls outside this interval.  The p-value can be calculated
using a computer, in this case it happens to be approximately 0.025.

As stated above, the p-value tells us how likely it would be for us to
obtain as much evidence against the the null hypothesis as we observed
in our actual data analysis, if we were certain that the null
hypothesis were true.  When the null hypothesis holds, any evidence
against the null hypothesis is spurious.  Thus, we will want to see
stronger evidence against the null from our actual analysis than we
would see if we know that the null hypothesis were true.  A smaller
p-value therefore reflects more evidence against the null hypothesis
than a larger p-value.

By convention, p-values of 0.05 or smaller are considered to represent
sufficiently strong evidence against the null hypothesis to make a
finding "statistically significant".  This threshold of 0.05 was
chosen arbitrarily 100 years ago, and there is no objective reason for
it.  In recent years, people have argued that either a lesser or a
greater p-value threshold should be used.  But largely due to
convention, the practice of deeming p-values smaller than 0.05 to be
statistically significant continues.

### Summary of this example

Here is a restatement of the above discussion, using slightly
different language.  In our analysis of COVID risk perceptions, we
found a difference in proportions of 0.085 between younger and older
subjects, with younger people perceiving a lower risk of dying.  This
is a difference based on the sample of data that we observed, but what
we really want to know is whether there is a difference in COVID risk
perception in the population (say, all US adults).

Suppose that in fact there is no difference in risk perception between
younger and older people.  For instance, suppose that in the
population, 15% of people believe that they have a substantial risk of
dying should they become infected with the novel coronavirus,
regardless of their age.  Even though the rates are equal in this
imaginary population (both being 15%), the rates in our sample would
typically not be equal.  Around 3% of the time (0.024=2.4% to be
exact), if the rates are actually equal in the population, we would
see a test statistic that is 2.4 or larger.  Since 3% represents a
fairly rare event, we can conclude that our observed data are not
compatible with the null hypothesis.  We can also say that there is
statistically significant evidence against the null hypothesis, and
that we have "rejected" the null hypothesis at the 3% level.

In this data analysis, as in any data analysis, we cannot confirm
definitively that the alternative hypothesis is true.  But based on
our data and the analysis performed above, we can claim that there is
substantial evidence against the null hypothesis, using standard
criteria for what is considered to be "substantial evidence".

Comparison of means
-------------------

A very common setting where hypothesis testing is used arises when we
wish to compare the means of a quantitative measurement obtained for
two populations.  Imagine, for example, that we have two ways of
manufacturing a battery, and we wish to assess which approach yields
batteries that are longer-lasting in actual use.  To do this, suppose
we obtain data that tells us the number of charge cycles that were
completed in 200 batteries of type A, and in 300 batteries of type B.
For the test developed below to be meaningful, the data must be
independent and identically distributed samples.

The raw data for this study consists of 500 numbers, but it turns out
that the most relevant information from the data is contained in the
sample means and sample standard deviations computed within each
battery type.  Note that this is a huge reduction in complexity, since
we started with 500 measurements and are able to summarize this down
to just four numbers.

Suppose the summary statistics are as follows, where
{{<katex>}}\bar{x}{{</katex>}},
{{<katex>}}\hat{\sigma}_x{{</katex>}}, and {{<katex>}}n{{</katex>}}
denote the sample mean, sample standard deviation, and sample size, respectively.

| Type       | {{<katex>}}\bar{x}{{</katex>}} | {{<katex>}}\hat{\sigma}_x{{</katex>}} |   {{<katex>}}n{{</katex>}}  |
| --:        |  --:                           |     --:                               | --:                        |
|   __A__    |  420                           |  70                                   |  200                       |
|   __B__    |  403                           |  90                                   |  300                       |

The simplest measure comparing the two manufacturing approaches is
the difference 420 - 403 = 17.  That is, batteries of type A tend
to have 17 more charge cycles compared to batteries of type B.  This
difference is present in our sample, but is it also true that the entire
population of type A batteries has more charge cycles than the entire
population of type B batteries?  That is the goal of conducting a hypothesis
test.

The next step in the present analysis is to divide the mean difference, which
is 17, by its standard error.  As we have seen, the standard error of the mean,
or SEM, is {{<katex>}}\sigma/n{{</katex>}}, where {{<katex>}}\sigma{{</katex>}}
is the standard deviation and {{<katex>}}n{{</katex>}} is the sample size.
Since {{<katex>}}\sigma{{</katex>}} is almost never known, we plug in
its estimate {{<katex>}}\hat{\sigma}{{</katex>}}.  For the type A batteries,
the estimated SEM is thus {{<katex>}}70/\sqrt{200} \approx 4.95{{</katex>}},
and for the type B batteries the
estimated SEM is {{<katex>}}90/\sqrt{300} \approx 5.2{{</katex>}}.

Since we are comparing two estimated means that are obtained from independent
samples, we can pool the standard deviations to obtain an overall standard
deviation of {{<katex>}}\sqrt{4.95^2 + 5.2^2} \approx 7.18{{</katex>}}.
We can now obtain our test statistic {{<katex>}}17/7.18 \approx 2.37{{</katex>}}.

The test statistic can be calibrated against a standard normal reference distribution.
The probability of observing a standard normal value that is greater in magnitude
than 2.37 is 0.018 (this can be obtained from a computer).  This is the p-value,
and since it is smaller than the conventional threshold of 0.05, we can claim
that there is a statistically significant difference between the average
number of charge cycles for the two types of batteries, with the A batteries
having more charge cycles on average.

The analysis illustrated here is called a _two independent samples Z-test_,
or just a  _two sample Z-test_.  It may be
the most commonly employed of all statistical tests.  It is also common to
see the very similar _two sample t-test_, which is different only in that it
uses the _Student t distribution_
rather than the normal (Gaussian) distribution to calculate the p-values.
In fact, there are quite a few minor variations on this testing framework,
including "one sided" and "two sided" tests, and tests based on different
ways of pooling the variance.
Due
to the CLT, if the sample size is modestly large (which is the case here), the
results of all of these tests will be almost identical.  For simplicity,
we only cover the Z-test in this course.

Assessment of a correlation
---------------------------

The tests for comparing proportions and means presented above are quite
similar in many ways.  To provide one more example of a hypothesis
test that is somewhat different,
we consider a test for a correlation coefficient.

Recall
that the sample correlation coefficient {{<katex>}}\hat{r}{{</katex>}} is
used to assess the relationship, or association, between two quantities
X and Y that are measured on the same units.  For example, we may ask
whether two biomarkers, serum creatinine and D-dimer, are correlated
with each other.  These biomarkers are both commonly used in medical
settings and are obtained using
blood tests.  D-dimer is used to assess whether a person has blood
clots, and serum creatinine is used to measure kidney performance.

Suppose we are interested in whether there is a correlation in the
population between D-dimer and serum creatinine.  The population
correlation coefficient between these two quantitites can be
denoted {{<katex>}}r{{</katex>}}.  Our null hypothesis is
{{<katex>}}r=0{{</katex>}}.  Suppose that we observe a sample
correlation coefficient of {{<katex>}}\hat{r}=0.15{{</katex>}},
using an independent and identically distributed sample of
pairs {{<katex>}}(x, y){{</katex>}}, where
{{<katex>}}x{{</katex>}} is a D-dimer measurement and
{{<katex>}}y{{</katex>}} is a serum creatinine measurement.
Are these data consistent with the null hypothesis?

As above, we proceed by constructing a test statistic by
taking the estimated statistic and dividing it by its standard
error.  The approximate standard error for
{{<katex>}}\hat{r}{{</katex>}} is {{<katex>}}1/\sqrt{n}{{</katex>}},
where {{<katex>}}n{{</katex>}} is the sample size.  The test
statistic is therefore {{<katex>}}\sqrt{n}\cdot \hat{r} \approx 1.48{{</katex>}}.

We now calibrate this test statistic by comparing it to a standard
normal reference distribution.  Recall from the empirical rule
that 5% of the time, a standard normal value falls outside the
interval (-2, 2).  Therefore, if the test statistic is smaller
than 2 in magnitude, as is the case here, its p-value is greater
than 0.05.  Thus, in this case we know that the p-value will
exceed 0.05 without calculating it, and therefore there is no
basis for claiming that D-dimer and serum creatinine levels are
correlated in this population.

Sampling properties of p-values
-------------------------------

A p-value is the most common way of calibrating evidence.  Smaller
p-values indicate stronger evidence against a null hypothesis.
By convention, if the p-value is smaller than some threshold,
usually 0.05, we reject the null hypothesis and declare a finding
to be "statistically significant".  How can we understand more
deeply what this means?  One major concern should be obtaining
a small p-value when the null hypothesis is true.  If the null
hypothesis is true, then it is incorrect to reject it.  If
we reject the null hypothesis, we are making a false claim.
This can never be prevented with complete certainty, but we
would like to have a very clear understanding of how likely
it is to reject the null hypothesis when the null hypothesis
is in fact true.

P-values have a special property that when the null distribution
is true, the probability of observing a p-value smaller than
0.05 is 0.05 (5%).  In fact, the probability of observing
a p-value smaller than {{<katex>}}t{{</katex>}} is equal to
{{<katex>}}t{{</katex>}}, for any threshold {{<katex>}}t{{</katex>}}.
For example, the probability of observing a p-value smaller
than 0.1, when the null hypothesis is true, is 10%.

This fact gives a more concrete understanding of how strong
the evidence is for a particular p-value.  If we always
reject the null hypothesis when the p-value is 0.1 or smaller,
then over the long run we will reject the null hypothesis 10%
of the time when the null hypothesis is true.  If we always
reject the null hypothesis when the p-value is 0.05 or smaller,
then over the long run we will reject the null hypothesis 5%
of the time when the null hypothesis is true.

Power
-----

The approach to hypothesis testing discussed above largely follows the
framework developed by RA Fisher around 1925.  Note that although
we mentioned the alternative hypothesis above, we never actually used it.
A more elaborate approach to hypothesis testing was developed somewhat
later by Egon Pearson and Jerzy Neyman.  The "Neyman-Pearson" approach
to hypothesis testing is even more formal than Fisher's approach, and is
most suited to highly planned research efforts in which the study is
carefully designed, then executed.  While ideally all research projects
should be carried out this way, in reality we often conduct research using
data that are already available, rather than using data that are specifically
collected to address the research question.

Neyman-Pearson hypothesis testing involves specifying an alternative hypothesis
that we anticipate encountering.  Usually this alternative hypothesis represents
a realistic guess about what we might find once the data are collected.  In each of
the three examples above, imagine that the data are not yet collected, and we
are asked to specify an alternative hypothesis. We may arrive at the following:

* In comparing risk perceptions for COVID, we may anticipate that older
people will perceive a 30% risk of dying, and younger people will anticipate
a 5% risk of dying.

* In comparing the number of charge cycles for two types of batteries, we may
anticipate that batter type A will have on average 500 charge cycles, and battery
type B will have on average 400 charge cycles.

* In assessing the correlation between D-dimer and serum creatinine levels,
we may anticipate a correlation of 0.3.

Note that none of the numbers stated here are data-driven --
they are specified before any data are collected, so they
do not match the results from the data, which were collected only later.
These alternative hypotheses are all essentially
speculations, based perhaps on related data or theoretical considerations.

There are several benefits of specifying an explicit alternative hypothesis,
as done here, even though it is not strictly necessary and can be avoided
entirely by adopting Fisher's approach to hypothesis testing.  One benefit
of specifying an alternative hypothesis is that we can use it to assess the
_power_ of our planned study, which can in turn inform the design of the study,
in particular the sample size.  The power is the probability of rejecting
the null hypothesis when the alternative hypothesis is true.  That is, it
is the probability of discovering something real.  The power should be contrasted
with the _level_ of a hypothesis test, which is the probability of rejecting
the null hypothesis when the null hypothesis is true.  That is, the level
is the probability of "discovering" something that is not real.

To calculate the power, recall that for many of the test statistics that we
are considering here, the test statistic has the form
{{<katex>}}\hat{\theta}/{\rm SE}(\hat{\theta}){{</katex>}}, where
{{<katex>}}\hat{\theta}{{</katex>}} is an estimate.
For example, {{<katex>}}\hat{\theta}{{</katex>}})
may be the correlation coefficient between D-dimer and serum creatinine levels.
As stated above, the power is the probability of rejecting the null hypothesis
when the alternative hypothesis is true.  Suppose we decide to reject
the null hypothesis when the test statistic is greater than 2, which is
approximately equivalent to rejecting the null hypothesis when the p-value
is less than 0.05.  The following calculation tells us how to obtain
the power in this setting:

{{<katex>}}
\begin{array}{lll}
P(\sqrt{n}\hat{r} > 2) &=& P(\sqrt{n}(\hat{r} - r + r) > 2)\\
&=& P(\sqrt{n}(\hat{r} - r) > 2 - \sqrt{n}r)\\
\end{array}
{{</katex>}}

Under the alternative hypothesis, {{<katex>}}\sqrt{n}(\hat{r} - r){{</katex>}}
approximately follows a standard normal distribution.  Therefore, if
{{<katex>}}r{{</katex>}} and {{<katex>}}n{{</katex>}} are given, we can
easily use the computer to obtain the probability of observing a value
greater than {{<katex>}}2 - \sqrt{n}r{{</katex>}}.  This gives us the power
of the test.  For example, if we anticipate {{<katex>}}r=0.3{{</katex>}} and
plan to collect data for {{<katex>}}n=100{{</katex>}} observations, the
power is 0.84.  This is generally considered to be good power -- if the
true value of {{<katex>}}r{{</katex>}} is in fact 0.3, we would reject
the null hypothesis 84% of the time.

A study usually has poor power because it has too small of a sample size.
Poorly powered studies can be very misleading, but since large sample
sizes are expensive to collect, a lot of research is conducted using sample
sizes that yield moderate or even low power.  If a study has low power, it
is unlikely to reject the null hypothesis even when the alternative hypothesis
is true, but it remains possible to reject the null hypothesis when the null
hypothesis is true (usually this probability is 5%).  Therefore the most
likely outcome of a poorly powered study may be an incorrectly rejected
null hypothesis.