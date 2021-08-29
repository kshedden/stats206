% Types of studies
% Kerby Shedden
% October 2, 2020

Research methodology
====================

Empirical research is a process
of asking questions, and gathering and interpreting evidence
to attempt to answer those questions.

Data science is a tool that is used in empirical research.

Research is conducted in academic settings, as well as in
industry and government.  It takes place in a huge range
of domains.

---

Research methodology
====================

When research is conducted in a formal manner, a single focused
research effort is called a _study_.

A good study should be _designed_, then executed.  Following
completion of the study, the raw data are available for
analysis and interpretation.

Data science is relevant at both the point of desiging a study,
and at the point of intepretion, data analysis, and synthesizing
the results into conclusions and findings.

Sometimes, data science tools are used in very informal
research efforts that do not follow a pre-defined plan.  These
could be exploratory efforts, which are sometimes quite
productive.  However most successful research efforts, regardless
of the setting, are executed according to a design, or plan
that is carefully considered before embarking on data collection
and analysis.

---

Research methodology
====================

Many studies can be seen as falling into one of the following two major
types:

* __Observational__: A study in which the system
of interest is observed in an unperturbed manner.

* __Interventional__: A study in which the system
of interest is perturbed or manipulated in order to elicit the findings of interest.

---

0bservational studies
=====================

Observational studies are extremely common, and are very frequently
reported in the media.  Most observational studies aim to make
comparisons, or to identify
_associations_.  Informally, an association is a relationship
between two variables.

For example, people with sugar-heavy diets may have more tooth decay.
This is an association that we would likely find evidence for if we were to conduct
a study where we collected data on sugar consumption and tooth decay.

A critical limitation of an observational study is that we cannot
conclude that an association is _mechanistic_ or _causal_.  Instead,
many associations that are found in observational studies are
spurious consequences of _confounders_.

---

Confounding
===========

A confounder is a variable that is associated with each of the two primary
variables being assessed in an observational study.

Suppose that we wish to conduct research looking at the relationship
between smoking and tooth decay.  Two possible confounders here are
age, and having fluoridated water at home.  It is possible that
older people may be more likely to smoke, and more likely to have tooth decay;
it is also possible that people without fluoridated water may be more likely
to smoke, and more likely to have tooth decay.

If either age or fluoridated water act in this way, they are confounders.
When confounders are present, we cannot conclude from our observational
study that smoking causes tooth decay.

Confounding is the reason that "correlation does not equal causation".

---

Confounding
===========

There are three main types of confounders:

* Known and measured

* Known but not measured

* Unknown

If known and measured confounders are present, it is usually possible to "adjust"
for them and reduce or eliminate their impact.

If known and unmeasured confounders are present, it may be possible to speculate
about their possible roles as confounders.

---

Interventional studies
======================

In an interentional study, the key variables of interest are manipulated
by the researchers, rather than occurring "naturally" (e.g. by the choice
of the research subjects).

It is (relatively) easy to conduct an interventional study with non-living
systems, or with non-human living systems.

For example, if we have two
types of glass for mobile phone screens, and we wish to know
which type results in a more shatter-resistant screen, we could manufacture 10 devices
with each type of glass, and test them for shatter-resistance.  This is
an interventional study because the researcher is directing which
devices be manufactured with each type of glass.

---

Randomized studies
==================

An interventional study gives us tools that we can use to minimize
the risk that any confounding is present.  The most useful such
tool is _randomization_.

Randomization (or "randomized assignment") means that we first
select a group of individuals (units) to participate in the study, then
randomly assign the levels of the primary variable of interest
to the individuals.

Randomization is not always ethically or practically possible.  We
cannot direct people to smoke in order to learn about the consequences
of smoking.

---

Randomized studies
==================

In the mobile phone study, we might have a means to randomly select
one phone out of each hundred that are produced at the factory, and randomly
select that the phone be manufactured with one or the other of the two types of
glass.

Randomization (if properly done) eliminates the risk of confounding.

Without randomization, there might still be a chance that there are
other reasons (besides the glass)
that the phones in one group were more prone to shattering (e.g.
the installer, other components of the device).

---

Randomized controlled trials
============================

A Randomized Controlled Trial (RCT) is especially common in research
involving human subjects, to establish the effectiveness of some
sort of "treatment".

_Control_ in this setting means that the treatment is always compared
to something that is already well-understood.

Randomization means that the determination as to which subjects recieve
the "active" treatment and which recieve the control is made at random.

---

Balance, representativeness, and controlled comparisons
=======================================================

In some research, the goal is to estimate a characteristic
of a population, for example:

* What percentage of US adults support a particular political candidate?

* What is the average extent of sulfidation on turbine blades in
US commercial aircraft?

Goals such as this have no explicit comparison.  The key factor
for such research to be successful is to have a representative
sample.

---

Balance, representativeness, and controlled comparisons
=======================================================

Other forms of research focus on making a comparison,
for example:

* Are people with lower levels of vitamin D more susceptible to
infections?

* Which of two forms of mathematics instruction is more effective
for children?

For addressing such comparative questions, it is very important
to minimize the roles of factors (confounders)
other than what we are studying.

---

Balance, representativeness, and controlled comparisons
=======================================================

Randomization (if properly conducted) gaurantees balance with respect to all
possible confounders on average.  However in small samples, the balance may
be poor for some factors.  Real-world circumstances (compliance, drop-out)
may also diminish the balance.

Suppose we are comparing people with high and low vitamin D levels
in an observational study.  To the extent possible, we would
like our two comparison groups to be balanced on as many other
traits as possible (sex, age, ...).  Lacking randomization, we
can try to achieve this through careful selection of subjects.

Sometimes, having a balanced
sample is in tension with having a representative sample.

---

Other aspects of study design
=============================

* Cross-sectional, longitudinal

* Prospective, retrospective

* Case/control, cohort

* Survey
