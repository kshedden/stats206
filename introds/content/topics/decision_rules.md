Algorithms and data-driven decision rules
=========================================

Perhaps the most profound way that data science has impacted the
broader society over the last 10 years has been through the rapid
proliferation of data-driven decision rules in commerce, government,
and healthcare, to name just a few areas.  A data-driven decision rule
is a way to make a _prediction_ about something that is currently
unknown.  These decisions are _algorithmic_, meaning that they are
mostly automated and performed by computers using rules, and are also
_data-driven_, meaning that observations made in the real world form
the raw material that the algorithms act on.  Both the nature of the
data and the structure of the algorithm are important in determining
the performance characteristics of a decision rule.

Machine learning and expert systems
-----------------------------------

Algorithmic decision making has roots in the field of statistics, for example
in work on decision theory, prediction, and forecasting, and in
computer science, especially in the subfield of artificial
intelligence.  A wave of interest in artificial intelligence among
computer scientists occurred during the 1980's.  But at that
time, there was much less interest in the use of data to drive the
decision-making process.  Researchers in that era largely felt that
the logic of human experts should be used as the basis for making
algorithmic predictions and decisions.  For example, it was thought that we could interview
a physician and aim to "elicit" all of the signs and symptoms that she
or he uses to make a medical diagnosis, then codify that logic into an
algorithm.  Such efforts, however, were largely unsuccessful.

A new wave of interest in artificial intelligence began around the
year 2000, and coincided with much wider availability of sensors for
wide-scale data collection, much greater computing and data storage
capacity, and much more extensive networking between computers.  This
has also been a time when people began to spend a great deal of
their lives in the digital world, which greatly facilitates the
collection of data about human behavior.  The predominant theme of
this era has been to make algorithmic decisions using _machine
learning_, which broadly means that we use "learning algorithms" to
develop the algorithms that are in turn used to make decisions.  Thus,
we are using algorithms to write algorithms.  These learning
algorithms are "trained" on data.  Major advances in the early 2000's
indicated that with sufficient amounts of training data, machine
learning algorithms can create extremely complex and accurate
prediction rules that reach or even exceed the performance level of
human experts.

The prevailing wisdom at the present time is that the cognitive
processes that human experts use in making judgments are in general
too complex and subtle to be represented explicitly as pure logic.  Also,
humans seem to be inefficient and ineffective at codifying the logic
behind our own thinking.  For these reasons, data-driven machine learning is
currently the dominant paradigm for developing algorithms to make
decisions in complex real-world settings.

Applications of algorithmic decision making
-------------------------------------------

We will not get into the mechanics of how a data-driven prediction
rule are constructed here (we will touch on this topic later in the
course).  Instead, we will discuss at a high level some of the tasks for
which data-driven prediction rules have been deployed, and we will
discuss some of their positive and negative impacts.

It is well-known that data-driven algorithms can be used to make
predictions of the values stocks and other securities, or the outcomes
of sporting competitions or elections.  But there are many other areas where
data-driven decision rules are used.  These algorithms can have
profound impacts on people's lives, and for the most part, people are
quite unaware of how widely they have been deployed.

One example of a data-driven decision rule is a _recommender system_,
which is something that is widely deployed in commerce, especially
internet commerce.  When you visit a shopping site on the internet,
products that might interest you are displayed along with any products
that you explicitly search for.  These recommended products are
identified by algorithms, and may be related to your current or past
searches, or may be items that other people with your demographic
profile have recently purchased.  While aiming to match your
interests, recommendations may also be biased in favor of products
that the owners of the platform would especially like to sell, perhaps
because the return is higher, or to help with inventory management.
Thus, while a recommender algorithm may be providing the user with a
valuable service, the algorithm is also
working to further the retailer's interests.

Recommender systems are also used in less-tangible commercial
settings, for example, they may be deployed in a streaming media service to recommend content
that a user may wish to watch.  The key point remains that the
recommendations are automatic and data-driven, and they generally aim to maximize the
likelihood that a user will end up making a purchase, or spend more time on the platform.  These goals are
accomplished by pooling information about the user's past activity on
the platform, e.g. products viewed or searched for in the past, with
the same information for
other users of the platform.  At a high level, the goal is to make
recommendations that have successfuly engaged "people like you" in the past.

