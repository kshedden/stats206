# # Scooter sharing in Austin, Texas

# In many cities around the world, micromobility in the form of
# electric scooters has recently become very popular.  The city of
# Austin, Texas has made available trip-level data from all scooter
# companies operating within the city limits.

# This is the first notebook that we see in Stats 206.  We are mainly
# focused here on introducing the software tools and doing some very
# basic summarization and description of the data.  There are a lot of
# new programming concepts below, and some of them are deliberately
# only explained at a high level.  We will revisit many of these
# concepts later in the course and discuss them in greater detail at
# that time.

# # Importing modules

# Python is a general-purpose programming language.  On its own, it
# can be used for some basic tasks.  Most of the time, when working
# with Python, you will be importing _modules_ containing code that is
# not part of the core Python language, that will help you perform
# more specialized tasks.  For scientific computing and data science,
# we almost always import the numpy and pandas modules.

import numpy as np
import pandas as pd

# In addition, we will often need the "os" (operating system) module:

import os

# # Loading data from a file

# The scooter data are in a format called "csv", which stands for
# "comma separated values".  This is the most common portable
# text-based format for rectangular data (data arranged in a table
# with rows and columns).  The "pandas" package, imported above,
# provides data management and basic data analysis capabilities in
# Python.  The central element of Pandas is a "dataframe", which is a
# rectangular structure for holding data.
#
# Our first step here is to read the data from a csv format file
# containing the scooter trips, and represent it in the computer's
# memory as a dataframe.

# First, modify this string according to your section number (001 or
# 002):

f = "stats206s002f21"

# Now Pandas can read the data using the line of code below:

base = "/scratch/%s_class_root/%s_class/shared_data/datasets" % (f, f)
df = pd.read_csv(os.path.join(base, "scooters_short.csv.gz"))

# The above commands create a dataframe holding the scooter trip data,
# and creates a variable named `df` that is bound to this value.
#
# In the above commands, the values enclosed in quotation marks are
# "strings".  A string is a value that contains a sequence of text or
# characters.  In this case, the string bound to the "base" variable
# is the "file path" pointing to the CSV file on greatlakes that we
# wish to load.

# Note also that the filename above ends with ".gz".  This indicates
# that the data are compressed so that the file takes up less space on
# the disk.  Pandas will automatically decompress the file when
# reading it.

# The dataframe that we just loaded contains all trips for a random
# selection of 20,000 scooters drawn from the complete Austin mobility
# dataset.

# # Getting some basic information about the data

# Now that we have the dataset loaded, we can do some basic things
# with it.  First, we will get the shape, or dimensions of the
# dataframe:

df.shape

# The shape attribute contains the number of rows and the number of
# columns in the dataframe.  This dataset is a subset containing about
# one quarter of the complete Austin e-mobility dataset.

# Like most rectangular datasets, the rows of this dataset represent
# cases and the columns represent variables.  A case here is a single
# trip on a rented scooter.  The columns (variables) provide
# information about the trip.  Next we will see what the names of the
# variables are.

df.columns

# Some of these variable names are self-explanatory, for others, we
# will explain their meaning below as needed.  The next line of code
# displays the first few rows of the dataframe.  Depending on the
# width of your screen, it is possible that only a subset of the
# columns will be shown, in which case the omitted columns are
# displayed as "...".

df.head()

# Note that in the preceeding two code cells, "head" is followed by
# parentheses and "column" is not. This is because "head" is a method
# while "columns" is an attribute.  Methods are essentially functions,
# and functions take arguments inside a pair of parentheses.
# Attributes are not functions, and therefore do not have parentheses.
# It is an error to use parentheses on an attribute, or to omit the
# parentheses on a method.  To avoid such errors, you will need to
# learn when you have an attribute and when you have a method.

# The `head` method takes an optional argument, which is the number of
# rows to display.  The default value of this argument is 5, so if we
# call the method without any arguments, like above, we see five rows
# of data.  If we want to see a different number of rows, we can pass
# an argument like this:

df.head(3)

# The "device ID" is a unique identifier for each scooter. The number
# of times that a device ID appears in the dataframe is the number of
# times that the scooter was rented during the period of time covered
# by the dataset.  Most of the device IDs appear multiple times in the
# data set, since most of the scooters were rented multiple times.
#
# To learn more about the device IDs, we can select the column of the
# dataframe containing these values using the syntax `df["Device
# ID"]`.  This creates a "series" since it contains data for only one
# variable. The `unique` method then constructs another series
# containing only the unique device IDs, and the `size` attribute of
# this series tells us how many elements it contains.  Thus, the
# following line of code tells us how many unique scooters are
# represented in this dataset.

