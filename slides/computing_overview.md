% Computing overview for Statistics 206

Python, tools, and libraries
----------------------------

* Python is a general-purpose programming language; to work with data
in Python usually involves utilizing additional libraries.

* In this course, the main libraries that we will use are Pandas 
(for data management), Numpy (for arrays and
mathematical calculations), and Seaborn/Matplotlib (for graphing).

* Jupyter provides an interface for working with Python in a web
browser.  It is one of several interfaces available for working with Python.
All computing work in this course will be done using Jupyter.

---

Cloud computing
---------------

* Greatlakes is a cluster of computing servers located in a data
  center near the University of Michigan campus.  Greatlakes has computational
  capacity and data storage that we utilize for data analysis.

* We connect to Greatlakes over the internet using a web browser. Code
  that you enter or modify in your Jupyter session is relayed to
  a Greatlakes server over the internet, then executed there.  The
  results of your code are then relayed back to your browser and
  displayed to you.

* Your computations are not running directly on your computer, and the
  data and software that you are working with are not stored or
  executed on your computer.  Thus, the capabilities of your computer
  are not relevant, as long as you have a modern web browser and stable
  internet connection.

---

Pandas (Python Data Analysis System)
------------------------------------

* Pandas is a large library that facilitates data manipulation in
  Python.

* We will make extensive use of Pandas in this course.  Most of the
  code that we use is best thought of as Pandas code, not Python
  code.

---

Datasets, CSV files, DataFrames
--------------------

* A CSV ("coma separated values") file is a text file that holds a
  rectangular dataset.  The CSV format is a means for storing and
  transmitting such data.  A CSV file lives on the disk and is not normally used directly for
  computation.

* A Pandas DataFrame is a “live” representation of a rectangular
  dataset in the computer’s memory.  A DataFrame has rows (cases) and
  columns (variables).  It can be manipulated and summarized, and is
  amenable to many forms of computation and analysis.

* CSV files and DataFrames are usually used for "rectangular data", which
  are indexed by rows and columns.  Many important datasets do not have
  a natural rectangular structure, but in this course we focus on datasets
  that are rectangular.

* In modern practice, more sophisticated file formats such as Apache Parquet
  are often used in place of CSV.  But in this introductory course, all of
  our data will be in CSV files.

---

DataFrame values, variables, and names
--------------------------------------

* In Python, a "variable" is a name like "x" that holds a "value".
  For example, if we use an assignment statement such as `x = 3`
  or `x = 'dog'`, then we are assigning the values '3' (a number)
  and 'dog' (a character string) to the variable named "x".

* DataFrames are values in a Python session, and like all values,
  are "bound" to variables.  If there is a meaningful short name for
  a dataframe, such as "income", then this would be a good choice for
  the dataframe's name.  Often we will use generic names such as
  'df' as dataframe variable names.

* A Python session may have multiple active dataframes in existence
  simultaneously.  These dataframes may have different sizes (rows
  and/or columns), and there is no presumption that the dataframes
  are "aligned" in that the rows of two dataframes correspond to
  the same cases, or that the columns of two dataframes correspond
  to the same variables.

---

Scalar and compound values
--------------------------

* A single numeric value, or a single string value, are both "scalar"
values.  The assignment statements `x = 3` and `x = "dog"`` both create
scalar values, and assign them to variables named x.

* A compound value is a "collection" or "container" that holds multiple
data values.  

* The most basic compound value is a "Python list".  We can construct
a literal list using an assignment statement like `x = [1, 3, 2]``.
A literal list is a list that we create by explicitly typing its
data values into our program code.

---

Functions in mathematics and in computing
-----------------------------------------

* In mathematics, a "function" is a rule that maps a value to another
  value, e.g. the function `x^2` maps the value 3 to the value 9.

* In computing, a function may either be a rule that maps a value to a new value,
  or an operation that transforms a value "in-place".

* For example, if the variable `x` holds the value 3, and the function `f`
  is the "squaring function", then calling "f(x)" returns the value 3,
  but the value of "x" is unchanged.

* We will often want to "assign" the result of a function
  call to a new variable, e.g. after executing the expression `y = f(x)`,
  the value of `y` will be 9 and the value of `x` will be 3.

---

Functions in mathematics and in computing
-----------------------------------------
* In computing, some functions "mutate" their arguments (these are
  sometimes called "impure" functions, or functions with "side effects").

