#!/usr/bin/env python3
"""Reviewer helper (aeneid-080): append hand scansions for X.689-790 to scan-fixes.json, in line order after
the last existing key; keys are f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them. Checks each entry against the build's word-match rule and the
validator's metre rule (half-line rule when the why starts 'Half-line'). sc None = the scanner's own fit (carrier lines).
Dry run unless --write."""
import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
FP = os.path.join(A.HERE, 'scan-fixes.json')
raw = open(FP, encoding='utf8').read(); fx = json.loads(raw)
assert json.dumps(fx, ensure_ascii=False, indent=1) + '\n' == raw
P = A.part('aeneid-080'); LL = A.lines_of(P)
L = {str(l.get('label', l['n'])): l['t'] for l in LL}
order = [str(l.get('label', l['n'])) for l in LL]
own = lambda n: SL.scan_line(L[n])[1]
AE = "Ae- is one long syllable (diphthong), and -nē- is long"
CAR = "; the entry is needed only because this line shares a unit with {h}, which the scanner cannot fit, and a unit with an unresolved line receives no sc at all."
NEW = {
 '690': (['1suc–ce–2dit–', 'pug–3nae–‖', 'Teu–4cros–que', 'in–5va–dit⏑', 'o⏑6van–tis×'],
  "Teucros has Greek eu as one long syllable (as 10.44, 10.617, 10.684), and its -que elides before invadit: suc-cē | dit pug | nae Teu | crōs (que) in | vā-dĭt ŏ | vān-tis (13 syllables). The scanner (cost 0.0, not flagged) split eu into Te-u and made nae Te-u a dactyl."),
 '705': (['1Cis–se–2is–', 're–3gi–na⏑', 'Pa⏑4rin–‖', 'cre⏑at⏑', '5ur–be⏑', 'pa⏑6ter–na×'],
  "Cisseis is three syllables (Greek Κισσηΐς, as 7.320), its -is long by position before r-; regina (nominative) has a short final a and Paris a short Pa-: Cis-sē | īs rē | gī-nă Pă | rīn crĕ-ăt | ur-bĕ pă | ter-na (15 syllables). The scanner (cost 1.5, not flagged) read Cisseis as two syllables and made -na and Pa- long."),
 '712': (['1nec–', 'cui–quam', '2i–ras–3ci–‖', 'pro⏑pi⏑4us–que', 'ac–5ce–de⏑re⏑', '6vir–tus×'],
  "cuiquam is two syllables, cui one long syllable as everywhere in Virgil (as 7.692), its -quam elided before irasci: nec cui | (quam) ī-rās | cī prŏ-pĭ | us (que) ac | cē-dĕ-rĕ | vir-tus (14 syllables). The scanner (cost 0.0, not flagged) split cui into cŭ-ĭ and made the first foot a dactyl."),
 '724': (['1sua–det⏑', 'e⏑2nim–', 've–3sa–na⏑', 'fa⏑4mes–‖', 'si–', '5for–te⏑', 'fu⏑6ga–cem×'],
  "Wrong quantities with the right count (cost 1.5, not flagged), the same half-line as 9.340: vēsāna has its first two syllables long (vē- + sānus), its final a short (nominative, with fames), and fămēs a short first syllable: suā-dĕt ĕ | nĭm vē | sā-nă fă | mēs sī | for-tĕ fŭ | gā-cem (15 syllables), suadet two syllables with consonantal u. The scanner made ve-sa short and -na fa- long."),
 '726': (None, "Carrier line, checked by hand: gau-dĕt hĭ | āns im | mā-nĕ cŏ | mās (que) ar | rē-xĭt ĕt | hae-ret (15 syllables). The scanner's fit is correct" + CAR.format(h='the half-line 10.728')),
 '727': (None, "Carrier line, checked by hand: vis-cĕ-rĭ | būs sŭ-pĕr | ac-cum | bēns lă-vĭt | in-prŏ-bă | tae-ter (16 syllables). The scanner's fit is correct" + CAR.format(h='the half-line 10.728')),
 '728': (['1o–ra⏑', 'cru⏑2or×'],
  "Half-line (hemistich), one of Virgil's unfinished lines, as 10.490 and 10.580: ō-ră crŭ | or, a dactyl and one syllable (– ⏑ ⏑ | ×), ōra long, cruor two syllables with a short cru-, the last syllable marked × as the end of the line (4 syllables). There is no hexameter to fit; the scanner returns UNRESOLVED. 726, 727 and 729, in the same unit, are entered as carriers."),
 '729': (None, "Carrier line, checked by hand: sīc rŭ-ĭt | in den | sōs ă-lă | cer Mē | zen-tĭ-ŭs | hos-tis (15 syllables). The scanner's fit is correct" + CAR.format(h='the half-line 10.728')),
 '743': (['1Nunc–', 'mo⏑re⏑re', '2Ast–', 'de–', '3me–‖', 'di–4vom–', 'pa⏑ter⏑', '5at–que', 'ho⏑mi⏑6num–', 'rex×'],
  "Wrong quantities with the right count (cost 0.3, not flagged). de and me are long (dē, mē), and pater is two shorts: Nunc mŏ-rĕ | r(e) āst dē | mē dī | vōm pă-tĕr | āt-qu(e) hŏ-mĭ | nūm rex (15 syllables), morere elided into Ast across the stop. The scanner made dē and mē short and both syllables of pater long."),
 '745': (['1ol–li–', '2du–ra⏑', 'qui⏑3es–‖', 'o⏑cu⏑4los–', 'et–', '5fer–re⏑us⏑', '6ur–get×'],
  "quies is two syllables, quĭ-ēs (as 1.723, 3.495, 7.598), and dura (nominative, with quies) has a short final a: ol-lī | dū-ră quĭ | ēs ŏ-cŭ | lōs et | fer-rĕ-ŭs | ur-get (15 syllables). The scanner (cost 0.0, not flagged) read quies as one syllable and made -ra long."),
 '753': (['1de–i⏑cit⏑', '2at–', 'Thro⏑ni⏑3um–‖', 'Sa⏑li⏑4us–', 'Sa⏑li⏑5um–que⏑', 'Ne⏑6al–ces×'],
  "deicit is three syllables, dē-ĭ-cit (dē + iacio, as 8.428), and its -cit is short before at: dē-ĭ-cĭt | at Thrŏ-nĭ | um Să-lĭ | us Să-lĭ | um-quĕ Nĕ | al-ces (17 syllables), five dactyls. The scanner (cost 1.8, not flagged) read dei- as one syllable and made -cit long before a vowel."),
 '769': (['1Huic–', 'con–tra', '2Ae–ne–3as–‖', 'spe⏑cu⏑4la–tus⏑', 'in⏑', '5ag–mi⏑ne⏑', '6lon–go×'],
  "Aenēās: " + AE + ", -ās long, and contra elides into it: Huic con | tr(a) Ae-nē | ās spĕ-cŭ | lā-tŭs ĭn | ag-mĭ-nĕ | lon-go (15 syllables), huic one syllable. The scanner (cost 1.2, not flagged) split the initial Ae into A-e."),
 '776': (['1Ae–ne–2ae–', 'Di–3xit–‖', 'stri–4den–tem–que', '5e–mi⏑nus⏑', '6has–tam×'],
  "Aenēae: " + AE + ": Ae-nē | ae Dī | xit stri | den-tem | (que) ē-mĭ-nŭs | has-tam (13 syllables), the -que of stridentemque elided into eminus; the stray closing mark of the print (rule 5b) does not affect the words. The scanner (cost 1.2, not flagged) split the initial Ae into A-e."),
 '781': (['1Ster–ni⏑tur⏑', '2in–fe–3lix–‖', 'a⏑li⏑4e–no–', '5vol–ne⏑re⏑', '6cae–lum×que'],
  "Hypermetric line (as 4.558, 5.753, 6.602, 8.228): the last -que of caelumque elides into aspicit, the first word of 782, so the line has sixteen syllables and fifteen count: Ster-nĭ-tŭr | in fē | līx ă-lĭ | ē-nō | vol-nĕ-rĕ | cae-lum(que). The final -que is not counted and is left unmarked, the end mark × on lum. The scanner cannot elide across a line end and returned UNRESOLVED. 782, in the same unit, is entered as a carrier."),
 '782': (None, "Carrier line, checked by hand: as-pĭ-cĭt | et dul | cīs mŏ-rĭ | ens rĕ-mĭ | nis-cĭ-tŭr | Ar-gos (16 syllables), the -que of caelumque (781) elided into its first syllable. The scanner's fit is correct" + CAR.format(h='the hypermetric 10.781')),
 '783': (['1tum–', 'pi⏑us⏑', '2Ae–ne–3as–‖', 'has–4tam–', 'ia⏑cit⏑', '5il–la⏑', 'per⏑', '6or–bem×'],
  "Aenēās: " + AE + ", -ās long: tum pĭ-ŭs | Ae-nē | ās has | tam iă-cĭt | il-lă pĕr | or-bem (15 syllables), iacit with consonantal i. The scanner (cost 1.2, not flagged) split the initial Ae into A-e."),
 '787': (['1Ae–ne–2as–', 'vi–3so–‖', 'Tyr–4rhe–ni–', '5san–gui⏑ne⏑', '6lae–tus×'],
  "Aenēās: " + AE + ", -ās long: Ae-nē | ās vī | sō Tyr | rhē-nī | san-guĭ-nĕ | lae-tus (13 syllables). The scanner (cost 1.2, not flagged) split the initial Ae into A-e."),
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
    m = re.search(r'\((\d+) syllables', why)
    if m: assert int(m.group(1)) == syl, (k, syl)
    else: assert 'fifteen count' in why and syl == 15, (k, syl)
    out[k] = {'sc': sc, 'why': why}
    print(k, syl, ' '.join(sc))
assert len(out) == len(fx) + len(NEW)
if '--write' in sys.argv:
    open(FP, 'w', encoding='utf8').write(json.dumps(out, ensure_ascii=False, indent=1) + '\n'); print('written')
