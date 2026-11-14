"""Syntax Quiz: a class game where every answer is a line of real Python.

Two kinds of question, both stored as plain text files in questions/:

    type: code       The player types a Python expression. The game runs it
                     and compares the result with the question's own answer.
    type: predict    The game shows some code. The player types what it prints.

Answers are stored encoded (the 'hidden' field) so nobody reads them by
accident on GitHub. Encoded is not encrypted: reveal() turns them back.

Classroom tool only: it runs whatever the player types and whatever a question
file contains. Read a question file before you merge it.
"""

import ast
import base64
import binascii
import contextlib
import difflib
import io
import os
import random
import re
import shutil
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
QUESTIONS_DIR = HERE / "questions"

FIELDS = ("type", "topic", "task", "setup", "answer", "hidden", "must_use", "code")
TRIES = 3


# ---------------------------------------------------------------- reading files

def parse_questions(text):
    """Turn the text of a question file into a list of question dicts.

    Raises ValueError with the line number when the text breaks the format.
    """
    questions, current, code_lines = [], {}, None

    def finish():
        nonlocal current, code_lines
        if code_lines is not None:
            current["code"] = "\n".join(code_lines).strip("\n")
        if current:
            questions.append(current)
        current, code_lines = {}, None

    for number, line in enumerate(text.splitlines(), start=1):
        if line.strip() == "---":
            finish()
        elif code_lines is not None:
            code_lines.append(line)
        elif not line.strip() or line.lstrip().startswith("#"):
            continue
        elif ":" not in line:
            raise ValueError(f"Line {number}: expected 'field: value', got {line.strip()!r}")
        else:
            field, value = line.split(":", 1)
            field, value = field.strip().lower(), value.strip()
            if field not in FIELDS:
                close = difflib.get_close_matches(field, FIELDS, n=1)
                hint = f" Did you mean '{close[0]}'?" if close else ""
                raise ValueError(f"Line {number}: unknown field '{field}'.{hint}")
            if field in current:
                raise ValueError(f"Line {number}: '{field}' is written twice. "
                                 "Put --- on its own line between two questions.")
            if field == "code":
                code_lines = [value] if value else []
            else:
                current[field] = value
    finish()
    if not questions:
        raise ValueError("The file has no question in it")
    return questions


@contextlib.contextmanager
def _scratch_folder():
    """Work inside a new empty folder, then remove it.

    Question code may create files. They land here, so every run starts with
    no files and nothing is left behind in the repo.
    """
    start = os.getcwd()
    folder = tempfile.mkdtemp(prefix="syntax_quiz_")
    os.chdir(folder)
    try:
        yield
    finally:
        os.chdir(start)
        shutil.rmtree(folder, ignore_errors=True)


def _run_expression(expression, setup):
    """Run the setup line, then return the value of the expression."""
    names = {}
    with _scratch_folder():
        exec(setup, names)
        return eval(expression, names)


def _run_and_capture(code):
    """Run code and return everything it printed."""
    output = io.StringIO()
    with _scratch_folder(), contextlib.redirect_stdout(output):
        exec(code, {})
    return output.getvalue()


