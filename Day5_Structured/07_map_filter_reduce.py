"""
==========================================================================
 Day 5 | Lesson 07 : map, filter, reduce
==========================================================================
 First principle
   Almost every loop over a list does one of three jobs:
     CHANGE every item          -> map
     KEEP only some items       -> filter
     COMBINE all into one value -> reduce
   These three functions name the job, so the reader does not have to
   read the whole loop to find out which one it is.

 What you will learn
   1. map    - the loop way, then the map way
   2. filter - the loop way, then the filter way
   3. reduce - the loop way, then the reduce way
   4. Chaining all three

 Run this file :  python 07_map_filter_reduce.py
==========================================================================
"""
from functools import reduce            # reduce lives in a module (Lesson 08)

marks = [35, 72, 48, 90, 66]

# --------------------------------------------------------------------------
# 1. map - CHANGE every item.   5 items in -> 5 items out
# --------------------------------------------------------------------------
# The loop way: add 5 grace marks to everyone
with_grace = []
for m in marks:
    with_grace.append(m + 5)
print(with_grace)                       # [40, 77, 53, 95, 71]

# The map way: map(function, list)
with_grace = list(map(lambda m: m + 5, marks))
print(with_grace)                       # [40, 77, 53, 95, 71]

# map gives back a "map object" that produces items when asked.
# list(...) asks for all of them.
print(map(lambda m: m + 5, marks))      # <map object at 0x...>

# Any function works, not only lambdas:
print(list(map(str, marks)))            # ['35', '72', '48', '90', '66']
print(list(map(len, ["hi", "hello"])))  # [2, 5]

# --------------------------------------------------------------------------
# 2. filter - KEEP some items.   5 items in -> 0 to 5 items out
# --------------------------------------------------------------------------
# The loop way: who passed (40 or more)?
passed = []
for m in marks:
    if m >= 40:
        passed.append(m)
print(passed)                           # [72, 48, 90, 66]

# The filter way: the function must answer True or False
passed = list(filter(lambda m: m >= 40, marks))
print(passed)                           # [72, 48, 90, 66]

# --------------------------------------------------------------------------
# 3. reduce - COMBINE into one.   5 items in -> 1 value out
# --------------------------------------------------------------------------
# The loop way: total marks
total = 0
for m in marks:
    total = total + m
print(total)                            # 311

# The reduce way: the function takes (answer so far, next item)
total = reduce(lambda so_far, m: so_far + m, marks)
print(total)                            # 311

# Step by step:  35+72=107   107+48=155   155+90=245   245+66=311

highest = reduce(lambda a, b: a if a > b else b, marks)
print(highest)                          # 90
# For common jobs Python already has sum(), max(), min(). Use those first.

# --------------------------------------------------------------------------
# 4. Chaining: total of the passing marks after grace
# --------------------------------------------------------------------------
after_grace = map(lambda m: m + 5, marks)               # change
passing = filter(lambda m: m >= 40, after_grace)        # keep
answer = reduce(lambda a, b: a + b, passing)            # combine
print(answer)                           # 336


# ==========================================================================
# PREDICT before you run!
#
#   nums = [1, 2, 3, 4]
#   print(list(map(lambda n: n * n, nums)))
#   print(list(filter(lambda n: n % 2 == 0, nums)))
#   print(reduce(lambda a, b: a * b, nums))
#
# TRY IT YOURSELF
#   prices = [120, 45, 300, 80]
#   1. Use map to add 18% tax to every price.
#   2. Use filter to keep prices above 100.
#   3. Use reduce to find the total of all prices.
#   4. Write task 1 again with a plain for loop. Which reads better to you?
# ==========================================================================