* For example, suppose that `x` is the array `[1,2,3]`.  We may have
  a function `g` that performs "in-place squaring".  After executing
  `g(x)`, the value of `x` has changed to `[1,4,9]`.

* A function that modifies its argument in-place may or may not have a return value;
  if there is no return value then the statement `y = g(x)` yields an error, since
  there is nothing to assign to `y`.

---

Functions, methods, and attributes
--------------------------------------------

* Python has two different ways to invoke a function -- one approach
  is simply referred to as a "function" and the other uses a slightly
  different syntax and is referred to as a "method".

* A function call is expressed using the syntax `f(x)`, where `f` is a
  function, and `x` is the argument to which `f` is applied.

* A method call is expressed using the syntax `x.f()`, where `f` is
  a method applied to the value 'x'.

---

Functions, methods, and attributes
--------------------------------------------

* A method call is "syntactic sugar" for a function call -- there is nothing
  that you can do with one that cannot be done with the other.

* The method call `x.f()` is equivalent to the function call `f(x)`.

* Method calls can take arguments, and the method call `x.f(y, z)` is
  equivalent to the function call `f(x, y, z)`.

* In the libraries that we are using in this course, you sometimes will have the choice
  to invoke a procedure as either a function or as a method.  In other
  cases only one of the two is allowed.  Whether to use a function or
  a method is mostly an arbitrary decision made by the people who created
  the library.

---

Chaining
--------

* Pandas DataFrames are manipulated using both functions and methods.

* Methods and functions can be “chained”, but the syntax for chaining
  methods is especially succinct.

* Function chaining has the form `f(g(h(x)))`.  This is read "inside out" --
  first `h` is applied to `x`, then the result of this operation is passed to
  `g`, then the result of this operation is passed to `f`, and so on.

* Method chaining has the form `x.f().g().h()`.  This is read from left
  to right -- the method `f` is applied to the value `x`, then the value of this
  operation is passed to the method `g`, and so on.

* If additional arguments are used, a method chain will appear as, e.g.
  `x.f(1).g("a")` -- the method f is applied to the value `x`, along
  with the additional argument `1`, and then the method `g` is invoked on
  the result of this operation, passing the additional argument "a".

---

DataFrame methods and attributes
--------------------------------

Python dataframes also have "attributes" that are referred to in
infix form, e.g. `df.size` is the "size" attribute of the dataframe
named "df".  Note that this is not a function or a method, and hence
does not use parentheses -- use `df.size` not `df.size()`.

If df is a DataFrame, some basic things to do with it are:

* `df.shape` -- obtain the shape (number of rows and columns) of `df`

* `df.head()` -- display the first few rows of data in `df`

* `df.head(10)` -- display the first 10 rows of data in `df`

* `df.columns` -- obtain the variable (column) names of `df`

* `df.dtypes` -- display the variable names and corresponding types
  in the dataframe `df`.

---

Series
------

* In Pandas, a column of a DataFrame is called a Series.

* If `df` is a DataFrame, and “v” is the name of a column in `df`,
then `df[“v”]` returns a Series containing the data for that column.
Alternate syntax is `df.loc[:, “v”]`, or `df.v` (not recommended).

* Accessing a Series from a dataset is called "indexing" or "slicing".

* You can call methods on Series to manipulate or summarize them.  If
`x` is a series, then the following are some useful methods:

    * `x.sum()` -- sum the values in `x`

    * `x.max()` -- obtain the maximum value in `x`

    * `x.unique()` -- obtain the unique values in `x`

    * `x.sort()` -- sort the values in `x`

---

Constructing variables
----------------------

Variables can be added to a dataframe.

Often, this involves constructing a new variable that is derived from
variables that are already in the dataframe.  For example, `df["y"] =
2*df["x"]` creates a new variable called `y` whose values are twice
the values of the existing variable `x`.

If there is already a variable called `y` in the dataframe, then it
is overwritten with the new variable named `y`.

This is a "vectorized" operation -- the dataframe `df` may have many
rows, and the calculation `y = 2*x` is performed for every
row of the dataframe -- if `df` has 1000 rows, then 1000 calculations
are performed.

---

Frequency tables
----------------

