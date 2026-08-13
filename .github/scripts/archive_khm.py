#!/usr/bin/env python3
"""
archive_khm.py — fetch the authentic 1857 Kinder- und Hausmärchen text from
de.wikisource.org and commit it as sources/khm-NNN-source.json.

WHY THIS EXISTS
    The Cowork sandbox cannot reach de.wikisource.org, so source archiving used
    to require Zev's Chrome to be open — the last human dependency in the text
    pipeline. A GitHub Actions runner has ordinary internet access, so the fetch
    moves here and an unattended nightly session gets every source it needs with
    an unauthenticated `git fetch`, never opening a browser.

HOW A TALE IS IDENTIFIED  (rewritten after the second live run)
    THE PRINTED NUMERAL IS THE DATUM. Every numbered 1857 tale carries its number
    in the text itself: the centred "76." standing above the title, straight off
    the scanned page. That is evidence from the artifact, so it is what decides,
    and it is read from the page's leading block before the leading-heading guard
    removes it (the guard still removes it — the published corpus proves the
    numeral and the title are not part of the tale).

    SONSTIGES IS A RENUMBERING HISTORY, NOT THE 1857 NUMBER. The second live run
    failed exactly here: Die Sternthaler's box offers 83 AND 153 (83 in the early
    editions, 153 in 1857); Die Goldkinder offers 63 and 85 (85 in 1857);
    Strohhalm, Kohle und Bohne is 18 in 1857 but its box yields 19. Picking the
    larger, the last, or refusing on ambiguity are all wrong, so the box is now a
    CROSS-CHECK ONLY: its KHM numbers are parsed, and if the printed numeral is
    not among them a warning is logged naming both — but the printed numeral is
    used, and nothing is skipped over the disagreement. Never off index position
    either: the index's link order is not edition order.

    NO PRINTED NUMERAL -> SKIP, NEVER FALL BACK. Those pages are the ten
    Kinderlegenden and Der goldene Schlüssel: numbered separately in the book (the
    legends run 1.-10. of their own) and out of scope for this pass. Their own
    "1." must never be taken for KHM 1 — that is what produced the bogus
    "KHM 121 claimed twice" line — so a page with a printed numeral but NO KHM
    number anywhere in its Textdaten box is skipped as a probable legend too.
    211 discovered pages - 11 legends/specials = the 200 numbered tales.

    The number is re-read from the page itself again at write time, so nothing is
    ever archived on the strength of a cached number.

HOW CANDIDATE PAGES ARE DISCOVERED
    From the TWO 1857 volume pages, via the API's prop=links (not by scraping
    hrefs out of rendered HTML). There is no third 1857 volume: "Band 3" is the
    Anmerkungsband, it is dated 1856, and it holds Grimm's scholarly notes rather
    than tales — asking for it at an 1857 title is what produced the "page you
    specified doesn't exist" line in the first live run. Links are kept when they
    are ns 0, exist, end in " (1857)", and are not themselves a volume page.

WHAT IT GUARANTEES — three controls, all fatal, all before anything is written
    0. FIXTURE TEST (offline, no network): synthetic MediaWiki HTML exercising
       every extraction rule, plus two injected defects the comparator must
       catch. A gate that has only ever returned "pass" has not been shown to
       test anything.
    1. NUMBER->TITLE MAPPING is proved against the published corpus (and two
       pages claiming the same number is a fatal defect, reported with both
       titles, never resolved by keeping the first): every Grimm
       tale already in stories.json must agree with the mapping. 84 independent
       agreements, plus a >=190-of-200 coverage assertion, is what licenses
       trust in the mapping for the tales not yet done. A partial mapping fails
       loudly rather than archiving "whatever it managed to find".
    2. THE EXTRACTOR is proved against published controls: three already-shipped
       tales (verse-bearing ones preferred) are re-extracted from Wikisource and
       compared to their shipped story files token-for-token AND
       line-break-for-line-break. A token gate cannot see whitespace, and the
       July-21 extractor's real defect was 24 invented verse breaks, so
       lineation gets its own explicit assertion.

EXTRACTION RULES (v2, from the browser extractor that produced batches P1-P3)
    * drop .ws-noexport, .noprint, table, sup, h1-h3, .catlinks, .mw-editsection,
      style, script, .reflist, #toc
    * strip [NN] reference markers
    * collect <p> and .poem in document order as {"t":"p"|"v","x":...}; a .poem
      is taken whole and never descended into, so its inner <p> is not counted
      twice
    * <br> IS THE ONLY REAL LINE BREAK. Raw newlines inside <p> are HTML
      formatting whitespace falling mid-sentence at printed page transitions;
      treating them as breaks is exactly the bug the controls exist to catch.

POLITENESS
    One request per 0.9 s, globally, with backoff. MediaWiki's throttle reply is
    PLAIN TEXT ("You are making too many requests"), so it fails JSON parsing
    rather than arriving as a clean status code; batch P3 hit it on 11 of 211
    pages with six concurrent workers. Non-JSON is therefore treated as throttle
    and retried, never as a fatal error.

Usage:
    python .github/scripts/archive_khm.py --selftest
    python .github/scripts/archive_khm.py --which missing --limit 40
    python .github/scripts/archive_khm.py --which 81,82,83
    python .github/scripts/archive_khm.py --rebuild-index
"""

import argparse
import collections
import json
import os
import re
import sys
import time
import unicodedata

import requests
from bs4 import BeautifulSoup

API = "https://de.wikisource.org/w/api.php"
UA = "Lectorium-archiver/1.0 (https://github.com/zevfarber/Lectorium; text archiving for a reading app)"

# The 1857 edition is TWO volumes. There is no "Band 3 (1857)": the third book
# is the Anmerkungsband, dated 1856, and it carries Grimm's notes, not tales.
# Tale pages are discovered from these two index pages via prop=links and
# filtered on the " (1857)" suffix; the numbers come from the pages themselves.
INDEX_PAGES = [
    "Kinder- und Haus-Märchen Band 1 (1857)",
    "Kinder- und Haus-Märchen Band 2 (1857)",
]

# Volume pages link to each other, so they turn up in prop=links themselves.
VOLUME_PREFIX = unicodedata.normalize("NFC", "Kinder- und Haus-Märchen")
YEAR_SUFFIX = " (1857)"

MIN_INTERVAL = 0.9        # seconds between requests, globally
MAX_ATTEMPTS = 5
DEFAULT_LIMIT = 40
MAPPING_MIN = 190         # of 200 numbered tales
KHM_MAX = 210             # 200 tales + the ten Kinderlegenden
TALE_MAX = 200            # the printed numeral of a numbered tale is 1..200


def _repo_root():
    """Walk up from this file until stories.json is found. Robust to the script
    living in .github/scripts/, tools/, or anywhere else."""
    d = os.path.dirname(os.path.abspath(__file__))
    for _ in range(6):
        if os.path.exists(os.path.join(d, "stories.json")):
            return d
        d = os.path.dirname(d)
    raise RuntimeError("could not locate the repository root (no stories.json above %s)"
                       % os.path.abspath(__file__))


ROOT = _repo_root()
SRC_DIR = os.path.join(ROOT, "sources")
INDEX_CACHE = os.path.join(SRC_DIR, "khm-index.json")

