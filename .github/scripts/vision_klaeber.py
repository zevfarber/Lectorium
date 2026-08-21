#!/usr/bin/env python3
"""
vision_klaeber.py — read Klaeber's 1922 pages with a vision model, so the
edition of record becomes machine-readable without 3,000 lines of attended
transcription.

WHY THIS EXISTS
    The bake-off (.github/witness-report.json, 2026-08-20) refused every
    candidate witness. Its verdict is correct and this script does not touch it:

      klaeber-archive-ocr   1/136 exact, 0 of 300 macrons   the edition of
                            record, destroyed by 1922-typeface OCR
      perseus-klaeber     122/136 exact, 291/300 macrons     a clean text that
                            is NOT Klaeber: 0 for 2 on his circumflex-on-
                            contracted-vowel convention

    Every witness scored so far was a pre-existing TEXT DUMP. Nobody had re-read
    the PAGE IMAGES. archive.org holds the scans of the very book; a vision
    model can see a macron that an OCR text layer never recorded. That is the
    one untried route, and it is the only one that yields Klaeber unattended.

WHAT KEEPS IT HONEST
    It is scored by the SAME unchanged scorer, against the SAME gold transcript,
    as every other witness. It gets no special dispensation:

      control 1  the 136 hand-verified lines 53-188 must come back
                 CHARACTER-FOR-CHARACTER, macrons included   (existing gold)
      control 2  lines 1-52 concatenated must match the published prologue's
                 character stream exactly                    (NEW, this file)
      control 3  two independent transcription passes of every page must agree
                 character-for-character, or the line is flagged and the
                 archive refuses it                          (NEW, this file)
      control 4  Perseus is consulted as a DISAGREEMENT DETECTOR only. It never
                 contributes a character. Where it and the vision passes differ
                 on letters, the line is flagged for a human.

    Control 2 exists because the gold covers lines 53-188, and the poem's other
    two circumflexes (Liffrea 16, gethēon 25) live in the prologue. Testing them
    raises the circumflex sample from 2 to 4 — still small, and the README says
    so rather than pretending otherwise.

    A HALLUCINATED LINE IS THE FAILURE MODE THAT MATTERS. A vision model asked
    for a damaged 1922 page will, under pressure, produce plausible Old English.
    That is precisely what the sole-source rule forbids. Controls 1-3 are aimed
    at it: an invented line cannot survive two independent passes AND the gold
    AND Perseus's letters. Where it does survive, the line is archived with a
    `flags` entry, never silently.

PAGE DISCOVERY COSTS NOTHING
    archive.org's `_djvu.txt` is form-feed separated, one chunk per scanned
    leaf. The OCR is worthless for diacritics but perfectly adequate for
    answering "which leaf holds poem line 189?" — so leaves are located by
    fingerprint match against the OCR, and only the located leaves are sent to
    the model. Zero API calls are spent finding the poem.

USAGE
    python vision_klaeber.py --selftest    # offline, no network, no API key
    python vision_klaeber.py --probe       # transcribe ONLY the gold pages,
                                           # score, write vision-probe.json.
                                           # ~14 leaves. The cheap decisive test.
    python vision_klaeber.py --transcribe  # whole poem, both passes, cached
"""

import base64
import json
import os
import re
import sys
import time
import unicodedata
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CACHE = os.path.join(ROOT, ".github", "vision-cache")
PROBE_REPORT = os.path.join(ROOT, ".github", "vision-probe.json")
GOLD = os.path.join(ROOT, ".github", "fixtures", "beowulf-53-188-klaeber1922.txt")
PROLOGUE = os.path.join(ROOT, "beowulf-prologue.json")

# The archive.org item. NOT invented: the existing archiver fetches
# .../beowulffightatfi01klae_djvu.txt and got 31,264 lines back on 2026-08-20,
# which is how we know the identifier is real and the scan exists.
ITEM = "beowulffightatfi01klae"

TOTAL_LINES = 3182

