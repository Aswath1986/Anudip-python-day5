# Day 5 lesson plan: functions in depth, modules and libraries

For the facilitator. Total time: about 2 hours 30 minutes including a break.
Students follow the files in [`Day5_Structured`](Day5_Structured); the
[`Day5_DeepDive`](Day5_DeepDive) folder is for self-study afterwards.

## The first-principles method, light version

For every topic, ask three questions in this order. Do not show syntax until
the class has answered the first one.

1. **What is the problem?** Show code that is awkward or impossible without the feature.
2. **What is the smallest idea that fixes it?** Say it in one plain sentence.
3. **What does it look like in Python?** Only now show the syntax, and predict before running.

Each structured lesson opens with a "First principle" paragraph that gives you
questions 1 and 2 ready to read out.

## Timings

| Time | Lesson | Ask the class first | Then |
|---|---|---|---|
| 0:00–0:10 | Recap | "Why do we write functions at all?" Collect answers: reuse, naming, one place to fix. | State today's thread: every topic is a way to reuse more with less typing. |
| 0:10–0:25 | 01 Parameters and arguments | "`greet('Chennai', 'Asha')` gives no error. How could Python have known?" | Positional, keyword, the mixing rule. Run the two error cases and read the messages aloud. |
| 0:25–0:35 | 02 Default arguments | "Ninety of our hundred students are from Chennai. Must we type it ninety times?" | Defaults, overriding by keyword, `print(sep, end)` as something they already use. |
| 0:35–0:50 | 03 `*args` | "Write `add` for 2 numbers. Now 3. Now 50. What is wrong with this approach?" | `*args` as one slot that collects; it is a tuple; `*` at the call unpacks. |
| 0:50–1:05 | 04 `**kwargs` | "A student form has name, then any other details. How do we accept details we did not plan for?" | `**kwargs` is a dict; all four kinds in one `def`; `**` at the call. |
| 1:05–1:15 | Break | | |
| 1:15–1:35 | 05 Recursion | Act it out: hand a "countdown from 3" card to one student, who says 3 and hands "countdown from 2" to the next. Ask: "Who finishes first?" | Base case and recursive case; factorial trace; the no-base-case crash; the nested box. |
| 1:35–1:50 | 06 Lambda | "Sort these names by their last letter. `sorted` needs a function. Is it worth a `def`?" | `lambda` shape; `sorted` and `max` with `key`. Stress: one expression only, readable beats short. |
| 1:50–2:05 | 07 map, filter, reduce | Write three loops on the board (add 5 to each, keep the passes, total). "What is the one-word job of each loop?" | Change, keep, combine. Loop way first, then the function way, every time. |
| 2:05–2:20 | 08 Modules and 09 Libraries | "You wrote `add_gst` yesterday. Today another program needs it. What do you do?" Let someone say copy-paste, then ask what happens when a bug is found. | `import` three ways, `__name__`. Then a five-minute tour of `math`, `random`, `datetime`, and what `pip install` does. |
| 2:20–2:30 | 10 Mini project and close | "Find each of today's ideas in this one file." | Students point to the line for each idea. Assign TRY IT YOURSELF and the deep dives. |

## How to run each lesson

1. Read the First principle paragraph aloud and ask the question from the table.
2. Students run the file and read the output against the comments.
3. Do the **PREDICT** block together: hands up for each answer before anyone runs it.
4. Leave **TRY IT YOURSELF** for pair practice or homework.

## Where time will slip

- **`*args` and `**kwargs`** take the longest for non-technical students. Keep saying
  "one star collects values into a tuple, two stars collect named values into a dict".
- **Recursion** is the hardest idea of the day. The acted-out countdown is worth its five minutes.
  If the class is lost, stop after factorial and leave the nested box for the deep dive.
- **If you are 15 minutes behind at the break,** teach `map` and `filter` only and leave `reduce`
  as reading, then shorten the library tour to `math` and `random`.

## Common mistakes to watch for

| Students write | What to ask them |
|---|---|
| `greet(name="Asha", "Chennai")` | "After a keyword, how would Python count positions?" |
| `def f(a=1, b):` | "If I call `f(5)`, is 5 for `a` or for `b`?" |
| `total(marks)` instead of `total(*marks)` | "How many arguments did you pass: one list, or three numbers?" |
| A recursive function with no base case | "When does this stop?" |
| `print(map(...))` showing `<map object>` | "It is waiting to be asked. What asks for all the items?" |
| A practice file saved as `random.py` or `math.py` | "Which `random` will `import random` find first?" |

## Self-study: the deep dives

| Deep dive | Follow-up to | Why a student would open it |
|---|---|---|
| 01 How arguments find their slots | Lessons 01–04 | To read any `TypeError` from a function call and know which step failed |
| 02 The call stack and recursion | Lesson 05 | To see the waiting calls, and why slow recursion can be made fast |
| 03 Functions are objects | Lesson 06 | To connect functions to Day 3: a function is an object behind a name |
| 04 Building map, filter and reduce | Lesson 07 | To write the three tools from plain loops |
| 05 How import works | Lessons 08–09 | To fix "No module named ..." without help |

## Checking understanding

Ask these at the close or at the start of the next session. A student who can
answer in plain words has understood the principle, not just the syntax.

1. What is the difference between a parameter and an argument?
2. Inside a function, what type is `args`? What type is `kwargs`?
3. What two parts must every recursive function have?
4. When would you write a `lambda` and when a `def`?
5. Which of `map`, `filter`, `reduce` always returns the same number of items it received?
6. What are the three things `import` does?
