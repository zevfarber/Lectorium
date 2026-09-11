#!/usr/bin/env python3
"""tools_french.py -- the gates for Perrault's Histoires ou contes du temps passe (1697).

Written 2026-09-10 (Perrault infrastructure firing). Adapted in spirit from tools_latin.py
and tools_grimm.py; lives in the repository so that it reaches every firing byte-exact.

    python3 tools_french.py selftest
    python3 tools_french.py gate --root <tree> [--ids id1,id2 | --all]
                                 [--baseline-glossary <json>] [--patch <json> ...]
                                 [--no-lexicon] [--json <out>]

<tree> is repository-shaped: stories.json, reader.html, index.html, perrault-glossary.json,
<id>.json story files, sources/perrault-NN-source.json and .github/tools/perrault-speech-map.json.

Gates (FAIL is fatal, WARN is reported):
  parse         JSON parses; field order and field values per conventions section 7
  concat        the units' `t`, whitespace aside, equal the archived source character for character
  lineation     every verse line break is a `\\n` or a unit boundary; no unit splits a line
  paragraphs    `p` exactly on prose/heading block starts, `v` on verse units and never with `p`
  inventory     every character of `t` is in the source's declared inventory
  coverage      100 % glossary coverage under the deployed reader's own WORD_RE and wordKey, run in
                node, glossary merged as Object.assign({}, shared, inline)
  homograph     glossary patches never silently contradict an existing key or each other
  density       notes on >= 75 % of units (repeat MORALITE headings, which take no note, excluded)
  say-parity    `say` has the tokens of `t` in order, each identical or mapped, plus declared symbol
                readings; nothing else differs but verse-line pause commas; `say` exists iff needed
  speech-lexicon every modern form in the speech map is a hunspell fr_FR word or a declared proper noun
  scan          reader-facing fields: no publisher framing, no undefined/NaN/[object Object],
                guillemets without inner spaces, no ' used as an opening quote, no straight "
  manifest      entries resolve, titles agree, glossaryFile exists, seq present, index.html == reader.html,
                stories.json re-serialises byte-exact
  regex-parity  align_wordref.py's Python WORD_RE tokenizes every unit exactly as the reader does
"""
import json, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
WORK = "Histoires ou contes du temps pass\u00e9"
WORK_EN = "Tales of Times Past (Perrault)"
GLOSSARY_FILE = "perrault-glossary.json"
DENSITY_FLOOR = 0.75

TEXTS = [  # seq, id, titleEn
    (1, "perrault-a-mademoiselle", "To Mademoiselle"),
    (2, "belle-au-bois-dormant", "The Sleeping Beauty in the Wood"),
    (3, "petit-chaperon-rouge", "Little Red Riding Hood"),
    (4, "barbe-bleue", "Bluebeard"),
    (5, "maitre-chat", "The Master Cat, or Puss in Boots"),
    (6, "les-fees", "The Fairies"),
    (7, "cendrillon", "Cinderella, or the Little Glass Slipper"),
    (8, "riquet-a-la-houppe", "Riquet with the Tuft"),
    (9, "petit-poucet", "Little Thumb"),
]
BY_ID = {i: (seq, t) for seq, i, t in TEXTS}

STORY_ORDER = ["id", "title", "titleEn", "language", "langCode", "work", "workEn", "part", "source",
               "about", "advisory", "wordClips", "glossaryFile", "glossary", "sentences"]
STORY_REQUIRED = [k for k in STORY_ORDER if k not in ("advisory", "glossary")]
SENT_ORDER = ["p", "v", "t", "say", "l", "i", "n"]
MANIFEST_ORDER = ["id", "title", "titleEn", "language", "work", "workEn", "part", "file", "seq"]

SOURCE_HEAD = ("Charles Perrault, \u00ab {title} \u00bb, dans Histoires ou contes du temps pass\u00e9. Avec des "
               "Moralitez (Paris, Claude Barbin, 1697) ; texte de l\u2019\u00e9dition originale d\u2019apr\u00e8s la "
               "transcription de Wikisource, orthographe de 1697 conserv\u00e9e.")
SOURCE_TAIL = ("Prononciation : fran\u00e7ais standard moderne ; les graphies de 1697 sont lues selon "
               "l\u2019usage moderne.")

HEADING_RE = re.compile(r"^(AUTRE\s+)?MORALIT[E\u00c9]S?\s*\.?$", re.I)

FATAL_SCAN = [
    (re.compile(r"\bundefined\b"), "undefined"),
    (re.compile(r"\bNaN\b"), "NaN"),
    (re.compile(r"\[object Object\]"), "[object Object]"),
    (re.compile(r"\b(Zev|Farber)\b"), "publisher's name"),
    (re.compile(r"\bpublisher\b", re.I), "publisher framing"),
    (re.compile(r"\bJewish\b|\bJew\b", re.I), "publisher framing (content-advisory input/output rule)"),
    (re.compile(r"\u00ab[\s\u00a0\u202f]|[\s\u00a0\u202f]\u00bb"), "guillemet with an inner space"),
    (re.compile(r"(?:^|[\s(\[\u2014\u2013])\u2019(?=\w)"), "\u2019 used as an opening quote (use \u2018)"),
    (re.compile(r'"'), 'straight double quote in the apparatus'),
]
TONE_WARN = re.compile(r"\b(learn(?:ing|s|ed)?|stud(?:y|ying|ied)|drill(?:s|ing)?|quiz(?:zes)?|practi[cs]e)\b", re.I)


# ----------------------------------------------------------------------------- reader regex in node
def reader_js_prelude(reader_path):
    src = open(reader_path, encoding="utf-8").read()
    a = src.index("const WORD_CLASS")
    b = src.index("function wordKey(")
    b = src.index("\n", b)
    return src[a:b + 1]


