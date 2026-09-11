#!/usr/bin/env python3
"""archive_perrault.py -- archive Perrault's 1697 Histoires ou contes du temps passe from
fr.wikisource.org into sources/perrault-NN-source.json, with fatal controls.

Written 2026-09-10 in the Perrault infrastructure firing. It runs on a GitHub runner, because the
Cowork sandbox cannot reach Wikisource. It was proved offline against synthetic fixtures only, so
its first live run is also the first time it has seen the real pages. That is why it records
everything it saw:

  * sources/perrault-archive-log.txt: discovery listing, per-page block summaries, every control
    line and a final verdict. It is committed whether the run passes or fails.
  * sources/perrault-raw/: the rendered HTML (and wikitext) of every page fetched, so a later
    firing can build real fixtures and repair the extractor offline.

A text is written only when every control for every text passes (all or nothing). No drafter is
ever handed text from a run that failed.

WITNESSES
  A (edition of record): "Histoires ou Contes du temps passe (1697)/Original", one page per
    text (the dedication and eight tales), plus its "Texte entier" page.
  B (check only): "OEuvres choisies de Charles Perrault, edition 1826", its eight prose tales.
    B never contributes a character to any archived text.

FATAL CONTROLS
  0 fixture     the offline fixture test, with injected defects the controls must catch
  1 discovery   exactly one A page per text, one Texte entier page, one B page per tale
  2 entier      each text's body, extracted from its own page, occurs contiguously and in book
                order inside the Texte entier extraction, token for token
  3 proofread   where a page transcludes the Page: namespace, every such page is at quality 3
                (proofread) or 4 (validated); a page without scans is recorded as such, and its
                source file carries `sourceClause` saying so
  4 inventory   every character outside the declared inventory fails the run, named
  5 collation   A against B after spelling normalisation: A carries at least as many MORALITE
                headings as B; no stretch longer than 40 words exists in B and not in A; every
                unmatched run longer than 5 words on either side is listed in the source file

Usage:
  python archive_perrault.py --fixture        offline fixture test only
  python archive_perrault.py                  archive (skips when all nine are archived)
  python archive_perrault.py --force          re-archive even if all nine exist
  python archive_perrault.py --replay sources/perrault-raw
                                              offline replay of the committed raw pages (writes nothing)

REPAIR OF 2026-09-11 (after the first live run failed, as designed): the extractor dropped bare text
between blocks (all of Le Maistre Chat's prose) and treated layout tables as furniture (the MORALITES
of Riquet and Le petit Poucet, and the verse in the dedication); invisible indentation spacers leaked
into verse; titles set over several centred lines were not recognised; a MORALITE and its verse in one
centred block were not split; and witness B was looked up through a red link. The walker now keeps
every character of visible text, a new fatal coverage control proves it, raw pages carry .meta.json
and .proofread.json, witness B uses existing pages only (falling back to the 1902 edition), and a
failed fetch is a logged control failure rather than an exception.
"""
import argparse, collections, difflib, hashlib, json, os, re, sys, time, unicodedata

API = "https://fr.wikisource.org/w/api.php"
WIKI = "https://fr.wikisource.org/wiki/"
A_ROOT = "Histoires ou Contes du temps pass\u00e9 (1697)/Original"
A_PREFIXES = ["Histoires ou Contes du temps pass\u00e9 (1697)", "Histoires ou contes du temps pass\u00e9 (1697)"]
B_ROOT = "\u0152uvres choisies de Charles Perrault, \u00e9dition 1826"
# Witness B is check-only. The 1826 edition comes first; a tale it lacks as an existing page is collated
# against the 1902 Casterman edition instead, and the log and the source file say which was used.
B_ROOTS = [B_ROOT, "Contes de Perrault (\u00e9d. 1902)"]
UA = "LectoriumArchiver/1.0 (https://github.com/zevfarber/Lectorium; reading-companion source archive)"
MIN_INTERVAL = 1.0
MAX_ATTEMPTS = 6
PAGE_NS = 104   # Page: on fr.wikisource

TEXTS = [  # seq, id, title patterns on the folded last path segment
    (1, "perrault-a-mademoiselle", [r"\bmademoiselle\b"]),
    (2, "belle-au-bois-dormant", [r"\bbelle au bois dormant\b"]),
    (3, "petit-chaperon-rouge", [r"\bchaperon rouge\b"]),
    (4, "barbe-bleue", [r"\bbarbe bleue\b"]),
    (5, "maitre-chat", [r"\bmais?tre chat\b", r"\bchat botte\b"]),
    (6, "les-fees", [r"^(les )?fees$"]),
    (7, "cendrillon", [r"\bcendrillon\b"]),
    (8, "riquet-a-la-houppe", [r"\briquet\b"]),
    (9, "petit-poucet", [r"\bpoucet\b"]),
]
ENTIER = [r"\btexte entier\b"]

# the reader's WORD_RE (same classes as reader.html and align_wordref.py)
WORD_CLASS = ('A-Za-z\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u00ff\\u0100-\\u024F\\u0300-\\u036F\\u1E00-\\u1EFF'
              '\u0386-\u03ff\u0400-\u04ff\\u1F00-\\u1FFF\\u1820-\\u1877\\u180B-\\u180E'
              '\\u0620-\\u065F\\u0670-\\u06D3\\u06D5-\\u06ED')
HAN_CLASS = '\\u3400-\\u4DBF\\u4E00-\\u9FFF\\uF900-\\uFAFF'
WORD_RE = re.compile('[' + HAN_CLASS + ']|[' + WORD_CLASS + ']+(?:[-\\[\\]()][' + WORD_CLASS + ']+)*')
TOKEN_RE = re.compile(WORD_RE.pattern + r"|[^\s]")

INVENTORY = ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
             "\u00e0\u00e2\u00e4\u00e7\u00e9\u00e8\u00ea\u00eb\u00ee\u00ef\u00f4\u00f6\u00f9\u00fb\u00fc\u00ff\u0153\u00e6\u00c0\u00c2\u00c4\u00c7\u00c9\u00c8\u00ca\u00cb\u00ce\u00cf\u00d4\u00d6\u00d9\u00db\u00dc\u0178\u0152\u00c6\u017f"
             "0123456789"
             ".,;:!?'\u2019\u00ab\u00bb()[]-\u2013\u2014\u2026&*")
HEADING_RE = re.compile(r"^(AUTRE\s+)?MORALIT[E\u00c9]S?\s*\.?$", re.I)
SUBTITLE_RE = re.compile(r"^(CONTE|CONTES)\s*\.?$", re.I)
BR = "\u241f"

HERE = os.path.dirname(os.path.abspath(__file__))


