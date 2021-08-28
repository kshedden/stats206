---
title : Computing
---

## Python and its libraries

All computing for this course will utilize a stack of tools based on
the [Python](https://python.org) programming language.  Python is a
general-purpose language.  On its own it is not very capable for
performing data analysis.  However a number of libraries can be used
with Python to provide a powerful data analysis system.  The libraries
we will use in this course are:

* [Pandas](https://pandas.pydata.org) -- data management

* [Seaborn](https://seaborn.pydata.org) -- high-level graphics

* [Statsmodels](http://statsmodels.org) -- statistics and modeling

* [Numpy](https://www.numpy.org) -- numerical and mathematical calculations

* [Scipy](https://scipy.org) -- scientific and mathematical calculations

* [Matplotlib](https://matplotlib.org) -- low level graphics

We will only be using a few components from each of these libraries.
All of the programming concepts that you need for this course will be
illustrated using examples that we provide.  The links above are shown
for your information -- there is no need to review the material at
these links, or to refer to any other Python tutorials or
documentation.

We will be using a Python distribution called
[Anaconda](https://www.anaconda.com/products/individual).  This
distribution includes Python itself along with all of the libraries
discussed above (and many more libraries that we will not be
using).  Anaconda is already installed and configured on the computing
system that we will use in this course.

## Jupyter

You will be using [Jupyter](https://jupyter.org) computational
notebooks for this course.  These notebooks run in your web browser.
You do not need to install any software on your computer to use these
notebooks, except a VPN client if you plan to do any work from off
the UM campus.

A Jupyter notebook consists of a series of "cells".  You can enter
code into a cell, and after running the cell, the result of that code
will appear in the notebook below the cell.  You can run all the cells
of the notebook from top to bottom using the "Run All" option from the
"Cell" menu, located in the menu bar at the top of the notebook.  You
can also run the cells one at a time, by typing "ctrl-enter" after
clicking on the cell that you wish to execute.

Next to each code cell appears the text "In [ ]".  If the brackets are
empty, this cell has not been executed.  If the brackets contain a
number, like "In [3]", these numbers reflect the order in which the
cells were executed.  If the brackets contain a star, like "In [*]",
the code in the cell is currently running.  When you use the "Run All"
menu as discussed above, the entire notebook will be run from top to
bottom.

If you execute the cells individually, the logic of the code follows
the order in which you execute the cells (shown in the "In [ ]"
label), not the order of the cells as they appear in the notebook.  As
a result, running individual cells can result in unexpected and
non-reproducible behavior.  It is best to always run all cells in the
notebook in sequence from top to bottom using the "run all" option
from the Jupyter menu bar.

Each code cell in a Jupyter notebook can contain multiple lines of
code.  By default, the result of the final line of code in a notebook
is printed, but the results of the other lines are not printed.  If
you want to display the result of a line of code that is not the final
line, use the `print` function.

## Greatlakes

You should run all analyses for this course using the
[Greatlakes](https://greatlakes.arc-ts.umich.edu) cloud computing
system (if you are off campus, this link will not work for you unless
you have turned on your VPN).  All of the software that we will use in
this course is already installed and configured on the Greatlakes
system.  Every student taking Stat 206 has a $100 credit for use of
Greatlakes during the term of enrollment, which should be far more
than needed if used appropriately.

Note that while the software used in this course is all open-source,
and the data that we will analyze are open-access, we strongly
discourage you from installing the software and running the analyses
on your own computer.  We will not be able to provide you with any
assistance if you choose to go that route.  Cloud-based computing is becoming
the standard working environment for professional data scientists, and
one of the learning goals for this course is to become proficient in a
cloud environment.  Cloud-based systems offer many adantages in terms
of performance, reliability, cost, and security compared to running
code on your own computer.

You will need to establish an account to use the Greatlakes system,
see [here](/~kshedden/stats206/post/computing_setup) for instructions.
After your account is established, and you start your VPN, you should
be able to access the Greatlakes system from the link given above.
You will have a home directory on Greatlakes where you can save your
Jupyter notebooks.  All of the data that we will be analyzing this
term are stored in a shared directory on Greatlakes.  You will not
need to copy or download any code or data.
