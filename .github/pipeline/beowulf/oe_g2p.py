#!/usr/bin/env python3
"""Old English (Klaeber 1922 normalized spelling) -> IPA pins for a carrier voice.

Convention (decided July 2026): reconstructed late West Saxon, c. 1000, after Campbell, Old English
Grammar (1959), §§ 15-66 on the values of the letters. Written 2026-10-12 for the Beowulf voice samples.

What the letters mean here
- Vowels: short a æ e i o u y = [ɑ æ ɛ ɪ ɔ ʊ ʏ]; long ā ǣ ē ī ō ū ȳ = [ɑː æː eː iː oː uː yː].
  Klaeber's circumflex marks a contracted (long) vowel; where he prints it on the second vowel of a pair
  (Līffreâ, geþeôn, heân) the pair is the long diphthong (ēa, ēo). A dot under a vowel (dōgọra) is
  his metrical sign and does not change the sound. ę (e caudata) is read as æ.
- Diphthongs: ea [æɑ], ēa [æːɑ], eo [ɛɔ], ēo [eːɔ], ie [ɪɛ], īe [iːɛ], io [ɪɔ], īo [iːɔ].
- c: [tʃ] word-initially before a front vowel (not before y, which in cyning, cyme is the umlaut of u),
  and after i/ī (ic, rīce, līc); otherwise [k]. A short list of common words with palatal c that the
  rule cannot see (sēcan, þencan, ǣlc, swylc, hwylc …) is in PALATAL_C.
- g: [j] word-initially before a front vowel (including y: LWS gyldan, gyf- are old gie-; gylden is
  the listed exception), and next to a front vowel inside the word (dæg, hālig); [g] after n and
  in cg/gg; [ɣ] after a back vowel or between back vowels; prefix ge- = [jɛ].
- sc = [ʃ]; cg = [dʒ]; ng = [ŋg]; nc = [ŋk]; x = [ks]; hw = [hw].
- h: [h] at the start of a word; [x] after a back vowel, [ç] after a front vowel elsewhere.
- f s þ/ð: voiced [v z ð] between voiced sounds inside a word, voiceless [f s θ] at the edges, next to
  a voiceless sound, and when doubled. A prefix or hyphen boundary counts as a word edge.
- Doubled consonants are true geminates; the token GEM marks them and the carrier reduction drops it
  where the voice rejects consonant length (German does).
- Stress: on the first syllable of the root. The unstressed prefixes ge-, be-, for-, of- (before a
  consonant) are recognized when what follows is a plausible root; nouns such as ymbsittend keep stress
  on the first syllable as the rule gives. Monosyllables carry no mark.

Known limits (stated, not hidden): compounds without a hyphen are not split, so a voiceless consonant
at the start of a second element between vowels is voiced (meodosetla -> [z]); palatal c/g outside the
rules and the list is read as velar; unstressed vowels keep their full quality.

The carrier step: ipa_tokens() returns ideal phones; reduce() maps each to the first candidate the
carrier accepts (CHAINS), with the accepted set probed against the live API (voice_samples.py).
"""
import re
import unicodedata as U

GEM = "GEM"
STRESS = "ˈ"

_V = {'a': ('a', 0), 'ā': ('a', 1), 'â': ('a', 1), 'æ': ('æ', 0), 'ǣ': ('æ', 1), 'ǽ': ('æ', 1),
      'ę': ('æ', 0), 'e': ('e', 0), 'ē': ('e', 1), 'ê': ('e', 1), 'i': ('i', 0), 'ī': ('i', 1),
      'î': ('i', 1), 'o': ('o', 0), 'ō': ('o', 1), 'ô': ('o', 1), 'u': ('u', 0), 'ū': ('u', 1),
      'û': ('u', 1), 'y': ('y', 0), 'ȳ': ('y', 1), 'ŷ': ('y', 1), 'í': ('i', 0), 'á': ('a', 0),
      'ó': ('o', 0), 'ë': ('e', 0), 'ö': ('o', 0), 'ü': ('u', 0), 'ä': ('a', 0)}
_CIRC = set('âêîôûŷ')
_SHORT = {'a': 'ɑ', 'æ': 'æ', 'e': 'ɛ', 'i': 'ɪ', 'o': 'ɔ', 'u': 'ʊ', 'y': 'ʏ'}
_LONG = {'a': 'ɑː', 'æ': 'æː', 'e': 'eː', 'i': 'iː', 'o': 'oː', 'u': 'uː', 'y': 'yː'}
_DIPH = {('e', 'a'): ('æ', 'ɑ'), ('e', 'o'): ('e', 'ɔ'), ('i', 'e'): ('i', 'ɛ'), ('i', 'o'): ('i', 'ɔ')}
FRONT_PHONES = {'ɪ', 'iː', 'ɛ', 'eː', 'æ', 'æː', 'ʏ', 'yː'}
VOICED = {'b', 'd', 'g', 'v', 'z', 'ð', 'ɣ', 'j', 'w', 'r', 'l', 'm', 'n', 'ŋ', 'dʒ'}
VOICELESS = {'p', 't', 'k', 'f', 's', 'θ', 'x', 'ç', 'h', 'ʃ', 'tʃ', 'hw'}

