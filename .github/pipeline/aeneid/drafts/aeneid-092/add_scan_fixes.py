#!/usr/bin/env python3
"""Reviewer helper (aeneid-092): write hand scansions for XII.107-215 directly into scan-fixes.json (no other review is
running in parallel), appended in line order; keys are
f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them, and must not already be in scan-fixes.json.
A hand scansion is written compactly, one word per item, syllables split by '.', each followed by its quantity:
'-' long, 'u' short, 'e' elided (left unmarked). Foot numbers, the final x and the caesura (after word index CAES) are
put in by this script, which then checks each entry against the build's word-match rule and the validator's metre rule
and the syllable count stated in its why. Dry run unless --write."""
import os, sys, json, re
HERE = '/home/user/Lectorium/.github/pipeline/aeneid/drafts/aeneid-092'
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
fx = A.jload(os.path.join(A.HERE, 'scan-fixes.json'))
OUT = os.path.join(A.HERE, 'scan-fixes.json')
P = A.part('aeneid-092'); LL = A.lines_of(P)
L = {str(l.get('label', l['n'])): l['t'] for l in LL}
order = [str(l.get('label', l['n'])) for l in LL]
MK = {'-': '–', 'u': '⏑'}

def build(spec, caes):
    words = []
    for w in spec.split():
        syl, q = w.rsplit(':', 1); syl = syl.split('.'); assert len(syl) == len(q), w
        words.append(list(zip(syl, q)))
    counted = [(wi, si) for wi, w in enumerate(words) for si, (s, m) in enumerate(w) if m in '-u']
    marks = [words[wi][si][1] for wi, si in counted]
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
            if m == 'e': tok += s; continue
            ci = counted.index((wi, si))
            tok += digit.get(ci, '') + s + ('×' if ci == len(counted) - 1 else MK[m])
        if wi == caes: tok += '‖'
        out.append(tok)
    return out

