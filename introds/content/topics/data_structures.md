Data structures and data manipulation
=====================================

Many (but by no means all) datasets can be logically viewed as a
collection of _variables_ measured on a collection of _cases_.  For
example, if we ask 100 people to tell us their age and country of
birth, then we have two variables (age and country of birth) and 100
cases (the people).  Conventionally, raw data of this form are
represented as a rectangular table, with the cases as the rows and the
variables as the columns.  This structure has come to be known as a
_dataframe_.

A dataframe is a two-dimensional data structure, since it has both
rows and columns.  If we select the data for one variable (column) or
for one case (row), then we have a 1-dimensional data structure that
is called a _series_.  A series obtained as the column of a dataframe
is a dataframe in its own right, that just happens to contain a single
variable.

Variables in a dataframe have "data types".  As we have discussed
previously, variables can be ordinal, nominal, or quantitative.  There
are some other data types as well, including _timestamp_ variables
that represent an instant in time, and _geopoint_ variables that
measure a location in space.  Timestamp variables are a special type
of quantitative variable, but are often treated distinctly since
special software tools are used to manipulate them.  Geopoint
variables generally contain two quantitative values, corresponding to
longitude and latitude, or other spatial coordinates for a specific
location.

Modern software for data analysis, including R, Python, and Julia,
among many other packages, all have their own syntax for manipulating
dataframes.  But the same basic capabilities and concepts are present
in each case.  Here, we will describe how dataframes are manipulated
in modern statistical software, using _pseudo-code_ instead of the
actual syntax of any one environment.

Accessing values
----------------

The most basic way to access values in a dataframe is by position.
For example, if we want the data value for the 5th case and the 3rd
variable in a dataframe, we might access this values by subscripting
the dataframe at `[5, 3]`.  We note here that some computing languages
(like Python) are zero-based, meaning that positions start at zero.
In that case, `[4, 2]` would give the data for the 5th case and 3rd
variable.

Modern software for data analysis supports _labeling_ of dataframe
rows and columns.  This means that the rows and columns have text or
numeric labels, and we can access the data through these labels.  For
example, the variables of a dataframe may have labels such as "age"
and "country" (for "country of birth"), and if our subjects have ID
numbers, these might be the row labels.  We can thus access the age
for a person with ID 312389 using a subscript syntax like `[312389,
"age"]`.  Even though 312389 is a number, this does not mean that the
data for that individual is stored in row 312389 of the dataframe.
When you access values by label, the computer will determine the
position where this value is actually stored and return the
appropriate value.

There are many advantages to using labels where possible.  For
example, if we manipulate a dataframe, say by removing rows or
columns, or by sorting the rows and/or columns, then the positions of
the values will change.  The row and column labels will always refer
to the correct values, so the subscript `[312389, "age"]` will always
give us the age for person 312389, regardless of how the dataframe is
manipulated, as long as that value is not removed from the dataframe.

Modern software for data analysis also supports _indexing_, which
makes a dataframe behave more like a database. Indexing is a big
topic, and we will only introduce it here.  In an indexed dataframe,
there is a special row and a special column (called the _column index_
and the _row index_, respectively).  Accessing values by index is very
fast.  For example, if we want to find the age for the person with ID
312389, and if ID is not the row index, then the computer would have
to search through every row of the dataframe to find this record.  If
the dataframe is indexed on the ID variable, this search is not
necessary.

After accessing individual elements, the next most common selection
operation on dataframes is _slicing_.  Slicing by position means that
we select a contiguous range of rows and/or columns.  Subscript syntax
for position-based slicing might be `[2:4, 5:7]`, In a one-based
language (e.g. R, Julia), this would select rows 2, 3, and 4, and
columns 5, 6, and 7.  The result is a 3 x 3 dataframe.  In a
zero-based language (e.g. Python), the final position in the slice is
omitted, so this would select rows 2 and 3 and columns 5 and 6, giving
us a 2 x 2 dataframe.  Note that rows 2 and 3 in a zero-based setting
are the 3rd and 4th rows in everyday language.