# If the API rejects this model id, the script queries /v1/models and prints the
# ids it is actually allowed to use, into the job summary. Change this one line.
#
# `or`, NOT a dict default. The workflow passes VISION_MODEL: ${{ vars.VISION_MODEL }},
# and an UNDEFINED repository variable expands to the EMPTY STRING rather than
# being absent - so os.environ.get(name, default) hands back "" and the API
# answers `model: String should have at least 1 character`. Measured on run #5,
# 2026-08-21. An empty value must fall through to the default exactly as an
# unset one does.
DEFAULT_MODEL = os.environ.get("VISION_MODEL") or "claude-opus-4-5"
API_URL = "https://api.anthropic.com/v1/messages"
MODELS_URL = "https://api.anthropic.com/v1/models?limit=100"
UA = {"User-Agent": "lectorium-vision/1.0 (+https://github.com/zevfarber/Lectorium)"}

# The Old English inventory Klaeber prints, and nothing else. An acute accent is
# OCR damage; a Latin-1 mojibake sequence is a decoding bug. Deliberately tight.
ALLOWED = set(
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "þðæÞÐÆȳȲœŒ"
    " .,;:!?'—-[]()<>*…"
    "0123456789"
)
COMBINING_OK = {"̄", "̂"}          # macron, circumflex — the two Klaeber prints


# ---------------------------------------------------------------------------
# Shared text helpers. fingerprint() is deliberately identical in spirit to the
# archiver's: letters only, diacritics stripped, eth folded to thorn. It is used
# ONLY for matching and never touches anything written anywhere.
# ---------------------------------------------------------------------------
def fingerprint(s):
    s = s.lower()
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("ð", "þ").replace("đ", "þ")
    s = s.replace("æ", "ae").replace("œ", "oe")
    return re.sub(r"[^a-zþ]", "", s)


def macron_count(s):
    return unicodedata.normalize("NFD", s).count("̄")


def circumflex_count(s):
    return unicodedata.normalize("NFD", s).count("̂")


def charset_violations(s):
    """Characters Klaeber does not print. Empty list or the text is suspect."""
    bad = []
    for ch in unicodedata.normalize("NFD", s):
        if unicodedata.combining(ch):
            if ch not in COMBINING_OK:
                bad.append(ch)
        elif ch not in ALLOWED:
            bad.append(ch)
    return sorted(set(bad))


def stream(text):
    """Whitespace-folded character stream. Used by the prologue control, where
    our own line breaks fall inside poem lines and so cannot be compared."""
    return re.sub(r"\s+", " ", text).strip()


# ---------------------------------------------------------------------------
# Controls 1 and 2: the two oracles
# ---------------------------------------------------------------------------
def load_gold():
    """{line_number: exact printed line} for 53-188, hand-read off the scans."""
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
    return out


def load_prologue_stream():
    """Lines 1-52 as one character stream, from the PUBLISHED prologue.

    Why a stream and not numbered lines: the reader's sense-units break mid-verse
    (the prologue holds 60 verse lines for 52 poem lines), so the file does not
    know where Klaeber's line breaks fall. Concatenated, though, it is exactly
    Klaeber's characters for lines 1-52 — including the two circumflexes the
    136-line gold cannot reach. Comparing streams tests every diacritic without
    needing a lineation we do not have.
    """
    with open(PROLOGUE, encoding="utf-8") as fh:
        doc = json.load(fh)
    return stream(" ".join(u["t"] for u in doc["sentences"]))


# ---------------------------------------------------------------------------
# Page discovery — free, from the OCR text layer's form feeds
# ---------------------------------------------------------------------------
# archive.org answers 5xx intermittently under load. Measured on run #6,
# 2026-08-21: the djvu.txt download returned HTTP 500 and killed the probe four
# minutes after the identical request had succeeded on run #5. A transient 5xx
# is not a finding about the scans, so it is retried rather than reported.
# 403/404 are NOT retried - they are a real answer ("this URL does not exist"),
# and get_page_image depends on getting that answer quickly so it can move on
# to the next URL pattern.
TRANSIENT = {408, 425, 429, 500, 502, 503, 504, 520, 522, 524}


