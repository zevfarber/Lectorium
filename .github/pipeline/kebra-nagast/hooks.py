"""Kebra Nagast — work hooks for .github/pipeline/run3/r3.py.

Words model with a fully mechanical interlinear: the drafter supplies only the sense-units (t cut from the
source, l, i, n, p) and glosses for the word forms; the per-sign transliteration, the word reading, the
readable `say`, the unit's `tr` and every word's morph are built here from Unicode names and the glossary,
exactly as the pilot kebra-nagast-ch1 was built (kn1_mech.py, 2026-07-23)."""
import glob, json, os, re, sys, unicodedata as ud
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'run3'))
import r3lib as R

SRC = os.path.join(HERE, 'source', 'kebra-nagast-bezold1905.json')
PUNCT = set('፡።፣፤፥፦፧፨')
TERMINAL = set('።፤፨')
VOWELS = [('AA', 'a'), ('EE', 'e'), ('A', 'ä'), ('U', 'u'), ('I', 'i'), ('E', 'ə'), ('O', 'o')]
CONS = {'H': 'h', 'L': 'l', 'HH': 'ḥ', 'M': 'm', 'SZ': 'ś', 'R': 'r', 'S': 's', 'SH': 'š', 'Q': 'q', 'QH': 'q̱',
        'B': 'b', 'V': 'v', 'T': 't', 'C': 'č', 'X': 'ḫ', 'N': 'n', 'NY': 'ñ', 'K': 'k', 'KX': 'ḵ',
        'W': 'w', 'Z': 'z', 'ZH': 'ž', 'Y': 'y', 'D': 'd', 'DD': 'ḍ', 'J': 'ǧ', 'G': 'g',
        'TH': 'ṭ', 'CH': 'č̣', 'PH': 'p̣', 'TS': 'ṣ', 'TZ': 'ṣ́', 'F': 'f', 'P': 'p',
        'GLOTTAL': 'ʾ', 'PHARYNGEAL': 'ʿ'}
DIG = {chr(0x1369 + i): i + 1 for i in range(9)}
TENS = {chr(0x1372 + i): (i + 1) * 10 for i in range(9)}
HUNDRED, MYRIAD = '፻', '፼'
NUMCH = set(DIG) | set(TENS) | {HUNDRED, MYRIAD}


def _src():
    return R.jload(SRC)


def chapter_text(c):
    return '\n'.join(c['paragraphs'])


def slice_source(p):
    src = _src()
    out = []
    for ch in p['chapters']:
        txt = chapter_text(src['chapters'][ch['n'] - 1])
        if 'span' in ch:
            txt = txt[ch['span'][0]:ch['span'][1]].strip()
        out.append(txt)
    return '\n\n'.join(out)


def syl_tr(ch):
    name = ud.name(ch)
    if not name.startswith('ETHIOPIC SYLLABLE '):
        raise ValueError(f'not a syllable: {ch} {name}')
    rest = name[len('ETHIOPIC SYLLABLE '):]
    if ' ' in rest:                                   # GLOTTAL A, PHARYNGEAL AA
        c, v = rest.split(' ', 1)
        return CONS[c] + dict(VOWELS)[v]
    for vt, v in VOWELS:
        if rest.endswith(vt):
            c = rest[:-len(vt)]
            if c in CONS:
                return CONS[c] + v
            if c.endswith('W') and c[:-1] in CONS:    # labiovelars: KWA, QWI, GWE, XWE …
                return CONS[c[:-1]] + 'ʷ' + v
    raise ValueError('no transliteration for ' + name)


def sign_key(ch):
    n = ud.name(ch)
    return n.replace('ETHIOPIC SYLLABLE ', '').replace('ETHIOPIC ', '')


def word_reading(trs):
    """Join per-sign values; the 6th-order ə is kept word-initially and after a consonant, dropped word-finally
    and after a vowel (the pilot's rule)."""
    out = ''
    for i, tr in enumerate(trs):
        cons, vow = tr[:-1], tr[-1]
        if vow != 'ə':
            out += tr
            continue
        if len(trs) == 1 or i == 0:
            keep = True
        elif i == len(trs) - 1:
            keep = False
        else:
            keep = not (out and out[-1] in 'äuiaeoə')
        out += cons + ('ə' if keep else '')
    return out