NODE_PROG = r"""
const fs = require('fs'); const vm = require('vm');
const [prelude, inp] = [fs.readFileSync(process.argv[2], 'utf8'), JSON.parse(fs.readFileSync(process.argv[3], 'utf8'))];
const ctx = {}; vm.createContext(ctx);
vm.runInContext(prelude + '\n;this.WORD_RE = WORD_RE; this.wordKey = wordKey;', ctx);
const toks = s => (s.match(new RegExp(ctx.WORD_RE.source, 'g')) || []);
const out = inp.map(u => {
  const tt = toks(u.t);
  const o = { t: tt, keys: tt.map(w => ctx.wordKey(w)) };
  if (typeof u.say === 'string') o.say = toks(u.say);
  if (u.gloss) { const g = Object.assign({}, u.gloss.shared, u.gloss.inline || {}); o.missing = o.keys.filter(k => g[k] === undefined); }
  return o;
});
process.stdout.write(JSON.stringify(out));
"""


def node_tokens(reader_path, units, gloss=None):
    """Tokenize with the deployed reader's WORD_RE (and check coverage when gloss is given)."""
    tmp = tempfile.mkdtemp()
    try:
        pre = os.path.join(tmp, "prelude.js"); open(pre, "w", encoding="utf-8").write(reader_js_prelude(reader_path))
        prog = os.path.join(tmp, "prog.js"); open(prog, "w", encoding="utf-8").write(NODE_PROG)
        payload = []
        for u in units:
            d = {"t": u["t"]}
            if isinstance(u.get("say"), str):
                d["say"] = u["say"]
            if gloss is not None:
                d["gloss"] = gloss
            payload.append(d)
        inp = os.path.join(tmp, "in.json"); json.dump(payload, open(inp, "w", encoding="utf-8"), ensure_ascii=False)
        r = subprocess.run(["node", prog, pre, inp], capture_output=True, text=True, check=True)
        return json.loads(r.stdout)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


# ----------------------------------------------------------------------------- speech map / say
def case_like(tok, val):
    if len(tok) > 1 and tok.isupper():
        return val.upper()
    if tok[:1].isupper():
        return val[:1].upper() + val[1:]
    return val


def expected_spoken(t, smap, symbols, word_pat):
    """[(kind, printed, spoken)] for `t`: kind 'w' (word) or 'sym' (declared symbol)."""
    if symbols:
        pat = re.compile(word_pat + "|[" + "".join(re.escape(c) for c in symbols) + "]")
    else:
        pat = re.compile(word_pat)
    out = []
    for m in pat.finditer(t):
        g = m.group(0)
        if g in symbols:
            out.append(("sym", g, symbols[g]))
        else:
            v = smap.get(g.lower())
            out.append(("w", g, case_like(g, v) if v else g))
    return out


def build_say(t, verse, smap, symbols, word_pat):
    """The one deterministic `say` builder (assemble_perrault.py imports this)."""
    word_re = re.compile(word_pat)
    sym_re = "|[" + "".join(re.escape(c) for c in symbols) + "]" if symbols else ""
    pat = re.compile(word_pat + sym_re)

    def sub(m):
        g = m.group(0)
        if g in symbols:
            return symbols[g]
        v = smap.get(g.lower())
        return case_like(g, v) if v else g
    say = pat.sub(sub, t)
    if verse:
        lines = say.split("\n")
        lines = [ln + "," if word_re.search(ln) and re.search("[" + WORD_CLASS_PY + "]$", ln) else ln
                 for ln in lines]
        say = "\n".join(lines)
    return None if say == t else say


# ----------------------------------------------------------------------------- the tree
def _py_word():
    sys.path.insert(0, os.path.join(HERE, "..", "scripts"))
    import align_wordref as AW
    return AW


AW = _py_word()
WORD_PAT = AW.WORD_PAT
WORD_CLASS_PY = AW.WORD_CLASS


class Report:
    def __init__(self):
        self.rows = []

    def fail(self, gate, where, msg):
        self.rows.append(("FAIL", gate, where, msg))

    def warn(self, gate, where, msg):
        self.rows.append(("WARN", gate, where, msg))

    def ok(self, gate, where, msg=""):
        self.rows.append(("PASS", gate, where, msg))

    def fails(self, gate=None):
        return [r for r in self.rows if r[0] == "FAIL" and (gate is None or r[1] == gate)]

    def text(self):
        return "\n".join("%s %-14s %-26s %s" % r for r in self.rows)


def load_json_bytes(path):
    b = open(path, "rb").read()
    return b, json.loads(b.decode("utf-8"))


def canonical_t(t):
    return "\n".join(re.sub(r"[ \t\u00a0\u202f]+", " ", ln).strip() for ln in t.split("\n"))


def stream(pieces):
    """pieces: [str] -> (S non-space chars, ws positions, nl positions, start positions)."""
    S, ws, nl, starts = [], set(), set(), []
    for p in pieces:
        starts.append(len(S))
        for ch in p:
            if ch == "\n":
                nl.add(len(S))
            elif ch.isspace():
                ws.add(len(S))
            else:
                S.append(ch)
    return "".join(S), ws, nl, starts


