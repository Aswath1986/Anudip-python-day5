"""
==========================================================================
 Day 5 | Lesson 03 : *args - Any Number of Positional Arguments
==========================================================================
 First principle
   A function has a fixed number of slots. But some jobs do not know the
   count in advance: add 2 numbers, or 3, or 50.
   *args is ONE slot that collects ALL the extra positional values
   into a tuple.

 What you will learn
   1. The problem with a fixed number of parameters
   2. *args collects extra positional arguments into a tuple
   3. Normal parameters together with *args
   4. The opposite direction: * unpacks a list at the call
   5. print() itself uses *args

 Run this file :  python 03_args_any_number_of_positionals.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. The problem
# --------------------------------------------------------------------------
def add_two(a, b):
    return a + b

print(add_two(1, 2))                    # 3
# add_two(1, 2, 3) fails. Writing add_three, add_four ... is not a solution.

# --------------------------------------------------------------------------
# 2. *args - one slot that collects everything
# --------------------------------------------------------------------------
def total(*numbers):
    print("numbers is", numbers, type(numbers))
    result = 0
    for n in numbers:
        result += n
    return result

print(total(1, 2))                      # 3
print(total(1, 2, 3, 4, 5))             # 15
print(total())                          # 0   (an empty tuple)

# The star does the collecting. The name is your choice:
# *numbers, *marks, *items. Many people write *args ("arguments").

# Why a tuple and not a list? The function received these values.
# It should read them, not change them. Day 3: share as immutable.

# --------------------------------------------------------------------------
# 3. Normal parameters first, *args takes the rest
# --------------------------------------------------------------------------
def report(student, *marks):
    print(student, "has", len(marks), "marks, highest is", max(marks))

report("Asha", 70, 85, 90)              # Asha has 3 marks, highest is 90

# --------------------------------------------------------------------------
# 4. The opposite direction: * at the CALL unpacks a list
# --------------------------------------------------------------------------
marks = [70, 85, 90]
print(total(*marks))                    # same as total(70, 85, 90) -> 245

# Without the star the whole list goes in as ONE argument:
# total(marks) would try 0 + [70, 85, 90] and raise a TypeError.

# --------------------------------------------------------------------------
# 5. print() has always worked this way
# --------------------------------------------------------------------------
print("one")
print("one", "two", "three")
print(*marks)                           # 70 85 90


# ==========================================================================
# PREDICT before you run!
#
#   def show(first, *rest):
#       print(first)
#       print(rest)
#
#   show(1)
#   show(1, 2, 3)
#   show(*"hi")
#
# TRY IT YOURSELF
#   1. Write average(*numbers). average(10, 20, 30) should return 20.0.
#      What should average() with no numbers do? Handle it with an if.
#   2. Write longest(*words) that returns the longest word.
# ==========================================================================