# Matches the reader's word class closely enough for a source-fidelity check.
NL = "⏎"          # explicit line-break marker inside a signature (visible)
WORD_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿĀ-ɏ]+(?:[-\[\]()][A-Za-zÀ-ÖØ-öø-ÿĀ-ɏ]+)*")

# A sentinel standing in for <br> while the surrounding whitespace is
# normalised. It is written as an EXPLICIT ESCAPE for a PRINTABLE symbol
# (U+241F SYMBOL FOR UNIT SEPARATOR — the picture of a control character, not
# one). Batch P2 used a raw control character; it did not survive transport and
# the block was split character-by-character. Never use a Cc codepoint here.
BR = "␟"
assert not any(unicodedata.category(c) == "Cc" for c in BR), \
    "the <br> sentinel must not contain a raw control character (see batch P2)"

DROP_SELECTOR = (
    ".ws-noexport, .noprint, table, sup, h1, h2, h3, .catlinks, "
    "style, script, .mw-editsection, .reflist, #toc, .toc"
)

# Titles are compared on a folded key so that typographic noise (case,
# punctuation, umlaut spelling) cannot fail the mapping control, while a
# genuinely different tale still does. Add an alias here ONLY after confirming
# by eye that the Wikisource page is the same tale under a variant spelling.
TITLE_ALIASES = {}

SESSION = requests.Session()
SESSION.headers["User-Agent"] = UA


# --------------------------------------------------------------------------
# fetching — one request per 0.9 s, globally, with throttle-aware backoff
# --------------------------------------------------------------------------

_last_request = [0.0]


def _throttle():
    wait = MIN_INTERVAL - (time.time() - _last_request[0])
    if wait > 0:
        time.sleep(wait)
    _last_request[0] = time.time()


def api_parse(page, props="text|wikitext|revid"):
    """Return {'html','wikitext','revid','title'} for a page, or raise."""
    p = api_parse_raw(page, props)
    return {
        "html": p.get("text") or "",
        "wikitext": p.get("wikitext") or "",
        "revid": p.get("revid"),
        "title": p.get("title") or page,
    }


def api_parse_raw(page, props):
    """The API's raw `parse` object. Everything goes through here, so prop=links
    gets the same throttling and the same throttle-aware backoff as prop=text."""
    last = None
    for attempt in range(MAX_ATTEMPTS):
        _throttle()
        try:
            r = SESSION.get(
                API,
                params={
                    "action": "parse",
                    "page": page,
                    "prop": props,
                    "formatversion": "2",
                    "format": "json",
                    "redirects": "1",
                },
                timeout=60,
            )
        except requests.RequestException as exc:      # transient network
            last = str(exc)
            time.sleep(2 ** attempt)
            continue

        if r.status_code in (429, 500, 502, 503, 504):
            last = "HTTP %s" % r.status_code
            retry_after = r.headers.get("Retry-After")
            try:
                pause = float(retry_after)
            except (TypeError, ValueError):
                pause = 5 * (attempt + 1)
            time.sleep(pause)
            continue
        if r.status_code != 200:
            raise RuntimeError("could not fetch %r (HTTP %s)" % (page, r.status_code))

        # The throttle reply is PLAIN TEXT ("You are making too many requests"),
        # so it arrives as a JSON parse failure, not a status code. Treat any
        # non-JSON body as throttling and back off; never as a fatal error.
        try:
            d = r.json()
        except ValueError:
            last = "non-JSON body: %s" % r.text[:120].replace("\n", " ")
            time.sleep(5 * (attempt + 1))
            continue

        if "error" in d:                              # genuine API error: no retry
            raise RuntimeError("wikisource error for %r: %s"
                               % (page, d["error"].get("info") or d["error"].get("code")))
        return d["parse"]
    raise RuntimeError("could not fetch %r after %d attempts (last: %s)"
                       % (page, MAX_ATTEMPTS, last))


# --------------------------------------------------------------------------
# extraction
# --------------------------------------------------------------------------

def _clean_ws(s):
    """Collapse every run of whitespace — including raw newlines — to one space."""
    s = s.replace(" ", " ").replace("​", "")
    s = re.sub(r"\[\d+\]", "", s)                     # [NN] reference markers
    return re.sub(r"\s+", " ", s).strip()


def _block_text(el):
    """Text of one block. <br> is the only line break; nothing else is."""
    frag = BeautifulSoup(str(el), "lxml")
    for br in frag.find_all("br"):
        br.replace_with(BR)
    raw = frag.get_text()
    lines = [_clean_ws(x) for x in raw.split(BR)]
    return "\n".join(x for x in lines if x)


def _is_poem(el):
    return "poem" in (el.get("class") or [])


# The centred numeral above the title: "76." — the 1857 number as the book
# itself prints it. \s* on both sides because the block text is taken as it
# comes; the guard's own input is already stripped.
PRINTED_NUMERAL_RE = re.compile(r"^\s*(\d{1,3})\.\s*$")


def drop_leading_headings(blocks, page="?"):
    """Remove the centred "76." / "Die Nelke." heading from the archived text.

    The second live run showed these arriving AS <p> blocks ("leading-heading
    guard dropped a block (bare numeral): '76.'"), so this fires routinely now
    rather than never. It still drops AT MOST the first two blocks, and only when
    a block is exactly a bare numeral or exactly the tale's own title; the
    published corpus proves neither belongs to the tale (nelke.json's sentence 0
    is the first line of the story). It still says what it dropped, because a
    page whose markup changed shape is news.

    THE NUMERAL IS EVIDENCE, NOT NOISE: read it with printed_number() BEFORE
    calling this. Dropping it from the archived text and using it as the tale's
    1857 number are not in conflict — the book prints it outside the tale.
    """
    bare = re.sub(r"\s*\(1857\)\s*$", "", page or "").strip()
    title_key = fold_title(bare) if bare and bare != "?" else ""

    out = list(blocks)
    for _ in range(2):
        if not out:
            break
        x = out[0]["x"].strip()
        if "\n" in x or not x:
            break
        why = None
        if PRINTED_NUMERAL_RE.match(x):
            why = "bare numeral"
        elif title_key and fold_title(x) == title_key:
            why = "tale title"
        if why is None:
            break
        print("  %s: leading-heading guard dropped a block (%s): %r"
              % (page, why, x), file=sys.stderr)
        out.pop(0)
    return out


def _pruned_root(html):
    """The parse fragment with the non-text furniture decomposed.

    Note this removes the Textdaten <table> along with everything else in
    DROP_SELECTOR, which is why the printed numeral read from here can never be
    contaminated by the box's numbers, and why the box must be read from its own
    fresh soup (see box_numbers)."""
    soup = BeautifulSoup(html or "", "lxml")
    root = soup.select_one(".mw-parser-output") or soup
    for el in root.select(DROP_SELECTOR):
        el.decompose()
    return root


