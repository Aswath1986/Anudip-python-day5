"""Secure feedback channel between each student and the facilitator.

Stage 1 (symmetric):  one personal key, made from your name and the class message.
                      The same key locks and unlocks.
Stage 2 (hybrid):     a random session key locks the message (symmetric), and the
                      facilitator's public key locks the session key (asymmetric).
                      Only the facilitator's private key can open it.

Both notebooks in this folder import these functions, so there is one copy of
the logic for everyone.
"""

import base64
import hashlib
import hmac
import json
from datetime import datetime, timezone
from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

HERE = Path(__file__).resolve().parent
CLASS_MESSAGE_FILE = HERE / "class_message.txt"
PUBLIC_KEY_FILE = HERE / "teacher_public_key.pem"
PRIVATE_KEY_FILE = HERE / "teacher_private_key.pem"   # in .gitignore
ROSTER_FILE = HERE / "roster.txt"                     # in .gitignore
SECRETS_DIR = HERE / "my_secrets"                     # in .gitignore
SESSION_KEY_FILE = SECRETS_DIR / "session_key.txt"
FEEDBACK_DIR = HERE / "feedback"
REPLIES_DIR = HERE / "replies"

_OAEP = padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None,
)


# ---------------------------------------------------------------- identity

def read_class_message():
    """Return the shared class message that everyone downloads from GitHub."""
    return CLASS_MESSAGE_FILE.read_text(encoding="utf-8").strip()


def normalize_name(name):
    """'  asha   KUMAR ' and 'Asha Kumar' must give the same key."""
    cleaned = " ".join(name.lower().split())
    if not cleaned:
        raise ValueError("Name cannot be empty")
    return cleaned


def make_key(name, class_message=None):
    """Mix a name with the class message and return a personal key.

    Same name + same class message -> always the same key.
    A different name -> a completely different key.
    """
    if class_message is None:
        class_message = read_class_message()
    digest = hmac.new(
        class_message.encode("utf-8"),
        normalize_name(name).encode("utf-8"),
        hashlib.sha256,
    ).digest()                                   # 32 bytes
    return base64.urlsafe_b64encode(digest).decode("ascii")


def student_id(key):
    """A short public label for a key. Safe to show: it cannot be turned back into the key."""
    return hashlib.sha256(key.encode("ascii")).hexdigest()[:8]


def read_roster():
    """Facilitator only: names from roster.txt, skipping blanks and # comments."""
    lines = ROSTER_FILE.read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip() and not line.startswith("#")]


def whose_key(key_or_id, roster, class_message=None):
    """Facilitator only: return the roster name that owns this key or student id, else None."""
    for name in roster:
        key = make_key(name, class_message)
        if key_or_id in (key, student_id(key)):
            return name
    return None


# ---------------------------------------------------------------- stage 1

def encrypt(message, key):
    """Lock a text message with a key. Returns text that is safe to share."""
    return Fernet(key.encode("ascii")).encrypt(message.encode("utf-8")).decode("ascii")


def decrypt(token, key):
    """Unlock a message. Raises ValueError if the key is wrong or the text was changed."""
    try:
        return Fernet(key.encode("ascii")).decrypt(token.encode("ascii")).decode("utf-8")
    except InvalidToken:
        raise ValueError("Wrong key, or the message was changed") from None


# ---------------------------------------------------------------- facilitator keys

def create_teacher_keys():
    """Facilitator, once: make the key pair. Refuses to replace an existing private key."""
    if PRIVATE_KEY_FILE.exists():
        raise FileExistsError(
            f"{PRIVATE_KEY_FILE.name} already exists. Replacing it would make every "
            "feedback already sent unreadable. Delete it yourself only if you are sure."
        )
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=3072)
    PRIVATE_KEY_FILE.write_bytes(private_key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption(),
    ))
    PUBLIC_KEY_FILE.write_bytes(private_key.public_key().public_bytes(
        serialization.Encoding.PEM,
        serialization.PublicFormat.SubjectPublicKeyInfo,
    ))
    return public_key_fingerprint()


def load_public_key():
    if not PUBLIC_KEY_FILE.exists():
        raise FileNotFoundError(
            f"{PUBLIC_KEY_FILE.name} is missing. Get the latest files from the "
            "facilitator's repo: git pull upstream main"
        )
    return serialization.load_pem_public_key(PUBLIC_KEY_FILE.read_bytes())


