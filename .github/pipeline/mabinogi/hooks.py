"""Pedeir Keinc y Mabinogi — work hooks for .github/pipeline/run3/r3.py.

Prose, text model, as in the pilot mabinogi-001 (2026-09-27). The White Book text (Evans 1907) is
established part by part (todo → established → published), exactly as the pilot's was: Evans's OCR for the
part's columns (source/drafts/<id>-ocr.txt) aligned against the second witness (source/drafts/<id>-witness.txt,
cy.wikisource, comparison only); every disagreement in the worklist (source/drafts/<id>-diffs.txt) settled
on Evans's page image (source/raw/evans1907.pdf); then our word division, punctuation, capitals and
quotation marks applied. The established text is source/established/<id>.txt: paragraphs separated by a
blank line."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'run3'))
import r3lib as R

EST = os.path.join(HERE, 'source', 'established')
DR = os.path.join(HERE, 'source', 'drafts')
GLOSS = os.path.join(R.ROOT, 'mabinogi-glossary.json')
BRANCH = {'First Branch: Pwyll': ('Pwyll Pendeuic Dyuet', 'Pwyll, Prince of Dyfed'),
          'Second Branch: Branwen': ('Branwen uerch Lyr', 'Branwen, Daughter of Llŷr'),
          'Third Branch: Manawydan': ('Manawydan uab Llyr', 'Manawydan, Son of Llŷr'),
          'Fourth Branch: Math': ('Math uab Mathonwy', 'Math, Son of Mathonwy')}


def est_path(p):
    return os.path.join(EST, p['id'] + '.txt')


def paragraphs(p):
    txt = open(est_path(p), encoding='utf-8').read().strip()
    return [re.sub(r'\s+', ' ', x).strip() for x in re.split(r'\n\s*\n', txt) if x.strip()]


def slice_source(p):
    if not os.path.exists(est_path(p)):
        return None
    return '\n\n'.join(paragraphs(p))


def establish_packet(p):
    return f"""# Establish — {p['id']}: {p['part']} ({p['group']})