The major on-line platforms collect and retain tremendous amounts of
data about their user's behaviors, and sometimes obtain information
about off-line behavior that can be linked to data from on-line
behavior.  Given this huge amount of data, many people are surprised
at how accurately a platform can anticipate their interests.  This
of course provides a valuable service to the user, which is not a bad
thing.  But there are many concerns about the broader impacts of the
mass deployment of this type of technology.  It is clear that in many
cases, recommendation systems that cater to people's existing
interests can lead to increased levels of polarization in society as a
whole.  This is clearly evident in on-line news aggregators, which
tend to recommend more content from the same viewpoint that the user
already has, rather than challenging people with viewpoints that
diverge from their own.

Data-driven prediction algorithms are also used in the "back-end" of
many commercial operations.  A famous example of this would be the
"credit scores" that determine how easily a person can get a credit
card, what the interest terms are, and what maximum balance is
allowed.  If "people like you" have generally paid off their credit
card bills on time, then the
prediction algorithm will consider you to be a "good risk", and may
give you a high credit limit and lower interest rate.  On the other
hand, if people like you have frequently defaulted or been slow to pay off their
balance, you may be given a higher interest rate and a lower credit
limit.

Ethical aspects of algorithmic decision making
----------------------------------------------

There are many ethical challenges in developing predictio algorithms
that are intended for mass deployment.  It
is possible that algorithms in current use discriminate against
certain classes of people, for example based on sex or ethnicity.
Even when it is illegal to explicitly use characteristics such as sex
or race in the implementation of a decision rule, it is possible that
the rule may use other information that is related to sex and race,
and end up making offers in a discriminatory way.

An especially controversial application area for algorithmic decisions
is in the court system.  In recent years,
prediction algorithms
have been widely used in the American criminal justice system
to inform decisions related to sentencing, and
to set bail (the money that must be given to the court to ensure that
a defendant does not flee before their trial).  If an algorithm
predicts that a person will "skip bail" and not attend their trial, a
judge may order a very high level of bail.  At the sentencing stage
after a person is convicted of a crime, if an algorithm predicts that
a person is more likely to re-offend, a judge may decide to give that
person a longer sentence.  The systems used to make such predictions
are generally proprietary, and their inner workings are secret.
Although it may be true, as claimed, that they do not explicitly use
demographic information such as race, it is entirely possible that the
algorithm may recommend higher bail or harsher sentences for people of
one race over another, even if the subjects being sentenced are
identical in every measured way other than race.

Another area where data-driven measures of risk have been extensively
used is the insurance industry.  The very purpose of the insurance industry is to make predictions
about risk, and price policies accordingly.  In its most traditional
form, people whose house is more likely to be destroyed in a natural
disaster pay more for homeowner's insurance, people whose car is more
likely to be stolen pay more for automobile insurance, and people who
are more likely to get a disease pay more for health insurance.
However it has long been noted that the circumstances that lead to
higher risk concentrate among certain demographic groups and in
certain geographic areas.  The traditional approach to pricing
insurance policies may therefore reinforce and amplify existing
inequalities and social divisions.

There have long been regulations
on how insurance rates can be set, but increasingly
sophisticated algorithms and methods of data analysis, and changing
social attitudes about inequality, mean that this topic remains
heavily debated.  For example, having a pre-existing medical condition is one of the
best predictors of the future medical expenses that a person will
generate.  In some cases, insurers have been prohibited from
increasing the price of a policy to account for this increased risk,
and therefore simply choose not to sell a policy to such people.
Recently, there has been intense debate about whether this should be
allowed.

Concerns about the "fairness" of algorithms used in ways that have
deep impacts on people's lives is an important emerging area of
data science.  This is a subtle topic, and it is not even
straightforward to define exactly what it means for an algorithm to be
"fair".

While major ethical challenges remain, it is also important to note
that algorithmic decision making has a positive side.  One of
the areas where machine learning is being deployed is in the
assessment of medical conditions, including imaging diagnostics such
as CT scans, and pathological assessment, e.g. to diagnose cancer or
other diseases.  In the past, many hospitals, especially rural
hospitals, could generate such diagnostic images, but did not have an
expert pathologist available to evaluate them.  Also, it has long been
noted that even experienced experts may disagree on the interpretation
of such data.  A very experienced expert with decades of experience
has seen, at best, tens of thousands of images, and likely remembers
only a tiny fraction of that information.  A machine learning
algorithm can be trained on essentially unlimited collections of
images, easily reaching into the millions, and has essentially no limit
on its ability to store and recall features of the images.
Algorithmic decisions based on medical images are rapidly approaching
and even exceeding the performance of human experts in this area, and
have the potential to bring a higher standard of healthcare to underserved
populations, and may also help to manage healthcare costs.
