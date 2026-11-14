# Syntax Quiz: facilitator run sheet

Total time: about 1 hour 50 minutes. Students follow `01_syntax_quiz.ipynb`
from top to bottom.

**The story to tell:** "A quiz app is only as good as its questions. The app is
written. The questions come from you. By the end of today the class plays a
game it built together."

## Before class (10 minutes)

1. Open the notebook and play one round yourself.
2. Pick two starter questions to demonstrate on the projector: one `code`, one `predict`.
3. Check every student has forked and cloned the repo, or plan time for it in the first block.

## In class

| Time | Part | You | Students |
|---|---|---|---|
| 0:00-0:10 | Story and demo | Tell the story. Answer one question on the projector and get it wrong on purpose, so they see an error message is help, not failure. | Watch, laptops closed |
| 0:10-0:25 | Part 0 and 1: warm-up round | Walk the room. Do not give answers; point at the error message and ask what it says. | Play 5 questions in pairs |
| 0:25-0:35 | Part 2: weak topic | Ask each pair which topic they chose and why. Note the popular ones for your next revision. | Play 5 questions on one topic |
| 0:35-0:45 | Part 3: the question file | Ask for the prediction first. Link it to last week's file operations. | Open a question file and read the format table |
| 0:45-1:00 | Part 4: the crash | Let the crash happen before you explain anything. Then ask: "Thirty players are waiting because of one typo. What do we need?" | See the crash, write `safe_load` with try and except |
| 1:00-1:10 | Break | | |
| 1:10-1:30 | Part 5: write a question | Push them to pick something they found hard last week. Send back any question whose task is unclear. | Write, check and test a question on their partner, then hide the answer |
| 1:30-1:40 | Part 6: pull request | Pause everyone at `git status` and ask what it shows. | Branch, commit, push, open a pull request |
| 1:40-1:50 | Part 7: tournament | Merge pull requests on the projector, reading each question aloud first: this is code review. Then start the tournament. | Pull, see the question count grow, play 15 questions |

Close with the four "Think about it" questions if time allows; otherwise open
the next session with them.

## Things to hold back

- Do not warn them that Part 4 will crash.
- Do not show the `safe_load` answer. One working answer:

```python
def safe_load(path):
    try:
        return simple_load(path)
    except ValueError as error:
        print("Skipped", path, "-", error)
        return []
```

## Where time will slip

- **Fork, clone and pull requests.** Pair a confident student with a slower one.
- **Merging.** With a large class, merge five or six pull requests live and the rest after class. The tournament works with whatever is merged; the full set can open the next session.
- **If you are behind at the break,** skip Part 2. Nothing later depends on it.

## Before you merge a pull request

The game runs the answer, `setup` and `code` lines of every question file, so
read each file before merging, and merge only files under
`SyntaxQuiz/questions/students/`.

Answers arrive hidden, so the pull request page shows a line such as
`hidden: bGVuKHdvcmQp`. To read the real answer, copy that value from the page
and run this in a notebook cell:

```python
import quiz
quiz.reveal("bGVuKHdvcmQp")
```

For a file already on your laptop, `quiz.reveal_file("questions/students/asha.txt")`
prints the whole file with answers readable. Neither command runs the answer.

A file with a mistake does not break the game: it is skipped and listed when
the questions load.

## About the hidden answers

The answers are encoded with Base64, not encrypted. This stops students
reading them by accident on GitHub; it does not stop a student who studies
`quiz.py`. Predict questions cannot be hidden at all, because running the shown
code gives the answer. Keep `quiz.reveal` to yourself until the tournament is
over, then use "Think about it" question 4 to let them discover that encoded is
not encrypted.

## After class

Each student file is named after its author, so the `students` folder shows who
contributed. The topics students chose in Part 2 and wrote about in Part 5 tell
you what to revise.
