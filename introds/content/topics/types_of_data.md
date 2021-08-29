Types of data
=============

In empirical research, we collect and interpret data in order to
answer questions about the world.  "Data" in this context usually
results from some form of "measurement".  The notion of measurement
here is very broad -- it could include familiar acts like using a
ruler to measure the length of an object, but it could also include
asking a human research subject a question to "measure" their attitude
about some topic.

Depending on the type of measurement that is made, the resulting data
value can take different forms. Here we will discuss some of the
common forms that can be taken by data.

Nominal data
------------

A _nominal_ measurement is one that can take on any element in a
finite set of unordered values.  A commonly encountered nominal
measurement that arises in research involving human subjects is
biological race.  There are many ways of "coding" race, but all of the
common ways to do this would be considered to have a nominal form.
The current United States Census Bureau approach to coding race uses
five categories: Asian American, Black or African American, Native
Americans and Alaska Native, Native Hawaiian and Other Pacific
Islander, and White American.  In some settings, subjects are given
the option to respond that they have two or more races, and may be
given the option to not respond.  Since these race categories have no
meaningful ordering, this is a nominal variable.  Nominal
variables are sometimes called _categorical_, or _factor-type_
variables.

Nominal variables often arise in research involving human subjects,
where common nominal variables include race, national origin (country
of birth), biological sex, marital status, and
immigration status.  These may be broadly termed _demographic traits_.

Nominal variables arise in many other settings as well:

* In medicine,
we may be studying people with cancer, and there are many forms of
cancer; for example, cancer can be classified based on the affected
organ (lung, ovary, brain, etc.).

* In market research, people have
brand preferences, e.g. for toothpaste.

* In astronomy, there are
different types of stars (brown dwarf, red dwarf, neutron, etc.).

Many nominal variables are _binary_, meaning that they can only take
on two possible values.  These arise, for example, when the variable
by definition refers to the presence of absence of some trait,
e.g. responses to questions such as "do you have health insurance", or
"are you married"?  These are sometimes called _dichotomous_ traits.
In some cases, the dichotomy is a simplification of a more complex
reality.  For example, we can ask someone whether they are currently
employed, which is a binary choice, or we can give them more
fine-grained options such as being employed full time, employed part
time, retired, etc.

Ordinal data
------------

An _ordinal_ variable is one that takes on values that can be ordered,
but are not quantifiable to arbitrarily high precision.  A common
ordinal variable is educational attainment.  This variable is often
coded as (1) did not complete high school, (2) graduated from high school,
(3) completed some college, (4) graduated from college, (5) completed some
advanced or professional training beyond college.  Note that in this setting, a
person belongs to the highest level that is applicable, so that a
person who completed college is in group (4) even though they also
have a high school degree.  Unlike a nominal variable, which cannot be
ordered, there is a meaningful ordering for variables such as
educational attainment.

Another common example of an ordinal variable would be a rating scale
-- suppose for example that patients with an injury are asked to rate
their pain on a scale from 1 (least pain) to 10 (greatest pain).  A
very famous form of ordinal value is the five-point "Likert scale"
used in questionnaires: the respondent is given a statement about a
topic and can respond whether they "strongly agree", "somewhat agree",
"neither agree nor disagree", "somewhat disagree", or "strongly
disagree" with the statement.

A key property of an ordinal value is that the increments between
adjacent categories cannot always be taken to have equal magnitudes.
For example, we do not know whether the difference between "neither
agree nor disagree" and "somewhat disagree" is equivalent to the
difference between "somewhat disagree" and "strongly disagree", even though
these are both pairs of adjacent categories.

Quantitative data
-----------------

A "quantitative" measurement is one that can be made to very high
accuracy on a numerical scale.  Physical measurements such as length
and weight are usually quantitative.  A quantitative variable will
usually have "units" associated with it, for example when measuring
length the units may be centimeters.  Income and age are two other
measurements that would generally be considered to be quantitative,
with units potentially being dollars and years, respectively.

Quantitative data are generally seen as containing more information
than ordinal data, partly because they are generally measured to high
precision, and also because unlike ordinal data, the presence of
measurement units give a precise meaning to differences along the
measurement scale.  The difference between 5cm and 4cm, and the
difference between 7cm and 6cm are both 1cm.  On the other hand, as
noted above, on a 10 point ordinal scale the difference between 5 and
4 may not convey the same meaning as the difference between 7 and 6,
even though they are both one point differences.

### Interval and ratio scales

Sometimes, people refer to quantitative data as having an _interval
scale_, and/or a _ratio scale_.  An interval scale is one in which it
makes sense to subtract two values, and a ratio scale is one in which
it makes sense to divide two values.  Most quantitative data have an
interval scale, but it is not always the case that the scale of a
quantitative variable is a ratio scale.