def _collect_blocks(root):
    """Ordered [{'t':'p'|'v','x':...}], before the leading-heading guard."""
    blocks = []

    def walk(node):
        for child in node.find_all(recursive=False):
            if _is_poem(child):
                txt = _block_text(child)
                if txt:
                    blocks.append({"t": "v", "x": txt})
                continue                  # never descend: the inner <p> is the poem
            if child.name == "p":
                txt = _block_text(child)
                if txt:
                    blocks.append({"t": "p", "x": txt})
                continue
            walk(child)

    walk(root)
    return blocks


# How far down the page a printed numeral may sit. Deliberately the same window
# the leading-heading guard drops from: a numeral is only ever accepted where the
# guard would also remove it, so the number used and the text archived can never
# disagree about what belongs to the tale.
LEADING_SCAN = 2


def leading_texts(root, limit=LEADING_SCAN):
    """The first few single-line text units in document order.

    Wider than _collect_blocks on purpose: the centred numeral is a <p> on the
    pages the live run met, but on other pages it sits in a bare
    <div style="text-align:center">, which the block extractor (rightly) ignores.
    A generic container with no block children counts as one unit here, so the
    numeral is found in either shape. Only the first few units are ever returned,
    so nothing deep in the tale can be mistaken for a heading.
    """
    out = []

    def walk(node):
        for child in node.find_all(recursive=False):
            if len(out) >= limit:
                return
            if _is_poem(child) or child.name == "p":
                txt = _block_text(child)
                if txt:
                    out.append(txt)
                continue
            if child.find(["p", "div", "table", "ul", "ol", "dl"]) is None:
                txt = _block_text(child)          # a leaf container: the centred div
                if txt:
                    out.append(txt)
                continue
            walk(child)

    walk(root)
    return out[:limit]


def printed_number(html, page="?"):
    """The 1857 number as the book prints it: the bare "76." above the title.

    THE authoritative number (see the module docstring). Returns None when the
    page has no such numeral — the Kinderlegenden and Der goldene Schlüssel —
    and the caller then skips the page. It never falls back to anything.
    """
    for txt in leading_texts(_pruned_root(html)):
        m = PRINTED_NUMERAL_RE.match(txt)
        if m:
            n = int(m.group(1))
            return n if 1 <= n <= TALE_MAX else None
    return None


def extract_blocks(html, page="?"):
    """Ordered [{'t':'p'|'v','x':...}] from a Wikisource parse fragment."""
    blocks = _collect_blocks(_pruned_root(html))
    blocks = drop_leading_headings(blocks, page)

    # Refuse an implausible result rather than returning it. The failure this
    # guards against is raw newlines being taken for line breaks, which sprays
    # breaks through prose. Slack is generous so that a genuinely verse-heavy
    # tale is not refused; the exact proof is the control gate, this is the net
    # for the 197 tales no control covers.
    if not blocks:
        raise RuntimeError("%s: extractor returned no blocks" % page)
    nl = sum(b["x"].count("\n") for b in blocks)
    if nl > 4 * len(blocks) + 10:
        raise RuntimeError("%s: implausible line-break count (%d breaks / %d blocks) — "
                           "the <br>-only rule is probably not holding" % (page, nl, len(blocks)))
    return blocks


# --------------------------------------------------------------------------
# the tale's 1857 number: printed numeral decides, Textdaten box cross-checks
# --------------------------------------------------------------------------

KHM_RE = re.compile(r"KHM\s*[:.\s]?\s*(\d{1,3})")
BOX_SELECTORS = ("table.ws-header", "#ws-data", "table.textdaten", ".ws-header", ".textdaten")

# The Textdaten template's own field, in raw wikitext: "|SONSTIGES=seit 1812:
# KHM 76". Unambiguous by construction — one named field of one template — and
# used only to reconstruct the box's cross-check set when the rendered box
# yielded nothing. It never supplies the tale's number.
SONSTIGES_FIELD_RE = re.compile(r"^\|\s*SONSTIGES\s*=(.*)$", re.M)


class DuplicateNumber(RuntimeError):
    """Two pages claimed the same 1857 number. A real defect — reported with both
    titles and fatal, never resolved by keeping the first."""

    def __init__(self, conflicts):
        self.conflicts = list(conflicts)
        RuntimeError.__init__(self, " | ".join(self.conflicts))


# number: the 1857 number, or None when the page is skipped.
# kind:   "numbered" | "legend".
# message: a warning (kind "numbered") or the reason for skipping ("legend").
NumberResult = collections.namedtuple("NumberResult", "number kind message")


def textdaten_box(soup):
    """The page's own header/Textdaten box, or None."""
    for sel in BOX_SELECTORS:
        el = soup.select_one(sel)
        if el is not None:
            return el
    for t in soup.find_all("table"):
        txt = t.get_text(" ", strip=True)
        if "Textdaten" in txt or KHM_RE.search(txt):
            return t
    return None


def box_numbers(html, wikitext=""):
    """Every KHM number the page's OWN Textdaten box offers — the renumbering
    history, as a set. CROSS-CHECK MATERIAL ONLY; it never decides a number.

    Only the BOX's text is searched, never the whole page: the "Andere Version"
    footer links to "Kinder- und Haus-Märchen Band 3 (1856)/Anmerkungen#76" and
    is exactly the sort of stray number that must not join the set. When the
    rendered box yields nothing, the header template's SONSTIGES field in the raw
    wikitext stands in for it — the same datum, same template, so a real tale is
    not mistaken for a legend just because the box did not render.

    Parses its own fresh soup: extract_blocks decomposes tables, and the box is
    one. Do not pass a shared, already-pruned soup in here.
    """
    nums = set()
    box = textdaten_box(BeautifulSoup(html or "", "lxml"))
    if box is not None:
        nums = _plausible(KHM_RE.findall(box.get_text(" ", strip=True)))
    if not nums:
        for value in SONSTIGES_FIELD_RE.findall(wikitext or ""):
            nums |= _plausible(KHM_RE.findall(value))
    return nums


def tale_number(html, wikitext="", page="?"):
    """The tale's 1857 number, as a NumberResult. The one place this is decided.

    THE PRINTED NUMERAL DECIDES. The box only cross-checks: a printed numeral
    absent from the box gets a warning naming both and is used anyway, because
    the box is a renumbering history (Sternthaler: 83 early, 153 in 1857;
    Strohhalm: box says 19, the 1857 book prints 18). Disagreement is EXPECTED
    for renumbered tales and never causes a skip.

    No printed numeral, or a printed numeral on a page whose box holds no KHM
    number at all, means one of the Kinderlegenden or Der goldene Schlüssel:
    kind "legend", number None, skipped with a reason. The second condition is
    what stops a legend's own "1." from being archived as KHM 1.
    """
    printed = printed_number(html, page)
    box = box_numbers(html, wikitext)

    if printed is None:
        return NumberResult(None, "legend",
                            "%s: no printed numeral above the title — one of the ten "
                            "Kinderlegenden or Der goldene Schlüssel, numbered separately in "
                            "the 1857 book and out of scope for this pass" % page)
    if not box:
        return NumberResult(None, "legend",
                            "%s: prints %r but its Textdaten box holds no KHM number at all — "
                            "probable Kinderlegende numbering itself 1.-10.; refusing to read "
                            "it as KHM %d" % (page, "%d." % printed, printed))
    if printed not in box:
        return NumberResult(printed, "numbered",
                            "%s: the page prints %r but its Textdaten box offers KHM %s — using "
                            "the printed numeral (SONSTIGES is a renumbering history, not the "
                            "1857 number)"
                            % (page, "%d." % printed, ", ".join(str(n) for n in sorted(box))))
    return NumberResult(printed, "numbered", None)