def gate_text_structure(rep, sid, story, source):
    blocks = source["blocks"]
    units = story["sentences"]
    for k, u in enumerate(units):
        if canonical_t(u["t"]) != u["t"]:
            rep.fail("concat", "%s#%d" % (sid, k), "t is not whitespace-canonical")
    S, sws, snl, bstarts = stream([b["text"] for b in blocks])
    U, uws, unl, ustarts = stream([u["t"] for u in units])
    if S != U:
        i = next((j for j in range(min(len(S), len(U))) if S[j] != U[j]), min(len(S), len(U)))
        rep.fail("concat", sid, "differs from source at char %d: source \u2026%s\u2026 units \u2026%s\u2026"
                 % (i, S[max(0, i - 20):i + 20], U[max(0, i - 20):i + 20]))
        return
    rep.ok("concat", sid, "%d characters" % len(S))
    ustart_set = set(ustarts)
    bstart_set = set(bstarts)
    # which block each position belongs to
    bounds = bstarts + [len(S)]

    def block_of(pos):
        lo, hi = 0, len(blocks) - 1
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if bounds[mid] <= pos:
                lo = mid
            else:
                hi = mid - 1
        return lo
    bad = 0
    for pos in sws:
        if pos not in uws and pos not in ustart_set:
            bad += 1; rep.fail("concat", "%s@%d" % (sid, pos), "a space in the source is missing in t")
    for pos in uws:
        if pos not in sws:
            bad += 1; rep.fail("concat", "%s@%d" % (sid, pos), "a space in t is not in the source")
    for pos in unl:
        if pos not in snl:
            bad += 1; rep.fail("lineation", "%s@%d" % (sid, pos), "a line break in t is not a verse line break in the source")
    for pos in snl:
        if pos not in unl and pos not in ustart_set:
            bad += 1; rep.fail("lineation", "%s@%d" % (sid, pos), "a source verse line break is lost")
    for b in bstarts:
        if b not in ustart_set:
            bad += 1; rep.fail("paragraphs", "%s@%d" % (sid, b), "a source block does not start a unit")
    for k, pos in enumerate(ustarts):
        u = units[k]
        blk = blocks[block_of(pos)] if pos < len(S) else blocks[-1]
        verse = bool(blk.get("v"))
        where = "%s#%d" % (sid, k)
        if pos in bstart_set:
            if verse:
                if not u.get("v") or u.get("p"):
                    bad += 1; rep.fail("paragraphs", where, "a verse block must start a unit with v and without p")
            elif not u.get("p") or u.get("v"):
                bad += 1; rep.fail("paragraphs", where, "a prose or heading block must start a unit with p")
        else:
            if u.get("p"):
                bad += 1; rep.fail("paragraphs", where, "p on a unit that does not start a source block")
            if verse:
                if not u.get("v"):
                    bad += 1; rep.fail("paragraphs", where, "a unit inside a verse block lacks v")
                if pos not in snl:
                    bad += 1; rep.fail("lineation", where, "a verse unit boundary splits a line")
            else:
                if u.get("v"):
                    bad += 1; rep.fail("paragraphs", where, "v on a prose unit")
                if pos not in sws:
                    bad += 1; rep.fail("concat", where, "a unit boundary falls inside a word")
        if u.get("p") and u.get("v"):
            bad += 1; rep.fail("paragraphs", where, "a unit carries both p and v")
        if not verse and "\n" in u["t"]:
            bad += 1; rep.fail("lineation", where, "a line break inside a prose unit")
    if not bad:
        rep.ok("lineation", sid); rep.ok("paragraphs", sid, "%d blocks, %d units" % (len(blocks), len(units)))
    inv = set(source.get("inventory", ""))
    extra = sorted({c for u in units for c in u["t"] if c not in inv and c not in " \n"})
    if not inv:
        rep.fail("inventory", sid, "source declares no inventory")
    elif extra:
        rep.fail("inventory", sid, "characters outside the declared inventory: %s"
                 % ", ".join("%r U+%04X" % (c, ord(c)) for c in extra))
    else:
        rep.ok("inventory", sid)


def gate_fields(rep, sid, story, source):
    keys = list(story.keys())
    order = [k for k in STORY_ORDER if k in story]
    unknown = [k for k in keys if k not in STORY_ORDER]
    if unknown:
        rep.fail("parse", sid, "unknown story fields: %s" % unknown)
    if keys != order:
        rep.fail("parse", sid, "story field order %s, expected %s" % (keys, order))
    for k in STORY_REQUIRED:
        if k not in story:
            rep.fail("parse", sid, "missing field %s" % k)
    seq, title_en = BY_ID.get(sid, (None, None))
    want = {"language": "French", "langCode": "fr-FR", "work": WORK, "workEn": WORK_EN,
            "wordClips": True, "glossaryFile": GLOSSARY_FILE, "id": sid}
    if seq is None:
        rep.fail("parse", sid, "id is not one of the nine planned ids")
    else:
        want["titleEn"] = title_en
        want["part"] = title_en
    for k, v in want.items():
        if story.get(k) != v:
            rep.fail("parse", sid, "%s is %r, expected %r" % (k, story.get(k), v))
    if story.get("title") != source.get("title"):
        rep.fail("parse", sid, "title %r differs from the source's printed title %r"
                 % (story.get("title"), source.get("title")))
    src = story.get("source", "")
    head = SOURCE_HEAD.format(title=source.get("title"))
    if not (src.startswith(head) and src.endswith(SOURCE_TAIL)):
        rep.fail("parse", sid, "source does not follow the conventions template")
    if not isinstance(story.get("about"), str) or len(story.get("about", "")) < 40:
        rep.fail("parse", sid, "about missing or too short")
    adv = story.get("advisory")
    if adv is not None and not (isinstance(adv, str) and adv.strip()) and not (
            isinstance(adv, dict) and set(adv) == {"lede", "more"} and all(isinstance(x, str) and x.strip() for x in adv.values())):
        rep.fail("parse", sid, "advisory must be a sentence or {lede, more}")
    if "glossary" in story and not (isinstance(story["glossary"], dict) and story["glossary"]):
        rep.fail("parse", sid, "an inline glossary, when present, holds homograph overrides and is non-empty")
    if not isinstance(story.get("sentences"), list) or not story["sentences"]:
        rep.fail("parse", sid, "no sentences"); return
    for k, u in enumerate(story["sentences"]):
        where = "%s#%d" % (sid, k)
        ks = list(u.keys())
        if [x for x in ks if x not in SENT_ORDER]:
            rep.fail("parse", where, "unknown sentence keys %s" % [x for x in ks if x not in SENT_ORDER])
        if ks != [x for x in SENT_ORDER if x in u]:
            rep.fail("parse", where, "sentence key order %s" % ks)
        for f in ("t", "l"):
            if not isinstance(u.get(f), str) or not u[f].strip():
                rep.fail("parse", where, "%s missing or empty" % f)
        for f in ("say", "i", "n"):
            if f in u and not (isinstance(u[f], str) and u[f].strip()):
                rep.fail("parse", where, "%s present but empty" % f)
        for f in ("p", "v"):
            if f in u and u[f] is not True:
                rep.fail("parse", where, "%s must be true when present" % f)
        if "i" in u and u.get("i") == u.get("l"):
            rep.fail("parse", where, "i identical to l (omit i)")
        if isinstance(u.get("l"), str) and isinstance(u.get("i"), str) and u.get("v"):
            if u["l"].count("\n") != u["t"].count("\n") or u["i"].count("\n") != u["t"].count("\n"):
                rep.fail("parse", where, "verse l/i must keep the line structure of t")
        elif u.get("v") and isinstance(u.get("l"), str) and u["l"].count("\n") != u["t"].count("\n"):
            rep.fail("parse", where, "verse l must keep the line structure of t")


