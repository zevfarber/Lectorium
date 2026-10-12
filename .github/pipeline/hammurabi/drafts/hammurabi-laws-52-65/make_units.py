# -*- coding: utf-8 -*-
"""Build units.json for hammurabi-laws-52-65 from Harper's lines in packet.md.

The transliteration is never retyped: each stele line is cut from packet.md, Harper's normalised logogram
words (eḳlim, šeʾam, kirêm ...) are replaced by the sign groups the plates show (LOGO below), syllables are
mapped to sign keys (SYL), and the drafter's annotations (say, morph, l, i, n) are attached unit by unit
from units_text.py. Run:  python make_units.py
"""
import json, os, re, sys, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', '..'))
sys.path.insert(0, HERE)
from units_text import UNITS, NEWG, TITLE_EN, PART, ABOUT  # noqa: E402

# ---------------------------------------------------------------- Harper's lines
def packet_lines():
    out = []
    for ln in open(os.path.join(HERE, 'packet.md'), encoding='utf-8'):
        m = re.match(r'^(XV|XVI) (\d+)\t(.*)$', ln.rstrip('\n'))
        if m:
            out.append((m.group(1), int(m.group(2)), m.group(3)))
    return out

# ---------------------------------------------------------------- syllable -> sign key
SYL = {
    'a': 'A', 'ab': 'AB', 'ad': 'AD', 'aḫ': 'AH', 'ak': 'AK', 'am': 'AM', 'an': 'AN', 'ar': 'AR', 'at': 'AD',
    'ba': 'BA', 'be': 'BAD', 'bi': 'BI', 'bil': 'BIL',
    'da': 'DA', 'dan': 'KAL', 'di': 'DI', 'du': 'DU',
    'e': 'E', 'el': 'EL', 'eš': 'ESH',
    'ga': 'GA', 'gar': 'GAR',
    'ḫa': 'HA', 'ḫal': 'HAL',
    'i': 'I', 'ib': 'IB', 'id': 'A2', 'ig': 'IG', 'ik': 'IG', 'il': 'IL', 'im': 'IM', 'in': 'IN', 'ip': 'IB',
    'ir': 'IR', 'is': 'GISH', 'iš': 'ISH', 'iṣ': 'GISH', 'it': 'A2', 'iz': 'GISH',
    'ka': 'KA', 'ki': 'KI', 'ku': 'KU',
    'ḳal': 'GAL', 'ḳi': 'KI', 'ḳu': 'KU',
    'la': 'LA', 'li': 'LI', 'lim': 'IGI', 'lu': 'LU', 'lum': 'LUM',
    'ma': 'MA', 'me': 'ME', 'mi': 'MI', 'mu': 'MU', 'mur': 'HAR',
    'na': 'NA', 'ni': 'NI', 'nim': 'NIM', 'nu': 'NU',
    'pa': 'PA', 'ra': 'RA', 'ri': 'RI', 'ru': 'RU',
    'sa': 'SA',
    'ša': 'SHA', 'še': 'SHE', 'ši': 'IGI', 'šu': 'SHU', 'šum': 'TAG',
    'ṣa': 'ZA', 'ṣi': 'ZI',
    'ta': 'TA', 'tab': 'TAB', 'tap': 'TAB', 'tam': 'UD', 'te': 'TE', 'ti': 'TI', 'tim': 'TIM', 'tu': 'TU',
    'tum': 'TUM',
    'u': 'U2', 'ub': 'UB', 'ul': 'UL', 'um': 'UM', 'un': 'KALAM', 'up': 'UB', 'uš': 'USH', 'uz': 'UZ3',
    'wi': 'PI', 'za': 'ZA', 'zi': 'ZI', 'zu': 'ZU',
}

def L(key, tr, val=''):
    return {'sign': key, 'role': 'log', 'tr': tr, 'val': val}

def D(key):
    return {'sign': key, 'role': 'det', 'tr': ''}

def P(key, tr):
    return {'sign': key, 'role': 'phon', 'tr': tr}

def C(key, tr):
    return {'sign': key, 'role': 'comp', 'tr': tr}

def N(key, tr, u=None):
    g = {'sign': key, 'role': 'log', 'tr': tr, 'val': tr}
    if u:
        g['u'] = u
    return g

ASA = lambda: [L('A', 'A', 'eqlum'), L('SHA3', 'ŠÀ')]
KIRI = lambda: [D('GISH'), L('SAR', 'KIRI₆', 'kirûm')]
SENE = lambda: [L('U8', 'U₈', 'ṣēnum'), L('LU', 'UDU'), D('HI'), D('A')]