def _plausible(found):
    """The distinct in-range numbers among regex hits."""
    return {int(x) for x in found if 1 <= int(x) <= KHM_MAX}


def assemble_mapping(claims):
    """{number: entry} from (number, entry) claims, or DuplicateNumber.

    Two pages claiming one number is a defect in the number-reading, not a tie to
    break: the run stops and names both pages. (Keeping the first is what let the
    bogus "KHM 19 claimed twice" pass through the second live run.)
    """
    mapping, conflicts = {}, []
    for number, entry in claims:
        prev = mapping.get(number)
        if prev is not None and prev["page"] != entry["page"]:
            conflicts.append("KHM %d claimed by two pages: %r and %r"
                             % (number, prev["page"], entry["page"]))
            continue
        mapping[number] = entry
    if conflicts:
        raise DuplicateNumber(conflicts)
    return mapping


# --------------------------------------------------------------------------
# the comparator (this is the thing that has to be right)
# --------------------------------------------------------------------------

def signature(blocks_or_text):
    """
    A comparable signature of a text: the token sequence with explicit newline
    markers interleaved. One comparison therefore catches a dropped or added
    word AND a moved or invented line break, which a token-only gate cannot see.
    """
    if isinstance(blocks_or_text, list):
        parts = [b["x"] if isinstance(b, dict) else b for b in blocks_or_text]
        # Joined with a SPACE, never a newline: block boundaries and sense-unit
        # boundaries do not line up (a paragraph holds several sense-units), so
        # joining with newlines would manufacture break mismatches against a
        # published story file's "t" fields. The only newlines that may reach a
        # signature are the real verse line breaks stored inside a block.
        text = " ".join(parts)
    else:
        text = blocks_or_text
    text = unicodedata.normalize("NFC", text)

    sig = []
    for line in text.split("\n"):
        sig.extend(WORD_RE.findall(line))
        sig.append(NL)
    while sig and sig[-1] == NL:
        sig.pop()
    return sig


def first_diff(a, b):
    """A readable context window around the first disagreement, or None."""
    n = min(len(a), len(b))
    for i in range(n):
        if a[i] != b[i]:
            lo = max(0, i - 6)
            return "index %d: expected %r, got %r\n  ...%s\n  ...%s" % (
                i, a[i], b[i], " ".join(a[lo:i + 6]), " ".join(b[lo:i + 6]))
    if len(a) != len(b):
        tail = (a if len(a) > len(b) else b)[n:n + 12]
        return "lengths differ (%d vs %d); extra: %s" % (len(a), len(b), " ".join(tail))
    return None


def story_signature(story):
    """Signature of a published story file, rebuilt from its sense-units."""
    return signature([x["t"] for x in story["sentences"]])


# --------------------------------------------------------------------------
# the published corpus
# --------------------------------------------------------------------------

def load_manifest():
    with open(os.path.join(ROOT, "stories.json"), encoding="utf-8") as f:
        data = json.load(f)
    return data["stories"] if isinstance(data, dict) else data


def published_khm():
    """{khm: (title, story_filename)} for every Grimm tale already live."""
    out = {}
    for e in load_manifest():
        if e.get("khm") and "Hausmärchen" in (e.get("work") or ""):
            out[int(e["khm"])] = (e["title"], e["file"])
    return out


def fold_title(t):
    """Comparison key: case, punctuation and umlaut spelling folded away."""
    t = unicodedata.normalize("NFC", t or "")
    t = re.sub(r"\s*\(1857\)\s*$", "", t).strip().lower()
    t = (t.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
          .replace("ß", "ss"))
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", t)


def slugify(title):
    t = re.sub(r"\s*\(1857\)\s*$", "", title).strip().lower()
    t = (t.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
          .replace("ß", "ss"))
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


# --------------------------------------------------------------------------
# CONTROL 0 — offline fixture test of every extraction rule
# --------------------------------------------------------------------------

FIXTURE_HTML = """
<div class="mw-parser-output">
<table class="ws-header"><tr><th>Textdaten</th></tr>
<tr><td>Titel:</td><td>Rapunzel</td></tr>
<tr><td>Aus:</td><td>Kinder- und Hausmärchen, Band 1</td></tr>
<tr><td>Sonstiges:</td><td>seit 1812: KHM 12</td></tr></table>
<div class="ws-noexport">Diese Seite ist zweimal korrekturgelesen. KHM 199</div>
<h2>Rapunzel<span class="mw-editsection">[bearbeiten]</span></h2>
<p>12.</p>
<p>Es war einmal ein Mann
und eine Frau<sup class="reference">FUSSNOTE-XYZ</sup>, die wünschten sich[7] ein Kind.</p>
<div class="poem"><p>Rapunzel, Rapunzel,<br/>
laß mir dein Haar herunter.</p></div>
<p>Da rief die Zauberin:<br>komm herab!</p>
<table class="prettytable"><tr><td>Fußnote KHM 200</td></tr></table>
<div class="catlinks">Kategorien: Märchen</div>
</div>
"""

# The real shape of a tale page, modelled on Die Nelke (1857) as the second live
# run met it: the numeral "76." and the title arrive as <p> blocks (the run's own
# log says so), the box's SONSTIGES row agrees, and the footer carries an "Andere
# Version" link to the 1856 Anmerkungsband — the decoy the box-only rule ignores.
FIXTURE_TEXTDATEN_HTML = """
<div class="mw-parser-output">
<table class="ws-header"><tr><th colspan="2">Textdaten</th></tr>
<tr><td>Autor:</td><td>Brüder Grimm</td></tr>
<tr><td>Titel:</td><td>Die Nelke</td></tr>
<tr><td>Sonstiges:</td><td>seit 1812: KHM 76</td></tr></table>
<p>76.</p>
<p><b>Die Nelke.</b></p>
<p>Es war eine Königin, die hatte unser Herr Gott verschlossen.</p>
<p>Da sprach der Koch: es soll geschehen.</p>
<div class="ws-noexport">Andere Version:
<a href="/wiki/Kinder-_und_Haus-M%C3%A4rchen_Band_3_(1856)/Anmerkungen#76">Anmerkungen</a>
— dort als KHM 199 geführt</div>
</div>
"""

# The same page in the other shape seen in the wild: the centred numeral in a
# bare <div>, which the block extractor ignores. The numeral must still be read.
FIXTURE_CENTERED_DIV_HTML = """
<div class="mw-parser-output">
<table class="ws-header"><tr><th colspan="2">Textdaten</th></tr>
<tr><td>Titel:</td><td>Die Nelke</td></tr>
<tr><td>Sonstiges:</td><td>seit 1812: KHM 76</td></tr></table>
<div style="text-align:center">76.</div>
<div style="text-align:center"><b>Die Nelke.</b></div>
<p>Es war eine Königin, die hatte unser Herr Gott verschlossen.</p>
<p>Da sprach der Koch: es soll geschehen.</p>
</div>
"""

