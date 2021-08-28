Types of studies
================

The central goal of data science is to answer meaningful questions
using data.  Here we will discuss various formal approaches to conducting research using
data science techniques.  A _study_ is a focused and rigorous research
effort aiming to address a specific question.  A good study should be
carefully _designed_ before being carried out.  There are many types
of studies, and the design of any particular study is determined by
the question of interest, the type of data that will be collected, and
the ethical and logistical challenges that constrain data collection.
We will discuss all of these issues here.

Research efforts can be broadly categorized into those that are
_observational_, meaning that data are collected from systems behaving
unperturbed in their natural way, and _interventional_, meaning that
we manipulate the system, or create an artificial system that we can
control, in order to obtain our data.  Both observational and
interventional approaches to research are common in all domains of
science and engineering, including in academic, government, and
industrial research settings.

Observational studies
---------------------

Observational studies, as the name suggests, involve mostly passive
observation of unperturbed systems.  A commonly encountered type of
observational study is one that aims to establish risk factors or
protective factors for health outcomes in humans.  In the most
prototypical of these studies, we have an _exposure_ which is
something that people do, or that happens to people.  The exposure is
then considered in relation to another variable called the _outcome_,
which may be caused by the exposure, or associated with it.  Examples
below will make this more concrete.

Suppose we are interested in the relationship between the consumption
of processed food and the presence of tooth decay.  To understand this
relationship, we might collect data on people's processed food
consumption (the exposure), and the presence or extent of tooth decay
in the same subjects (the outcome).  If the people who consume more
processed food have more tooth decay, then we have found an
_association_ between these two variables.

The critical issue with an observational study is that the subjects
with a higher level of the exposure may also have other
characteristics that influence their outcome.  For example, it may be
that the people who consume processed food also tend to smoke, and it
is actually the smoking that leads to the tooth decay.  Or, it could
be that people who consume a lot of processed food are less meticulous
when brushing their teeth.  There are an almost unlimited number of
such factors that could be imagined.

### Confounders

A factor such as smoking or oral hygiene is known as a _confounder_,
since it is potentially related to both the exposure and the outcome.
As a result, we don't know if the exposure causes the outcome
directly, or if the exposure causes the confounder, which in turn
causes the outcome.  Other possibilities exist as well: the confounder
could cause the exposure, which then causes the outcome, or another
(unmeasured or unknown) factor could cause both the exposure and the
outcome.

Most scientific research aims to identify mechanisms and causes.  That
is, we want to know not just what happens, but why it happens.
Therefore, when using data analysis in the setting of scientific
research, it is important to be clear about when any findings might
support a causal or mechanistic relationship, or alternatively if they only
identify an association.  An association is generally a weaker type of
scientific finding compared to a causal relationship.

An everyday example of a confounder would arise if we measure the air
temperature, the intensity of sunlight, and the number of cars driving
on the street.  We would likely see an association between the number
of cars driving on the street and the air temperature, since the
traffic on most roads is higher during the day, and the air
temperature is also higher during the day.  But common sense tells us
that traffic is not the main factor causing days to be warmer than
nights (heat emitted from the vehicles would make a very small
contribution compared to the warmth from the sun).  The association
between traffic and air temperature is a real association (it would
continue to be found as we collect more data in different locations),
but it is not causal.  Such an association is sometimes called a
_spurious association_.  The relationship between sunlight intensity
and temperature, however, is causal.

Observational research is widely used in science, but it can be the
source of much controversy.  Most observational research cannot, on
its own, provide evidence that a relationship is causal.  In the mid
20th century, some famous statisticians argued that smoking was not a
cause of lung cancer, but rather people who smoke are doing other
things that increase their risk of lung cancer.  There is now an
overwhelming consensus that smoking is a causal factor behind many
types of cancer.  Part (but not all) of the evidence for this comes
from observational studies.  Careful interpretation of multiple
observational studies bearing on an important question can help
support a causal relationship, although other lines of argument are
generally needed to fully demonstrate that a relationship is causal.

One way to use observational analyses to support a causal claim is to
carefully consider all the plausible confounders, and either directly
account for their effects, or, argue that the observed relationship is
too strong to be entirely attributable to the confounders.  In this
way, we can increase the quality of evidence that comes from an
observational study. In doing this, we need to distinguish between
three types of confounders: (i) known, measured confounders, (ii)
known, unmeasured confounders, and (iii) unknown confounders.  Note
that unknown confounders must always be unmeasured.

For example, in the study of tooth decay discussed above, smoking is
known to be associated with unhealthy diet (e.g. processed food
consumption) and with tooth decay.  Therefore, smoking is a confounder
of the relationship between processed food consumption and tooth
decay.  But we can measure whether a person smokes.  Therefore, this
is a known, measured confounder.  There are statistical techniques (to
be discussed later in the course) that can at least partly account for
a known, measured confounder such as smoking.  On the other hand, it
might be quite difficult to get an accurate sense of a person's oral
hygiene habits.  Thus, this will be a known but unmeasured confounder.