# Harper's word (after {b} is dropped) -> (reading, glyphs) as the plate shows it
LOGO = {
    'eḳlim': ('A.ŠÀ', ASA), 'eḳlam': ('A.ŠÀ', ASA), 'eḳil': ('A.ŠÀ', ASA), 'eḳlum': ('A.ŠÀ', ASA),
    'eḳil-šu': ('A.ŠÀ-šu', lambda: ASA() + [P('SHU', 'šu')]),
    'eḳlu(=a-na)': ('A.ŠÀ(=a-na)', lambda: [L('A', 'A', 'ana'), L('SHA3', 'ŠÀ(=a-na)')]),
    'še-am': ('ŠE-am', lambda: [L('SHE', 'ŠE', 'šeʾum'), C('AM', 'am')]),
    'šeʾam': ('ŠE', lambda: [L('SHE', 'ŠE', 'šeʾum')]),
    'šeʾi-šu-nu': ('ŠE-šu-nu', lambda: [L('SHE', 'ŠE', 'šeʾum'), P('SHU', 'šu'), P('NU', 'nu')]),
    'šamaššammam': ('ŠE.GIŠ.Ì', lambda: [L('SHE', 'ŠE', 'šamaššammū'), L('GISH', 'GIŠ'), L('NI', 'Ì')]),
    '[kâri]-šu': ('[KAR]-šu', lambda: [L('KAR', '[KAR]', 'kārum'), P('SHU', 'šu')]),
    'kâri-[šu]': ('KAR-[šu]', lambda: [L('KAR', 'KAR', 'kārum'), P('SHU', '[šu]')]),
    'kâri-šu': ('KAR-šu', lambda: [L('KAR', 'KAR', 'kārum'), P('SHU', 'šu')]),
    'ugaram': ('A.GÀR', lambda: [L('A', 'A', 'ugārum'), L('GAR3', 'GÀR')]),
    'ugarim': ('A.GÀR', lambda: [L('A', 'A', 'ugārum'), L('GAR3', 'GÀR')]),
    'mâr+ugarê': ('DUMU A.GÀR{meš}', lambda: [L('TUR', 'DUMU', 'mārum'), L('A', 'A', 'ugārum'), L('GAR3', 'GÀR'),
                                              D('ME'), D('ESH')]),
    'kaspim': ('KÙ.BABBAR', lambda: [L('KU3', 'KÙ', 'kaspum'), L('UD', 'BABBAR')]),
    'X': ('10', lambda: [N('U', '10')]),
    'XX': ('20', lambda: [N('U', '20', 'CUNEIFORM SIGN U U')]),
    'LX': ('60', lambda: [N('GESH2', '60')]),
    '½': ('1/2', lambda: [N('MASH', '1/2')]),
    'GAN.E': ('GAN₂.E', lambda: [L('GAN2', 'GAN₂', 'būrum'), L('E', 'E')]),
    'ŠE.GUR': ('ŠE.GUR', lambda: [L('SHE', 'ŠE', 'kur šeʾam'), L('GUR', 'GUR')]),
    'rêʾum': ('SIPA', lambda: [L('PA', 'SIPA', 'rēʾûm'), L('LU', '')]),
    'ṣênê': ('U₈.UDU{ḫi.a}', SENE),
    'abullim': ('KÁ.GAL', lambda: [L('KA2', 'KÁ', 'abullum'), L('GAL', 'GAL')]),
    'ebûrim': ('BURU₁₄', lambda: [L('BURU14', 'BURU₁₄', 'ebūrum')]),
    'kirêm': ('{giš}KIRI₆', KIRI), 'kirê': ('{giš}KIRI₆', KIRI), 'kirâm': ('{giš}KIRI₆', KIRI),
    'kirûm': ('{giš}KIRI₆', KIRI),
    'kirâ-šu': ('{giš}KIRI₆-šu', lambda: KIRI() + [P('SHU', 'šu')]),
    'NU.kirêm': ('NU.{giš}KIRI₆', lambda: [L('NU', 'NU', 'nukaribbum'), D('GISH'), L('SAR', 'KIRI₆')]),
    'NU.kirûm': ('NU.{giš}KIRI₆', lambda: [L('NU', 'NU', 'nukaribbum'), D('GISH'), L('SAR', 'KIRI₆')]),
    'šattam_IV{kam}': ('MU 4{kam}', lambda: [L('MU', 'MU', 'šattum'),
                                             N('DISH', '4', 'CUNEIFORM NUMERIC SIGN FOUR DISH'), D('KAM')]),
    'zitti-šu': ('ḪA.LA-šu', lambda: [L('HA', 'ḪA', 'zittum'), L('LA', 'LA'), P('SHU', 'šu')]),
    'abšênum': ('AB.SÍN', lambda: [L('AB', 'AB', 'absinnum'), L('SHE', 'SÍN'), L('NAGA', '')]),
    'bilat': ('GÚN', lambda: [L('GUN', 'GÚN', 'biltum')]),
    'KI.KAL': ('KI.KAL', lambda: [L('KI', 'KI', 'nidûtum'), L('KAL', 'KAL')]),
}

