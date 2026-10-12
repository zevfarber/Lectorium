#!/usr/bin/env python3
"""Run 3 shared machinery — the "unusual texts" run (Hammurabi, Kebra Nagast, Secret History,
Mabinogi, Cid, Azatiwada, Sumerian King List).

Each work lives in .github/pipeline/<work>/ with:
    work.json      fixed facts about the work (prefix, header fields for every story, glossary mode)
    parts.json     the cut: one entry per part, with status todo | established | published
    hooks.py       the work's own code: source slice, packet, assembly, validation
    source/        the pinned public-domain source (and, for scan-based works, established/<id>.txt)
    conventions.md, runbook.md, LOG.md, QUESTIONS.md, claims/, drafts/<id>/

This module holds what every work shares. Python standard library only.
"""
import hashlib, importlib.util, json, os, re, sys, time, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
PIPE = os.path.dirname(HERE)                      # .github/pipeline
ROOT = os.path.dirname(os.path.dirname(PIPE))     # repository root
sys.path.insert(0, os.path.join(ROOT, '.github', 'scripts'))
from wordre import WORD_RE  # the reader's own word splitter (one copy, shared)  # noqa: E402

CLAIM_STALE_HOURS = 6


def die(*a):
    print('REFUSED:', *a)
    sys.exit(1)


def jload(p):
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def jdump(obj, p, indent=1):
    tmp = p + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=indent)
        f.write('\n')
    os.replace(tmp, p)


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def wdir(work):
    d = os.path.join(PIPE, work)
    if not os.path.isdir(d):
        die('no work folder', d)
    return d


def work_cfg(work):
    return jload(os.path.join(wdir(work), 'work.json'))


def parts_doc(work):
    return jload(os.path.join(wdir(work), 'parts.json'))


def save_parts(work, doc):
    jdump(doc, os.path.join(wdir(work), 'parts.json'))


def part(work, pid):
    for p in parts_doc(work)['parts']:
        if p['id'] == pid:
            return p
    die(f'{pid} is not in {work}/parts.json')


def hooks(work):
    path = os.path.join(wdir(work), 'hooks.py')
    spec = importlib.util.spec_from_file_location(f'hooks_{work.replace("-", "_")}', path)
    m = importlib.util.module_from_spec(spec)
    sys.path.insert(0, wdir(work))
    spec.loader.exec_module(m)
    return m


def drafts(work, pid):
    d = os.path.join(wdir(work), 'drafts', pid)
    os.makedirs(d, exist_ok=True)
    return d


# ---------------------------------------------------------------- claims
def claims_dir(work):
    d = os.path.join(wdir(work), 'claims')
    os.makedirs(d, exist_ok=True)
    return d


def live_claim(work, pid):
    p = os.path.join(claims_dir(work), pid + '.md')
    if not os.path.exists(p):
        return False
    txt = open(p, encoding='utf-8').read()
    m = re.search(r'(\d{4}-\d\d-\d\dT\d\d:\d\d)', txt)
    if not m:
        return True
    t = time.mktime(time.strptime(m.group(1), '%Y-%m-%dT%H:%M')) - time.timezone
    return (time.time() - t) / 3600 < CLAIM_STALE_HOURS


def next_part(work):
    """The first part not yet published and not under a live claim. Returns (part, action) where
    action is 'establish' (a scan-based part whose text is not yet established) or 'draft'."""
    cfg = work_cfg(work)
    for p in parts_doc(work)['parts']:
        if p.get('status') == 'published':
            continue
        if live_claim(work, p['id']):
            continue
        needs = p.get('establish', cfg.get('establish', False))
        if needs and p.get('status') != 'established':
            return p, 'establish'
        return p, 'draft'
    return None, None


# ---------------------------------------------------------------- text helpers
def tokens(t):
    """Reader tokens for glossary lookup: WORD_RE matches, lowercased, editorial brackets removed."""
    return [re.sub(r'[\[\]()]', '', w).lower() for w in WORD_RE.findall(t)]


