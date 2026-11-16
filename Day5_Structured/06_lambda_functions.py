"""
==========================================================================
 Day 5 | Lesson 06 : Lambda Functions
==========================================================================
 First principle
   Sometimes you need a tiny function exactly once, as an input to
   another function. Giving it a def and a name is more ceremony than
   the job deserves. A LAMBDA is a function written as one expression,
   with no name.

 What you will learn
   1. def and lambda side by side
   2. The shape: lambda parameters: expression
   3. The real use: handing a small function to another function
   4. What a lambda cannot do

 Run this file :  python 06_lambda_functions.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. The same function, written two ways
# --------------------------------------------------------------------------
def square(x):
    return x * x

square_short = lambda x: x * x

print(square(5))                        # 25
print(square_short(5))                  # 25

# --------------------------------------------------------------------------
# 2. The shape
# --------------------------------------------------------------------------
#   lambda  x, y  :  x + y
#   ------  ----     -----
#   keyword inputs   the value that is returned (no "return" word)

add = lambda x, y: x + y
print(add(2, 3))                        # 5

always_ten = lambda: 10                 # no inputs is allowed
print(always_ten())                     # 10

with_default = lambda name, greeting="Hello": f"{greeting} {name}"
print(with_default("Asha"))             # Hello Asha

# --------------------------------------------------------------------------
# 3. The real use: a function as an input
# --------------------------------------------------------------------------
# sorted() accepts key=<a function>. It calls that function on every item
# and sorts by the answers.
names = ["Ravi", "Meenakshi", "Asha", "Bo"]

print(sorted(names))                            # alphabetical
print(sorted(names, key=len))                   # by length
print(sorted(names, key=lambda n: n[-1]))       # by LAST letter

students = [("Asha", 82), ("Ravi", 67), ("Meena", 91)]
print(sorted(students, key=lambda s: s[1]))     # by marks
print(max(students, key=lambda s: s[1]))        # ('Meena', 91)

# Without lambda you would write this, and use it only once:
def get_marks(student):
    return student[1]

print(sorted(students, key=get_marks))          # same result

# --------------------------------------------------------------------------
# 4. What a lambda cannot do
# --------------------------------------------------------------------------
# One expression only. No if-blocks, no loops, no assignments, no try.
# If the job needs two lines, write a def. Readable beats short.


# ==========================================================================
# PREDICT before you run!
#
#   f = lambda a, b=2: a * b
#   print(f(3))
#   print(f(3, 3))
#   print((lambda x: x + 1)(9))
#
#   words = ["pear", "fig", "banana"]
#   print(sorted(words, key=lambda w: len(w)))
#
# TRY IT YOURSELF
#   1. Write a lambda that turns Celsius into Fahrenheit (c * 9 / 5 + 32).
#   2. Sort [("pen", 10), ("book", 60), ("bag", 450)] by price, highest
#      first. Hint: sorted(..., key=..., reverse=True).
#   3. Rewrite your lambda from 1 as a def. Which do you prefer here?
# ==========================================================================
