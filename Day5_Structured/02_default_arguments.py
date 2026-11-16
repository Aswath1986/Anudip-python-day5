"""
==========================================================================
 Day 5 | Lesson 02 : Default Arguments
==========================================================================
 First principle
   Most calls to a function use the same value for some slot.
   Making the caller repeat it every time is wasted effort.
   A DEFAULT is a value the function uses when the caller gives nothing.

 What you will learn
   1. How to give a parameter a default value
   2. How to override the default
   3. The rule: parameters with defaults come last
   4. You have used defaults all along: print(sep, end)

 Run this file :  python 02_default_arguments.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. A default fills the slot when the caller leaves it empty
# --------------------------------------------------------------------------
def greet(name, city="Chennai"):
    print(f"Hello {name} from {city}")

greet("Asha")                           # Hello Asha from Chennai
greet("Ravi", "Delhi")                  # Hello Ravi from Delhi
greet("Meena", city="Pune")             # Hello Meena from Pune

# --------------------------------------------------------------------------
# 2. More than one default - use keywords to pick which one to change
# --------------------------------------------------------------------------
def power(base, exponent=2, show=False):
    result = base ** exponent
    if show:
        print(f"{base} to the power {exponent} is {result}")
    return result

print(power(5))                         # 25
print(power(5, 3))                      # 125
power(5, show=True)                     # 5 to the power 2 is 25
# show=True skipped over exponent. Only a keyword can do that.

# --------------------------------------------------------------------------
# 3. The rule: no-default parameters first, default parameters last
# --------------------------------------------------------------------------
# This line is not allowed. Remove the # to see the SyntaxError:
# def greet(city="Chennai", name):
#     pass
# Why? greet("Asha") would be unclear: is "Asha" the city or the name?

# --------------------------------------------------------------------------
# 4. print() has defaults too
# --------------------------------------------------------------------------
print("a", "b", "c")                    # a b c      (sep=" " is the default)
print("a", "b", "c", sep="-")           # a-b-c
print("no new line", end=" | ")         # end="\n" is the default
print("same line")


# ==========================================================================
# PREDICT before you run!
#
#   def bill(amount, tax=5, tip=0):
#       print(amount + tax + tip)
#
#   bill(100)
#   bill(100, 10)
#   bill(100, tip=20)
#   bill(tip=1, amount=1)
#
# TRY IT YOURSELF
#   1. Write area(length, width=1). area(5) should return 5,
#      area(5, 2) should return 10.
#   2. Write welcome(name, greeting="Hello", mark="!") and call it so that
#      only the mark changes.
# ==========================================================================