def repo_root():
    d = HERE
    for _ in range(6):
        if os.path.exists(os.path.join(d, "stories.json")):
            return d
        d = os.path.dirname(d)
    return os.getcwd()


LOG = []
QUIET = [False]


def log(msg=""):
    LOG.append(msg)
    if not QUIET[0]:
        print(msg)


# ----------------------------------------------------------------------------- API layer
class Api:
    """Live MediaWiki API. The fixture test substitutes FakeApi with the same two methods."""

    def __init__(self):
        import requests
        self.s = requests.Session()
        self.s.headers["User-Agent"] = UA
        self.last = 0.0

    def _get(self, params):
        import requests
        params = dict(params, format="json", formatversion="2")
        last = None
        for attempt in range(MAX_ATTEMPTS):
            wait = MIN_INTERVAL - (time.time() - self.last)
            if wait > 0:
                time.sleep(wait)
            self.last = time.time()
            try:
                r = self.s.get(API, params=params, timeout=60)
            except requests.RequestException as e:
                last = str(e); time.sleep(2 ** attempt); continue
            if r.status_code in (429, 500, 502, 503, 504):
                last = "HTTP %s" % r.status_code
                try:
                    pause = float(r.headers.get("Retry-After"))
                except (TypeError, ValueError):
                    pause = 5 * (attempt + 1)
                time.sleep(pause); continue
            if r.status_code != 200:
                raise RuntimeError("HTTP %s for %r" % (r.status_code, params))
            try:
                d = r.json()
            except ValueError:
                last = "non-JSON body"; time.sleep(5 * (attempt + 1)); continue
            if "error" in d:
                raise RuntimeError("API error for %r: %s" % (params.get("page") or params.get("titles"), d["error"]))
            return d
        raise RuntimeError("could not fetch %r (last: %s)" % (params, last))

    def parse(self, page, props="text|wikitext|revid|templates|links"):
        return self._get({"action": "parse", "page": page, "prop": props, "redirects": "1"})["parse"]

    def query(self, params):
        out, cont = [], {}
        while True:
            d = self._get(dict({"action": "query"}, **params, **cont))
            out.append(d.get("query", {}))
            if "continue" not in d:
                return out
            cont = d["continue"]


# ----------------------------------------------------------------------------- folding / extraction
def fold(s):
    s = s.replace("\u017f", "s").replace("\u0153", "oe").replace("\u0152", "OE").replace("\u00e6", "ae").replace("\u00c6", "AE")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    s = re.sub(r"[\u2019'`\-\u2013\u2014_]", " ", s)
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def classify(title, patterns):
    last = fold(title.rsplit("/", 1)[-1])
    return any(re.search(p, last) for p in patterns)


def clean_ws(s):
    s = s.replace("\u00ad", "").replace("\u200b", "").replace("\ufeff", "")
    return re.sub(r"[\s\u00a0\u202f\u2009\u2007]+", " ", s).strip()


DROP_SELECTOR = (".ws-noexport, .noprint, sup.reference, style, script, .catlinks, .mw-editsection, "
                 ".reflist, .references, #toc, .toc, .pagenum, .ws-pagenum, [class*=pagenum], "
                 "#headertemplate, .headertemplate, .ws-header, #subheader, #footertemplate, .footertemplate, "
                 ".ws-footer, #subpages, .mw-empty-elt, figure, img")
# Furniture that is expected to carry words; anything else removed with words is logged by name.
EXPECTED_FURNITURE = ("headertemplate", "subheader", "ws-data", "footertemplate", "modernisations",
                      "small .ws-noexport")
HIDDEN_STYLE_RE = re.compile(r"visibility\s*:\s*hidden|display\s*:\s*none", re.I)
HEADINGS = {"h1", "h2", "h3", "h4", "h5", "h6"}
BLOCKY = {"p", "div", "center", "blockquote", "ul", "ol", "li", "dl", "dd", "dt", "table", "tbody", "thead",
          "tfoot", "tr", "td", "th", "poem", "figure"} | HEADINGS
TITLE_TAGS = {"div", "center"} | HEADINGS
FIN_RE = re.compile(r"^FIN\s*\.?$")
BLANK = "␀"


def is_poem(el):
    cls = el.get("class") or []
    return el.name == "poem" or any("poem" in c for c in cls)


def has_blocky_child(el):
    return any(getattr(c, "name", None) in BLOCKY for c in el.descendants)


def _lines(nodes):
    """Text of a run of nodes, split at <br> and at nested block boundaries. '' marks a blank line."""
    from bs4 import NavigableString, Comment
    parts = []

    def rec(n):
        if isinstance(n, Comment):
            return
        if isinstance(n, NavigableString):
            parts.append(str(n)); return
        if n.name == "br":
            parts.append(BR); return
        blocky = n.name in BLOCKY
        if blocky:
            parts.append(BR)
        for c in n.children:
            rec(c)
        if blocky:
            parts.append(BR)
    for n in nodes:
        rec(n)
    raw = "".join(parts).split(BR)
    lines = [clean_ws(x) for x in raw]
    # trim leading and trailing blanks; keep internal blanks (a stanza or section separator)
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    return lines


def prepare(html):
    """The page body with furniture and invisible elements removed. Returns (root, removed-notes)."""
    from bs4 import BeautifulSoup, Comment
    soup = BeautifulSoup(html or "", "lxml")
    root = soup.select_one(".mw-parser-output") or soup.body or soup
    for c in root.find_all(string=lambda s: isinstance(s, Comment)):
        c.extract()
    removed = []
    for el in root.select(DROP_SELECTOR):
        if getattr(el, "decomposed", False):
            continue
        words = 0 if el.name in ("style", "script") else len(WORD_RE.findall(el.get_text(" ")))
        ident = " ".join([el.name or ""] + (["#" + el.get("id")] if el.get("id") else []) + ["." + c for c in (el.get("class") or [])])
        if words > 3 and not any(x in ident for x in EXPECTED_FURNITURE):
            removed.append("%s (%d words): %s" % (ident, words, clean_ws(el.get_text(" "))[:80]))
        el.decompose()
    for el in root.find_all(style=HIDDEN_STYLE_RE):
        if getattr(el, "decomposed", False):
            continue
        el.decompose()
    return root, removed


