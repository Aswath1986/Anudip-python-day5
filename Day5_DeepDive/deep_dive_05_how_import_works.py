"""
==========================================================================
 Day 5 | Deep Dive 05 : How import Works
==========================================================================
 Goes deeper than Lessons 08 and 09.

 First principle
   import is not magic. It does three plain things:
     1. FIND a file with that name
     2. RUN that file from top to bottom, once
     3. Give you a NAME that points to the result (a module object)
   Every question about import is answered by one of these three steps.

 What you will learn
   1. Step 2: the file really runs, and only once
   2. Step 3: a module is an object, shared by everyone who imports it
   3. Step 1: where Python searches
   4. Where the standard library and pip libraries live
   5. Two import styles to avoid

 This file uses noisy_module.py from this folder.

 Run this file :  python deep_dive_05_how_import_works.py
==========================================================================
"""
import sys

# --------------------------------------------------------------------------
# 1. import RUNS the file, once
# --------------------------------------------------------------------------
print("first import:")
import noisy_module                     # its print line appears now

print("second import:")
import noisy_module                     # nothing is printed

# Python keeps every loaded module in a dict called sys.modules.
# On import it looks there first, and runs the file only if it is missing.
print("noisy_module" in sys.modules)    # True

# --------------------------------------------------------------------------
# 2. A module is an object, and everyone shares the same one
# --------------------------------------------------------------------------
print(type(noisy_module))               # <class 'module'>

import noisy_module as other_name
print(other_name is noisy_module)       # True: two names, one object

print(noisy_module.bump())              # 1
print(other_name.bump())                # 2   the same counter went up
# Day 3 again: a module is a mutable object reached through names.

# --------------------------------------------------------------------------
# 3. Where does Python search? sys.path, in order
# --------------------------------------------------------------------------
print("Python searches", len(sys.path), "places. The first is this file's folder.")
# First match wins. So if YOU create a file called random.py or math.py
# next to your program, "import random" finds YOUR file, not Python's.
# Never give your file the name of a library you use.

try:
    import a_module_that_does_not_exist
except ModuleNotFoundError as error:
    print("Error:", error)
# This is the error you see when a library is not installed, or when the
# file name is misspelt.

# --------------------------------------------------------------------------
# 4. Where libraries live
# --------------------------------------------------------------------------
import json                             # standard library: a .py file on disk
print(json.__file__.endswith("__init__.py"))    # True: json is a package (a folder)

print(noisy_module.__file__.endswith("noisy_module.py"))    # True: one file

print(sys.executable)                   # the Python that is running this file
# pip install puts third-party libraries in a folder named site-packages
# that belongs to THIS Python. If you have two Pythons installed, a
# library installed for one is invisible to the other. Use
#     python -m pip install name
# to be sure pip and python are the same one.

# --------------------------------------------------------------------------
# 5. Two styles to avoid
# --------------------------------------------------------------------------
# (a) from math import *
#     Pours every name from math into your file. You can no longer tell
#     where a name came from, and it can silently replace your own names.
#
# (b) import inside the middle of a file
#     Works, but readers expect all imports at the top, where one glance
#     shows what the program depends on.


# ==========================================================================
# THINK ABOUT IT
#   1. Why does Python run a module only once, even if ten files
#      import it? Think about speed, and about the counter in section 2.
#   2. A student saves their practice file as random.py and then
#      random.randint stops working. Which step of import went wrong?
#   3. shop_tools.py (Lesson 08) hides its tests under
#      if __name__ == "__main__":  What would happen on import without it?
# ==========================================================================