df["Device ID"].unique().size

# The above code uses "chaining" to do three things in one line of
# code.  It may be instructive to see how this can be done in three
# lines, without chaining.

x = df["Device ID"]
y = x.unique()
y.size

# We can now look at some summary statistics of how many times each
# scooter was rented.  The `value_counts` method determines all of the
# distinct values in a series and counts how many times each occurs.
# The `describe` method then produces a set of summary statistics for
# these counts.

df["Device ID"].value_counts().describe()

# When Pandas reads a CSV file, the date and time variables are
# usually not automatically converted to proper Pandas format.  The
# `dtypes` attribute tells us the storage format of each variable in
# the dataframe.  We can see below that the "Start Time" and "End
# Time" variables have `object` storage format. To work with these
# variables as time values we will want to convert them to "datetime"
# values.

df.dtypes

# The following lines of code perform this conversion for the "Start
# Time" variable.  Don't worry about the details of this conversion at
# the moment.

f = "%m/%d/%Y %I:%M:%S %p"
df["Start Time"] = pd.to_datetime(df["Start Time"], format=f)

# Now that we have this variable in a proper format, we can determine
# the period of time covered by this dataset.

print(df["Start Time"].min())
print(df["Start Time"].max())

# Regarding the use of `print` above -- the `print` function is used
# to print a value to the notebook output cell.  By default, the value
# of the last expression in any code cell is always printed.  If you
# want to print more than one value from within a single code cell,
# you should use the `print` function.

# ## Scooter lifespan

# One question that is often asked about scooter rentals is how long
# the scooters stay in the fleet.  In some cities, scooters have
# generally not lasted very long before breaking or being stolen or
# lost.  To address this question, we can look at the earliest and
# last rental of each scooter in the dataset.  We do this by creating
# a "grouped dataframe" with the `groupby` method.  Grouped dataframes
# are very powerful and we will use them frequently in this course.
# We will explain how grouped dataframes work in more detail later.
# This example is an introduction to show how grouped dataframes can
# be used to achieve our current goals.

dx = df.groupby("Device ID")["Start Time"].agg([np.min, np.max])
print(dx.columns)
dx["duration"] = dx["amax"] - dx["amin"]
print(df.shape, dx.shape)
dx["duration"].describe()

# `groupby` carries out a stratification of the data.  In this case,
# we are stratifying the data by the `Device ID` variable.  Every
# distinct value of `Device ID` forms a group.  A group contains all
# trips recorded for one scooter.  We then select only the `Start
# Time` variable.  Finally, the `agg` method is used to carry out an
# aggregation or summarization of the data for each group.

# The functions passed as arguments to `agg()` are the functions used
# to do the aggregation.  Here we are aggregating using the `min` and
# `max` functions. These will give us the minimum (earliest) and
# maximum (latest) trip for each scooter.  The `np.` is placed in
# front of the `min` and `max` functions because they are part of the
# numpy package, which we imported above.

# Sometimes it can be hard to know what names the variables created by
# the aggregation will have.  Therefore, we print the names and see
# here that they are "amax" and "amin".

# We also printed the shapes of the two dataframes `df` and `dx`.
# Here, `df` is the original dataframe that we loaded from a csv file,
# and `dx` is the summarized dataframe containing one row for each
# distinct device ID.  Since there are 20,000 scooters in the dataset,
# this summarized dataframe contains exactly 20,000 rows.

# Once we have the minimum and maximum rental date per scooter, we can
# subtract them to get the duration of time between the first and last
# rental.  Then, we use the `describe` method to get some basic
# summary information about these durations.

# We see that the median scooter was used for a period of 82 days.
# Note that this is a biased estimate of the actual median lifespan
# due to "truncation" and "censoring".  We won't define these terms
# precisely here, but they refer to the fact that some scooters were
# in use before and/or after the period of time covered by this
# dataset, so their actual lifespan is longer than the value
# calculated here.  There are more advanced statistical methods that
# can be used to correct for this bias, but we will not pursue that
# here.

# ## Scooter usage over time

# The usage of scooters varies throughout the year, and over the span
# of several years.  Scooter usage also varies by time of day and day
# of week, but this is a separate topic that we will revisit later.
# To focus on the longer term variation in scooter usage, we create a
# variable below that counts the total number of trips taken during
# each week within the dataset.  We have around two year's of data, so
# there are slightly more than 100 weeks.

# To accomplish this goal, we will add two new columns to the
# dataframe, one containing the year in which the trip occured, and
# one containing the week within the year that the trip occured (which
# is an integer between 1 and 52).  Since we already have the start
# time of each trip, we only need to exract the year and week from the
# start time, as shown below.  The `dt` symbol is a special attribute
# of datetime variables that allows us to do things that only make
# sense with date and/or time values.

