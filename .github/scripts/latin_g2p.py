#!/usr/bin/env python3
"""Latin -> IPA pins for Lectorium's restored Classical reading (after Allen, Vox Latina), for a
carrier voice under <phoneme> tags. Decided by Zev 2026-10-04: normal WORD stress (not the metrical
beat), long vowels held long.

Input words must carry macrons on long vowels (ā ē ī ō ū ȳ). The edition prints none; a scansion /
macronizing pass supplies them. Rules:
- vowels: a/ā a/aː, e/ē ɛ/eː, i/ī ɪ/iː, o/ō ɔ/oː, u/ū ʊ/uː, y/ȳ ʏ/yː
- ae aɪ, oe ɔʏ, au aʊ, eu ɛʊ
- c k, g g, gn ŋn, n before c g q x ŋ, qu kw, ngu+vowel ŋgw, su+ā/ē in suāvis etc. not handled
- v and consonantal i -> w, j (initial i before a vowel; i between vowels is jj)
- x ks, z z, h h, ph th ch -> p+h t+h k+h (the carrier rejects the ʰ diacritic)
- geminates read single (the carrier cannot hold a consonant)
- stress: penult if heavy (long vowel, diphthong, or closed), else antepenult; two-syllable words
  on the first; before an enclitic -que -ne -ve the stress falls on the syllable before it.
"""
import re, unicodedata as U

LONG = {'ā': 'a', 'ē': 'e', 'ī': 'i', 'ō': 'o', 'ū': 'u', 'ȳ': 'y'}
SHORT_IPA = {'a': 'a', 'e': 'ɛ', 'i': 'ɪ', 'o': 'ɔ', 'u': 'ʊ', 'y': 'ʏ'}
LONG_IPA = {'a': 'aː', 'e': 'eː', 'i': 'iː', 'o': 'oː', 'u': 'uː', 'y': 'yː'}
DIPH = {'ae': 'aɪ', 'oe': 'ɔʏ', 'au': 'aʊ', 'eu': 'ɛʊ'}
VOWELS = set('aeiouy')
NOT_ENCLITIC = {'atque', 'neque', 'itaque', 'usque', 'undique', 'ubique', 'utique', 'uterque',
                'utraque', 'utrumque', 'plerumque', 'denique', 'absque'}
MUTA, LIQ = set('pbtdcgkf'), set('lr')
ENCLITICS = ('que',)   # -ne and -ve are too often ordinary endings (origine, nave) to detect safely


def _units(w):
    """Split a lowercase macronized word into ('V', base, long, diph) / ('C', ipa, count) units."""
    w = U.normalize('NFC', w.lower())
    out, i, n = [], 0, len(w)
    def isv(ch): return ch in VOWELS or ch in LONG
    while i < n:
        ch = w[i]; nx = w[i + 1] if i + 1 < n else ''
        if isv(ch):
            base = LONG.get(ch, ch); long_ = ch in LONG
            pair = base + LONG.get(nx, nx)
            # consonantal i/u handled below; here only vowel nuclei
            if pair in DIPH and nx not in LONG and not (pair == 'eu' and False):
                out.append(('V', DIPH[pair], True, True)); i += 2; continue
            # i between vowels = consonantal (jj): maior, Troiae
            if base == 'i' and not long_ and out and out[-1][0] == 'V' and i + 1 < n and isv(nx):
                out.append(('C', 'j', 2)); i += 1; continue
            # initial i before a vowel = j (iam, iactatus, Iuno)
            if base == 'i' and not long_ and i == 0 and isv(nx):
                out.append(('C', 'j', 1)); i += 1; continue
            out.append(('V', (LONG_IPA if long_ else SHORT_IPA)[base], long_, False)); i += 1; continue
        if ch == 'q' and nx == 'u':
            out.append(('C', 'kw', 1)); i += 2; continue
        if ch == 'g' and nx == 'u' and i + 2 < n and isv(w[i + 2]) and i > 0 and w[i - 1] == 'n':
            out.append(('C', 'gw', 1)); i += 2; continue
        if ch in 'ptc' and nx == 'h':
            out.append(('C', {'p': 'p', 't': 't', 'c': 'k'}[ch] + 'h', 1)); i += 2; continue
        if ch == 'g' and nx == 'n':
            out.append(('C', 'ŋ', 1)); i += 1; continue
        if ch == 'n' and nx and nx in 'cgqx':
            out.append(('C', 'ŋ', 1)); i += 1; continue
        if ch == 'x':
            out.append(('C', 'ks', 2)); i += 1; continue
        if ch == 'z':
            out.append(('C', 'z', 2)); i += 1; continue
        if ch == 'v' or (ch == 'u' and False):
            out.append(('C', 'w', 1)); i += 1; continue
        if ch == 'j':
            out.append(('C', 'j', 1)); i += 1; continue
        if ch == 'c' or ch == 'k':
            out.append(('C', 'k', 1)); i += 1; continue
        if ch.isalpha():
            if out and out[-1][0] == 'C' and out[-1][1] == ch:   # geminate: read single, counts double
                out[-1] = ('C', ch, out[-1][2] + 1); i += 1; continue
            out.append(('C', ch, 1)); i += 1; continue
        i += 1
    return out


def _stress_index(units, enclitic):
    vidx = [k for k, u in enumerate(units) if u[0] == 'V']
    if len(vidx) <= 1:
        return vidx[0] if vidx else None
    if enclitic:
        # stress the syllable before the enclitic (the last vowel of the host)
        return vidx[-2]
    if len(vidx) == 2:
        return vidx[0]
    pen = vidx[-2]
    heavy = units[pen][2]
    if not heavy:
        cons = []
        k = pen + 1
        while k < len(units) and units[k][0] == 'C':
            cons.append(units[k]); k += 1
        count = sum(c[2] for c in cons)
        mcl = len(cons) == 2 and cons[0][1][-1] in MUTA and cons[1][1] in LIQ
        heavy = count >= 2 and not mcl
    return pen if heavy else vidx[-3]


def ipa(word):
    """IPA for one macronized Latin word, with ˈ before the stressed syllable."""
    w = U.normalize('NFC', word.lower())
    enclitic = (any(w.endswith(e) and len(w) > len(e) + 1 for e in ENCLITICS)
                and not w.startswith(('qu', 'cu')) and w not in NOT_ENCLITIC)
    units = _units(w)
    s = _stress_index(units, enclitic)
    out = []
    for k, u in enumerate(units):
        if k == s and len([x for x in units if x[0] == 'V']) > 1:
            # onset: last consonant before the vowel, two if muta cum liquida
            j = len(out); back = 0
            if k >= 1 and units[k - 1][0] == 'C':
                back = 1
                if k >= 2 and units[k - 2][0] == 'C' and units[k - 2][1][-1] in MUTA and units[k - 1][1] in LIQ:
                    back = 2
            pos = len(out) - back
            out.insert(pos, 'ˈ')
        out.append(u[1])
    return ''.join(out)


if __name__ == '__main__':
    import sys
    for w in sys.argv[1:]:
        print(w, ipa(w))