def is_heading(u):
    return bool(HEADING_RE.match(u["t"].strip()))


def gate_density(rep, sid, story):
    units = story["sentences"]
    seen_heading = False
    denom = noted = 0
    for u in units:
        if is_heading(u):
            if seen_heading:
                continue
            seen_heading = True
        denom += 1
        if isinstance(u.get("n"), str) and u["n"].strip():
            noted += 1
    d = noted / float(denom or 1)
    msg = "%.1f %% (%d of %d units)" % (100 * d, noted, denom)
    (rep.ok if d >= DENSITY_FLOOR else rep.fail)("density", sid, msg)
    return d


def gate_say(rep, sid, story, smap_doc, node_out):
    smap = {k.lower(): v for k, v in (smap_doc.get("map") or {}).items()}
    symbols = smap_doc.get("symbols") or {}
    bad = 0
    for k, (u, no) in enumerate(zip(story["sentences"], node_out)):
        where = "%s#%d" % (sid, k)
        exp = expected_spoken(u["t"], smap, symbols, WORD_PAT)
        exp_tokens = [x[2] for x in exp]
        needs_comma = bool(u.get("v")) and any(
            re.search("[" + WORD_CLASS_PY + "]$", ln) for ln in u["t"].split("\n"))
        needed = exp_tokens != [x[1] for x in exp if x[0] == "w"] or needs_comma
        say = u.get("say")
        if say is None:
            if needed:
                bad += 1; rep.fail("say-parity", where, "say is required (archaic spelling, symbol or verse pause) but absent")
            continue
        if not needed:
            bad += 1; rep.fail("say-parity", where, "say present on a unit that needs none")
        got = no.get("say", [])
        if len(got) != len(exp_tokens):
            bad += 1; rep.fail("say-parity", where, "say has %d tokens, t implies %d" % (len(got), len(exp_tokens)))
            continue
        for j, (g, e) in enumerate(zip(got, exp_tokens)):
            if g != e:
                bad += 1; rep.fail("say-parity", where, "token %d: say has %r, the map gives %r" % (j, g, e))
                break
        # nothing but tokens and pause commas may differ
        word_re = re.compile(WORD_PAT)
        sym_re = re.compile("[" + "".join(re.escape(c) for c in symbols) + "]") if symbols else None
        tsk = word_re.sub("\x00", u["t"])
        if sym_re:
            tsk = sym_re.sub("\x00", tsk)
        ssk = word_re.sub("\x00", say)
        norm = lambda x: re.sub("\x00,(?=\n|$)", "\x00", x)
        if norm(tsk) != norm(ssk) or ssk.count(",") < tsk.count(","):
            bad += 1; rep.fail("say-parity", where, "say differs from t outside the tokens")
        if needs_comma:
            for ln_t, ln_s in zip(u["t"].split("\n"), say.split("\n")):
                if re.search("[" + WORD_CLASS_PY + "]$", ln_t) and not ln_s.endswith(","):
                    bad += 1; rep.fail("say-parity", where, "an unpunctuated verse line has no pause comma in say")
                    break
    if not bad:
        rep.ok("say-parity", sid, "%d units with say" % sum(1 for u in story["sentences"] if "say" in u))


def gate_map_shape(rep, smap_doc):
    ok = True
    for k, v in (smap_doc.get("map") or {}).items():
        if k != k.lower() or len(AW.WORD_RE.findall(k)) != 1 or AW.WORD_RE.fullmatch(k) is None:
            ok = False; rep.fail("say-parity", "speech-map", "key %r is not one lowercase WORD_RE token" % k)
        if len(AW.WORD_RE.findall(v)) != 1 or AW.WORD_RE.fullmatch(v) is None:
            ok = False; rep.fail("say-parity", "speech-map", "value %r for %r is not one WORD_RE token" % (v, k))
    for c, v in (smap_doc.get("symbols") or {}).items():
        if AW.WORD_RE.search(c) or AW.WORD_RE.fullmatch(v) is None:
            ok = False; rep.fail("say-parity", "speech-map", "symbol %r -> %r malformed" % (c, v))
    if ok:
        rep.ok("say-parity", "speech-map", "%d entries, %d symbols" % (len(smap_doc.get("map") or {}), len(smap_doc.get("symbols") or {})))


def gate_lexicon(rep, smap_doc, lexicon=True):
    values = sorted(set((smap_doc.get("map") or {}).values()) | set((smap_doc.get("symbols") or {}).values()))
    if not lexicon:
        rep.warn("speech-lexicon", "speech-map", "skipped by --no-lexicon (%d forms unchecked)" % len(values))
        return
    if not shutil.which("hunspell") or not os.path.exists("/usr/share/hunspell/fr_FR.dic"):
        rep.fail("speech-lexicon", "speech-map", "hunspell with fr_FR is not installed (apt-get install hunspell hunspell-fr)")
        return
    if not values:
        rep.ok("speech-lexicon", "speech-map", "no modern forms yet"); return
    proper = {w.lower() for w in smap_doc.get("properNouns") or []}
    r = subprocess.run(["hunspell", "-d", "fr_FR", "-l"], input="\n".join(values), capture_output=True, text=True)
    bad = sorted({w for w in r.stdout.split() if w.lower() not in proper})
    # hunspell splits at apostrophes and hyphens itself; a value is bad if any piece is listed
    if bad:
        rep.fail("speech-lexicon", "speech-map", "not French words or declared proper nouns: %s" % ", ".join(bad))
    else:
        rep.ok("speech-lexicon", "speech-map", "%d modern forms" % len(values))


