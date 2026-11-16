# Day 5 – Deep Dive Sessions

Take these **after** the structured lessons, in your own time. Each deep dive picks one idea
from class and rebuilds it from first principles, so you see *why* Python behaves that way.

| # | File | Goes deeper into | Key ideas |
|---|------|------------------|-----------|
| 01 | `deep_dive_01_how_arguments_find_their_slots.py` | Lessons 01–04 | the four steps of every call, keyword-only (`*`), positional-only (`/`), the mutable default trap, arguments as shared objects |
| 02 | `deep_dive_02_the_call_stack_and_recursion.py` | Lesson 05 | watching the call stack, frames, the recursion limit, repeated work in Fibonacci, memoization, `lru_cache` |
| 03 | `deep_dive_03_functions_are_objects.py` | Lesson 06 | functions as values, a dict of functions, closures, `lambda` vs `def`, the loop-lambda trap |
| 04 | `deep_dive_04_building_map_filter_reduce.py` | Lesson 07 | writing `my_map`, `my_filter`, `my_reduce`, lazy objects, list comprehensions |
| 05 | `deep_dive_05_how_import_works.py` | Lessons 08–09 | find, run once, bind a name; `sys.modules`, `sys.path`, where `pip` installs, naming your file `random.py` |

`noisy_module.py` is imported by Deep Dive 05. Keep it in this folder.

Every file ends with **THINK ABOUT IT** questions. Several of them connect back to Day 3
(objects, names and mutability), because the same ideas explain functions and modules too.

> Exact error messages, the recursion limit and file paths can differ between Python versions
> and computers. The behaviour does not.

```bash
cd Day5_DeepDive
python deep_dive_01_how_arguments_find_their_slots.py
```
