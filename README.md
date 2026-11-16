# Anudip-python-day5
Covering all concepts with story method and strong industry use case

## Day 5 lessons: functions in depth, modules and libraries

| Path | What it is |
|------|------------|
| [`LESSON_PLAN.md`](LESSON_PLAN.md) | Facilitator plan: timings, the question to ask before each topic, common mistakes |
| [`Day5_Structured/`](Day5_Structured) | 10 numbered lessons with PREDICT and TRY IT YOURSELF: arguments, defaults, `*args`, `**kwargs`, recursion, lambda, map/filter/reduce, modules, libraries, mini project |
| [`Day5_DeepDive/`](Day5_DeepDive) | 5 first-principles deep dives for self-study |

Suggested order: structured lessons 01 → 10 in class, deep dives 01 → 05 in your own time, then the Syntax Quiz below.

## SyntaxQuiz: the class builds a game, then plays it

A quiz where every answer is a line of real Python that the game runs. Each
student adds one question through a pull request, then the whole class plays
the combined set. It revises Week 1 syntax by typing it, and gives file
operations, try/except and the fork-and-pull-request flow a visible purpose.

| File | What it is |
|---|---|
| `SyntaxQuiz/STUDENT_SETUP.md` | Students start here: fork, clone and open the notebook |
| `SyntaxQuiz/01_syntax_quiz.ipynb` | The student lab |
| `SyntaxQuiz/RUN_SHEET.md` | Facilitator timings and what to say when |
| `SyntaxQuiz/quiz.py` | The game engine |
| `SyntaxQuiz/questions/` | 112 starter questions on Week 1; student questions go in `students/` |
| `SyntaxQuiz/broken_examples/` | A question file with a typo, used for the try/except lesson |

Answers in the question files are stored encoded, so students cannot read
them at a glance on GitHub; `RUN_SHEET.md` explains how the facilitator reveals
them for review.

Needs only Python and Jupyter, nothing to install. The game runs the code in
question files and in players' answers, so it is a classroom tool: read a
question file before merging it.
