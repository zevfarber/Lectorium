"""Popol Vuh — work hooks for .github/pipeline/run3/r3.py (set up 2026-11-20 for the shared text pipeline).

Prose with a strong couplet structure, text model with a per-word modern spelling (`mt`), as in the
pilot popol-vuh-001 (2026-10-26). Every part takes two firings: ACTION establish reads the K'iche'
column of three manuscript pages into source/established/<id>.txt; ACTION draft translates it.

Established file format (UTF-8):
    # name: <short English name of the episode, for the library>
    # title: <the part's first words in the manuscript spelling, for the K'iche' title>
    # fols: <folios as Ximénez numbers them, e.g. fols. 2v–4r>
    <paragraph>

    <paragraph>
Paragraphs are separated by a blank line; inside a paragraph, line breaks are ignored."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'run3'))
import r3lib as R

EST = os.path.join(HERE, 'source', 'established')
PAGES = os.path.join(HERE, 'source', 'pages')
GLOSS = os.path.join(R.ROOT, 'popol-vuh-glossary.json')
PILOT_END = ('…rutzinic vbanatahic cumal.  (the pilot, popol-vuh-001, ends with these words on the first line of '
             'image 0012; popol-vuh-002 begins with the next words: Ta xquinohih chic vchicopil huyub …)')


def est_path(p):
    return os.path.join(EST, p['id'] + '.txt')


def header(p):
    h = {}
    if os.path.exists(est_path(p)):
        for line in open(est_path(p), encoding='utf-8'):
            m = re.match(r'#\s*(name|title|fols)\s*:\s*(.+)', line)
            if m:
                h[m.group(1)] = m.group(2).strip()
    return h


def paragraphs(p):
    txt = '\n'.join(l for l in open(est_path(p), encoding='utf-8').read().split('\n') if not l.startswith('#')).strip()
    return [re.sub(r'\s+', ' ', x).strip() for x in re.split(r'\n\s*\n', txt) if x.strip()]


def slice_source(p):
    if not os.path.exists(est_path(p)):
        return None
    h = header(p)
    return '\n'.join(f'# {k}: {h.get(k, "")}' for k in ('name', 'title', 'fols')) + '\n' + '\n\n'.join(paragraphs(p))


def _previous(p):
    ps = R.parts_doc('popol-vuh')['parts']
    i = [q['id'] for q in ps].index(p['id'])
    return ps[i - 1] if i else None


def establish_packet(p):
    prev = _previous(p)
    if prev is None:
        start = PILOT_END
    else:
        tail = ' '.join(' '.join(paragraphs(prev)).split()[-14:]) if os.path.exists(est_path(prev)) else '(not found)'
        start = f'…{tail}  (the end of {prev["id"]}; begin with the words that follow these)'
    imgs = ", ".join(f"source/pages/i{n:04d}.jpg" for n in range(p["first_image"], p["last_image"] + 2) if n <= 124 and n not in (86, 102))
    if any(n in (86, 102) for n in range(p["first_image"], p["last_image"] + 1)):
        imgs += " (the Library of Congress has no image 0086 / 0102; see the note in parts.json)"
    return f"""# Establish — {p['id']} (images {p['images']})

Read `conventions.md` first ("What the text looks like", the Parra letters, word division).

Start: {start}
Images: {imgs} (the last one only to finish a sentence that runs over the edge of image {p['last_image']:04d}).
Each image is the K'iche' (left) column of one manuscript page, background flattened. Ximénez's Spanish is in
the right-hand column of the original and is not in these crops.

Procedure (the image decides every letter):
1. Read the column in strips (crop about six lines at a time and enlarge 2–3×, e.g. with PIL), top to bottom,
   image by image, from the start point to the last full stop on image {p['last_image']:04d} (or, if the
   sentence runs on, to its end on the next image). Write the letters as Ximénez wrote them: c/qu, v, z, h, b,
   doubled vowels, and the colonial letters ꜩ ꜯ ꜭ ꜭh ꜫ (capitals Ꜩ Ꜯ Ꜭ Ꜫ). Where the hand is ambiguous between
   ꜭ, ꜫ, g, q, c, look up the same passage in Brasseur 1861 (`source/raw/brasseur1861_djvu.txt`, OCR; his
   q = ꜭ, his g = ꜫ; search for a distinctive name or word near the spot) to choose between letters only —
   Brasseur is never the text.
2. Words Ximénez runs together across a line break are divided; particles he joins to a word are divided as
   the conventions say. A word he adds above the line is printed in place (note it in the log).
3. Punctuation, capitals and quotation marks are ours (“ ” around direct speech). Capitals: sentence start,
   names, the divine titles.
4. Paragraphs: Ximénez's own paragraphs and headings; a heading in capitals is its own paragraph, in
   capitals as he writes it.
5. Log every letter decided against Brasseur, every doubtful reading and every supralinear word in
   `drafts/{p['id']}/establish-log.md`; the drafter turns these into notes.
6. Write `source/established/{p['id']}.txt` in this format:
       # name: <short English name for the library, what happens in this stretch: "The animals are made">
       # title: <the first four to six words of the part, in the manuscript spelling>
       # fols: <folios, as Ximénez numbers them at the top right of each recto, e.g. "fols. 2v–4r">
       <paragraph>

       <paragraph>
   then pin it: `python3 ../run3/r3.py pin popol-vuh {p['id']}`.
