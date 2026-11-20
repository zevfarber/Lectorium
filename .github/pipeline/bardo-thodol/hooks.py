"""Bar do thos grol chen mo — work hooks for .github/pipeline/run3/r3.py (set up 2026-11-20 for the shared
text pipeline).

Words model, Classical Tibetan, as in the pilot bardo-thodol-001 (2026-11-16; its build.py, units.py,
glossary.py are kept here as the model). Every part takes two firings: ACTION establish reads the print, line
by line, into source/established/<id>.txt; ACTION draft divides it into words and translates it.

Established file format (UTF-8), the format of source/w23710-pp09-17.txt plus header lines:
    # name: <short English name of what this stretch says, for the library>
    # pages: pp. A–B
    # fix: <as printed> => <as the text gives it>      (zero or more: line-end abbreviations written out,
                                                          clear misprints, a tsheg missing at a line join)
    {18}
    <one line of the print per line>
    ...
`[?]` after a syllable marks a doubtful reading. Every `# fix:` that is a misprint must be named in a note.

Draft (drafts/<id>/units.json):
    {"about": "...", "sentences": [{"w": "<the text divided into words; ' / ' = a verse-line break>",
                                    "l": "...", "i": "...", "n": "...", "p": 1?, "v": 1?}]}
The units' letters must equal the established text's letters, after the fixes, exactly."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'run3'))
sys.path.insert(0, HERE)
import r3lib as R

EST = os.path.join(HERE, 'source', 'established')
GLOSS = os.path.join(HERE, 'glossary.json')        # the work's master glossary: word key -> meaning
DEFAULT_FIXES = [('༄༅༔ ༔', ''), ('༄༅༔', ''), ('[?]', '')]
PILOT_END = ('…ཞེས་ཕྱི་དབུགས་མ་ཆད་པའི་གོང་ནས་རྣ་བར་ལན་མང་དུ་བཤད་ལ་ཡིད་ལ་འཇགས་སུ་བཅུག་གོ༔ — the pilot (bardo-thodol-001) ends '
             'there, on the last line of p. 17 (leaf n18). bardo-thodol-002 begins with the next words, དེ་ནས་ at the end of '
             'that line: start the established file with {17} and that line-end fragment, then {18}.')


def tib():
    import tib as T                     # needs pyewts: pip install pyewts
    return T


def est_path(p):
    return os.path.join(EST, p['id'] + '.txt')


def _lines(p):
    return open(est_path(p), encoding='utf-8').read().split('\n')


def header(p):
    h, fixes = {}, []
    for line in _lines(p):
        m = re.match(r'#\s*(name|pages)\s*:\s*(.+)', line)
        if m:
            h[m.group(1)] = m.group(2).strip()
        m = re.match(r'#\s*fix\s*:\s*(.+?)\s*=>\s*(.*)$', line)
        if m:
            fixes.append((m.group(1).strip(), m.group(2).strip()))
    h['fixes'] = fixes
    return h


def print_lines(p):
    return [l for l in _lines(p) if l.strip() and not l.startswith('#') and not re.fullmatch(r'\{\d+\}', l.strip())]


def letters(p):
    """The established text as one letter stream: lines joined, spaces gone, the fixes applied."""
    s = ''.join(l.strip() for l in print_lines(p)).replace(' ', '')
    for a, b in DEFAULT_FIXES + header(p)['fixes']:
        s = s.replace(a.replace(' ', ''), b.replace(' ', ''))
    return s


def slice_source(p):
    if not os.path.exists(est_path(p)):
        return None
    return open(est_path(p), encoding='utf-8').read().strip()


def _previous(p):
    ps = R.parts_doc('bardo-thodol')['parts']
    i = [q['id'] for q in ps].index(p['id'])
    return ps[i - 1] if i else None


def establish_packet(p):
    prev = _previous(p)
    if prev is None:
        start = PILOT_END
    else:
        tail = letters(prev)[-60:] if os.path.exists(est_path(prev)) else '(not found)'
        start = f'…{tail} — the end of {prev["id"]}; begin with what follows (if that is mid-line, start the file with that page\'s {{N}} and the rest of the line)'
    leaves = ', '.join(f'source/pages/n{q + 1}.jpg' for q in range(p['first_page'], min(p['last_page'] + 1, 121) + 1) if q != 80)
    if p['last_page'] in (80, 121):
        leaves += f' (p. {p["last_page"]} is the last page of text {p.get("text")}: the part ends where the text ends)'
    return f"""# Establish — {p['id']} ({p['pages']} of the reproduction)