def harper_words(text):
    t = text.replace('{b}', '')
    t = t.replace('ga ma-ar tim', 'ga-ma-ar-tim')       # XV 68: one word on the plate (GA MA AR TIM)
    t = t.replace('NU. kirûm', 'NU.kirûm')
    t = t.replace('šattam IV{kam}', 'šattam_IV{kam}')
    return t.split()

def syllabic(word):
    glyphs = []
    for syl in word.split('-'):
        bare = syl.strip('[]')
        if bare not in SYL:
            raise SystemExit(f'no sign for syllable {syl!r} in {word!r}')
        glyphs.append(P(SYL[bare], syl))
    return word, glyphs

def make_word(hw):
    if hw in LOGO:
        r, f = LOGO[hw]
        return r, f()
    if hw == 'u':
        return 'ù', [P('U3', 'ù')]
    return syllabic(hw)

# ---------------------------------------------------------------- glossary of earlier parts
def earlier_glossary():
    G = {}
    order = ['prologue', 'litany', 'laws-1-10', 'laws-11-25', 'laws-26-41', 'laws-42-51']
    for o in order:
        f = os.path.join(ROOT, f'hammurabi-{o}.json')
        if os.path.exists(f):
            G.update(json.load(open(f, encoding='utf-8')).get('glossary', {}))
    return G

def morph(spec, n, G, where):
    """spec: 'lemma' (all glyphs) or 'lemma:k lemma2:k2 ...' (k glyphs each, in order; '*' = the rest).
    A lemma written lemma@gloss is not split further. Numbers count the glyphs, determinatives included."""
    parts = spec.split('|')
    out, i = [], 0
    for j, p in enumerate(parts):
        p = p.strip()
        m = re.search(r':(\d+|\*)$', p)
        if m:
            lem = p[:m.start()]
            k = n - i if m.group(1) == '*' else int(m.group(1))
        else:
            lem, k = p, (n - i if j == len(parts) - 1 else 1)
        lem = lem.strip()
        idx = list(range(i, i + k))
        i += k
        gl = NEWG.get(lem) or G.get(lem)
        if not gl:
            raise SystemExit(f'{where}: no gloss for lemma {lem!r}')
        out.append({'lemma': lem, 'gloss': gl, 'g': idx})
    if i != n:
        raise SystemExit(f'{where}: morph covers {i} of {n} glyphs ({spec})')
    return out

def build():
    lines = packet_lines()
    pos = {(c, n): k for k, (c, n, _) in enumerate(lines)}
    G = earlier_glossary()
    sentences = []
    for u in UNITS:
        a, b = pos[tuple(u['from'])], pos[tuple(u['to'])]
        words = []
        for k in range(a, b + 1):
            for wi, hw in enumerate(harper_words(lines[k][2])):
                r, gl = make_word(hw)
                w = {'reading': r, 'glyphs': gl}
                if k > a and wi == 0:
                    w['nl'] = True
                words.append(w)
        ann = u['words']
        where = f"unit {u['from']}"
        if len(ann) != len(words):
            raise SystemExit(f"{where}: {len(words)} words on the stone, {len(ann)} annotated: "
                             + ' '.join(w['reading'] for w in words))
        out = []
        for w, (say, spec) in zip(words, ann):
            ow = {'reading': w['reading'], 'say': say, 'glyphs': w['glyphs'],
                  'morph': morph(spec, len(w['glyphs']), G, where + ' ' + w['reading'])}
            if w.get('nl'):
                ow['nl'] = True
            out.append(ow)
        s = {'col': u['from'][0], 'line': u['from'][1]}
        if u.get('ln'):
            s['ln'] = u['ln']
            s['p'] = True
        s.update({'l': u['l'], 'i': u['i'], 'n': u['n'], 'words': out})
        sentences.append(s)
    doc = {'titleEn': TITLE_EN, 'part': PART, 'about': ABOUT, 'sentences': sentences}
    with open(os.path.join(HERE, 'units.json'), 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    print(f'wrote units.json: {len(sentences)} units')

if __name__ == '__main__':
    build()
