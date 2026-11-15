#!/usr/bin/env python3
"""Reviewer helper (aeneid-082): append hand scansions for XI.1-99 to scan-fixes.json, in line order after the last
existing key; keys are f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them.
A hand scansion is written compactly, one word per item, syllables split by '.', each followed by its quantity:
'-' long, 'u' short, 'e' elided (left unmarked), 'h' a hypermetric syllable elided into the next line (unmarked, after ×).
Foot numbers, the final × and the caesura (after word index CAES) are put in by this script, which then checks each entry
against the build's word-match rule and the validator's metre rule (half-line rule when the why starts 'Half-line') and the
syllable count stated in the why. sc None = the scanner's own fit (carrier lines). Dry run unless --write."""
import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
FP = os.path.join(A.HERE, 'scan-fixes.json')
raw = open(FP, encoding='utf8').read(); fx = json.loads(raw)
assert json.dumps(fx, ensure_ascii=False, indent=1) + '\n' == raw
P = A.part('aeneid-082'); LL = A.lines_of(P)
L = {str(l.get('label', l['n'])): l['t'] for l in LL}
order = [str(l.get('label', l['n'])) for l in LL]
own = lambda n: SL.scan_line(L[n])[1]
MK = {'-': '–', 'u': '⏑'}

def build(spec, caes, half=False):
    """spec: 'Ae.ne.ae:--- su.bi.it:uu-' ... -> sc tokens"""
    words = []
    for w in spec.split():
        syl, q = w.rsplit(':', 1); syl = syl.split('.'); assert len(syl) == len(q), w
        words.append(list(zip(syl, q)))
    counted = [(wi, si) for wi, w in enumerate(words) for si, (s, m) in enumerate(w) if m in '-u']
    marks = [words[wi][si][1] for wi, si in counted]
    # parse feet
    starts, i = [], 0
    while i < len(marks):
        starts.append(i)
        assert marks[i] == '-' or (i == len(marks) - 1), ('foot must start long', spec, i)
        if i == len(marks) - 1: i += 1; break
        if marks[i + 1] == 'u' and i + 2 < len(marks) and marks[i + 2] == 'u' and i + 2 != len(marks) - 1: i += 3
        elif i + 2 == len(marks) - 1 and marks[i + 1] == 'u' and marks[i + 2] == 'u': i += 3
        else: i += 2
    digit = {s: str(k + 1) for k, s in enumerate(starts)}
    out = []
    for wi, w in enumerate(words):
        tok = ''
        for si, (s, m) in enumerate(w):
            if m in 'eh': tok += s; continue
            ci = counted.index((wi, si))
            tok += digit.get(ci, '') + s + ('×' if ci == len(counted) - 1 else MK[m])
        if wi == caes: tok += '‖'
        out.append(tok)
    return out

