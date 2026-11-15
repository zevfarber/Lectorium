#!/usr/bin/env python3
"""Reviewer helper (aeneid-077): append hand scansions for X.439-509 to scan-fixes.json, in line order after
the last existing key; keys are f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them. Checks each entry against the build's word-match rule and the
validator's metre rule (half-line rule when the why starts 'Half-line'). Dry run unless --write."""
import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
FP = os.path.join(A.HERE, 'scan-fixes.json')
raw = open(FP, encoding='utf8').read(); fx = json.loads(raw)
assert json.dumps(fx, ensure_ascii=False, indent=1) + '\n' == raw
P = A.part('aeneid-077'); LL = A.lines_of(P)
L = {str(l.get('label', l['n'])): l['t'] for l in LL}
order = [str(l.get('label', l['n'])) for l in LL]
own = lambda n: SL.scan_line(L[n])[1]
EU = "has Greek eu as one long syllable"
NEW = {
 '453': (['1De–si⏑lu⏑2it–', 'Tur–3nus–‖', 'bi⏑iu⏑4gis–', 'pe⏑des⏑', '5ap–pa⏑rat⏑', '6i–re×'],
  "biiugis is bĭ-jŭ-gīs, three syllables, the second i consonantal and bi- short, as at 5.144, 10.253 and 10.399; pedes is the nominative pĕdĕs, 'on foot': Dē-sĭ-lŭ | ĭt Tūr | nūs bĭ-jŭ | gīs pĕ-dĕs | ap-pă-răt | ī-re (16 syllables), caesura after Turnus. The scanner (COSTLY 2.5, flagged) ran bi-iu together into one long syllable, a fit with 15."),
 '486': (['1Il–le⏑', 'ra⏑2pit–', 'ca⏑li⏑3dum–‖', 'frus–4tra–', 'de–', '5vol–ne⏑re⏑', '6te–lum×'],
  "Wrong quantities with the right count (cost 0.0, no flag). calidum is short-short-long here (călĭdus), frustra ends in a long a (frūstrā) and de is long: Il-lĕ ră | pĭt că-lĭ | dum frūs | trā dē | vol-nĕ-rĕ | tē-lum (15 syllables), caesura after calidum. The scanner made ca and li long and the a of frustra and de short."),
 '490': (['1Quem–', 'Tur–2nus–', 'su⏑per⏑', '3ad–sis–4tens×'],
  "Half-line (hemistich), one of Virgil's unfinished lines, as 10.284: Quem Tur | nūs sŭ-pĕr | ad-sis | tens, a spondee, a dactyl, a spondee and one syllable (– – | – ⏑ ⏑ | – – | ×), the r of super carried onto adsistens, the last syllable marked × as the end of the line (8 syllables). There is no hexameter to fit; the scanner returns UNRESOLVED. 491 and 492, in the same unit, are entered as carriers."),
 '491': (None,
  "Carrier line, checked by hand: Ar-că-dĕs | haec in | quit mĕ-mŏ | rēs mĕ-ă | dic-tă rĕ | fer-te (16 syllables), Arcades with the short Greek -ĕs. The scanner's fit is correct; the entry is needed only because this line shares a unit with the half-line 10.490, which the scanner cannot fit, and a unit with an unresolved line receives no sc at all."),
 '492': (None,
  "Carrier line, checked by hand: Eu-an | drō quā | lem mĕ-rŭ | it Pal | lan-tă rĕ | mit-to (14 syllables), Euandro with Greek eu as one long syllable. The scanner's fit is correct; the entry is needed only because the first word of this line closes a unit with the half-line 10.490, which the scanner cannot fit, and a unit with an unresolved line receives no sc at all."),
}
strip = lambda s: re.sub(r'[0-9–⏑×‖]', '', s)
out = dict(fx)
for n in [x for x in order if x in NEW]:
    sc, why = NEW[n]
    if sc is None: sc = own(n)
    k = f"{P['book']}.{n}"; assert k not in fx, k
    assert [strip(x) for x in sc] == A.WORD_RE.findall(L[n]), (k, sc, A.WORD_RE.findall(L[n]))
    seg = ' '.join(sc); feet = re.findall(r'[1-6]', seg); syl = len(re.findall(r'[–⏑×]', seg))
    if why.startswith('Half-line'):
        assert feet == list('123456'[:len(feet)]) and 0 < len(feet) < 6 and seg.count('×') == 1, k
    else:
        body = re.sub(r'[^0-9–⏑×]', '', seg); fp = re.findall(r'\d([–⏑×]+)', body)
        assert feet == list('123456') and 12 <= syl <= 17 and seg.count('×') == 1, (k, feet, syl)
        assert all(f in ('–⏑⏑', '––') for f in fp[:5]) and fp[5] in ('–×', '⏑×'), (k, fp)
    m = re.search(r'(\d+) syllables', why); assert m and int(m.group(1)) == syl, (k, syl)
    out[k] = {'sc': sc, 'why': why}
    print(k, syl, ' '.join(sc))
assert len(out) == len(fx) + len(NEW)
if '--write' in sys.argv:
    open(FP, 'w', encoding='utf8').write(json.dumps(out, ensure_ascii=False, indent=1) + '\n'); print('written')
