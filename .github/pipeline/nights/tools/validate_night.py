#!/usr/bin/env python3
"""Gate a published Nights story file against the archive it was built from.

    python3 tools/validate_night.py ../../../nights-01.json --from P10L10 --to P14L08

Four mechanical checks, in order of how badly they bite:

1. BARE-STRIP IDENTITY. Strip the combining marks from the story's original text and it must
   equal the archived lines token-for-token. This is the single most important check in the
   Arabic pipeline: it proves the vocalisation added nothing and dropped nothing, and it is
   also what catches precomposed hamza (أ إ آ ؤ ئ), which does NOT strip back to the bare rasm
   and would silently break the reader's "bare" toggle. Never "fix" a failure here by running
   NFC over the file — that breaks every Arabic text in the library. Fix the word.
1b. VERSE AS PRINTED. Where the archived line is verse and the archive word already carries
   marks, the story's word must be the archive's word codepoint for codepoint: Calcutta II
   points its verse, and that pointing is final. Catches what 1 cannot — a drafter re-pointing
   printed verse, or writing its combining hamza as precomposed أ/إ, or adding a hamza the
   edition does not print (all strip to the same letters). Added 2026-09-23 after Night 8.
   Repair with check_slice.py --fix on the assembled file.
2. GLOSSARY COVERAGE. Every word form in every sentence resolves in the shared glossary, with
   the reader's own diacritic-insensitive fallback allowed. Must be 100%.
3. SHAPE. Required fields present; rtl/script/langCode as the Arabic texts use them; l on every
   sentence; the recension note present in about.
4. MANIFEST. stories.json carries the entry and points at this file.

Exit status 0 only when every check passes; the run prints RESULT PASS / RESULT FAIL.
"""

import json
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
NIGHTS = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(NIGHTS, "..", "..", ".."))
ARCHIVE = os.path.join(NIGHTS, "archive")
GLOSSARY = os.path.join(ROOT, "nights-glossary.json")
STORIES = os.path.join(ROOT, "stories.json")

# Exactly the ranges the reader strips for the bare state. Keep in step with reader.html.
STRIP = re.compile("[ً-ٰٟۖ-ۭ]")
# Furniture that is ours, not the edition's: verse hemistich separator, line breaks.
FURNITURE = re.compile(r"[*\n]+")
WORD = re.compile(r"[ؠ-ٰٟ-ۓە-ۭ]+")


def bare(s):
    return STRIP.sub("", s)


def tokens(s):
    return WORD.findall(bare(FURNITURE.sub(" ", s)))


def archive_tokens(first_ref, last_ref):
    """Tokens of the archived lines from first_ref to last_ref inclusive, in printed order."""
    out, inside = [], False
    for name in sorted(os.listdir(ARCHIVE)):
        if not (name.startswith("pp") and name.endswith(".json")):
            continue
        with open(os.path.join(ARCHIVE, name), encoding="utf-8") as fh:
            doc = json.load(fh)
        for line in doc["lines"]:
            if line["ref"] == first_ref:
                inside = True
            if inside:
                out.extend(tokens(line.get("t", "")))
            if line["ref"] == last_ref and inside:
                return out
    return out


def archive_verse_marked(first_ref, last_ref):
    """Parallel to archive_tokens(): (marked word, ref) for a pointed verse word, else None."""
    out, inside = [], False
    for name in sorted(os.listdir(ARCHIVE)):
        if not (name.startswith("pp") and name.endswith(".json")):
            continue
        with open(os.path.join(ARCHIVE, name), encoding="utf-8") as fh:
            doc = json.load(fh)
        for line in doc["lines"]:
            if line["ref"] == first_ref:
                inside = True
            if inside:
                verse = bool(line.get("v"))
                for w in WORD.findall(FURNITURE.sub(" ", line.get("t", ""))):
                    out.append((w, line["ref"]) if verse and w != bare(w) else None)
            if line["ref"] == last_ref and inside:
                return out
    return out


def fold(w):
    """The reader's fallback key: bare consonantal skeleton."""
    return unicodedata.normalize("NFC", bare(w))