NEW = {
 '108': ('Ae.ne.as:--- a.cu.it:uu- Mar.tem:-e et:- se:- sus.ci.tat:-uu i.ra:--', 1,
  "Aenēās has the initial diphthong Ae- as one long syllable and a long -nē-: Ae-nē | ās ă-cŭ | ĭt Mar | t(em) et sē | sus-cĭ-tăt | ī-rā (14 syllables), Martem elided into et, caesura after acuit. The scanner (cost 1.8, not flagged) split A-e and read A-e-ne as a dactyl."),
 '110': ('tum:- so.ci.os:uu- maes.ti.que:--u me.tum:u- so.la.tur:--u I.u.li:u--', 3,
  "Iūlī is three syllables, Ĭ-ū-lī, with a vowel I (as 1.556, 6.364), so -tur before it is short and the fifth foot a dactyl: tum sŏ-cĭ | ōs maes | tī-quĕ mĕ | tum sō | lā-tŭr Ĭ | ū-lī (15 syllables), caesura after metum. The scanner (COSTLY 2.0, flagged) read Iu- as one syllable with consonantal I and made a spondaic fifth foot."),
 '117': ('di.men.si:--- Ru.tu.li.que:uu-u vi.ri:u- Teu.cri.que:--u pa.ra.bant:u--', 2,
  "Teucrique has the Greek diphthong eu, one long syllable (as 11.842, 12.78): dī-men | sī Rŭ-tŭ | lī-quĕ vĭ | rī Teu | crī-quĕ pă | rā-bant (15 syllables), caesura after viri. The scanner (cost 0.0, not flagged) read Te-u-cri with two short syllables and counted 16."),
 '162': ('qua.dri.iu.go:-uu- ve.hi.tur:uu- cur.ru:-- cui:- tem.po.ra:-uu cir.cum:--', 1,
  "quadriiugo is quā-drĭ-jŭ-gō, four syllables, quadri- + iugum with the second i consonantal (as 10.571 quadriiugis), and cui one long syllable: quā-drĭ-jŭ | gō vĕ-hĭ | tur cur | rū cui | tem-pŏ-ră | cir-cum (15 syllables), caesura after vehitur. The scanner (cost 1.5, not flagged) ran quadri- together as one syllable and counted 14."),
 '166': ('hinc:- pa.ter:uu Ae.ne.as:--- Ro.ma.nae:--- stir.pis:-u o.ri.go:u--', 2,
  "Aenēās has the initial diphthong Ae- as one long syllable (as 1.378): hinc pă-tĕr | Ae-nē | ās Rō | mā-nae | stir-pĭs ŏ | rī-gō (14 syllables), caesura after Aeneas. The scanner (cost 1.2, not flagged) split A-e and read A-e-ne as a dactyl."),
 '175': ('Tum:- pi.us:uu Ae.ne.as:--- stric.to:-- sic:- en.se:-u pre.ca.tur:u--', 2,
  "Aenēās has the initial diphthong Ae- as one long syllable (as 1.378): Tum pĭ-ŭs | Ae-nē | ās stric | tō sīc | en-sĕ prĕ | cā-tur (14 syllables), caesura after Aeneas. The scanner (cost 1.5, not flagged) split A-e and read A-e-ne as a dactyl."),
 '178': ('et:- pa.ter:uu om.ni.po.tens:-uu- et:- tu:- Sa.tur.ni.a:--uu con.iunx:--', 2,
  "Same feet and quantities as the scanner's, different syllable division (as 2.519, 12.17): coniunx (con + iunx) has the i consonantal after the prefix, con | iunx, not co-niunx: et pă-tĕr | om-nĭ-pŏ | tens et | tū Sā | tur-nĭ-ă | con-iunx (15 syllables), caesura after omnipotens."),
 '185': ('ce.det:-u I.u.lus:u-u a.gris:u- nec:- post:- ar.ma:-e ul.la:-u re.bel.les:u--', 2,
  "Iūlus is three syllables, Ĭ-ū-lus, with a vowel I (as 1.267, 1.556 and 12.110), so the -det of cedet is short before it: cē-dĕt Ĭ | ū-lŭs ă | grīs nec | post ar | m(a) ul-lă rĕ | bel-lēs (15 syllables), arma elided into ulla, caesura after agris. The scanner (cost 0.0, not flagged) read Iu- as one syllable with consonantal I, lengthening -det by position, and counted 14."),
 '189': ('non:- e.go:uu nec:- Teu.cris:-- I.ta.los:uu- pa.re.re:--u iu.be.bo:u--', 3,
  "Teucris has the Greek diphthong eu, one long syllable (as 12.78): nōn ĕ-gŏ | nec Teu | crīs Ĭ-tă | lōs pā | rē-rĕ iŭ | bē-bō (15 syllables), caesura after Teucris. The scanner (cost 0.3, not flagged) read Te-u-cris with two short syllables and counted 16."),
 '195': ('Sic:- pri.or:uu Ae.ne.as:--- se.qui.tur:uu- sic:- dein.de:-u La.ti.nus:u--', 2,
  "Aenēās has the initial diphthong Ae- as one long syllable (as 1.378), and deinde is two syllables: Sīc prĭ-ŏr | Ae-nē | ās sĕ-quĭ | tur sīc | dein-dĕ Lă | tī-nus (15 syllables), caesura after Aeneas. The scanner (cost 1.2, not flagged) split A-e and read A-e-ne as a dactyl."),
 '197': ('Haec:- e.a.dem:uue Ae.ne.a:--- ter.ram:-- ma.re:uu si.de.ra:-uu iu.ro:--', 2,
  "Aenēā, the Greek vocative, is three long syllables with the initial diphthong one syllable, and eadem elides into it (as 8.496); măre has two short syllables: Haec ĕ-ă | d(em) Ae-nē | ā ter | ram mă-rĕ | sī-dĕ-ră | iū-rō (15 syllables), caesura after Aenea. The scanner (cost 0.6, not flagged) read Ae-ne-a as a dactyl with short -nē- and made mare long-long."),
 '208': ('cum:- se.mel:uu in:- sil.vis:-- i.mo:-- de:- stir.pe:-u re.ci.sum:u--', 3,
  "Confirmed by hand, entered as a carrier because the unit 208–211 gets no sc from the scanner (211 is UNRESOLVED): cum sĕ-mĕl | in sil | vīs ī | mō dē | stir-pĕ rĕ | cī-sum (14 syllables), caesura after silvis. The scanner's parse is right."),
 '209': ('ma.tre:-u ca.ret:u- po.su.it.que:uu-u co.mas:u- et:- brac.chi.a:-uu fer.ro:--', 3,
  "Confirmed by hand, entered as a carrier because the unit 208–211 gets no sc from the scanner (211 is UNRESOLVED): mā-trĕ că | ret pŏ-sŭ | it-quĕ cŏ | mās et | brac-chĭ-ă | fer-rō (16 syllables), caesura after comas. The scanner's parse is right."),
 '210': ('o.lim:-e ar.bos:-- nunc:- ar.ti.fi.cis:-uu- ma.nus:uu ae.re:-u de.co.ro:u--', 3,
  "Confirmed by hand, entered as a carrier because the unit 208–211 gets no sc from the scanner (211 is UNRESOLVED): ō-l(im) ar | bos nunc | ar-tĭ-fĭ | cis mă-nŭs | ae-rĕ dĕ | cō-rō (15 syllables), olim elided into arbos, caesura after artificis. The scanner's parse is right."),
 '211': ('in.clu.sit:--- pa.tri.bus.que:uu-u de.dit:u- gesture:e ges.ta.re:--u La.ti.nis:u--', 2,
  "Flagged UNRESOLVED. The print's 'gesture gestare' has an extra word, a misprint for 'gestare' (rule 5b: t as printed, the note says so); the line is scanned without it and 'gesture' is left unmarked like an elided word: in-clū | sit pă-trĭ | bus-quĕ dĕ | dit ges | tā-rĕ Lă | tī-nīs (15 syllables), caesura after dedit. With the extra word no hexameter fits."),
}
strip = lambda s: re.sub(r'[0-9–⏑×‖]', '', s)
out = {}
for n in [x for x in order if x in NEW]:
    spec, caes, why = NEW[n]
    sc = build(spec, caes)
    k = f"{P['book']}.{n}"; assert k not in fx, k
    assert [strip(x) for x in sc] == A.WORD_RE.findall(L[n]), (k, sc, A.WORD_RE.findall(L[n]))
    seg = ' '.join(sc); feet = re.findall(r'[1-6]', seg); syl = len(re.findall(r'[–⏑×]', seg))
    body = re.sub(r'[^0-9–⏑×]', '', seg); fp = re.findall(r'\d([–⏑×]+)', body)
    assert feet == list('123456') and 12 <= syl <= 17 and seg.count('×') == 1, (k, feet, syl)
    assert all(f in ('–⏑⏑', '––') for f in fp[:5]) and fp[5] in ('–×', '⏑×'), (k, fp)
    m = re.search(r'\((\d+) syllables', why); assert m and int(m.group(1)) == syl, (k, syl)
    own = SL.scan_line(L[n])[1]
    if why.startswith('Confirmed'): assert own == sc, (k, own, sc)
    else: assert own != sc, k
    out[k] = {'sc': sc, 'why': why}
    print(k, syl, ' '.join(sc))
assert len(out) == len(NEW)
if '--write' in sys.argv:
    for k in out: assert k not in fx, k
    fx.update(out)
    open(OUT, 'w', encoding='utf8').write(json.dumps(fx, ensure_ascii=False, indent=1) + '\n'); print('written', OUT, len(out), 'entries added')
