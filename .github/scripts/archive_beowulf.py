#!/usr/bin/env python3
"""
archive_beowulf.py — put an authentic Klaeber-1922 Beowulf text into the repo as
sources/beowulf-fitt-NN-source.json, so an unattended Cowork firing can draft the
poem without a browser and without a human.

WHY THIS EXISTS
    Same reason as archive_khm.py: the Cowork sandbox cannot reach archive.org,
    Wikisource, Gutenberg or heorot.dk (all measured at 000 on 2026-08-20; only
    GitHub answers). A GitHub Actions runner has ordinary internet, so the fetch
    lives here and a scheduled session gets its source with `git fetch`.

WHAT MAKES THIS HARDER THAN THE KHM ARCHIVER
    Klaeber prints þ ð æ *and vowel-length macrons*, and 1922-typeface OCR is
    exactly where those die. A dropped macron is a corrupted reader text that no
    downstream gate would notice. So this script never trusts a witness: it
    proves one against a gold transcript first.

    THE GOLD TRANSCRIPT IS THE WHOLE DESIGN. Lines 53-188 were read by hand off
    the Klaeber page scans in attended sessions and are already published in the
    reader (fitts I and II). That transcript lives at
    .github/fixtures/beowulf-53-188-klaeber1922.txt and is the oracle: a witness
    is usable only if it reproduces those 136 lines CHARACTER-FOR-CHARACTER,
    macrons included. 136 lines is a large enough sample that no plausible OCR
    failure survives it.

TWO MODES
    --bakeoff   fetch every candidate witness, score each against the gold
                transcript, write .github/witness-report.json, write nothing to
                sources/. This is the honest first run: it answers "does an
                adequate machine-readable Klaeber exist?" with evidence rather
                than with hope. ALWAYS SAFE - it cannot corrupt the corpus.
    --archive   use the best passing witness to emit all 44 source files.
                Refuses to write anything at all unless the winning witness
                scored a perfect 136/136 and the derived text covers exactly
                lines 1-3182.

TWO-WITNESS COLLATION
    Klaeber is the edition of record and the only text ever archived. A second
    witness (a public-domain Wyatt 1894 digitisation) is used ONLY to collate:
    where the two disagree on a line, the line is archived with Klaeber's
    reading plus a `variant` recording the other. Those flags are where a
    drafting agent - or Zev - should look. The variant is never silently mixed
    into the text: no hybrid edition is ever produced.

USAGE
    python archive_beowulf.py --bakeoff
    python archive_beowulf.py --archive
    python archive_beowulf.py --selftest      # offline, no network
"""

import argparse
import json
import os
import re
import sys
import unicodedata
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GOLD = os.path.join(ROOT, ".github", "fixtures", "beowulf-53-188-klaeber1922.txt")
REPORT = os.path.join(ROOT, ".github", "witness-report.json")
SOURCES = os.path.join(ROOT, "sources")

TOTAL_LINES = 3182

