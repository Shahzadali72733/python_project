"""Simple wrapper around the Mewati model logic for web use.

The original `mewati_model 01.py` is a desktop Tkinter app. For the
web/Flask frontend we only need a small, fast callable that returns a
string instead of opening any GUI windows.
"""

import re


def predict_beauty_score(text: str) -> str:
    """Return a lightweight 'score' for the provided text.

    Replace this with your real model logic when ready. Keeping it tiny
    avoids loading the heavyweight Tkinter/nltk GUI during web requests.
    """
    if not text:
        return "Please enter some text."

    # Example heuristic: length and vowel ratio.
    cleaned = re.sub(r"\s+", " ", text.strip())
    length = len(cleaned)
    vowels = sum(ch.lower() in "aeiou" for ch in cleaned)
    vowel_ratio = (vowels / length) if length else 0
    score = round((length % 10) + vowel_ratio * 5, 2)

    return f"Beauty Score for your text: {score}"


