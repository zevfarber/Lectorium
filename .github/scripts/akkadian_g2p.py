#!/usr/bin/env python3
"""Normalized Old Babylonian Akkadian (the `say` layer: šumma awīlum …) -> IPA pins for a carrier voice.

Convention: conventional reconstructed Old Babylonian, standard Assyriological values
(Huehnergard, A Grammar of Akkadian, §§ on phonology and stress):
- š = [ʃ], ḫ = [x], q = [k] (carrier has no [q]), ṣ = [ts] (the affricate reading of the emphatic),
  ṭ = [t] (emphasis not rendered), ʾ = hiatus (no glottal stop in the carrier set), w = [w], y = [j].
- vowels: short a e i u -> a ɛ ɪ ʊ ; long ā ē ī ū and contracted â ê î û -> aː e iː u
  (the carrier keeps true length only on aː iː; e/u are length-by-quality, as for Greek and Norse).
- stress (Huehnergard's rule): on the last non-final heavy syllable (long vowel or closed);
  a final contracted (circumflex) vowel takes the stress; if no heavy syllable, the first syllable.
- geminates are read single (the carrier rejects consonant length) — the honest limitation.

Two variants: inventory "de" (de-DE Neural2/WaveNet accepted set, probed for Norse) and "ar"
(Arabic carrier: keeps q, ṣ ṭ emphatics, ʔ and geminates IF the voice honours them — must be probed).
"""
import unicodedata as U, re, sys

LONG = {'ā':'a','ē':'e','ī':'i','ū':'u'}
CIRC = {'â':'a','ê':'e','î':'i','û':'u'}
SHORT = set('aeiu')

def segments(word):
    w = U.normalize('NFC', word.lower().replace("'", 'ʾ').replace('’','ʾ'))
    w = w.replace('j', 'y')
    w = re.sub(r'[^a-zāēīūâêîûšṣṭḫʾ]', '', w)
    out = []
    for ch in w:
        if ch in LONG:  out.append(('V', LONG[ch], 'long'))
        elif ch in CIRC: out.append(('V', CIRC[ch], 'circ'))
        elif ch in SHORT: out.append(('V', ch, 'short'))
        else: out.append(('C', ch, None))
    return out

def syllables(segs):
    """CV(C) syllabification: a single consonant between vowels opens the next syllable;
    of a cluster, the first closes the preceding syllable."""
    vidx = [i for i, s in enumerate(segs) if s[0] == 'V']
    if not vidx: return [segs]
    bounds = [0]
    for a, b in zip(vidx, vidx[1:]):
        ncons = b - a - 1
        bounds.append(b - 1 if ncons >= 1 else b)
    bounds.append(len(segs))
    return [segs[bounds[k]:bounds[k+1]] for k in range(len(bounds)-1)]

def stress_index(syls):
    n = len(syls)
    if n == 1: return 0
    def heavy(s):
        v = [x for x in s if x[0] == 'V'][0]
        return v[2] != 'short' or s[-1][0] == 'C'
    last_v = [x for x in syls[-1] if x[0] == 'V'][0]
    if last_v[2] == 'circ': return n - 1
    for k in range(n - 2, -1, -1):
        if heavy(syls[k]): return k
    return 0

CONS_DE = {'b':'b','d':'d','g':'g','k':'k','p':'p','t':'t','l':'l','m':'m','n':'n','r':'r',
           's':'s','z':'z','š':'ʃ','ḫ':'x','q':'k','ṣ':'ts','ṭ':'t','w':'w','y':'j','ʾ':''}
VOW_DE = {('a','short'):'a', ('e','short'):'ɛ', ('i','short'):'ɪ', ('u','short'):'ʊ',
          ('a','long'):'aː', ('e','long'):'e', ('i','long'):'iː', ('u','long'):'u'}
CONS_AR = dict(CONS_DE, **{'q':'q','ṣ':'sˤ','ṭ':'tˤ','ʾ':'ʔ'})
VOW_AR = {('a','short'):'a', ('e','short'):'e', ('i','short'):'i', ('u','short'):'u',
          ('a','long'):'aː', ('e','long'):'eː', ('i','long'):'iː', ('u','long'):'uː'}