def main():
    if len(sys.argv) < 2:
        print("usage: validate_night.py <story.json> --from <REF> --to <REF>")
        return 2
    path = sys.argv[1]
    first = sys.argv[sys.argv.index("--from") + 1]
    last = sys.argv[sys.argv.index("--to") + 1]

    fails, warns = [], []
    with open(path, encoding="utf-8") as fh:
        story = json.load(fh)

    # --- 3. shape -------------------------------------------------------------------
    for field in ("id", "title", "titleEn", "language", "source", "about", "sentences",
                  "work", "workEn", "part", "glossaryFile"):
        if not story.get(field):
            fails.append("shape: missing or empty field %r" % field)
    if story.get("rtl") is not True:
        fails.append("shape: rtl must be true")
    if story.get("script") != "arabic":
        fails.append("shape: script must be \"arabic\"")
    if story.get("trStyle") != "line":
        fails.append("shape: trStyle must be \"line\" (romanisation is an overlay, not a column)")
    if story.get("langCode") != "ar-XA":
        fails.append("shape: langCode must be \"ar-XA\"")
    if "recension" not in (story.get("about") or "").lower() and \
       "ZER" not in (story.get("about") or ""):
        fails.append("shape: about must state plainly that this is the late Egyptian recension")
    if "editorial" not in (story.get("source") or "").lower():
        fails.append("shape: source must declare that the vocalisation is editorial")
    if story.get("glossary"):
        fails.append("shape: inline glossary present — the Nights uses the shared "
                     "nights-glossary.json via glossaryFile")

    sents = story.get("sentences") or []
    for i, s in enumerate(sents):
        if not s.get("t"):
            fails.append("sentence %d: no original text" % i)
        if not s.get("l"):
            fails.append("sentence %d: no literal layer" % i)
        if not s.get("tr"):
            fails.append("sentence %d: no transliteration" % i)

    # --- 1. bare-strip identity ------------------------------------------------------
    story_toks = []
    for s in sents:
        story_toks.extend(tokens(s.get("t", "")))
    arch_toks = archive_tokens(first, last)
    if not arch_toks:
        fails.append("archive: no lines found for %s..%s" % (first, last))
    if story_toks != arch_toks:
        n = min(len(story_toks), len(arch_toks))
        where = next((j for j in range(n) if story_toks[j] != arch_toks[j]), n)
        fails.append(
            "BARE-STRIP MISMATCH at token %d of %d (archive has %d): archive %r, story %r. "
            "The vocalised text must strip back to the edition exactly — check for precomposed "
            "hamza, and never run NFC over the file." % (
                where, len(story_toks), len(arch_toks),
                arch_toks[where] if where < len(arch_toks) else "(end)",
                story_toks[where] if where < len(story_toks) else "(end)"))

    # --- 1b. verse as printed ---------------------------------------------------------
    if arch_toks and story_toks == arch_toks:
        story_words = []
        for s in sents:
            story_words.extend(WORD.findall(FURNITURE.sub(" ", s.get("t", ""))))
        marked = archive_verse_marked(first, last)
        vbad = [(m[1], w, m[0]) for w, m in zip(story_words, marked)
                if m is not None and w != m[0]]
        if vbad:
            fails.append(
                "VERSE RE-VOCALISED: %d pointed verse word(s) differ from the edition, e.g. %s. "
                "Verse t is copied from the archive as printed; run check_slice.py --fix on this "
                "file with the night's --from/--to." % (len(vbad), "; ".join(
                    "%s %r (archive %r)" % v for v in vbad[:4])))

    # --- 2. glossary coverage --------------------------------------------------------
    if os.path.exists(GLOSSARY):
        with open(GLOSSARY, encoding="utf-8") as fh:
            gloss = json.load(fh)
        exact = set(gloss)
        folded = {fold(k) for k in gloss}
        missing = []
        for s in sents:
            for w in WORD.findall(FURNITURE.sub(" ", s.get("t", ""))):
                if w in exact or fold(w) in folded:
                    continue
                missing.append(w)
        if missing:
            uniq = sorted(set(missing))
            fails.append("glossary: %d word forms unresolved (%d distinct), e.g. %s" % (
                len(missing), len(uniq), ", ".join(uniq[:8])))
    else:
        fails.append("glossary: %s does not exist — create it on the first publishing run "
                     "(migrate the pilot's inline glossary into it)" % GLOSSARY)

    # --- 4. manifest -----------------------------------------------------------------
    with open(STORIES, encoding="utf-8") as fh:
        stories = json.load(fh)
    entries = stories if isinstance(stories, list) else stories.get("stories", [])
    entry = next((e for e in entries if e.get("id") == story.get("id")), None)
    if entry is None:
        fails.append("manifest: stories.json has no entry with id %r" % story.get("id"))
    else:
        if entry.get("file") != os.path.basename(path):
            fails.append("manifest: entry points at %r, not %r" % (
                entry.get("file"), os.path.basename(path)))
        for field in ("work", "workEn", "part"):
            if not entry.get(field):
                warns.append("manifest: entry has no %r — the library groups the nights by it"
                             % field)

    for w in warns:
        print("WARN  " + w)
    for f in fails:
        print("FAIL  " + f)
    print("\nsentences %d · tokens %d · archive %s..%s" % (
        len(sents), len(story_toks), first, last))
    print("RESULT %s" % ("FAIL" if fails else "PASS"))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