def nfc_ok(s):
    return unicodedata.normalize('NFC', s) == s


def first_lemma(entry):
    return entry.split(' — ', 1)[0].strip()


# ---------------------------------------------------------------- manifest
def manifest_insert(work, pid, entry):
    """Insert/replace the stories.json entry for pid right after the previous part of this work."""
    mp = os.path.join(ROOT, 'stories.json')
    M = jload(mp)
    st = M['stories']
    st[:] = [e for e in st if e.get('id') != pid]
    order = [p['id'] for p in parts_doc(work)['parts']]
    prior = set(order[:order.index(pid)]) | set(work_cfg(work).get('publishedBefore', []))
    idx = [k for k, e in enumerate(st) if e.get('id') in prior]
    pos = (max(idx) + 1) if idx else len(st)
    st.insert(pos, entry)
    jdump(M, mp)


# ---------------------------------------------------------------- common validation
def common_checks(story, p, cfg):
    errs, warns = [], []
    if story.get('id') != p['id']:
        errs.append('id does not match the part')
    for k in cfg.get('header', {}):
        if story.get(k) != cfg['header'][k]:
            errs.append(f'header field {k} differs from work.json')
    for k in ('title', 'titleEn', 'part', 'source', 'sentences'):
        if not story.get(k):
            errs.append(f'missing {k}')
    blob = json.dumps(story, ensure_ascii=False)
    if not nfc_ok(blob):
        errs.append('text is not NFC')
    for k, s in enumerate(story.get('sentences', [])):
        if not (s.get('t') or '').strip():
            errs.append(f'unit {k}: empty t')
        if not (s.get('l') or '').strip():
            errs.append(f'unit {k}: missing l')
        if not (s.get('n') or '').strip():
            warns.append(f'unit {k}: no note')
        for f in ('l', 'i', 'n'):
            v = s.get(f) or ''
            if re.search(r'\b(Heaney|Tolkien|Budge|Guest|Gantz|Roth|Richardson|de Rachewiltz|Cleaves|Hawkins|Jacobsen)\b', v):
                warns.append(f'unit {k}: {f} names a modern translator — check it is not borrowing wording')
            if len(v) > 1600:
                warns.append(f'unit {k}: {f} is very long ({len(v)} chars)')
    for phrase in cfg.get('redFlags', []):
        if phrase.lower() in blob.lower():
            errs.append(f'red-flag phrase from a modern translation found: {phrase!r}')
    return errs, warns


def glossary_coverage(story, gloss):
    """Text-model works: every reader token of every t has an entry."""
    missing = sorted({w for s in story['sentences'] for w in tokens(s['t']) if w not in gloss})
    return missing


def words_checks(story, sign_glossary=None, signs_needed=True):
    """Words-model works: every unit has words; every glyph has s/role/tr; sign keys known."""
    errs, warns = [], []
    for k, s in enumerate(story['sentences']):
        ws = s.get('words')
        if not ws:
            errs.append(f'unit {k}: no words[]')
            continue
        for j, w in enumerate(ws):
            if not w.get('glyphs'):
                errs.append(f'unit {k} word {j}: no glyphs')
            for g in w.get('glyphs', []):
                if not g.get('s'):
                    errs.append(f'unit {k} word {j}: glyph without s')
                if g.get('role') not in ('phon', 'log', 'det', 'comp', 'num', 'punct', 'suff'):
                    errs.append(f'unit {k} word {j}: bad role {g.get("role")!r}')
                if sign_glossary is not None and signs_needed and g.get('sign') and g['sign'] not in sign_glossary \
                        and g.get('role') != 'punct':
                    errs.append(f'unit {k} word {j}: sign {g["sign"]!r} is not in the sign glossary')
            for m in w.get('morph', []):
                if not m.get('lemma') or not isinstance(m.get('g'), list):
                    errs.append(f'unit {k} word {j}: malformed morph')
    return errs, warns
