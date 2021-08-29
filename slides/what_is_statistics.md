% What is data science?
% Kerby Shedden
% September 3, 2020

The term __data__ refers to a collection of values (numeric, text, or other forms) that measure
something of interest, or that convey information about a question at
hand.

Data are useful because they help us answer questions about the world that arise in
science, business, government, and other areas.

__Data science__ is the study of methods for drawing meaningful insight from data.

It is a _methodological_ subject, because it primarily deals with the _techniques_
that we use to learn things, and not the specific _domains_ where the techniques
are applied.

---

# What do data scientists know and do?

Data scientists know how to _use_ methods and tools for analyzing data.

More importantly, data scientists _study_ methods for analyzing
data, just like biologists study living organisms and sociologists
study human behavior.

Data scientists understand the _properties_ of methods for analyzing
data:

- When do they give meaningful results?

- When might they give misleading results?

- What remains uncertain after we have made full use of our data?

- What properties do various data science methods have, independent
  of the specific domain in which they are applied?

---

# Data science as a tool for research

_Research_ is any effort that aims to answer a question that has
never been answered before.

Successful research almost always starts with a focused question.
Research efforts that do not aim to address a specific question
usually fail.

- _Empirical_ research proceeds by observation, taking measurements, and
interpreting what is observed.

- _First principles_ research proceeds through logical deduction and theory.

Data science belongs to the "empirical" branch of research methodology,
but can also contribute to first principles research.

---

# Allied fields of data science

- __Statistics__ : the rigorous study of variation and uncertainty; the
science of gaining insight from data

- __Computer science__ : the study of computation, information, algorithms

- __Mathematics__ : a formal framework for studying quantity,
structure, relation, shape, order, and change.

Statistics contributes approaches for making predictions and drawing
mechanistic insights from data, for defining the limitations of what can be learned
from various forms and amounts of data, and for constructing efficient approaches
to learning from data.

Mathematics provides a way to define the foundational
concepts of data science, through which we can rigorously assess
(via proof) whether data science techniques posess desirable properties.

Computer science contributes formal systems for representing data,
for transforming it via algorithms, and provides principles for
structuring efficient and verifiable algorithms and software implementations
for manipulating data, enabling us to gain insight into their meaning.

---

# Variation

Given any type of "entity" (people, firms, bicycles, asteroids...)
there are properties that all entities of the type posess.

In almost any real-world setting, any interesting property will
vary among entities of the same type.

- People have varying heights

- Firms have varying valuations

- Bicycles have varying sizes

- Asteroids have varying shapes

---

# Uncertainty

Data provide us with a window into the system that we are studying.

But a finite amount of data will almost never reveal every aspect of
a complex system of interest.

"Uncertainty" refers to the limits of
what we can learn about the system that we are studying
based on the data that we posess.

__Example__: What percentage of American adults think that
US presidential elections should allow voting by mail?  We can never know
this percentage exactly.  However we can conduct a survey in which
we ask 1000 adults their attitude about this issue.  This
study may lead us to conclude that it is very likely ("with high confidence")
that between 58% and 64% of US adults support allowing mail-in
voting.  By providing our findings as a range, we are accounting for uncertainty --
our inability to know the exact answer to our question of interest.

---

# Probability

Probability is a branch of mathematics.  It is the foundation of
statistics and one of the pillars of data science.

Probability gives us tools for understanding variation.

Probability gives us a formal framework for thinking about uncertainty.

---

# Samples and populations

Most statistics (and data science) takes place within a formal framework
with two levels:

- The __population__ is the complete system of interest.  It is usually
impossible to obtain an exact and complete representation of the population,
or to answer any question about the population exactly.

- The __sample__ is a finite subset, or a "partial view" of the population.
It is always something that we can obtain and study directly.

---

# Examples of samples and populations

- If we are interested in the attitudes of the US adult population in regard
to some issue, say immigration policy, then the set of all adults in the US is the population; a sample
would be any subset of this population for whom we can actually observe or
measure the attitudes of interest.

- If we are interested in the strength of glass made in a particular manner, the
population is the set of all possible pieces of glass manufactured in this way; the
sample is a finite set of pieces of glass that were actually manufactured, provided
to us, and subsequently measured for strength.

- If we are interested in the effectiveness of a drug for treating dementia,
the population would be the responses to the drug for all possible patients
with the relevant form of dementia; a sample would be the measured effectiveness
of the drug for a finite number of people who are given the drug and then observed.

- If we are interested in the Earth's climate, the population is a complete description of
all possible climate parameters (wind, temperature, humiditiy, etc. at every location on
Earth and at every time since the Earth was formed); a sample would be a finite set of observed parameters,
possibly measured with some amount of error.

---

# Prediction

One of the main goals of data science is to turn data into predictions.

* If we have data on what items customers have purchased in the past, can we make
predictions about what items a specific customer will purchase in the future?

* If we have data on people's responses to a medical treatment
in the past, can we make predictions about what types of people will respond
well to the treatment in the future?

* If we have data on driving characteristics of various drivers, can we
make predictions about what specific drivers will be involved in a serious car
accident in the future?

Data-driven predictions can be used to solve real-world problems, and often
can be commercialized.  However they don't tell us "why" something is happening,
which means that predictions alone are not a substitute for the human-led
process of scientific research.

---

# Attribution and causality

The goal of science is usually to understand why something is happening, not
only to observe what is happening.

It is often said that science focuses on understanding "mechanisms", not
only on "description".

The connection between empirical (observation-driven) and mechanistic science
is that in the latter we _attribute_ our observations to specific underlying
_causes_.

Many data sets, on their own, do not allow us to make assertions about the
causes or mechanisms that underly our observations.  For example, if we observe
that patients with a disease who take drug A have better outcomes than
patients with the disease who take drug B, we don't know if this is due to the
drug, or due to some other difference between the patients taking the two drugs
(e.g. maybe patients who choose to take drug A have milder disease).

Many empirical research efforts are subject to "confounding" -- two phenomena
can be related without either causing the other: "correlation is not
causation".

In some settings, data science can be used to assess causal hypotheses about a system -- but
there are many subtle challenges in doing so.

__Experiments__ can provide strong evidence for (or against) causality.  An
experiment is a data collection effort in which specific measures have
been taken to prevent confounding.

Data that are not collected in a deliberate way to avoid confounding are called
_observational_.  It is easy to forget that a dataset is observational, and
incorrectly make a causal claim based on it.

