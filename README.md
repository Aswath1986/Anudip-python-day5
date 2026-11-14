# Anudip-python-day5
Covering all concepts with story method and strong industry use case

Two labs live here. Start with SyntaxQuiz; SecureChannel is the harder one.

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
| `SyntaxQuiz/questions/` | 89 starter questions on Week 1; student questions go in `students/` |
| `SyntaxQuiz/broken_examples/` | A question file with a typo, used for the try/except lesson |

Answers in the question files are stored encoded, so students cannot read
them at a glance on GitHub; `RUN_SHEET.md` explains how the facilitator reveals
them for review.

Needs only Python and Jupyter, nothing to install. The game runs the code in
question files and in players' answers, so it is a classroom tool: read a
question file before merging it.

## SecureChannel: a private feedback line over a public repo

Each student sends feedback to the facilitator through a pull request. Everyone
can see the file. Only the facilitator can read it. Building this reuses Week 1
(encoding, hex, bitwise operators, functions, try/except, files) and adds
hashing, symmetric and asymmetric encryption, and `.gitignore`.

### The HTTPS picture

The lab is an HTTPS connection acted out by people. Each student is a
**client**, the facilitator is the **server**, and the public repo is the
**internet** that anyone can watch.

| Step in HTTPS | In this lab |
|---|---|
| 1. Hello: client asks for the server's certificate | Student pulls `teacher_public_key.pem` |
| 2. Client checks the certificate | Student compares the fingerprint with the facilitator's screen |
| 3. Key exchange (asymmetric) | Student's random session key travels as `wrapped_key` |
| 4. Encrypted request (symmetric) | Feedback travels as `token` |
| 5. Encrypted response (symmetric) | Facilitator's reply, locked with the same session key |

The lab wraps the session key with the server's public key, as HTTPS did for
many years. TLS 1.3 instead lets both sides build the key together, so a
private key stolen later cannot unlock old traffic. Part 6 of the student
notebook explains this and opens a real HTTPS connection for comparison.

### Files

| File | For | What it is |
|---|---|---|
| `SecureChannel/01_student_secure_channel.ipynb` | Students | The guided lab |
| `SecureChannel/02_teacher_secure_channel.ipynb` | Facilitator | Setup, open feedback, reply |
| `SecureChannel/secure_channel.py` | Both | All the functions, in one place |
| `SecureChannel/class_message.txt` | Both | The shared message every key is made from |
| `SecureChannel/feedback/`, `replies/` | Both | Sealed envelopes travel here |
| `SecureChannel/roster.example.txt` | Facilitator | Template for the private `roster.txt` |

### Design

**Stage 1, symmetric.** `make_key(name)` mixes the student's name with the
class message (HMAC-SHA256) and returns a personal key. Each name gives a
different key, and the facilitator can rebuild any key from the roster, so the
facilitator always knows whose key it is. The weakness is deliberate: the key is
made only from public things, so a classmate who knows your name can rebuild it.
Students find this themselves in the *Break it* exercise.

**Stage 2, hybrid.** This is what carries the real feedback.

```
student laptop                                   facilitator laptop
--------------                                   ------------------
random session key  (stays in my_secrets/)       private key (stays here)
message  --locked with session key-->  token
session key --locked with PUBLIC key--> wrapped_key
            feedback/<id>_<time>.json  ---- pull request ---->  private key opens wrapped_key
                                                                session key opens token
            replies/<id>_<time>.json   <------- git pull -----  reply locked with the same session key
```

- A classmate who has your personal key and your envelope still cannot read it.
- The personal key is now only a label: its short id names the envelope.
- The private key, the roster and each student's session key are in
  `.gitignore` and never reach GitHub.

**Known limits, good for class discussion.** Anyone can seal a letter under
another student's name (fixing that needs digital signatures). File names and
Git history show who sent a file and when, but not what it says.

### Running the session

Facilitator, once before class:

1. Run Part 0 of `02_teacher_secure_channel.ipynb`. It creates the key pair.
2. Commit and push `SecureChannel/teacher_public_key.pem`.
3. Back up `teacher_private_key.pem` somewhere safe. Without it nobody can read the feedback.
4. Copy `roster.example.txt` to `roster.txt` and fill in the names.

Students: fork, clone, `pip install -r SecureChannel/requirements.txt`, open
`01_student_secure_channel.ipynb` and follow it top to bottom. The notebook
covers the branch, commit, push and pull request steps.

Facilitator, after class: merge the pull requests, `git pull`, then run Parts 3
and 4 of the facilitator notebook to read and reply.