Fortunately, improvements in technology often can turn a known,
unmeasured confounder into a known, measured confounder.  For example,
it may be possible to develop an electric toothbrush that records its
use, making it much easier to obtain accurate information about
people's oral hygiene habits.  Such a device is known as a _sensor_.
Use of advanced sensors is revolutionizing many areas of research, and
is a major driver behind the demand for data science experts and new
data science techniques.

The limitation of this strategy of identifying and accounting for
confounders is that there can always be unknown confounders that we
have not yet identified.  For example, almost every health outcome can
be influenced by genetics, and we are still decades away from having a
comprehensive understanding of the genetic determinants of many human
traits.  Therefore, genetic factors will remain an unknown confounding
factor for many observational relationships for the foreseeable
future.

Interventional studies
----------------------

In an interventional study, the factor of interest is controlled by
the researcher, rather than happening naturally to the subjects.  An
interventional study is most often called an _experiment_.
Experiments are the canonical way approach to scientific
investigations, although in many areas of science it is difficult to
conduct experiments for ethical or logistical reasons.

For example, we could consider turning our observational study looking
at the relationship between processed food consumption and tooth decay
into an experiment.  To do so, we would need the ability to force some
people to consume processed food, and prevent other people from doing
so.  In a type of experiment called a _randomized controlled trial_
(RCT), we would randomly choose some people to never consume processed
food, these people would comprise the _control arm_ of the experiment.
The remaining people would be required to consume processed food, and
these people would comprise the _treatment arm_ of the experiment.
Because the assignment to the treatment and control arms in a RCT is
random, it is impossible for there to be any confounders -- any
association between processed food consumption and tooth decay seen in
a properly conducted RCT is causal, not spurious.  However, there are
significant ethical and practical constraints in such a study that may
make it quite difficult to conduct.

It is unethical to induce someone to do something that is known to be
harmful to them.  It may be possible to induce people to stop eating
processed food, e.g. by giving them a financial reward for doing so.
Thus, we could conduct a study in which people are randomly assigned
to a treatment arm in which they are induced to eat no processed food,
and a control arm in which they eat whatever they choose.  This may be
sufficient to demonstrate a relationship between processed food
consumption and tooth decay.  However, since the control group may
choose to eat relatively small amounts of processed food, and the
treatment group may also choose to each processed food (i.e. the
inducement may fail), then the difference between the two groups may
be attenuated.  Also, since tooth decay develops somewhat slowly over
time, it would be very difficult to maintain these controlled
influences on people's behaviors over, say, several years.

In some limited circumstances, it may be ethical to conduct a study in
which people are induced to do something that may confer some risk,
such as eating more processed food.  But this could only be done for a
limited time, and could never be done with a dangerous and addictive
exposure such as smoking. For example, it may be possible to conduct a
study in which people are provided with an unhealthy meal once a day
for a month.  A study like this would be reviewed very carefully
before being approved by an Institutional Review Board (IRB, the panel
of experts that must approve all studies within an institution that
involve human subjects).  Also, it would be necessary to demonstrate
ahead of time that the value of performing the study is high.  Such a
study would almost certainly be restricted to low-risk participants
(e.g. young people with no significant health problems).

Analogously, it may be possible to completely prevent people from
eating processed food for a short period of time, for example, by
having the subjects live in a research facility where all of their
food is provided to them.  But clearly this would be expensive, and
could only be done for a short period of time (far too short to see an
association with tooth decay).

Other aspects of study design
-----------------------------

The distinction between observational and interventional studies is
arguably the most important aspect of a research study.  But there are
other aspects of study designs that are also important to be aware of.
We will discuss a few such notions here.

A _cross-sectional_ study takes a dynamic, time-evolving system, and
studies it based on a snapshot taken at a specific point in time.
Cross-sectional studies are somewhat simpler to conduct than other
types of studies, but may be less informative.  For example, a basic
cross-sectional study looking at the relationship between processed
food consumption and dental cavities would involve contacting people
on a single occasion, and asking them about their diet and oral
hygiene habits.  Since we would only be contacting the subjects one
time, we would only be able to directly measure the _current status_
of these two factors.  We would not know anything about processed food
consumption in the past, so we would not know whether any cavities
that are present preceded, or followed periods of eating a diet heavy
in processed foods. Due to these and other issues, most
cross-sectional studies provide less evidence for causal relationships
than other types of observational studies.

