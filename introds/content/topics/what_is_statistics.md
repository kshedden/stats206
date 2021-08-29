What is data science?
=====================

The term _data_ refers to any collection of observations that measure something of
interest, or that convey information about a question at hand.  This is a
data science course, and also a statistics course.  For our purposes, the terms "data science" and "statistics" are essentially synonyms,
referring to the methodology used to learn from data.  Mathematics and computer science are
also important components of data science.

Nearly every branch of science involves collecting and analyzing data,
but a "domain scientist" such as a biologist or a sociologist is primarily
interested in the core questions of their domain, not in the methods used
to analyze data.  Data scientists
do analyze data, but even more importantly, data scientists analyze the
_methods_ for analyzing data.  This is what distinguishes a data
scientist, or a statistician, from a scientist studying and analyzing
a data set
that arises in their domain of research.

Good data science, like good statistics, starts with a question.  For
example, in a business setting, we may have questions about what type
of person is most likely to buy a product, or whether people would be
willing to pay more for a product that has premium features.  In
natural and social science, questions are often expressed in the form
of a _hypothesis_.  For
example, in a medical research setting we may have a hypothesis that
"people who sleep less than six hours per night tend to have higher
blood pressure than people who sleep more than seven hours per night".
When we express such a hypothesis, we must be open to the possibility
that the hypothesis is either true or false.  Upon systematically
collecting relevant data, we will accumulate evidence that informs
us about the truth of our hypothesis.

Data science is part of an _empirical_ approach to answering research
questions, meaning that we make progress by observing, taking
measurements, and collecting and interpreting data.  In contrast, a
_first principles_ approach to research aims to answer questions using
logical deduction and theory.  Logical deduction and theory do play
important roles in data science, but in data science we prefer as much
as possible to "let the data speak for itself".

Data science and statistics are "methodological" subjects, meaning
that they focus on developing methods, tools, and approaches for
conducting empirical investigations.  A primary aim of data science is to
develop an understanding of the strengths and
limitations of various methods for analyzing data.  Thus, data science
is to some extent a "meta subject" which focuses on the merits of different
approaches for learning about reality.

There is a very active theoretical branch of data science that deals with
"pure" questions about data analysis that exist outside the context of any 
specific application.  However this
course will primarily develop the tools of statistics and data science
through case studies that are set in various application domains.
There is also a more abstract dimension to this course, because we
will see that statistical tools often have properties that hold
regardless of the specific type of data or application context in
which the tool is applied.

Uncertainty in data analysis
----------------------------

Statistical data analysis is based on the idea that the data we collect in
order to address our questions of interest can never be sufficient to
povide definitive answers.  There will always be _uncertainty_ in
our findings.  The goal of a statistical data analysis is to obtain
the strongest conclusions that can legitimately be made from the
available data, and then quantify the uncertainty in these findings.

Historically, it has been challenging to formalize exactly what we
mean by "uncertainty".  A major advance occurred in the late 1800's,
when probability theory matured as a branch of mathematics.
Probability theory turns out to be a very useful tool for defining and
quantifying what we mean by "uncertainty".  In spite of decades of
progress, there remain many unresolved challenges in statistical data
analysis.  New methods and approaches to analyzing data continue to be
developed, and the strengths and limitations of existing methods
continue to be examined.  Statistics and data science are dynamic
fields, and there is ongoing active discussion and healthy debate as
to which approaches to data analysis are most appropriate in various
settings.

Samples and populations
-----------------------

The most prototypical setting for a statistical analysis is when our
data constitute a representative or random sample from a population of interest.  We
will discuss these terms in much more detail later in the course.  For
now, we will introduce the main ideas using an example.  Suppose that
our research goal is to estimate the fraction of adults in the
state of Michigan who travel more than 20 miles to work each day.
Imagine that we could obtain a representative sample of 1,000 adults
in Michigan (which has an adult population of roughly 7.5 million, so
our sample contains less than one in seven thousand of the
population).  If 274 of the people in our sample travel more than 20
miles to work each day, then we would estimate that 274/1000 = 27.4%
of the Michigan population travels more than 20 miles to work each
day.

The true proportion of Michigan adults
who travel more than 20 miles to work each day is very unlikely
to be exactly equal to 27.4%
(i.e., it is very unlikely that exactly 2.055 million Michigan adults
travel more than 20 miles to work each day).  Although the true
proportion may be quite close to this value, it is very unlikely to be
exactly equal to it.  The goal of uncertainty quantification is to
state how different the estimated proportion obtained from the sample
of data that we have collected (27.4%) is from the exact, true proportion (which is
unknown).

It turns out that as long as we know some key pieces of information
about how our sample was obtained, then it is possible to make precise
and useful statements about the likely error in our estimate relative
to the truth.  On the other hand, if we know very little about how our
sample was obtained, it can be very difficult to say anything about
such errors.  This is a very common theme in statistics and data
science -- it is very important to understand how the data being
analyzed were collected, otherwise we will be very limited in the
types of claims that we can make.

More challenging population settings
------------------------------------

A representative sample from a finite population, as described above,
is perhaps the simplest setting in which to conduct a data analysis.
Unfortunately, our data and population are usually more challenging to
work with.

One such example is "time series" data from a "dynamical system".
Such a system, can be continuously changing, so that the system we
observe today differs fundamentally from the system that we observed in
the past.  Consider, for example, research on the Earth's climate.  We
can collect data such as temperature, ice cover, and carbon dioxide
levels -- but the relationships among these variables may appear to
drift over time.  It's not that the laws of nature are changing, but
rather there are almost always additional relevant factors beyond what
we have measured.  As these unobserved quantities change, the
relationships among the observable variables may change as well.

Temporal systems with such dynamic behavior arise in many different
fields of research.  For example, in economics and public policy,
there is great interest in the relationship between public debt,
unemployment, and inflation.  In the past, it was consistently
observed that greater government spending was associated with
greater public debt, lower unemployment, wage growth, and price
inflation.  But in recent years, many regions of the world have
simultaneously experienced low unemployment, high public debt, and low
wage growth, but also low inflation.

A system that is in a constant state of structural change is said to
be "nonstationary".  Standard methods for analyzing data
from other settings may not give meaningful results here.  It is often
possible to carry out meaningful empirical research by analyzing data
obtained from such systems, but it is very important to be aware that
your data analysis is being conducted in such a setting, and to make
use of methods that are appropriate for it.

Causality
---------

The most interesting scientific findings are usually those that
identify causes.  For example, a researcher may have a hypothesis that
among those with COVID, people who are overweight are more likely to
become severely ill.  This hypothesis, while interesting, reflects a
"predictive" relationship, not necessarily one that is causal or
"mechanistic".  For example, it could be that the cause of severe
illness in COVID patients is insulin resistance, and overweight people
just tend to have insulin resistance (but a non-overweight COVID
patient with insulin resistance would be just as likely to become
severely ill).

Causal statements are usually much more interesting than
statements that are not causal.  But causal statements are more difficult to
demonstrate.  One of the major challenges in data analysis is to
identify the situations in which causal conclusions may be drawn.
Just as importantly, we should aim to determine when this cannot be done and
communicate to our audience that a causal conclusion is not
justified.