For example, suppose we are measuring temperature in degrees
Fahrenheit, and we observe on a particular day that Cleveland and
Atlanta reach high temperatures of 25 and 50 degrees, respectively.
As an interval scale, it makes sense to subtract the two measurements
and state that the Atlanta is 25 degrees warmer than the Cleveland.
However it generally does not make sense to state that Atlanta is
twice as warm as Cleveland based on Fahrenheit measurements.  The
origin (0 degree point) for Fahrenheit temperature is 32 degrees below
the freezing point of water, which is a somewhat arbitrary value.  To
state that "Atlanta is twice as warm as Cleveland" would mean that
Atlanta is twice as far from 0F compared to Cleveland, which is
technically true but arguably not very meaningful.  If we were to
work on the centigrade scale, and we observe on a given day that
the temperature in Atlanta is 20 degrees centigrade, and the temperature
in Cleveland is 10
degrees centigrade, then we can make a stronger case for the scale
having a ratio interpretation, since 0C is the freezing point of water,
which has important real-world consequences.

Through this example, we can see that whether a scale is an interval
and/or a ratio scale is somewhat a matter of judgment.  The key thing to
keep in mind at this point is that some pairs of quantitative
variables can be compared through differences, some through ratios,
and sometimes both type of comparisons make sense.

Practical considerations
------------------------

The typology described above is often useful, but in practice we
encounter cases where it is ambiguous what type of data we
have.  We give examples of such ambiguous cases below.  The key
thing to keep in mind is that these terms are meant to help us
communicate about our data.  In some settings, terms such
as "ordinal" or "ratio" may have unclear meanings.  In that case, simply
don't use them in that setting.

For example, we might represent a person's employment status with five
levels: (i) employed full-time, (ii) employed part time, looking for
full-time work, (iii) employed part time, not looking for full-time
work, (iv) not employed, looking for work, (v) not employed, not
looking for work.  These could be treated as nominal, but
alternatively, we could view this as an ordered spectrum in which (i)
represents the greatest participation (desired or achieved) in the
workforce, and (v) represents the least participation in the
workforce.  Thus, this variable could be viewed as either ordinal or
nominal.

Considering educational attainment, we could code this variable as the
number of years of schooling a person has completed.  This could be
taken to be quantitative, with units of years.  However, it could also
be considered to be ordinal. One reason to consider it as ordinal
would be that it is much less common to have a partial year of
schooling than to have a full year of schooling, and a person who
completes, say, 11.5 years of schooling does not necessarily gain half
of the benefit of their incomplete 12th year of schooling compared to
someone with 12 full years of schooling.  In other words, this scale is
primarily discrete with whole-year increments, rather than being
continuous with arbitrarily-fine increments.

Yet another type of ambiguity arises when we consider quantitative
data.  This type of data arises from measurements that are made at
high precision, and are treated as real numbers.  However, in practice
every quantitative measurement has limited, finite precision due to
the limitations of our measurement systems.  For example, a digital
scale may read out only to 1/100 of a gram.  In some cases, a
"quantitative" measurement made with very low precision might best be
treated as ordinal.

When we consider the impact or consequences of changes in a
variable's value, we see that just because a variable is quantitative
does not mean that every increment on its scale has the same
consequences.  For example, comparing temperatures of 33C to 30C, and
43C to 40C both result in a 3C difference of temperature.  However, it
may be argued that we care about a variable such as temperature only
to the extent that it relates to something else that directly impacts
us.  For example, the "heat index" aims to reflect the comfort or discomfort that humans
feel in environments with different temperatures.  It takes account of the
fact that a one degree
change in temperature in a low humidity setting gives a lower
perceived increase in heat than a one degree change in temperature in
a high humidity setting.  Thus, with respect to heat as perceived
through the heat index, the temperature scale may not be an interval
scale after all, since a fixed difference, say of 3 degrees C, does
not always have the same impact on our preception of temperature.

Another useful example is the relationship between wealth and health.
Wealth can be taken as a quantitative variable, defined to be the
financial resources of an individual or family.  In one sense, wealth
is certainly an interval and a ratio scale.  If one person has wealth
of $400K, and another person has wealth of $100K, then the first
person can buy $300K more stuff than the second person, suggesting that
wealth is an interval scale.  It is also true that the first person can buy four
times more stuff than the second person, suggesting that wealth is a
ratio scale.  However, if we are focusing on wealth as it relates to health, then the first
person may not tend to be any healthier than the second person.  Both
of these individuals have relatively high wealth compared to the
population as a whole.  It is well-established that both within and
between countries, wealthier people tend to be healthier and live
longer.  But this effect is largely seen when contrasting the poorest
individuals to individuals who are closer to the median, rather than
contrasting wealthy to very wealthy individuals.

In summary, keep in mind that the purpose of the terms discussed here
is to help us communicate, and we should not worry too much about the
ambiguous cases.  Instead, use these terms when it makes sense to do
so, and avoid them in cases where it is not helpful.
