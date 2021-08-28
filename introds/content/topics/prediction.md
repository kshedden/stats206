Prediction and regression
=========================

Statistics is sometimes said to have "two cultures" -- one that focuses
on modeling and understanding mechanisms and causes, and one that focuses
on prediction.  Here are two examples that fall at the opposite ends of this
spectrum.

* Suppose we are interested in whether improving highway illumination reduces
traffic accidents.  We may proceed by conducting an experiment in which 100
road segments are identified.  Then, 50 of them are fitted with new bright
lights, and the other 50 are not.  For two years, accident data are collected,
and at the end of this period we assess whether fewer accidents occurred on the
road segments that were fitted with bright lights.  This is an experiment
in which the goal is to establish whether improved highway lighting reduces
accidents.  There is essentially no role for prediction here.  This study is entirely
aimed at estimating whether improved lighting is helpful in preventing accidents.

* Suppose we are interested in identifying drivers who are at high risk
of being involved in a traffic accident.  We recruit 2000 drivers, and
each of them agrees to have a device installed in their car that measures
characteristics of their driving (speed, acceleration, braking and turning behavior, etc.).  We
then develop a model that predicts a person's risk of being in an accident
in terms of these features.  This is primarily a prediction-focused
study in which the goal is to assess each individual driver's risk of
being in an accident.  There may be a mechanistic aspect of this
study as well, because we may find that some features (e.g. rapid acceleration)
are more predictive of accidents than others (e.g. average speed).  However
attributing risk to specific features is not a primary goal of this project.

In recent years, the era of big data and big computing has led to prediction
taking on a very prominent role in the broader society.  Tools that you likely use every day like
Google search and Amazon make extensive use of prediction algorithms.  The goal of
a Google search is to predict what information or web resource you want to
view, based on the query that you have entered.  One goal for Amazon is
to identify what products you might want to buy, based on your past purchases
and searches. Some other prominent examples of prediction are:

* Facial recognition -- predicting what individual is depicted in an image

* Object detection -- recognizing specific objects in an image or video (e.g.
detecting pedestrians in a video taken from a camera mounted on a vehicle)

* Speech recognition -- predicting what words were spoken based on a recording of speech

* Translation -- predicting what expression in a target language is equivalent to an expression
in a source language

* Handwriting recognition -- predicting what letters were written based on an
image of someone's handwriting

* Sentiment analysis -- predicting based on a short segment of text (e.g. a text
message, tweet, email, memo) whether a person is conveying a positive, neutral, or negative "affect"

In a typical prediction task, there is one value called the _outcome_ or _response_
that we aim to predict, and one or more (often many) _features_ that we
use for making the prediction.  For example, in predicting traffic accident
risk, the outcome might be whether a given driver has an accident within a one-year
period, and the features might be the average number of miles driven per day, the average speed per trip,
the average maximum acceleration per trip, and the average speed at which brakes are applied.

The standard notation in this setting is that {{<katex>}}y{{</katex>}} denotes the
outcome and {{<katex>}}x{{</katex>}} denotes the features.  Here
{{<katex>}}y{{</katex>}} is a scalar (a single value) and {{<katex>}}x{{</katex>}}
is a vector, containing the values for all of the features.  In the most conventional
setting for prediction, we have a training set consisting of pairs
{{<katex>}}(y_i, x_i){{</katex>}}, where {{<katex>}}i=1, \ldots, n{{</katex>}}
indexes observations.  The key point is that in the training set, we observe both
{{<katex>}}y{{</katex>}} and {{<katex>}}x{{</katex>}}.  Then we are given
a feature vector {{<katex>}}x{{</katex>}} but are not shown its corresponding
outcome {{<katex>}}y{{</katex>}}, and the goal is to predict {{<katex>}}y{{</katex>}}
from {{<katex>}}x{{</katex>}}.
The prediction can be denoted {{<katex>}}\hat{y}{{</katex>}}, or
{{<katex>}}\hat{y}(x){{</katex>}}, with the latter notation emphasizing that the
prediction is based on the features.

Nearest neighbor prediction
---------------------------

Most predictive models utilize information from many features to form the prediction.
The key challenge is how to combine the information in the features in the most
effective way.
A very simple prediction algorithm is called _nearest neighbor prediction_ (NN).  In
NN prediction, we define a distance function on the features, and set
{{<katex>}}\hat{y}(x){{</katex>}} to be the training value {{<katex>}}y_i{{</katex>}}
whose {{<katex>}}x_i{{</katex>}} is closest to {{<katex>}}x{{</katex>}}.
As a very simple example, suppose we are predicting whether a driver has an accident,
and we have only two features, {{<katex>}}x[1]{{</katex>}} is the average number of miles
driven per day, and {{<katex>}}x[2]{{</katex>}} is the average speed at which the person drives.
Our training data are as follows:

| y   |  x[1]  | x[2] |
| --: |  --:   |  --: |
| 0   |  45    | 35   |
| 0   |  10    | 28   |
| 1   |  85    | 65   |
| 1   |  48    | 56   |
| 0   |  130   | 32   |

Now suppose that we are asked to make a prediction for someone who drives 77 miles
on average per day, and whose average speed is 61 miles per hour.  This individual
is called the _test driver_.  As a distance
function, we can use the _Euclidean distance_.  Recall that the Euclidean distance
between two vectors {{<katex>}}x{{</katex>}} and {{<katex>}}z{{</katex>}} is

{{<katex>}}
\sqrt{(x[1] - z[1])^2 + (x[2] - z[2])^2 + \cdots + (x[p] - z[p])^2)}
{{</katex>}}