Evans cols {p['evans_cols']}, PDF pages {p['pdf_pages']} of source/raw/evans1907.pdf (column c is on PDF page
(c+65)//2; odd columns on the left). Opens: «{p['opening']}» — closes: «{p['closing']}».
Inputs: source/drafts/{p['id']}-ocr.txt (Evans's OCR, his lines), source/drafts/{p['id']}-witness.txt (the
second witness, cy.wikisource — NOT the edition, never adopted without the image), source/drafts/{p['id']}-diffs.txt
(the worklist: {p['disagreements']['check']} 'check' items and {p['disagreements']['loss']} 'loss' items to look at;
{p['disagreements']['glyph']} 'glyph' items are known misreadings of Evans's special letters, settled without the image).
Issues found on 2026-10-12: {'; '.join(p.get('issues') or ['none'])}

Procedure (as for mabinogi-001; the image decides):
1. For every 'check' and 'loss' item, render a crop of the column (±2 lines, 220–260 dpi; `python3 ../run3/page.py
   source/raw/evans1907.pdf <page> --zoom 3.2 --clip x0,y0,x1,y1`) and read Evans's letters. Also look at:
   the part's opening capital (P, B, G, M are large initials the OCR drops), every raised (inserted) letter, every
   blank space the scribe left, and every witness word missing from the OCR. Log each decision in
   drafts/{p['id']}/establish-log.md.
2. Evans's special sorts, as the conventions render them: 6-shaped w → w; r-rotunda → r; dotted y → y; long s → s.
   Raised letters go into the line. Evans's underlines, accents, ' marks and * are dropped; line-end marks
   (= - ' ^ / » «) join the word, never read as letters.
3. White Book defects: where Evans shows a blank and the sense needs the Red Book's word(s), supply only what the
   sense needs and record it for the drafter's note (source/raw/rhys-evans1905_djvu.txt is the Red Book, a
   public-domain third witness). Phrases the second witness supplies from the Red Book that the sense does not
   need are NOT supplied. A scribal slip that is still readable stays as written.
4. Apply our word division (proclitics separated; fused forms with an apostrophe: a'y, y'r, o'r, i'th, a'm …),
   modern punctuation, capitals for sentence starts and proper names only, and “ ” around speech. Follow the
   practice of the published mabinogi-001 (source/mabinogi-001-established.txt is its established text).
5. Paragraphs: a new paragraph at each change of scene or speaker-exchange (ours), separated by a blank line.
6. Write source/established/{p['id']}.txt and pin it: `python3 ../run3/r3.py pin mabinogi {p['id']}` (it checks the
   text against the OCR letter by letter and refuses wholesale drift).
"""


def _letters(s):
    s = s.lower()
    for a, b in [('ẏ', 'y'), ('ſ', 's'), ('ꝛ', 'r')]:
        s = s.replace(a, b)
    return re.sub(r'[^a-zâêîôûŵŷäëïöüẅÿáéíóúẃý]', '', s)


def check_established(p):
    import difflib
    errs = []
    if not os.path.exists(est_path(p)):
        return [f'{os.path.relpath(est_path(p), R.ROOT)} does not exist']
    est = slice_source(p)
    if '⟦' in est or '⟧' in est or re.search(r'[0-9^&£{}<>|]', est):
        errs.append('OCR marks or digits left in the established text')
    if est.count('“') != est.count('”'):
        errs.append('unbalanced quotation marks')
    ocr = open(os.path.join(DR, p['id'] + '-ocr.txt'), encoding='utf-8').read()
    m = re.search(r'⟦(.*)⟧', ocr, re.S)
    body = m.group(1) if m else re.sub(r'^#.*$', '', ocr, flags=re.M)
    body = re.sub(r'^##.*$', '', body, flags=re.M)
    r = difflib.SequenceMatcher(None, _letters(body), _letters(est), autojunk=False).ratio()
    if r < 0.75:
        errs.append(f'established text agrees with the OCR letter stream only {r:.2f} — expected ≥ 0.75 (the OCR is noisy, '
                    f'but not that noisy); check that the whole part, and only the part, is there')
    return errs


def packet(p):
    paras = paragraphs(p)
    out = [f'# Packet — {p["id"]}: {p["part"]} ({p["group"]})', '',
           f'Evans cols {p["evans_cols"]}. The established text (pinned) follows, one paragraph per block; a unit\'s `t` '
           'is cut from it by script (a sentence, or a long sentence cut at its strongest pause).', '']
    for i, x in enumerate(paras):
        out += [f'¶{i + 1}', x, '']
    log = os.path.join(R.drafts('mabinogi', p['id']), 'establish-log.md')
    if os.path.exists(log):
        out += ['## Establishment log (supplied words, slips kept, readings decided on the image — the notes must say so)', '',
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
    cfg = R.work_cfg('mabinogi')
    G = R.jload(GLOSS)                       # mabinogi-glossary.json is a flat {form: entry} object
    broaden = gloss.pop('__broaden__', {}) if isinstance(gloss, dict) else {}
    for k, v in gloss.items():
        if v and k not in G:
            G[k] = v
    G.update(broaden)
    paras = paragraphs(p)
    starts, acc = set(), 0
    for x in paras:
        starts.add(acc)
        acc += len(re.sub(r'\s', '', x))
    sents, pos = [], 0
    for u in units['sentences']:
        s = {'t': u['t'], 'l': u['l']}
        for f in ('i', 'n'):
            if u.get(f):
                s[f] = u[f]
        if pos in starts:
            s['p'] = True
        sents.append(s)
        pos += len(re.sub(r'\s', '', u['t']))
    title, en = BRANCH[p['group']]
    story = dict(cfg['header'])
    story.update({'id': p['id'], 'sourceId': p['id'], 'title': title, 'titleEn': f'{en} — {p["part"]}',
                  'part': p['part'], 'group': p['group'], 'glossaryFile': 'mabinogi-glossary.json',
                  'source': cfg['sourceStatement'].replace('{cite}', f'columns {p["evans_cols"]}').replace('{branch}', p['group'].split(': ')[0]),
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
    paras = paragraphs(p)
    np = sum(1 for s in story['sentences'] if s.get('p'))
    if np != len(paras):
        errs.append(f'{np} units start a paragraph, the text has {len(paras)} paragraphs (a unit may not straddle two)')
    g = R.jload(GLOSS)
    miss = R.glossary_coverage(story, g)
    if miss:
        errs.append(f'{len(miss)} forms have no glossary entry: {miss[:20]}')
    for k, s in enumerate(story['sentences']):
        if len(s['t'].split()) > 45:
            warns.append(f'unit {k}: {len(s["t"].split())} words — cut at the strongest pause if it runs past about forty')
        if not s.get('i'):
            warns.append(f'unit {k}: no idiomatic English (the pilot gives i on every unit)')
    return errs, warns