def extract(html, _drop_hook=None):
    """[{'kind':'p'|'br'|'v'|'h', 'lines':[...], 'tag':..., 'gap':bool}] in document order.

    Every character of visible text lands in exactly one item: bare text between blocks becomes its
    own item, and tables are layout, not furniture. `gap` is True when a blank separator (an empty
    paragraph, a spacer div or a blank line) stands between this item and the previous one; a page
    break alone is not a gap. The coverage control proves nothing was lost.
    """
    from bs4 import NavigableString, Comment
    root, _ = prepare(html)
    out = []
    state = {"gap": False}

    def emit(kind, lines, tag):
        if _drop_hook and _drop_hook(lines):
            return
        if not any(lines):
            state["gap"] = True
            return
        group, first = [], True
        for ln in lines + [""]:
            if ln:
                group.append(ln); continue
            if group:
                k = kind if kind in ("v", "h") else ("br" if len(group) > 1 else "p")
                out.append({"kind": k, "lines": group, "tag": tag, "gap": state["gap"] or not first})
                state["gap"] = False
                group, first = [], False
            else:
                state["gap"] = True

    def flush(run):
        if not run:
            return
        lines = _lines(run)
        if not any(lines):
            # an empty inline run (whitespace, or the empty wrapper a page number leaves behind) is
            # not a separator; a bare <br> between blocks is
            if any(getattr(n, "name", None) == "br" for n in run):
                state["gap"] = True
            return
        emit("p", lines, "#text")

    def walk(node):
        run = []
        for ch in list(node.children):
            if isinstance(ch, Comment):
                continue
            if isinstance(ch, NavigableString) or ch.name not in BLOCKY:
                run.append(ch); continue
            flush(run); run = []
            if is_poem(ch):
                emit("v", _lines([ch]), ch.name)
            elif ch.name in HEADINGS:
                lines = [x for x in _lines([ch]) if x]
                emit("h", [" ".join(lines)] if lines else [], ch.name)
            elif has_blocky_child(ch):
                walk(ch)
            else:
                emit("p", _lines([ch]), ch.name)
        flush(run)
    walk(root)
    return out


def coverage(html, items):
    """Fatal control: the visible text of the page, whitespace ignored, equals the items' text."""
    root, removed = prepare(html)
    page = re.sub(r"\s+", "", root.get_text(""))
    got = re.sub(r"\s+", "", "".join("".join(it["lines"]) for it in items))
    if page == got:
        return None, removed
    k = 0
    while k < min(len(page), len(got)) and page[k] == got[k]:
        k += 1
    return ("extraction differs from the page's visible text at character %d of %d: page …%s… extracted …%s…"
            % (k, len(page), page[max(0, k - 30):k + 30], got[max(0, k - 30):k + 30])), removed


def join_prose(lines, notes):
    out = lines[0]
    for ln in lines[1:]:
        if re.search(r"[" + WORD_CLASS + r"]-$", out):
            notes.append("a line ending in a hyphen joined without a space: %r" % (out[-20:] + ln[:20]))
            out += ln
        else:
            out += " " + ln
    return out


def structure(raw, text_patterns, sid, witness_b=False):
    """Title, then blocks with p/v/heading. Returns (title, printed, blocks, notes)."""
    notes = []
    items = list(raw)
    parts, k = [], 0
    while k < len(items) and len(parts) < 5:
        it = items[k]
        txt = " ".join(it["lines"])
        if (it["tag"] in TITLE_TAGS and it["kind"] != "v" and len(WORD_RE.findall(txt)) <= 8
                and not SUBTITLE_RE.match(txt) and not HEADING_RE.match(txt)):
            parts.append(txt); k += 1
        else:
            break
    title = printed = None
    if parts and any(re.search(p, fold(" ".join(parts))) for p in text_patterns):
        printed = " ".join(parts)
        title = re.sub(r"\s*\.\s*$", "", printed)
        notes.append("title block(s) %s dropped from the text: %r" % (list(range(k)), parts))
        items = items[k:]
    else:
        if not witness_b:
            notes.append("NO TITLE FOUND: leading title-like blocks %r" % parts)
    while items and SUBTITLE_RE.match(" ".join(items[0]["lines"])):
        notes.append("subtitle dropped: %r" % " ".join(items[0]["lines"]))
        items = items[1:]
    if items and FIN_RE.match(" ".join(items[-1]["lines"])):
        notes.append("closing %r dropped from the text" % " ".join(items[-1]["lines"]))
        items = items[:-1]
    blocks = []
    in_moral = False
    for it in items:
        groups, cur = [], []
        for ln in it["lines"]:
            if HEADING_RE.match(ln):
                if cur:
                    groups.append(("lines", cur)); cur = []
                groups.append(("heading", ln))
            else:
                cur.append(ln)
        if cur:
            groups.append(("lines", cur))
        for gi, (what, val) in enumerate(groups):
            if what == "heading":
                blocks.append({"text": val, "heading": True, "p": True})
                in_moral = True
                continue
            gap = it["gap"] if gi == 0 else True
            if it["kind"] == "v" or in_moral:
                text = "\n".join(val)
                if blocks and blocks[-1].get("v") and not gap:
                    notes.append("verse continued across a page break merged into one block: %r" % val[0][:50])
                    blocks[-1]["text"] += "\n" + text
                else:
                    blocks.append({"text": text, "v": True})
            else:
                if len(val) > 1:
                    notes.append("line breaks inside a prose block joined: %r" % " ".join(val)[:80])
                blocks.append({"text": join_prose(val, notes), "p": True})
    return title, printed, blocks, notes


def tokens(text):
    return TOKEN_RE.findall(text)


# ----------------------------------------------------------------------------- controls
def ctl_entier(bodies, entier_blocks):
    """bodies: [(sid, blocks)] in book order. Every body contiguous and in order in entier."""
    E = tokens("\n".join(b["text"] for b in entier_blocks))
    pos, fails, gaps = 0, [], []
    for sid, blocks in bodies:
        B = tokens("\n".join(b["text"] for b in blocks))
        if not B:
            fails.append("%s: empty body" % sid); continue
        found = -1
        head = B[:8]
        i = pos
        while True:
            try:
                i = E.index(head[0], i)
            except ValueError:
                break
            if E[i:i + len(B)] == B:
                found = i; break
            i += 1
        if found < 0:
            # locate the first divergence for the log
            best, where = 0, None
            for j in range(pos, len(E)):
                if E[j:j + len(head)] == head:
                    k = 0
                    while k < len(B) and j + k < len(E) and E[j + k] == B[k]:
                        k += 1
                    if k > best:
                        best, where = k, j
            ctx = ("diverges after %d of %d tokens: page \u2026%s\u2026 entier \u2026%s\u2026"
                   % (best, len(B), " ".join(B[max(0, best - 5):best + 5]),
                      " ".join(E[where + max(0, best - 5):where + best + 5]))) if where is not None else "start not found"
            fails.append("%s: body not found contiguously in Texte entier (%s)" % (sid, ctx))
            continue
        if found > pos:
            gaps.append("%s: %d token(s) in Texte entier before it: %s" % (sid, found - pos, " ".join(E[pos:found])[:160]))
        pos = found + len(B)
    if pos < len(E):
        gaps.append("after the last text: %d token(s): %s" % (len(E) - pos, " ".join(E[pos:])[:160]))
    return fails, gaps