def prepare(question):
    """Check one question and work out its expected result.

    Raises ValueError when the question is incomplete or its own answer fails.
    """
    kind = question.get("type")
    if kind not in ("code", "predict"):
        raise ValueError("'type' must be code or predict")
    question.setdefault("topic", "general")

    if kind == "code":
        if question.get("hidden") and question.get("answer"):
            raise ValueError("Use 'answer' or 'hidden', not both")
        if question.get("hidden"):
            question["answer"] = reveal(question["hidden"])
        for field in ("task", "answer"):
            if not question.get(field):
                raise ValueError(f"A code question needs '{field}'")
        question.setdefault("setup", "")
        try:
            question["expected"] = _run_expression(question["answer"], question["setup"])
        except Exception as error:
            raise ValueError(
                f"Its own answer does not run: {type(error).__name__}: {error}"
            ) from None
        words = question.get("must_use", "")
        question["must_use_words"] = [w.strip() for w in words.split(",") if w.strip()]
        for word in question["must_use_words"]:
            if not _uses(question["answer"], word):
                raise ValueError(f"must_use says '{word}' but its own answer does not use it")
    else:
        if not question.get("code"):
            raise ValueError("A predict question needs 'code' (as the last field)")
        question.setdefault("task", "What does this code print?")
        try:
            printed = _run_and_capture(question["code"])
        except Exception as error:
            raise ValueError(
                f"Its code does not run: {type(error).__name__}: {error}"
            ) from None
        if not printed.strip():
            raise ValueError("Its code prints nothing, so there is nothing to predict")
        question["expected"] = printed
    return question


def load_file(path):
    """Read one question file. Returns its questions, or raises ValueError."""
    path = Path(path)
    questions = parse_questions(path.read_text(encoding="utf-8"))
    for position, question in enumerate(questions, start=1):
        try:
            prepare(question)
        except ValueError as error:
            raise ValueError(f"Question {position}: {error}") from None
        question["source"] = path.name
    return questions


def load_questions(folder=None):
    """Read every .txt file under the questions folder.

    Returns (questions, problems). A broken file never stops the game: it is
    skipped and reported in problems as (file name, reason).
    """
    folder = Path(folder) if folder else QUESTIONS_DIR
    questions, problems = [], []
    for path in sorted(folder.rglob("*.txt")):
        try:
            questions.extend(load_file(path))
        except (ValueError, OSError, UnicodeDecodeError) as error:
            problems.append((path.name, str(error)))
    return questions, problems


def check_file(path):
    """Tell the author whether a question file is ready. Returns True or False."""
    try:
        questions = load_file(path)
    except FileNotFoundError:
        print("File not found:", path)
        return False
    except (ValueError, OSError, UnicodeDecodeError) as error:
        print("Not ready:", error)
        return False
    print(f"Ready: {len(questions)} question(s) in {Path(path).name}")
    for question in questions:
        print(f"  [{question['topic']}] {question['task']}")
    return True


def topics(questions=None):
    """Return the topic names with how many questions each has."""
    if questions is None:
        questions, _ = load_questions()
    counts = {}
    for question in questions:
        counts[question["topic"]] = counts.get(question["topic"], 0) + 1
    return dict(sorted(counts.items()))


# ---------------------------------------------------------------- hiding answers

def hide(answer):
    """Encode an answer so it cannot be read at a glance."""
    return base64.b64encode(answer.encode("utf-8")).decode("ascii")


def reveal(hidden):
    """Turn a hidden value back into the answer. Raises ValueError if it is damaged."""
    try:
        return base64.b64decode(hidden.encode("ascii"), validate=True).decode("utf-8")
    except (binascii.Error, UnicodeError):
        raise ValueError("The 'hidden' value is damaged") from None


def _swap_field(text, old, new, change):
    """Rewrite every 'old: value' line as 'new: change(value)'. Code blocks are left alone."""
    lines, in_code = [], False
    for line in text.splitlines():
        field, colon, value = line.partition(":")
        if line.strip() == "---":
            in_code = False
        elif not in_code and colon and field.strip().lower() == "code":
            in_code = True
        elif not in_code and colon and field.strip().lower() == old:
            line = f"{new}: {change(value.strip())}"
        lines.append(line)
    return "\n".join(lines) + "\n"


def hide_file(path):
    """Replace every answer in a question file with its hidden form. Returns True if done."""
    path = Path(path)
    if not check_file(path):
        print("Nothing was changed. Fix the file first.")
        return False
    text = path.read_text(encoding="utf-8")
    path.write_text(_swap_field(text, "answer", "hidden", hide), encoding="utf-8")
    print("Answers hidden in", path.name)
    return True