# ---------------------------------------------------------------------------
# The fitts. Klaeber's continuous Prologue + I-XLIII, from claude/beowulf-fitt-plan.md,
# where the boundaries were verified against three independent sources. Names are
# this project's own display titles; the line range is the citation.
# ---------------------------------------------------------------------------
FITTS = [
    (0,  "Prologue", 1,    52,   "Scyld's Ship-Funeral"),
    (1,  "I",        53,   114,  "The Building of Heorot"),
    (2,  "II",       115,  188,  "Twelve Winters of Grendel"),
    (3,  "III",      189,  257,  "Beowulf Sets Sail"),
    (4,  "IV",       258,  319,  "An Answer on the Shore"),
    (5,  "V",        320,  370,  "At Heorot's Door"),
    (6,  "VI",       371,  455,  "Beowulf's Vow"),
    (7,  "VII",      456,  498,  "Hrothgar's Welcome"),
    (8,  "VIII",     499,  558,  "Unferth's Challenge"),
    (9,  "IX",       559,  661,  "Sea-Monsters and the Queen's Cup"),
    (10, "X",        662,  709,  "The Watch in the Hall"),
    (11, "XI",       710,  790,  "Grendel Comes to Heorot"),
    (12, "XII",      791,  836,  "The Arm Torn Away"),
    (13, "XIII",     837,  924,  "The Song of Sigemund"),
    (14, "XIV",      925,  990,  "Hrothgar Gives Thanks"),
    (15, "XV",       991,  1049, "Gifts for the Victor"),
    (16, "XVI",      1050, 1124, "Hildeburh's Sorrow"),
    (17, "XVII",     1125, 1191, "Hengest's Winter"),
    (18, "XVIII",    1192, 1250, "The Queen's Necklace"),
    (19, "XIX",      1251, 1320, "The Mother's Revenge"),
    (20, "XX",       1321, 1382, "The Haunted Mere"),
    (21, "XXI",      1383, 1472, "Hrunting"),
    (22, "XXII",     1473, 1556, "The Dive"),
    (23, "XXIII",    1557, 1650, "The Giant's Sword"),
    (24, "XXIV",     1651, 1739, "The Golden Hilt"),
    (25, "XXV",      1740, 1816, "The Price of Pride"),
    (26, "XXVI",     1817, 1887, "Farewell to Heorot"),
    (27, "XXVII",    1888, 1962, "The Voyage Home"),
    (28, "XXVIII",   1963, 2038, "Beowulf's Report"),
    (29, "XXIX",     2039, 2092, "The Old Spear-Bearer"),
    (30, "XXX",      2093, 2143, "The Tale Retold"),
    (31, "XXXI",     2144, 2220, "Fifty Winters - and a Dragon"),
    (32, "XXXII",    2221, 2311, "The Hoard and the Last Survivor"),
    (33, "XXXIII",   2312, 2390, "Fire in the Night"),
    (34, "XXXIV",    2391, 2459, "The Sorrow of Hrethel"),
    (35, "XXXV",     2460, 2601, "The Last Boast"),
    (36, "XXXVI",    2602, 2693, "Wiglaf Comes to His Lord"),
    (37, "XXXVII",   2694, 2751, "The Dragon Slain"),
    (38, "XXXVIII",  2752, 2820, "The Barrow Promised"),
    (39, "XXXIX",    2821, 2891, "Wiglaf's Rebuke"),
    (40, "XL",       2892, 2945, "The Messenger's Tidings"),
    (41, "XLI",      2946, 3057, "Ravenswood and the Curse"),
    (42, "XLII",     3058, 3136, "The Hoard Brought Out"),
    (43, "XLIII",    3137, 3182, "The Barrow on the Headland"),
]


def check_fitt_table():
    """The table must be contiguous and sum to the poem. Fatal if not."""
    prev_end = 0
    for _, num, a, b, _ in FITTS:
        if a != prev_end + 1:
            raise SystemExit("FITT TABLE BROKEN: fitt %s starts at %d, previous ended at %d"
                             % (num, a, prev_end))
        if b < a:
            raise SystemExit("FITT TABLE BROKEN: fitt %s ends before it starts" % num)
        prev_end = b
    if prev_end != TOTAL_LINES:
        raise SystemExit("FITT TABLE BROKEN: last line is %d, expected %d" % (prev_end, TOTAL_LINES))


# ---------------------------------------------------------------------------
# Normalisation. Two different things live here, and the difference matters:
#   restore_printing() undoes a digitisation's MECHANICAL re-encodings (caesura
#   spacing, -- for the em dash) and IS applied to what gets archived, because
#   the goal is Klaeber's printed line. The 136-line gold control proves it.
#   fingerprint() is brutal folding used ONLY to match a witness line to a gold
#   line, and never touches anything that is written anywhere.
# ---------------------------------------------------------------------------
BRACKETS = "[]()<>{}"