def readable(r):
    for a, b in [('ʷ', 'w'), ('ə', 'e'), ('ä', 'a'), ('ś', 's'), ('š', 'sh'), ('ḥ', 'h'), ('ḫ', 'h'),
                 ('ṭ', 't'), ('ṣ́', 's'), ('ṣ', 's'), ('q̱', 'q'), ('p̣', 'p'), ('ʾ', ''), ('ʿ', ''),
                 ('č̣', 'ch'), ('č', 'ch'), ('ñ', 'ny'), ('ž', 'zh'), ('ǧ', 'j')]:
        r = r.replace(a, b)
    return r


def num_value(chars):
    """Ethiopic numeral → integer (፲ወ፰ = 18: ወ 'and' joins parts; ፻ multiplies what precedes it by 100)."""
    total, group, cur = 0, 0, 0
    for c in chars:
        if c in DIG or c in TENS:
            cur += DIG.get(c, 0) + TENS.get(c, 0)
        elif c == HUNDRED:
            group += (cur or 1) * 100
            cur = 0
        elif c == MYRIAD:
            total += (group + cur or 1) * 10000
            group = cur = 0
    return total + group + cur


def build_word(w):
    if any(c in NUMCH for c in w):
        glyphs, numchars = [], []
        for i, c in enumerate(w):
            if c in NUMCH:
                glyphs.append({'s': c, 'sign': sign_key(c), 'role': 'num', 'tr': str(DIG.get(c) or TENS.get(c) or (100 if c == HUNDRED else 10000))})
                numchars.append(c)
            elif c == 'ወ' and 0 < i < len(w) - 1 and w[i - 1] in NUMCH:
                glyphs.append({'s': c, 'sign': 'WA', 'role': 'num', 'tr': 'and'})
            else:
                glyphs.append({'s': c, 'sign': sign_key(c), 'role': 'phon', 'tr': syl_tr(c)})
        h = len(numchars) // 2
        if len(numchars) % 2 == 0 and numchars[:h] == numchars[h:]:
            v = str(num_value(numchars[:h]))          # distributive doubling: በበ፯፯ "seven by seven"
            val = f'{v}-{v}'
        else:
            val = str(num_value(numchars))
        lead = ''.join(syl_tr(c) for c in w[:next(i for i, c in enumerate(w) if c in NUMCH)])
        rd = (readable_prefix(lead) + '-' + val) if lead else val
        return {'reading': rd, 'say': rd, 'glyphs': glyphs}
    trs = [syl_tr(c) for c in w]
    glyphs = [{'s': c, 'sign': sign_key(c), 'role': 'phon', 'tr': t} for c, t in zip(w, trs)]
    rd = word_reading(trs)
    return {'reading': rd, 'say': readable(rd), 'glyphs': glyphs}


def readable_prefix(t):
    """A proclitic written before a numeral (ዘ፫…, ለ፪…): its value without the vowel mark of the 1st order."""
    return t.replace('ä', 'a').replace('ə', '')


def split_words(t):
    """Words of a unit: split at the wordspace and at every other Ethiopic punctuation mark."""
    return [w for w in re.split('[' + ''.join(PUNCT) + r'\s]+', t) if w]


def forms_of_text(txt):
    return split_words(txt)


def published_glossary():
    g = {}
    for f in sorted(glob.glob(os.path.join(R.ROOT, 'kebra-nagast-*.json'))):
        d = R.jload(f)
        g.update(d.get('glossary', {}))
    return g


def forms(p):
    known = published_glossary()
    seen, novel, kn = set(), {}, {}
    for w in forms_of_text(slice_source(p)):
        if w in seen:
            continue
        seen.add(w)
        if w in known:
            kn[w] = known[w]
        else:
            novel[w] = ''
    return novel, kn


