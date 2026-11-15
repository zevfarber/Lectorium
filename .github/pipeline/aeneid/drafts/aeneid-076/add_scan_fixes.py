#!/usr/bin/env python3
"""Reviewer helper (aeneid-076): append hand scansions for X.362-438 to scan-fixes.json, in line order after
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
P = A.part('aeneid-076'); LL = A.lines_of(P)
L = {str(l.get('label', l['n'])): l['t'] for l in LL}
order = [str(l.get('label', l['n'])) for l in LL]
own = lambda n: SL.scan_line(L[n])[1]
EU = "has Greek eu as one long syllable"
NEW = {
 '366': (['1as–pe⏑ra⏑', '2quis–', 'na–3tu–ra⏑', 'lo⏑4ci–‖', 'di–5mit–te⏑re⏑', '6quan–do×'],
  "Wrong quantities with the right count (cost 0.0, no flag). natura has long a and long u (nātūra), and loci a short o: ās-pĕ-ră | quīs nā | tū-ră lŏ | cī dī | mit-tĕ-rĕ | quan-do (15 syllables), the caesura after loci. The scanner made na-tu short-short and lo long."),
 '369': (None,
  "Carrier line, checked by hand: Quō fŭ-gĭ | tīs sŏ-cĭ | ī Pēr | vōs ēt | for-tĭ-ă | fac-ta (15 syllables). The scanner's fit is correct; the entry is needed only because this line shares a unit with 10.371, which the scanner cannot fit (the misprint Opemque), and a unit with an unresolved line receives no sc at all."),
 '370': (None,
  "Carrier line, checked by hand: pēr dŭ-cĭs | Ē-vān | drī nō | mēn dē | vic-tă-quĕ | bel-la (14 syllables). The scanner's fit is correct; the entry is needed only because this line shares a unit with 10.371, which the scanner cannot fit (the misprint Opemque), and a unit with an unresolved line receives no sc at all."),
 '371': (['1Opem–que⏑', 'me⏑2am–', 'pa⏑tri⏑3ae–‖', 'quae–', '4nunc–', 'su⏑bit⏑', '5ae–mu⏑la⏑', '6lau–di×'],
  "The print has Opemque, a misprint for spemque (rule 5b: t as printed, the note says so); the line is scanned as spemque, marked on the printed word (as the 5.181 Illum, 7.254 voluit and 10.20 Rutulli entries scan the corrected reading): spem-quĕ mĕ | ām pă-trĭ | ae quae | nunc sŭ-bĭt | ae-mŭ-lă | lau-di (16 syllables), caesura after patriae. The scanner returns UNRESOLVED: ops has a short o (ŏpis), so Opemque meam cannot open a hexameter."),
 '372': (None,
  "Carrier line, checked by hand: fī-dĭ-tĕ | nē pĕ-dĭ | būs Fer | rō rum | pen-dă pĕr | hos-tis (15 syllables). The scanner's fit is correct; the entry is needed only because this line shares a unit with 10.371, which the scanner cannot fit (the misprint Opemque), and a unit with an unresolved line receives no sc at all."),
 '376': (['1mor–ta–2les–', 'to⏑ti⏑3dem–‖', 'no–4bis–', 'a⏑ni⏑5mae–que⏑', 'ma⏑6nus–que×'],
  "Wrong quantities with the right count (cost 0.0, no flag). nobis is long-long (nōbīs) and animae has short a and short i: mor-tā | lēs tŏ-tĭ | dem nō | bīs ă-nĭ | mae-quĕ mă | nus-que (15 syllables). The scanner made no-bis short-short and a-ni long-long."),
 '391': (['1Dau–ci⏑a⏑', '2La–ri–3de–‖', 'Thym–4ber–que⏑', 'si⏑5mil–li⏑ma⏑', '6pro–les×'],
  "Wrong quantities with the right count (COSTLY 0.6, not flagged). Laride has three long syllables (Lārīdē, the Greek vocative in -ē), as at 10.395, where the metre allows nothing else and the scanner reads it so; -que and the si of simillima are short: Dau-cĭ-ă | Lā-rī | dē Thym | ber-quĕ sĭ | mil-lĭ-mă | prō-les (15 syllables). The scanner made ri and de short and then had to lengthen both -que and si."),
 '399': (['1Tum–', 'Pal–2las–', 'bi⏑iu⏑3gis–‖', 'fu⏑gi⏑4en–tem–', '5Rhoe–te⏑a⏑', '6prae–ter×'],
  "biiugis is bĭ-jŭ-gīs, the second i consonantal and bi- short, as at 5.144 and 10.253: Tum Pal | las bĭ-jŭ | gīs fŭ-gĭ | en-tem | Rhoē-tĕ-ă | prae-ter (15 syllables). The scanner (COSTLY 1.5, not flagged) ran bi-iu together into one syllable, a fit with 14."),
 '400': (['1tra–i⏑cit⏑', '2Hoc–', 'spa⏑ti⏑3um–‖', 'tan–4tum–que⏑', 'mo⏑5rae–', 'fu⏑it⏑', '6I–lo×'],
  "traicit (trans + iacio) is trā-ĭ-cĭt, a dactyl, with -cit short before the vowel of Hoc, as at 9.634: trā-ĭ-cĭt | Hōc spă-tĭ | um tan | tum-quĕ mŏ | rae fŭ-ĭt | Ī-lo (16 syllables). The scanner (COSTLY 1.8, not flagged) read trai- as one syllable and made -cit long, a fit with 15."),
 '413': (['1Hic–', 'mac–2tat–', 'La–3do–na⏑‖', 'Phe⏑4re–ta⏑que⏑', '5De–mo⏑do⏑6cum–que×'],
  "Wrong quantities with the right count (cost 0.0, no flag). Ladona has long a and long o (Lādōn, as in Ovid; Greek -ωνα) and a short final a, and Phereta has a short first syllable (Greek Φέρητα): Hīc mac | tāt Lā | dō-nă Phĕ | rē-tă-quĕ | Dē-mŏ-dŏ | cum-que (15 syllables), the pause after Ladona. The scanner made La-do short-short, -na long and Phe long."),
 '419': (['1in–ie–2ce–re⏑', 'ma⏑3num–‖', 'Par–4cae–', 'te–5lis–que⏑', 'sa⏑6cra–runt×'],
  "iniecere (in + iacio): the i after the prefix is consonantal, in-jē-cē-re, four syllables, as iniecit at 2.408: in-jē | cē-rĕ mă | num Par | cae tē | lis-quĕ să | crā-runt (14 syllables). The scanner read i-ni-e-ce-re with a vowel i, a fit with 15."),
 '430': (['1et–', 'vos–', '2O–', 'Gra–3is–‖', 'im–4per–di⏑ta⏑', '5cor–po⏑ra⏑', '6Teu–cri×'],
  "Grais is two long syllables (Grāīs, as 6.529 and 8.135), and imperdita has a short di and a short final a; Teucri has Greek eu as one long syllable: et vōs | Ō Grā | īs im | per-dĭ-tă | cor-pŏ-ră | Teu-cri (14 syllables). The scanner (COSTLY 1.5, not flagged) made Gra-is short-short and di-ta long-long."),
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