AE = "Ae- is one long syllable (diphthong), and -nē- is long"
AESC = "The scanner (cost {c}, not flagged) split the initial Ae into A-e."
NEW = {
 '2': ('Ae.ne.as:--- quam.quam:-e et:- so.ci.is:uu- da.re:uu tem.pus:-u hu.man.dis:u--', 3,
  "Aenēās: " + AE + ", -ās long: Ae-nē | ās quam | qu(am) et sŏ-cĭ | īs dă-rĕ | tem-pŭs hŭ | man-dis (15 syllables), quamquam elided into et and the caesura after sociis. " + AESC.format(c='1.2')),
 '4': (None, None, "Flagged COSTLY 2.0; confirmed by hand, entered only to clear the flag: vō-tă dĕ | um prī | mō vic | tor sōl | vē-băt Ĕ | ō-o (14 syllables). deum is two syllables (dĕ-um, the old genitive plural), and Eōō has a short E- here, as in the same line-end at 3.588 (primo surgebat Eoo) and at 6.831; it is long at 1.489. The scanner's parse is right."),
 '31': ('ser.va.bat:--- se.ni.or:uu- qui:- Par.rha.si.o:-uu- E.van.dro:---', 1,
  "Hiatus and a spondaic fifth foot: Parrhasiō keeps its long -ō unelided before Ēvandrō, in the Greek manner of the two Greek names: ser-vā | bat sĕ-nĭ | ōr quī | Par-rhă-sĭ | ō Ē | van-dro (14 syllables). senior has short se- and -ni-, its -or long by position before qui. The scanner (COSTLY 2.0) made se- and -ni- long and ran -o E- together as one short syllable."),
 '36': ('Ut:- ve.ro:-e Ae.ne.as:--- fo.ri.bus:uu- se.se:-e in.tu.lit:-uu al.tis:--', 2,
  "Aenēās: " + AE + ", -ās long, and vero elides into it: Ut vē | r(o) Ae-nē | ās fŏ-rĭ | bus sē | s(e) in-tŭ-lĭt | al-tis (14 syllables). " + AESC.format(c='1.2')),
 '55': ('Haec:- me.a:uu mag.na:-u fi.des:u- At:- non:- E.van.dre:--u pu.den.dis:u--', 3,
  "Wrong quantities with the right count (cost 0.0, not flagged): magnă (nominative with fides) has a short final a, fĭdēs a short fi- and long -ēs, and nōn is long: Haec mĕ-ă | mag-nă fĭ | dēs At | nōn Ē | van-drĕ pŭ | den-dis (15 syllables), Evandre with long E- (Greek eu) and the caesura after fides. The scanner made -na and fi- long and non and E- short."),
 '58': ('prae.si.di.um:-uue Au.so.ni.a:-uue et:- quan.tum:-- tu:- per.dis:-u I.u.le:u--', 3,
  "Iule is Ĭ-ū-le, three syllables, with a vowel I (house practice, as 5.546, 5.569), so the fifth foot is a dactyl and perdis has a short -dis before the vowel: prae-sĭ-dĭ | (um) Au-sŏ-nĭ | (a) et quan | tum tū | per-dĭs Ĭ | ū-le (15 syllables), praesidium elided into Ausonia and Ausonia into et. The scanner (COSTLY 2.0) took Iu- as consonantal, made -dis long and the fifth foot a spondee."),
 '73': ('ex.tu.lit:-uu Ae.ne.as:--- quas:- il.li:-- lae.ta:-u la.bo.rum:u--', 1,
  "Aenēās: " + AE + ", -ās long: ex-tŭ-lĭt | Ae-nē | ās quās | il-lī | lae-tă lă | bō-rum (14 syllables). " + AESC.format(c='1.2')),
 '92': ('vic.tor:-u ha.bet:u- Tum:- maes.ta:-u pha.lanx:u- Teu.cri.que:--u se.quun.tur:u--', 4,
  "Teucrī: eu is the Greek diphthong, one long syllable (as Teucri at 3.601 and 4.397): vic-tŏr hă | bet tum | maes-tă phă | lanx Teu | crī-quĕ sĕ | quun-tur (15 syllables), caesura after phalanx. The scanner (cost 0.0, not flagged) split Teu- into Te-u and counted 16 syllables."),
 '95': ('sub.sti.tit:-uu Ae.ne.as:--- ge.mi.tu.que:uu-e haec:- ad.di.dit:-uu al.to:--', 1,
  "Aenēās: " + AE + ", -ās long: sub-stĭ-tĭt | Ae-nē | ās gĕ-mĭ | tū-qu(e) haec | ad-dĭ-dĭt | al-to (15 syllables), gemitū ablative, its -que elided before haec. " + AESC.format(c='1.2')),
}
strip = lambda s: re.sub(r'[0-9–⏑×‖]', '', s)
out = dict(fx)
for n in [x for x in order if x in NEW]:
    spec, caes, why = NEW[n]
    sc = own(n) if spec is None else build(spec, caes)
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
    else: assert 'thirteen count' in why and syl == 13, (k, syl)
    out[k] = {'sc': sc, 'why': why}
    print(k, syl, ' '.join(sc))
assert len(out) == len(fx) + len(NEW)
assert list(out)[:len(fx)] == list(fx)
if '--write' in sys.argv:
    open(FP, 'w', encoding='utf8').write(json.dumps(out, ensure_ascii=False, indent=1) + '\n'); print('written')