def packet(p):
    src = slice_source(p)
    order = [q['id'] for q in R.parts_doc('kebra-nagast')['parts']]
    i = order.index(p['id'])
    prev = None
    if i > 0:
        pf = os.path.join(R.ROOT, R.part('kebra-nagast', order[i - 1])['file'])
        if os.path.exists(pf):
            prev = R.jload(pf)['sentences'][-1]
    out = [f'# Packet — {p["id"]} ({p["cite"]})', '',
           'The Geʿez below is the pinned source (Bezold 1905 via HaCohen). Cut `t` from it by script, never retype.',
           'Paragraphs are separated by a blank line; chapters by a line `== chapter N ==`.', '']
    srcd = _src()
    for ch in p['chapters']:
        c = srcd['chapters'][ch['n'] - 1]
        out.append(f'== chapter {c["label"]} ==' + (f' (characters {ch["span"][0]}–{ch["span"][1]} of the chapter)' if 'span' in ch else ''))
        txt = chapter_text(c)
        if 'span' in ch:
            txt = txt[ch['span'][0]:ch['span'][1]].strip()
        out.append(txt.replace('\n', '\n\n'))
        out.append('')
    if prev:
        out += ['## The previous part ends', '', f'- t: {prev["t"]}', f'- i: {prev.get("i") or prev["l"]}', '']
    out += [f'Words in this part: {len(forms_of_text(src))}.', '']
    return '\n'.join(out)


def _gloss_entry(g, w):
    e = g.get(w)
    if not e:
        return None
    return e


def assemble(p, units, gloss):
    cfg = R.work_cfg('kebra-nagast')
    src = slice_source(p)
    known = published_glossary()
    broaden = gloss.pop('__broaden__', {}) if isinstance(gloss, dict) else {}
    G = dict(known)
    G.update({k: v for k, v in gloss.items() if v})
    G.update(broaden)
    sents = []
    for k, u in enumerate(units['sentences']):
        t = u['t'].strip()
        words = []
        for w in split_words(t):
            wd = build_word(w)
            e = G.get(w)
            if e:
                lemma, _, rest = e.partition(' — ')
                wd['morph'] = [{'lemma': lemma.strip(), 'gloss': rest.strip() or e, 'g': list(range(len(wd['glyphs'])))}]
            else:
                wd['morph'] = []
            words.append(wd)
        s = {'t': t, 'tr': ' '.join(x['reading'] for x in words), 'l': u.get('l', ''), 'i': u.get('i', ''), 'n': u.get('n', '')}
        if u.get('p'):
            s['p'] = True
        s['words'] = words
        if not s['i']:
            del s['i']
        sents.append(s)
    used = {w for s in sents for w in split_words(s['t'])}
    story = dict(cfg['header'])
    story.update({'id': p['id'], 'title': units.get('title') or cfg['titleBase'],
                  'titleEn': units['titleEn'], 'work': cfg['header'].get('work'), 'part': units['part'],
                  'source': cfg['sourceStatement'].replace('{cite}', p['cite']),
                  'about': units.get('about', ''), 'sentences': sents,
                  'glossary': {w: G[w] for w in sorted(used) if w in G}})
    if not story['about']:
        del story['about']
    return story, {}


def validate(p, story):
    errs, warns = [], []
    src = slice_source(p)
    joined = ''.join(s['t'] for s in story['sentences'])
    if re.sub(r'\s', '', joined) != re.sub(r'\s', '', src):
        a, b = re.sub(r'\s', '', joined), re.sub(r'\s', '', src)
        i = next((k for k in range(min(len(a), len(b))) if a[k] != b[k]), min(len(a), len(b)))
        errs.append(f'units do not reproduce the source: first difference at character {i}: units {a[i:i+30]!r} vs source {b[i:i+30]!r}')
    for k, s in enumerate(story['sentences']):
        last = s['t'].rstrip()[-1:]
        if last not in TERMINAL and k != len(story['sentences']) - 1:
            errs.append(f'unit {k}: does not end at ። ፤ or ፨')
        for j, w in enumerate(s['words']):
            if not w.get('morph'):
                errs.append(f'unit {k} word {j} ({"".join(g["s"] for g in w["glyphs"])}): no glossary entry')
    # paragraph starts must be marked
    starts = set()
    pos = 0
    for para in re.split(r'\n+', src):
        starts.add(re.sub(r'\s', '', src[:src.find(para, pos)]).__len__())
        pos = src.find(para, pos) + len(para)
    pos = 0
    for k, s in enumerate(story['sentences']):
        if pos in starts and not s.get('p'):
            warns.append(f'unit {k}: begins a paragraph of the source but has no p:true')
        pos += len(re.sub(r'\s', '', s['t']))
    e2, w2 = R.words_checks(story)
    errs += e2
    warns += w2
    for w, e in story['glossary'].items():
        if ' — ' not in e:
            errs.append(f'glossary {w}: entry must be "lemma — meaning (grammar)"')
    return errs, warns
