"""
==========================================================================
 Day 5 | Lesson 05 : Recursive Functions
==========================================================================
 First principle
   Some problems contain a smaller copy of themselves.
   "Count down from 3" = say 3, then "count down from 2".
   A RECURSIVE function solves a small piece, then calls ITSELF
   for the smaller copy. It must also know when to stop.

 What you will learn
   1. A function can call itself
   2. The two parts: BASE CASE (stop) and RECURSIVE CASE (shrink)
   3. Factorial, step by step
   4. What happens with no base case
   5. Where recursion is the natural tool: things inside things

 Run this file :  python 05_recursion.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. A function that calls itself
# --------------------------------------------------------------------------
def countdown(n):
    if n == 0:                          # BASE CASE: stop here
        print("Lift off!")
        return
    print(n)
    countdown(n - 1)                    # RECURSIVE CASE: a smaller problem

countdown(3)

# --------------------------------------------------------------------------
# 2. Factorial: 4! = 4 * 3 * 2 * 1
# --------------------------------------------------------------------------
# Look for the smaller copy:  4! = 4 * 3!     3! = 3 * 2!     ...
def factorial(n):
    if n <= 1:                          # BASE CASE
        return 1
    return n * factorial(n - 1)         # RECURSIVE CASE

print(factorial(4))                     # 24

# How Python works it out. Each call WAITS for the call below it:
#   factorial(4) = 4 * factorial(3)
#                      3 * factorial(2)
#                          2 * factorial(1)
#                              1            <- base case, answers start
#                          2 * 1 = 2           coming back up
#                      3 * 2 = 6
#                  4 * 6 = 24

# --------------------------------------------------------------------------
# 3. The same job with a loop
# --------------------------------------------------------------------------
def factorial_loop(n):
    result = 1
    for number in range(2, n + 1):
        result *= number
    return result

print(factorial_loop(4))                # 24
# Anything recursion can do, a loop can do too. Choose the one that is
# easier to read for the problem in front of you.

# --------------------------------------------------------------------------
# 4. No base case = no stopping
# --------------------------------------------------------------------------
def forever(n):
    return forever(n + 1)               # never gets smaller, never stops

try:
    forever(1)
except RecursionError:
    print("Python stopped it: too many calls waiting")

# --------------------------------------------------------------------------
# 5. Where recursion fits best: things inside things
# --------------------------------------------------------------------------
# A box can hold numbers and other boxes. How deep? We do not know.
box = [1, 2, [3, 4, [5, 6]], 7]

def total(items):
    result = 0
    for item in items:
        if type(item) == list:          # a box inside the box:
            result += total(item)       #   the same problem, but smaller
        else:
            result += item
    return result

print(total(box))                       # 28
# Folders inside folders, comments under comments, menus inside menus:
# all have this shape.


# ==========================================================================
# PREDICT before you run!
#
#   def mystery(n):
#       if n == 0:
#           return 0
#       return n + mystery(n - 1)
#
#   print(mystery(4))
#
# TRY IT YOURSELF
#   1. Write count_up(n) that prints 1 to n using recursion.
#      Hint: call yourself first, print after.
#   2. Write power(base, exponent) using recursion.
#      power(2, 3) = 2 * power(2, 2). What is the base case?
#   3. Write reverse(text) that returns the text backwards.
#      reverse("abc") = reverse("bc") + "a".
# ==========================================================================
