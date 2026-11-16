"""
==========================================================================
 Day 5 | Deep Dive 01 : How Arguments Find Their Slots
==========================================================================
 Goes deeper than Lessons 01 to 04.

 First principle
   A call is a matching game between values and slots. Python plays it
   in a fixed order, and every "strange" error message is simply the
   step of the game that failed.

 What you will learn
   1. The four steps Python follows on every call
   2. Keyword-only parameters (after a bare *)
   3. Positional-only parameters (before a /)
   4. A default value is created ONCE, when def runs
   5. An argument is another name for the SAME object (Day 3)

 Run this file :  python deep_dive_01_how_arguments_find_their_slots.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. The four steps of every call
# --------------------------------------------------------------------------
#   Step 1  positional values fill slots left to right
#   Step 2  leftover positional values go to *args (or: error)
#   Step 3  keyword values fill slots by name; unknown names go to
#           **kwargs (or: error)
#   Step 4  empty slots take their default (or: error)
def greet(name, city="Chennai"):
    return f"{name} from {city}"

print(greet("Asha"))                    # steps 1 and 4

try:
    greet("Asha", name="Ravi")          # step 1 filled name, step 3 tries again
except TypeError as error:
    print("Error:", error)

try:
    greet("Asha", town="Pune")          # step 3: no slot called town
except TypeError as error:
    print("Error:", error)

try:
    greet()                             # step 4: name has no default
except TypeError as error:
    print("Error:", error)

# --------------------------------------------------------------------------
# 2. Keyword-only: everything after a bare * must be named
# --------------------------------------------------------------------------
# The problem: transfer(500, 1001, 2002). Which account is which?
def transfer(amount, *, from_account, to_account):
    return f"{amount} from {from_account} to {to_account}"

print(transfer(500, from_account=1001, to_account=2002))

try:
    transfer(500, 1001, 2002)
except TypeError as error:
    print("Error:", error)
# The function's author forced every caller to write readable code.
# A parameter that comes after *args is keyword-only for the same reason.

# --------------------------------------------------------------------------
# 3. Positional-only: everything before a / cannot be named
# --------------------------------------------------------------------------
def square(number, /):
    return number * number

print(square(4))                        # 16
try:
    square(number=4)
except TypeError as error:
    print("Error:", error)

# Many built-ins work like this. len() never lets you write the name:
try:
    len(obj="hello")
except TypeError as error:
    print("Error:", error)
# The author stays free to rename the parameter later without
# breaking anyone's code.

# --------------------------------------------------------------------------
# 4. A default is created once, when the def line runs
# --------------------------------------------------------------------------
def add_item(item, basket=[]):          # ONE list, made here, kept forever
    basket.append(item)
    return basket

print(add_item("pen"))                  # ['pen']
print(add_item("book"))                 # ['pen', 'book']   <- surprise!
print(add_item.__defaults__)            # (['pen', 'book'],)  the stored default

# The fix: use None as the default and build a new list inside.
def add_item_fixed(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket

print(add_item_fixed("pen"))            # ['pen']
print(add_item_fixed("book"))           # ['book']
# Immutable defaults (numbers, strings, None, tuples) are always safe,
# because nobody can change them in place.

# --------------------------------------------------------------------------
# 5. A parameter is a new NAME for the caller's object
# --------------------------------------------------------------------------
def change_in_place(items):
    items.append(99)                    # changes the shared list

def point_elsewhere(items):
    items = [0, 0, 0]                   # only moves the local name

marks = [1, 2]
change_in_place(marks)
print(marks)                            # [1, 2, 99]
point_elsewhere(marks)
print(marks)                            # [1, 2, 99]   unchanged


# ==========================================================================
# THINK ABOUT IT
#   1. print(*values, sep=" ", end="\n"): why did Python's authors make
#      sep and end keyword-only? What would print("a", "b", "-") mean
#      otherwise?
#   2. Section 4: why is basket=() a safe default but basket=[] is not?
# ==========================================================================
