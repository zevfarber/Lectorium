"""Ardā Wirāz Nāmag (Book of Arda Viraf) — work hooks for .github/pipeline/run3/r3.py.

Text model with two extras, as in the pilot arda-wiraz-001 (2026-11-13/18):
  * every unit carries `wr`, the letters of the script per word (transliteration), beside `t`, the words as read;
  * every unit carries `img`, word images cut from Haug's 1872 Pahlavi type — the script on the page.

A part is established first (todo → established → published). The established text is two files:
  source/established/<id>.txt       Haug's own Roman reading, one numbered sentence per line ("2.14<TAB>…")
  source/established/<id>.cut.json  where each sentence's Pahlavi sits on the page images (lines, numerals)
Needs numpy + Pillow for the image cut (pip install numpy pillow)."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'run3'))
sys.path.insert(0, os.path.join(HERE, 'tools'))
import r3lib as R

W = 'arda-wiraz'
EST = os.path.join(HERE, 'source', 'established')
GLOSS = os.path.join(R.ROOT, 'arda-wiraz-glossary.json')      # what the reader loads: entry + how it is written
BASE = os.path.join(HERE, 'glossary-base.json')               # {form: "lemma — meaning (grammar)"}
SPELL = os.path.join(HERE, 'spellings.json')                  # {form: [every wr spelling met so far]}
IMG = os.path.join(R.ROOT, 'img', 'arda-wiraz')
WR_OK = set("ʾbgdhwzklmnspcštyr'ABGDEHWZKLMNSOPCQRŠTY0123456789-")
T_OK = re.compile(r"^[A-Za-zāēīōūĀĒĪŌŪšŠčČǰγžŽ \-.,;:?!“”‘’()—]+$")


def est_path(p):
    return os.path.join(EST, p['id'] + '.txt')


def cut_path(p):
    return os.path.join(EST, p['id'] + '.cut.json')


def chapters(p):
    a, b = p['chapters']
    return list(range(a, b + 1))


def sentences(p):
    """[(id, roman)] from the established file, in order; id is 'chapter.sentence'."""
    out = []
    for line in open(est_path(p), encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip() or line.startswith('#'):
            continue
        sid, _, txt = line.partition('\t')
        out.append((sid.strip(), txt.strip()))
    return out


def header(p, key):
    for line in open(est_path(p), encoding='utf-8'):
        m = re.match(r'#\s*%s\s*:\s*(.+)' % key, line)
        if m:
            return m.group(1).strip()
    return None


def slice_source(p):
    if not (os.path.exists(est_path(p)) and os.path.exists(cut_path(p))):
        return None
    cut = json.dumps(R.jload(cut_path(p)), ensure_ascii=False, sort_keys=True)
    return '\n'.join(f'{a}\t{b}' for a, b in sentences(p)) + '\n' + cut


def start_leaf(p):
    if p.get('startLeaf'):
        return p['startLeaf']
    ps = R.parts_doc(W)['parts']
    k = [q['id'] for q in ps].index(p['id'])
    prev = ps[k - 1]
    return (prev.get('leaves') or [None, None])[1]


def _ocr_segment(path, chs):
    s = open(path, encoding='utf-8').read()

    def rom(x):
        v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
        x = x.upper().replace('LLL', 'LII')
        n = 0
        for a, b in zip(x, x[1:] + ' '):
            if a not in v:
                return None
            n += -v[a] if b in v and v[b] > v[a] else v[a]
        return n
    heads = [(m.start(), rom(m.group(1))) for m in re.finditer(r'C\s*h\s*a\s*p\s*t\s*e\s*r\s+([IVXLCl]+)\s*\.', s)]
    lo = next((pos for pos, n in heads if n == chs[0]), None)
    hi = next((pos for pos, n in heads if n == chs[-1] + 1 and lo is not None and pos > lo), None)
    if lo is None:
        return '(the OCR has no heading for chapter %d here — find it by reading on from the previous chapter)' % chs[0]
    return s[lo:hi if hi else lo + 12000]


def establish_packet(p):
    chs = chapters(p)
    leaf = start_leaf(p)
    ocr = _ocr_segment(os.path.join(HERE, 'source', 'raw', 'haug1872-text-ocr.txt'), chs)
    return f"""# Establish — {p['id']}: chapters {chs[0]}–{chs[-1]} of Haug & West 1872