We can also slice by index.  For example, if we want to select the
rows for all ID's between 1000 and 2000, the subscript would be
`[1000:2000, :]`.  Note that we use a `:` here to indicate that we
want to keep all of the columns for these row IDs.

Long and wide form data
-----------------------

It is common that we want to organize data according to two or more
factors.  For example, we may have a clinical study in which the
levels of a biomarker, say c-reactive protein (CRP) is assessed three
times for each subject, say at weeks 3, 6, and 9 following recruitment
into the study.  This might yield the following data for two subjects
with IDs 25 and 41:

|  ID\Visit |    3   |   6    |   9   |
|     ---:  |   ---: |  ---:  |  ---: |
|   25      |  3     |   5    |   4   |
|   41      |  2     |   6    |   7   |

The above is called "wide-form" data, because the values of one factor
(time of CRP measurement) are spread across the columns of the
dataframe.  The same information can be placed into "long-form" as
follows:

| ID   | Week | CRP  |
| ---: | ---: | ---: |
|  25  |  3   |  3   |
|  25  |  6   |  5   |
|  25  |  9   |  4   |
|  41  |  3   |  2   |
|  41  |  6   |  6   |
|  41  |  9   |  7   |

One advantage of long-form data is that the time variable does not
have to take on the same values for every subject.  For example, we
could have the following data, which would be difficult to represent
in wide format.

| ID   | Week | CRP  |
| ---: | ---: | ---: |
|  25  |  3   |  8   |
|  25  |  6   |  1   |
|  25  |  9   |  2   |
|  41  |  2   |  4   |
|  41  |  5   |  2   |
|  41  |  10  |  3   |

Another advantage of long-form data is that we can include multiple
variables in the same dataframe.  For example, if we also measure
systolic blood pressure (SBP) for each subject, we would have

| ID   | Week | CRP  | SBP  |
| ---: | ---: | ---: | ---: |
|  25  |  3   |  8   | 141  |
|  25  |  6   |  1   | 135  |
|  25  |  9   |  2   | 131  |
|  41  |  2   |  4   | 128  |
|  41  |  5   |  2   | 119  |
|  41  |  10  |  3   | 122  |

The modern convention in data science is to use long format data
wherever possible when conducting data analyses.  If the data has a
natural two-way structure, it is fine to present the final results in
wide form.  But the internal calculations are generally done
exclusively with long-form data.

The process of converting data from wide to long form, or vice-versa,
is sometimes called _pivoting_, or _stacking_ (wide to long), and
_unstacking_ (long to wide).

Grouping and aggregating
------------------------

Many data analyses can be conceptualized as a process where we first
break the data into groups, then we apply some summarization to the
groups.  This paradigm is called _group by/aggregate_.  For example,
if we have blood pressure data on human subjects, and we want to know
the mean blood pressure by race and by age group (age less than 50
versus greater than or equal to 50), then we would group by race and
age group, and aggregate using the mean function.  A very small
illustration of this would be to take the following raw data

| Sex  | Age   | SBP  |
| --:  | --:   | --:  |
| F    | <50   | 131  |
| F    | <50   | 121  |
| M    | <50   | 125  |
| F    | >=50  | 121  |
| M    | >=50  | 146  |
| M    | >=50  | 142  |
| M    | >=50  | 150  |

Then we aggregate this to produce the following reduced table

| Sex  | Age   | SBP  |
| --:  | --:   | --:  |
| F    | <50   | 126  |
| M    | <50   | 125  |
| F    | >=50  | 121  |
| M    | >=50  | 146  |

It is also common that we want to "merge back" the summarized values
into our original data, like this:

| Sex  | Age   | SBP  | SBP_mean |
| --:  | --:   | --:  |   --:    |
| F    | <50   | 131  |   126    |
| F    | <50   | 121  |   126    |
| M    | <50   | 125  |   125    |
| F    | >=50  | 121  |   121    |
| M    | >=50  | 146  |   146    |
| M    | >=50  | 142  |   146    |
| M    | >=50  | 150  |   146    |

Note that since SBP_mean is the average blood pressure for one sex/age
group, it is constant across people sharing common values for these
variables.