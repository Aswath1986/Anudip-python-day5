"""
==========================================================================
 Day 5 | Lesson 09 : Libraries
==========================================================================
 First principle
   Most problems you meet were solved by someone else years ago:
   square roots, dates, random numbers, reading web pages.
   A LIBRARY is a collection of modules that someone packaged so that
   everyone can reuse it. Good programmers look before they build.

 The words
   module            one .py file
   package           a folder of modules
   library           a collection of modules/packages made for reuse
   standard library  the library that is installed with Python itself
   third-party       a library you add yourself with:  pip install name

 What you will learn
   1. A tour of the standard library: math, random, datetime, statistics, os
   2. How to find out what a module offers: dir() and help()
   3. Third-party libraries and pip

 Run this file :  python 09_libraries.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. The standard library - already on your laptop
# --------------------------------------------------------------------------
import math
print(math.sqrt(144))                   # 12.0
print(math.ceil(4.1), math.floor(4.9))  # 5 4
print(math.factorial(5))                # 120  (Lesson 05, already written!)

import random
print(random.randint(1, 6))             # a dice roll: different each run
print(random.choice(["Asha", "Ravi", "Meena"]))

import datetime
republic_day = datetime.date(2026, 1, 26)
print(republic_day.strftime("%A"))      # Monday
print(datetime.date(2026, 12, 31) - republic_day)       # 339 days, 0:00:00

import statistics
print(statistics.mean([70, 80, 90]))    # 80
print(statistics.median([5, 1, 9]))     # 5

import os
print(os.path.exists("shop_tools.py"))  # True if you run from this folder
print(os.path.basename(os.getcwd()))    # the folder you are in

# --------------------------------------------------------------------------
# 2. What is inside a module?
# --------------------------------------------------------------------------
names = dir(math)                       # every name the module offers
print(len(names), "names in math. Some of them:", names[-5:])

# In the Python shell, try:   help(math.sqrt)
print(math.sqrt.__doc__)                # the one-line description

# --------------------------------------------------------------------------
# 3. Third-party libraries - installed with pip
# --------------------------------------------------------------------------
# These do not come with Python. You install them once from the terminal:
#     pip install requests
# Python downloads them from PyPI (pypi.org), a public shelf of libraries.
try:
    import requests
    print("requests is installed, version", requests.__version__)
except ModuleNotFoundError:
    print("requests is not installed. Run:  pip install requests")

# Libraries you will meet in industry:
#   requests   talk to websites and APIs
#   pandas     tables of data, like Excel in code
#   numpy      fast maths on large sets of numbers
#   flask      build a website
#   pytest     test your code


# ==========================================================================
# PREDICT before you run!
#
#   import math
#   print(math.floor(-2.5))
#   print(math.ceil(-2.5))
#
#   from math import sqrt
#   print(sqrt(16) + 1)
#
# TRY IT YOURSELF
#   1. Use random to pick a random student from a list of five names.
#   2. Use datetime.date.today() to print today's date, then find how
#      many days remain until 31 December.
#   3. Open pypi.org, search for a library about something you like
#      (cricket, music, maps). Read what it does. Do not install it yet.
# ==========================================================================