# A RENUMBERED tale — Die Sternthaler, KHM 83 in the early editions and 153 in
# 1857. Its box offers both. This is the case that failed the second live run.
FIXTURE_RENUMBERED_HTML = """
<div class="mw-parser-output">
<table class="ws-header"><tr><th>Textdaten</th></tr>
<tr><td>Titel:</td><td>Die Sternthaler</td></tr>
<tr><td>Sonstiges:</td><td>seit 1812: KHM 83; seit 1857: KHM 153</td></tr></table>
<p>153.</p>
<p><b>Die Sternthaler.</b></p>
<p>Es war einmal ein kleines Mädchen, dem war Vater und Mutter gestorben.</p>
<p>Da fielen die Sterne vom Himmel.</p>
</div>
"""

# A DISAGREEING tale — Strohhalm, Kohle und Bohne prints 18. in 1857 while its
# box yields only KHM 19. The printed numeral wins; a warning is logged.
FIXTURE_DISAGREE_HTML = """
<div class="mw-parser-output">
<table class="ws-header"><tr><th>Textdaten</th></tr>
<tr><td>Titel:</td><td>Strohhalm, Kohle und Bohne</td></tr>
<tr><td>Sonstiges:</td><td>seit 1812: KHM 19</td></tr></table>
<p>18.</p>
<p><b>Strohhalm, Kohle und Bohne.</b></p>
<p>In einem Dorfe wohnte eine arme alte Frau.</p>
<p>Da lachte der Strohhalm.</p>
</div>
"""

# A KINDERLEGENDE — Die zwölf Apostel: no printed numeral, and no KHM number
# anywhere in its box. Skipped, never numbered, never guessed from wikitext.
FIXTURE_LEGEND_HTML = """
<div class="mw-parser-output">
<table class="ws-header"><tr><th>Textdaten</th></tr>
<tr><td>Titel:</td><td>Die zwölf Apostel</td></tr>
<tr><td>Sonstiges:</td><td>Kinderlegende</td></tr></table>
<p>Es war dreihundert Jahre vor der Geburt des Herrn Christus.</p>
<p>Da gieng sie hin.</p>
</div>
"""

# A legend that DOES print a numeral — its own "1.", because the Kinderlegenden
# are numbered 1.-10. separately. Its box holds no KHM number, so it is skipped:
# reading this as KHM 1 is precisely the bogus "claimed twice" defect.
FIXTURE_LEGEND_NUMBERED_HTML = """
<div class="mw-parser-output">
<table class="ws-header"><tr><th>Textdaten</th></tr>
<tr><td>Titel:</td><td>Der heilige Joseph im Walde</td></tr>
<tr><td>Sonstiges:</td><td>Kinderlegende Nr. 1</td></tr></table>
<p>1.</p>
<p><b>Der heilige Joseph im Walde.</b></p>
<p>Es war eine Mutter, die hatte drei Töchter.</p>
<p>Da gieng die älteste hinaus in den Wald.</p>
</div>
"""

# A box with no number at all, on a page that DOES print its numeral: the
# wikitext SONSTIGES field stands in as the cross-check set.
FIXTURE_NO_BOX_NUMBER_HTML = """
<div class="mw-parser-output">
<table class="ws-header"><tr><th>Textdaten</th></tr>
<tr><td>Titel:</td><td>Die Nelke</td></tr></table>
<p>76.</p>
<p>Es war eine Königin.</p>
</div>
"""

FIXTURE_WIKITEXT = """{{Textdaten
|AUTOR=Brüder Grimm
|TITEL=Die Nelke
|SONSTIGES=seit 1812: KHM 76
}}
"""

# What action=parse&prop=links returns for a volume page: ns 0 tale titles
# alongside the sibling volume, a non-1857 edition, a redlink, and other
# namespaces. Every non-tale here has been seen in the live link list.
FIXTURE_LINKS = [
    {"ns": 0, "title": "Der Froschkönig oder der eiserne Heinrich (1857)", "exists": True},
    {"ns": 0, "title": "Rapunzel (1857)", "exists": True},
    {"ns": 0, "title": "Die Nelke (1857)", "exists": True},
    {"ns": 0, "title": "Von dem Fischer un syner Fru (1857)", "exists": True},
    {"ns": 0, "title": "Von dem Tode des Hühnchens (1857)", "exists": True},
    {"ns": 0, "title": "Das kluge Grethel (1857)", "exists": True},
    {"ns": 0, "title": "Mährchen von einem, der auszog das Fürchten zu lernen (1857)",
     "exists": True},
    # the sibling volume: ns 0, exists, ends in " (1857)" — excluded by prefix
    {"ns": 0, "title": "Kinder- und Haus-Märchen Band 2 (1857)", "exists": True},
    # the Anmerkungsband is 1856, and is not a tale page
    {"ns": 0, "title": "Kinder- und Haus-Märchen Band 3 (1856)", "exists": True},
    # a different edition of a real tale — excluded by the year suffix
    {"ns": 0, "title": "Rapunzel (1812)", "exists": True},
    # a redlink and other namespaces
    {"ns": 0, "title": "Der Wolf und der Fuchs (1857)", "exists": False},
    {"ns": 14, "title": "Kategorie:Märchen (1857)", "exists": True},
    {"ns": 104, "title": "Seite:Grimms Märchen (1857) 076.jpg (1857)", "exists": True},
]

# The centred heading as the extractor actually meets it (generic containers,
# not <p>), and the shape the guard exists for if that ever changes.
FIXTURE_HEADING_AS_P_HTML = """
<div class="mw-parser-output">
<p>76.</p>
<p>Die Nelke.</p>
<p>77.</p>
<p>Es war eine Königin, die hatte unser Herr Gott verschlossen.</p>
</div>
"""