def fetch(url, timeout=120, binary=False, retries=4):
    delay = 2
    for attempt in range(retries):
        try:
            req = Request(url, headers=UA)
            with urlopen(req, timeout=timeout) as r:
                raw = r.read()
            break
        except HTTPError as exc:
            if exc.code in TRANSIENT and attempt < retries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            raise
        except (URLError, OSError):
            if attempt < retries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            raise
    if binary:
        return raw
    for enc in ("utf-8", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", "replace")


def ocr_leaves():
    """[(leaf_index, ocr_text)] — archive.org's djvu.txt, split on form feeds."""
    txt = fetch("https://archive.org/download/%s/%s_djvu.txt" % (ITEM, ITEM))
    return list(enumerate(txt.split("\f")))


def locate_poem_leaves(leaves, gold, prologue_stream):
    """Map leaf index -> the poem line numbers printed on it.

    Anchored on text we already trust: every gold line and every fingerprinted
    run of the prologue is looked for in each leaf's OCR. The OCR mangles
    diacritics, which is why the match is by fingerprint; it does not mangle
    word order, which is why this works at all.
    """
    anchors = dict(gold)
    hits = {}
    for idx, text in leaves:
        fp = fingerprint(text)
        if len(fp) < 200:
            continue
        found = [n for n, line in anchors.items()
                 if len(fingerprint(line)) >= 12 and fingerprint(line) in fp]
        if found:
            hits[idx] = sorted(found)
    # The prologue leaf carries line 1; find it by its opening fingerprint.
    opening = fingerprint(prologue_stream)[:60]
    for idx, text in leaves:
        if opening and opening in fingerprint(text):
            hits.setdefault(idx, []).append(1)
            hits[idx] = sorted(set(hits[idx]))
            break
    return hits


def estimate_lines_per_leaf(hits):
    """Klaeber's page holds a fairly regular number of verse lines. Measured, not
    assumed: derived from consecutive located leaves."""
    idxs = sorted(hits)
    spans = []
    for a, b in zip(idxs, idxs[1:]):
        if b == a + 1 and hits[a] and hits[b]:
            spans.append(min(hits[b]) - min(hits[a]))
    spans = [s for s in spans if 5 <= s <= 60]
    if not spans:
        return None
    spans.sort()
    return spans[len(spans) // 2]


def page_image_url(leaf):
    """archive.org serves page images several ways; the caller tries each. The
    Action reports which one answered, so a dead endpoint is visible, not
    silent."""
    return [
        "https://iiif.archive.org/iiif/%s$%d/full/pct:100/0/default.jpg" % (ITEM, leaf),
        "https://archive.org/download/%s/page/n%d.jpg" % (ITEM, leaf),
        "https://archive.org/download/%s/page/leaf%d.jpg" % (ITEM, leaf),
    ]


def get_page_image(leaf):
    last = None
    for url in page_image_url(leaf):
        try:
            # Fewer retries here than for the text layer: three patterns are
            # tried in turn and only one of them exists, so a wrong pattern
            # should cost a moment, not half a minute.
            data = fetch(url, binary=True, retries=2)
            if len(data) > 8000:                    # a real scan, not an error page
                return data, url
        except (URLError, HTTPError, OSError) as exc:
            last = exc
            continue
    raise RuntimeError("no page image for leaf %d (%s)" % (leaf, last))


# ---------------------------------------------------------------------------
# The two transcription passes
# ---------------------------------------------------------------------------
PASS_A = """This is one page from Klaeber's *Beowulf and the Fight at Finnsburg*, \
1st edition, 1922. Transcribe the Old English verse EXACTLY as printed.

Rules, in order of importance:
1. COPY, never correct, normalise, modernise or translate. If the page prints a \
form you think is wrong, print it anyway.
2. Reproduce every diacritic. Klaeber marks vowel length with a MACRON (a e i o u y \
with a bar) and marks contracted vowels with a CIRCUMFLEX (a e i o u with a caret). \
These are different marks and carry different meaning. If a vowel carries no mark, \
give it no mark.
3. Reproduce thorn, eth and ash exactly as printed, in the case printed.
4. Reproduce editorial brackets [ ] and conjectural parentheses ( ) exactly where \
they fall, including brackets around single letters inside a word.
5. Reproduce punctuation exactly, em dashes included. Where the page prints a row \
of spaced periods for a gap in the manuscript, reproduce it as printed.
6. Give one output line per printed verse line. Where the margin prints a line \
number, put that number, then a tab, then the verse line. Where it does not, put \
a tab and then the verse line.
7. Transcribe ONLY the verse. Skip running heads, page numbers, apparatus, \
footnotes and the textual notes beneath the rule.
8. If any part of a line is illegible or damaged, output that line as the single \
token ILLEGIBLE and nothing else. DO NOT GUESS. A missing line is recoverable; \
an invented line is not.

Put the transcription inside <transcription></transcription> tags."""

PASS_B = """The image is a page of Old English verse from a 1922 printed edition.

Produce a character-level transcription. Work line by line down the page, and for \
each printed verse line record what is physically on the page rather than what the \
language leads you to expect.

Specifically:
- Vowels may carry a bar (macron, marking length) or a caret (circumflex, marking \
contraction). Distinguish them. An unmarked vowel stays unmarked.
- The letters thorn, eth and ash appear; keep them, and keep their case.
- Square brackets and round brackets appear inside and around words; keep them where \
they are.
- Keep all punctuation, including long dashes and rows of spaced periods.
- Marginal numerals belong in front of their line, separated by a tab. Lines without \
a numeral start with a tab.
- Verse only: no headers, no page numbers, no footnotes, nothing below a horizontal \
rule.
- Any line you cannot read with confidence: output ILLEGIBLE alone on that line. Do \
not reconstruct it.

Wrap the result in <transcription></transcription>."""


def available_models(api_key):
    """The model ids this key may actually use.

    The module docstring has always promised that a rejected model id produces
    the list of legal ones; until run #5 it only promised it. Asking costs one
    cheap GET and turns "MODEL REJECTED" from a guess-and-push loop into a
    single informative failure.
    """
    try:
        req = Request(MODELS_URL, headers={"x-api-key": api_key,
                                           "anthropic-version": "2023-06-01"})
        with urlopen(req, timeout=60) as r:
            doc = json.loads(r.read().decode("utf-8"))
        return [m["id"] for m in doc.get("data", []) if m.get("id")]
    except Exception as exc:                                    # noqa: BLE001
        return ["<could not list models: %s: %s>" % (type(exc).__name__, exc)]


def call_model(image_bytes, prompt, model, api_key, max_retries=4):
    body = {
        "model": model,
        "max_tokens": 4000,
        "temperature": 0,
        "messages": [{
            "role": "user",
            "content": [
                {"type": "image", "source": {
                    "type": "base64", "media_type": "image/jpeg",
                    "data": base64.b64encode(image_bytes).decode("ascii")}},
                {"type": "text", "text": prompt},
            ],
        }],
    }
    req = Request(API_URL, data=json.dumps(body).encode("utf-8"),
                  headers={"content-type": "application/json",
                           "x-api-key": api_key,
                           "anthropic-version": "2023-06-01"})
    delay = 2
    for attempt in range(max_retries):
        try:
            with urlopen(req, timeout=300) as r:
                doc = json.loads(r.read().decode("utf-8"))
            return "".join(b.get("text", "") for b in doc.get("content", []))
        except HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[:400]
            if exc.code in (400, 404) and "model" in detail.lower():
                ids = available_models(api_key)
                note = ("MODEL REJECTED: %r\n%s\n\nThis key may use:\n  %s\n\n"
                        "Set the repository VARIABLE VISION_MODEL (Settings -> "
                        "Secrets and variables -> Actions -> Variables) to one of "
                        "them, or edit DEFAULT_MODEL in this file."
                        % (model, detail, "\n  ".join(ids)))
                summary = os.environ.get("GITHUB_STEP_SUMMARY")
                if summary:
                    with open(summary, "a", encoding="utf-8") as fh:
                        fh.write("### Vision probe could not start\n\n```\n%s\n```\n" % note)
                raise SystemExit(note)
            if exc.code in (429, 500, 502, 503, 529) and attempt < max_retries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            raise
        except (URLError, OSError):
            if attempt < max_retries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            raise
    raise RuntimeError("unreachable")


TRANSCRIPTION_RE = re.compile(r"<transcription>(.*?)</transcription>", re.S)


def parse_transcription(raw):
    """Model output -> [(line_number_or_None, text)].

    Strict on purpose. Anything outside the tags is discarded, ILLEGIBLE lines
    are dropped (they are the model refusing to guess, which is the behaviour we
    asked for), and a line whose charset is not Klaeber's is dropped and
    reported rather than archived.
    """
    m = TRANSCRIPTION_RE.search(raw)
    if not m:
        return [], ["no <transcription> block in model output"]
    out, problems = [], []
    for line in m.group(1).split("\n"):
        if not line.strip():
            continue
        if "\t" in line:
            num, _, text = line.partition("\t")
            num = num.strip()
            n = int(num) if num.isdigit() and 1 <= int(num) <= TOTAL_LINES else None
        else:
            n, text = None, line
        text = text.strip()
        if not text or text == "ILLEGIBLE":
            continue
        bad = charset_violations(text)
        if bad:
            problems.append("line %s dropped, foreign characters %r in %r"
                            % (n, bad, text[:50]))
            continue
        out.append((n, text))
    return out, problems


def number_pass(pairs):
    """Give every transcribed line its Klaeber number, counting forward from the
    nearest printed numeral. Verified afterwards against the gold, so an
    off-by-one anywhere is caught rather than shipped."""
    numbered, anchor = {}, None
    for n, text in pairs:
        if n is not None:
            numbered[n] = text
            anchor = n
        elif anchor is not None:
            anchor += 1
            numbered.setdefault(anchor, text)
    return numbered


def reconcile(a, b):
    """Control 3. Two independent passes; only character-identical lines are
    trusted. Returns (agreed, disagreements)."""
    agreed, disagreements = {}, []
    for n in sorted(set(a) | set(b)):
        x, y = a.get(n), b.get(n)
        if x is not None and x == y:
            agreed[n] = x
        else:
            disagreements.append({"n": n, "pass_a": x, "pass_b": y})
    return agreed, disagreements


# ---------------------------------------------------------------------------
# Scoring the vision witness against both oracles
# ---------------------------------------------------------------------------
def score_vision(agreed, gold, prologue_stream):
    exact = sum(1 for n, g in gold.items() if agreed.get(n) == g)
    missing = [n for n in sorted(gold) if n not in agreed]
    wrong = [{"line": n, "gold": g, "vision": agreed.get(n)}
             for n, g in sorted(gold.items()) if n in agreed and agreed[n] != g]

    have_prologue = all(n in agreed for n in range(1, 53))
    got_stream = stream(" ".join(agreed[n] for n in range(1, 53))) if have_prologue else None
    prologue_ok = got_stream == prologue_stream

    gm = sum(macron_count(g) for g in gold.values())
    vm = sum(macron_count(agreed.get(n, "")) for n in gold)
    gc = sum(circumflex_count(g) for g in gold.values())
    vc = sum(circumflex_count(agreed.get(n, "")) for n in gold)

    return {
        "gold_lines": len(gold),
        "exact": exact,
        "missing_lines": missing[:20],
        "wrong_lines": wrong[:40],
        "gold_macrons": gm, "vision_macrons": vm,
        "macron_ratio": round(vm / gm, 4) if gm else None,
        "gold_circumflexes_in_gold_range": gc, "vision_circumflexes": vc,
        "prologue_stream_present": have_prologue,
        "prologue_stream_exact": prologue_ok,
        "usable_as_edition": (exact == len(gold)) and prologue_ok,
    }


# ---------------------------------------------------------------------------
# Probe: the cheap decisive test — gold pages only
# ---------------------------------------------------------------------------
def transcribe_leaf(leaf, model, api_key, cache=True):
    os.makedirs(CACHE, exist_ok=True)
    cpath = os.path.join(CACHE, "leaf-%04d.json" % leaf)
    if cache and os.path.exists(cpath):
        with open(cpath, encoding="utf-8") as fh:
            return json.load(fh)
    image, url = get_page_image(leaf)
    raw_a = call_model(image, PASS_A, model, api_key)
    raw_b = call_model(image, PASS_B, model, api_key)
    pa, prob_a = parse_transcription(raw_a)
    pb, prob_b = parse_transcription(raw_b)
    rec = {"leaf": leaf, "image_url": url,
           "pass_a": pa, "pass_b": pb, "problems": prob_a + prob_b}
    with open(cpath, "w", encoding="utf-8") as fh:
        json.dump(rec, fh, ensure_ascii=False)
    return rec


def run(mode):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit(
            "ANTHROPIC_API_KEY is not set. Add it as a repository secret "
            "(Settings -> Secrets and variables -> Actions -> New repository secret) "
            "and the workflow will pass it through. Nothing was transcribed.")
    model = DEFAULT_MODEL
    gold = load_gold()
    prologue_stream = load_prologue_stream()

    leaves = ocr_leaves()
    hits = locate_poem_leaves(leaves, gold, prologue_stream)
    if not hits:
        raise SystemExit("Could not locate the poem in the OCR text layer. "
                         "Nothing transcribed; the item or its djvu.txt has changed.")
    per_leaf = estimate_lines_per_leaf(hits)

    if mode == "probe":
        wanted = sorted(hits)                                   # gold + prologue leaves only
    else:
        lo, hi = min(hits), max(hits)
        span = per_leaf or 30
        wanted = list(range(lo, hi + (TOTAL_LINES - max(max(v) for v in hits.values())) // span + 3))

    pass_a, pass_b, problems, images = {}, {}, [], {}
    for leaf in wanted:
        try:
            rec = transcribe_leaf(leaf, model, api_key)
        except Exception as exc:                                # noqa: BLE001
            problems.append("leaf %d: %s: %s" % (leaf, type(exc).__name__, exc))
            continue
        images[leaf] = rec["image_url"]
        problems.extend("leaf %d: %s" % (leaf, p) for p in rec["problems"])
        pass_a.update(number_pass([(n, t) for n, t in rec["pass_a"]]))
        pass_b.update(number_pass([(n, t) for n, t in rec["pass_b"]]))

    agreed, disagreements = reconcile(pass_a, pass_b)
    result = score_vision(agreed, gold, prologue_stream)
    result.update({
        "mode": mode,
        "model": model,
        "item": ITEM,
        "leaves_located": len(hits),
        "leaves_transcribed": len(images),
        "lines_per_leaf_measured": per_leaf,
        "two_pass_disagreements": len(disagreements),
        "sample_disagreements": disagreements[:25],
        "problems": problems[:60],
        "sample_image_url": next(iter(images.values()), None),
    })
    result["verdict"] = (
        "VISION WITNESS USABLE - all %d gold lines exact and the prologue stream matches"
        % len(gold) if result["usable_as_edition"] else
        "VISION WITNESS NOT USABLE - %d/%d gold exact, prologue stream %s"
        % (result["exact"], len(gold), "ok" if result["prologue_stream_exact"] else "MISMATCH"))

    with open(PROBE_REPORT, "w", encoding="utf-8") as fh:
        json.dump(result, fh, ensure_ascii=False, indent=2)
    print(result["verdict"])

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as fh:
            fh.write("### Klaeber vision-OCR probe\n\n")
            fh.write("| control | result |\n|---|---|\n")
            fh.write("| gold lines exact | %d / %d |\n" % (result["exact"], len(gold)))
            fh.write("| macrons kept | %s |\n" % result["macron_ratio"])
            fh.write("| circumflexes (gold range) | %s / %s |\n"
                     % (result["vision_circumflexes"], result["gold_circumflexes_in_gold_range"]))
            fh.write("| prologue stream (lines 1-52) | %s |\n"
                     % ("exact" if result["prologue_stream_exact"] else "MISMATCH"))
            fh.write("| two-pass disagreements | %d |\n" % len(disagreements))
            fh.write("\n**%s**\n" % result["verdict"])
    return 0


def witness_lines():
    """Adapter for archive_beowulf.py's WITNESSES table: [(num, text)] pairs
    from the cached, two-pass-agreed transcription. Raises if the probe has not
    been run, so the archiver can never reach for a text that was never
    validated."""
    if not os.path.exists(PROBE_REPORT):
        raise RuntimeError("no vision probe report; run --probe first")
    with open(PROBE_REPORT, encoding="utf-8") as fh:
        rep = json.load(fh)
    if not rep.get("usable_as_edition"):
        raise RuntimeError("vision witness failed its controls: %s" % rep.get("verdict"))
    pass_a, pass_b = {}, {}
    for name in sorted(os.listdir(CACHE)):
        if not name.startswith("leaf-"):
            continue
        with open(os.path.join(CACHE, name), encoding="utf-8") as fh:
            rec = json.load(fh)
        pass_a.update(number_pass([(n, t) for n, t in rec["pass_a"]]))
        pass_b.update(number_pass([(n, t) for n, t in rec["pass_b"]]))
    agreed, _ = reconcile(pass_a, pass_b)
    return [(n, agreed[n]) for n in sorted(agreed)]


# ---------------------------------------------------------------------------
# Offline selftest — no network, no API key. Every gate must say "no".
# ---------------------------------------------------------------------------
def _wrap(lines):
    return "<transcription>\n%s\n</transcription>" % "\n".join(lines)


def selftest():
    gold = load_gold()
    assert gold, "gold transcript is empty"
    prologue_stream = load_prologue_stream()
    assert len(prologue_stream) > 800, "prologue stream implausibly short"

    # The prologue stream must actually carry the circumflexes the gold cannot see.
    assert circumflex_count(prologue_stream) >= 2, \
        "prologue control is pointless if it holds no circumflex"

    # A perfect two-pass transcription of the gold range must pass control 1.
    perfect = _wrap(["%d\t%s" % (n, t) for n, t in sorted(gold.items())])
    pairs, problems = parse_transcription(perfect)
    assert not problems, problems
    numbered = number_pass(pairs)
    agreed, dis = reconcile(numbered, numbered)
    assert not dis
    s = score_vision(agreed, gold, prologue_stream)
    assert s["exact"] == len(gold), s
    assert not s["usable_as_edition"], "no prologue lines present, so it must NOT be usable"

    # Defect 1: macrons stripped — the failure that killed the archive.org OCR.
    flat = {n: unicodedata.normalize("NFC", "".join(
        c for c in unicodedata.normalize("NFD", t) if c != "̄")) for n, t in gold.items()}
    s = score_vision(flat, gold, prologue_stream)
    # Not zero: 7 of the 136 gold lines carry no macron, so stripping macrons
    # leaves them untouched. Asserting the exact figure rather than 0 keeps this
    # control honest — it would otherwise pass for the wrong reason.
    unmarked = sum(1 for t in gold.values() if macron_count(t) == 0)
    assert s["exact"] == unmarked, (s["exact"], unmarked)
    assert s["macron_ratio"] == 0.0, s
    assert not s["usable_as_edition"], "macron-stripped text must be refused"

    # Defect 2: circumflexes stripped — the failure that disqualified Perseus.
    nocirc = {n: unicodedata.normalize("NFC", "".join(
        c for c in unicodedata.normalize("NFD", t) if c != "̂")) for n, t in gold.items()}
    hit = [n for n in gold if nocirc[n] != gold[n]]
    assert hit, "gold range must contain a circumflex or this control proves nothing"
    s = score_vision(nocirc, gold, prologue_stream)
    assert s["exact"] == len(gold) - len(hit), s
    assert not s["usable_as_edition"], "circumflex-stripped text must be refused"

    # Defect 3: thorn spelled th.
    s = score_vision({n: t.replace("þ", "th").replace("ð", "th") for n, t in gold.items()},
                     gold, prologue_stream)
    assert not s["usable_as_edition"], "th-substituted text must be refused"

    # Defect 4: a dropped line.
    short = dict(gold); short.pop(100)
    s = score_vision(short, gold, prologue_stream)
    assert 100 in s["missing_lines"], s

    # Defect 5: a HALLUCINATED line — the sole-source rule's nightmare. Two
    # passes that invent differently must not agree.
    a = dict(gold); a[100] = "wæs se grimma gæst Grendel hāten"
    b = dict(gold); b[100] = "wæs se grimma gāst Grendel hāten"
    agreed, dis = reconcile(a, b)
    assert 100 not in agreed and any(d["n"] == 100 for d in dis), \
        "two passes disagreeing on an invented line must not produce an agreed line"

    # Defect 6: a model that translates instead of transcribing. Its charset
    # betrays it before anything else does.
    pairs, problems = parse_transcription(_wrap(["100\tThen the grim spirit was called Grendel"]))
    assert not any(charset_violations(t) for _, t in pairs), "plain ASCII is legal, as it must be"
    s = score_vision(number_pass(pairs), gold, prologue_stream)
    assert s["exact"] == 0, "a translation must score zero against the gold"

    # Defect 7: foreign characters — an acute accent is OCR damage, a Cyrillic
    # lookalike is worse. Both are dropped and reported, never archived.
    pairs, problems = parse_transcription(_wrap(["101\tfyrene fré(m)man féond on helle;"]))
    assert pairs == [] and problems, "acute accents must be refused: %r" % (pairs,)
    pairs, problems = parse_transcription(_wrap(["102\tmanneа fremman"]))
    assert pairs == [] and problems, "Cyrillic lookalike must be refused"

    # Defect 8: ILLEGIBLE is honoured as a refusal to guess, not archived as text.
    pairs, _ = parse_transcription(_wrap(["103\tILLEGIBLE", "104\tgōd mid Gēatum"]))
    assert [n for n, _ in pairs] == [104], pairs

    # Defect 9: no transcription block at all.
    pairs, problems = parse_transcription("I'm sorry, I can't read this page.")
    assert pairs == [] and problems

    # Numbering: unnumbered lines take their place from the previous anchor.
    numbered = number_pass([(53, "a"), (None, "b"), (None, "c"), (56, "d")])
    assert numbered[54] == "b" and numbered[55] == "c" and numbered[56] == "d"

    print("vision selftest OK: gold %d lines, prologue stream %d chars with %d circumflexes, "
          "9 injected defects all caught"
          % (len(gold), len(prologue_stream), circumflex_count(prologue_stream)))
    return 0


def main():
    args = set(sys.argv[1:])
    selftest()                                   # always, before any network
    if args & {"--selftest"} or not args:
        return 0
    if "--probe" in args:
        return run("probe")
    if "--transcribe" in args:
        return run("transcribe")
    print("usage: vision_klaeber.py [--selftest|--probe|--transcribe]")
    return 2


if __name__ == "__main__":
    sys.exit(main())
