"""Cantar de mio Cid — work hooks for .github/pipeline/run3/r3.py.

Verse, text model, as in the pilot cid-tiradas-01-04 (2026-07-20). Pidal 1923's text is established part by
part (status todo → established → published): the run starts from the mechanically cleaned OCR draft in
source/ocr/<id>.txt (structure and line numbers already checked against every page image on 2026-10-12),
reads every line on the page image (source/raw/pidal1923_text.pdf), corrects letters, marks Pidal's italics
as [brackets], and writes source/established/<id>.txt. The drafting run then tiles that text exactly."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'run3'))
import r3lib as R

OCR = os.path.join(HERE, 'source', 'ocr')
EST = os.path.join(HERE, 'source', 'established')
GLOSS = os.path.join(R.ROOT, 'cid-glossary.json')
JUNK = set('£^{}|<>~_\\@#$%*=')


def parse(path):
    """[(tirada, label, text)] from an OCR draft or an established file; PROSE lines and comments skipped."""
    out, tir = [], None
    for raw in open(path, encoding='utf-8'):
        line = raw.rstrip('\n')
        m = re.match(r'##\s*tirada\s+(\S+)', line)
        if m:
            tir = m.group(1)
            continue
        if not line.strip() or line.startswith('#'):
            continue
        parts = line.split('\t')
        if parts[0].strip().upper() == 'PROSE':
            continue
        out.append((tir, parts[0].strip(), parts[1] if len(parts) > 1 else ''))
    return out


def est_path(p):
    return os.path.join(EST, p['id'] + '.txt')


def slice_source(p):
    if not os.path.exists(est_path(p)):
        return None
    return '\n'.join(f'{t}\t{l}\t{x}' for t, l, x in parse(est_path(p)))


def establish_packet(p):
    return f"""# Establish — {p['id']}: tiradas {p['tiradas'][0]}–{p['tiradas'][1]}, lines {p['lines']['first']}–{p['lines']['last']}

Starting draft: source/ocr/{p['id']}.txt (OCR text layer, mechanically cleaned; line labels and tirada
breaks already checked by eye on 2026-10-12 — keep them unless the image plainly shows otherwise, and say so
in LOG.md if you change one). Page images: source/raw/pidal1923_text.pdf, PDF pages {p['pdfPages'][0]}–{p['pdfPages'][-1]}
(printed page = PDF page − 4).

Flags on this part (from the structural check): {'; '.join(p.get('flags') or ['none'])}

Procedure — the image is the authority for every letter:
1. Render each page with pymupdf (`pip install pymupdf` if needed) at zoom 1.3–1.5, cropped between the
   printed rule under the running head and the rule above Pidal's footnotes (footnotes are smaller type,
   each beginning with a line number — never verse). Then read strips of about 8 lines at zoom 2.
2. Correct every line letter by letter against the image. Known OCR faults: ç read as q, £, (J or c;
   an accent added to Pidal's unaccented "mio" (OCR "mió"); accents lost or added; rn→m, e→c; spaces
   inside words; a line number stuck to the first word; the overflow of a long line printed on the next
   line after "[" — put it back at the end of its own line; words dropped at line end.
3. Italics are Pidal's restorations and the OCR never shows them: look for them on every line. Letter- or
   word-level italics become [brackets] (entróv[e], R[o]y, [Burgos]); a wholly italic line is printed plain
   and keeps the marker "\t[ITALIC LINE]" after its text (the drafter flags it in the note).
4. Quotation marks: keep a single opening “ and closing ” per speech; drop the repeated quote Pidal sets at
   the start of every line inside a speech. No inverted ¡ ¿ unless Pidal prints them.
5. Leave out Pidal's prose restorations of the lost folios (lines marked PROSE): the poem does not have
   them; the drafter's note says what is lost and what Pidal supplies from the chronicle.
6. Write source/established/{p['id']}.txt in the same layout as the draft: "## tirada N" lines, then one
   verse per line as "<label>\\t<text>" in Pidal's PRINT order (he sometimes moves lines but keeps their
   numbers — keep his order and his numbers).
7. `python3 ../run3/r3.py pin cid {p['id']}` checks it (every label of the draft present, in order; no OCR
   junk characters; brackets balanced) and pins it. Record in LOG.md how many lines you corrected and any
   reading you were unsure of; put a genuinely unreadable spot in QUESTIONS.md and mark it in the text with
   the OCR reading and a trailing "\\t[UNSURE]".