The pages are in source/pages/n<leaf>.jpg (leaf = printed page + 101). Each page has, top to bottom: the
Pahlavi text in Pahlavi type with small sentence numbers inside the lines; a rule; Haug's Roman reading of the
same sentences, numbered the same way; the manuscript variants in small type. The running head names the
chapter and sentences on the page ("Ardâ-Vîrâf IV. 12–30"); a new chapter has a centred heading "Chapter N."
in both the Pahlavi block and the Roman block.

The print numbers its chapters in Roman numerals (Chapter II., Chapter XLV.). This part starts at the heading for
chapter {chs[0]}, on or just after leaf n{leaf}, and ends with the last sentence of chapter {chs[-1]} (the line before the
heading for chapter {chs[-1] + 1}{' — chapter 101 is the last; the text ends on about leaf n237' if chs[-1] == 101 else ''}).

You write two files and then pin them (`python3 ../run3/r3.py pin arda-wiraz {p['id']}`).

## 1. source/established/{p['id']}.txt — Haug's Roman reading
Read the Roman block of each page from the image (Read the page file; crop and enlarge with Pillow where a
letter is unclear). The OCR below is a help for the words only: its accents are wrong almost everywhere, so
every letter with a mark (â ê î ô û, ŏ, ḍ, sh, ch, kh) comes from the image. Copy exactly what Haug prints,
including his hyphens and his -i; words he sets in italics (not in all his manuscripts) are copied without any
mark. Leave out the variants at the foot.
Format, one sentence per line:
    # label: Chapters {chs[0]}–{chs[-1]} · <six words or fewer saying what happens, in plain English>
    # leaves: <first leaf>-<last leaf>
    {chs[0]}.1<TAB>Va akhar …
    {chs[0]}.2<TAB>…
The label is what the reader sees in the library, so make it say what is in these chapters (for the hell
chapters: whose punishment, e.g. "Chapters 24–27 · Hell: false measures, bad rulers, the slanderer").

## 2. source/established/{p['id']}.cut.json — where each sentence's Pahlavi sits
`python3 tools/sheet.py <leaf> …` writes numbered sheets to drafts/_sheets/ (one strip per printed line, L0 at
the top; the word shapes of each line boxed and numbered from the RIGHT, 0 first). Read them and write:
    {{"leaves": {{"{leaf}": {{"lines": [6, 7], "num": {{"6,0": "{chs[0]}.1", "7,4": "{chs[0]}.2"}}, "drop": ["7,9"]}},
                 "{(leaf or 0) + 1}": {{"lines": [0, 1, 2, 3, 4, 5, 6, 7], "num": {{…}}, "drop": [...]}}}}}}
- "lines": the strips that are Pahlavi text of THIS part, in order. Leave out: the heading lines "Chapter N.",
  the Roman lines, the footnotes, and on the first and last leaf the lines of the neighbouring chapters.
- "num": every small sentence number in those lines, as "line,shape": "chapter.sentence". A sentence's shapes
  are everything from its number to the next number, across line and page ends.
- "drop": shapes that are not words: the small rings (o) the print sets before some numbers, and the
  ornament (⁘) at the end of a paragraph.
If a number is fused in one box with a word, or a word is split in a way that hides a number, do not guess:
put the sentence id on the nearest box, say so in LOG.md, and go on.
The pin checks that the numbers in the cut file are exactly the sentences of the .txt, in order.

