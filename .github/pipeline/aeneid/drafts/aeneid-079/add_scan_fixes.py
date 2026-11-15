#!/usr/bin/env python3
"""Reviewer helper (aeneid-079): append hand scansions for X.606-688 to scan-fixes.json, in line order after
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
P = A.part('aeneid-079'); LL = A.lines_of(P)
L = {str(l.get('label', l['n'])): l['t'] for l in LL}
order = [str(l.get('label', l['n'])) for l in LL]
own = lambda n: SL.scan_line(L[n])[1]
AE = "Ae- is one long syllable (diphthong), and -nē- is long"
NEW = {
 '617': (['1Nunc–', 'pe⏑re⏑2at–', 'Teu–3cris–que⏑', 'pi⏑4o–‖', 'det–', '5san–gui⏑ne⏑', '6poe–nas×'],
  "Teucris has Greek eu as one long syllable (as 10.44): Nunc pĕ-rĕ | at Teu | crīs-quĕ pĭ | ō det | san-guĭ-nĕ | poe-nas (15 syllables), pereat's -at long by position before T-. The scanner (cost 0.0, not flagged) split eu into Te-u and made at Te-u a dactyl."),
 '623': (['1o–ra–2tur–', 'iu⏑ve⏑3ni–‖', 'me–que', '4hoc–', 'i⏑ta⏑', '5po–ne⏑re⏑', '6sen–tis×'],
  "Wrong quantities with the right count (cost 0.0, not flagged). me is long (mē), its -que elides before hoc, hoc is long, and ita is two shorts: ō-rā | tur iŭ-vĕ | nī mē | (que) hōc ĭ-tă | pō-nĕ-rĕ | sen-tis (15 syllables). The scanner made me and hoc short and both syllables of ita long."),
 '628': (['1Et–', 'Iu–no', '2ad–la⏑cri⏑3mans–‖', 'Quid–', '4si–', 'quae–', '5vo–ce⏑', 'gra⏑6va–ris×'],
  "Wrong quantities with the right count (cost 0.0, not flagged). Iuno has a long Iū-, and adlacrimans is ad-lă-crĭ-māns, ad- long by position before l, lacrimo short-short: Et Iū | n(o) ad-lă-crĭ | māns Quid | sī quae | vō-cĕ gră | vā-ris (14 syllables), Iuno elided before adlacrimans. The scanner made Iu- short, ad- short and -dla-cri- long."),
 '637': (['1in–', 'fa⏑ci⏑em', '2Ae–ne–3ae–‖', 'vi–4su–', 'mi–5ra–bi⏑le⏑', '6mons–trum×'],
  "Aenēae: " + AE + ", and faciem elides into it: in fă-cĭ | (em) Ae-nē | ae vī | sū mī | rā-bĭ-lĕ | mons-trum (14 syllables), caesura after Aeneae. The scanner (COSTLY 1.2, not flagged) split the initial Ae into A-e and made a dactyl of it."),
 '647': (['1Tum–', 've–ro', '2Ae–ne–3an–‖', 'a–4ver–sum', 'ut–', '5ce–de⏑re⏑', '6Tur–nus×'],
  "Aenēān (Greek accusative): " + AE + ", -ān long (as 10.81), and vero elides into it: Tum vē | (ro) Ae-nē | ān ā | vers(um) ut | cē-dĕ-rĕ | Tur-nus (13 syllables), the first four feet spondees. The scanner (COSTLY 1.5, not flagged) split the initial Ae."),
 '649': (['1Quo–', 'fu⏑gis⏑', '2Ae–ne–3a–‖', 'Tha⏑la⏑4mos–', 'ne–', '5de–se⏑re⏑', '6pac–tos×'],
  "Aenēā (Greek vocative of Aeneas, long final ā): Ae- is one long syllable and -nē- is long, and thalamos is short-short-long (θάλαμος): Quō fŭ-gĭs | Ae-nē | ā Thă-lă | mōs nē | dē-sĕ-rĕ | pac-tos (15 syllables), caesura after Aenea. The scanner (cost 0.6, not flagged) kept Ae whole but made -ne-a two shorts and tha-la two longs."),
 '653': (['1For–te⏑', 'ra⏑2tis–', 'cel–3si–‖', 'con–4iunc–ta⏑', 'cre⏑5pi–di⏑ne⏑', '6sa–xi×'],
  "coniuncta (con + iuncta): the i is consonantal, so con | iunc | ta, three syllables, con long by position (as coniunx at 1.343, 2.597): For-tĕ ră | tis cel | sī con | iunc-tă crĕ | pī-dĭ-nĕ | sa-xi (15 syllables), caesura after celsi. The scanner (cost 0.0, not flagged) read co-ni-unc-ta with a vowel i, a fit with 16."),
 '656': (['1Huc–', 'se–2se–', 'tre⏑pi⏑da', '3Ae–ne–4ae–‖', 'fu⏑gi⏑5en–tis⏑', 'i⏑6ma–go×'],
  "Aenēae: " + AE + ", and trepida elides into it; sese is long-long: Hūc sē | sē trĕ-pĭ | (da) Ae-nē | ae fŭ-gĭ | en-tĭs ĭ | mā-go (15 syllables), caesura after Aeneae. The scanner (COSTLY 1.2, not flagged) split the initial Ae and made sese two shorts."),
 '661': (['1Il–lum', 'au–tem', '2Ae–ne–3as–‖', 'ab–4sen–tem', 'in–', '5prae–li⏑a⏑', '6pos–cit×'],
  "Aenēās: " + AE + ", and -ās long, with autem elided into it: Il-l(um) au | t(em) Ae-nē | ās ab | sen-t(em) in | prae-lĭ-ă | pos-cit (13 syllables). The words follow the print's praelia (a misprint for proelia, corrected in the reading text; the scansion is the same). The scanner (COSTLY 1.2, not flagged) split the initial Ae."),
 '684': (['1cur–va⏑', 'pe⏑2tat–', 'Teu–3crum–que', 'i⏑te⏑4rum–‖', 'se–', '5red–dat⏑', 'in⏑', '6ar–ma×'],
  "Teucrum has Greek eu as one long syllable, and its -que elides before iterum: cur-vă pĕ | tat Teu | crum(que) ĭ-tĕ | rum sē | red-dăt ĭn | ar-ma (15 syllables). The scanner (cost 0.6, not flagged) split eu into Te-u and made tat Te-u a dactyl."),
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