"""


def check_established(p):
    errs = []
    if not os.path.exists(est_path(p)):
        return [f'{os.path.relpath(est_path(p), R.ROOT)} does not exist']
    draft = parse(os.path.join(OCR, p['id'] + '.txt'))
    est = parse(est_path(p))
    if [(t, l) for t, l, _ in draft] != [(t, l) for t, l, _ in est]:
        a = [(t, l) for t, l, _ in draft]
        b = [(t, l) for t, l, _ in est]
        i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)))
        errs.append(f'tirada/line labels differ from the checked draft at position {i}: draft {a[i] if i < len(a) else None} vs established {b[i] if i < len(b) else None} — if the image really shows otherwise, change the draft too and say so in LOG.md')
    for t, l, x in est:
        if not x.strip():
            errs.append(f'line {l}: empty')
        bad = sorted(c for c in set(x) if c in JUNK)
        if bad:
            errs.append(f'line {l}: OCR junk {bad}')
        if x.count('[') != x.count(']'):
            errs.append(f'line {l}: unbalanced brackets')
        if re.search(r'\d', x):
            errs.append(f'line {l}: a digit in the verse')
    return errs


def verses(p):
    return [(t, l, re.sub(r'\t\[(ITALIC LINE|UNSURE)\]$', '', x).split('\t')[0]) for t, l, x in parse(est_path(p))]


def packet(p):
    v = verses(p)
    out = [f'# Packet — {p["id"]}: {p["name"]}', '',
           f'Tiradas {p["tiradas"][0]}–{p["tiradas"][1]}, Pidal lines {p["lines"]["first"]}–{p["lines"]["last"]} ({p["cantar"]}).',
           'The established text below is pinned. A unit\'s `t` is one or more consecutive verses joined by "\\n", cut by script.',
           'Flags: ' + '; '.join(p.get('flags') or ['none']), '']
    tir = None
    marks = {l: m.group(1) for t, l, x in parse(est_path(p)) for m in [re.search(r'\t\[(ITALIC LINE|UNSURE)\]$', x)] if m}
    for t, l, x in v:
        if t != tir:
            tir = t
            out.append(f'\n## tirada {t}\n')
        out.append(f'{l}\t{x}' + (f'\t[{marks[l]}]' if l in marks else ''))
    g = R.jload(GLOSS)['glossary']
    toks = {w for _, _, x in v for w in R.tokens(x)}
    out += ['', f'Glossary: {len([w for w in toks if w in g])} of {len(toks)} forms already in cid-glossary.json.']
    return '\n'.join(out) + '\n'


def forms(p):
    g = R.jload(GLOSS)['glossary']
    novel, known = {}, {}
    for _, _, x in verses(p):
        for w in R.tokens(x):
            (known if w in g else novel)[w] = g.get(w, '')
    return novel, known


def assemble(p, units, gloss):
    cfg = R.work_cfg('cid')
    v = verses(p)
    G = R.jload(GLOSS)
    broaden = gloss.pop('__broaden__', {}) if isinstance(gloss, dict) else {}
    for k, val in gloss.items():
        if val and k not in G['glossary']:
            G['glossary'][k] = val
    G['glossary'].update(broaden)
    tstart = set()
    prev = None
    for i, (t, l, x) in enumerate(v):
        if t != prev:
            tstart.add(i)
            prev = t
    sents, pos = [], 0
    for k, u in enumerate(units['sentences']):
        n = u['t'].count('\n') + 1
        s = {'v': True, 'ln': int(re.match(r'\d+', v[pos][1]).group()) if pos < len(v) else 0, 't': u['t'], 'l': u['l']}
        for f in ('i', 'n'):
            if u.get(f):
                s[f] = u[f]
        if pos in tstart:
            s['p'] = True
        sents.append(s)
        pos += n
    story = dict(cfg['header'])
    a, b = p['tiradas']
    story.update({'id': p['id'], 'title': 'Cantar de mio Cid',
                  'titleEn': units.get('titleEn') or f'The Song of the Cid — {p["name"]} (tiradas {a}–{b}, lines {p["lines"]["first"]}–{p["lines"]["last"]})',
                  'part': units.get('part') or f'Tiradas {a}–{b} · {p["name"]} (lines {p["lines"]["first"]}–{p["lines"]["last"]})',
                  'glossaryFile': 'cid-glossary.json',
                  'source': cfg['sourceStatement'].replace('{cite}', f'pp. {p["printedPages"][0]}–{p["printedPages"][-1]}, lines {p["lines"]["first"]}–{p["lines"]["last"]} (tiradas {a}–{b})'),
                  'sentences': sents})
    if units.get('about'):
        story['about'] = units['about']
    return story, {GLOSS: G}


def validate(p, story):
    errs, warns = [], []
    v = verses(p)
    joined = '\n'.join(s['t'] for s in story['sentences'])
    want = '\n'.join(x for _, _, x in v)
    if joined != want:
        a, b = joined.split('\n'), want.split('\n')
        i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)))
        errs.append(f'units do not reproduce the established text at verse {i} ({v[i][1] if i < len(v) else "end"}): '
                    f'{a[i] if i < len(a) else None!r} vs {b[i] if i < len(b) else None!r}')
    g = R.jload(GLOSS)['glossary']
    miss = R.glossary_coverage(story, g)
    if miss:
        errs.append(f'{len(miss)} forms have no glossary entry: {miss[:20]}')
    for k, s in enumerate(story['sentences']):
        if s['t'].count('\n') + 1 > 6:
            warns.append(f'unit {k}: more than six verses')
        if s.get('l', '').count('\n') != s['t'].count('\n'):
            warns.append(f'unit {k}: l should keep the line division of t')
    return errs, warns