def fixture_test(verbose=True):
    """Offline proof that the extraction rules and the comparator behave.
    Runs on every invocation: it costs nothing and needs no network."""
    def check(name, cond, detail=""):
        if not cond:
            raise AssertionError("fixture: %s FAILED %s" % (name, detail))
        if verbose:
            print("  fixture ok: %s" % name)

    blocks = extract_blocks(FIXTURE_HTML, page="<fixture>")
    kinds = [b["t"] for b in blocks]
    texts = [b["x"] for b in blocks]

    check("three blocks, p/v/p in document order", kinds == ["p", "v", "p"], kinds)
    check("raw newline inside <p> is NOT a line break", "\n" not in texts[0], repr(texts[0]))
    check("<br> IS a line break (verse)", texts[1].count("\n") == 1, repr(texts[1]))
    check("<br> IS a line break (prose)", texts[2].count("\n") == 1, repr(texts[2]))
    check(".poem is one v block, its <p> not double-counted",
          kinds.count("v") == 1 and texts[1].startswith("Rapunzel, Rapunzel,"), texts[1])
    check(".ws-noexport dropped", not any("korrekturgelesen" in t for t in texts))
    check("table dropped", not any("Fußnote" in t for t in texts))
    check(".catlinks dropped", not any("Kategorien" in t for t in texts))
    check(".mw-editsection dropped", not any("bearbeiten" in t for t in texts))
    check("sup content dropped", "FUSSNOTE-XYZ" not in texts[0], repr(texts[0]))
    check("[NN] markers stripped", "[7]" not in texts[0], repr(texts[0]))
    check("h2 not collected", not any(t.strip() == "Rapunzel" for t in texts))

    r = tale_number(FIXTURE_HTML, page="<fixture>")
    check("printed '12.' is the number; the box agrees; 199/200 ignored",
          r.number == 12 and r.message is None, r)
    check("the printed numeral is still removed from the archived text",
          not any(PRINTED_NUMERAL_RE.match(t) for t in texts), texts)

    # ---- CASE 1: agreement — printed '76.', box says only KHM 76 ------------
    r = tale_number(FIXTURE_TEXTDATEN_HTML, page="Die Nelke (1857)")
    check("printed '76.' with a box saying only KHM 76 reads as 76, no warning",
          r == NumberResult(76, "numbered", None), r)
    check("the 1856 Anmerkungen footer (#76 / 'KHM 199') is not read as the number",
          r.number == 76 and "KHM 199" in FIXTURE_TEXTDATEN_HTML, r)
    check("the numeral is also found when it sits in a centred <div>, not a <p>",
          tale_number(FIXTURE_CENTERED_DIV_HTML, page="Die Nelke (1857)").number == 76)

    # The box is a <table> and the extractor decomposes tables. Reading the
    # number must not depend on extraction order — prove both orders agree.
    _ = extract_blocks(FIXTURE_TEXTDATEN_HTML, page="Die Nelke (1857)")
    check("number still readable after the extractor has run (no shared soup)",
          tale_number(FIXTURE_TEXTDATEN_HTML, page="Die Nelke (1857)").number == 76)

    # ---- CASE 2: a RENUMBERED tale — printed 153., box offers 83 and 153 ----
    r = tale_number(FIXTURE_RENUMBERED_HTML, page="Die Sternthaler (1857)")
    check("renumbered tale takes the printed 153, not the box's earlier 83",
          r.number == 153, r)
    check("a box offering two numbers is no longer a skip (renumbering is normal)",
          r.kind == "numbered" and r.message is None, r)
    check("the corpus agrees: Die Sternthaler is published as KHM 153",
          published_khm().get(153, ("", ""))[0] == "Die Sternthaler", published_khm().get(153))

    # ---- CASE 3: DISAGREEMENT — printed 18., box offers only 19 -------------
    r = tale_number(FIXTURE_DISAGREE_HTML, page="Strohhalm, Kohle und Bohne (1857)")
    check("the printed 18. beats the box's 19 — never skipped, never overridden",
          r.number == 18 and r.kind == "numbered", r)
    check("the disagreement is warned about, naming page, numeral and box numbers",
          r.message and "18" in r.message and "19" in r.message
          and "Strohhalm" in r.message, r.message)
    check("the corpus agrees: KHM 18 is Strohhalm and KHM 19 is the Fischer",
          published_khm().get(18, ("", ""))[0] == "Strohhalm, Kohle und Bohne"
          and published_khm().get(19, ("", ""))[0] == "Von dem Fischer un syner Fru")

    # ---- CASE 4: a KINDERLEGENDE — no numeral, no KHM in the box -----------
    r = tale_number(FIXTURE_LEGEND_HTML, page="Die zwölf Apostel (1857)")
    check("a page with no printed numeral is skipped as a legend, not numbered",
          r.number is None and r.kind == "legend", r)
    check("the skip message says it is a legend and names the page",
          r.message and "Kinderlegende" in r.message and "Apostel" in r.message, r.message)
    check("wikitext |SONSTIGES= never rescues a page with no printed numeral",
          tale_number(FIXTURE_LEGEND_HTML, FIXTURE_WIKITEXT,
                      "Die zwölf Apostel (1857)").number is None)

    # ---- CASE 5: a legend that prints its OWN '1.' -------------------------
    r = tale_number(FIXTURE_LEGEND_NUMBERED_HTML, page="Der heilige Joseph im Walde (1857)")
    check("a leading '1.' with no KHM anywhere in the box is NEVER returned as KHM 1",
          r.number is None and r.kind == "legend", r)
    check("that skip says why (probable legend numbering itself 1.-10.)",
          r.message and "Kinderlegende" in r.message, r.message)

    check("the box's cross-check set falls back to wikitext |SONSTIGES=",
          box_numbers(FIXTURE_NO_BOX_NUMBER_HTML, FIXTURE_WIKITEXT) == {76})
    check("a printed numeral with a wikitext-only box still reads as 76",
          tale_number(FIXTURE_NO_BOX_NUMBER_HTML, FIXTURE_WIKITEXT).number == 76)

    # ---- CASE 6: two pages claiming one number is FATAL --------------------
    claims = [(19, {"page": "Strohhalm, Kohle und Bohne (1857)", "title": "a", "revid": 1}),
              (19, {"page": "Von dem Fischer un syner Fru (1857)", "title": "b", "revid": 2})]
    try:
        assemble_mapping(claims)
        dup = None
    except DuplicateNumber as exc:
        dup = str(exc)
    check("two pages claiming the same number fail hard, never 'keeping the first'",
          dup is not None, dup)
    check("the duplicate report names BOTH pages",
          dup and "Strohhalm" in dup and "Fischer" in dup, dup)
    check("distinct numbers assemble normally",
          sorted(assemble_mapping([(18, claims[0][1]), (19, claims[1][1])])) == [18, 19])

    # ---- discovery from prop=links -----------------------------------------
    titles = tale_links(FIXTURE_LINKS)
    check("sibling volume page excluded from candidates",
          "Kinder- und Haus-Märchen Band 2 (1857)" not in titles)
    check("the 1856 Anmerkungsband excluded", not any("1856" in t for t in titles))
    check("non-1857 edition excluded", "Rapunzel (1812)" not in titles)
    check("redlink (exists=false) excluded",
          "Der Wolf und der Fuchs (1857)" not in titles)
    check("non-zero namespaces excluded", not any(":" in t for t in titles), titles)
    anchors = ["Der Froschkönig oder der eiserne Heinrich (1857)", "Rapunzel (1857)",
               "Die Nelke (1857)", "Von dem Fischer un syner Fru (1857)",
               "Von dem Tode des Hühnchens (1857)", "Das kluge Grethel (1857)",
               "Mährchen von einem, der auszog das Fürchten zu lernen (1857)"]
    check("all seven live-verified tale titles kept",
          [t for t in titles] == anchors, titles)

    # ---- the leading-heading guard -----------------------------------------
    real = extract_blocks(FIXTURE_TEXTDATEN_HTML, page="Die Nelke (1857)")
    check("guard removes the printed numeral AND the title from the archived text",
          len(real) == 2 and real[0]["x"].startswith("Es war eine Königin"), real)
    centred = extract_blocks(FIXTURE_CENTERED_DIV_HTML, page="Die Nelke (1857)")
    check("centred-<div> heading was never collected in the first place",
          len(centred) == 2 and centred[0]["x"].startswith("Es war eine Königin"), centred)
    check("archived text is identical in both page shapes",
          first_diff(signature(real), signature(centred)) is None)
    for name, html in (("Die Sternthaler", FIXTURE_RENUMBERED_HTML),
                       ("Strohhalm, Kohle und Bohne", FIXTURE_DISAGREE_HTML)):
        got = extract_blocks(html, page="%s (1857)" % name)
        check("%s: numeral and title dropped, tale kept whole" % name,
              len(got) == 2 and not any(PRINTED_NUMERAL_RE.match(b["x"]) for b in got), got)
    guarded = extract_blocks(FIXTURE_HEADING_AS_P_HTML, page="Die Nelke (1857)")
    check("guard drops a bare numeral and the bare title when they ARE <p>s",
          [b["x"] for b in guarded] == ["77.", "Es war eine Königin, die hatte unser "
                                        "Herr Gott verschlossen."], guarded)
    check("guard drops at most two blocks (the third '77.' survives)",
          guarded[0]["x"] == "77.", guarded)

    # The comparator must not be blind. Inject one dropped word and one moved
    # line break and require both to be caught.
    base = signature([{"t": "v", "x": "Es war einmal\nein König"}])
    dropped = signature([{"t": "v", "x": "Es einmal\nein König"}])
    moved = signature([{"t": "v", "x": "Es war einmal ein\nKönig"}])
    check("comparator catches a dropped word", first_diff(base, dropped) is not None)
    check("comparator catches a moved line break", first_diff(base, moved) is not None)
    check("comparator passes an identical text", first_diff(base, signature(
        [{"t": "v", "x": "Es war einmal\nein König"}])) is None)
    # Blocks join with a SPACE, so re-blocking prose must not change the signature.
    check("block boundaries do not affect the signature",
          signature([{"t": "p", "x": "a b"}, {"t": "p", "x": "c d"}]) == signature("a b c d"))
    return True