PALATAL_C = {  # whole word forms (and their common inflections by prefix match) with palatal c
    'sēc', 'sōht', 'þenc', 'þync', 'drenc', 'benc', 'wrecc', 'recc', 'ǣlc', 'swylc', 'hwylc',
    'ǣghwylc', 'ylc', 'tǣc', 'rǣc', 'strecc', 'bēc', 'rīc', 'mycel', 'micel', 'ðicc', 'þicc',
    'lǣc', 'ǣlǣc', 'spræc', 'cēn', 'cīd', 'cild', 'cyrc', 'cȳs', 'brēc', 'stenc', 'ecg',
}
VELAR_G_INITIAL = ('gylden', 'gyrd', 'gylt')   # initial gy- that is umlaut of u, not old gie-
UNSTRESSED_PREFIXES = ('ge', 'be', 'for', 'of')
NOT_PREFIXED = {'beran', 'berað', 'bereð', 'forma', 'forman', 'forð', 'fore', 'forþ', 'ofer', 'ofost',
                'begen', 'bēga', 'gegnum', 'forst', 'fōre', 'getenga'}


def normalize(word):
    w = U.normalize('NFD', word.lower())
    w = w.replace('̣', '')                    # Klaeber's metrical dot: no change of sound
    w = U.normalize('NFC', w)
    w = re.sub(r"[\[\]()†’'‘·]", '', w)
    return w


def _units(part):
    """Split a word part into ('V', phones, front) and ('C', letter) units."""
    out, i, n = [], 0, len(part)
    while i < n:
        ch = part[i]
        if ch in _V:
            b1, l1 = _V[ch]
            if i + 1 < n and part[i + 1] in _V:
                b2, l2 = _V[part[i + 1]]
                if (b1, b2) in _DIPH:
                    long_ = l1 or (part[i + 1] in _CIRC)
                    p1, p2 = _DIPH[(b1, b2)]
                    first = _LONG[p1] if long_ else _SHORT[p1]
                    out.append(('V', [first, p2 if p2 != 'e' else 'ɛ'], True)); i += 2; continue
            ph = _LONG[b1] if l1 else _SHORT[b1]
            out.append(('V', [ph], b1 in 'æeiy')); i += 1
        elif ch.isalpha():
            out.append(('C', 'þ' if ch == 'ð' else ch)); i += 1
        else:
            i += 1
    return out


def _palatal_c_word(part):
    return any(part.startswith(p) for p in PALATAL_C)


