% Samples and Populations
% Kerby Shedden
% September 8, 2020

In most statistical analyses, the _sample_ is the data that we have
and can work with.

The sample is a subset of the _population_, which is usually much
larger than the sample (often it is infinite).

Ideally the sample should be _representative_ of the population.  We
will define the term "representative" more precisely later.

If the sample is not representative of the population, then there is
still a possibility of obtaining meaningful results from our analysis
of the data, but we need to be aware of the ways in which our sample
fails to be representative.

Whether a sample is representative is largely determined by how the
sample is collected.  "Random samples" (to be discussed later in
detail) are often but not always representative.  Non-random samples
can also be representative, if chosen carefully.

---

Examples of populations
-----------------------

A population is to some extent imaginary, but some populations
are more tangible and easier to work with than others.

If we are studying the adult population of the United States,
the population is fairly concrete (if not taken too literally).

Suppose we are conducting an experiment in which we grow plants using
different types of fertilizer.  We select eight plots of land, and
randomly select four of them to use fertilizer A, and the remaining
four plots use fertilizer B.

We then grow the plants for one growing season, and measure the yield.

What is the population here?  There are several ways to approach this:
one possibility is to imagine all the similar plots of land that we
could have chosen but did not, then imagine the results that we would
have obtained had we used these other plots in our study.

---

Simple Random Samples
---------------------

A simple random sample (SRS) from a finite population is one in which
every subset of the desired size is equally likely to be selected.

Imagine that our population contains three elements labeled A, B, and
C.

A simple random sample of size 2 results from a process in which we
obtain the samples {A, B}, {A, C}, and {B, C} one-third of the time
each.

Note that in a simple random sample, each element of the population
can only be included in the sample one time.

A SRS is often obtained sequentially by sampling "without
replacement".  We draw an element from the population at random, and
do not return it to the population (therefore, it can never be chosen
again).

---

Independent and identically distributed samples
-----------------------------------------------

In the fertilizer experiment (discussed earlier), the population is
arguably infinite, as there are infinitely many possible plots of land
that could be included in the study.

Also, based on the day that we start the study, the amount of rainfall
in the year that the study is run, and many other factors that we
cannot control, the results would presumably vary.

Therefore, it is not easy to imagine how we would obtain a simple
random sample in the setting of the fertilizer experiment.

An _independent and identically distributed_ sample, or _IID sample_
is a more abstract type of sample that can be used in cases where it
doesn't make sense to think about an SRS.

---

Independent and identically distributed samples
-----------------------------------------------

In an IID sample $x_1, \ldots, x_n$:

* Each element of the (usually infinite) population is equally likely
to be included as the $k^\textrm{th}$ element of the sample,
i.e. $x_k$ is equally likely to be any element of the population.

* The inclusion of one element of the population into the sample, say
as element $k$, does not impact or contain any information about the
values of the other elements of the sample.

The second condition implies that the sample can contain repeated
elements.

An IID sample can be generated sequentially by sampling "with
replacement".  We draw an element from the population, and after
noting what value we obtained, we return it to the population.
Therefore, we are just as likely to draw it again when selecting the
remainder of the sample.

---

Example of a non-IID sample
---------------------------

Our goal is to obtain a representative sample of the adult population
of Japan.  We place an add on Facebook (that runs only in Japan),
offering 25 USD to anyone who completes our on-line questionnaire.
After someone completes the survey, they are asked to name up to five
friends who will then be shown the same ad the next time they log into
Facebook.

Why is this not an IID sample (or an SRS), and therefore likely not
representative of the population?

* Not everyone is on Facebook (so everyone in the population is not
equally likely to be included in the sample).

* Some people are more likely to be incentivized to participate by the
cash offer (again, everyone in the population is not equally likely to
be included in the sample).

* Since participants can share the offer with their friends, one
person being in the sample
influences the likelihood that their friends will be included in the
sample (violates condition 2).

---

Example of a non-IID sample
---------------------------

We are interested in rainfall patterns within Texas during late
spring.  We selected 50 locations inside Texas, and measured the
rainfall at those locations for every day in May, 2019.

We can think of the population as being every possible location
on every day of May in every year (say since 1900).

Why is this not an IID sample (or an SRS), and therefore likely not
representative of the population?

* May, 2019 may have been have had unusual weather that differed from
May in other years.

* The 50 locations that we selected may have different climates than
most other regions in Texas.
