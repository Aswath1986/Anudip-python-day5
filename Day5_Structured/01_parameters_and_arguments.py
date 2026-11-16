"""
==========================================================================
 Day 5 | Lesson 01 : Parameters and Arguments
==========================================================================
 First principle
   A function is a machine with empty slots. The slots are PARAMETERS.
   The values you put into the slots are ARGUMENTS.
   Every rule in this lesson answers one question:
   "How does Python decide which value goes into which slot?"

 What you will learn
   1. Parameter vs argument
   2. Positional arguments - the ORDER decides
   3. Keyword arguments - the NAME decides
   4. Mixing both, and the one rule about mixing
   5. What happens when a slot is left empty

 Run this file :  python 01_parameters_and_arguments.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. Parameter vs argument
# --------------------------------------------------------------------------
def greet(name, city):                  # name, city        -> PARAMETERS (slots)
    print(f"Hello {name} from {city}")

greet("Asha", "Chennai")                # "Asha", "Chennai" -> ARGUMENTS (values)

# --------------------------------------------------------------------------
# 2. Positional arguments - the order decides
# --------------------------------------------------------------------------
# First value -> first slot, second value -> second slot.
greet("Chennai", "Asha")                # Hello Chennai from Asha
# No error! Python cannot know you swapped them. The order is your job.

# --------------------------------------------------------------------------
# 3. Keyword arguments - the name decides
# --------------------------------------------------------------------------
# You write slot=value. Now the order does not matter.
greet(city="Chennai", name="Asha")      # Hello Asha from Chennai

# --------------------------------------------------------------------------
# 4. Mixing both - positional first, keyword after
# --------------------------------------------------------------------------
greet("Asha", city="Chennai")           # Hello Asha from Chennai

# This line is not allowed. Remove the # to see the SyntaxError:
# greet(name="Asha", "Chennai")
# Why? After a keyword, Python can no longer count positions safely.

# --------------------------------------------------------------------------
# 5. Every slot must be filled exactly once
# --------------------------------------------------------------------------
try:
    greet("Asha")                       # city is left empty
except TypeError as error:
    print("Error:", error)

try:
    greet("Asha", "Chennai", "India")   # one value too many
except TypeError as error:
    print("Error:", error)


# ==========================================================================
# PREDICT before you run!
#
#   def divide(top, bottom):
#       print(top / bottom)
#
#   divide(10, 2)
#   divide(2, 10)
#   divide(bottom=2, top=10)
#
# TRY IT YOURSELF
#   1. Write a function ticket(name, seat, price) that prints one line.
#   2. Call it three ways: all positional, all keyword, and mixed.
#   3. Which call is the easiest for another person to read? Why?
# ==========================================================================