A _longitudinal study_ involves repeated interactions with the same
subject over a period of time.  On each occasion, we obtain additional
data.  In our study of dental cavities, we would see new cavities as
they occur, and we would also be able to track changes in people's
dietary and oral hygiene habits.  A critical advantage of a
longitudinal study over a cross-sectional study is that we can see the
temporal ordering of the exposure and the outcome, rather than only
seeing them at one time (as would be the case for diet in a cross
sectional study), or seeing them only in cumulative form (as would be
the case for cavities in a cross-sectional study).  Longitudinal
studies require more effort and expense for those collecting the data,
and can sometimes involve more advanced statistical methods for data
analysis.  But in most cases, a longitudinal study will provide a
better quality of evidence than a cross-sectional study.

Studies can have either a _prospective_ or a _retrospective_
character, and this distinction is especially relevant for studies
involving human subjects.  A retrospective study is one in which all
data are collected after the events of interest have occurred.  For
example, if we were interested in the relationship between dental
cavities and processed food consumption in young children, but
collected data from teenagers, then this would be a retrospective
study.  In a prospective study for the same research question, we
would enroll young children into our study, and follow them as they
progress through childhood.  A retrospective study often asks the
subjects to recall past exposures and past outcomes, and for many such
characteristics recall can be inaccurate and biased.

In general, prospective studies yield more informative data than
retrospective studies.  But in some situations, retrospective studies
can still provide high-quality evidence.  In the case of dental
cavities, dental records should provide accurate information about
when cavities occurred.  However data on food consumption obtained
retrospectively would generally be far inferior to data on food
consumption obtained prospectively.

A _trial_ is a specific type of research study aiming to establish
whether one way of doing something is more effective than another.
Trials are especially common in medical research, where they are often
called "clinical trials."  The goal of a clinical trial is usually to
establish whether a drug, medical device, or therapy is safe and
effective.  Trials also arise in non-medical settings.  For example,
in education research we may have a trial to compare different
approaches to teaching a subjects.  In manufacturing, we may have a
trial to compare the efficiency and quality of two ways of
manufacturing a product.

A _case/control study_ is used when studying a rare trait (such as a
rare disease).  In a standard case/control study, we identify a set of
people with the trait of interest, say, people who are being treated
for a form of cancer in a particular hospital, then we identify an
equal number of people who don't have the disease.  The people with
the disease are the _cases_ and the people without the disease are the
_controls_.  This basic case/control design has 1:1 matching, so that
there is one control for every case.  Other ratios are possible,
e.g. having three controls for every case.  Often in a case/control
study, we will attempt to match the cases to the controls on other
relevant factors.  For example, if we are studying cancer cases whose
average age is 68, we would aim to identify controls whose average age
is 68.

A _cohort study_ is essentially the opposite of a case/control study.
In a cohort study we identify a collection of individuals (say,
people), and then determine who within that group has the condition of
interest and who does not.  For example, we could define the
population of Ann Arbor residents over age 65 as the cohort, and then
aim to identify within that cohort who has a particular disease of
interest.  Cohort studies also have cases and controls, but the "case
status" is determined after the sample is obtained, rather than being
part of the sampling process.

A _cluster sample_ is a common way of collecting data on very large
populations that are very dispersed and thus difficult to sample
directly.  A basic example of a cluster sample of the United States
population would be to first randomly sample 20 counties out of all
counties in the US.  Then we would randomly sample, say, 100 people
from each of the 20 selected counties.  This would give us an overall
sample size of 2000, but it is not a simple random sample of the
United States population.  Each person is equally likely to be
included in the sample, but each subset of size 2000 is not equally
likely to be chosen (this is the definition of simple random sample).
Subsets that cover more than 20 counties have zero chance of being
selected in the cluster sample described above.

The main reason to use a cluster sample is logistics.  If you aim to
interview people, or request administrative data (say medical or
school records), it is much easier to work with a limited number of
counties, and interview or otherwise obtain data on multiple people
per county, rather than having a sample that is spread over the US,
with most people in our study being the only representative of their
county.

A _survey_ is a study whose goal is to estimate the absolute level of
one or more variables, with a particular focus on obtaining estimates
that accurately reflect a defined target population.  For example, we
may wish to estimate the proportion of people who support a candidate
in an upcoming election.  For such an estimate to be of value, it is
essential that it reflect the population of people who are eligible to
vote, or who are likely to vote in the election.  An estimate that
reflects only a subset of people in the population is of very little
value, because it is not generally a good predictor of the election's
outcome.  Although accurately reflecting a target population is
desirable in many forms of research, it is most essential in a survey,
since that is the explicit goal of many surveys.

The main challenge of a survey is that in most cases we cannot force
people to respond or participate.  This leads to a form of _selection
bias_, in which it is possible that, say, supporters of one candidate
in an election are under-represented in the survey compared to
supporters of another candidate.  This could lead to the survey
misstating which candidate is expected to win the election.  A common
technique in survey research for addressing this issue is to use
_weighting_ to compensate for this.  For example, suppose that we
conduct a survey in which men are half as likely to respond as women.
A weighting adjustment would involve counting each man's vote twice
when estimating the level of support for each candidate.