# --------------------------------------------------------------------------
# CONTROL 1 — the KHM number -> page title mapping
# --------------------------------------------------------------------------

def tale_links(links):
    """The tale pages among one volume's prop=links list.

    A link is a candidate when it is ns 0 (so Seite:, Datei:, Kategorie: drop
    out), when the page actually exists, when it ends in " (1857)" (so the 1856
    Anmerkungsband and other editions drop out), and when it is not itself a
    volume page — Band 1 links to Band 2, and that sibling ends in " (1857)"
    too, so the suffix test alone would let it through.
    """
    out = []
    for link in links or []:
        if link.get("ns") != 0 or not link.get("exists"):
            continue
        title = unicodedata.normalize("NFC", (link.get("title") or "").strip())
        if not title.endswith(YEAR_SUFFIX):
            continue
        if title.startswith(VOLUME_PREFIX):
            continue
        out.append(title)
    return out


def discover_titles():
    """Candidate tale pages, from the two 1857 volume pages, via prop=links.

    prop=links is the API's own view of a page's outgoing links: it arrives
    already parsed, already carrying ns and exists, and does not depend on the
    skin's HTML. Scraping hrefs out of rendered HTML is what this replaces.
    """
    seen, out = set(), []
    for idx in INDEX_PAGES:
        try:
            links = api_parse_raw(idx, "links").get("links") or []
        except Exception as exc:
            print("  index %r unavailable: %s" % (idx, exc), file=sys.stderr)
            continue
        found = 0
        for title in tale_links(links):
            if title in seen:
                continue
            seen.add(title)
            out.append(title)
            found += 1
        print("  %s: %d tale page(s)" % (idx, found))
    return out


def crawl_mapping():
    """{khm: {page,title,revid}} built by asking every candidate page what number
    it prints. Slow (one request per page) but done once and cached."""
    titles = discover_titles()
    print("discovered %d candidate 1857 pages" % len(titles))
    claims, legends, unreadable, warnings = [], 0, 0, 0
    for t in titles:
        try:
            page = api_parse(t)
        except Exception as exc:
            print("  skip %s: %s" % (t, exc), file=sys.stderr)
            unreadable += 1
            continue
        res = tale_number(page["html"], page["wikitext"], t)
        if res.number is None:
            legends += 1
            print("  skip %s" % res.message, file=sys.stderr)
            continue
        if res.message:                      # a renumbered tale: expected, not fatal
            warnings += 1
            print("  WARNING %s" % res.message, file=sys.stderr)
        claims.append((res.number, {
            "page": t,
            "title": re.sub(r"\s*\(1857\)\s*$", "", t).strip(),
            "revid": page["revid"],
        }))

    try:
        mapping = assemble_mapping(claims)
    except DuplicateNumber as exc:
        print("\nNUMBERING CONTROL FAILED — one 1857 number, two pages:", file=sys.stderr)
        for line in exc.conflicts:
            print("  " + line, file=sys.stderr)
        print("Committing nothing.", file=sys.stderr)
        raise SystemExit(3)

    print("mapping: %d numbered tales" % len(mapping))
    print("skipped as Kinderlegenden/specials (unnumbered in the 1857 sequence, "
          "out of scope for this pass): %d" % legends)
    if warnings:
        print("%d page(s) where the printed numeral disagreed with SONSTIGES — renumbered "
              "tales; the printed numeral was used" % warnings)
    if unreadable:
        print("%d page(s) could not be fetched" % unreadable)
    return mapping


def save_mapping(mapping):
    os.makedirs(SRC_DIR, exist_ok=True)
    with open(INDEX_CACHE, "w", encoding="utf-8") as f:
        json.dump({"note": "KHM number read off each page's own Textdaten box; never positional.",
                   "mapping": {str(k): v for k, v in sorted(mapping.items())}},
                  f, ensure_ascii=False, indent=1)
        f.write("\n")


def load_mapping():
    if not os.path.exists(INDEX_CACHE):
        return {}
    try:
        with open(INDEX_CACHE, encoding="utf-8") as f:
            d = json.load(f)
        return {int(k): v for k, v in d.get("mapping", {}).items()}
    except Exception as exc:
        print("index cache unreadable (%s) — rebuilding" % exc, file=sys.stderr)
        return {}


def verify_mapping(mapping, fatal=True):
    """Prove the mapping against every published Grimm tale. Returns a list of
    disagreements (empty means proved)."""
    pub = published_khm()
    if not pub:
        raise SystemExit("no published Grimm tales found in stories.json — refusing to proceed")

    problems = []
    for khm, (title, _f) in sorted(pub.items()):
        got = mapping.get(khm)
        if not got:
            problems.append("KHM %d: mapping has no entry (published as %r)" % (khm, title))
            continue
        want_key = fold_title(TITLE_ALIASES.get(title, title))
        if fold_title(got["title"]) != want_key:
            problems.append("KHM %d: Wikisource says %r, corpus says %r"
                            % (khm, got["title"], title))
    if len(mapping) < MAPPING_MIN:
        problems.append("mapping too sparse: %d of 200 (need >= %d) — the Textdaten boxes are "
                        "not being read as expected" % (len(mapping), MAPPING_MIN))

    if fatal and problems:
        print("\nMAPPING CONTROL FAILED — refusing to archive anything:", file=sys.stderr)
        for p in problems[:20]:
            print("  " + p, file=sys.stderr)
        if len(problems) > 20:
            print("  ... and %d more" % (len(problems) - 20), file=sys.stderr)
        raise SystemExit(3)
    if not problems:
        print("mapping control PASSED: %d entries; all %d published tales agree."
              % (len(mapping), len(pub)))
    return problems


