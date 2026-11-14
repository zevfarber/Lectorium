#!/usr/bin/env python3
"""Reviewer helper (aeneid-071): append hand scansions for IX.717-818 to scan-fixes.json, in line order after
the last existing key; checks each entry against the build's word-match rule and the validator's metre rule."""
import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
FP = os.path.join(A.HERE, 'scan-fixes.json')
raw = open(FP, encoding='utf8').read(); fx = json.loads(raw)
assert json.dumps(fx, ensure_ascii=False, indent=1) + '\n' == raw
P = A.part('aeneid-071'); L = {l['n']: l['t'] for l in A.lines_of(P)}
own = lambda n: SL.scan_line(L[n])[1]
NEW = {
 719: (['1im–mi–2sit–que⏑', 'Fu⏑3gam–‖', 'Teu–4cris–', 'a–5trum–que⏑', 'Ti⏑6mo–rem×'],
  "Teucris has Greek eu as one long syllable (as 9.510 and 9.516): im-mī | sit-quĕ Fŭ | gam Teu | crīs ā | trum-quĕ Tĭ | mō-rem (14 syllables). The scanner (no flag) split Te-u into two short syllables, a fit with 15."),
 721: (['1bel–la–2tor–que', 'a⏑ni⏑3mo–', 'de⏑us⏑', '4in–ci⏑dit×'],
  "Half-line (hemistich), one of Virgil's unfinished lines: bel-lā | tōr-qu(e) ă-nĭ | mō dĕ-ŭs | in-cĭ-dit, a spondee and three dactyls (– – | – ⏑ ⏑ | – ⏑ ⏑ | – ⏑ ×), 11 syllables; -que is elided into animo, animō is the dative with long -ō, and deus is two short syllables. The last syllable is marked × as the end of the line. There is no hexameter to fit; the scanner forced one (COSTLY 8.4) by lengthening a-ni and de-us."),
 725: (['1ob–ni–2xus–', 'la–3tis–‖', 'u⏑me⏑4ris–', 'mul–5tos–que⏑', 'su⏑6o–rum×'],
  "Wrong quantities with the right count (no flag). lātīs (lātus, 'broad') is long-long and ŭmĕrīs has two short syllables: ob-nī | xus lā | tīs ŭ-mĕ | rīs mul | tōs-quĕ sŭ | ō-rum (14 syllables), caesura after latis. The scanner made la-tis short-short and u-me long-long."),
 756: (['1Dif–fu⏑gi⏑2unt–', 'ver–3si–‖', 'tre⏑pi⏑4da–', 'for–5mi–di⏑ne⏑', '6Tro–es×'],
  "Trōĕs is two syllables (Greek nominative plural, as 9.689), and trĕpĭdā has two short syllables before the long ablative -ā: Dif-fŭ-gĭ | unt ver | sī trĕ-pĭ | dā for | mī-dĭ-nĕ | Trō-ĕs (15 syllables). The scanner (no flag) ran Troes into one syllable and made tre-pi long-long and -ne long, a fit with 14."),
 760: (None, "Carrier line, checked by hand: sed fŭ-rŏr | ar-den | tem cae | dis-qu(e) in | sā-nă cŭ | pī-do (14 syllables), the scanner's own fit. Listed because it shares a unit with the half-line 761, which the scanner cannot fit, and a unit with an unresolved line receives no sc at all."),
 761: (['1e–git⏑', 'in⏑', '2ad–ver–3sos×'],
  "Half-line (hemistich), one of Virgil's unfinished lines: ē-gĭt ĭn | ad-ver | sōs, a dactyl, a spondee and one syllable (– ⏑ ⏑ | – – | ×), 6 syllables; ēgit has the long ē of the perfect, and its -it and in are short before vowels. The last syllable is marked × as the end of the line. There is no hexameter to fit; the scanner returns UNRESOLVED."),
 767: (['1Al–can–2drum–que', 'Ha⏑li⏑3um–que⏑', 'No⏑4e–mo⏑na⏑5que–', 'Pry⏑ta⏑6nim–que×'],
  "Noemona is four syllables, Nŏ-ē-mŏ-nă (Greek Νοήμονα, no diphthong), and the -que after Noemona is lengthened before Pr-, as Homer's τε before Πρύτανιν in the line Virgil copies (Iliad 5.678): Al-can | drum-qu(e) Hă-lĭ | um-quĕ Nŏ | ē-mŏ-nă | quē Prў-tă | nim-que (16 syllables). The scanner (no flag) read Noe- as a diphthong and lengthened the -que after Halium instead, a fit with 15."),
 772: (['1vas–ta–2to–rem', 'A⏑my⏑3cum–‖', 'quo–', '4non–', 'fe–5li–ci⏑or⏑', '6al–ter×'],
  "Wrong quantities with the right count (no flag). vāstātōrem has long -tā- and -tō- (vāstāre, -tor), and Ămўcum two short syllables (Greek Ἄμυκος; as nunc Amyci casum 1.221): vas-tā | tō-r(em) Ă-mў | cum quō | nōn fē | lī-cĭ-ŏr | al-ter (14 syllables), caesura after Amycum. The scanner made -ta-to- short-short and A-my- long-long."),
 779: (['1con–ve⏑ni⏑2unt–', 'Teu–3cri–‖', 'Mnes–4theus–', 'a–5cer–que⏑', 'Se⏑6res–tus×'],
  "Teucri has Greek eu as one long syllable (as Mnestheus in the same line): con-vĕ-nĭ | unt Teu | crī Mnes | theus ā | cer-quĕ Sĕ | res-tus (14 syllables), with the long ā of ācer. The scanner (COSTLY 1.5, not flagged) split Te-u into two short syllables, a fit with 15."),
 787: (['1et–', 'mag–ni', '2Ae–ne–3ae–‖', 'seg–4nes–', 'mi⏑se⏑5ret–que⏑', 'pu⏑6det–que×'],
  "Ae-nē-ae: three long syllables, magni elided into it (as 1.92): et mag | n(i) Ae-nē | ae seg | nēs mĭ-sĕ | ret-quĕ pŭ | det-que (14 syllables). The scanner (COSTLY 1.2, not flagged) split the initial diphthong and shortened -ne-, a fit with 15."),
 791: (['1a–cri⏑us⏑', '2hoc–', 'Teu–3cri–‖', 'cla–4mo–re', 'in–5cum–be⏑re⏑', '6mag–no×'],
  "Teucri has Greek eu as one long syllable (as 9.516): ā-crĭ-ŭs | hōc Teu | crī clā | mō-r(e) in | cum-bĕ-rĕ | mag-no (14 syllables). The scanner (no flag) split Te-u into two short syllables, a fit with 15."),
 805: (['1ni–', 'Tur–2nus–', 'ce–3dat–‖', 'Teu–4cro–rum–', '5moe–ni⏑bus⏑', '6al–tis×'],
  "Teucrorum has Greek eu as one long syllable: nī Tur | nus cē | dat Teu | crō-rum | moe-nĭ-bŭs | al-tis (13 syllables). The scanner (no flag) split Te-u into two short syllables, a fit with 14."),
 811: (None, "Flagged COSTLY 2.2; confirmed by hand, entered only to clear the flag: ic-tĭ-bŭs | in-gĕ-mĭ | nant has | tīs et | Trō-ĕs ĕt | ip-se (15 syllables). Troes is two syllables (Greek nominative plural, -ĕs short before et), as the scanner reads it; the scanner's parse is right."),
}
strip = lambda s: re.sub(r'[0-9–⏑×‖]', '', s)
out = dict(fx)
for n in sorted(NEW):
    sc, why = NEW[n]
    if sc is None: sc = own(n)
    k = f'9.{n}'; assert k not in fx, k
    assert [strip(x) for x in sc] == A.WORD_RE.findall(L[n]), (k, sc)
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
if '--write' in sys.argv:
    open(FP, 'w', encoding='utf8').write(json.dumps(out, ensure_ascii=False, indent=1) + '\n'); print('written')