def norm_words(text):
    s = text.replace("&", " et ").replace("\u017f", "s")
    s = s.replace("\u00e7", "c").replace("\u00c7", "C")
    words = fold(s).split()
    out = []
    for w in words:
        w = re.sub(r"sc(?=[aou])", "s", w)
        w = w.replace("y", "i")
        w = w.replace("oi", "ai")
        w = re.sub(r"(?<=[a-z])s(?=[bcdfgjklmnpqtvz])", "", w)
        w = re.sub(r"z$", "s", w)
        w = re.sub(r"([a-z])\1", r"\1", w)
        out.append(w)
    return out


def ctl_collation(sid, a_blocks, b_blocks):
    fails, runs = [], []
    a_head = sum(1 for b in a_blocks if b.get("heading"))
    b_head = sum(1 for b in b_blocks if b.get("heading"))
    if a_head == 0:
        fails.append("%s: witness A has no MORALIT\u00c9 heading" % sid)
    if a_head < b_head:
        fails.append("%s: witness A has %d MORALIT\u00c9 heading(s), witness B %d" % (sid, a_head, b_head))
    A = norm_words(" ".join(b["text"] for b in a_blocks))
    B = norm_words(" ".join(b["text"] for b in b_blocks))
    sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        la, lb = i2 - i1, j2 - j1
        if la > 5 or lb > 5:
            runs.append({"op": op, "aWords": la, "bWords": lb, "aAt": i1, "bAt": j1,
                         "a": " ".join(A[i1:i2])[:200], "b": " ".join(B[j1:j2])[:200]})
        if lb - la > 40:
            fails.append("%s: %d words in witness B are missing from witness A near A word %d: %s"
                         % (sid, lb - la, i1, " ".join(B[j1:j1 + 12])))
    return fails, runs, round(sm.ratio(), 4)


# ----------------------------------------------------------------------------- discovery
def discover(api):
    """Witness-A and witness-B pages. Only pages that exist count (allpages lists existing pages; a
    root page's links can be red links, so links are logged but never chosen)."""
    titles = set()
    for pre in A_PREFIXES:
        for q in api.query({"list": "allpages", "apprefix": pre + "/", "apnamespace": 0, "aplimit": "max"}):
            titles.update(p["title"] for p in q.get("allpages", []))
    a_cands = sorted(t for t in titles if "/original" in t.lower() and t != A_ROOT)
    log("discovery: %d existing witness-A page(s) under /Original:" % len(a_cands))
    for t in a_cands:
        log("   A  %s" % t)
    b_by_root = {}
    for broot in B_ROOTS:
        bt = set()
        for q in api.query({"list": "allpages", "apprefix": broot + "/", "apnamespace": 0, "aplimit": "max"}):
            bt.update(p["title"] for p in q.get("allpages", []))
        b_by_root[broot] = bt
        log("discovery: %d existing witness-B page(s) under %s" % (len(bt), broot))
        for t in sorted(bt):
            if not t.rsplit("/", 1)[-1].lower().startswith("remarque"):
                log("   B  %s" % t)
    fails, amap, bmap = [], {}, {}
    for seq, sid, pats in TEXTS:
        hits = [t for t in a_cands if classify(t, pats) and not classify(t, ENTIER)]
        if len(hits) != 1:
            fails.append("discovery: %s matches %d witness-A page(s): %s" % (sid, len(hits), hits))
        else:
            amap[sid] = hits[0]
        if seq == 1:
            continue
        chosen = None
        for broot in B_ROOTS:
            bh = sorted(t for t in b_by_root[broot] if classify(t, pats))
            if len(bh) == 1:
                chosen = bh[0]
                if broot != B_ROOTS[0]:
                    log("discovery: %s has no page in %s; witness B falls back to %s" % (sid, B_ROOTS[0], chosen))
                break
            if len(bh) > 1:
                fails.append("discovery: %s matches %d witness-B page(s) in %s: %s" % (sid, len(bh), broot, bh))
                chosen = False
                break
        if chosen:
            bmap[sid] = chosen
        elif chosen is None:
            fails.append("discovery: %s has no existing witness-B page in any of %s" % (sid, B_ROOTS))
    ent = [t for t in a_cands if classify(t, ENTIER)]
    if len(ent) != 1:
        fails.append("discovery: Texte entier matches %d page(s): %s" % (len(ent), ent))
    return fails, amap, bmap, (ent[0] if len(ent) == 1 else None)


def proofread_levels(api, templates):
    pages = sorted(t["title"] for t in templates if t.get("ns") == PAGE_NS or t["title"].startswith("Page:"))
    levels = {}
    for i in range(0, len(pages), 50):
        for q in api.query({"prop": "proofread", "titles": "|".join(pages[i:i + 50])}):
            for p in q.get("pages", []):
                pr = p.get("proofread") or {}
                levels[p["title"]] = pr.get("quality")
    return pages, levels


# ----------------------------------------------------------------------------- the run
def safe_name(title):
    return re.sub(r"[^A-Za-z0-9]+", "_", fold(title))[:90]


def entier_blocks(items):
    """Texte entier items rendered with the same joins the per-text blocks use."""
    out = []
    for it in items:
        if it["kind"] == "v":
            out.append({"text": "\n".join(it["lines"])})
        else:
            out.append({"text": join_prose(it["lines"], [])})
    return out