def load_private_key():
    if not PRIVATE_KEY_FILE.exists():
        raise FileNotFoundError(
            f"{PRIVATE_KEY_FILE.name} is missing. Only the facilitator's laptop has it."
        )
    return serialization.load_pem_private_key(PRIVATE_KEY_FILE.read_bytes(), password=None)


def public_key_fingerprint():
    """Short code to compare with the one the facilitator shows in class."""
    der = load_public_key().public_bytes(
        serialization.Encoding.DER,
        serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    digest = hashlib.sha256(der).hexdigest()[:16]
    return " ".join(digest[i:i + 4] for i in range(0, 16, 4))


# ---------------------------------------------------------------- stage 2

def get_session_key():
    """Return your random session key, creating and saving it the first time.

    It is saved in my_secrets/, which Git ignores. It never leaves your laptop
    in readable form.
    """
    if SESSION_KEY_FILE.exists():
        return SESSION_KEY_FILE.read_text(encoding="ascii").strip()
    SECRETS_DIR.mkdir(exist_ok=True)
    key = Fernet.generate_key().decode("ascii")
    SESSION_KEY_FILE.write_text(key, encoding="ascii")
    return key


def _timestamp():
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def seal(message, name, session_key=None, class_message=None):
    """Student: put a message in an envelope only the facilitator can open."""
    if session_key is None:
        session_key = get_session_key()
    sent_at = _timestamp()
    letter = json.dumps({"name": name.strip(), "message": message, "sent_at": sent_at})
    wrapped_key = load_public_key().encrypt(session_key.encode("ascii"), _OAEP)
    return {
        "version": 1,
        "student_id": student_id(make_key(name, class_message)),
        "sent_at": sent_at,
        "wrapped_key": base64.b64encode(wrapped_key).decode("ascii"),
        "token": encrypt(letter, session_key),
    }


def save_envelope(envelope, folder=None):
    """Write an envelope as a JSON file named <student_id>_<time>.json. Returns the path."""
    folder = Path(folder) if folder else FEEDBACK_DIR
    folder.mkdir(exist_ok=True)
    path = folder / f"{envelope['student_id']}_{envelope['sent_at']}.json"
    path.write_text(json.dumps(envelope, indent=2), encoding="utf-8")
    return path


def open_envelope(envelope, private_key=None, class_message=None):
    """Facilitator: open an envelope.

    Returns a dict with name, message, sent_at, session_key and id_matches.
    id_matches is False when the name inside does not belong to the id on the
    outside of the envelope.
    """
    if private_key is None:
        private_key = load_private_key()
    try:
        session_key = private_key.decrypt(
            base64.b64decode(envelope["wrapped_key"]), _OAEP
        ).decode("ascii")
    except ValueError:
        raise ValueError("This envelope was not sealed with our public key") from None
    letter = json.loads(decrypt(envelope["token"], session_key))
    letter["session_key"] = session_key
    letter["student_id"] = envelope["student_id"]
    letter["id_matches"] = (
        student_id(make_key(letter["name"], class_message)) == envelope["student_id"]
    )
    return letter


def read_envelopes(folder=None):
    """Return every envelope in a folder, oldest first."""
    folder = Path(folder) if folder else FEEDBACK_DIR
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(folder.glob("*.json"))]


def seal_reply(message, letter):
    """Facilitator: answer an opened letter, locked with that student's session key."""
    sent_at = _timestamp()
    return {
        "version": 1,
        "student_id": letter["student_id"],
        "sent_at": sent_at,
        "token": encrypt(message, letter["session_key"]),
    }


def open_replies(name, session_key=None, folder=None, class_message=None):
    """Student: read every reply addressed to you. Returns a list of (sent_at, text)."""
    if session_key is None:
        session_key = get_session_key()
    my_id = student_id(make_key(name, class_message))
    replies = []
    for reply in read_envelopes(folder or REPLIES_DIR):
        if reply["student_id"] != my_id:
            continue
        try:
            replies.append((reply["sent_at"], decrypt(reply["token"], session_key)))
        except ValueError:
            replies.append((reply["sent_at"], "(locked with an older session key)"))
    return replies