def gate_scan(rep, sid, story):
    fields = [("about", story.get("about", ""))]
    adv = story.get("advisory")
    if isinstance(adv, str):
        fields.append(("advisory", adv))
    elif isinstance(adv, dict):
        fields += [("advisory.lede", adv.get("lede", "")), ("advisory.more", adv.get("more", ""))]
    fields.append(("source", story.get("source", "")))
    for k, u in enumerate(story["sentences"]):
        for f in ("l", "i", "n"):
            if isinstance(u.get(f), str):
                fields.append(("%s#%d.%s" % ("", k, f), u[f]))
    bad = 0
    for name, text in fields:
        for rx, label in FATAL_SCAN:
            if name == "source" and label in ("guillemet with an inner space",):
                continue   # the source statement is French typography, not apparatus
            if rx.search(text or ""):
                bad += 1; rep.fail("scan", sid + name, label)
        if name.endswith(".n") or name == "about":
            m = TONE_WARN.search(text or "")
            if m:
                rep.warn("scan", sid + name, "classroom word %r" % m.group(0))
    if not bad:
        rep.ok("scan", sid, "advisory: %s" % ("none" if adv is None else ("string" if isinstance(adv, str) else "object")))


def gate_homograph(rep, baseline, patches, stories):
    """First lander wins. A patch key already in the baseline with a different value needs an inline
    override in every batch story that uses the form; two patches giving one key two values fail."""
    if baseline is None:
        rep.warn("homograph", "batch", "no baseline glossary given; homograph gate not run")
        return
    seen, bad = {}, 0
    for pname, p in patches:
        for k, v in (p.get("entries") or {}).items():
            if k in seen and seen[k][1] != v:
                bad += 1; rep.fail("homograph", k, "patches %s and %s gloss it differently" % (seen[k][0], pname))
            seen.setdefault(k, (pname, v))
    for k, (pname, v) in seen.items():
        if k in baseline and baseline[k] != v:
            users = [sid for sid, st, keys in stories if k in keys and k not in (st.get("glossary") or {})]
            if users:
                bad += 1; rep.fail("homograph", k, "existing gloss differs from %s's and %s carry no override"
                                   % (pname, ", ".join(users)))
    for sid, st, keys in stories:
        for k, v in (st.get("glossary") or {}).items():
            if baseline.get(k) == v:
                rep.warn("homograph", "%s:%s" % (sid, k), "inline override equals the shared gloss")
            if k not in keys:
                bad += 1; rep.fail("homograph", "%s:%s" % (sid, k), "inline override for a form the text does not use")
    if not bad:
        rep.ok("homograph", "batch", "%d patch keys" % len(seen))


def gate_manifest(rep, root, ids):
    mb, man = load_json_bytes(os.path.join(root, "stories.json"))
    if json.dumps(man, ensure_ascii=False, indent=1).encode("utf-8") != mb:
        rep.fail("manifest", "stories.json", "does not re-serialise byte-exact with indent=1, ensure_ascii=False")
    entries = man["stories"] if isinstance(man, dict) else man
    ids_seen = [e.get("id") for e in entries]
    dup = sorted({i for i in ids_seen if ids_seen.count(i) > 1})
    if dup:
        rep.fail("manifest", "stories.json", "duplicate ids %s" % dup)
    per = [e for e in entries if e.get("work") == WORK]
    seqs = []
    for e in per:
        sid = e.get("id")
        where = "manifest:%s" % sid
        path = os.path.join(root, e.get("file", ""))
        if not e.get("file") or not os.path.exists(path):
            rep.fail("manifest", where, "file does not resolve"); continue
        st = json.load(open(path, encoding="utf-8"))
        if st.get("glossaryFile") is None and sid == "petit-chaperon-rouge" and sid not in ids:
            rep.warn("manifest", where, "pilot published but not yet re-issued")
            continue
        if list(e.keys()) != MANIFEST_ORDER:
            rep.fail("manifest", where, "entry keys %s, expected %s" % (list(e.keys()), MANIFEST_ORDER))
        for k in ("title", "titleEn", "language", "work", "workEn"):
            if e.get(k) != st.get(k):
                rep.fail("manifest", where, "%s disagrees with the story file" % k)
        if e.get("part") != st.get("titleEn"):
            rep.fail("manifest", where, "part must equal titleEn")
        if e.get("file") != sid + ".json" or st.get("id") != sid:
            rep.fail("manifest", where, "file/id mismatch")
        if sid in BY_ID and e.get("seq") != BY_ID[sid][0]:
            rep.fail("manifest", where, "seq %r, expected %r" % (e.get("seq"), BY_ID[sid][0]))
        gf = st.get("glossaryFile")
        if not gf or not os.path.exists(os.path.join(root, gf)):
            rep.fail("manifest", where, "glossaryFile does not exist")
        seqs.append(e.get("seq"))
    if len([s for s in seqs if s is not None]) != len(set(s for s in seqs if s is not None)):
        rep.fail("manifest", "stories.json", "duplicate seq among Perrault entries")
    ra, ib = os.path.join(root, "reader.html"), os.path.join(root, "index.html")
    if open(ra, "rb").read() != open(ib, "rb").read():
        rep.fail("manifest", "index.html", "index.html differs from reader.html")
    if not rep.fails("manifest"):
        rep.ok("manifest", "stories.json", "%d Perrault entries" % len(per))
    return per


def gate_glossary_shape(rep, g):
    need = {"work", "workEn", "language", "note", "glossary"}
    if set(g) != need:
        rep.fail("coverage", GLOSSARY_FILE, "keys %s, expected %s" % (sorted(g), sorted(need)))
        return
    bad = [k for k, v in g["glossary"].items() if k != AW.word_key(k) or not isinstance(v, str) or " \u2014 " not in v]
    if bad:
        rep.fail("coverage", GLOSSARY_FILE, "%d malformed entries, e.g. %r" % (len(bad), bad[:3]))