def run(api, out_dir, raw_dir, texts=TEXTS, write=True, fixed_discovery=None):
    """Returns (passed, results, fails). Writes source files only when every control passes."""
    all_fails = []
    controls = collections.defaultdict(list)
    if fixed_discovery:
        fails, amap, bmap, entier = fixed_discovery
    else:
        fails, amap, bmap, entier = discover(api)
    all_fails += fails
    for f in fails:
        log("FAIL " + f)
    if not fails:
        log("PASS discovery: one witness-A page per text, one Texte entier page, one witness-B page per tale")
    results = {}
    wanted = [(s, i, p) for s, i, p in TEXTS if i in {x[1] for x in texts}]

    def fetch(title):
        p = api.parse(title)
        if raw_dir:
            os.makedirs(raw_dir, exist_ok=True)
            base = os.path.join(raw_dir, safe_name(title))
            open(base + ".html", "w", encoding="utf-8").write(p.get("text") or "")
            open(base + ".wikitext", "w", encoding="utf-8").write(p.get("wikitext") or "")
            meta = {k: p.get(k) for k in ("title", "revid", "templates")}
            meta["requested"] = title
            open(base + ".meta.json", "w", encoding="utf-8").write(json.dumps(meta, ensure_ascii=False, indent=1))
        return p

    for seq, sid, pats in wanted:
        if sid not in amap:
            continue
        f = []
        try:
            page = fetch(amap[sid])
        except Exception as e:  # noqa: BLE001
            f.append("%s: witness-A page %r could not be fetched: %s" % (sid, amap[sid], e))
            for x in f:
                log("FAIL " + x)
            all_fails += f
            continue
        html = page.get("text")
        raw = extract(html)
        cov, removed = coverage(html, raw)
        title, printed, blocks, notes = structure(raw, pats, sid)
        log("")
        log("== %s  %s  (revid %s)" % (sid, amap[sid], page.get("revid")))
        log("   printed title: %r; %d block(s): %d prose, %d verse, %d heading"
            % (printed, len(blocks), sum(1 for b in blocks if b.get("p") and not b.get("heading")),
               sum(1 for b in blocks if b.get("v")), sum(1 for b in blocks if b.get("heading"))))
        for r in removed:
            log("   removed as furniture: " + r)
        for n in notes:
            log("   note: " + n)
        for b in blocks:
            t = b["text"].replace("\n", " / ")
            log("   | [%s] %s" % ("v" if b.get("v") else "h" if b.get("heading") else "p",
                                  t if len(t) <= 150 else t[:90] + " … " + t[-50:]))
        if cov:
            f.append("%s: coverage: %s" % (sid, cov))
        else:
            controls[sid].append("PASS coverage: every character of the page's visible text is in the title, "
                                 "a dropped subtitle or closing, or a block")
        if title is None:
            f.append("%s: no printed title found" % sid)
        if not blocks or sum(len(WORD_RE.findall(b["text"])) for b in blocks) < 80:
            f.append("%s: extraction implausibly short" % sid)
        if seq != 1 and not any(b.get("heading") for b in blocks):
            f.append("%s: no MORALITÉ heading found in the text" % sid)
        bad = sorted({c for b in blocks for c in b["text"] if c not in INVENTORY and c not in " \n"})
        if bad:
            f.append("%s: characters outside the declared inventory: %s"
                     % (sid, ", ".join("%r U+%04X %s" % (c, ord(c), unicodedata.name(c, "?")) for c in bad)))
        else:
            controls[sid].append("PASS inventory: every character of the text is in the declared inventory")
        clause = None
        pages = []
        try:
            pages, levels = proofread_levels(api, page.get("templates") or [])
        except Exception as e:  # noqa: BLE001
            f.append("%s: proofread levels could not be read: %s" % (sid, e))
            levels = {}
        if pages:
            low = {p: q for p, q in levels.items() if q is None or q < 3}
            if low:
                f.append("%s: %d of %d transcluded scan page(s) below 'proofread': %s"
                         % (sid, len(low), len(pages), ", ".join("%s=%s" % kv for kv in sorted(low.items())[:10])))
            else:
                hist = collections.Counter(levels.values())
                controls[sid].append("PASS proofread: %d transcluded scan page(s), quality %s"
                                     % (len(pages), ", ".join("%s×%d" % (k, v) for k, v in sorted(hist.items()))))
            if raw_dir:
                open(os.path.join(raw_dir, safe_name(amap[sid]) + ".proofread.json"), "w", encoding="utf-8").write(
                    json.dumps(levels, ensure_ascii=False, indent=1))
        elif not any("proofread levels" in x for x in f):
            clause = "La transcription de ce texte n’est pas rattachée à des pages de fac-similé relues sur Wikisource."
            controls[sid].append("PASS proofread: not scan-backed (no Page: transclusion); recorded in sourceClause")
        for x in f:
            log("FAIL " + x)
        all_fails += f
        results[sid] = {"seq": seq, "page": amap[sid], "revid": page.get("revid"), "title": title,
                        "titlePrinted": printed, "blocks": blocks, "notes": notes, "scanPages": len(pages),
                        "sourceClause": clause}

    # Texte entier, token for token
    if entier and results:
        try:
            page = fetch(entier)
            html = page.get("text")
            raw = extract(html)
            cov, _ = coverage(html, raw)
            order = [(sid, results[sid]["blocks"]) for _, sid, _ in wanted if sid in results]
            f, gaps = ctl_entier(order, entier_blocks(raw))
            if cov:
                f.append("Texte entier coverage: %s" % cov)
            log("")
            log("== Texte entier  %s  (revid %s): %d item(s)" % (entier, page.get("revid"), len(raw)))
            for g in gaps:
                log("   between texts: " + g)
        except Exception as e:  # noqa: BLE001
            order, f = [], ["Texte entier %r could not be fetched: %s" % (entier, e)]
        for x in f:
            log("FAIL entier " + x)
        all_fails += f
        for sid, _ in order:
            if not any(x.startswith(sid + ":") or "Texte entier coverage" in x for x in f):
                controls[sid].append("PASS entier: the body extracted from its own page occurs contiguously, "
                                     "in book order, token for token, in %s" % entier)

    # collation against witness B. Every B page is fetched and saved before any B control runs, so a
    # failing run still leaves the raw pages a repair needs.
    bpages = {}
    for seq, sid, pats in wanted:
        if seq == 1 or sid not in results or sid not in bmap:
            continue
        try:
            bpages[sid] = fetch(bmap[sid])
        except Exception as e:  # noqa: BLE001
            x = "collation %s: witness-B page %r could not be fetched: %s" % (sid, bmap[sid], e)
            log("FAIL " + x); all_fails.append(x)
    for seq, sid, pats in wanted:
        if sid not in bpages:
            continue
        bp = bpages[sid]
        _, _, bblocks, bnotes = structure(extract(bp.get("text")), pats, sid, witness_b=True)
        f, runs, ratio = ctl_collation(sid, results[sid]["blocks"], bblocks)
        results[sid]["collation"] = {"witnessB": bmap[sid], "revidB": bp.get("revid"), "ratio": ratio,
                                     "unmatchedRunsOver5Words": runs}
        log("")
        log("== collation %s against %s: similarity %.3f, %d unmatched run(s) > 5 words" % (sid, bmap[sid], ratio, len(runs)))
        for r in runs[:40]:
            log("   %s A%d:%d B%d:%d  A[%s]  B[%s]" % (r["op"], r["aAt"], r["aWords"], r["bAt"], r["bWords"], r["a"][:70], r["b"][:70]))
        for x in f:
            log("FAIL collation " + x)
        all_fails += f
        if not f:
            controls[sid].append("PASS collation: MORALITÉ headings A %d ≥ B %d; no stretch over 40 words in B missing "
                                 "from A; %d unmatched run(s) over 5 words listed (similarity %.3f; witness B %s)"
                                 % (sum(1 for b in results[sid]["blocks"] if b.get("heading")),
                                    sum(1 for b in bblocks if b.get("heading")), len(runs), ratio, bmap[sid]))
    if 1 in {s for s, _, _ in wanted} and "perrault-a-mademoiselle" in results:
        controls["perrault-a-mademoiselle"].append("PASS collation: not applicable (witness B does not print the dedication)")
    for seq, sid, _ in wanted:
        if seq != 1 and sid in results and not any(c.startswith("PASS collation") for c in controls[sid]) \
                and not any(("collation " + sid) in x or x.startswith("discovery: " + sid) for x in all_fails):
            x = "collation %s: no witness-B collation ran" % sid
            log("FAIL " + x); all_fails.append(x)

    passed = not all_fails and len(results) == len(wanted)
    if passed and write:
        os.makedirs(out_dir, exist_ok=True)
        stamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        me = hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
        for seq, sid, _ in wanted:
            r = results[sid]
            doc = {"id": sid, "seq": seq, "title": r["title"], "titlePrinted": r["titlePrinted"],
                   "witness": {"page": r["page"], "revid": r["revid"], "url": WIKI + r["page"].replace(" ", "_"),
                               "scanPages": r["scanPages"]},
                   "witnessB": r.get("collation", {}).get("witnessB"),
                   "blocks": r["blocks"],
                   "tokens": sum(len(WORD_RE.findall(b["text"])) for b in r["blocks"]),
                   "inventory": INVENTORY,
                   "normalisation": ["runs of whitespace, including no-break and thin spaces, collapsed to one space",
                                     "soft hyphens and zero-width characters removed",
                                     "invisible indentation spacers (visibility:hidden) removed",
                                     "the printed title (possibly over several lines) and any CONTE subtitle removed from blocks and kept in title",
                                     "a closing FIN. removed",
                                     "a prose line ending in a hyphen joined to the next line without a space",
                                     "verse continued across a page break kept in one block"],
                   "extractionNotes": r["notes"],
                   "collation": r.get("collation"),
                   "controls": ["PASS fixture: offline fixture test with injected defects"] + ["PASS discovery"] + controls[sid],
                   "archivedAt": stamp, "archiverSha256": me}
            if r.get("sourceClause"):
                doc["sourceClause"] = r["sourceClause"]
            p = os.path.join(out_dir, "perrault-%02d-source.json" % seq)
            open(p, "w", encoding="utf-8").write(json.dumps(doc, ensure_ascii=False, indent=1))
            log("wrote %s (%d blocks, %d tokens)" % (os.path.relpath(p, repo_root()), len(doc["blocks"]), doc["tokens"]))
    log("")
    log("ARCHIVE VERDICT: %s (%d control failure(s))" % ("PASS" if passed else "FAIL", len(all_fails)))
    return passed, results, all_fails