If `x` is a series, we can obtain its frequency table using the
`value_counts` method, e.g. by calling `x.value_counts()`.

For example, if `x` contains the values [3, 1, 1, 5, 3], the result of
calling `value_counts` on `x` is

|     |     |
| :-- | :-- |
| 1   | 2   |
| 3   | 2   |
| 5   | 1   |

---

Statistical summaries
---------------------

If `x` is a series, you can obtain a set of common statistical
summaries for the data in `x` by calling `x.describe()`.

If you want a specific quantile for the data in `x`, say the 0.3
quantile (30th percentile), use `x.quantile(0.3)`.

Other useful statistical summaries are:

* `x.mean()` -- the mean (average) of the values in `x`

* `x.std()` -- the standard deviation of the values in `x`

* `x.var()` -- the variance of the values in `x`

---

Selecting
---------

Suppose we have this dataframe (`df`):

x   |  y  |  z
--: | --: | --:
1   | 2   | 9
2   | 3   | 2
2   | 4   | 2
1   | 1   | 8

If we wish to retain only the rows where `y` is less than or equal to
3, we can use `df.loc[df["y"] <= 3, :]`.  This gives us

x   |  y  |  z
--: | --: | --:
1   | 2   | 9
2   | 3   | 2
1   | 1   | 8

---

Selecting
---------

If we wish to retain only the rows where `y` is less than or equal to
3 and `z` is less than 9, we can use
`df.loc[(df["y"] <= 3) & (df["z"] < 9), :]`.  This gives us

x   |  y  |  z
--: | --: | --:
2   | 3   | 2
1   | 1   | 8

---

Slicing, indexing
-----------------

If we want to select an entire row or entire column by position, we
can use syntax like `df.iloc[3, :]` or `df.iloc[:, 3]`.  Note
that the method here is "iloc" not "loc" -- the "i" in "iloc"
refers to "index", meaning the numerical position from which the
value is taken.

Since we count from zero in Python, this selects the fourth row, or the fourth
column (when counting from one).

If we want to select a single value by position, we can use syntax
like `df.iloc[3, 5]` (to select the value in the fourth row and the
sixth column, counting from one).

We can select part of a column, e.g. `df.iloc[2:5, 7]` returns rows 2,
3, and 4 in column 7 (counting here from zero).

---

Slicing, indexing
-----------------

Dataframes always have column names, and may have row names
(technically called an "index").

|        | x   |  y  |  z
| --:    | --: | --: | --:
| __A__  | 1   | 2   | 9
| __B__  | 2   | 3   | 2
| __C__  | 1   | 1   | 8

We can select an entire column with `df["y"]`, an entire row with
`df.loc["B", :]`, and an individual value with `df.loc["A", "y"]`.

---

Counting
--------

If you want to count the number of times that something happens,
you can take advantage of the fact that Boolean values (True/False)
can be treated as numbers, with True being treated as 1 and False
being treated as 0.

Therefore, the code `(df["x"] >= 3).sum()` returns the number of
elements of column "x" of dataframe `df` that are greater than
or equal to 3.

Similarly, we may wish to know the proportion of elements of
a series (or array) that satisfy a given condition.  In this
case we can use the `mean` method.  For example,
`(df["x"] >= 3).mean()` returns the proportion of the elements
in column "x" of dataframe `dx` that are greater than or equal
to 3.

---

Groupby/aggregate
-----------------

A very powerful way to manipulate and summarize data is using a
"groupby/aggregation" workflow.  This is mainly used if you want to
stratify your data on one (nominal) variable, and summarize a
different quantitative variable within each stratum.

Suppose we have this dataframe, called `df`:

x   |  y  |  z
--: | --: | --:
1   | 2   | 9
2   | 3   | 2
2   | 4   | 2
1   | 1   | 8

---

Groupby/aggregate
-----------------

The following code will determine the maximum value of `y` within each
level of `x`.

`df.groupby("x")["y"].agg(np.max)`

This gives us

x   |     |
--: | --: |
1   |  2  |
2   |  4  |

An (almost) equivalent syntax is:

`df.groupby("x").agg({"y": np.max})`

The function `max` is written `np.max` because it is part of the numpy
library (to be discussed more later).

---

Groupby/aggregate
-----------------

If we want to calculate multiple summaries on the same variable, we
can use this approach:

`df.groupby("x").agg({"y": [np.min, np.max]})`

