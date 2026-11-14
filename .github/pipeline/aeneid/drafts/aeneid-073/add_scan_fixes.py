#!/usr/bin/env python3
"""Reviewer helper (aeneid-073): append hand scansions for X.96-184 to scan-fixes.json, in line order after
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
P = A.part('aeneid-073'); LL = A.lines_of(P)
L = {str(l.get('label', l['n'])): l['t'] for l in LL}
order = [str(l.get('label', l['n'])) for l in LL]
own = lambda n: SL.scan_line(L[n])[1]
EU = "has Greek eu as one long syllable"
NEW = {
 '105': (['1Quan–do⏑qui⏑dem', '2Au–so⏑ni⏑3os–‖', 'con–4iun–gi–', '5foe–de⏑re⏑', '6Teu–cris×'],
  "coniungi is con-iun-gi: the i after the prefix is consonantal, so con- is long by position; Teucris " + EU + ": Quan-dŏ-quĭ | d(em) Au-sŏ-nĭ | ōs con | iun-gī | foe-dĕ-rĕ | Teu-cris (15 syllables), caesura after Ausonios. The scanner (COSTLY 1.5, not flagged) read the i as a vowel, co-ni-un-gi, with the right count but short co-."),
 '107': (['1quae–', 'cui–que', '2est–', 'for–3tu–na', 'ho⏑di⏑4e–‖', 'quam–', '5quis–que⏑', 'se⏑6cat–', 'spem×'],
  "cuique is two syllables, cui- one long syllable, as at 111 in the same speech and in quae cuique est copia (5.100): quae cui | qu(e) est for | tū-n(a) hŏ-dĭ | ē quam | quis-quĕ sĕ | cat spem (14 syllables). The scanner (COSTLY 0.6, not flagged) made cuique three syllables, cŭ-ĭ-que, a fit with 15."),
 '109': (['1Seu–', 'fa–2tis–', 'I⏑ta⏑3lum–‖', 'cas–tra', '4ob–si⏑di⏑5o–ne⏑', 'te⏑6nen–tur×'],
  "Wrong quantities with the right count (no flag). fātīs (ablative plural of fātum) is long-long, and Ĭtălum has a short I- here, the only fit (as at 10.41): Seu fā | tīs Ĭ-tă | lum cas | tr(a) ob-sĭ-dĭ | ō-nĕ tĕ | nen-tur (15 syllables). The scanner made fa-tis short-short and I-ta long-long."),
 '123': (['1A–si⏑us⏑', '2Im–bra⏑si⏑3des–‖', 'Hi⏑ce⏑4ta–o⏑ni⏑5us–que⏑', 'Thy⏑6moe–tes×'],
  "Hicetaonius (Greek Ἱκετάων, short ι and ε, long ᾱ) is Hĭ-cĕ-tā-ŏ-nĭ-us, six syllables, and the line runs five dactyls: Ā-sĭ-ŭs | Im-bră-sĭ | dēs Hĭ-cĕ | tā-ŏ-nĭ | us-quĕ Thy̆ | moe-tes (17 syllables). The scanner (COSTLY 1.5, not flagged) lengthened Hi-ce- and ran -nius into one syllable, a fit with 16."),
 '136': (['1in–clu–2sum–', 'bu–3xo–‖', 'aut–', '4O–ri⏑ci⏑5a–', 'te⏑re⏑6bin–tho×'],
  "Hiatus: buxo is not elided before aut (the long o stays long, at the main caesura, as Samo hic at 1.16): in-clū | sum bux | ō aut | Ō-rĭ-cĭ | ā tĕ-rĕ | bin-tho (14 syllables), with Ōrĭcĭā (ablative, with terebintho) and tĕrĕbinthō (Greek τερέβινθος) in their natural quantities. The scanner (COSTLY 2.0, flagged) elided buxo and made the -ri- of Oricia long and te-re- long-long, a fit with 13."),
 '141': (['1Mae–o⏑ni⏑2a–', 'ge⏑ne⏑3ro–se⏑', 'do⏑4mo–‖', 'u⏑bi⏑', '5pin–gui⏑a⏑', '6cul–ta×'],
  "Hiatus: domo is not elided before ubi (the long o stays long, at the caesura after the fourth arsis): Mae-ŏ-nĭ | ā gĕ-nĕ | rō-sĕ dŏ | mō ŭ-bĭ | pin-guĭ-ă | cul-ta (17 syllables), with gĕnĕrōsĕ in its natural quantities. With the elision there are four short syllables running (-sĕ dŏ-m(o) ŭ-bĭ) and no fit under natural quantities. The scanner (COSTLY 1.0, not flagged) elided domo and lengthened ge-ne- and do-, shortening -ro-."),
 '147': (['1con–tu⏑le⏑2rant–', 'me⏑di⏑a', '3Ae–ne–4as–‖', 'fre⏑ta⏑', '5noc–te⏑', 'se⏑6ca–bat×'],
  "Aenēās: Ae- is one long syllable, and media is elided into it: con-tŭ-lĕ | rant mĕ-dĭ | (a) Ae-nē | ās frĕ-tă | noc-tĕ sĕ | cā-bat (16 syllables). The scanner (COSTLY 1.2, not flagged) split the initial diphthong into A-e, a fit with 17."),
 '156': (['1ex–ter–2no–', 'com–3mis–sa⏑', 'du⏑4ci–‖', 'Ae–5ne–i⏑a⏑', '6pup–pis×'],
  "Hiatus across the full stop: duci is not elided before Aeneia (as colo. Huc at 5.735); Aenēĭa as at 7.1 (Aeneia nutrix), with Ae- one long syllable: ex-ter | nō com | mis-să dŭ | cī Ae | nē-ĭ-ă | pup-pis (14 syllables). With the elision there are 13 syllables and no fit under natural quantities. The scanner (COSTLY 1.0, not flagged) elided duci and lengthened commissa's -a and du-."),
 '157': (['1pri–ma⏑', 'te⏑2net–', 'ros–3tro–‖', 'Phry⏑gi⏑4os–', 'sub–5iunc–ta⏑', 'le⏑6o–nes×'],
  "subiuncta is sub-iunc-ta: the i after the prefix is consonantal, so sub- is long by position: prī-mă tĕ | net rōs | trō Phry̆-gĭ | ōs sub | iunc-tă lĕ | ō-nes (15 syllables). The scanner (no flag) read the i as a vowel, su-bi-unc-ta, a fit with 16."),
 '159': (['1Hic–', 'mag–2nus–', 'se⏑det⏑', '3Ae–ne–4as–‖', 'se–5cum–que⏑', 'vo⏑6lu–tat×'],
  "Aenēās: Ae- is one long syllable: Hic mag | nus sĕ-dĕt | Ae-nē | ās sē | cum-quĕ vŏ | lū-tat (14 syllables). The scanner (COSTLY 1.2, not flagged) split the initial diphthong into A-e, a fit with 15."),
 '165': (['1Ae–ne–2an–', 'ar–3met–que⏑', 'ra⏑4tes–‖', 'pe⏑la⏑5go–que⏑', 've⏑6ha–tur×'],
  "Wrong quantities with the right count (COSTLY 0.6, not flagged). Aenēān, Greek accusative, has Ae- one syllable and long -nē- and -ān (as 10.65): Ae-nē | ān ar | met-quĕ ră | tēs pĕ-lă | gō-quĕ vĕ | hā-tur (15 syllables). The scanner made -ne-an short-short and -que ra- long-long."),
 '179': (['1Hos–', 'pa–2re–re⏑', 'iu⏑3bent–‖', 'Al–4phe–ae', 'ab⏑', 'o⏑5ri–gi⏑ne⏑', '6Pi–sae×'],
  "Alphēae (Ἀλφειός) is elided before ab: Hōs pā | rē-rĕ iŭ | bent Al | phē(ae) ăb ŏ | rī-gĭ-nĕ | Pī-sae (15 syllables). The scanner (COSTLY 1.5, not flagged) got the same feet another way, running -eae into one syllable by synizesis and leaving ab in hiatus; the entry gives the ordinary elision, as the note does."),
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
