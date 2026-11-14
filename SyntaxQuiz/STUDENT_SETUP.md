# Syntax Quiz: student setup

Windows Command Prompt. Type one line at a time and press Enter.
Replace anything in `<ANGLE-BRACKETS>` with your own value.

## 1. Fork the repo (in browser)

1. Sign in to GitHub.
2. Open https://github.com/Aswath1986/Anudip-python-day5
3. Click **Fork**, then **Create fork**. You now have your own copy.
4. On your fork, click the green **Code** button and copy the URL.

## 2. Clone your fork and link the original

```cmd
cd %USERPROFILE%\Documents
git clone <YOUR-FORK-URL>
cd Anudip-python-day5
git remote add upstream https://github.com/Aswath1986/Anudip-python-day5.git
git remote -v
```

The last line should list both `origin` (your fork) and `upstream` (the
facilitator's repo).

## 3. Open the quiz notebook

**In VS Code** (needs the Python and Jupyter extensions):

```cmd
code .
```

Then open `SyntaxQuiz`, then `01_syntax_quiz.ipynb`. If VS Code asks for a
kernel, choose your Python.

**Or in the browser with Jupyter:**

```cmd
pip install notebook
cd SyntaxQuiz
jupyter notebook
```

Then click `01_syntax_quiz.ipynb`.

## 4. Start playing

1. Run the first code cell (Part 0). It should print `Questions ready: 112`.
2. Run the Part 1 cell and type your answers in the box that appears. Press
   Enter after each one.
3. Carry on down the notebook. Parts 6 and 7 give the Git commands for sending
   your own question and getting everyone else's.

## If something goes wrong

- **`No module named 'quiz'`:** the notebook was opened from the wrong place.
  Open the one inside the `SyntaxQuiz` folder.
- **`git` or `python` is not recognized:** it is not installed or not on the
  PATH. Call the facilitator.
- **First push asks you to sign in:** sign in to GitHub in the window that opens.
- **Lost in Git?** Run `git status`.
