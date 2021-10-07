---
title : Computing setup
---

The computing in this class will use the University of Michigan's
cloud computing system called _Greatlakes_.  To access this system,
you will need access to a computer with a web browser, a VPN client
(if working off-campus), and
a stable internet connection.  You will not need to install any other
software on your computer.

All students in this course must request a Greatlakes account by
filling out [this
form](https://teamdynamix.umich.edu/TDClient/30/Portal/Requests/TicketRequests/NewForm?ID=iT-mreMQ984_).
Please do this as soon as possible as it may take a few days for the
request to be processed.  When filling out the form, enter the name of
your Statistics 206 instructor as the "advisor", enter "Statistics
206" under the project description, and enter "Literature, Science, and the
Arts" in the college/department field.  For the final question on the
form, the ARC-TS service to which you are requesting access is "Great
Lakes" (do not select any of the other services except for Great Lakes).

You will need to run a VPN client on your computer when accessing Greatlakes
from off campus.  Information about obtaining and
configuring free VPN clients for all major platforms can be found
[here](https://its.umich.edu/enterprise/wifi-networks/vpn/getting-started).
If you are working on the UM campus, you do not need to use a VPN.

Greatlakes uses two-factor authentication.  You will need to
have your phone or other two-factor device with you whenever you plan
to use this system.

The IT staff must manually add everyone from the Statistics 206 roster
to the account for this course.  Near the beginning of the semester,
everyone who is currently enrolled in Statistics 206 will be added.
If you add the class late and cannot access the system, let your
instructor know that you need to be added to the account.

# Connecting to Jupyter -- step-by-step instructions

The following five steps will create a Jupyter session for you.  You
will need to follow these five steps every time you want to use Jupyter
on Greatlakes.

1. If working off-campus, make sure your VPN client is activated.

2. Connect to [Greatlakes](https://greatlakes.arc-ts.umich.edu) using
your web browser.  If you click this link and get a message saying
something like "this site can't be reached", then most likely you
are off campus and your VPN is not turned on.

3. After connecting to Greatlakes, select the "Interactive Apps" menu
at the top of the window, then press "Jupyter Notebook".

4. You will be taken to a form that allows you to request access to
the Jupyter notebook server.  Most fields in the form will be set to
default values that you do not need to change.  Under _account_, you
should enter "stats206s###f21_class", where ### is your three digit
section number, either "001" or "002".  By default, you will be given
access for one hour.  You can change this to a greater value, but
requesting very long sessions may rapidly deplete your $100 computing
allocation.  You should always request 1 core and 4 GB memory per node
(changing these to greater values will not provide any benefit, and
may rapidly deplete your allocation).

5. Press the _Launch_ button and you will be taken to another page
showing that your request is processing.  Within a minute or two, a
button that says "Connect to Jupyter" should appear.  Press this
button and you will be directed to a file listing for your home
directory.

# Obtaining the notebooks

The first time that you connect to Jupyter, you should perform the following
steps to obtain local copies of all the notebooks that you can execute
and edit.  You will only need to do this one time (if you do it again, it will
over-write any changes to the notebooks that you have made).

1. Near the top right corner of the screen, there is a menu that says
"New".  Press it, then select "Terminal".

2. At the prompt in the terminal window, type "cd" then press "enter".  Then type
"pwd" followd by "enter" and you should see the path to your home directory,
which will have the form "/home/uniqname", where "uniqname" is your UM uniqname.

3. Type or copy/paste the following command into the terminal and press "enter":

`wget raw.github.com/kshedden/stats206/main/case_studies/download.sh -O download.sh`

4. Type "bash download.sh" then press "enter".

5. To confirm that everything worked, type "ls -lt" followed by "enter".  You should
see the names of several files ending with ".ipynb".  These are the Jupyter 
notebook files that we will use in this course.  

You can open any notebook
by double clicking the file name in the directory listing.  Once the
notebook is open, you can run it by 
clicking on "Cell" in the top menubar, then selecting "Run All".