def _part_phones(part, prefix_g=False):
    """Phones for one stressable part (word edge on both sides)."""
    u = _units(part)
    ph = []                                         # list of (phone, kind) kind in V/C
    k = 0
    palc = _palatal_c_word(part)

    def nucleus(j):                                 # the nucleus unit at j, or None
        return u[j] if 0 <= j < len(u) and u[j][0] == 'V' else None

    def prev_nuc(j):
        for t in range(j - 1, -1, -1):
            if u[t][0] == 'V':
                return u[t]
        return None

    while k < len(u):
        t = u[k]
        if t[0] == 'V':
            ph.append((''.join(t[1]), 'V'))
            k += 1; continue
        c = t[1]
        nxt = u[k + 1] if k + 1 < len(u) else None
        nc = nxt[1] if nxt and nxt[0] == 'C' else None
        initial = k == 0
        final = k == len(u) - 1
        gem = nc == c
        if c == 's' and nc == 'c':
            ph.append(('ʃ', 'C')); k += 2; continue
        if c == 'c' and nc == 'g':
            ph.append(('dʒ', 'C')); k += 2; continue
        if c == 'h' and nc == 'w':
            ph.append(('hw', 'C')); k += 2; continue
        if c == 'x':
            ph.append(('k', 'C')); ph.append(('s', 'C')); k += 1; continue
        if c == 'n' and nc in ('g', 'c', 'k'):
            ph.append(('ŋ', 'C')); k += 1; continue
        if c == 'c':
            fn = nucleus(k + (2 if gem else 1))
            pv = prev_nuc(k)
            pal = False
            if initial and fn and fn[2] and fn[1][0] not in ('ʏ', 'yː'):
                pal = True
            elif pv and pv[1][-1] in ('ɪ', 'iː') and not (fn and fn[1][0] in ('ɑ', 'ɑː', 'ɔ', 'oː', 'ʊ', 'uː')):
                pal = True
            elif palc and not initial:
                pal = True
            ph.append(('tʃ' if pal else 'k', 'C'))
            if gem: ph.append((GEM, 'C')); k += 2
            else: k += 1
            continue
        if c == 'g':
            prevc = u[k - 1][1] if k > 0 and u[k - 1][0] == 'C' else None
            if prevc == 'n' or gem:
                ph.append(('g', 'C'))
                if gem: ph.append((GEM, 'C')); k += 2
                else: k += 1
                continue
            fn = nucleus(k + 1)
            pv = prev_nuc(k)
            if initial:
                front = fn and (fn[2] or fn[1][0] in ('ʏ', 'yː'))
                if front and part.startswith(VELAR_G_INITIAL):
                    front = False
                ph.append(('j' if front else 'g', 'C'))
            elif (pv and pv[1][-1] in FRONT_PHONES and prevc is None) or (fn and fn[2] and prevc is None):
                ph.append(('j', 'C'))
            elif prevc in ('l', 'r') and pv and pv[1][-1] in FRONT_PHONES:
                ph.append(('j', 'C'))
            else:
                ph.append(('ɣ', 'C'))
            k += 1; continue
        if c == 'h':
            if initial:
                ph.append(('h', 'C')); k += 1; continue
            pv = prev_nuc(k)
            ph.append(('ç' if pv and pv[1][-1] in FRONT_PHONES else 'x', 'C'))
            k += 2 if gem else 1
            continue
        if c in ('f', 's', 'þ'):
            base = {'f': 'f', 's': 's', 'þ': 'θ'}[c]
            if gem:
                ph.append((base, 'C')); ph.append((GEM, 'C')); k += 2; continue
            ph.append(('?' + base, 'C')); k += 1; continue
        simple = {'b': 'b', 'd': 'd', 'p': 'p', 't': 't', 'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n',
                  'r': 'r', 'w': 'w', 'z': 'ts', 'j': 'j', 'q': 'k', 'v': 'v'}
        if c in simple:
            ph.append((simple[c], 'C'))
            if gem: ph.append((GEM, 'C')); k += 2
            else: k += 1
            continue
        k += 1
    # resolve voicing of f s þ between voiced sounds
    out = []
    for j, (p, kind) in enumerate(ph):
        if p.startswith('?'):
            base = p[1:]
            prv = next((q for q, _ in reversed(ph[:j]) if q != GEM), None)
            nx = next((q for q, _ in ph[j + 1:] if q != GEM), None)
            def voiced(q):
                return q is not None and (q in VOICED or q in _ALLV)
            if voiced(prv) and voiced(nx):
                p = {'f': 'v', 's': 'z', 'θ': 'ð'}[base]
            else:
                p = base
        out.append(p)
    return out


_VOWEL_START = set('ɑæɛeɪiɔoʊuʏyaə')


def is_vowel(p):
    return bool(p) and p[0] in _VOWEL_START


class _AllV:
    def __contains__(self, p):
        return is_vowel(p)


_ALLV = _AllV()


def _nuclei(phones):
    return sum(1 for p in phones if is_vowel(p))


def split_prefix(w):
    if w in NOT_PREFIXED or '-' in w:
        return '', w
    for pf in UNSTRESSED_PREFIXES:
        if w.startswith(pf) and len(w) - len(pf) >= 3:
            rest = w[len(pf):]
            if rest[0] in _V or not any(ch in _V for ch in rest):
                continue
            if pf == 'for' and rest[0] in 'ðþ':
                continue
            return pf, rest
    return '', w


_PREFIX_PH = {'ge': ['j', 'ɛ'], 'be': ['b', 'ɛ'], 'for': ['f', 'ɔ', 'r'], 'of': ['ɔ', 'f']}


# Compounds whose second element starts with f, s or þ/ð after a vowel or voiced sound (which the
# voicing rule would otherwise voice), split by hand. Extend as the build meets them.
SPLITS = {'meodosetla': 'meodo-setla', 'ymbsittendra': 'ymb-sittendra', 'ymbsittend': 'ymb-sittend',
          'ǣghwylc': 'ǣg-hwylc'}


def ipa_tokens(word):
    """Ideal phone tokens for one word, with STRESS before the stressed syllable of polysyllables."""
    w = normalize(word)
    w = SPLITS.get(w, w)
    if not re.search(r'[a-zæþðāǣēīōūȳâêîôûŷę]', w):
        return []
    parts = [p for p in w.split('-') if p]
    pf, first = split_prefix(parts[0])
    toks = list(_PREFIX_PH[pf]) if pf else []
    root = _part_phones(first)
    rest = []
    for p in parts[1:]:
        rest += _part_phones(p)
    total = _nuclei(toks + root + rest)
    if total >= 2:
        toks = toks + [STRESS] + root + rest
    else:
        toks = toks + root + rest
    return toks


