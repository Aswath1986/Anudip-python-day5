"""
==========================================================================
 Day 5 | Lesson 04 : **kwargs - Any Number of Keyword Arguments
==========================================================================
 First principle
   *args collects extra values that have a POSITION.
   Some extra values need a NAME as well: age=21, city="Pune".
   **kwargs is one slot that collects all extra name=value pairs
   into a dictionary.

 What you will learn
   1. **kwargs collects extra keyword arguments into a dict
   2. All four kinds of parameter in one function, and their order
   3. The opposite direction: ** unpacks a dict at the call

 Run this file :  python 04_kwargs_any_number_of_keywords.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. **kwargs - a dict of everything that came with a name
# --------------------------------------------------------------------------
def profile(**details):
    print("details is", details, type(details))
    for key, value in details.items():
        print(f"  {key} -> {value}")

profile(name="Asha", age=21)
profile(name="Ravi", city="Delhi", course="Python", year=1)
profile()                               # an empty dict

# Two stars collect pairs. The name is your choice; many people
# write **kwargs ("keyword arguments").

# --------------------------------------------------------------------------
# 2. All four kinds together
# --------------------------------------------------------------------------
# The usual order in the def line:
#   1. normal parameters
#   2. *args
#   3. parameters with defaults
#   4. **kwargs
def enrol(name, *subjects, fee=1000, **extra):
    print("name    :", name)
    print("subjects:", subjects)
    print("fee     :", fee)
    print("extra   :", extra)

enrol("Asha", "Python", "SQL", fee=1500, city="Chennai", batch="A")

# How Python fills the slots:
#   "Asha"            -> name       (first position)
#   "Python", "SQL"   -> subjects   (the remaining positions)
#   fee=1500          -> fee        (name matches a parameter)
#   city=, batch=     -> extra      (names that match nothing else)

print("---")
enrol("Ravi")                           # everything optional is empty

# --------------------------------------------------------------------------
# 3. The opposite direction: ** at the CALL unpacks a dict
# --------------------------------------------------------------------------
def greet(name, city):
    print(f"Hello {name} from {city}")

person = {"name": "Meena", "city": "Pune"}
greet(**person)                         # same as greet(name="Meena", city="Pune")


# ==========================================================================
# PREDICT before you run!
#
#   def show(a, *b, c=0, **d):
#       print(a, b, c, d)
#
#   show(1)
#   show(1, 2, 3)
#   show(1, 2, c=3)
#   show(1, x=2, y=3)
#
# TRY IT YOURSELF
#   1. Write make_card(name, **details) that prints the name, then one
#      line for every detail. Call it with 0, 1 and 3 details.
#   2. Write order(item, *toppings, size="medium", **notes) and call it
#      so that every slot receives something.
# ==========================================================================
