#!/usr/bin/env python3
"""Index the night divisions in the Nights archive, and say which are ready to publish.

A publishing run calls this first:

    python3 tools/nights_index.py          # human-readable table
    python3 tools/nights_index.py --next   # the one night to publish, as JSON, or nothing

A "night" runs from its own opening formula to the opening formula of the next night. It is
COMPLETE only when the NEXT night's formula is also archived — otherwise its last lines are
still unread pages, and publishing it would ship a truncated night.

The formula is فلما كانت الليلة <ordinal> <tag>, which may straddle a line break, so the search
runs over the concatenated archive text rather than line by line. Night 1 is the exception: it
opens الليلة الاولى قالت شهرزاد, with no فلما كانت.

Every ordinal is parsed to a number and checked against the night's position. A night whose
ordinal does not parse to the expected number, or that is implausibly long, is a MISMATCH, and
--next never offers it or anything after it: a missed formula would otherwise swallow the next
night into this one and publish two nights as one (see the 2026-10-04 entry in QUESTIONS.md —
exactly that was about to happen to Nights 20–29).

Published is decided by the repository, never by a log: night N is published iff the root file
nights-<NN>.json exists.
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
NIGHTS = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(NIGHTS, "..", "..", ".."))
ARCHIVE = os.path.join(NIGHTS, "archive")

# The opening formula. The ordinal is one to four words: a single word up to 10 (الثانية), two
# for the teens (الحادية عشر), two joined by و for 21–29 and the like (الحادية والعشرون), and
# this edition's "completing" form at the round tens (الموفية للثلثين, "the one completing
# thirty"). The narrator's tag (قالت / قال / قلت — the spelling varies) must follow within
# those four words: found 2026-09-27 publishing what --next called "night 16", printed pp.
# 107-114 ("...فلما كانت الليلة القابلة علقت والدتي بي...", the young man's own backstory
# saying "the following night" — no tag follows, and it is not a frame-formula ordinal at all)
# — see QUESTIONS.md. Without the tag requirement this false marker split one real night into
# two and mislabeled every night after it.
#
# History: until 2026-10-04 the ordinal was (\S+(?:\s+عشر)?), one word plus an optional عشر.
# That matched العشرون but not الحادية والعشرون, so from Night 21 on no formula was found, Night
# 20 never became "complete", --next returned nothing for five days of firings (every one fell
# through to transcribing), and once Night 30's one-word-looking formula arrived Nights 20–29
# would have been published as a single "Night 20". Hence the parsed-ordinal check below.
MARKER = re.compile(r"كانت\s+الليلة\s+((?:\S+\s+){1,4}?)(?:قالت|قال|قلت)\b")
FIRST = re.compile(r"الليلة\s+الاولى\s+قالت")

# Longest night published so far is 248 lines (Night 18). A unit over this many lines almost
# certainly contains a formula the regex missed; refuse to publish it.
MAX_NIGHT_LINES = 400

# --- ordinal → number -----------------------------------------------------------------------
# Spelling is normalised before lookup: diacritics stripped, ة→ه, ى→ي, hamza seats → bare
# letter, آ→ا, and the article prefix ال / لل / وال dropped from each word.

_DIACRITICS = re.compile("[\\u0610-\\u061A\\u064B-\\u065F\\u0670\\u06D6-\\u06ED\\u0640]")

def _norm(word):
    w = _DIACRITICS.sub("", word)
    w = (w.replace("ة", "ه").replace("ى", "ي").replace("أ", "ا").replace("إ", "ا")
          .replace("آ", "ا").replace("ؤ", "و").replace("ئ", "ي"))
    for pre in ("وال", "لل", "ال", "و"):
        if w.startswith(pre) and len(w) > len(pre) + 1:
            w = w[len(pre):]
            break
    return w

UNITS = {
    "اولي": 1, "اوله": 1, "حاديه": 1, "واحده": 1,
    "ثانيه": 2, "ثالثه": 3, "رابعه": 4, "خامسه": 5, "سادسه": 6,
    "سابعه": 7, "ثامنه": 8, "تاسعه": 9, "عاشره": 10,
}
TEEN = {"عشر": 10, "عشره": 10}
TENS = {
    "عشرون": 20, "عشرين": 20,
    "ثلثون": 30, "ثلاثون": 30, "ثلثين": 30, "ثلاثين": 30,
    "اربعون": 40, "اربعين": 40, "خمسون": 50, "خمسين": 50,
    "ستون": 60, "ستين": 60, "سبعون": 70, "سبعين": 70,
    "ثمانون": 80, "ثمانين": 80, "تسعون": 90, "تسعين": 90,
    "مائه": 100, "مايه": 100, "ماءه": 100,
}
COMPLETING = {"موفيه", "مكمله", "متممه"}


def ordinal_number(ordinal):
    """The number an ordinal phrase names, or None when it cannot be read."""
    words = [_norm(w) for w in ordinal.split()]
    words = [w for w in words if w]
    if not words:
        return None
    if words[0] in COMPLETING:
        # الموفية للثلثين = the one completing thirty
        rest = words[1:]
        if len(rest) == 1 and rest[0] in TENS:
            return TENS[rest[0]]
        if len(rest) == 2 and rest[0] in TENS and rest[1] in TENS:   # مائة وعشرين
            return TENS[rest[0]] + TENS[rest[1]]
        return None
    if len(words) == 1:
        if words[0] in UNITS:
            return UNITS[words[0]]
        if words[0] in TENS:
            return TENS[words[0]]
        return None
    if len(words) == 2:
        if words[0] in UNITS and words[1] in TEEN:          # الحادية عشر
            return 10 + UNITS[words[0]]
        if words[0] in UNITS and words[1] in TENS:          # الحادية والعشرون
            return TENS[words[1]] + UNITS[words[0]]
        if words[0] in TENS and words[1] in TENS:           # المائة والعشرون
            return TENS[words[0]] + TENS[words[1]]
        return None
    if len(words) == 3:
        # الحادية والعشرون بعد المائة is 4 words; three words: الحادية عشر بعد ... not expected.
        if words[0] in UNITS and words[1] in TENS and words[2] in TENS:
            return TENS[words[2]] + TENS[words[1]] + UNITS[words[0]]
        return None
    if len(words) == 4 and words[2] == "بعد":                # الحادية والعشرون بعد المائة
        head = ordinal_number(" ".join(words[:2]))
        if head is not None and words[3] in TENS:
            return TENS[words[3]] + head
    return None


def load_lines():
    """Every archived line in printed order, as (ref, text)."""
    out = []
    for name in sorted(os.listdir(ARCHIVE)):
        if not (name.startswith("pp") and name.endswith(".json")):
            continue
        with open(os.path.join(ARCHIVE, name), encoding="utf-8") as fh:
            doc = json.load(fh)
        for line in doc["lines"]:
            out.append((line["ref"], line.get("t", "")))
    return out


def load_records():
    """Every archived line in printed order as its full record — ref, t, and the verse flag
    "v" where the archive sets it. --text must hand drafters this, not load_lines()'s bare
    (ref, text) pairs: until 2026-09-25 it dropped "v", so drafters could not see which lines
    were verse (found publishing Nights 11 and 12)."""
    out = []
    for name in sorted(os.listdir(ARCHIVE)):
        if not (name.startswith("pp") and name.endswith(".json")):
            continue
        with open(os.path.join(ARCHIVE, name), encoding="utf-8") as fh:
            doc = json.load(fh)
        for line in doc["lines"]:
            rec = {"ref": line["ref"], "t": line.get("t", "")}
            if line.get("v"):
                rec["v"] = True
            out.append(rec)
    return out


def find_markers(lines):
    """Character-offset search over the joined text, mapped back to line indexes."""
    text_parts, owner = [], []
    for i, (_ref, t) in enumerate(lines):
        text_parts.append(t)
        owner.extend([i] * (len(t) + 1))  # +1 for the space joiner
    text = " ".join(text_parts)

    found = []
    m = FIRST.search(text)
    if m:
        found.append((owner[m.start()], "الاولى"))
    for m in MARKER.finditer(text):
        # anchor on الليلة, which is the line a reader would see the night begin on
        anchor = text.find("الليلة", m.start())
        found.append((owner[anchor if anchor >= 0 else m.start()], m.group(1).strip()))

    found.sort(key=lambda p: p[0])
    deduped = []
    for idx, ordinal in found:
        if deduped and deduped[-1][0] == idx:
            continue
        deduped.append((idx, ordinal))
    return deduped


def build():
    lines = load_lines()
    if not lines:
        return []
    markers = find_markers(lines)
    nights = []
    # The frame material before Night 1. The pilot (nights-frame-01) already covers printed
    # pp. 1-3 down to a mid-page sentence boundary, so a run publishing this unit starts after
    # the pilot's last sentence, not at P03L01 — see publish-runbook.md.
    if markers and markers[0][0] > 0:
        nights.append({
            "night": 0,
            "id": "nights-frame-02",
            "start": lines[0][0],
            "end": lines[markers[0][0] - 1][0],
            "lines": markers[0][0],
            "complete": True,
            "published": os.path.exists(os.path.join(ROOT, "nights-frame-02.json")),
            "ordinal_ok": True,
            "ordinal_read": "(frame, before Night 1)",
            "note": "overlaps the pilot nights-frame-01; start after the pilot's last sentence",
        })
    for n, (idx, ordinal) in enumerate(markers, start=1):
        end_idx = markers[n][0] - 1 if n < len(markers) else len(lines) - 1
        count = end_idx - idx + 1
        number = ordinal_number(ordinal)
        complete = n < len(markers)
        ok = number == n and (not complete or count <= MAX_NIGHT_LINES)
        nt = {
            "night": n,
            "id": "nights-%02d" % n,
            "start": lines[idx][0],
            "end": lines[end_idx][0],
            "lines": count,
            "complete": complete,
            "published": os.path.exists(os.path.join(ROOT, "nights-%02d.json" % n)),
            "ordinal_ok": ok,
            "ordinal_read": ordinal,
            "ordinal_number": number,
        }
        if number != n:
            nt["problem"] = ("ordinal reads as %s, expected %d" % (number, n)
                             if number is not None else "ordinal not understood")
        elif complete and count > MAX_NIGHT_LINES:
            nt["problem"] = "%d lines — far longer than any night; a formula was missed" % count
        nights.append(nt)
    return nights


def main():
    nights = build()
    want_next = "--next" in sys.argv

    if "--text" in sys.argv:
        # --text <night-number> : the archived lines of that unit, as JSON, for drafting.
        want = int(sys.argv[sys.argv.index("--text") + 1])
        nt = next((n for n in nights if n["night"] == want), None)
        if nt is None:
            print("no such night: %d" % want, file=sys.stderr)
            return 2
        inside, out = False, []
        for rec in load_records():
            if rec["ref"] == nt["start"]:
                inside = True
            if inside:
                out.append(rec)
                if rec["ref"] == nt["end"]:
                    break
        print(json.dumps({"unit": nt, "lines": out}, ensure_ascii=False, indent=1))
        return 0

    if want_next:
        for nt in nights:
            if not nt["ordinal_ok"]:
                # Never publish this unit or anything after it — see the module docstring.
                print("MISMATCH at night %d (%s): %s — fix nights_index.py or the archive "
                      "before publishing; record it in QUESTIONS.md"
                      % (nt["night"], nt["ordinal_read"], nt.get("problem", "")),
                      file=sys.stderr)
                return 0
            if nt["complete"] and not nt["published"]:
                print(json.dumps(nt, ensure_ascii=False))
                return 0
        return 0

    if not nights:
        print("no night markers found — archive may be frame material only")
        return 0

    print("night lines range                complete           published ordinal")
    for nt in nights:
        print("%5d %5d %-8s→%-8s %-18s %-9s %s" % (
            nt["night"], nt["lines"], nt["start"], nt["end"],
            "yes" if nt["complete"] else "NO (tail unread)",
            "yes" if nt["published"] else "no",
            nt["ordinal_read"] + ("" if nt["ordinal_ok"] else "  <-- MISMATCH: " + nt.get("problem", "")),
        ))
    ready = [n for n in nights if n["complete"] and not n["published"] and n["ordinal_ok"]]
    print("\ncomplete and unpublished: %d" % len(ready))
    if any(not n["ordinal_ok"] for n in nights):
        print("ORDINAL MISMATCH: a night formula was missed or mis-detected — do not publish "
              "past it; record it in QUESTIONS.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
