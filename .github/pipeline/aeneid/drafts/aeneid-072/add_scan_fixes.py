#!/usr/bin/env python3
"""Reviewer helper (aeneid-072): append hand scansions for X.1-95 to scan-fixes.json, in line order after
the last existing key; keys are f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them
(so the half-line 'Tum regia Iuno' is 10.62b). Checks each entry against the build's word-match rule and the
validator's metre rule (half-line rule when the why starts 'Half-line'). Dry run unless --write."""
import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
FP = os.path.join(A.HERE, 'scan-fixes.json')
raw = open(FP, encoding='utf8').read(); fx = json.loads(raw)
assert json.dumps(fx, ensure_ascii=False, indent=1) + '\n' == raw
P = A.part('aeneid-072'); LL = A.lines_of(P)
L = {str(l.get('label', l['n'])): l['t'] for l in LL}
order = [str(l.get('label', l['n'])) for l in LL]
own = lambda n: SL.scan_line(L[n])[1]
EU = "has Greek eu as one long syllable"
NEW = {
 '6': (['1Cae–li⏑co⏑2lae–', 'mag–3ni–‖', 'qui⏑a⏑4nam–', 'sen–5ten–ti⏑a⏑', '6vo–bis×'],
  "quianam is three syllables, quĭ-ă-nam (as Heu quianam, 5.13): Cae-lĭ-cŏ | lae mag | nī quĭ-ă | nam sen | ten-tĭ-ă | vō-bis (15 syllables), caesura after magni. The scanner (no flag) ran qui-a together into one long syllable, a fit with 14."),
 '16': (None, "Carrier line, checked by hand: Iup-pĭ-tĕr | haec pau | cīs at | nōn Vĕ-nŭs | au-rĕ-ă | con-tra (15 syllables), the scanner's own fit. Listed because it shares a unit with the half-line 17, which the scanner cannot fit, and a unit with an unresolved line receives no sc at all."),
 '17': (['1pau–ca⏑', 're⏑2fert×'],
  "Half-line (hemistich), one of Virgil's unfinished lines: pau-că rĕ | fert, a dactyl and one syllable (– ⏑ ⏑ | ×), 4 syllables. The last syllable is marked × as the end of the line. There is no hexameter to fit; the scanner returns UNRESOLVED."),
 '18': (['1O–', 'pa⏑ter⏑', '2O–', 'ho⏑mi⏑3num–‖', 're–4rum–que', 'ae–5ter–na⏑', 'po⏑6tes–tas×'],
  "The interjection O is never elided: Ō pă-tĕr | Ō hŏ-mĭ | num rē | rum-qu(e) ae | ter-nă pŏ | tes-tas (15 syllables), only rerumque elided. The scanner (no flag) elided the second O and lengthened ho-mi, a fit with 14."),
 '20': (['1Cer–nis⏑', 'ut⏑', '2in–sul–3tent–‖', 'Ru⏑tu⏑4lli–', 'Tur–5nus–que⏑', 'fe⏑6ra–tur×'],
  "The print has Rutulli, a misprint for Rutuli; the tokens spell the line as printed (the build matches the words of the line), but it is scanned as Rutuli, Rŭ-tŭ-lī, with the stray l carried on the last syllable: Cer-nĭs ŭt | in-sul | tent Rŭ-tŭ | lī Tur | nus-quĕ fĕ | rā-tur (15 syllables), caesura after insultent. The scanner returns UNRESOLVED, since the double l makes -tul- long and no hexameter fits."),
 '21': (None, "Carrier line, checked by hand: per mĕ-dĭ | ōs in | sig-nĭs ĕ | quīs tŭ-mĭ | dus-quĕ sĕ | cun-do (16 syllables), the scanner's own fit. Listed because it shares a unit with line 20, which the scanner cannot fit (the misprint Rutulli), and a unit with an unresolved line receives no sc at all."),
 '22': (None, "Carrier line, checked by hand: Mar-tĕ rŭ | at nōn | clau-să tĕ | gunt iam | moe-nĭ-ă | Teu-cros (15 syllables), the scanner's own fit, Teucros with eu as one syllable. Listed because its first words (Marte ruat) share a unit with line 20, which the scanner cannot fit, and a unit with an unresolved line receives no sc at all."),
 '25': (['1Ae–ne–2as–', 'ig–3na–rus⏑', 'a⏑4best–‖', 'Num–5quam–ne⏑', 'le⏑6va–ri×'],
  "Aenēās: Ae- is one long syllable (diphthong), -nē- and -ās long: Ae-nē | ās ig | nā-rŭs ă | best Num | quam-nĕ lĕ | vā-ri (14 syllables). The scanner (COSTLY 1.2, not flagged) split the initial diphthong into A-e, a fit with 15."),
 '26': (['1ob–si⏑di⏑2o–ne⏑', 'si⏑3nes–‖', 'Mu–4ris–', 'i⏑te⏑rum', '5im–mi⏑net⏑', '6hos–tis×'],
  "Wrong quantities with the right count (no flag). mūrīs (ablative/dative plural of mūrus) is long-long and ĭtĕrum short-short: ob-sĭ-dĭ | ō-nĕ sĭ | nēs mū | rīs ĭ-tĕ | r(um) im-mĭ-nĕt | hos-tis (16 syllables). The scanner made Mu-ris short-short and i-te- long-long."),
 '28': (['1at–que', 'i⏑te⏑rum', '2in–', 'Teu–3cros–‖', 'Ae–4to–lis–', '5sur–git⏑', 'ab⏑', '6Ar–pis×'],
  "Teucros " + EU + ": at-qu(e) ĭ-tĕ | r(um) in Teu | crōs Ae | tō-līs | sur-gĭt ăb | Ar-pis (14 syllables); Aetolis has Ae- as one syllable. The scanner (no flag) split Te-u into two short syllables, a fit with 15."),
 '44': (['1Si–', 'nul–la', '2est–', 're⏑gi⏑3o–‖', 'Teu–4cris–', 'quam–', '5det–', 'tu⏑a⏑', '6co–niunx×'],
  "Teucris " + EU + ", and coniunx is con-iunx with consonantal i: sī nūl | l(a) est rĕ-gĭ | ō Teu | crīs quam | dēt tŭ-ă | con-iunx (14 syllables). The scanner (COSTLY 1.5, not flagged) split Te-u into two short syllables, a fit with 15."),
 '48': (['1Ae–ne–2as–', 'sa–ne', '3ig–no–4tis–‖', 'iac–5te–tur⏑', 'in⏑', '6un–dis×'],
  "Aenēās: Ae- is one long syllable, and sane is elided into ignotis: Ae-nē | ās sā | n(e) ig-nō | tīs iac | tē-tŭr ĭn | un-dis (13 syllables). The scanner (COSTLY 1.2, not flagged) split the initial diphthong into A-e and shortened -nē-, a fit with 14."),
 '58': (['1dum–', 'La⏑ti⏑2um–', 'Teu–3cri–‖', 're⏑ci⏑4di–va⏑que⏑', '5Per–ga⏑ma⏑', '6quae–runt×'],
  "Teucri " + EU + ": dum Lă-tĭ | um Teu | crī rĕ-cĭ | dī-vă-quĕ | Per-gă-mă | quae-runt (16 syllables), rĕcĭdīva as at 4.344. The scanner (no flag) split Te-u into two short syllables, a fit with 17."),
 '62': (['1da–', 'pa⏑ter⏑', '2I–li⏑a⏑3cos–', 'Teu–4cris×'],
  "Half-line (hemistich), the first half of the shared line 62: dā pă-tĕr | Ī-lĭ-ă | cōs Teu | crīs, two dactyls, a spondee and one syllable (– ⏑ ⏑ | – ⏑ ⏑ | – – | ×), 9 syllables; Teucris has eu as one syllable. The last syllable is marked × as the end of Venus's speech. Greenough sets 'Tum regia Iuno' as a separate half-line, 62b, which completes the hexameter (crīs Tum | rē-gĭ-ă | Iū-nō); the scanner, seeing each piece alone, returns UNRESOLVED."),
 '62b': (['1Tum–', '2re–gi⏑a⏑', '3Iu–no×'],
  "Half-line (hemistich), the second half of the shared line 62: Tum | rē-gĭ-ă | Iū-nō, one long syllable, a dactyl and a spondee (– | – ⏑ ⏑ | – ×), 6 syllables, numbered from this half-line's start as the validator requires; in the full verse, with da, pater, Iliacos Teucris (62), they are the fourth to sixth feet: crīs Tum | rē-gĭ-ă | Iū-nō. The scanner returns UNRESOLVED."),
 '65': (['1Ae–ne–2an–', 'ho⏑mi⏑3num–‖', 'quis–4quam–', 'di–5vom–que⏑', 'su⏑6be–git×'],
  "Wrong quantities with the right count (no flag). Aenēān, Greek accusative (Αἰνείαν), has Ae- one syllable and long -nē- and -ān: Ae-nē | ān hŏ-mĭ | num quis | quam dī | vom-quĕ sŭ | bē-git (14 syllables). The scanner made -ne- and -an short and ho-mi long-long."),
 '81': (['1Tu–', 'po⏑tes⏑', '2Ae–ne–3an–‖', 'ma⏑ni⏑4bus–', 'sub–5du–ce⏑re⏑', '6Gra–ium×'],
  "Aenēān: Ae- is one long syllable: Tū pŏ-tĕs | Ae-nē | ān mă-nĭ | bus sub | dū-cĕ-rĕ | Grā-ium (15 syllables), Graium two syllables with consonantal i. The scanner (COSTLY 1.2, not flagged) split the initial diphthong into A-e, a fit with 16."),
 '85': (['1Ae–ne–2as–', 'ig–3na–rus⏑', 'a⏑4best–‖', 'ig–5na–rus⏑', 'et⏑', '6ab–sit×'],
  "Aenēās: Ae- is one long syllable (as 25, which this line repeats): Ae-nē | ās ig | nā-rŭs ă | best ig | nā-rŭs ĕt | ab-sit (14 syllables). The scanner (COSTLY 1.2, not flagged) split the initial diphthong into A-e, a fit with 15."),
 '89': (['1co–na–2mur–', 'nos–', '3an–‖', 'mi⏑se⏑4ros–', 'qui–', '5Tro–as⏑', 'A⏑6chi–vis×'],
  "Trōăs is two syllables, long-short (Greek Τρῶας), qui is long, and Ăchīvis has a short A- and long -chī-: cō-nā | mur nōs | an mĭ-sĕ | rōs quī | Trō-ăs Ă | chī-vis (14 syllables). The scanner (COSTLY 2.8) had the count right but made qui and Tro- short and -as and A- long."),
 '90': (['1ob–ie–2cit–', 'Quae–', '3cau–sa⏑', 'fu⏑4it–‖', 'con–5sur–ge⏑re', 'in⏑', '6ar–ma×'],
  "obiecit is ob-iē-cit: the i after the prefix is consonantal, so ob- is long by position: ob-iē | cīt quae | cau-să fŭ | it con | sur-gĕ-r(e) ĭn | ar-ma (14 syllables). The scanner (no flag) read the i as a vowel, o-bi-e-cit, a fit with 15."),
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