def run_gates(root, ids, baseline=None, patches=(), lexicon=True):
    rep = Report()
    smap_doc = json.load(open(os.path.join(root, ".github", "tools", "perrault-speech-map.json"), encoding="utf-8"))
    reader = os.path.join(root, "reader.html")
    gpath = os.path.join(root, GLOSSARY_FILE)
    shared_doc = json.load(open(gpath, encoding="utf-8")) if os.path.exists(gpath) else None
    if shared_doc is None:
        rep.fail("coverage", GLOSSARY_FILE, "shared glossary missing")
        shared = {}
    else:
        gate_glossary_shape(rep, shared_doc)
        shared = shared_doc.get("glossary", {})
    gate_map_shape(rep, smap_doc)
    gate_lexicon(rep, smap_doc, lexicon)
    stories_for_homograph, density = [], {}
    for sid in ids:
        path = os.path.join(root, sid + ".json")
        try:
            story = json.load(open(path, encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            rep.fail("parse", sid, "does not parse: %s" % e); continue
        raw = open(path, "rb").read()
        if json.dumps(story, ensure_ascii=False, indent=1).encode("utf-8") != raw:
            rep.fail("parse", sid, "not serialised as indent=1, ensure_ascii=False, no trailing newline")
        seq = BY_ID.get(sid, (0,))[0]
        spath = os.path.join(root, "sources", "perrault-%02d-source.json" % seq)
        if not os.path.exists(spath):
            rep.fail("concat", sid, "no archived source %s" % os.path.basename(spath)); continue
        source = json.load(open(spath, encoding="utf-8"))
        if not any("PASS" in c for c in source.get("controls", [])) or any("FAIL" in c for c in source.get("controls", [])):
            rep.fail("concat", sid, "source metadata does not record passing controls")
        gate_fields(rep, sid, story, source)
        if rep.fails("parse") and not isinstance(story.get("sentences"), list):
            continue
        gate_text_structure(rep, sid, story, source)
        no = node_tokens(reader, story["sentences"], {"shared": shared, "inline": story.get("glossary") or {}})
        missing = sorted({k for o in no for k in o.get("missing", [])})
        if missing:
            rep.fail("coverage", sid, "%d forms have no gloss: %s" % (len(missing), ", ".join(missing[:12])))
        else:
            rep.ok("coverage", sid, "%d distinct forms" % len({k for o in no for k in o["keys"]}))
        par = 0
        for k, (u, o) in enumerate(zip(story["sentences"], no)):
            if AW.WORD_RE.findall(u["t"]) != o["t"] or (
                    isinstance(u.get("say"), str) and AW.WORD_RE.findall(u["say"]) != o.get("say")):
                par += 1; rep.fail("regex-parity", "%s#%d" % (sid, k), "Python and reader tokenize differently")
        if not par:
            rep.ok("regex-parity", sid)
        density[sid] = gate_density(rep, sid, story)
        gate_say(rep, sid, story, smap_doc, no)
        gate_scan(rep, sid, story)
        stories_for_homograph.append((sid, story, {k for o in no for k in o["keys"]}))
    gate_homograph(rep, baseline, patches, stories_for_homograph)
    gate_manifest(rep, root, ids)
    return rep, density


# ----------------------------------------------------------------------------- selftest
def _fixture_tree(tmp, reader_src):
    """A synthetic, invented text (not Perrault's words) exercising every rule."""
    title = "LE MEUNIER ET LA F\u00c9E"
    blocks = [
        {"text": "Il estoit un Meunier & sa femme, qui avoient un moulin. Ils vivoient heureux.", "p": True},
        {"text": "La F\u00e9e vint un jour ; elle dit : \u00ab Je vous donne un don. \u00bb", "p": True},
        {"text": "MORALIT\u00c9.", "heading": True, "p": True},
        {"text": "On voit icy qu'un bien donn\u00e9\nNe se perd jamais,\nQuand le c\u0153ur est bon.", "v": True},
        {"text": "AUTRE MORALIT\u00c9.", "heading": True, "p": True},
        {"text": "Le don vaut mieux que l'or.", "p": True},
    ]
    inventory = "".join(sorted(set("".join(b["text"] for b in blocks)) - {" ", "\n"}))
    src = {"id": "petit-chaperon-rouge", "seq": 3, "title": title, "blocks": blocks,
           "tokens": 0, "inventory": inventory, "controls": ["fixture: PASS"]}
    os.makedirs(os.path.join(tmp, "sources"))
    os.makedirs(os.path.join(tmp, ".github", "tools"))
    json.dump(src, open(os.path.join(tmp, "sources", "perrault-03-source.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    smap = {"work": WORK, "note": "fixture", "symbols": {"&": "et"},
            "wordClipReadings": {"l": "le", "qu": "que"}, "properNouns": [],
            "map": {"estoit": "\u00e9tait", "avoient": "avaient", "vivoient": "vivaient", "icy": "ici"}}
    json.dump(smap, open(os.path.join(tmp, ".github", "tools", "perrault-speech-map.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    S = lambda **kw: {k: kw[k] for k in SENT_ORDER if k in kw}
    sents = [
        S(p=True, t="Il estoit un Meunier & sa femme, qui avoient un moulin.",
          l="There was a Miller and his wife, who had a mill.", n="\u00abestoit\u00bb is the 1697 spelling of \u00ab\u00e9tait\u00bb."),
        S(t="Ils vivoient heureux.", l="They lived happy.", i="They lived happily.", n="\u00abvivoient\u00bb: imperfect, modern \u00abvivaient\u00bb."),
        S(p=True, t="La F\u00e9e vint un jour ; elle dit : \u00ab Je vous donne un don. \u00bb",
          l="The Fairy came one day; she said: \u201cI you give a gift.\u201d", i="One day the Fairy came and said, \u201cI give you a gift.\u201d",
          n="Pass\u00e9 simple \u00abvint\u00bb; \u2018came\u2019."),
        S(p=True, t="MORALIT\u00c9.", l="MORAL.", n="The moral follows the tale in verse."),
        S(v=True, t="On voit icy qu'un bien donn\u00e9\nNe se perd jamais,\nQuand le c\u0153ur est bon.",
          l="One sees here that a good given\nNot itself loses ever,\nWhen the heart is good.",
          i="Here we see that a kindness done\nis never lost\nwhen the heart is good.", n="\u00abicy\u00bb for \u00abici\u00bb."),
        S(p=True, t="AUTRE MORALIT\u00c9.", l="ANOTHER MORAL."),
        S(p=True, t="Le don vaut mieux que l'or.", l="The gift is-worth more than the gold.", i="A gift is worth more than gold.",
          n="\u00abvaut mieux que\u00bb: \u2018is better than\u2019."),
    ]
    for u in sents:
        say = build_say(u["t"], bool(u.get("v")), smap["map"], smap["symbols"], WORD_PAT)
        if say:
            items = list(u.items()); u.clear()
            for k, v in items:
                u[k] = v
                if k == "t":
                    u["say"] = say
    story = {"id": "petit-chaperon-rouge", "title": title, "titleEn": "Little Red Riding Hood", "language": "French",
             "langCode": "fr-FR", "work": WORK, "workEn": WORK_EN, "part": "Little Red Riding Hood",
             "source": SOURCE_HEAD.format(title=title) + " " + SOURCE_TAIL,
             "about": "An invented fixture text used only by the selftest; it exercises every gate rule.",
             "wordClips": True, "glossaryFile": GLOSSARY_FILE, "sentences": sents}
    json.dump(story, open(os.path.join(tmp, "petit-chaperon-rouge.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    words = sorted({AW.word_key(w) for u in sents for w in AW.WORD_RE.findall(u["t"])})
    gl = {"work": WORK, "workEn": WORK_EN, "language": "French", "note": "fixture",
          "glossary": {w: "%s \u2014 fixture gloss" % w for w in words}}
    json.dump(gl, open(os.path.join(tmp, GLOSSARY_FILE), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    man = {"stories": [
        {"id": "other", "title": "X", "titleEn": "X", "language": "German", "work": "W", "workEn": "W", "part": "X", "file": "other.json"},
        {"id": "petit-chaperon-rouge", "title": title, "titleEn": "Little Red Riding Hood", "language": "French",
         "work": WORK, "workEn": WORK_EN, "part": "Little Red Riding Hood", "file": "petit-chaperon-rouge.json", "seq": 3}]}
    open(os.path.join(tmp, "stories.json"), "wb").write(json.dumps(man, ensure_ascii=False, indent=1).encode("utf-8"))
    open(os.path.join(tmp, "other.json"), "w").write('{"id":"other","sentences":[]}')
    open(os.path.join(tmp, "reader.html"), "w", encoding="utf-8").write(reader_src)
    open(os.path.join(tmp, "index.html"), "w", encoding="utf-8").write(reader_src)


def _edit_json(path, fn):
    d = json.load(open(path, encoding="utf-8"))
    fn(d)
    open(path, "wb").write(json.dumps(d, ensure_ascii=False, indent=1).encode("utf-8"))


def selftest():
    reader = None
    for cand in (os.path.join(HERE, "..", "..", "reader.html"), "reader.html"):
        if os.path.exists(cand):
            reader = open(cand, encoding="utf-8").read(); break
    if reader is None:
        print("selftest: FAIL \u2014 reader.html not found (run from a repository checkout)")
        return 1
    SID = "petit-chaperon-rouge"
    ST = SID + ".json"

    def sent(d, k):
        return d["sentences"][k]

    def set_say(d, k, v):
        u = d["sentences"][k]; items = [(a, b) for a, b in u.items() if a != "say"]; u.clear()
        for a, b in items:
            u[a] = b
            if a == "t":
                u["say"] = v

    DEFECTS = [
        ("dropped word", "concat", ST, lambda d: sent(d, 1).__setitem__("t", "Ils heureux.")),
        ("moved p flag", "paragraphs", ST, lambda d: (sent(d, 2).pop("p"), sent(d, 1).__setitem__("p", True))),
        ("v unit given p", "paragraphs", ST, lambda d: d["sentences"].__setitem__(4, dict([("p", True)] + list(sent(d, 4).items())))),
        ("say with one token too many", "say-parity", ST, lambda d: set_say(d, 0, sent(d, 0)["say"].replace("un moulin", "un grand moulin"))),
        ("say token not in the map", "say-parity", ST, lambda d: set_say(d, 1, "Ils vivent heureux.")),
        ("say on a unit needing none", "say-parity", ST, lambda d: set_say(d, 6, "Le don vaut mieux que l'or.")),
        ("verse pause comma missing", "say-parity", ST, lambda d: set_say(d, 4, sent(d, 4)["say"].replace("donn\u00e9,", "donn\u00e9"))),
        ("line split across verse units", "lineation", ST, lambda d: d["sentences"][4:5].__len__() and d["sentences"].__setitem__(
            slice(4, 5), [dict(v=True, t="On voit icy qu'un bien", say="On voit ici qu'un bien", l="a", n="x"),
                          dict(v=True, t="donn\u00e9\nNe se perd jamais,\nQuand le c\u0153ur est bon.", say="donn\u00e9,\nNe se perd jamais,\nQuand le c\u0153ur est bon.", l="b\nc\nd", n="y")])),
        ("missing gloss", "coverage", GLOSSARY_FILE, lambda d: d["glossary"].pop("moulin")),
        ("density below floor", "density", ST, lambda d: [u.pop("n", None) for u in d["sentences"][:4]]),
        ("publisher name in about", "scan", ST, lambda d: d.__setitem__("about", d["about"] + " Chosen by Zev.")),
        ("undefined in a note", "scan", ST, lambda d: sent(d, 0).__setitem__("n", "undefined")),
        ("guillemet inner space", "scan", ST, lambda d: sent(d, 1).__setitem__("n", "\u00ab vivoient \u00bb is old.")),
        ("\u2019 as opening quote", "scan", ST, lambda d: sent(d, 2).__setitem__("n", "Pass\u00e9 simple, \u2019came\u2019.")),
        ("manifest title mismatch", "manifest", "stories.json", lambda d: d["stories"][1].__setitem__("title", "Autre")),
        ("manifest seq missing", "manifest", "stories.json", lambda d: d["stories"][1].pop("seq")),
        ("bad modern form in map", "speech-lexicon", ".github/tools/perrault-speech-map.json", lambda d: d["map"].__setitem__("icy", "icci")),
        ("field order", "parse", ST, lambda d: (lambda items: (d.clear(), d.update([items[1], items[0]] + items[2:])))(list(d.items()))),
        ("audio field present", "parse", ST, lambda d: d.__setitem__("audio", "audio/x")),
        ("title differs from source", "parse", ST, lambda d: d.__setitem__("title", "Le Meunier")),
    ]
    SPECIAL = [
        ("index.html differs", "manifest", lambda tmp: open(os.path.join(tmp, "index.html"), "a").write("<!-- -->")),
        ("character outside inventory", "inventory", lambda tmp: (
            _edit_json(os.path.join(tmp, ST), lambda d: sent(d, 6).__setitem__("t", "Le don vaut mieux que l'or \u00a7.")),
            _edit_json(os.path.join(tmp, "sources", "perrault-03-source.json"),
                       lambda d: d["blocks"][5].__setitem__("text", "Le don vaut mieux que l'or \u00a7.")))),
        ("stories.json not byte-exact", "manifest", lambda tmp: open(os.path.join(tmp, "stories.json"), "ab").write(b"\n")),
    ]
    failures = 0
    tmp0 = tempfile.mkdtemp()
    try:
        _fixture_tree(tmp0, reader)
        rep, dens = run_gates(tmp0, [SID], baseline={}, patches=[], lexicon=True)
        control_fails = rep.fails()
        print("selftest control: %s" % ("PASS" if not control_fails else "FAIL"))
        if control_fails:
            print(rep.text()); failures += 1
        # homograph: a patch contradicting the baseline with no override
        rep_h, _ = run_gates(tmp0, [SID], baseline={"moulin": "moulin \u2014 something else"},
                             patches=[("patch-a", {"entries": {"moulin": "moulin \u2014 mill"}})], lexicon=True)
        caught = bool(rep_h.fails("homograph"))
        print("  %-34s -> %-14s %s" % ("homograph conflict, no override", "homograph", "caught" if caught else "MISSED"))
        failures += 0 if caught else 1
        for name, gate, rel, fn in DEFECTS:
            tmp = tempfile.mkdtemp()
            try:
                _fixture_tree(tmp, reader)
                _edit_json(os.path.join(tmp, rel), fn)
                r, _ = run_gates(tmp, [SID], baseline={}, patches=[], lexicon=True)
                caught = bool(r.fails(gate))
                why = r.fails(gate)[0][3][:70] if caught else ""
            except Exception as e:  # noqa: BLE001
                caught = False; why = ""; print("    exception: %s" % e)
            finally:
                shutil.rmtree(tmp, ignore_errors=True)
            print("  %-34s -> %-14s %s  %s" % (name, gate, "caught" if caught else "MISSED", why))
            failures += 0 if caught else 1
        for name, gate, fn in SPECIAL:
            tmp = tempfile.mkdtemp()
            try:
                _fixture_tree(tmp, reader)
                fn(tmp)
                r, _ = run_gates(tmp, [SID], baseline={}, patches=[], lexicon=True)
                caught = bool(r.fails(gate))
                why = r.fails(gate)[0][3][:70] if caught else ""
            finally:
                shutil.rmtree(tmp, ignore_errors=True)
            print("  %-34s -> %-14s %s  %s" % (name, gate, "caught" if caught else "MISSED", why))
            failures += 0 if caught else 1
    finally:
        shutil.rmtree(tmp0, ignore_errors=True)
    print("selftest: %s (%d defect kinds + control)" % ("PASS" if not failures else "FAIL", len(DEFECTS) + len(SPECIAL) + 1))
    return 0 if not failures else 1


def reader_js_prelude_from_text(src):
    a = src.index("const WORD_CLASS"); b = src.index("\n", src.index("function wordKey("))
    return src[a:b + 1]


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__); return 0
    if argv[0] == "selftest":
        return selftest()
    if argv[0] == "gate":
        import argparse
        ap = argparse.ArgumentParser()
        ap.add_argument("--root", required=True)
        ap.add_argument("--ids", default="")
        ap.add_argument("--all", action="store_true")
        ap.add_argument("--baseline-glossary")
        ap.add_argument("--patch", action="append", default=[])
        ap.add_argument("--no-lexicon", action="store_true")
        ap.add_argument("--json")
        a = ap.parse_args(argv[1:])
        if a.all:
            man = json.load(open(os.path.join(a.root, "stories.json"), encoding="utf-8"))
            ids = [e["id"] for e in man["stories"] if e.get("work") == WORK
                   and json.load(open(os.path.join(a.root, e["file"]), encoding="utf-8")).get("glossaryFile")]
        else:
            ids = [x for x in a.ids.split(",") if x]
        baseline = None
        if a.baseline_glossary:
            baseline = json.load(open(a.baseline_glossary, encoding="utf-8")) if os.path.exists(a.baseline_glossary) else {"glossary": {}}
            baseline = baseline.get("glossary", baseline)
        patches = [(os.path.basename(p), json.load(open(p, encoding="utf-8"))) for p in a.patch]
        rep, dens = run_gates(a.root, ids, baseline, patches, lexicon=not a.no_lexicon)
        print(rep.text())
        nf = len(rep.fails())
        print("GATES: %s (%d FAIL, %d WARN) over %s" % ("PASS" if not nf else "FAIL", nf,
              sum(1 for r in rep.rows if r[0] == "WARN"), ",".join(ids) or "(no stories)"))
        if a.json:
            json.dump({"rows": rep.rows, "density": dens}, open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        return 0 if not nf else 1
    print("unknown command %r" % argv[0]); return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