def restore_printing(line):
    """Undo a digitisation's mechanical re-encodings of Klaeber's printing.

    Perseus carries Klaeber's own text - macrons, brackets, conjectural
    parentheses and all - but encodes two things differently from the page:
    the caesura gap between half-lines becomes a run of spaces, and the em dash
    becomes a double hyphen. Both are re-encodings of typography, not editorial
    choices, so restoring them recovers Klaeber's line rather than inventing
    one. The 136-line gold control is what proves that claim; if this function
    ever over-reaches, the control fails and nothing is archived.
    """
    line = line.replace("\u2014", "--")          # normalise, then re-derive
    line = re.sub(r"-{2,}", "\u2014", line)
    line = re.sub(r"\s+", " ", line).strip()
    line = re.sub(r"\s*\u2014\s*", " \u2014 ", line)      # one space each side
    line = re.sub(r" \u2014 (?=[,.;:!?])", " \u2014", line)  # ... except before punctuation
    return line.strip()


def fingerprint(s):
    """Letters only, diacritics stripped, eth folded to thorn, lowercased.

    Deliberately brutal: it must match a line across editions that differ in
    punctuation, macrons, editorial brackets and thorn/eth choice, because that
    is exactly the class of difference between Klaeber, Wyatt and an OCR pass.
    """
    s = s.lower()
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("ð", "þ").replace("đ", "þ")  # ð, đ -> þ
    s = s.replace("æ", "ae").replace("œ", "oe")
    return re.sub(r"[^a-zþ]", "", s)


def macron_count(s):
    """How many combining macrons the line carries - the OCR canary."""
    d = unicodedata.normalize("NFD", s)
    return d.count("̄")


def load_gold():
    """The oracle: {line_number: exact printed line} for lines 53-188."""
    out = {}
    with open(GOLD, encoding="utf-8") as fh:
        for raw in fh:
            raw = raw.rstrip("\n")
            if not raw.strip():
                continue
            m = re.match(r"^\s*(\d{1,4})\s+(.*)$", raw)
            if not m:
                raise SystemExit("GOLD TRANSCRIPT BROKEN: unnumbered line %r" % raw[:60])
            out[int(m.group(1))] = m.group(2).strip()
    if not out:
        raise SystemExit("GOLD TRANSCRIPT EMPTY: %s" % GOLD)
    lo, hi = min(out), max(out)
    if sorted(out) != list(range(lo, hi + 1)):
        raise SystemExit("GOLD TRANSCRIPT BROKEN: gap between %d and %d" % (lo, hi))
    return out


# ---------------------------------------------------------------------------
# Witnesses. Each returns a list of candidate text lines, in poem order, with
# whatever line numbers it carries stripped into (number_or_None, text).
# ---------------------------------------------------------------------------
UA = {"User-Agent": "lectorium-archiver/1.0 (+https://github.com/zevfarber/Lectorium)"}