df["year"] = df["Start Time"].dt.year
df["weekofyear"] = df["Start Time"].dt.isocalendar().week

# Now that we have a variables indicating the year and week of each
# trip, we can use `groupby` to count how many trips occur for each
# combination of a year and a week.  Note that here, unlike above, we
# are grouping by two variables, which must be placed in a list using
# square brackets (`[]`).

dx = df.groupby(["year", "weekofyear"]).size()

# Here we are taking advantage of the built in `size` aggregation
# method.  This gives us the number of rows per group, which is
# equivalent to the number of trips per week.  The same result can be
# obtained using

dxx = df.groupby(["year", "weekofyear"])["Device ID"].agg(np.size)

# To confirm that these two series are equal, we can use the
# following:

assert(all(dx == dxx))

# It would make most sense to graph these counts, but we are not
# introducing graphing yet in this notebook, so we will simply display
# the counts in a table.  Since our grouped dataframe here groups by
# two variables, we have what is called a "hierarchical index".  We
# could view the result (`dx`) directly, but to make it easier to read
# the table, we can "unstack" it to produce a table in which the rows
# are years and the columns are weeks.  This will be a 4 x 52 table
# since we have at least some data in each of four years.  For viewing
# on the screen, it is better to have a table that is longer rather
# than wider, so we use the transpose (`T`) attribute to put the weeks
# in the rows and the years in the columns.

dx.unstack().T

# In the result of the above cell, a `NaN` ("not a number") will
# appear in any cell that has no data.  This includes some cells that
# fall in the future relative to when the data were obtained, and some
# earlier cells for which no data are available.

# The results show that scooter usage increased rapidly in late summer
# of 2018 and remained very popular until late fall of 2019.  Note the
# spike in week 11 of 2019, corresponding to the "South by Southwest"
# event.  By late fall of 2019 and into the early winter of 2020,
# scooter usage had dropped by around half relative to the same period
# in the previous year.  Then around week 12 of 2020, the COVID
# pandemic reached the US, and scooter usage plumetted (although not
# to zero).  By the end of the data series in the summer of 2020,
# usage had recovered slightly, but only to around 15% of usage in the
# previous year.  In 2021, scooter usage remained somewhat lower than
# pre-pandemic levels.

# ## Trip duration

# Another characteristic of interest is the length of time of each
# trip.  We can get this by subtracting the start time from the end
# time for each trip.  But first we will convert the end time to a
# proper datetime format, like we did for the start time earlier.

f = "%m/%d/%Y %I:%M:%S %p"
df["End Time"] = pd.to_datetime(df["End Time"], format=f)
df["Duration"] = df["End Time"] - df["Start Time"]

# We can use `describe` again to obtain some basic summary
# information, but this mainly reveals that there are some issues with
# the data.  This is extremely common with administrative data such as
# we have here.  For example, we see that the longest trip was several
# weeks long, and the shortest trip had a negative duration.

df["Duration"].describe()

# If we look at all the distinct duration values, we see that they are
# all in 15 minute increments.

df["Duration"].value_counts()

# The start time and end time values are rounded in the data to the
# nearest quarter hour, so that very short trips will be recorded as
# having zero duration.  The next cell shows what proportion of the
# trips are recorded as beginning and ending at the same (rounded)
# time point, and thus having a reported duration of zero.

du = df["Duration"]
(du == pd.to_timedelta(0)).mean()

# In the cell above, we use the `mean` method to calculate a
# proportion, and we use the `to_timedelta` function to create a time
# duration with zero length to use in the comparison.

# Quantiles (compared to moments such as the mean) tend to be less
# affected by data errors (as long as there aren't too many of them).
# We can look at a few of the quantiles below, and we see that many of
# the lower quantiles have zero duration, and the median duration is
# 15 minutes.

du.quantile([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

# A more concise way to obtain these same quantiles is as follows:

q = np.arange(0.1, 0.91, 0.1)
du.quantile(q)

# The function `np.arange(a, b, c)` creates a sequence of
# regularly-spaced values, starting at `a`, increasing in steps of
# `c`, and continuing as long as the value is less than `b`.  Note
# that to include 0.9 in the list, the value of `b` must be strictly
# larger than 0.9.

# We see that the vast majority of trips are under 30 minutes.  To see
# the longer trips, we will want to look at more extreme quantiles

du.quantile([0.95, 0.99, 0.999])

# This shows us, for example, that around 1 in 100 trips lasts one
# hour and 15 minutes or longer.
