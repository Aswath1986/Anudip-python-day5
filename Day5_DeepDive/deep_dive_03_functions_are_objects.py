"""
==========================================================================
 Day 5 | Deep Dive 03 : Functions Are Objects
==========================================================================
 Goes deeper than Lesson 06.

 First principle
   Day 3: everything in Python is an object with a value, a type and an
   identity, and a variable is only a name pointing at it.
   A function is an object too. "def greet" builds a function object and
   points the name greet at it. Once you see that, lambda, sorted(key=...),
   map and filter stop being special.

 What you will learn
   1. A function has a type and an id, like any object
   2. Two names, one function
   3. Functions inside lists and dicts
   4. A function as an argument
   5. A function that builds functions (closure)
   6. lambda makes the same kind of object as def
   7. A classic trap: lambdas made in a loop

 Run this file :  python deep_dive_03_functions_are_objects.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. A function is an object
# --------------------------------------------------------------------------
def greet(name):
    return f"Hello {name}"

print(type(greet))                      # <class 'function'>
print(greet.__name__)                   # greet
# greet   -> the function object itself
# greet() -> CALL it and get its result

# --------------------------------------------------------------------------
# 2. Two names, one function
# --------------------------------------------------------------------------
say_hello = greet                       # no brackets: nothing is called
print(say_hello("Asha"))                # Hello Asha
print(say_hello is greet)               # True

# --------------------------------------------------------------------------
# 3. Functions can sit inside lists and dicts
# --------------------------------------------------------------------------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

calculator = {"+": add, "-": subtract}  # a menu of actions
print(calculator["+"](8, 3))            # 11
print(calculator["-"](8, 3))            # 5
# This replaces a long if / elif chain. Adding a new operation is one line.

# --------------------------------------------------------------------------
# 4. A function as an argument
# --------------------------------------------------------------------------
def apply_twice(action, value):
    return action(action(value))

def add_ten(n):
    return n + 10

print(apply_twice(add_ten, 5))          # 25
print(apply_twice(str.upper, "hi"))     # HI
# sorted(key=...), map and filter all work exactly like apply_twice:
# they receive your function and call it for you.

# --------------------------------------------------------------------------
# 5. A function that builds functions
# --------------------------------------------------------------------------
def make_multiplier(factor):
    def multiply(n):
        return n * factor               # remembers factor from outside
    return multiply                     # hand back the function, not a number

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(10), triple(10))           # 20 30
# The inner function keeps the value of factor it was born with.
# This is called a closure.

# --------------------------------------------------------------------------
# 6. lambda builds the same kind of object
# --------------------------------------------------------------------------
square = lambda x: x * x
print(type(square))                     # <class 'function'>
print(square.__name__)                  # <lambda>   (it has no name of its own)
# def = build a function AND give it a name.
# lambda = build a function only. That is the whole difference.

# --------------------------------------------------------------------------
# 7. The trap: lambdas made in a loop
# --------------------------------------------------------------------------
actions = []
for i in range(3):
    actions.append(lambda: i)           # each lambda says "look up i later"

print(actions[0](), actions[1](), actions[2]())     # 2 2 2   <- not 0 1 2
# All three look up the SAME name i, and the loop left it at 2.

# The fix: a default argument stores the value at creation time.
actions = []
for i in range(3):
    actions.append(lambda i=i: i)

print(actions[0](), actions[1](), actions[2]())     # 0 1 2


# ==========================================================================
# THINK ABOUT IT
#   1. What is the difference between   x = greet   and   x = greet("A") ?
#   2. In section 3, how would you add multiplication to the calculator
#      with a lambda, in one line?
#   3. Section 7 is fixed with a default argument. Which section of
#      Deep Dive 01 explains why that works?
# ==========================================================================
