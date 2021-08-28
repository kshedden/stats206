Measurement
===========

In designing a data-driven research study, two of the most important
questions are "who to measure" and "what to measure".  The first
question is about what "units" we should study.  The second question
is about what characteristics of these "units" we should focus on.
_Measurement_ deals with all aspects of capturing the relevant
characteristics of our analysis units.  In some cases, measurement is
fairly straightforward.  If we want to know how many cars a person
owns, most people can provide a straightforward answer about this when
asked.  Nevertheless, we could encounter some corner cases where
someone may have an undriveable car parked in their backyard,
or a motorcycle, or a car that
they own jointly with another person.

Traits that arise in various fields of scientific study are often
quite difficult to measure.  Here are three examples:

* In molecular biology, there are many traits related to genetics, or
to the molecular composition of cells and tissues, or to the
microbiome that is resident in nearly all multicellular organisms.  In
recent years, great progress has been made in developing assays that
allow molecular-level traits to be measured on humans and other
research subjects.  However these assays are expensive, hard to use,
and are subject to poorly-understood errors.

* In physics, some atomic and subatomic phenomena are extremely
difficult to measure, and we can even encounter the famed "Heisenberg
uncertainty principal", stating that certain characteristics of a
particle are impossible to measure together.

* In psychology, the field of "measurement" has been studied
intensely.  For example, the challenges of measuring "mood",
"personality", and various forms of "intelligence" have been
extensively considered over the past 100 years.

Systematic and random measurement error
---------------------------------------

_Measurement error_ is any difference that exists between the
measurement we make, and the idealized value that we would wish to
obtain.  From a statistical perspective, measurement errors are often
seen as having two components: a _systematic component_ and a _random
component_.  The systematic component of measurement error affects all
collected data values equally.  The random component of measurement
error impacts each collected data value in a unique way.

Systematic measurement error reflects _bias_ that is inherent in the
measurement process.  For example, if you conduct a survey of office
workers and ask people whether they ever come to work intoxicated, the
data are likely to underestimate the rate at which this happens.  This
is due to "social desirability bias" that impacts the way that people
respond to questions about sensitive topics.  This type of error is
almost certainly systematic rather than random, since it is much more
likely that people will fail to acknowledge a socially undesirable
activity, rather than exaggerate it.

Random measurement error is often simply thought of as "noise".  Even
a physical measurement like length or mass can only be measured in
practice to some degree of precision.  Attempts to measure beyond the
precision limits of the measurement instrument may lead to seemingly
random errors in the data -- these errors are random because in many
cases it is equally likely that the error leads to the value being
larger than the truth versus being smaller than the truth.

Some traits, like blood pressure, are known to have a very substantial
component of random error when measured in the conventional way (i.e. with
a blood pressure cuff).  If two people measure a subject's blood
pressure at almost the same time, or if one person measures a
subject's blood pressure twice in rapid succession, the measured values can
easily differ by 10 mm/Hg (the units of blood pressure).  This may be
because of a subjective component to the way that the measures are
obtained (the person taking the reading has to make judgments based
on sounds), or it may be because the subject's actual blood pressure can
change quite rapidly, making it difficult to define a value that is
meaningful beyond the moment at which it was measured. Regardless, it is difficult to quantify a
person's blood pressure to high precision due to a major contribution
from random measurement error.

It is important to distinguish random measurement error from actual
variation in the trait of interest.  Considering the trait of blood
pressure, as noted above there may be 10 mm/Hg random measurement error
in any particular blood pressure measurement.  However the true blood
pressures of two different people may differ, and the true blood
pressure of one person may change over time.  By "true" blood
pressure, we mean the blood pressure as if it were measured without
any measurement error.  If these differences in true blood pressure
are similar to or smaller in magnitude than the measurement error, it
may be hard to see the differences using data, but the differences are
still there.  For blood pressure, inter-person differences can easily
be 40 mm/Hg or more; differences of this magnitude will be easily
distinguishable from the measurement error.

Systematic and random sources of measurement error have very different
implications for the analysis that is being conducted.  Due to the law
of large numbers, which we will discuss later in the course, the
impact of random measurement error on many summary statistics will
diminish as the sample size grows. This is because random measurement
errors tend to "cancel out" when averaging.  However systematic
measurement errors are not impacted by sample size.  Thus, in many
settings, systematic errors are the greater challenge, although if
data are very expensive to collect and we are forced to work with a
small sample, random measurement errors can also play a major role in
determining the overall uncertainty of our findings.
