"""
==========================================================================
 Day 5 | Lesson 08 : Modules
==========================================================================
 First principle
   A function saves you from writing the same lines twice in one file.
   But what about the same function in two different programs?
   Copy-paste means fixing every bug twice.
   A MODULE is a .py file whose functions other files can borrow.

 What you will learn
   1. A module is just a .py file
   2. import module           -> use module.name
   3. from module import name -> use name directly
   4. import module as short  -> a nickname
   5. __name__ and "if __name__ == '__main__':"

 This lesson uses shop_tools.py from this folder. Open it first.

 Run this file :  python 08_modules.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. import module - bring in the whole file, use it with a dot
# --------------------------------------------------------------------------
import shop_tools

print(shop_tools.add_gst(100))          # 105.0
print(shop_tools.apply_discount(200))   # 180.0
print(shop_tools.GST_RATE)              # 5   (variables come along too)

# The dot says where the name lives. Two modules can both have a function
# called add_gst and they will never be mixed up.

# --------------------------------------------------------------------------
# 2. from module import name - bring in one name, use it without the dot
# --------------------------------------------------------------------------
from shop_tools import add_gst

print(add_gst(200))                     # 210.0

# --------------------------------------------------------------------------
# 3. import module as nickname
# --------------------------------------------------------------------------
import shop_tools as st

print(st.apply_discount(1000, percent=25))      # 750.0

# --------------------------------------------------------------------------
# 4. Python comes with modules too
# --------------------------------------------------------------------------
import math

print(math.sqrt(49))                    # 7.0
print(math.pi)                          # 3.141592653589793

# --------------------------------------------------------------------------
# 5. __name__ - "am I the main program, or was I imported?"
# --------------------------------------------------------------------------
print(__name__)                         # __main__   (this file was run directly)
print(shop_tools.__name__)              # shop_tools (that file was imported)

# Look at the bottom of shop_tools.py. Its test lines sit under
#     if __name__ == "__main__":
# so they did NOT print when we imported it here.
# Now run   python shop_tools.py   and they DO print.
# One file, two roles: a tool for others, and a program that tests itself.


# ==========================================================================
# PREDICT before you run!
#   (make a file called helper.py with the first three lines)
#
#   # helper.py
#   print("helper loaded")
#   def double(n):
#       return n * 2
#
#   # main.py
#   import helper
#   import helper
#   print(helper.double(4))
#
#   How many times is "helper loaded" printed?
#
# TRY IT YOURSELF
#   1. Create my_tools.py with a function is_even(n).
#   2. In another file, import it in all three ways and call it.
#   3. Add a test under if __name__ == "__main__": in my_tools.py.
#      Run both files and compare what is printed.
# ==========================================================================
