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

HOW A TALE IS IDENTIFIED  (the rule grimm-corpus-plan.md proves and requires)
    The KHM number is read off EACH PAGE'S OWN Textdaten box, out of its
    SONSTIGES row ("seit 1812: KHM 76"). Never off index position, never off the
    index entry's text: the index's link order is not edition order — Die
    Goldkinder (KHM 85) sits between 62 and 63 in the DOM. Only the BOX's text is
    searched, never the whole page: the "Andere Version" footer links to
    .../Anmerkungen#76 and would be a second number to trip over. A box offering
    two different numbers fails loudly and the tale is skipped — never guessed.
    The number is re-read from the page's own box again at write time, so nothing
    is ever archived on the strength of a cached number.

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
    1. NUMBER->TITLE MAPPING is proved against the published corpus: every Grimm
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


BARE_NUMERAL_RE = re.compile(r"^\d{1,3}\.$")


def drop_leading_headings(blocks, page="?"):
    """Defensive no-op guard for the centred "76." / "Die Nelke." heading.

    On a real tale page those two lines sit in a generic container, not a <p>,
    so the extractor never collects them (nelke.json's sentence 0 is the first
    line of the story, proving it). This drops AT MOST the first two blocks, and
    only when a block is exactly a bare numeral or exactly the tale's own title.
    It is expected never to fire; if it does, it says so, because a page whose
    markup changed shape is news, not something to swallow silently.
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
        if BARE_NUMERAL_RE.match(x):
            why = "bare numeral"
        elif title_key and fold_title(x) == title_key:
            why = "tale title"
        if why is None:
            break
        print("  %s: leading-heading guard dropped a block (%s): %r"
              % (page, why, x), file=sys.stderr)
        out.pop(0)
    return out


def extract_blocks(html, page="?"):
    """Ordered [{'t':'p'|'v','x':...}] from a Wikisource parse fragment."""
    soup = BeautifulSoup(html, "lxml")
    root = soup.select_one(".mw-parser-output") or soup

    for el in root.select(DROP_SELECTOR):
        el.decompose()

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
# the KHM number, read off the page's OWN Textdaten box
# --------------------------------------------------------------------------

KHM_RE = re.compile(r"KHM\s*[:.\s]?\s*(\d{1,3})")
BOX_SELECTORS = ("table.ws-header", "#ws-data", "table.textdaten", ".ws-header", ".textdaten")

# The Textdaten template's own field, in raw wikitext: "|SONSTIGES=seit 1812: KHM 76".
# Unambiguous by construction — it is one named field of one template.
SONSTIGES_RE = re.compile(r"^\|\s*SONSTIGES\s*=.*?KHM\s*[:.\s]?\s*(\d{1,3})", re.M)


class AmbiguousNumber(RuntimeError):
    """The Textdaten box offered more than one KHM number. Never guess."""


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


def khm_number(html, wikitext="", page="?"):
    """Read the KHM number off the page's OWN Textdaten box.

    The index page's link order is NOT edition order (Die Goldkinder, KHM 85,
    sits between 62 and 63 in the DOM). Never count positions, and never take
    the number from prose elsewhere on the page when a box is present.

    PRIMARY PATH — the box's SONSTIGES row, which reads "seit 1812: KHM 76".
    Only the BOX's text is searched, never the whole page: the "Andere Version"
    footer links to "Kinder- und Haus-Märchen Band 3 (1856)/Anmerkungen#76" and
    is exactly the sort of second number that must not be mistaken for the datum.

    Two different numbers in the box raises AmbiguousNumber. A tale whose number
    cannot be read fails loudly and is skipped; it is never guessed.

    Read this BEFORE the extractor touches the page. The box is a <table> and
    extract_blocks decomposes tables — but each parses its own fresh soup from
    the HTML string, so neither can strip the other's evidence. Keep it that way:
    do not pass a shared, already-pruned soup in here.
    """
    soup = BeautifulSoup(html or "", "lxml")
    box = textdaten_box(soup)
    if box is not None:
        nums = _plausible(KHM_RE.findall(box.get_text(" ", strip=True)))
        if len(nums) > 1:
            raise AmbiguousNumber(
                "%s: Textdaten box offers %d different KHM numbers (%s) — refusing to guess"
                % (page, len(nums), ", ".join(str(n) for n in sorted(nums))))
        if nums:
            return nums.pop()

    # Fallbacks, in order, only when the box yielded nothing: the same datum as
    # a named field of the header template in the raw wikitext, then any KHM
    # mention in the wikitext at all.
    m = SONSTIGES_RE.search(wikitext or "")
    if m:
        n = int(m.group(1))
        if 1 <= n <= KHM_MAX:
            return n
    m = KHM_RE.search(wikitext or "")
    if m:
        n = int(m.group(1))
        if 1 <= n <= KHM_MAX:
            return n
    return None


def _plausible(found):
    """The distinct in-range numbers among regex hits."""
    return {int(x) for x in found if 1 <= int(x) <= KHM_MAX}


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
<p>Es war einmal ein Mann
und eine Frau<sup class="reference">FUSSNOTE-XYZ</sup>, die wünschten sich[7] ein Kind.</p>
<div class="poem"><p>Rapunzel, Rapunzel,<br/>
laß mir dein Haar herunter.</p></div>
<p>Da rief die Zauberin:<br>komm herab!</p>
<table class="prettytable"><tr><td>Fußnote KHM 200</td></tr></table>
<div class="catlinks">Kategorien: Märchen</div>
</div>
"""