Read `conventions.md` first ("Text of record", "What the page shows", "The print's readings").
`pip install pyewts` if `python3 -c "import pyewts"` fails (it is needed for the draft and the build).

Start: {start}
Pages: {leaves} (page p is leaf n(p+1); the last one only to finish a sentence that runs over the edge of
p. {p['last_page']}).

Procedure (the image decides every letter):
1. Read each page line by line, enlarging (crop one line at a time and scale ×3; ×5 for a doubtful syllable).
   Write each print line as one line of the file, under a {{page}} marker, exactly as printed: tsheg, ༔ and །
   where the print has them, the line-end abbreviations as printed (པའཾ, ལཾ), the opening ornament ༄༅༔ ༔ if
   a page begins with it. Put `[?]` after any syllable you are not sure of.
2. Check your reading against the dzogchengonpa.org transcription of this same print and the bo.wikipedia.org
   text of another print if this sandbox can reach them; they find your place and flag a misread syllable, but
   the image decides. If they cannot be reached, say so in the log and read with extra care.
3. Stop at the last ༔ or ། that closes a sentence on p. {p['last_page']}, or finish the sentence from the next page.
4. Add `# fix:` lines for what the text will give differently from the print: each line-end abbreviation
   written out (`# fix: པའཾ => པའམ`), a tsheg missing where two print lines join (`# fix: རྣམསབར => རྣམས་བར`),
   and a clear misprint (README rule 5b; the note must name it). Nothing else.
5. Log every doubtful reading, every misprint, every place the other print differs in sense, in
   `drafts/{p['id']}/establish-log.md`; the drafter turns them into notes.
6. Write `source/established/{p['id']}.txt` with the header lines `# name:` (a short English name for the
   library: what this stretch says, e.g. "The second bardo: when the clear light is not recognised") and
   `# pages: {p['pages']}` (adjusted if it ran over), the `# fix:` lines, then the page-marked lines. Pin it:
   `python3 ../run3/r3.py pin bardo-thodol {p['id']}`.
