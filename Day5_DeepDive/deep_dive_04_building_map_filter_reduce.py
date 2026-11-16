"""
==========================================================================
 Day 5 | Deep Dive 04 : Building map, filter and reduce Yourself
==========================================================================
 Goes deeper than Lesson 07.

 First principle
   You understand a tool when you can build it. map, filter and reduce
   are each a for loop of about four lines that receives a function.
   We build them, then look at the one thing the real ones do
   differently: they are lazy.

 What you will learn
   1. my_map, my_filter, my_reduce from plain loops
   2. reduce with a starting value
   3. The real map and filter are lazy: they work only when asked
   4. A lazy object can be used only once
   5. map over two lists at once
   6. The same jobs as list comprehensions

 Run this file :  python deep_dive_04_building_map_filter_reduce.py
==========================================================================
"""
from functools import reduce

marks = [35, 72, 48, 90]

# --------------------------------------------------------------------------
# 1. Build them
# --------------------------------------------------------------------------
def my_map(action, items):
    result = []
    for item in items:
        result.append(action(item))     # CHANGE every item
    return result

def my_filter(test, items):
    result = []
    for item in items:
        if test(item):                  # KEEP if the test says True
            result.append(item)
    return result

def my_reduce(combine, items):
    so_far = items[0]
    for item in items[1:]:
        so_far = combine(so_far, item)  # COMBINE with the answer so far
    return so_far

print(my_map(lambda m: m + 5, marks))               # [40, 77, 53, 95]
print(my_filter(lambda m: m >= 40, marks))          # [72, 48, 90]
print(my_reduce(lambda a, b: a + b, marks))         # 245

print(my_map(lambda m: m + 5, marks) == list(map(lambda m: m + 5, marks)))  # True

# --------------------------------------------------------------------------
# 2. reduce with a starting value
# --------------------------------------------------------------------------
try:
    reduce(lambda a, b: a + b, [])      # nothing to start from
except TypeError as error:
    print("Error:", error)

print(reduce(lambda a, b: a + b, [], 0))            # 0    starts from 0
print(reduce(lambda a, b: a + b, marks, 1000))      # 1245 starts from 1000

# The starting value can be a different type from the items:
words = ["pen", "book", "bag"]
print(reduce(lambda count, word: count + len(word), words, 0))  # 10

# --------------------------------------------------------------------------
# 3. The real map is lazy
# --------------------------------------------------------------------------
def noisy_double(n):
    print("  doubling", n)
    return n * 2

lazy = map(noisy_double, [1, 2, 3])
print("map was called, nothing has been doubled yet")
print(next(lazy))                       # only now "doubling 1" appears, then the answer 2
print("the rest:", list(lazy))          # "doubling 2", "doubling 3", then [4, 6]
# Why lazy? With a million items, map does not build a million-item list
# in memory. It hands over one answer at a time.

# --------------------------------------------------------------------------
# 4. A lazy object is used up after one pass
# --------------------------------------------------------------------------
passed = filter(lambda m: m >= 40, marks)
print(list(passed))                     # [72, 48, 90]
print(list(passed))                     # []   <- already used up
# Keep the result by storing list(...) in a name.

# --------------------------------------------------------------------------
# 5. map over two lists at once
# --------------------------------------------------------------------------
theory = [40, 35, 45]
practical = [45, 30, 50]
print(list(map(lambda t, p: t + p, theory, practical)))     # [85, 65, 95]

# --------------------------------------------------------------------------
# 6. The same jobs as list comprehensions
# --------------------------------------------------------------------------
# Many Python programmers write map and filter like this instead:
print([m + 5 for m in marks])                   # map
print([m for m in marks if m >= 40])            # filter
print([m + 5 for m in marks if m >= 40])        # both at once
print(sum(marks))                               # the common reduce
# Both styles are correct. Read both; write the one your team uses.


# ==========================================================================
# THINK ABOUT IT
#   1. my_reduce crashes on an empty list. Add a third parameter 'start'
#      so that it does not.
#   2. Our my_map builds the whole list at once. For 5 items, does that
#      matter? For 50 million?
#   3. Can you write my_map using my_reduce? (Hint: start with [] and
#      let combine append to it.)
# ==========================================================================
