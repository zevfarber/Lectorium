#!/usr/bin/env python3
"""Reviewer helper (aeneid-075): append hand scansions for X.276-361 to scan-fixes.json, in line order after
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
P = A.part('aeneid-075'); LL = A.lines_of(P)
L = {str(l.get('label', l['n'])): l['t'] for l in LL}
order = [str(l.get('label', l['n'])) for l in LL]
own = lambda n: SL.scan_line(L[n])[1]
EU = "has Greek eu as one long syllable"
NEW = {
 '279': (['1Quod–', 'vo–2tis–', 'op–3tas–tis⏑', 'a⏑4dest–‖', 'per–5frin–ge⏑re⏑', '6dex–tra×'],
  "Wrong quantities with the right count (cost 0.0, no flag). votis has a long o (votum, from voveo) and is long-long, and the a of adest is short: Quod vō | tīs op | tās-tĭs ă | dēst per | frin-gĕ-rĕ | dex-tra (14 syllables), with the trochaic pause after optastis and the main caesura after adest. The scanner made vo-tis short-short and the a of adest long."),
 '284': (['1Au–den–2tis–', 'For–3tu–na⏑', 'iu⏑4vat×'],
  "Half-line (hemistich), one of Virgil's unfinished lines: Au-den | tīs For | tū-nă iŭ | vat, two spondees, a dactyl and one syllable (– – | – – | – ⏑ ⏑ | ×), Fortūna with long u, iuvat with consonantal i, the last syllable marked × as the end of the line (8 syllables). There is no hexameter to fit; the scanner returns UNRESOLVED. 285 and 286, in the same unit, are entered as carriers."),
 '285': (None,
  "Carrier line, checked by hand: haec ă-ĭt | ēt sē | cūm vēr | sāt quōs | dū-cĕ-rĕ | con-tra (14 syllables). The scanner's fit is correct; the entry is needed only because this line shares a unit with the half-line 10.284, which the scanner cannot fit, and a unit with an unresolved line receives no sc at all."),
 '286': (None,
  "Carrier line, checked by hand: vel quĭ-bŭs | ob-ses | sōs pos | sīt con | crē-dĕ-rĕ | mū-ros (14 syllables). The scanner's fit is correct; the entry is needed only because this line shares a unit with the half-line 10.284, which the scanner cannot fit, and a unit with an unresolved line receives no sc at all."),
 '287': (['1In–te⏑re⏑a', '2Ae–ne–3as–‖', 'so⏑ci⏑4os–', 'de–', '5pup–pi⏑bus⏑', '6al–tis×'],
  "Aeneas: Ae- is one long syllable, with Interea elided into it: In-tĕ-r(e) | (a) Ae-nē | ās sŏ-cĭ | ōs dē | pup-pĭ-bŭs | al-tis (15 syllables). The scanner (COSTLY 1.8, not flagged) split the initial diphthong into A-e, a fit with 16."),
 '309': (['1to–tam', 'a⏑ci⏑em', '2in–', 'Teu–3cros–‖', 'et–', '4con–tra', 'in–', '5li–to⏑re⏑', '6sis–tit×'],
  "Teucros " + EU + ": tō-t(am) ă-cĭ | (em) in Teu | crōs et | con-tr(a) in | lī-tŏ-rĕ | sis-tit (14 syllables). The scanner (cost 0.0, not flagged) split eu into Te-u, a fit with 15."),
 '311': (['1Ae–ne–2as–', 'o–3men–‖', 'pug–4nae–', 'stra–5vit–que⏑', 'La⏑6ti–nos×'],
  "Aeneas: Ae- is one long syllable: Ae-nē | ās ō | men pug | nae strā | vit-quĕ Lă | tī-nos (13 syllables). The scanner (COSTLY 1.2, not flagged) split the initial diphthong into A-e, a fit with 14."),
 '313': (['1Ae–ne–2an–', 'pe⏑tit⏑', '3huic–‖', 'gla⏑di⏑4o–', 'per–que', '5ae–re⏑a⏑', '6su–ta×'],
  "Aenean: Ae- is one long syllable, and huic one: Ae-nē | ān pĕ-tĭt | huic glă-dĭ | ō per | qu(e) ae-rĕ-ă | sū-ta (15 syllables); petit has a short i, so it is the present. The scanner (COSTLY 1.2, not flagged) split the initial diphthong into A-e, a fit with 16."),
 '316': (['1et–', 'ti⏑bi⏑', '2Phoe–be⏑', 'sa⏑3crum–‖', 'ca–4sus–', 'e–5va–de⏑re⏑', '6fer–ri×'],
  "Wrong quantities with the right count (COSTLY 0.6, not flagged). Phoebe is the vocative of Phoebus, with short final e; sacrum has a short a; casus is accusative plural, object of evadere, with long -ūs; evadere has a long ē: et tĭ-bĭ | Phoe-bĕ să | crum cā | sūs ē | vā-dĕ-rĕ | fer-ri (15 syllables). The scanner made Phoebe long-long, sa- long, casus long-short and e- short."),
 '332': (['1al–ma⏑', 'Ve⏑2nus–', 'Fi–dum', '3Ae–ne–4as–‖', 'ad–5fa–tur⏑', 'A⏑6cha–ten×'],
  "Aeneas: Ae- is one long syllable, with Fidum elided into it: al-mă Vĕ | nus fī | d(um) Ae-nē | ās ad | fā-tŭr Ă | chā-ten (14 syllables). The scanner (COSTLY 1.2, not flagged) split the initial diphthong into A-e, a fit with 15."),
 '337': (['1Mae–o⏑nis⏑', '2et–', 'tho–3ra–ca⏑', 'si⏑4mul–‖', 'cum–', '5pec–to⏑re⏑', '6rum–pit×'],
  "Wrong quantities with the right count (cost 0.0, no flag). thōrāca has long o and long a (Lewis & Short thōrax, ācis) and the short Greek accusative -a; simul has a short i: Mae-ŏ-nĭs | et thō | rā-că sĭ | mul cum | pec-tŏ-rĕ | rum-pit (15 syllables), caesura after simul. The scanner made tho-ra- short-short and ca si- long-long."),
 '343': (['1Ae–ne–2an–', 'pe⏑ti⏑3it–‖', 'sed–', '4non–', 'et–', '5fi–ge⏑re⏑', '6con–tra×'],
  "Aenean: Ae- is one long syllable: Ae-nē | ān pĕ-tĭ | it sed | nōn et | fī-gĕ-rĕ | con-tra (14 syllables). The scanner (COSTLY 1.5, not flagged) split the initial diphthong into A-e, a fit with 15."),
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