def fetch(url, timeout=90):
    req = Request(url, headers=UA)
    with urlopen(req, timeout=timeout) as r:
        raw = r.read()
    for enc in ("utf-8", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", "replace")


def strip_html(html):
    html = re.sub(r"(?is)<(script|style|table|sup|ref)[^>]*>.*?</\1>", " ", html)
    html = re.sub(r"(?i)<br\s*/?>", "\n", html)
    html = re.sub(r"(?i)</(p|div|li|h[1-6])>", "\n", html)
    html = re.sub(r"(?s)<[^>]+>", "", html)
    html = (html.replace("&nbsp;", " ").replace("&amp;", "&")
                .replace("&lt;", "<").replace("&gt;", ">").replace("&#160;", " "))
    return html


LINENUM = re.compile(r"^\s*(\d{1,4})\s+(.+?)\s*$")
TRAILNUM = re.compile(r"^\s*(.+?)\s+(\d{1,4})\s*$")


def split_numbered(text):
    """Turn raw text into (line_number_or_None, line_text) pairs.

    Klaeber and most editions print the numeral in the margin, which lands
    either before or after the verse line depending on the digitisation. Both
    are recognised; a line with no numeral keeps None and is positioned by its
    neighbours later.
    """
    out = []
    for raw in text.split("\n"):
        s = raw.strip()
        if not s:
            continue
        m = LINENUM.match(s)
        if m and len(m.group(2)) > 8:
            out.append((int(m.group(1)), m.group(2).strip()))
            continue
        m = TRAILNUM.match(s)
        if m and len(m.group(1)) > 8:
            out.append((int(m.group(2)), m.group(1).strip()))
            continue
        out.append((None, s))
    return [(n, restore_printing(t)) for n, t in out]


def w_klaeber_ocr():
    """Klaeber 1922 itself, via archive.org's OCR full text. The edition of record."""
    for url in (
        "https://archive.org/download/beowulffightatfi01klae/beowulffightatfi01klae_djvu.txt",
        "https://ia800207.us.archive.org/BookReader/BookReaderJSIA.php?id=beowulffightatfi01klae",
    ):
        try:
            return split_numbered(fetch(url))
        except (URLError, HTTPError, OSError):
            continue
    raise RuntimeError("archive.org unreachable")


def w_perseus_klaeber():
    """Perseus's Beowulf, which carries Klaeber's lineation."""
    url = ("https://www.perseus.tufts.edu/hopper/dltext?doc=Perseus%3Atext%3A2003.01.0001")
    return split_numbered(strip_html(fetch(url)))


def w_wyatt_wikisource():
    """Wyatt 1894 (public domain) via Wikisource - collation witness only."""
    api = ("https://en.wikisource.org/w/index.php?action=raw&title=")
    parts = []
    for title in ("Beowulf_(Wyatt)", "Beowulf"):
        try:
            parts.append(fetch(api + title))
        except (URLError, HTTPError, OSError):
            continue
    if not parts:
        raise RuntimeError("wikisource unreachable")
    return split_numbered(strip_html("\n".join(parts)))


def w_wyatt_oll():
    """Wyatt 1894 via the Online Library of Liberty - collation witness only."""
    url = "https://oll.libertyfund.org/titles/wyatt-beowulf-original-lang"
    return split_numbered(strip_html(fetch(url)))


def w_ang_wikisource():
    url = "https://ang.wikisource.org/w/index.php?action=raw&title=B%C4%93owulf"
    return split_numbered(strip_html(fetch(url)))


WITNESSES = [
    ("klaeber-archive-ocr", "Klaeber 1922 (edition of record), archive.org OCR", True,  w_klaeber_ocr),
    ("perseus-klaeber",     "Perseus Beowulf, Klaeber lineation",                True,  w_perseus_klaeber),
    ("wyatt-wikisource",    "Wyatt 1894 via Wikisource",                         False, w_wyatt_wikisource),
    ("wyatt-oll",           "Wyatt 1894 via Online Library of Liberty",          False, w_wyatt_oll),
    ("ang-wikisource",      "Old English Wikisource Beowulf",                    False, w_ang_wikisource),
]


# ---------------------------------------------------------------------------
# Scoring a witness against the gold transcript
# ---------------------------------------------------------------------------
def score(lines, gold):
    """How well does this witness reproduce the 136 hand-verified lines?

    exact   - character-for-character, macrons included. The only score that
              licenses archiving.
    matched - found at all (fingerprint match). A witness with high matched and
              low exact is a real Beowulf whose orthography we cannot trust.
    """
    index = {}
    for i, (_, text) in enumerate(lines):
        fp = fingerprint(text)
        if len(fp) >= 12:
            index.setdefault(fp, i)

    exact = matched = 0
    gold_macrons = witness_macrons = 0
    misses, mismatches = [], []
    for n in sorted(gold):
        g = gold[n]
        gold_macrons += macron_count(g)
        i = index.get(fingerprint(g))
        if i is None:
            misses.append(n)
            continue
        matched += 1
        w = lines[i][1]
        witness_macrons += macron_count(w)
        if w == g:
            exact += 1
        elif len(mismatches) < 400:
            mismatches.append({"line": n, "gold": g, "witness": w})
    return {
        "lines_fetched": len(lines),
        "gold_lines": len(gold),
        "matched": matched,
        "exact": exact,
        "gold_macrons": gold_macrons,
        "witness_macrons": witness_macrons,
        "macron_ratio": round(witness_macrons / gold_macrons, 4) if gold_macrons else None,
        "missing_lines": misses[:20],
        "sample_mismatches": mismatches,
        "usable_as_edition": matched == len(gold) and exact == len(gold),
    }


def bakeoff():
    check_fitt_table()
    gold = load_gold()
    report = {"gold_lines": len(gold), "witnesses": []}
    for key, desc, is_klaeber, fn in WITNESSES:
        entry = {"key": key, "description": desc, "is_edition_of_record": is_klaeber}
        try:
            lines = fn()
            entry.update(score(lines, gold))
        except Exception as exc:                                   # noqa: BLE001
            entry.update({"error": "%s: %s" % (type(exc).__name__, exc), "usable_as_edition": False})
        report["witnesses"].append(entry)
        print("%-22s %s" % (key, json.dumps({k: v for k, v in entry.items()
                                             if k in ("matched", "exact", "macron_ratio", "error")})))

    # Dump the best edition-of-record witness in full, so a later session can
    # develop against real data instead of guessing from a 12-line sample.
    best = max((w for w in report["witnesses"] if w["is_edition_of_record"]),
               key=lambda w: w.get("exact", 0) * 1000 + w.get("matched", 0), default=None)
    if best and best.get("matched"):
        try:
            lines = dict((k, f) for k, _, _, f in WITNESSES)[best["key"]]()
            with open(os.path.join(ROOT, ".github", "witness-dump.txt"), "w", encoding="utf-8") as fh:
                for n, t in lines:
                    fh.write("%s\t%s\n" % ("" if n is None else n, t))
            report["dump"] = ".github/witness-dump.txt (%s, %d lines)" % (best["key"], len(lines))
        except Exception as exc:                                   # noqa: BLE001
            report["dump"] = "dump failed: %s" % exc

    winners = [w for w in report["witnesses"] if w.get("usable_as_edition") and w["is_edition_of_record"]]
    report["verdict"] = ("ARCHIVE-READY: " + winners[0]["key"]) if winners else \
        "NO ADEQUATE KLAEBER WITNESS - the automated route is blocked; see the plan's decision (a)/(b)/(c)"
    report["winner"] = winners[0]["key"] if winners else None
    os.makedirs(os.path.dirname(REPORT), exist_ok=True)
    with open(REPORT, "w", encoding="utf-8") as fh:
        json.dump(report, fh, ensure_ascii=False, indent=2)
    print("\nVERDICT: " + report["verdict"])
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write("### Beowulf witness bake-off\n\n")
            fh.write("| witness | matched / %d | exact | macrons kept |\n|---|---|---|---|\n" % len(gold))
            for w in report["witnesses"]:
                fh.write("| `%s` | %s | %s | %s |\n" % (
                    w["key"], w.get("matched", "-"), w.get("exact", w.get("error", "-")),
                    w.get("macron_ratio", "-")))
            fh.write("\n**%s**\n" % report["verdict"])
    return 0 if winners else 0     # never fail the job: a negative result IS the finding


# ---------------------------------------------------------------------------
# Archiving
# ---------------------------------------------------------------------------
def number_lines(lines, gold):
    """Give every witness line its Klaeber number.

    Prefer the witness's own numerals. Where it has none, count forward from the
    nearest numbered anchor. Verified afterwards against the gold transcript, so
    an off-by-one anywhere in the poem is caught rather than shipped.
    """
    numbered = {}
    anchor = None
    for num, text in lines:
        if num is not None and 1 <= num <= TOTAL_LINES:
            numbered[num] = text
            anchor = num
        elif anchor is not None:
            anchor += 1
            if anchor <= TOTAL_LINES:
                numbered.setdefault(anchor, text)
    return numbered


def archive():
    check_fitt_table()
    gold = load_gold()
    if not os.path.exists(REPORT):
        raise SystemExit("No witness report. Run --bakeoff first.")
    with open(REPORT, encoding="utf-8") as fh:
        report = json.load(fh)
    if not report.get("winner"):
        raise SystemExit("REFUSING TO ARCHIVE: %s" % report.get("verdict"))

    fn = dict((k, f) for k, _, _, f in WITNESSES)[report["winner"]]
    primary = number_lines(fn(), gold)

    # Control 1: the gold lines must come back exactly, at the right numbers.
    bad = [n for n, g in gold.items() if primary.get(n) != g]
    if bad:
        raise SystemExit("REFUSING TO ARCHIVE: %d of %d gold lines wrong (first: %s)"
                         % (len(bad), len(gold), bad[:5]))
    # Control 2: the poem must be complete.
    missing = [n for n in range(1, TOTAL_LINES + 1) if n not in primary]
    if missing:
        raise SystemExit("REFUSING TO ARCHIVE: %d lines missing (first: %s)"
                         % (len(missing), missing[:5]))

    # Collation witness, used only to flag disagreement.
    collation = {}
    for key, _, is_klaeber, cfn in WITNESSES:
        if is_klaeber or key == report["winner"]:
            continue
        try:
            collation = number_lines(cfn(), gold)
            break
        except Exception:                                          # noqa: BLE001
            continue

    os.makedirs(SOURCES, exist_ok=True)
    written = 0
    for idx, num, a, b, name in FITTS:
        text_lines = [{"n": n, "t": primary[n]} for n in range(a, b + 1)]
        variants = []
        for n in range(a, b + 1):
            other = collation.get(n)
            if other and fingerprint(other) != fingerprint(primary[n]):
                variants.append({"n": n, "klaeber": primary[n], "collation": other})
        doc = {
            "id": "beowulf-prologue" if idx == 0 else "beowulf-fitt-%02d" % idx,
            "fitt": num,
            "name": name,
            "lines": [a, b],
            "line_count": b - a + 1,
            "tokens": sum(len(l["t"].split()) for l in text_lines),
            "edition": "Klaeber, Beowulf and the Fight at Finnsburg, 1st ed., 1922",
            "witness": report["winner"],
            "collation_witness": None if not collation else "second witness, flags only",
            "variants": variants,
            "text_lines": text_lines,
        }
        path = os.path.join(SOURCES, "beowulf-fitt-%02d-source.json" % idx)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(doc, fh, ensure_ascii=False, indent=1)
        written += 1
    print("Archived %d source files, %d lines, controls green." % (written, TOTAL_LINES))
    return 0


# ---------------------------------------------------------------------------
# Offline selftest - runs on every invocation, no network
# ---------------------------------------------------------------------------
def selftest():
    check_fitt_table()
    gold = load_gold()
    assert len(gold) == 136, "gold transcript should hold lines 53-188, has %d" % len(gold)

    # A perfect witness scores perfect.
    perfect = [(n, t) for n, t in sorted(gold.items())]
    s = score(perfect, gold)
    assert s["usable_as_edition"], "a perfect witness must pass: %r" % s

    # Injected defect 1: macrons stripped. Must match but NOT be usable.
    flat = [(n, unicodedata.normalize("NFC", "".join(
        c for c in unicodedata.normalize("NFD", t) if c != "̄"))) for n, t in perfect]
    s = score(flat, gold)
    assert s["matched"] == 136 and not s["usable_as_edition"], \
        "macron-stripped OCR must be caught: %r" % s
    assert s["macron_ratio"] == 0.0

    # Injected defect 2: thorn to th. Fingerprint still matches; exact must not.
    thorned = [(n, t.replace("þ", "th").replace("ð", "th")) for n, t in perfect]
    s = score(thorned, gold)
    assert not s["usable_as_edition"], "th-substituted text must be caught"

    # Injected defect 3: a dropped line must show as missing.
    s = score(perfect[:-1], gold)
    assert s["matched"] == 135 and 188 in s["missing_lines"], "a dropped line must be caught"

    # Numbering: unnumbered lines take their place from the previous anchor.
    numbered = number_lines([(53, "a"), (None, "b"), (None, "c"), (56, "d")], gold)
    assert numbered[54] == "b" and numbered[55] == "c" and numbered[56] == "d"

    print("selftest OK: fitt table sums to %d, gold holds %d lines, 5 controls pass"
          % (TOTAL_LINES, len(gold)))
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bakeoff", action="store_true")
    ap.add_argument("--archive", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    selftest()                       # always, before anything touches the network
    if args.selftest:
        return 0
    if args.bakeoff:
        return bakeoff()
    if args.archive:
        return archive()
    ap.error("choose --bakeoff, --archive or --selftest")


if __name__ == "__main__":
    sys.exit(main())
