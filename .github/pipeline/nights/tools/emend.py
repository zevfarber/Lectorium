"""Misprint corrections for the reading edition (owner's rule, 2026-11-06).

The archive records the 1839 print exactly and is never changed. Where the print has a clear
misprint (a dropped or misplaced dot, a swapped letter, a slip of the compositor such that the
sense allows one reading only), the reading text carries the corrected word and the unit's `n`
gives the print's reading ("The print has X"). Middle Arabic forms and doubtful readings are
not misprints and stay as printed.

../emend.json lists each correction:

    {"ref": "P470L01", "print": "المثمانين", "read": "الثمانين", "night": 80,
     "why": "misprint for the ordinal"}

`print` and `read` are bare letters (no marks). `read` may hold a space when the print runs two
words together by mistake, or be "" when the print repeats a word by mistake. `nth` (optional,
1-based) picks the occurrence when the printed word appears more than once on the line.

The checks in check_slice.py and validate_night.py compare the story with the archive AFTER
these corrections, so a corrected word passes and an unlisted change still fails.
"""

import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
EMEND_FILE = os.path.join(os.path.dirname(HERE), "emend.json")

STRIP = re.compile("[ً-ٰٟۖ-ۭ]")
FURNITURE = re.compile(r"[*\n]+")
WORD = re.compile(r"[ؠ-ٰٟ-ۓە-ۭ]+")

_cache = None


def _load():
    global _cache
    if _cache is None:
        _cache = {}
        if os.path.exists(EMEND_FILE):
            with open(EMEND_FILE, encoding="utf-8") as fh:
                for e in json.load(fh):
                    _cache.setdefault(e["ref"], []).append(e)
    return _cache


def line_words(line):
    """The archived line's words, marks kept, with any listed correction applied. A corrected
    word comes back as bare letters, so the verse-as-printed check never applies to it."""
    ws = WORD.findall(FURNITURE.sub(" ", line.get("t", "")))
    fixes = _load().get(line.get("ref"), [])
    if not fixes:
        return ws
    out = list(ws)
    for e in fixes:
        # nth counts occurrences in the line as printed, so entries never shift each other
        nth = int(e.get("nth", 1))
        hits = [i for i, w in enumerate(ws) if STRIP.sub("", w) == e["print"]]
        if len(hits) < nth:
            raise SystemExit("emend.json: %s has no %r (occurrence %d) — fix the entry"
                             % (e["ref"], e["print"], nth))
        out[hits[nth - 1]] = WORD.findall(e["read"])
    flat = []
    for w in out:
        flat.extend(w if isinstance(w, list) else [w])
    return flat
