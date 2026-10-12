"""Shared cuneiform helpers for Run 3 (Hammurabi, Sumerian King List).

Glyph characters are never typed by a drafter. A glyph names its sign by its key in signs-cuneiform.json and
the build copies that entry's glyph; a numeral whose character varies with its count (NUMERIC SIGN EIGHT
SHAR2) also gives `u`, the exact Unicode character name, and the build takes the character from Python's
unicodedata. A sign missing from the glossary is added with run3/signs.py (which also updates the copy
embedded in the reader), never by hand."""
import difflib, os, re, sys, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r3lib as R

SIGNS = os.path.join(R.ROOT, 'signs-cuneiform.json')


def signs():
    return R.jload(SIGNS)['signs']


def fill_glyph(g, S, where, problems):
    key = g.get('sign')
    if key not in S:
        problems.append(f'{where}: sign {key!r} is not in signs-cuneiform.json — add it with run3/signs.py')
        return None
    if g.get('u'):
        try:
            ch = unicodedata.lookup(g['u'])
        except KeyError:
            problems.append(f'{where}: no Unicode character named {g["u"]!r}')
            return None
    else:
        ch = S[key]['glyph']
    ng = {'s': ch, 'sign': key, 'role': g['role'], 'tr': g.get('tr', '')}
    if 'val' in g:
        ng['val'] = g['val']
    for f in ('nl', 'u'):
        if g.get(f):
            ng[f] = g[f]
    return ng


def fill_words(u, S, G, k, problems):
    words = []
    for j, w in enumerate(u['words']):
        gl = [x for x in (fill_glyph(g, S, f'unit {k} word {j}', problems) for g in w['glyphs']) if x]
        nw = {'reading': w['reading'], 'say': w.get('say', ''), 'glyphs': gl,
              'morph': [{'lemma': m['lemma'], 'gloss': m.get('gloss') or G.get(m['lemma'], ''), 'g': m['g']}
                        for m in w.get('morph', [])]}
        if w.get('nl'):
            nw['nl'] = True
        words.append(nw)
    return words


def build_t(words):
    t = ''
    for i, w in enumerate(words):
        ws = ''
        for g in w['glyphs']:
            ws += ('\n' if g.get('nl') and ws else '') + g['s']
        t += ('' if i == 0 else ('\n' if w.get('nl') else ' ')) + ws
    return t


def lines_tr(s):
    """The unit's transliteration, one string per written line (determinatives left out)."""
    lines = [[]]
    for wi, w in enumerate(s['words']):
        if wi and w.get('nl'):
            lines.append([])
        for gi, g in enumerate(w['glyphs']):
            if gi and g.get('nl'):
                lines.append([])
            if g['role'] != 'det':
                lines[-1].append(g['tr'])
    return [''.join(x) for x in lines]


def skeleton(s):
    s = (s or '').lower().replace('ḳ', 'q')  # before NFD, which would split ḳ into k + dot
    s = unicodedata.normalize('NFD', s)
    s = re.sub(r'\{[^}]*\}|\([^)]*\)', '', s)
    s = ''.join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r'[₀-₉0-9]', '', s)
    return re.sub(r'[^a-zšṣṭḫqĝʾ]', '', s)


def ratio(a, b):
    return difflib.SequenceMatcher(None, skeleton(a), skeleton(b)).ratio()


def glyph_checks(story, S):
    errs, warns = [], []
    for k, s in enumerate(story['sentences']):
        for j, w in enumerate(s['words']):
            for g in w['glyphs']:
                if g.get('u'):
                    if unicodedata.name(g['s'], '') != g['u']:
                        errs.append(f'unit {k} word {j}: glyph is not {g["u"]}')
                elif g['s'] != S.get(g['sign'], {}).get('glyph'):
                    errs.append(f'unit {k} word {j}: glyph does not match the sign glossary for {g["sign"]}')
            if not w.get('say'):
                errs.append(f'unit {k} word {j}: no say')
            for m in w['morph']:
                if not m['gloss']:
                    errs.append(f'unit {k} word {j}: lemma {m["lemma"]!r} has no gloss')
        if 'ln' in s and not isinstance(s['ln'], int):
            errs.append(f'unit {k}: ln must be an integer')
        if story.get('numbering') == 'line' and not isinstance(s.get('ln'), int):
            errs.append(f'unit {k}: needs ln (the line number)')
        if story.get('numbering') == 'clause' and s.get('p') and not isinstance(s.get('ln'), int):
            errs.append(f'unit {k}: the first unit of a law needs ln (the law number)')
    return errs, warns
