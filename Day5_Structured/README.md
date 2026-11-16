# Day 5 – Structured Lessons

**Topic: functions in depth, then modules and libraries.**
Go through the files **in number order**. Each lesson uses only what the lessons before it taught.

Every lesson opens with a **First principle**: the problem that made the feature necessary.
Read it before the code. If you can say the problem in your own words, the syntax is easy to remember.

| # | File | Concept | The problem it solves |
|---|------|---------|-----------------------|
| 01 | `01_parameters_and_arguments.py` | parameter vs argument, positional, keyword | Which value goes into which slot? |
| 02 | `02_default_arguments.py` | default values, `print(sep, end)` | The caller repeats the same value every time |
| 03 | `03_args_any_number_of_positionals.py` | `*args`, unpacking with `*` | The number of inputs is not known in advance |
| 04 | `04_kwargs_any_number_of_keywords.py` | `**kwargs`, unpacking with `**`, order of parameters | Extra inputs that need names |
| 05 | `05_recursion.py` | base case, recursive case, `RecursionError` | A problem that contains a smaller copy of itself |
| 06 | `06_lambda_functions.py` | `lambda`, `sorted(key=...)`, `max(key=...)` | A tiny function that is needed only once |
| 07 | `07_map_filter_reduce.py` | `map`, `filter`, `functools.reduce` | Naming the three jobs every loop does |
| 08 | `08_modules.py` | `import`, `from ... import`, `as`, `__name__` | Reusing a function in more than one program |
| 09 | `09_libraries.py` | standard library, `dir()`, `pip`, PyPI | Someone has already solved this |
| 10 | `10_mini_project_canteen_bill.py` | everything above in one program | Putting it together |

`shop_tools.py` is a small module that Lessons 08 and 10 import. Keep it in this folder.

## How each lesson is laid out

1. **First principle**: the problem, in plain words.
2. **What you will learn**: the goals for the lesson.
3. **Numbered sections**: short explanations followed by code you can run.
4. **PREDICT before you run!**: write down what you expect, then check by running it.
5. **TRY IT YOURSELF**: small exercises to practise.

## Running a lesson

```bash
cd Day5_Structured
python 01_parameters_and_arguments.py
```

Lesson 09 prints a random dice roll and a random name, so those two lines change on every run.

When you finish, go on to the deep dives in [`../Day5_DeepDive`](../Day5_DeepDive).
The facilitator's timings are in [`../LESSON_PLAN.md`](../LESSON_PLAN.md).