## OCR of the Roman text for these chapters (words only; accents unreliable)
{ocr}
"""


def _cut_sequence(p):
    """-> [(sentence id, leaf, base, block)] in reading order; raises ValueError with a plain message."""
    import pagelib
    doc = R.jload(cut_path(p))
    spec = doc['leaves']
    seq, cur, seen = [], None, []
    for e in doc.get('pre', []):           # a line the detector does not find (the invocation above chapter 1)
        seen.append(e['id'])
        d0 = pagelib.detect(int(e['leaf']))
        seq += [(e['id'], int(e['leaf']), e['base'], blk, d0['x0']) for blk in e['blocks']]
    for leaf in sorted(spec, key=int):
        d = pagelib.detect(int(leaf))
        e = spec[leaf]
        num = {tuple(int(x) for x in k.split(',')): v for k, v in e.get('num', {}).items()}
        drop = {tuple(int(x) for x in k.split(',')) for k in e.get('drop', [])}
        for li in e['lines']:
            if li >= len(d['lines']):
                raise ValueError(f'leaf {leaf}: no line {li} (the page has {len(d["lines"])})')
            for j, b in enumerate(d['lines'][li]['blocks']):
                if (li, j) in num:
                    cur = num[(li, j)]
                    seen.append(cur)
                    continue
                if (li, j) in drop:
                    continue
                if cur is None:
                    raise ValueError(f'leaf {leaf} line {li}: word shapes before the first sentence number')
                seq.append((cur, int(leaf), d['lines'][li]['base'], b, d['x0']))
        for (li, j) in list(num) + list(drop):
            if li not in e['lines'] or li >= len(d['lines']) or j >= len(d['lines'][li]['blocks']):
                raise ValueError(f'leaf {leaf}: {li},{j} is not a shape of a listed line')
    return seq, seen


def check_established(p):
    errs = []
    for f in (est_path(p), cut_path(p)):
        if not os.path.exists(f):
            errs.append(f'{os.path.relpath(f, R.ROOT)} does not exist')
    if errs:
        return errs
    label, leaves = header(p, 'label'), header(p, 'leaves')
    if not label or len(label) > 90 or '·' not in label:
        errs.append('the .txt needs "# label: Chapters a–b · <what happens>" (90 characters at most)')
    m = re.fullmatch(r'(\d+)\s*-\s*(\d+)', leaves or '')
    if not m:
        errs.append('the .txt needs "# leaves: <first>-<last>"')
    sents = sentences(p)
    ids = [a for a, _ in sents]
    want_ch = chapters(p)
    got_ch = []
    for a in ids:
        c = int(a.split('.')[0])
        if c not in got_ch:
            got_ch.append(c)
    if got_ch != want_ch:
        errs.append(f'chapters in the .txt are {got_ch}; the part is chapters {want_ch}')
    for c in got_ch:
        ns = [int(a.split('.')[1]) for a in ids if int(a.split('.')[0]) == c]
        if ns != list(range(ns[0], ns[0] + len(ns))) or ns[0] not in (0, 1):
            errs.append(f'chapter {c}: sentence numbers are not 1…{len(ns)} in order: {ns[:12]}…')
    for a, t in sents:
        if len(t) < 3 or re.search(r'[§¶{}|<>^&*#@=~_]|\d', re.sub(r'\b[IVXLC]+\b', '', t)):
            errs.append(f'{a}: OCR debris or a stray digit in the Roman text: {t[:60]!r}')
    try:
        seq, seen = _cut_sequence(p)
        if seen != ids:
            k = next((i for i in range(min(len(seen), len(ids))) if seen[i] != ids[i]), min(len(seen), len(ids)))
            errs.append(f'cut file numbers do not match the .txt at position {k}: cut {seen[k:k+3]} vs text {ids[k:k+3]} '
                        f'({len(seen)} numbers, {len(ids)} sentences)')
        counts = {}
        for s in seq:
            counts[s[0]] = counts.get(s[0], 0) + 1
        for a, t in sents:
            n, w = counts.get(a, 0), len(t.split())
            if n == 0:
                errs.append(f'{a}: no word shapes between its number and the next')
            elif n > 2.2 * w + 3 or n < 0.4 * w - 2:
                errs.append(f'{a}: {n} word shapes for {w} Roman words — a number is misplaced nearby')
    except ValueError as e:
        errs.append(str(e))
    except Exception as e:                      # numpy / Pillow missing, unreadable page …
        errs.append(f'the cut could not be checked: {e!r}')
    if not errs:
        p['name'] = label
        p['leaves'] = [int(m.group(1)), int(m.group(2))]
        p['cite'] = f'pp. {int(m.group(1)) - 101}–{int(m.group(2)) - 101}'
    return errs


def written(forms):
    out = []
    for f in forms:
        if re.fullmatch(r'\d+', f):
            out.append('the figure ' + f)
        elif any(c.isupper() for c in f):
            out.append(f + (' (Aramaic word-sign with Persian ending)' if any(c.islower() for c in f) else ' (Aramaic word-sign)'))
        else:
            out.append(f)
    return ' · Written ' + ', also '.join(out) + '.'


def reader_glossary(base, spell):
    return {k: base[k] + written(spell[k]) for k in sorted(base) if k in spell}


def packet(p):
    sents = sentences(p)
    base, spell = R.jload(BASE), R.jload(SPELL)
    eng = _ocr_segment(os.path.join(HERE, 'source', 'raw', 'haug1872-english-ocr.txt'), chapters(p))
    out = [f'# Packet — {p["id"]}: {p.get("name", "")}', '',
           f'Leaves n{p["leaves"][0]}–n{p["leaves"][1]} (source/pages/). Haug\'s Roman reading, pinned, one sentence per line. '
           'It tells you which word-sign or spelling stands behind each word; `t` (the words as read) and `w` (the letters as '
           'written) are yours to write from it, by conventions.md. Where a spelling is in doubt, look at the Pahlavi type on the page.', '']
    out += [f'{a}\t{t}' for a, t in sents]
    out += ['', '## Spellings already settled (form as read ← letters as written). Use these; do not respell a known word.', '']
    out += [f'{k} ← {" / ".join(v)}' for k, v in sorted(spell.items())]
    out += ['', '## Haug\'s 1872 English for these chapters (OCR). A check on the sense only. Never take wording from it; '
            'it is also out of date in places (see conventions.md, "Haug\'s readings and later corrections").', '', eng, '']
    out += ['## Glossary forms already entered', '', ', '.join(sorted(base))]
    return '\n'.join(out) + '\n'


def _number(p):
    return re.search(r'(\d+)$', p['id']).group(1)


def assemble(p, units, gloss):
    import pagelib
    cfg = R.work_cfg(W)
    base, spell = R.jload(BASE), R.jload(SPELL)
    broaden = gloss.pop('__broaden__', {}) if isinstance(gloss, dict) else {}
    for k, v in gloss.items():
        if v and k not in base:
            base[k] = v
    base.update(broaden)
    seq, _ = _cut_sequence(p)
    by = {}
    for s in seq:
        by.setdefault(s[0], []).append(s)
    nnn = _number(p)
    outdir = os.path.join(IMG, nnn)
    os.makedirs(outdir, exist_ok=True)
    for f in os.listdir(outdir):
        os.remove(os.path.join(outdir, f))
    pages = {}
    sents = []
    for u, x in enumerate(units['sentences']):
        toks = R.WORD_RE.findall(x['t'])
        wr = x['w'].split()
        s = {'t': x['t'], 'wr': wr, 'l': x['l'], 'hs': x['sents']}
        if not x['sents'][0].endswith('.0'):          # the invocation above chapter 1 has no number
            s['ln'] = x['sents'][0]
        for f in ('i', 'n'):
            if x.get(f):
                s[f] = x[f]
        if x.get('p'):
            s['p'] = True
        files = []
        for sid in x['sents']:
            for (_, leaf, basey, b, x0) in by.get(sid, []):
                if leaf not in pages:
                    pages[leaf] = pagelib.page(leaf)
                im = pagelib.cut(pages[leaf], x0, basey, b)
                if im is None:
                    continue
                fn = f'u{u:02d}-{len(files):02d}.png'
                im.save(os.path.join(outdir, fn), optimize=True)
                files.append({'f': fn, 'w': im.size[0], 'h': im.size[1]})
        s['img'] = files
        sents.append(s)
        if len(toks) == len(wr):
            for a, b in zip(toks, wr):
                spell.setdefault(a.lower(), [])
                if b not in spell[a.lower()]:
                    spell[a.lower()].append(b)
    name = p['name']
    story = dict(cfg['header'])
    story.update({'id': p['id'], 'title': cfg['title'], 'titleEn': f'{cfg["workEn_short"]} — {name}', 'part': name,
                  'numbering': 'clause', 'glossaryFile': 'arda-wiraz-glossary.json', 'imgBase': f'img/arda-wiraz/{nnn}/',
                  'source': cfg['sourceStatement'].replace('{cite}', p.get('cite', '')),
                  'about': units.get('about') or cfg['about'], 'sentences': sents})
    if units.get('advisory'):
        story['advisory'] = units['advisory']
    return story, {GLOSS: reader_glossary(base, spell), BASE: base, SPELL: spell}


def validate(p, story):
    errs, warns = [], []
    ids = [a for a, _ in sentences(p)]
    got = [h for s in story['sentences'] for h in s.get('hs', [])]
    if got != ids:
        k = next((i for i in range(min(len(got), len(ids))) if got[i] != ids[i]), min(len(got), len(ids)))
        errs.append(f'the units do not cover the established sentences in order at position {k}: units {got[k:k+3]} vs text {ids[k:k+3]}')
    g = R.jload(GLOSS)
    miss = R.glossary_coverage(story, g)
    if miss:
        errs.append(f'{len(miss)} forms have no glossary entry: {miss[:20]}')
    nnn = _number(p)
    for k, s in enumerate(story['sentences']):
        toks = R.WORD_RE.findall(s['t'])
        wr = s.get('wr') or []
        if len(toks) != len(wr):
            errs.append(f'unit {k}: {len(toks)} words in t but {len(wr)} in w — they must pair one to one')
        if not T_OK.match(s['t']):
            bad = sorted(set(c for c in s['t'] if not T_OK.match(c)))
            errs.append(f'unit {k}: t has characters outside the transcription alphabet: {bad}')
        for f in wr:
            if set(f) - WR_OK:
                errs.append(f'unit {k}: w form {f!r} has characters outside the transliteration alphabet: {sorted(set(f) - WR_OK)}')
        if s.get('ln') != (s.get('hs') or [None])[0] and not (s.get('ln') is None and (s.get('hs') or [''])[0].endswith('.0')):
            errs.append(f'unit {k}: ln must be the unit\'s first sentence id')
        im = s.get('img') or []
        if not im:
            errs.append(f'unit {k}: no print images')
        for x in im:
            if not os.path.exists(os.path.join(IMG, nnn, x['f'])):
                errs.append(f'unit {k}: image {x["f"]} is missing')
        if im and (len(im) > 1.8 * len(toks) + 3 or len(im) < 0.5 * len(toks) - 2):
            warns.append(f'unit {k}: {len(im)} print shapes for {len(toks)} words — check the unit\'s sentences against the cut')
        if len(toks) > 45:
            warns.append(f'unit {k}: {len(toks)} words — cut at the strongest pause')
        if not s.get('i'):
            warns.append(f'unit {k}: no idiomatic English')
    return errs, warns
