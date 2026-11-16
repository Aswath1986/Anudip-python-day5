"""
==========================================================================
 Day 5 | Deep Dive 02 : The Call Stack and Recursion
==========================================================================
 Goes deeper than Lesson 05.

 First principle
   When a function calls another, the caller must WAIT and remember
   where it was. Python keeps these waiting calls in a pile: the
   CALL STACK. Recursion is nothing special: it is the same pile,
   with the same function on it many times.

 What you will learn
   1. Watching the stack grow and shrink
   2. Every call has its own private variables
   3. The stack has a limit, and why
   4. Recursion can repeat work: counting the calls of fibonacci
   5. Remembering answers (memoization)

 Run this file :  python deep_dive_02_the_call_stack_and_recursion.py
==========================================================================
"""
import sys
from functools import lru_cache

# --------------------------------------------------------------------------
# 1. Watching the stack
# --------------------------------------------------------------------------
def factorial(n, depth=0):
    indent = "    " * depth
    print(f"{indent}factorial({n}) starts")
    if n <= 1:
        print(f"{indent}factorial({n}) returns 1")
        return 1
    answer = n * factorial(n - 1, depth + 1)
    print(f"{indent}factorial({n}) returns {answer}")
    return answer

factorial(4)
# Read the output from top to bottom. The calls pile up going right,
# then finish in the OPPOSITE order: last in, first out.

# --------------------------------------------------------------------------
# 2. Every call has its own variables
# --------------------------------------------------------------------------
def show(n):
    label = f"call with n={n}"          # a separate 'label' for every call
    if n > 0:
        show(n - 1)
    print(label)                        # still intact after the inner calls

show(2)
# The inner calls did not overwrite the outer call's 'label'. Each call
# gets its own box of local names, called a frame.

# --------------------------------------------------------------------------
# 3. The pile has a limit
# --------------------------------------------------------------------------
print("Limit:", sys.getrecursionlimit())        # usually 1000

def depth_reached(n):
    try:
        return depth_reached(n + 1)
    except RecursionError:
        return n

print("Stopped near depth", depth_reached(1))
# Every waiting call uses memory. Python stops a runaway recursion with a
# clear error before the operating system has to stop the whole program.

# A loop has no such limit, because nothing is waiting:
total = 0
for number in range(1, 100001):
    total += number
print(total)                            # 5000050000

# --------------------------------------------------------------------------
# 4. Recursion can repeat the same work
# --------------------------------------------------------------------------
# Fibonacci: each number is the sum of the two before it. 0 1 1 2 3 5 8 ...
calls = 0

def fib(n):
    global calls
    calls += 1
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(20), "found with", calls, "calls")    # 6765 found with 21891 calls
# fib(20) asks for fib(18) twice, fib(17) three times, fib(16) five times...

# --------------------------------------------------------------------------
# 5. Remember the answers: memoization
# --------------------------------------------------------------------------
calls = 0
memory = {}

def fib_memo(n):
    global calls
    calls += 1
    if n in memory:                     # seen before? answer at once
        return memory[n]
    if n < 2:
        return n
    memory[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memory[n]

print(fib_memo(20), "found with", calls, "calls")   # 6765 found with 39 calls

# The standard library does this for you in one line:
@lru_cache(maxsize=None)
def fib_fast(n):
    if n < 2:
        return n
    return fib_fast(n - 1) + fib_fast(n - 2)

print(fib_fast(80))                     # 23416728348467685, instantly


# ==========================================================================
# THINK ABOUT IT
#   1. In section 1, which call finishes first: factorial(4) or
#      factorial(1)? Which one started first?
#   2. When would you choose recursion even though a loop is possible?
#      Think about the nested box in Lesson 05.
#   3. memory is a dict. Why must its keys be immutable (Day 3)?
# ==========================================================================