"""


def check_established(p):
    errs = []
    if not os.path.exists(est_path(p)):
        return [f'{os.path.relpath(est_path(p), R.ROOT)} does not exist']
    h = header(p)
    for k in ('name', 'pages'):
        if not h.get(k):
            errs.append(f'the header line "# {k}:" is missing or empty')
    s = letters(p)
    if len(s) < 1500:
        errs.append(f'only {len(s)} letters — nine pages of this print hold far more; is the whole part there?')
    bad = sorted({c for c in s if not ('ༀ' <= c <= '࿿')})
    if bad:
        errs.append(f'characters outside the Tibetan block in the text: {bad[:10]}')
    if not re.search(r'\{\d+\}', open(est_path(p), encoding='utf-8').read()):
        errs.append('no {page} markers')
    if not errs:
        p['name'] = h['name']
        p['part'] = h['name']
        p['cite'] = h['pages']
    return errs


def packet(p):
    h = header(p)
    out = [f'# Packet — {p["id"]}: {h.get("name", "")} ({h.get("pages", "")})', '',
           'The established print, line by line (pinned). The fixes below are applied by the build: the units\' `w` '
           'must give the text AFTER them (abbreviations written out, misprints corrected), letter for letter.', '',
           'Fixes: ' + ('; '.join(f'{a} → {b}' for a, b in h['fixes']) or 'none') + ' (and always: the ornament ༄༅༔ ༔ and [?] marks are dropped).', '',
           '```', slice_source(p), '```', '',
           'Model: `../../../bardo-thodol-001.json` and `units.py` (the pilot\'s units: its `w` division, `l`/`i` register, '
           'note density). Glossary: `glossary.json` here (word key -> meaning); `novel-forms.json` lists the words of this '
           'part not yet in it — but the word division is the drafter\'s, so the glosser works from units.json, not from '
           'that list alone.', '']
    log = os.path.join(R.drafts('bardo-thodol', p['id']), 'establish-log.md')
    if os.path.exists(log):
        out += ['## Establishment log (doubtful readings, misprints, other-print differences — the notes must say so)', '',
                open(log, encoding='utf-8').read()]
    return '\n'.join(out) + '\n'


def forms(p):
    """Syllables are known, words are not until the drafter divides them; report the drafted words if a draft
    exists, else nothing (the glosser runs after the drafter)."""
    G = R.jload(GLOSS)
    up = os.path.join(R.drafts('bardo-thodol', p['id']), 'units.json')
    novel, known = {}, {}
    if os.path.exists(up):
        T = tib()
        for u in R.jload(up)['sentences']:
            for tok in u['w'].split():
                if tok == '/' or all(c in T.PUNCT for c in tok):
                    continue
                key = T.word(tok)[0]
                (known if key in G else novel)[key] = G.get(key, '')
    return novel, known


def assemble(p, units, gloss):
    cfg = R.work_cfg('bardo-thodol')
    T = tib()
    G = R.jload(GLOSS)
    broaden = gloss.pop('__broaden__', {}) if isinstance(gloss, dict) else {}
    for k, v in gloss.items():
        if v and k not in G:
            G[k] = v
    G.update(broaden)
    h = header(p)
    sents, used = [], {}
    for u in units['sentences']:
        words, t, br, lead = [], '', False, ''
        for tok in u['w'].split():
            if tok == '/':
                br = True
                t = t.rstrip(' ') + '\n'
                continue
            if all(c in T.PUNCT for c in tok):
                lead = tok + ' '
                t += tok + ' '
                continue
            key, glyphs, reading, say = T.word(tok)
            used[key] = reading
            if lead:
                glyphs.insert(0, {'s': lead.strip(), 'tr': ' ', 'role': 'punct'})
                lead = ''
            w = {'reading': reading, 'say': say, 'glyphs': glyphs,
                 'morph': [{'lemma': reading, 'gloss': G.get(key, ''),
                            'g': [i for i, g in enumerate(glyphs) if g.get('role') != 'punct']}]}
            if br:
                w['br'] = True
                br = False
            words.append(w)
            t += tok + (' ' if tok[-1] in T.PUNCT else '')
        d = {'t': t.strip(), 'words': words, 'l': u['l']}
        for k in ('i', 'n'):
            if u.get(k):
                d[k] = u[k]
        if u.get('p'):
            d['p'] = True
        if u.get('v'):
            d['v'] = True
        sents.append(d)
    story = dict(cfg['header'])
    story.update({'id': p['id'], 'title': 'བར་དོ་ཐོས་གྲོལ་ཆེན་མོ།', 'titleRead': 'Bardo Thödröl Chenmo',
                  'titleEn': f'The Tibetan Book of the Dead — {h.get("name", "")}',
                  'part': f'{p["seq"]} · {h.get("name", "")}', 'provisional': True,
                  'draftNote': 'Read from one blockprint at the resolution of an online scan; doubtful places are marked in the notes, and the text has not yet been collated with other prints.',
                  'source': cfg['sourceStatement'].replace('{textname}', p.get('textname', '')).replace('{text}', p.get('text', ''))
                            .replace('{pages}', 'pages ' + h.get('pages', '').replace('pp. ', '') + ' of the reproduction'),
                  'sentences': sents,
                  'glossary': {k: used[k] + ' — ' + G[k] for k in sorted(used) if k in G}})
    if units.get('about'):
        story['about'] = units['about']
    return story, {GLOSS: G}


def validate(p, story):
    errs, warns = [], []
    T = tib()
    G = R.jload(GLOSS)
    mine = ''.join(s['t'] for s in story['sentences']).replace(' ', '').replace('\n', '')
    want = letters(p)
    if mine != want:
        i = next((k for k in range(min(len(mine), len(want))) if mine[k] != want[k]), min(len(mine), len(want)))
        errs.append(f'units differ from the established text (after its fixes) at letter {i}: units {mine[i:i+20]!r} vs text {want[i:i+20]!r}')
    for k, s in enumerate(story['sentences']):
        if ''.join(g['s'] for w in s['words'] for g in w['glyphs']) != s['t'].replace(' ', '').replace('\n', ''):
            errs.append(f'unit {k}: glyphs do not rebuild t')
        if s.get('v') and s['t'].count('\n') != s['l'].count('\n'):
            errs.append(f'unit {k}: verse lines in t and l differ')
        for w in s['words']:
            key = T.TSHEG.join(x['s'].rstrip(T.TSHEG) for x in w['glyphs'] if x.get('role') != 'punct')
            if key not in G:
                errs.append(f'unit {k}: no glossary entry for {key} ({w["reading"]})')
        if not s.get('i'):
            warns.append(f'unit {k}: no idiomatic English (the pilot gives i on every unit)')
    if not any(s.get('p') for s in story['sentences']):
        errs.append('no unit starts a paragraph (the first unit of a part always does)')
    if not story.get('about'):
        warns.append('no about (a short paragraph on what this part says, as the pilot has)')
    return errs, warns
