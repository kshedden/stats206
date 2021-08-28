Samples and populations
=======================

An important principle in rigorous data analysis is that we should not
exclusively be interested in understanding the data that we have
collected.  Instead, our goal should be to use the data that we have
collected to learn about the _population_ that our data represent.
The act of using results from the _sample_ (the data in-hand) to make
statements about the population is called _generalization_, or
_inference_. In order to do this in a meaningful way, it is important
to be precise about what population we aim to generalize to, and about
how our data were collected.

Populations
-----------

In some situations, the population of interest is clear.  If we are
studying characteristics of the US adult population, such as income,
or health, then the population of interest could be taken to be the
set of all adults currently in the United States.  This population is
quite tangible, but even so, there are some ambiguities.  In the time
that it takes to read this paragraph, someone may have been born, and
someone else may have died, so the population will have changed.
Also, in some cases we may wish to treat the US population as people
residing in the US, or as people currently physically present in the
US, or as people with US citizenship or permanent residency,
regardless of where they are located at the moment.  Other meaningful
definitions of US population are also possible.

In some other settings where we wish to conduct a statistical
analysis, the appropriate notion of the population is somewhat less
clear.  Suppose our goal is to understand how the levels of different
soil nutrients relate to the yield of a crop such as corn.  We may
conduct an experiment in which we create plots of land with controlled
concentrations of the nutrients of interest, then grow corn in each
plot and measure the yield at the end of the growing season.  Suppose
we have 10 such plots of land.  It is clear that our sample consists
of these 10 plots.  The population is a bit more ambiguous.  We might
think of the population in this case as being all the plots that we
could have created for our experiment, but did not.  These plots will
be slightly different from the actual experimental plots with respect
to the key variables of interest (soil nutrients), and also with
respect to other variables that we cannot control, such as sunlight
and rainfall.  Therefore, they would have different corn yields than
the 10 plots that we actually observed.

Sampling
--------

As noted above, understanding how the sample was obtained is very
important. The most basic type of sample is a _simple random sample_,
or _SRS_.  A simple random sample of the US adult population is one in
which each possible sample of the population that has the desired
sample size, say n=1000, is equally likely to be chosen.  We have not
covered probability yet so cannot discuss this notion here in a
precise way.  But intuitively, you should imagine a SRS as resulting
from a completely random process where you select people from the
population like drawing beans from a jar.  Once a person is selected,
they cannot be selected again.  Thus, this type of sampling is
sometimes called _sampling without replacement_.

Although an SRS is ideal, in practice such a sample can be difficult
or impossible to obtain.  For example, we do not have access to a list
of all 328 million Americans, and even if we did, we would not have a
way to contact many of the people on the list, and those who we
contact cannot be compelled to participate in our research
project. For a population such as the entire United States, obtaining
a SRS is an ideal that cannot realistically be achieved.

For populations that are much smaller than a whole country, say the
population of all physicians working for the University of Michigan
Health System, it is more realistic that we could get an actual SRS.
At least we could imagine having a list of all such people, and some
means to contact those whom we select.  However it would generally
still be the case that some people may be difficult to reach, or may
refuse to participate in our study.

Now return to the research study described above, aiming to understand
the relationship between soil nutrients and crop yield.  It is not
clear what it would mean to obtain an SRS in this setting.  For such
situations, it is common to consider a different type of random sample
called an _independent and identically distributed sample_, or _IID_
sample.  An IID sample is defined in a slightly more abstract way than
an SRS.  An IID sample, like a SRS, is formally defined using
probability, so we will visit this topic again later when we have
developed some probability tools.  But intuitively, in an IID sample,
each element of the (possibly infinite) population is equally likely
to be selected, and selection of one element into the sample does not
change the likelihood of selecting any other element.  An IID sample
can be thought of as _sampling with replacement_ from a possibly
infinite target population.

It might be helpful to describe some ways of collecting data that
generally will not produce an IID sample.  We describe two such
examples below.

Suppose we place ads on a social media platform like Facebook,
inviting subjects to participate in a study.  Suppose further that
there is a 50 USD payment for participating, and that the ad is
shareable with your Facebook friends.  This may be a good way to
quickly recruit a lot of participants, but it is quite unlikely to
produce an IID sample of the US population.  Some people in the US do
not have a Facebook account, or do not actively use the platform.
These people will not be reached.  If Facebook users and non-users
differ in ways that are relevant for the research aims, this will
render the sample non-IID for the overall US population.  Also, the 50
USD incentive may motivate some types of people to respond more than
others, and in general the type of person who will respond to such an
offer is different from the type of person who will not.  Finally,
allowing the offer to be shareable means that the first few people who
respond to the offer may share the ad within their network of friends,
so the remaining subjects will tend to resemble thee initial
responders.  This violates the requirement in an iid sample that the
inclusion of one individual in the sample must not impact the
likelihood that anyone else is included in the sample.

As a second example of a non-iid sample, suppose we observe daily
rainfall amounts at 50 locations in Texas, for every day during May of
2019.  For several reasons, it is not clear what the population should
be here.  First, note that there will only ever be one May of 2019,
and that is the sample.  To construct a population that this sample
may generalize to, imagine that we are actually interested in rainfall
throughout Texas, but we only have the ability to collect data at 50
locations.  Also, suppose that we are actually interested in the
rainfall in Texas in May of any year, not only in May of 2019.
Specifically, suppose that our idealized population involves choosing
a random location in Texas, and a random day within May from the past
100 years, and obtaining the rainfall on the given day and at the
given location.  Does our sample, consisting of 50 arbitrarily chosen
locations that are then observed for every day in May of 2019
represent this target population in an iid manner?  Almost certainly
it does not.  First, May of 2019 may have been an unusually wet or dry
year compared to other years in the population.  Second, some of the
locations where we collected data may have been so close together that
if it is raining in one location it is almost certain to be raining in
the other (this is sometimes called "twinning").  If we have strong or
perfect twinning, only one meaningful unit of information is provided
by the two twinned locations.