# The real shape of a tale page, modelled on Die Nelke (1857) as it is live
# today: the number lives in the Textdaten box's SONSTIGES row, and the footer
# carries an "Andere Version" link to the 1856 Anmerkungsband whose fragment is
# also "76" — the decoy the box-only rule exists to ignore.
FIXTURE_TEXTDATEN_HTML = """
<div class="mw-parser-output">
<table class="ws-header"><tr><th colspan="2">Textdaten</th></tr>
<tr><td>Autor:</td><td>Brüder Grimm</td></tr>
<tr><td>Titel:</td><td>Die Nelke</td></tr>
<tr><td>Sonstiges:</td><td>seit 1812: KHM 76</td></tr></table>
<div style="text-align:center">76.</div>
<div style="text-align:center"><b>Die Nelke.</b></div>
<p>Es war eine Königin, die hatte unser Herr Gott verschlossen.</p>
<p>Da sprach der Koch: es soll geschehen.</p>
<div class="ws-noexport">Andere Version:
<a href="/wiki/Kinder-_und_Haus-M%C3%A4rchen_Band_3_(1856)/Anmerkungen#76">Anmerkungen</a>
— dort als KHM 199 geführt</div>
</div>
"""

# A box offering two different numbers: must fail loudly, never be guessed.
FIXTURE_AMBIGUOUS_HTML = """
<div class="mw-parser-output">
<table class="ws-header"><tr><th>Textdaten</th></tr>
<tr><td>Sonstiges:</td><td>seit 1812: KHM 76</td></tr>
<tr><td>Anmerkung:</td><td>vergleiche KHM 77</td></tr></table>
<p>Es war einmal.</p>
</div>
"""

# A box with no number at all: the wikitext SONSTIGES field is the fallback.
FIXTURE_NO_BOX_NUMBER_HTML = """
<div class="mw-parser-output">
<table class="ws-header"><tr><th>Textdaten</th></tr>
<tr><td>Titel:</td><td>Die Nelke</td></tr></table>
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

    n = khm_number(FIXTURE_HTML)
    check("KHM number read off the Textdaten box (12, not 199/200)", n == 12, n)

    # ---- the number, in the shape the live pages actually have --------------
    n = khm_number(FIXTURE_TEXTDATEN_HTML, page="Die Nelke (1857)")
    check("SONSTIGES row 'seit 1812: KHM 76' reads as 76", n == 76, n)
    check("the 1856 Anmerkungen footer (#76 / 'KHM 199') is not read as the number",
          n == 76 and "KHM 199" in FIXTURE_TEXTDATEN_HTML, n)

    # The box is a <table> and the extractor decomposes tables. Reading the
    # number must not depend on extraction order — prove both orders agree.
    _ = extract_blocks(FIXTURE_TEXTDATEN_HTML, page="Die Nelke (1857)")
    check("number still readable after the extractor has run (no shared soup)",
          khm_number(FIXTURE_TEXTDATEN_HTML, page="Die Nelke (1857)") == 76)

    try:
        bad = khm_number(FIXTURE_AMBIGUOUS_HTML, page="<ambiguous>")
        raised = False
    except AmbiguousNumber as exc:
        raised, bad = True, str(exc)
    check("two different numbers in the box fail loudly, never guessed", raised, bad)
    check("the ambiguity message names both numbers",
          raised and "76" in bad and "77" in bad, bad)

    check("wikitext |SONSTIGES= is the fallback when the box has no number",
          khm_number(FIXTURE_NO_BOX_NUMBER_HTML, FIXTURE_WIKITEXT) == 76)
    check("no number anywhere returns None (caller skips loudly)",
          khm_number(FIXTURE_NO_BOX_NUMBER_HTML, "") is None)

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
    check("guard is a no-op on the real page shape (heading is not a <p>)",
          len(real) == 2 and real[0]["x"].startswith("Es war eine Königin"), real)
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
    """{khm: {page,title,revid}} built by asking every candidate page its own
    number. Slow (one request per page) but done once and cached."""
    titles = discover_titles()
    print("discovered %d candidate 1857 pages" % len(titles))
    mapping, skipped = {}, 0
    for t in titles:
        try:
            page = api_parse(t)
        except Exception as exc:
            print("  skip %s: %s" % (t, exc), file=sys.stderr)
            skipped += 1
            continue
        try:
            n = khm_number(page["html"], page["wikitext"], t)
        except AmbiguousNumber as exc:      # never guessed; loud and skipped
            print("  skip %s: %s" % (t, exc), file=sys.stderr)
            skipped += 1
            continue
        if n is None:
            print("  skip %s: no KHM number in its own Textdaten box" % t, file=sys.stderr)
            skipped += 1
            continue
        if n in mapping and mapping[n]["page"] != t:
            print("  KHM %d claimed twice: %r and %r — keeping the first"
                  % (n, mapping[n]["page"], t), file=sys.stderr)
            continue
        mapping[n] = {
            "page": t,
            "title": re.sub(r"\s*\(1857\)\s*$", "", t).strip(),
            "revid": page["revid"],
        }
    print("mapping: %d numbered tales (%d pages skipped)" % (len(mapping), skipped))
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

    # Never archive on the strength of a cached number: re-read it from this
    # page's own Textdaten box, now — and before the extractor, which drops the
    # tables the box is made of.
    n = khm_number(got["html"], got["wikitext"], page)
    if n is None:
        raise RuntimeError("%s: no KHM number in its own Textdaten box" % page)
    if n != khm:
        raise RuntimeError("%s: page says KHM %d, index says KHM %d" % (page, n, khm))

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
        "extractor": "archive_khm.py v1 (rules v2: <br>-only breaks, KHM off the Textdaten box)",
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