This will give us

x   | amin | amax
--: | --:  | --:
1   |  1   | 2
2   |  3   | 4

`amin` and `amax` are names chosen by Pandas for the minimum and
maximum values.

---

Groupby/aggregate
-----------------

If we want to calculate one or more summaries on each of several
variables, we can use this approach:

`df.groupby("x").agg({"y": [np.min, np.max], "z": np.sum})`

This will give us

|         | y        |          | z       |
| --:     | --:      | --:      | --:     |
| __x__   | __amin__ | __amax__ | __sum__ |
| 1       |  1       | 2        |  17     |
| 2       |  3       | 4        |   4     |

---

Groupby/aggregate
-----------------

Sometimes we can use a simplified syntax that does not require us to
name the variables we are summarizing.

* `df.groupby("x").size()` returns the number of rows corresponding to
each unique value of "x" (this is another way to get the frequency
table).

* `df.groupby("x").min()` returns the minimum value of every variable
in the dataframe (except `x`), calculated within each stratum defined
by `x`.

---

Groupby/aggregate
-----------------

We may wish to group by multiple variables simultaneously.  For
example, suppose we have

x   |  y  |  z
--: | --: | --:
1   | 2   | 9
2   | 1   | 2
2   | 2   | 2
1   | 1   | 8
1   | 1   | 3
2   | 2   | 5

---

Groupby/aggregate
-----------------

We can group by both `x` and `y` simultaneously, using
`df.groupby(["x", "y"])["z"].sum()`


| x   |  y  |     |
| --: | --: | --: |
| 1   |  1  | 11  |
|     |  2  |  9  |
| 2   |  1  |  2  |
|     |  2  |  7  |

---

Pivoting
--------

Sometimes it is easier to understand the results of a
groupby/aggregate with two grouping variables if we "pivot" the second
grouping variable to the columns, like this:

`df.groupby(["x", "y"])["z"].sum().unstack()`

|        |  y      |        |
| --:    | --:     | --:    |
| __x__  |  __1__  | __2__  |
| 1      |  11     | 9      |
| 2      |  2      |  7     |

---

Renaming and dropping variables
-------------------------------

If we have a dataframe `df` with a variable named "x", and we wish to
rename this variable to "y", we can use `df.rename(columns={"x":
"y"})`.

If we wish to drop one or more columns by name, we can use the `drop`
method, for example, `df.drop(["x", "y"], axis=1)` drops columns named
"x" and "y".

---

Missing values
--------------

In some cases, a value in a dataset may be missing or unknown.  In
Pandas, this is denoted `NaN`, for "not a number".  Suppose we have
the following dataframe denoted `df`:

x   |  y   |  z
--: | --:  | --:
1   | 2    | 9
2   | NaN  | 2
2   | 2    | 2
1   | 1    | 8
1   | NaN  | NaN
2   | 2    | 5

---

Missing values
--------------

Calling the method `dropna` will drop all rows with missing values, so
that `df.dropna()` yields

x   |  y   |  z
--: | --:  | --:
1   | 2    | 9
2   | 2    | 2
1   | 1    | 8
2   | 2    | 5

---

Missing values
--------------

If we want to know how many rows within each column are missing, we
can use `pd.isnull(df).sum()`, which in this case would yield:

|     |     |
| :-- | --: |
| x   | 0   |
| y   | 2   |
| z   | 1   |

---

Merging
-------

Suppose we have two dataframes named `df1` and `df2`:

| df1=  | a   |  y   |  z  | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | df2= | b    |  u  |  v
| --:   | --: | --:  | --: | --:  | --:  | --:  | --: | --:
|       | 1   | 2    | 9   |      |      | 3    | 2   | 9
|       | 2   | 2    | 2   |      |      | 4    | 2   | 2
|       | 3   | 1    | 8   |      |      | 5    | 1   | 8
|       | 4   | 2    | 5   |      |      | 6    | 2   | 5

---

Merging
-------

We can merge (join) two dataframes using syntax like `pd.merge(df1,
df2, left_on="a", right_on="b")`, which produces the merged dataframe:

