% Data manipulation
% Kerby Shedden
% September 20, 2020

A _dataframe_ is a rectangular data _container_ in which the
rows represent _cases_ (_observations_) and the columns represent
_variables_.

A single column, or variable from a dataframe may be called a
_series_.

A single row, or case from a dataframe may be called a _record_.

A column of a dataframe usually has a fixed _storage type_.
This is the way that the value is stored in the computer's
memory.  For example, a number may be stored as an integer
or a floating point value.

A variable generally will also have a statistical type, such
as being ordinal, nominal, or quantitative.  This is a _semantic_
type in the sense that it reflects what the variable means,
rather than how it is stored or represented.

---

Accessing values
----------------

Elements from a dataframe can be accessed by position, or
using the dataframe's _index_ (or _label_), if one is present.

Suppose we have the following 4x4 dataframe,
where the first row is the column labels and the first
column is the row labels:

| Index      | Sex   | Age   | State  |   SBP  |
| --:        |  --:  | --:   | --:    |   --:  |
| __1432__   |  F    | <50   | CA     |   126  |
| __5434__   |  F    | <50   | AZ     |   126  |
| __1763__   |  M    | <50   | CA     |   125  |
| __7234__   |  F    | >=50  | FL     |   121  |

The row index is derived from a subject ID variable.

---

Accessing values
----------------

In _position-based indexing_, we would access the
element in the second row and third column
with syntax like

* [2, 3] in a ones-based language like R

* [1, 2] in a zeros-based language like Python

This would return "AZ", the state of residence of the
subject with ID (index value) 5434.

---

Accessing values
----------------

In _label-based indexing_, we access elements by label,
e.g. [5434, "State"] yields "AZ" without referring to
its row and column position.

Label-based indexing helps prevent certain types of programming errors.
For example, if the rows or columns are reordered,
the row and column positions for a given value change.

The row and column labels move accordingly if the rows and columns
are reordered, so label-based indexing continues to give
the correct values.

---

Accessing values
----------------

The following dataframe is equivalent to what we
saw above, but now sorted by state:

| Index      | Sex   | Age   | State  |   SBP  |
| --:        |  --:  | --:   | --:    |   --:  |
| __5434__   |  F    | <50   | AZ     |   126  |
| __1432__   |  F    | <50   | CA     |   126  |
| __1763__   |  M    | <50   | CA     |   125  |
| __7234__   |  F    | >=50  | FL     |   121  |

[5434, "State"] continues to yield the correct state
of residence (Arizona) for subject 5434.  But indexing
[1, 2] by position (in zeros-based counting) now yields "CA",
which is incorrect.

---

Slicing
-------

Ranges are defined with colons (:).  If we slice the dataframe
on the previous slide using positions, with [0:2, 1:3]
(in zero-based counting) we get

| Index  | Age   | State  |
| --:    | --:   | --:    |
| 5434   | <50   | AZ     |
| 1432   | <50   | CA     |

By convention, in zero-based counting, the range `i:j` includes
positions `i`, `i+1`, ..., `j-1`.

---

Selecting with Boolean expressions
----------------------------------

Specific rows or columns can be selected based on a condition.

For example, suppose that the expression "State" == "CA" yields
[False, True, True, False].  If we then select from the dataframe
with this Boolean vector, we get

| Index  | Sex   | Age   | State  |   SBP  |
| --:    |  --:  | --:   | --:    |   --:  |
| 1432   |  F    | <50   | CA     |   126  |
| 1763   |  M    | <50   | CA     |   125  |

---

Long/wide data
--------------

Many datasets contain _repeated measurements_ on
a collection of _units_ or _individuals_.

A _long format_ version of such a dataset has one row
per observation.  A _wide format_ version of such a dataset
has one row per individual.

---

Long/wide data
--------------

The following dataframes are wide and long versions
of the same data (the values contained in the first
dataframe are C-reactive protein levels, denoted CRP):

|  ID\Visit |    3   |   6    |   9   |
|     ---:  |   ---: |  ---:  |  ---: |
|   25      |  3     |   5    |   4   |
|   41      |  2     |   6    |   7   |

| ID   | Week | CRP  |
| ---: | ---: | ---: |
|  25  |  3   |  3   |
|  25  |  6   |  5   |
|  25  |  9   |  4   |
|  41  |  3   |  2   |
|  41  |  6   |  6   |
|  41  |  9   |  7   |

---

Long/wide data
--------------

Some long form datasets cannot easily be represented
in wide form, because the repeated measures are not
made on common sets of time points:

| ID   | Week | CRP  | SBP  |
| ---: | ---: | ---: | ---: |
|  25  |  3   |  8   | 141  |
|  25  |  6   |  1   | 135  |
|  25  |  9   |  2   | 131  |
|  41  |  2   |  4   | 128  |
|  41  |  5   |  2   | 119  |
|  41  |  10  |  3   | 122  |

---

Grouping and aggregating
------------------------

Many data analyses follow a paradigm known
as _split/apply/combine_.  This is a very
flexible and powerful framework.  Here we
give one example (SBP is "systolic blood pressure").

Supppose we have the following dataframe:


| Sex  | Age   | SBP  |
| --:  | --:   | --:  |
| F    | <50   | 131  |
| F    | <50   | 121  |
| M    | <50   | 125  |
| F    | >=50  | 121  |
| M    | >=50  | 146  |
| M    | >=50  | 142  |
| M    | >=50  | 150  |

---

Grouping and aggregating
------------------------

Aggregating by taking the mean over sex/age groups
produces the following reduced table:

| Sex  | Age   | SBP  |
| --:  | --:   | --:  |
| F    | <50   | 126  |
| M    | <50   | 125  |
| F    | >=50  | 121  |
| M    | >=50  | 146  |