# ----------------------------------------------------------------------------- fixture
class FakeApi:
    def __init__(self, pages, allpages, quality):
        self.pages, self.allpages, self.quality = pages, allpages, quality

    def parse(self, page, props="text"):
        if page not in self.pages:
            raise RuntimeError("missing page %r" % page)
        return dict(self.pages[page], title=page)

    def query(self, params):
        if params.get("list") == "allpages":
            pre = params["apprefix"]
            return [{"allpages": [{"title": t} for t in self.allpages if t.startswith(pre)]}]
        if params.get("prop") == "proofread":
            return [{"pages": [{"title": t, "proofread": {"quality": self.quality.get(t, 4)}} for t in params["titles"].split("|")]}]
        return [{}]


def _fixture_pages():
    """Invented French in the 1697 manner, not Perrault's text."""
    ded = ["\u00c0 MADEMOISELLE", "Mademoiselle, on ne trouvera pas estrange qu'un Enfant ait pris plaisir \u00e0 composer les Contes de ce Recueil, mais on s'estonnera qu'il ait eu la hardiesse de vous les presenter. Cependant, Mademoiselle, quelque disproportion qu'il y ait entre la simplicit\u00e9 de ces Recits & les lumieres de vostre esprit, si on examine bien ces Contes, on verra que je ne suis pas si bl\u00e2mable que je le parois d'abord. Ils renferment tous une Morale tres-sens\u00e9e, & qui se d\u00e9couvre plus ou moins, selon le degr\u00e9 de penetration de ceux qui les lisent.",
           "Je suis, Mademoiselle, vostre tres-humble & tres-obe\u00efssant serviteur,", "P. DARMANCOUR."]
    tale_prose = ["Il estoit une fois un Meusnier qui avoit trois fils, & il ne leur laissa pour tout bien que son moulin, son asne & un vieil habit. Les partages furent bientost faits, ny le Notaire ny le Procureur n'y furent point appellez ; ils auroient eu bientost mang\u00e9 tout le pauvre patrimoine.",
                  "L'aisn\u00e9 eut le moulin, le second eut l'asne, & le plus jeune n'eut que le vieil habit. Ce dernier ne pouvoit se consoler d'avoir un si pauvre lot : mes freres, disoit-il, pourront gagner leur vie honnestement en se mettant ensemble ; pour moy, lors que j'auray us\u00e9 mon habit, il faudra que je meure de faim.",
                  "Le vieil habit, qui entendoit ce discours, mais qui n'en fit pas semblant, luy dit d'un air pos\u00e9 & serieux : Ne vous affligez point, mon maistre, vous n'avez qu'\u00e0 me donner un sac, & vous verrez que vous n'estes pas si mal partag\u00e9 que vous croyez."]
    moral = ["MORALIT\u00c9.", "Quelque grand que soit l'avantage\nDe jo\u00fcir d'un riche heritage\nVenant \u00e0 nous de pere en fils,\nAux jeunes gens pour l'ordinaire,\nL'industrie & le s\u00e7avoir faire\nValent mieux que des biens acquis."]

    def html(title, paras, moral_lines, pagenum=True, real=False):
        """real=True reproduces markup met on the live 1697 pages (2026-09-11): a title over several
        centred divs, a paragraph as bare text with no <p>, invisible indentation spacers, and a
        MORALITE set inside a layout table whose verse continues across a page break."""
        h = ['<div class="mw-parser-output"><div id="headertemplate" class="ws-noexport">Header noise</div>']
        if real:
            first, _, rest = title.partition(" OU ")
            h.append('<p><span><span class="pagenum ws-pagenum" id="2"></span></span></p><figure><img src="x.png"/></figure><p><br/></p>')
            h.append('<div style="text-align:center; font-size:120%%;">%s</div><div style="text-align:center;">OU %s</div><p><br/></p>' % (first, rest))
        else:
            h.append('<div style="text-align:center"><span style="font-size:120%%">%s</span></div>' % title)
        for k, p in enumerate(paras):
            pn = '<span class="pagenum ws-pagenum" id="%d">%d</span>' % (k + 3, k + 3) if pagenum else ""
            if real and k == 0:
                h.append("\n%s%s\n" % (p.replace("&", "&amp;").replace(" ", " <span>" + pn + "</span>", 1), ""))
            else:
                h.append("<p>%s%s</p>" % (pn, p.replace("&", "&amp;")))
        if moral_lines and real:
            lines = moral_lines[1].replace("&", "&amp;").split("\n")
            spacer = '<span style="visibility:hidden; color:transparent;"><i>Qu</i></span>'
            h.append('<p><br/></p><center><table><tbody><tr><td align="center"><p><br/><span style="font-size:120%%">%s</span><br/> <br/>' % moral_lines[0])
            h.append("<br/>\n".join("<i>%s</i>" % ln for ln in lines[:3]))
            h.append('<br/>&#32;<span><span class="pagenum ws-pagenum" id="9"></span></span>')
            h.append("<br/>\n".join(spacer + "<i>%s</i>" % ln for ln in lines[3:]))
            h.append("</p></td></tr></tbody></table></center>")
        elif moral_lines:
            h.append('<div style="text-align:center">%s</div>' % moral_lines[0])
            h.append('<div class="poem"><p>%s</p></div>' % "<br />\n".join(moral_lines[1].replace("&", "&amp;").split("\n")))
        h.append("</div>")
        return "".join(h)

    A_DED = A_ROOT + "/\u00c0 Mademoiselle"
    A_TALE = A_ROOT + "/Le Maistre Chat, ou le Chat bott\u00e9"
    A_ENT = A_ROOT + "/Texte entier"
    B_TALE = B_ROOT + "/Le Ma\u00eetre Chat ou le Chat bott\u00e9"
    ded_html = html(ded[0], ded[1:], None)
    tale_html = html("LE MAISTRE CHAT, OU LE CHAT BOTT\u00c9.", tale_prose, moral, real=True)
    ent_html = '<div class="mw-parser-output"><p>HISTOIRES OU CONTES DU TEMPS PASS\u00c9.</p>' + \
        ded_html.replace('<div class="mw-parser-output">', "<div>") + tale_html.replace('<div class="mw-parser-output">', "<div>") + "</div>"
    b_prose = [p.replace("estoit", "\u00e9tait").replace("avoit", "avait").replace("&", "et") for p in tale_prose]
    b_html = html("LE MA\u00ceTRE CHAT OU LE CHAT BOTT\u00c9", b_prose, ["MORALIT\u00c9.", moral[1].replace("&", "et")], pagenum=False)
    tmpl = [{"ns": 104, "title": "Page:Perrault - Histoires 1697.djvu/%d" % n} for n in (3, 4, 5)]
    pages = {
        A_ROOT: {"text": "", "links": [{"ns": 0, "title": A_DED}, {"ns": 0, "title": A_TALE}, {"ns": 0, "title": A_ENT}]},
        A_DED: {"text": ded_html, "wikitext": "", "revid": 1, "templates": tmpl},
        A_TALE: {"text": tale_html, "wikitext": "", "revid": 2, "templates": tmpl},
        A_ENT: {"text": ent_html, "wikitext": "", "revid": 3, "templates": []},
        B_ROOT: {"text": "", "links": [{"ns": 0, "title": B_TALE}]},
        B_TALE: {"text": b_html, "wikitext": "", "revid": 4, "templates": []},
    }
    allpages = [A_DED, A_TALE, A_ENT, B_TALE, "Histoires ou Contes du temps pass\u00e9 (1697)/Le Maistre Chat"]
    return pages, allpages, {"A_TALE": A_TALE, "A_ENT": A_ENT, "B_TALE": B_TALE, "A_DED": A_DED}, tale_prose