"""


def check_established(p):
    errs = []
    if not os.path.exists(est_path(p)):
        return [f'{os.path.relpath(est_path(p), R.ROOT)} does not exist']
    h = header(p)
    for k in ('name', 'title', 'fols'):
        if not h.get(k):
            errs.append(f'the header line "# {k}:" is missing or empty')
    paras = paragraphs(p)
    body = ' '.join(paras)
    if len(body.split()) < 150:
        errs.append(f'only {len(body.split())} words — three manuscript pages hold far more; is the whole part there?')
    if re.search(r'[0-9<>{}|\\^]', body):
        errs.append('digits or markup left in the established text')
    if body.count('“') != body.count('”'):
        errs.append('unbalanced quotation marks')
    if re.search(r'[ʼ’\']', body):
        errs.append('an apostrophe in the manuscript text — Ximénez writes no apostrophes; ejectives are the Parra letters')
    if not errs:                       # name the part for the library and the plan
        p['name'] = h['name']
        p['part'] = h['name']
        p['cite'] = h['fols']
    return errs


def packet(p):
    h = header(p)
    out = [f'# Packet — {p["id"]}: {h.get("name", "")} ({h.get("fols", "")})', '',
           'The established text (pinned) follows, one paragraph per block. A unit\'s `t` is cut from it by script '
           '(a sentence, or a long sentence or litany cut at a syntactic joint; couplets never split).', '']
    for i, x in enumerate(paragraphs(p)):
        out += [f'¶{i + 1}', x, '']
    log = os.path.join(R.drafts('popol-vuh', p['id']), 'establish-log.md')
    if os.path.exists(log):
        out += ['## Establishment log (doubtful readings, letters chosen, supralinear words — the notes must say so)', '',
                open(log, encoding='utf-8').read()]
    return '\n'.join(out) + '\n'


def forms(p):
    g = R.jload(GLOSS)
    novel, known = {}, {}
    for x in paragraphs(p):
        for w in R.tokens(x):
            (known if w in g else novel)[w] = g.get(w, '')
    return novel, known


def assemble(p, units, gloss):
    cfg = R.work_cfg('popol-vuh')
    G = R.jload(GLOSS)
    broaden = gloss.pop('__broaden__', {}) if isinstance(gloss, dict) else {}
    for k, v in gloss.items():
        if v and k not in G:
            G[k] = v
    G.update(broaden)
    h = header(p)
    starts, acc = set(), 0
    for x in paragraphs(p):
        starts.add(acc)
        acc += len(re.sub(r'\s', '', x))
    sents, pos = [], 0
    for u in units['sentences']:
        s = {'t': u['t'], 'mt': list(u.get('mt') or []), 'l': u['l']}
        for f in ('i', 'n'):
            if u.get(f):
                s[f] = u[f]
        if pos in starts:
            s['p'] = True
        sents.append(s)
        pos += len(re.sub(r'\s', '', u['t']))
    story = dict(cfg['header'])
    story.update({'id': p['id'], 'sourceId': p['id'], 'title': h.get('title', ''),
                  'titleEn': f'Popol Vuh — {h.get("name", "")}', 'part': h.get('name', ''),
                  'glossaryFile': 'popol-vuh-glossary.json',
                  'source': cfg['sourceStatement'].replace('{name}', h.get('name', '')).replace('{fols}', h.get('fols', '')),
                  'sentences': sents})
    if units.get('about'):
        story['about'] = units['about']
    return story, {GLOSS: G}


def validate(p, story):
    errs, warns = [], []
    want = re.sub(r'\s+', ' ', ' '.join(paragraphs(p))).strip()
    got = re.sub(r'\s+', ' ', ' '.join(s['t'] for s in story['sentences'])).strip()
    if want != got:
        i = next((k for k in range(min(len(want), len(got))) if want[k] != got[k]), min(len(want), len(got)))
        errs.append(f'units do not tile the established text at character {i}: units {got[i:i+40]!r} vs text {want[i:i+40]!r}')
    np = sum(1 for s in story['sentences'] if s.get('p'))
    if np != len(paragraphs(p)):
        errs.append(f'{np} units start a paragraph, the text has {len(paragraphs(p))} paragraphs (a unit may not straddle two)')
    for k, s in enumerate(story['sentences']):
        n = len(R.WORD_RE.findall(s['t']))
        if len(s.get('mt') or []) != n:
            errs.append(f'unit {k}: mt has {len(s.get("mt") or [])} modern spellings for {n} words')
        if not s.get('i'):
            warns.append(f'unit {k}: no idiomatic English (the pilot gives i on every unit)')
        if len(s['t'].split()) > 45:
            warns.append(f'unit {k}: {len(s["t"].split())} words — cut at a syntactic joint if it runs past about forty')
    if not story.get('about'):
        warns.append('no about (a short paragraph on what happens in this part, as the pilot has)')
    miss = R.glossary_coverage(story, R.jload(GLOSS))
    if miss:
        errs.append(f'{len(miss)} forms have no glossary entry: {miss[:20]}')
    return errs, warns
