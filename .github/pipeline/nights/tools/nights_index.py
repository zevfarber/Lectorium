#!/usr/bin/env python3
"""Index the night divisions in the Nights archive, and say which are ready to publish.

A publishing run calls this first:

    python3 tools/nights_index.py            # human-readable table
    python3 tools/nights_index.py --next     # the one night to publish, as JSON, or nothing

A "night" runs from its own opening formula to the opening formula of the next night. It is
COMPLETE only when the NEXT night's formula is also archived — otherwise its last lines are
still unread pages, and publishing it would ship a truncated night.

The formula is فلما كانت الليلة <ordinal>, which may straddle a line break, so the search runs
over the concatenated archive text rather than line by line. Night 1 is the exception: it opens
الليلة الاولى قالت شهرزاد, with no فلما كانت.

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

# The opening formula. ال is optionally dropped/attached in this edition's spelling, and the
# ordinal itself is not parsed for numbering — order of appearance is what numbers a night.
MARKER = re.compile(r"كانت\s+الليلة\s+(\S+)")
FIRST = re.compile(r"الليلة\s+الاولى\s+قالت")

ORDINALS = [
    "الاولى", "الثانية", "الثالثة", "الرابعة", "الخامسة", "السادسة", "السابعة",
    "الثامنة", "التاسعة", "العاشرة",
]


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
        owner.extend([i] * (len(t) + 1))   # +1 for the space joiner
    text = " ".join(text_parts)

    found = []
    m = FIRST.search(text)
    if m:
        found.append((owner[m.start()], "الاولى"))
    for m in MARKER.finditer(text):
        # anchor on الليلة, which is the line a reader would see the night begin on
        anchor = text.find("الليلة", m.start())
        found.append((owner[anchor if anchor >= 0 else m.start()], m.group(1)))

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
        expected = ORDINALS[n - 1] if n <= len(ORDINALS) else None
        nights.append({
            "night": n,
            "id": "nights-%02d" % n,
            "start": lines[idx][0],
            "end": lines[end_idx][0],
            "lines": end_idx - idx + 1,
            "complete": n < len(markers),
            "published": os.path.exists(os.path.join(ROOT, "nights-%02d.json" % n)),
            "ordinal_ok": expected is None or ordinal == expected,
            "ordinal_read": ordinal,
        })
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
            if nt["complete"] and not nt["published"]:
                print(json.dumps(nt, ensure_ascii=False))
                return 0
        return 0

    if not nights:
        print("no night markers found — archive may be frame material only")
        return 0

    print("night  lines  range              complete  published  ordinal")
    for nt in nights:
        print("%5d  %5d  %-8s→%-8s  %-8s  %-9s  %s" % (
            nt["night"], nt["lines"], nt["start"], nt["end"],
            "yes" if nt["complete"] else "NO (tail unread)",
            "yes" if nt["published"] else "no",
            nt["ordinal_read"] + ("" if nt["ordinal_ok"] else "  <-- MISMATCH"),
        ))
    ready = [n for n in nights if n["complete"] and not n["published"]]
    print("\ncomplete and unpublished: %d" % len(ready))
    if any(not n["ordinal_ok"] for n in nights):
        print("ORDINAL MISMATCH: a night formula was missed or mis-detected — do not publish "
              "past it; record it in QUESTIONS.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