Here, {{<katex>}}p{{</katex>}} is the number of features.  We can now calculate the
distance from our test driver whose feature vector is {{<katex>}}(77, 61){{</katex>}} to
each member of the training set:

| y   |  x[1]  | x[2] | d    |
| --: |  --:   |  --: | --:  |
| 0   |  45    | 35   | 41.2 |
| 1   |  10    | 28   | 74.7 |
| 1   |  85    | 65   | 8.9  |
| 0   |  48    | 56   | 29.4 |
| 0   |  130   | 32   | 60.4 |

The nearest neighbor to our test driver is the third driver in the training set.  Since
the third driver in the training set had an accident, we predict that our driver
will also have an accident.

A slightly more elaborate version of NN prediction is _k-nearest neighbor_ prediction (kNN),
in which we take the _k_ closest members of the training set (not only the closest
member of the training set), and average their outcomes to form a prediction.  For
example, of {{<katex>}}k=2{{</katex>}}, then we take the two closest members of the
training set and average their outcomes to form a prediction.  In the example above,
the two closest members of the training set to our test driver are the third and fourth
members.  The average of their outcomes is 1/2.  Thus, we would predict that our
test driver has a 50% chance of having an accident using 2-NN prediction.

A natural question for using kNN is what value of {{<katex>}}k{{</katex>}} to use.
This is an important practical question and has received a great deal of attention.
There are good methods for selecting {{<katex>}}k{{</katex>}} semi-automatically,
but we will not discuss them here.  In many cases, {{<katex>}}k{{</katex>}} can
be specied by trial and error.

Bias/variance tradeoff
----------------------

The specification of {{<katex>}}k{{</katex>}} exemplifies a very important principle
in statistics, namely that of the _bias/variance tradeoff_.  If we choose a small
value of {{<katex>}}k{{</katex>}}, then the prediction is made using only the closest
neighbors.  In the example above, if we choose {{<katex>}}k=1{{</katex>}}, we are
able to find a match that is only 8 miles different in terms of average miles
driven per day, and only 4 miles per hour different in terms of average speed.
Thus, the third element of the training set is a very good match to our driver.
This means that there is very low bias in using that training driver to predict
the behavior of our test driver.  In general, choosing smaller values of {{<katex>}}k{{</katex>}}
entails less bias.

On the other hand, using a small value of {{<katex>}}k{{</katex>}} means that we are
averaging very few outcomes from the training set to form our prediction.  An average
of a small set can be quite variable.  For example, using {{<katex>}}k=1{{</katex>}}
entails no averaging at all.  The fact that the third driver in the training set
had an accident does not mean that all people who drive like that person will
always have an accident.  As a result, using a small value of {{<katex>}}k{{</katex>}}
leads to greater variance in the prediction.

Both bias and variance are bad, but as we have seen, having a smaller bias necessitates
having a larger variance, and having a larger variance necessitates having a smaller
bias.  This is the bias/variance tradeoff.  The goal when selecting the value of
{{<katex>}}k{{</katex>}} for a k-NN prediction is to balance these two quantities.

Curse of dimensionality
-----------------------

The basic idea of nearest neighbor prediction is to identify approximate
matches between the test unit's feature vector and the feature vectors
in the training set.  The ability to find matches is limited by the size
of the training set, and by the number of features.  For a fixed training
set sample size, it becomes harder to find matches as the number of
features grows.  For example, if we are matching people on demographic
characteristics, it may be relatively easy to find someone with your
same sex and (similar) age, but it gets harder as we also aim to
approximately match your height, weight, income, state of residence, and so on.

This phenomenon is called thje _curse of dimensionality_, with "dimension"
here referring to the dimension of the feature space, i.e. the number of
features.
In principle, if we have enough training samples, we can find approximate matches
even in quite high dimensional feature spaces.  However, the volume of space grows
very rapidly as the dimension increases, and it is practically impossible to find close
matches with more than say 10 features.  This limits the applicability of the
kNN approaches discussed here, but fortunately there are many other approaches
to prediction modeling that can circumvent the curse of dimensionality, at least
in specific settings.

Regression modeling
-------------------

Regression analysis is the term used to refer to a broad class of statistical methods
that can be used to understand how one or more variables (deemed "features", or _covariates_)
relate to an outcome.  Most commonly, regression analysis aims to estimate the conditional
mean of the outcome, given the features.  As we have seen before, this conditional mean
can be denoted {{<katex>}}E[y | x[1], \ldots, x[p]]{{</katex>}}.  The conceptual meaning of this
quantity is that we take the average {{<katex>}}y{{</katex>}} for all possible
observations that have exactly the given value of {{<katex>}}x{{</katex>}} as their
covariates or features.  This conditional mean is a property of the population, since
we would never have access to all possible observations with a given value of
{{<katex>}}x{{</katex>}}.  In fact, our data set may contain only one observation with
any particular value of {{<katex>}}x{{</katex>}}.

Regression analysis is one of the major branches of statistics.  While it is extremely
well developed, new regression methods are being invented every year.  The kNN approach
discussed above can be viewed as a regression method, as it has exactly the same goal,
namely, to estimate the conditional mean function (and then use it for prediction).

Perhaps the most well-known regression methods are called _linear models_ and _generalized linear models_.
Which are fit using _least squares_ (or an iterative version of least squares).  These topics
are not covered in this class, but you can get a sense of what they do based on our
discussion of kNN.  Also note that earlier in the course we discussed scatterplot smoothing
using LOWESS.  The underlying algorithm for LOWESS is very similar to kNN, with the caveat
the the standard LOWESS algorithm can only be used with one covariate.