def fixture_test():

    subset = [(1, "perrault-a-mademoiselle", None), (5, "maitre-chat", None)]
    global TEXTS
    saved = TEXTS
    saved_log = list(LOG)
    TEXTS = [t for t in saved if t[1] in {"perrault-a-mademoiselle", "maitre-chat"}]
    ok = True
    try:
        def attempt(mutate=None, quality=None):
            pages, allpages, names, prose = _fixture_pages()
            if mutate:
                mutate(pages, allpages, names, prose)
            LOG.clear()
            api = FakeApi(pages, allpages, quality or {})
            QUIET[0] = True
            try:
                return run(api, None, None, texts=subset, write=False)
            finally:
                QUIET[0] = False

        passed, res, fails = attempt()
        tale = res.get("maitre-chat", {})
        shape_ok = (passed and tale.get("title") == "LE MAISTRE CHAT, OU LE CHAT BOTT\u00c9"
                    and [b.get("heading", False) for b in tale["blocks"]] == [False, False, False, True, False]
                    and tale["blocks"][4].get("v") and tale["blocks"][4]["text"].count("\n") == 5
                    and tale["blocks"][0]["text"].startswith("Il estoit une fois")
                    and "Header noise" not in json.dumps(res, ensure_ascii=False)
                    and not re.search(r"\b3Il\b|^\d", tale["blocks"][0]["text"])
                    and res["perrault-a-mademoiselle"]["blocks"][-1]["text"] == "P. DARMANCOUR."
                    and "QuAux" not in tale["blocks"][4]["text"] and "Aux jeunes gens" in tale["blocks"][4]["text"])
        print("fixture control: %s" % ("PASS" if shape_ok else "FAIL"))
        if not shape_ok:
            print("\n".join(LOG[-40:])); print(fails)
        ok &= shape_ok

        def drop_word_in_entier(pages, allpages, n, prose):
            pages[n["A_ENT"]]["text"] = pages[n["A_ENT"]]["text"].replace("trois fils", "fils", 1)

        def low_quality(pages, allpages, n, prose):
            pass

        def bad_char(pages, allpages, n, prose):
            for k in (n["A_TALE"], n["A_ENT"]):
                pages[k]["text"] = pages[k]["text"].replace("son moulin", "son mo\u1ebdulin")

        def b_extra_moral(pages, allpages, n, prose):
            pages[n["B_TALE"]]["text"] = pages[n["B_TALE"]]["text"].replace(
                "</div></div>", "</div><div>AUTRE MORALIT\u00c9.</div><div class=\"poem\"><p>Si le fils d'un Meunier<br />trouve fortune.</p></div></div>")

        def a_missing_run(pages, allpages, n, prose):
            extra = (" Il fit tant de choses qu'on ne s\u00e7auroit les conter toutes, car il alloit par les champs & par les bois, "
                     "prenant des lapins, des perdrix & des cailles qu'il portoit au Roy, qui en estoit fort content, "
                     "& qui luy donnoit chaque fois quelque piece d'argent pour sa peine & pour son soin.")
            pages[n["B_TALE"]]["text"] = pages[n["B_TALE"]]["text"].replace("mal partag\u00e9 que vous croyez.", "mal partag\u00e9 que vous croyez." + extra)

        def ambiguous(pages, allpages, n, prose):
            dup = A_ROOT + "/Le Chat bott\u00e9"
            allpages.append(dup)
            pages[dup] = pages[n["A_TALE"]]

        def title_missing(pages, allpages, n, prose):
            t = pages[n["A_TALE"]]["text"].replace(">LE MAISTRE CHAT,<", "><").replace(">OU LE CHAT BOTT\u00c9.<", "><")
            pages[n["A_TALE"]]["text"] = t

        def walker_drops_a_block(pages, allpages, n, prose):
            pass   # the defect is injected into extract() itself, below

        def no_moral_heading(pages, allpages, n, prose):
            for k in (n["A_TALE"], n["A_ENT"]):
                pages[k]["text"] = pages[k]["text"].replace(">MORALIT\u00c9.<", "><")

        def b_only_a_red_link(pages, allpages, n, prose):
            allpages.remove(n["B_TALE"])

        cases = [
            ("Texte entier missing a word", drop_word_in_entier, None, "entier"),
            ("scan page below proofread", low_quality, {"Page:Perrault - Histoires 1697.djvu/4": 1}, "below 'proofread'"),
            ("character outside inventory", bad_char, None, "outside the declared inventory"),
            ("B has an AUTRE MORALIT\u00c9 A lacks", b_extra_moral, None, "MORALIT\u00c9 heading"),
            ("A missing a 40+ word stretch", a_missing_run, None, "missing from witness A"),
            ("two pages match one text", ambiguous, None, "discovery"),
            ("no printed title", title_missing, None, "no printed title"),
            ("extractor loses a paragraph", walker_drops_a_block, None, "coverage"),
            ("MORALIT\u00c9 heading missing in A", no_moral_heading, None, "no MORALIT\u00c9 heading"),
            ("B page is only a red link", b_only_a_red_link, None, "no existing witness-B page"),
        ]
        for name, fn, q, expect in cases:
            real_extract = globals()["extract"]
            if fn is walker_drops_a_block:
                globals()["extract"] = lambda h, _d=None: real_extract(h, _drop_hook=lambda lines: any("L'aisn" in x for x in lines))
            try:
                passed, _, fails = attempt(fn, q)
            finally:
                globals()["extract"] = real_extract
            caught = (not passed) and any(expect in x for x in fails)
            print("  %-34s %s" % (name, "caught" if caught else "MISSED  %s" % fails))
            ok &= caught
    finally:
        TEXTS = saved
        LOG[:] = saved_log
    print("FIXTURE TEST: %s" % ("PASS" if ok else "FAIL"))
    return ok


