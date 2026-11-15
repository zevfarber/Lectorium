#!/usr/bin/env python3
"""Reviewer helper (aeneid-078): append hand scansions for X.510-605 to scan-fixes.json, in line order after
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
P = A.part('aeneid-078'); LL = A.lines_of(P)
L = {str(l.get('label', l['n'])): l['t'] for l in LL}
order = [str(l.get('label', l['n'])) for l in LL]
own = lambda n: SL.scan_line(L[n])[1]
AE = "Aenēās: Ae- is one long syllable (diphthong), and -nē- and -ās are long"
NEW = {
 '511': (['1ad–vo⏑lat⏑', '2Ae–ne–3ae–‖', 'te⏑nu⏑4i–', 'dis–5cri–mi⏑ne⏑', '6le–ti×'],
  "Aenēae: Ae- is one long syllable (diphthong), -nē- long: ad-vŏ-lăt | Ae-nē | ae tĕ-nŭ | ī dis | crī-mĭ-nĕ | lē-ti (15 syllables), caesura after Aeneae. The scanner (COSTLY 1.2, not flagged) split the initial Ae into A-e and made a dactyl of it."),
 '515': (['1cae–de⏑', 'no⏑2va–', 'quae–3rens–‖', 'Pal–4las–', 'Eu–5an–der⏑', 'in⏑', '6ip–sis×'],
  "Euander has Greek eu as one long syllable (as Euandro at 10.492): cae-dĕ nŏ | vā quae | rens Pal | lās Eu | an-dĕr ĭn | ip-sis (14 syllables). The scanner (cost 0.0, not flagged) split E-u and made las E-u a dactyl."),
 '524': (['1Per–', 'pa⏑tri⏑2os–', 'ma–3nis–‖', 'et–', '4spes–', 'sur–5gen–tis⏑', 'I⏑6u–li×'],
  "Iuli is three syllables, Ĭ-ū-lī, the I a vowel (as cognomen Iulo, 1.267; per spes surgentis Iuli, 6.364): Per pă-trĭ | ōs mā | nīs et | spēs sur | gen-tĭs Ĭ | ū-li (14 syllables). The scanner (COSTLY 2.0, flagged) read Iu- as one syllable with consonantal i and made the fifth foot a spondee, a fit with 13."),
 '530': (['1Di–xe⏑rat⏑', '2Ae–ne–3as–‖', 'con–4tra–', 'cui–', '5ta–li⏑a⏑', '6red–dit×'],
  AE + ": Dī-xĕ-răt | Ae-nē | ās con | trā cui | tā-lĭ-ă | red-dit (14 syllables), cui one syllable. The scanner (COSTLY 1.2, not flagged) split the initial Ae."),
 '534': (['1Hoc–', 'pa⏑tris⏑', '2An–chi–3sae–‖', 'ma–4nes–', 'hoc–', '5sen–tit⏑', 'I⏑6u–lus×'],
  "Iulus is three syllables, Ĭ-ū-lus, as at 10.524: Hōc pă-trĭs | An-chī | sae mā | nēs hōc | sen-tĭt Ĭ | ū-lus (14 syllables). The scanner (COSTLY 2.0, flagged) read Iu- as one syllable and made the fifth foot a spondee, a fit with 13."),
 '536': (['1cer–vi–ce', '2o–ran–3tis–‖', 'ca⏑pu⏑4lo–', 'te⏑nus⏑', '5ap–pli⏑cat⏑', '6en–sem×'],
  "Wrong quantities with the right count (cost 0.0, not flagged). cervīce has a long i, ōrantis a long o, and capulo is short-short-long (căpŭlō): cer-vī | c(e) ō-ran | tis că-pŭ | lō tĕ-nŭs | ap-plĭ-căt | en-sem (15 syllables), caesura after orantis. The scanner made vi and o short and ca and pu long."),
 '538': (['1in–fu⏑la⏑', '2cui–', 'sa–3cra–‖', 're⏑di⏑4mi–bat–', '5tem–po⏑ra⏑', '6vit–ta×'],
  "Wrong quantities with the right count (cost 0.0, not flagged). sacra is the ablative sacrā with vitta, its first syllable long by position before cr, and redimibat is rĕ-dĭ-mī-bat (old imperfect, long ī): in-fŭ-lă | cui să | crā rĕ-dĭ | mī-bat | tem-pŏ-ră | vit-ta (15 syllables), caesura after sacra. The scanner made sa-cra short-short and re-di long-long, which redimio cannot have."),
 '569': (['1sic–', 'to–to', '2Ae–ne–3as–‖', 'de–4sae–vit⏑', 'in⏑', '5ae–quo⏑re⏑', '6vic–tor×'],
  AE + ", and toto elides into it: sīc tō | t(o) Ae-nē | ās dē | sae-vĭt ĭn | ae-quŏ-rĕ | vic-tor (14 syllables). The scanner (COSTLY 1.2, not flagged) split the initial Ae."),
 '571': (['1qua–dri⏑iu⏑2gis–', 'in⏑', 'e⏑3quos–‖', 'ad–4ver–sa⏑que⏑', '5pec–to⏑ra⏑', '6ten–dit×'],
  "quadriiugis is quā-drĭ-jŭ-gīs, four syllables, quadri- + iugum with the second i consonantal (as biiugis at 10.453): quā-drĭ-jŭ | gīs ĭn ĕ | quōs ad | ver-să-quĕ | pec-tŏ-ră | ten-dit (16 syllables). The scanner (COSTLY 1.5, not flagged) ran quadri- into one syllable, a fit with 15."),
 '575': (['1In–te⏑re⏑2a–', 'bi⏑iu⏑3gis–‖', 'in–4fert–', 'se–', '5Lu–ca⏑gus⏑', '6al–bis×'],
  "biiugis is bĭ-jŭ-gīs, three syllables, the second i consonantal and bi- short, as at 10.453: In-tĕ-rĕ | ā bĭ-jŭ | gīs in | fert sē | Lū-că-gŭs | al-bis (15 syllables), caesura after biiugis. The scanner (COSTLY 2.1, flagged) ran bi-iu together into one long syllable, a fit with 14."),
 '578': (['1Haud–', 'tu⏑lit⏑', '2Ae–ne–3as–‖', 'tan–4to–', 'fer–5vo–re⏑', 'fu⏑6ren–tis×'],
  AE + ": Haud tŭ-lĭt | Ae-nē | ās tan | tō fer | vō-rĕ fŭ | ren-tis (14 syllables). The scanner (COSTLY 1.2, not flagged) split the initial Ae."),
 '580': (['1Cui–', 'Li⏑ger×'],
  "Half-line (hemistich), one of Virgil's unfinished lines, as 10.284 and 10.490: Cui Lĭ-ger, cui one long syllable and the short Li of Liger (as 9.571), the last syllable marked × as the end of the line (3 syllables). There is no hexameter to fit; the scanner returns UNRESOLVED. 581, 582 and 583, in the same unit, are entered as carriers."),
 '581': (None,
  "Carrier line, checked by hand: Nōn Dĭ-ŏ | mē-dĭs ĕ | quōs nec | cur-rum | cer-nĭs Ă | chil-lis (15 syllables). The scanner's fit is correct; the entry is needed only because this line shares a unit with the half-line 10.580, which the scanner cannot fit, and a unit with an unresolved line receives no sc at all."),
 '582': (None,
  "Carrier line, checked by hand: aut Phrў-gĭ | ae cam | pōs nunc | bel-lī | fī-nĭs ĕt | ae-vi (14 syllables). The scanner's fit is correct; the entry is needed only because this line shares a unit with the half-line 10.580, which the scanner cannot fit, and a unit with an unresolved line receives no sc at all."),
 '583': (None,
  "Carrier line, checked by hand: hīs dă-bĭ | tur ter | rīs Vē | sā-nō | tā-lĭ-ă | lā-te (14 syllables). The scanner's fit is correct; the entry is needed only because the first words of this line close a unit with the half-line 10.580, which the scanner cannot fit, and a unit with an unresolved line receives no sc at all."),
 '587': (['1ad–mo⏑nu⏑2it–', 'bi⏑iu⏑3gos–‖', 'pro–4iec–to–', '5dum–', 'pe⏑de⏑', '6lae–vo×'],
  "biiugos is bĭ-jŭ-gōs, three syllables, as at 10.575; proiecto has consonantal i after the prefix, prō-jec-tō: ad-mŏ-nŭ | it bĭ-jŭ | gōs prō | iec-tō | dum pĕ-dĕ | lae-vo (15 syllables), caesura after biiugos. The scanner (COSTLY 1.5, not flagged) ran bi-iu together, a fit with 14."),
 '591': (['1Quem–', 'pi⏑us⏑', '2Ae–ne–3as–‖', 'dic–4tis–', 'ad–5fa–tur⏑', 'a⏑6ma–ris×'],
  AE + ": Quem pĭ-ŭs | Ae-nē | ās dic | tīs ad | fā-tŭr ă | mā-ris (14 syllables). The scanner (COSTLY 1.2, not flagged) split the initial Ae."),
 '595': (['1ar–ri⏑pu⏑2it–', 'bi⏑iu⏑3gos–‖', 'fra–4ter–', 'ten–5de–bat⏑', 'i⏑6ner–tis×'],
  "biiugos is bĭ-jŭ-gōs, three syllables, as at 10.575: ar-rĭ-pŭ | it bĭ-jŭ | gōs frā | ter ten | dē-băt ĭ | ner-tis (15 syllables), caesura after biiugos. The scanner (COSTLY 1.5, not flagged) ran bi-iu together, a fit with 14."),
 '599': (['1Plu–ri⏑bus⏑', '2o–ran–ti', '3Ae–ne–4as–‖', 'Haud–', '5ta–li⏑a⏑', '6du–dum×'],
  AE + ", and oranti elides into it: Plū-rĭ-bŭs | ō-ran | t(i) Ae-nē | ās Haud | tā-lĭ-ă | dū-dum (14 syllables), caesura after Aeneas. The scanner (COSTLY 1.2, not flagged) split the initial Ae."),
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