|     |  y   |  z  |  u  |  v
| --: | --:  | --: | --: | --:
| 1   | 2    | 9   | NaN | NaN
| 2   | 2    | 2   | NaN | NaN
| 3   | 1    | 8   | 2   | 9
| 4   | 2    | 5   | 2   | 2
| 5   | NaN  | NaN | 1   | 8
| 6   | NaN  | NaN | 2   | 5

---

Dates and times
---------------

Pandas has a way to represent dates and times in a way that is very
efficient for computation.

When reading dates from a file, they may initially be read as strings
(text), e.g. "2012-9-7" is a string and cannot be directly manipulated
as a date.

Pandas has a function called `pd.to_datetime` that converts dates
and/or times in string form to "datetime" values.

Subtracting two datetime variables produces a "timedelta" variable
that represents a duration of time.

For example, if we have variables named "start" and "end" that contain
the beginning and ending times of some event, then the following code
calculates the duration of this event:

`df["end"] - df["start"]`

---

Dates and times
---------------

The `dt` "accessor" gives us access to special information that only
makes sense for dates, times, and durations.

If `df["start"]` is a datetime, then
`df["start"].dt.isocalendar().year`, `df["start"].dt.month`,
`df["start"].dt.isocalendar().week`, `df["start"].dt.weekday`, return
the year, month, week, day of the week, etc.

If we have a "timedelta" variable called "d", then we can use the `dt`
accessor to obtain aspects of the duration, e.g.  `df["d"].dt.days`
contains the number of days represented by the duration.

---

Numpy
-----

Sometimes we don't want to work with dataframes, we just need arrays
of values.  In this case, we might work with the numpy library instead
of with Pandas.

Numpy provides a data structure called a `ndarray` ("n-dimensional
array").  It is like a Pandas dataframe in many ways, with three key
differences:

* There are no names for rows or columns in a `ndarray` -- all
  indexing, selecting, and slicing must be done by numerical position.
  When accessing values from a `ndarray`, do not use `loc` or `iloc`,
  e.g. if `x` is a `ndarray`, `x[2, 3]`, `x[2, :]`, `x[:, 3]`, and
  `x[3:5, 5:9]` are typical indexing and slicing operations.

* The entire `ndarray` must contain values of a single type
  (e.g. float64).  In a Pandas dataframe, each column must have a
  single type, but different columns can have different types.

* Pandas dataframes can be "indexed", ndarrays cannot.

---

Numpy
-----

The Numpy library provides many functions for manipulating arrays of
values.  Many of these functions can be used interchangeably with
Pandas data containers (dataframes and series). Here are a few
examples of useful numpy functions:

* `np.arange(3, 8)` -- produce a series of values 3, 4, 5, 6, 7.

* `np.arange(3, 8, 2)` -- produce a series of values 3, 5, 7.

* `np.linspace(1, 2, 4)` -- produce a grid of 5 values from 1 to 2.

* `np.sum`, `np.min`, `np.max`, `np.log`, `np.mean`, `np.median` -- mathematical and statistical functions

* `np.clip(x, 1, 2)` -- values in `x` are changed to their closest value in the interval [1, 2]


---

Python syntax and programming concepts
--------------------------------------

* Python is a procedural language, lines of code generally execute in
  sequence, although “control flow” can be modified, e.g. by calling a
  function.

* Variables in Python have a name and a value.  Almost any string
  consisting only of alphanumeric characters can be a variable name,
  as long as the first character is alphabetical.  All Python code,
  including variable names, is case-sensitive.

* Different variables (with different names) can refer to the same
  value, this is called _aliasing_.  If variable names `x` and `y` are
  aliased to refer to the same variable, then changing the value of
  `x` also changes the value of `y`.

* The value referred to by a Python variable is usually a number, a
  string (text), lists of values, or a compound value such as a Pandas
  DataFrame.  There are other types of Python values but these are the
  most common.

---

Functions and data structures in Python
---------------------------------------

* Clear, readable, maintainable Python code makes heavy use of
  functions.  A function in Python is a block of code that takes one
  or more arguments, computes something with them, and then returns
  one or more values.  Some functions are built into Python, and you
  can create your own functions using `def`.

* Good Python code makes heavy use of data structures.  A data
  structure is a collection of related values that are stored as a
  single "object".

* The abstract definition of an object is called a "class", and an
  actual instance of a class is called an "object".

* A Pandas dataframe is a complex class, which contains the column
  names, column types, index information, and the actual data held in
  the dataframe.