def ipa(word, inv='de'):
    C, V = (CONS_DE, VOW_DE) if inv == 'de' else (CONS_AR, VOW_AR)
    segs = segments(word)
    if not segs: return ''
    syls = syllables(segs)
    st = stress_index(syls)
    out = []
    for k, syl in enumerate(syls):
        piece = ''
        prev = None
        for t, ch, q in syl:
            if t == 'V':
                piece += V[(ch, 'short' if q == 'short' else 'long')]
            else:
                c = C[ch]
                if inv == 'de' and c and prev == c: continue   # geminate -> single
                piece += c
            prev = C.get(ch) if t == 'C' else None
        if k == st and len(syls) > 1: piece = 'ˈ' + piece
        out.append(piece)
    s = ''.join(out)
    # German carrier rejects consonant length: geminates become single (stress mark may sit between them).
    # The Arabic carrier keeps the doubled letters as written (bb, mm), its natural way to say a geminate.
    if inv == 'de':
        for c in sorted(set(C.values()) - {''}, key=len, reverse=True):
            s = s.replace(c + 'ˈ' + c, 'ˈ' + c).replace(c + c, c)
    return s

# Numerals as the stele writes them (digits in `say`) -> spoken Old Babylonian forms.
# Cardinals before a counted noun; "N-šu" is the multiplicative "N-fold" (adi 5-šu = adi ḫamšīšu).
CARDINAL = {'1': 'ištēn', '2': 'šinā', '3': 'šalāš', '4': 'erbe', '5': 'ḫamiš', '6': 'šeššet',
            '10': 'ešer', '12': 'šinšer', '20': 'ešrā', '30': 'šalāšā', '60': 'šūšum'}
MULT = {'2': 'šinīšu', '3': 'šalāšīšu', '5': 'ḫamšīšu', '6': 'šeššīšu', '10': 'ešrīšu',
        '12': 'šinšerīšu', '30': 'šalāšāšu'}

def spoken_words(say):
    """A word's `say` -> list of speakable words: split on spaces and hyphens, numerals spelled out."""
    out = []
    for part in say.split():
        m = re.fullmatch(r'(\d+)-šu', part)
        if m and m.group(1) in MULT:
            out.append(MULT[m.group(1)]); continue
        if part.isdigit():
            out.append(CARDINAL.get(part, part)); continue
        out.extend(p for p in part.split('-') if p)
    return out

def say_ipa(say):
    """IPA for a whole `say` (several words joined by a space; each word keeps its own stress)."""
    return ' '.join(p for p in (ipa(w) for w in spoken_words(say)) if p)

# --- build_pinned.py interface (2026-10-11) -------------------------------------------------
# Akkadian stories are words-model: `t` holds cuneiform, each words[i].say the normalized reading.
# The builder calls sentence_ssml(s) for a unit and word_ipa_map(story, word_key) for the word clips;
# the aligner (align_wordref.py) times one span per words[] entry, keyed by word_key(say).
from xml.sax.saxutils import escape as _esc

def _ph(p, say):
    return '<phoneme alphabet="ipa" ph="%s">%s</phoneme>' % (_esc(p, {'"': '&quot;'}), _esc(say))

def sentence_ssml(s):
    parts = []
    for w in s.get('words', []):
        say = (w.get('say') or '').strip()
        if not say:
            continue
        for sw in spoken_words(say):
            p = ipa(sw)
            if p:
                parts.append(_ph(p, sw))
    return '<speak>' + ' '.join(parts) + '</speak>'

def word_ipa_map(story, word_key):
    out = {}
    for s in story['sentences']:
        for w in s.get('words', []):
            say = (w.get('say') or '').strip()
            if say:
                out.setdefault(word_key(say), say_ipa(say))
    return out

if __name__ == '__main__':
    for w in sys.argv[1:] or 'šumma awīlum awīlam ubbirma nērtam elišu iddīma lā uktīnšu mubbiršu iddâk'.split():
        print(w, ipa(w), ipa(w, 'ar'))