def ideal_ipa(word):
    return ''.join('ː' if t == GEM else t for t in ipa_tokens(word))


# Carrier reduction: each ideal phone -> candidates in order of preference.
CHAINS = {
    # diphthongs: the reconstructed value first, then nearer-to-carrier fallbacks
    'æɑ': ['æɑ', 'æa', 'ɛa', 'ɛɑ', 'a'], 'æːɑ': ['æːɑ', 'æːa', 'æɑ', 'æa', 'ɛa', 'aː'],
    'ɛɔ': ['ɛɔ', 'eɔ', 'ɛo', 'eo', 'ɛ'], 'eːɔ': ['eːɔ', 'eːo', 'eɔ', 'eo', 'ɛo', 'e'],
    'ɪɛ': ['ɪɛ', 'iɛ', 'ɪe', 'ie', 'ɪ'], 'iːɛ': ['iːɛ', 'iːe', 'iɛ', 'ie', 'iː'],
    'ɪɔ': ['ɪɔ', 'iɔ', 'io', 'ɪ'], 'iːɔ': ['iːɔ', 'iːo', 'iɔ', 'io', 'iː'],
    'ɑ': ['ɑ', 'a'], 'ɑː': ['ɑː', 'aː', 'ɑ', 'a'], 'æ': ['æ', 'ɛ'], 'æː': ['æː', 'æ', 'ɛ'],
    'ɛ': ['ɛ', 'e'], 'e': ['e', 'ɛ'], 'eː': ['eː', 'e', 'ɛ'], 'ɪ': ['ɪ', 'i'], 'iː': ['iː', 'i'],
    'ɔ': ['ɔ', 'o'], 'oː': ['oː', 'o', 'ɔ'], 'ʊ': ['ʊ', 'u'], 'uː': ['uː', 'u'],
    'ʏ': ['ʏ', 'y', 'ɪ'], 'yː': ['yː', 'y', 'iː', 'i'],
    'θ': ['θ', 't'], 'ð': ['ð', 'd'], 'x': ['x', 'h', 'k'], 'ç': ['ç', 'x', 'h'],
    'ɣ': ['ɣ', 'g'], 'hw': ['hw', 'w'], 'r': ['r', 'ɹ'], 'tʃ': ['tʃ', 't͡ʃ', 'ʃ'], 'dʒ': ['dʒ', 'd͡ʒ', 'ʒ', 'j'],
    'ŋ': ['ŋ', 'n'], 'w': ['w', 'v'], 'v': ['v', 'f'], 'z': ['z', 's'], 'ts': ['ts', 's'],
    'j': ['j'], 'ʃ': ['ʃ'], 'h': ['h'], 'f': ['f'], 's': ['s'], 'p': ['p'], 'b': ['b'], 't': ['t'],
    'd': ['d'], 'k': ['k'], 'g': ['g'], 'l': ['l'], 'm': ['m'], 'n': ['n'],
}


def all_candidates():
    s = set()
    for v in CHAINS.values():
        s.update(v)
    return sorted(s)


def reduce(tokens, accepted, gem_ok=False, log=None):
    """Map ideal tokens to the carrier's accepted inventory. `log` collects (ideal, used) fallbacks."""
    out = []
    for t in tokens:
        if t == STRESS:
            out.append(STRESS); continue
        if t == GEM:
            if gem_ok: out.append('ː')
            elif log is not None: log.append(('GEM', ''))
            continue
        cands = CHAINS.get(t, [t])
        use = next((c for c in cands if c in accepted), None)
        if use is None:
            use = cands[-1]
        if use != t and log is not None:
            log.append((t, use))
        out.append(use)
    s = ''.join(out)
    return s


_PLAIN = str.maketrans({'þ': 'th', 'ð': 'th', 'æ': 'ae', 'ǣ': 'ae', 'ā': 'a', 'ē': 'e', 'ī': 'i',
                        'ō': 'o', 'ū': 'u', 'ȳ': 'y', 'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o',
                        'û': 'u', 'ŷ': 'y', 'ę': 'e', 'ǽ': 'ae'})


def plain(word):
    """What the voice reads if it ever refuses a pin: the word in plain letters."""
    return normalize(word).translate(_PLAIN).replace('-', ' ')


if __name__ == '__main__':
    import sys
    for w in sys.argv[1:]:
        print(w, ideal_ipa(w))
