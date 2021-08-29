% Types of data
% Kerby Shedden
% September 6, 2020

_Data_ can take many forms, such as free-form text, images, audio recordings,
and networks of relationships.

For most of this class, we will focus on a conventional form of data in which we have
a collection of _cases_ (_observations_), and we measure multiple _characteristics_
of each case.  The characteristics may also be called _attributes_, or _variables_.

Such data may be said to have a _rectangular form_.  By convention, the rows
of the rectangle correspond to the cases and the columns correspond to the variables.

---

For example, the first few rows of a dataset describing patient visits to a hospital
emergency department (ED) may look like this:


| ID     | DOB       | Cause            | Date      | Time    | Duration | Outcome    |
| :--    | :--       |  :--             | :--       | :--     | :--      | :--        |
| 195852 | 1961-3-12 |  Diff. breathing | 2020-8-3  | 8:34    | 93       | Discharged |
| 723401 | 1947-9-23 |  Bleeding        | 2020-6-2  | 14:12   | 211      | Admitted   |
| 914323 | 1982-6-11 |  Fever           | 2019-11-1 | 23:52   | 57       | Discharged |
| 643549 | 1939-12-2 |  Back pain       | 2020-5-2  | 10:13   | 113      | Discharged |
| 723401 | 1947-9-23 |  Bleeding        | 2020-7-5  | 9:23    | 189      | Discharged |

(an actual dataset of this type may have hundreds of variables and millions of cases)

_Notes_: "ID" is a patient identifier,
"DOB" is the patient's date of birth, "Duration" refers to the duration of time
in minutes spent in the ED, "Outcome" refers
to whether the patient was admitted to an inpatient facility following the ED visit.

---

An important concept in statistics is that of the _unit of analysis_ -- what
objects are
we studying?

In the ED visit example, one reasonable choice for the unit of analysis is
"person visit" (a unique occasion on which a person visits the ED).
The sample size is 5 for this choice of the unit of analysis.

Sometimes, the unit of analysis depends on our perspective or goals.  People
may visit the ED multiple times (e.g. ID 723401 visits twice).  If we were focusing
on people, rather than distinct ED visits, then our unit
of analysis might be "person" rather than "person visit".  Person 723401 has
two visits, and the other three people have one visit each.  The sample
size is 4 for this choice of the unit of analysis, since we only count
each person once.

In some datasets, there is no meaningful unit of analysis.  For example,
if we have a _time series_ containing the daily maximum temperature in Ann Arbor
over a period of 10 years, the term "unit of analysis" is not that helpful.

---

A characteristic of most datasets is that each variable has a _type_.
For example, in the ED dataset, "DOB" is a date, "Cause" is a string
of text, and "Duration" is a number.

Within a variable (a column), all values have the same type.

Within a case (a row), the values generally have different types
as we move across the variables.

In fact, there are at least two different "variable types" of interest to us:

From a software point of view, the __storage type__ of a variable
corresponds to how the values are stored in the computer's memory.
Storage types include dates, _strings_ (text), and numbers (floating point,
integer), among others.

The __statistical type__ of a variable describes the form of information
represented by a variable, rather than how it is stored on a computer.  The
most common statistical types of variables are
_nominal_, _ordinal_, and _quantitative_.

---

A __nominal variable__ is an unordered set of labels.  Here are some examples
of nominal variables:

* Country of birth

* Religious affiliation

* The type of cancer that a cancer patient has

* The preferred brand of a customer (e.g. of toothpaste)

---

An __ordinal variable__ is an ordered set of labels, with no implication
that we can attribute meaning to the size of "gaps" between the labels.  Here
are some examples of ordinal variables:

* Labor force status, coded as: unemployed not looking for work; unemployed looking
for work; employed part-time not looking for full time work; employed part
time looking for full time work; employed full time.  Note that these labels
are ordered, because each label implies more actual or desired labor force participation
than the label before it.

* Attitude regarding an issue, e.g. given the statement "religious organizations have
too much influence in politics" people may respond: "strongly disagree", "disagree",
"neither agree nor disagree", "agree", "strongly agree".  These labels are ordered
based on the intensity of agreement with the statement.

---

A __quantitative variable__ measures something in numeric terms to high precision,
often capturing an amount or the change in an amount.

Quantitative variables usually have _measurement units_ like "years" or "kilograms".

Some examples of quantitative variables are:

* Age (e.g. of a person), measured typically in years

* Income, measured in currency, e.g. US dollars (USD)

* Body mass index (BMI), measured in kg/m^2

---

In theory, physical quantities have arbitrarily-high precision, which means that
they vary _continuously_.  In practice we can
usually only measure something in the real world to finite precision.  For example,
our measure of mass may only be accurate to 1 gram (0.001 kilogram).

For this reason, real-world quantitative variables are _discrete_.  This gives them
something in common with ordinal variables, which are also discrete.

However quantitative variables, unlike ordinal variables, have measurement units,
and the "gaps" between quantitative values have meaning.

More formally, quantitative variables generally have an __interval scale__, meaning
that it makes sense to subtract two values, and the resulting difference has
the same measurement units as the values being differenced.

For example, if two subjects have BMI equal to 24 and 28, then it makes sense to
say that the second subject has 4 kg/m^2 greater BMI than the first.

Almost all quantitative variables have in interval scale.

---

A quantitative variable has a __ratio scale__ if it makes sense to compare values
using division.  Some quantitative variables have a ratio scale, but some do not.

When comparing values using a ratio, the result is _dimensionless_, or _dimension free_.
When forming a ratio, the units "cancel out".

If one person is 40 years old, and another person is 20 years old, then the first
person is twice as old as the second person.  We get the same ratio of 2 if we represent
age in days, years, months, or years.

Age is an example of a ratio scale, and as
with all ratio scales, the results of forming ratios
do not depend on the units in which the variables
being compared are measured.

---

On the other hand, let's consider temperature.
Suppose that on a particular autumn day, the temperature is 35F in Detroit and
70F in Miami.  If temperature is a ratio scale, then we could say that
it is twice as warm in Miami as it is in Detroit.  But does this make sense?

If we convert the temperatures to centigrade, then 35F becomes 1.7C, and 70F becomes
21.1C.  So in Centigrade, the ratio is over 12.

So is Miami twice as warm as detroit, or twelve times warmer than Detroit?

Or does this concept not make sense for temperatures?

Temperature is not a ratio scale, because different temperature scales have
different origins.  The origin point for Centigrade is the freezing point of
water, the origin point for Fahrenheit is not.

---

The terms discussed here such as ordinal, quantitative, interval, and ratio, are
useful ways to communicate about different types of measurements.

Sometimes we encounter corner-cases where these terms are ambiguous.  Rather than getting
involved in a debate about such situations, it is better just to not use
the terms when their meaning and implications are not clear.