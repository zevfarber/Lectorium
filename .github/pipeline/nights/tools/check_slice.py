#!/usr/bin/env python3
"""Check one drafting slice against the archive — by script, never by an agent's say-so.

    python3 tools/check_slice.py /tmp/slice3.json --from P31L10 --to P32L04
    python3 tools/check_slice.py /tmp/slice3.json --from P31L10 --to P32L04 --fix

Why this exists. Publishing Night 5 (2026-09-22), all five drafting agents reported that they
had checked the bare-strip identity of their slice and found zero mismatches. On assembly, 1224
of the night's 1798 tokens failed it: every agent had written hamza with the precomposed letters
(أ إ ؤ ئ), which look identical to the required base-letter-plus-combining-mark encoding in any
editor, and differ only at the codepoint level. No agent, and no human, can see this defect;
only a script can. So the rule is: an agent's claim that it verified its slice is worth nothing
and is never asked for. The orchestrator runs THIS tool on every slice the moment it comes
back, and a slice does not go into the night until it prints RESULT PASS.

What it checks. The slice's original text (`t` of every sentence, in order), with the
combining marks stripped, must equal the archived lines --from..--to token for token — the same
identity `validate_night.py` gates the whole night on, applied early, per slice, while it is
cheap to fix.

What --fix repairs, mechanically and only where the archive proves the repair right:
  * precomposed hamza where the edition prints the bare letter: أ إ → ا + U+0654/U+0655,
    ؤ → و + U+0654, ئ → ي + U+0654 (and آ → ا + U+0653 where the edition prints bare alif);
  * a word the drafter fused that the archive prints as two tokens (the edition's frequent
    stray "و " before its host word, or a word split across a page-line break): a space is
    put back at the archive's boundary, inside the vocalised word;
  * two words the drafter split that the archive prints as one: joined.
Every other mismatch — a changed, missing or extra word — is reported and left alone: that is
a drafting error the orchestrator has to look at, not an encoding slip.

The same word-level fixes are propagated into the slice's glossary keys, so the entries still
resolve. A fused key that had to be split becomes two keys carrying the old entry text, and
each is listed under WARN so the orchestrator rewrites the two meanings; the tool cannot
invent glosses.

Input. A JSON file that is either a list of sentence objects, or an object with "sentences"
(and optionally "glossary"). Exactly the shape a drafting agent hands back. With --fix the
file is rewritten in place and the check re-run; exit status 0 only on RESULT PASS.
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
NIGHTS = os.path.dirname(HERE)
ARCHIVE = os.path.join(NIGHTS, "archive")

# Keep these three in step with validate_night.py (and reader.html).
STRIP = re.compile("[ً-ٰٟۖ-ۭ]")
FURNITURE = re.compile(r"[*\n]+")
WORD = re.compile(r"[ؠ-ٰٟ-ۓە-ۭ]+")

# Precomposed hamza/madda → base letter + combining mark. The edition prints the bare base
# letter almost everywhere; where it prints the precomposed letter itself, the archive token
# carries it and the strip test expects it, so the map is applied only when it makes the word
# match the archive.
DECOMPOSE = {
    "أ": "أ",   # أ → ا + hamza above
    "إ": "إ",   # إ → ا + hamza below
    "ؤ": "ؤ",   # ؤ → و + hamza above
    "ئ": "ئ",   # ئ → ي + hamza above
    "آ": "آ",   # آ → ا + madda above
}


def bare(s):
    return STRIP.sub("", s)


def words(s):
    """Vocalised words of a sentence, in order (furniture removed, marks kept)."""
    return WORD.findall(FURNITURE.sub(" ", s))


def archive_tokens(first_ref, last_ref):
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
                out.extend(WORD.findall(bare(FURNITURE.sub(" ", line.get("t", "")))))
            if line["ref"] == last_ref and inside:
                return out
    return out


def decomposed(w):
    for k, v in DECOMPOSE.items():
        w = w.replace(k, v)
    return w


def align(story_words, arch):
    """Walk the slice's words against the archive tokens. Returns (fixed_words, problems,
    fixes) where fixed_words is a list of vocalised words with the mechanical repairs applied
    (spaces inside a word mark a split), problems is a list of strings for what could not be
    repaired, and fixes counts what was repaired by kind."""
    out, problems = [], []
    fixes = {"hamza": 0, "split": 0, "join": 0}
    i = j = 0
    while i < len(story_words) and j < len(arch):
        w = story_words[i]
        b = bare(w)
        a = arch[j]
        if b == a:
            out.append(w); i += 1; j += 1; continue
        d = decomposed(w)
        if bare(d) == a:
            out.append(d); fixes["hamza"] += 1; i += 1; j += 1; continue
        # fused: the story word covers two (or more) archive tokens
        db = bare(d)
        if j + 1 < len(arch) and db.startswith(a):
            k, acc = j, ""
            while k < len(arch) and len(acc) < len(db) and db.startswith(acc + arch[k]):
                acc += arch[k]; k += 1
            if acc == db and k > j + 1:
                fixed = rebuild_split(d, [len(t) for t in arch[j:k]])
                out.append(fixed); fixes["split"] += (k - j - 1)
                if w != d:
                    fixes["hamza"] += 1
                i += 1; j = k; continue
        # split: the archive token covers two (or more) story words
        if i + 1 < len(story_words) and a.startswith(db):
            k, acc, accw = i, "", []
            while k < len(story_words) and len(acc) < len(a) and \
                    a.startswith(acc + bare(decomposed(story_words[k]))):
                acc += bare(decomposed(story_words[k])); accw.append(decomposed(story_words[k])); k += 1
            if acc == a and k > i + 1:
                # keep `out` parallel to story_words: the joined word sits at the first
                # position and the consumed words become empty
                out.append("".join(accw)); out.extend([""] * (k - i - 1))
                fixes["join"] += (k - i - 1)
                i = k; j += 1; continue
        problems.append("token %d: archive %r, slice %r" % (j, a, b))
        out.append(w); i += 1; j += 1
    if i < len(story_words):
        problems.append("slice has %d extra word(s) after the archive ends, first %r"
                        % (len(story_words) - i, bare(story_words[i])))
        out.extend(story_words[i:])
    if j < len(arch):
        problems.append("slice stops %d token(s) before the archive ends, next archive token %r"
                        % (len(arch) - j, arch[j]))
    return out, problems, fixes


def rebuild_split(w, pieces):
    """Split vocalised word w into len(pieces) words whose bare lengths are `pieces`."""
    parts, cur, count, idx = [], "", 0, 0
    for ch in w:
        if not STRIP.match(ch) and count == pieces[idx] and idx < len(pieces) - 1:
            parts.append(cur); cur, count, idx = "", 0, idx + 1
        cur += ch
        if not STRIP.match(ch):
            count += 1
    parts.append(cur)
    return " ".join(parts)


def apply_to_sentences(sents, fixed_words):
    """Write the repaired words back into each sentence's t, in place, keeping punctuation,
    verse furniture and everything else untouched."""
    it = iter(fixed_words)
    for s in sents:
        t = s.get("t", "")
        if not t:
            continue
        t = WORD.sub(lambda m: next(it), t)
        # a joined word leaves an empty slot behind it: collapse the doubled space
        t = re.sub(r"[ \t]{2,}", " ", t)
        t = re.sub(r" +\n", "\n", t)
        t = re.sub(r"\n +", "\n", t)
        s["t"] = t.strip(" ")


def main():
    if len(sys.argv) < 2 or "--from" not in sys.argv or "--to" not in sys.argv:
        print("usage: check_slice.py <slice.json> --from <REF> --to <REF> [--fix]")
        return 2
    path = sys.argv[1]
    first = sys.argv[sys.argv.index("--from") + 1]
    last = sys.argv[sys.argv.index("--to") + 1]
    fix = "--fix" in sys.argv

    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    sents = doc if isinstance(doc, list) else doc.get("sentences", [])
    gloss = None if isinstance(doc, list) else doc.get("glossary")

    arch = archive_tokens(first, last)
    if not arch:
        print("FAIL  archive: no lines found for %s..%s" % (first, last))
        print("RESULT FAIL"); return 1

    story_words = []
    for s in sents:
        story_words.extend(words(s.get("t", "")))
    fixed, problems, fixes = align(story_words, arch)
    changed = [(o, n) for o, n in zip(story_words, fixed) if o != n]

    if changed and not fix:
        print("FAIL  %d word(s) do not strip back to the archive but are mechanically repairable "
              "(hamza %d, split %d, join %d) — rerun with --fix"
              % (len(changed), fixes["hamza"], fixes["split"], fixes["join"]))
        for o, n in changed[:6]:
            print("      %r -> %r%s" % (o, n, "  (precomposed hamza -> combining mark; "
                  "identical to the eye)" if bare(decomposed(o)) == bare(n) and " " not in n
                  and o != n and len(o) != len(n) else ""))
    if changed and fix:
        apply_to_sentences(sents, fixed)
        print("FIXED %d word(s): hamza %d, split %d, join %d"
              % (len(changed), fixes["hamza"], fixes["split"], fixes["join"]))
        if gloss is not None:
            remap = {}
            for o, n in changed:
                remap.setdefault(o, n)
            newg = {}
            for k, v in gloss.items():
                if k in remap and remap[k] != k:
                    n = remap[k]
                    if " " in n:
                        for half in n.split(" "):
                            newg.setdefault(half, v)
                        print("WARN  glossary key %r split into %s — rewrite the two meanings"
                              % (k, ", ".join(repr(h) for h in n.split(" "))))
                    else:
                        newg[n] = v
                else:
                    newg[decomposed(k) if bare(decomposed(k)) in set(arch) and
                         bare(k) not in set(arch) else k] = v
            doc["glossary"] = newg
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=1)
            fh.write("\n")
        # re-check after writing
        story_words = []
        for s in sents:
            story_words.extend(words(s.get("t", "")))
        fixed2, problems, _ = align(story_words, arch)
        if [bare(w) for w in fixed2] != [bare(w) for w in story_words]:
            problems.append("internal: repair did not converge — report this")

    for p in problems:
        print("FAIL  " + p)
    total = sum(len(words(s.get("t", ""))) for s in sents)
    print("\nsentences %d · words %d · archive tokens %d · %s..%s"
          % (len(sents), total, len(arch), first, last))
    ok = not problems and (fix or not changed)
    print("RESULT %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