# ----------------------------------------------------------------------------- replay
class RawApi:
    """Replays a committed raw archive (sources/perrault-raw/ plus the discovery lists in
    sources/perrault-archive-log.txt) with no network, so an extractor repair can be proved offline
    against the real pages before it is landed. Diagnostic only: a replay never writes sources."""

    def __init__(self, raw_dir, log_path):
        self.raw_dir = raw_dir
        self.listed = []
        for line in open(log_path, encoding="utf-8"):
            m = re.match(r"^   [AB]  (.+)$", line.rstrip("\n"))
            if m:
                self.listed.append(m.group(1))
        self.levels = {}
        for f in os.listdir(raw_dir):
            if f.endswith(".proofread.json"):
                self.levels.update(json.load(open(os.path.join(raw_dir, f), encoding="utf-8")))

    def parse(self, page, props=None):
        base = os.path.join(self.raw_dir, safe_name(page))
        if not os.path.exists(base + ".html"):
            raise RuntimeError("not in the raw archive: %r" % page)
        meta = json.load(open(base + ".meta.json", encoding="utf-8")) if os.path.exists(base + ".meta.json") else {}
        return {"title": page, "text": open(base + ".html", encoding="utf-8").read(),
                "wikitext": open(base + ".wikitext", encoding="utf-8").read() if os.path.exists(base + ".wikitext") else "",
                "revid": meta.get("revid", "replay"), "templates": meta.get("templates") or []}

    def query(self, params):
        if params.get("list") == "allpages":
            pre = params["apprefix"]
            return [{"allpages": [{"title": t} for t in self.listed if t.startswith(pre)]}]
        if params.get("prop") == "proofread":
            return [{"pages": [{"title": t, "proofread": {"quality": self.levels.get(t)}} for t in params["titles"].split("|")]}]
        return [{}]


# ----------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fixture", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--replay", metavar="RAW_DIR", help="offline replay of a committed raw archive (diagnostic, writes nothing)")
    a = ap.parse_args()
    if a.fixture:
        sys.exit(0 if fixture_test() else 1)
    if a.replay:
        if not fixture_test():
            sys.exit(1)
        log_path = os.path.join(os.path.dirname(os.path.abspath(a.replay)), "perrault-archive-log.txt")
        LOG.clear()
        passed, _, fails = run(RawApi(a.replay, log_path), None, None, write=False)
        print("REPLAY (diagnostic only, nothing written): %d failure(s)" % len(fails))
        sys.exit(0 if passed else 1)
    root = repo_root()
    out_dir = os.path.join(root, "sources")
    log_path = os.path.join(out_dir, "perrault-archive-log.txt")
    existing = [os.path.join(out_dir, "perrault-%02d-source.json" % s) for s, _, _ in TEXTS]
    if not a.force and all(os.path.exists(p) for p in existing):
        good = all(any(c.startswith("PASS") for c in json.load(open(p, encoding="utf-8")).get("controls", [])) for p in existing)
        if good:
            print("all nine Perrault sources are archived with passing controls; nothing to do")
            return
    os.makedirs(out_dir, exist_ok=True)
    LOG.clear()
    log("archive_perrault.py run at %s" % time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
    log("archiver sha256 %s" % hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest())
    ok = fixture_test()
    LOG.insert(2, "fixture test: %s" % ("PASS" if ok else "FAIL"))
    passed = False
    if ok:
        try:
            passed, _, _ = run(Api(), out_dir, os.path.join(out_dir, "perrault-raw"))
        except Exception as e:  # noqa: BLE001
            import traceback
            log("EXCEPTION: %s" % e)
            log(traceback.format_exc())
            log("ARCHIVE VERDICT: FAIL (exception)")
    else:
        log("ARCHIVE VERDICT: FAIL (fixture test)")
    open(log_path, "w", encoding="utf-8").write("\n".join(LOG) + "\n")
    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