def build_mapping(force_rebuild=False, need=()):
    """Cached mapping, rebuilt from the pages themselves whenever the cache is
    missing, stale, incomplete for what was asked, or fails the control."""
    mapping = {} if force_rebuild else load_mapping()
    stale = (not mapping
             or verify_mapping(mapping, fatal=False)
             or any(k not in mapping for k in need))
    if stale:
        if mapping:
            print("index cache incomplete or disagreeing — rebuilding from the pages themselves")
        mapping = crawl_mapping()
        save_mapping(mapping)
    else:
        print("index cache: %d entries (%s)" % (len(mapping), os.path.relpath(INDEX_CACHE, ROOT)))
    verify_mapping(mapping, fatal=True)      # fatal, every invocation
    return mapping


# --------------------------------------------------------------------------
# CONTROL 2 — re-extract published tales and demand exact agreement
# --------------------------------------------------------------------------

def pick_controls(pub, mapping, n=3):
    """Prefer tales that exercise verse as well as prose."""
    verse, prose = [], []
    for khm in sorted(pub):
        if khm not in mapping:
            continue
        try:
            with open(os.path.join(ROOT, pub[khm][1]), encoding="utf-8") as f:
                story = json.load(f)
        except Exception:
            continue
        breaks = sum(s["t"].count("\n") for s in story["sentences"])
        (verse if breaks else prose).append(khm)
    chosen = verse[:max(1, n - 1)] + prose[:1]
    for khm in verse + prose:                 # top up if a bucket was empty
        if len(chosen) >= n:
            break
        if khm not in chosen:
            chosen.append(khm)
    return chosen[:n]


def extractor_control(mapping):
    pub = published_khm()
    controls = pick_controls(pub, mapping)
    if len(controls) < 3:
        print("EXTRACTOR CONTROL: fewer than three usable published tales.", file=sys.stderr)
        raise SystemExit(4)

    print("\n--- extractor control (%s) ---" % ", ".join("KHM %d" % k for k in controls))
    for khm in controls:
        title, fname = pub[khm]
        with open(os.path.join(ROOT, fname), encoding="utf-8") as f:
            story = json.load(f)
        page = mapping[khm]["page"]
        got = signature(extract_blocks(api_parse(page, props="text")["html"], page))
        want = story_signature(story)
        d = first_diff(want, got)
        if d:
            print("CONTROL FAILED for KHM %d (%s):\n  %s" % (khm, page, d), file=sys.stderr)
            print("Committing nothing.", file=sys.stderr)
            raise SystemExit(4)
        nl = want.count(NL)
        print("  KHM %-3d %-42s %4d tokens, %d line break(s)  OK"
              % (khm, title[:42], len(want) - nl, nl))


# --------------------------------------------------------------------------
# archiving
# --------------------------------------------------------------------------

def source_path(khm):
    return os.path.join(SRC_DIR, "khm-%03d-source.json" % khm)


def archive_one(khm, entry):
    page = entry["page"]
    got = api_parse(page)

    # Never archive on the strength of a cached number: re-read the numeral the
    # page itself prints, now.
    res = tale_number(got["html"], got["wikitext"], page)
    if res.number is None:
        raise RuntimeError(res.message)
    if res.message:
        print("  " + res.message, file=sys.stderr)
    if res.number != khm:
        raise RuntimeError("%s: the page prints %d., the index says KHM %d"
                           % (page, res.number, khm))

    blocks = extract_blocks(got["html"], page)
    if len(blocks) < 2:
        raise RuntimeError("%s: only %d block(s) — refusing to archive" % (page, len(blocks)))

    sig = signature(blocks)
    doc = {
        "khm": khm,
        "title": entry["title"],
        "slug": slugify(entry["title"]),
        "page": page,
        "revid": got["revid"],
        "source": ("Brüder Grimm, Kinder- und Hausmärchen, 7. Auflage (Ausgabe letzter Hand), "
                   "Dieterich, Göttingen 1857, KHM %d. Text from de.wikisource.org "
                   "(twice proofread); 1857 spelling preserved exactly." % khm),
        "extractor": ("archive_khm.py v2 (rules v2: <br>-only breaks; 1857 number off the "
                      "numeral the page prints, Textdaten box as cross-check only)"),
        "tokens": len([t for t in sig if t != NL]),
        "lineBreaks": sig.count(NL),
        "blocks": blocks,
    }
    os.makedirs(SRC_DIR, exist_ok=True)
    with open(source_path(khm), "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
        f.write("\n")
    return doc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--which", default="missing",
                    help='"missing", "all", or a comma-separated list of KHM numbers')
    ap.add_argument("--limit", type=int, default=DEFAULT_LIMIT,
                    help="max tales to archive in one run (keeps a run polite and bounded)")
    ap.add_argument("--selftest", action="store_true", help="run the controls and stop")
    ap.add_argument("--fixture", action="store_true",
                    help="run the offline fixture test only (no network)")
    ap.add_argument("--rebuild-index", action="store_true",
                    help="re-derive the number->title mapping from the pages themselves")
    args = ap.parse_args()

    print("=== control 0: fixture test (offline) ===")
    fixture_test()
    if args.fixture:
        print("\nfixture only: no network, no files written.")
        return

    want_explicit = []
    if args.which not in ("missing", "all"):
        want_explicit = [int(x) for x in re.split(r"[,\s]+", args.which.strip()) if x]

    print("\n=== control 1: number -> title mapping ===")
    mapping = build_mapping(force_rebuild=args.rebuild_index, need=want_explicit)

    print("\n=== control 2: extractor vs the published corpus ===")
    extractor_control(mapping)

    if args.selftest:
        print("\nselftest only: no source files written.")
        return

    if args.which == "all":
        want = sorted(mapping)
    elif args.which == "missing":
        want = [k for k in sorted(mapping) if not os.path.exists(source_path(k))]
    else:
        want = want_explicit

    print("\n%d tale(s) to archive; taking up to %d this run." % (len(want), args.limit))
    done, failed = [], []
    for khm in want[:args.limit]:
        entry = mapping.get(khm)
        if not entry:
            failed.append((khm, "no page for this number in the mapping"))
            print("  KHM %-3d FAILED: not in the mapping" % khm, file=sys.stderr)
            continue
        try:
            doc = archive_one(khm, entry)
        except Exception as exc:            # one bad tale never stops the rest
            failed.append((khm, str(exc)))
            print("  KHM %-3d FAILED: %s" % (khm, exc), file=sys.stderr)
            continue
        done.append(khm)
        print("  KHM %-3d %-42s %4d tokens, %d break(s), %d verse block(s)"
              % (khm, doc["title"][:42], doc["tokens"], doc["lineBreaks"],
                 sum(1 for b in doc["blocks"] if b["t"] == "v")))

    print("\narchived %d, failed %d, remaining %d"
          % (len(done), len(failed), max(0, len(want) - args.limit)))
    for khm, why in failed:
        print("  pending: KHM %d — %s" % (khm, why))


if __name__ == "__main__":
    main()