def reveal_file(path):
    """Facilitator: print a question file with its answers readable. Runs nothing, changes nothing."""
    text = Path(path).read_text(encoding="utf-8")
    print(_swap_field(text, "hidden", "answer", reveal), end="")


# ---------------------------------------------------------------- checking answers

def _uses(text, word):
    """True if the answer text uses this word or operator."""
    if word.replace("_", "").isalnum():
        return re.search(rf"(?<![A-Za-z0-9_]){re.escape(word)}(?![A-Za-z0-9_])", text) is not None
    return word in text


def _is_plain_value(text):
    """True if the text is just a value such as 42 or 'abc', with nothing to compute."""
    try:
        ast.literal_eval(text)
    except (ValueError, SyntaxError, MemoryError, RecursionError):
        return False
    return True


def _squash(text):
    return " ".join(text.split())


def check_answer(question, typed):
    """Mark one answer. Returns (verdict, message).

    verdict is 'right', 'wrong' or 'again'. 'again' means the answer was not
    a real attempt, so it does not use up a try.
    """
    typed = typed.strip()
    if not typed:
        return "again", "Type an answer."

    if question["type"] == "predict":
        if _squash(typed) == _squash(question["expected"]):
            return "right", "Correct."
        return "wrong", "That is not what it prints."

    if _is_plain_value(typed) and not _is_plain_value(question["answer"]):
        return "again", "That is the result. Type the Python that works it out."
    for word in question["must_use_words"]:
        if not _uses(typed, word):
            return "again", f"Use {word} in your answer."
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            result = _run_expression(typed, question["setup"])
    except SyntaxError as error:
        return "wrong", f"SyntaxError: {error.msg}"
    except Exception as error:
        return "wrong", f"{type(error).__name__}: {error}"

    expected = question["expected"]
    if result == expected and type(result) is type(expected):
        return "right", "Correct."
    if result == expected:
        return "wrong", (f"Right value, wrong type: you gave {type(result).__name__}, "
                         f"expected {type(expected).__name__}.")
    if typed.startswith("print(") and result is None:
        return "wrong", "Leave out print. Type only the expression."
    return "wrong", f"Your code gave {result!r}."


# ---------------------------------------------------------------- playing

def show(question, say=print):
    say(f"[{question['topic']}] {question['task']}")
    if question["type"] == "predict":
        for line in question["code"].splitlines():
            say("    " + line)
        if len(question["expected"].splitlines()) > 1:
            say("  (It prints more than one line. Type them on one line with a space between.)")
    elif question["setup"]:
        say("    Already done for you:  " + question["setup"])


def ask(question, read=input, say=print):
    """Ask one question. Returns points: 3, 2 or 1 by number of tries, else 0."""
    show(question, say)
    tries = 0
    while tries < TRIES:
        verdict, message = check_answer(question, read(">>> "))
        if verdict == "again":
            say("  " + message)
            continue
        tries += 1
        if verdict == "right":
            points = TRIES + 1 - tries
            say(f"  {message} +{points}")
            return points
        say(f"  {message} Tries left: {TRIES - tries}")
    if question["type"] == "predict":
        say("  It prints: " + _squash(question["expected"]))
    else:
        say("  One answer: " + question["answer"])
    return 0


def play(count=10, topic=None, questions=None, read=input, say=print):
    """Play a round. Returns (points, best possible points)."""
    if questions is None:
        questions, problems = load_questions()
        for name, reason in problems:
            say(f"Skipped {name}: {reason}")
    if topic:
        questions = [q for q in questions if q["topic"] == topic]
    if not questions:
        say("No questions found.")
        return 0, 0
    chosen = random.sample(questions, min(count, len(questions)))
    points = 0
    for number, question in enumerate(chosen, start=1):
        say(f"\nQuestion {number} of {len(chosen)}")
        points += ask(question, read, say)
    best = TRIES * len(chosen)
    say(f"\nScore: {points} out of {best}")
    return points, best
