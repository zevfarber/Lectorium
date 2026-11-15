#!/usr/bin/env python3
"""Reviewer helper (aeneid-081): append hand scansions for X.791-908 to scan-fixes.json, in line order after the last
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
P = A.part('aeneid-081'); LL = A.lines_of(P)
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
 '798': ('Ae.ne.ae:--- su.bi.it:uu- mu.cro.nem:--e ip.sum.que:--u mo.ran.do:u--', 1,
  "Aenēae: " + AE + ", and it does not elide before subiit: Ae-nē | ae sŭ-bĭ | īt mū | crō-n(em) ip | sum-quĕ mŏ | ran-do (14 syllables), the -it of subiit long by position before m-. " + AESC.format(c='1.2')),
 '802': ('mis.si.li.bus:-uu- Fu.rit:uu Ae.ne.as:--- tec.tus.que:--u te.net:u- se:-', 2,
  "Aenēās: " + AE + ", -ās long: mis-sĭ-lĭ | būs fŭ-rĭt | Ae-nē | ās tec | tus-quĕ tĕ | net sē (15 syllables), ending on the monosyllable se. " + AESC.format(c='1.2')),
 '809': ('Ae.ne.as:--- nu.bem:-- bel.li:-- dum:- de.to.net:-uu om.nis:--', 1,
  "Aenēās: " + AE + ", -ās long: Ae-nē | ās nū | bem bel | lī dum | dē-tŏ-nĕt | om-nis (13 syllables). " + AESC.format(c='1.2')),
 '816': ('per:- me.di.um:uue Ae.ne.as:--- iu.ve.nem:uu- to.tum.que:--u re.con.dit:u--', 2,
  "Aenēās: " + AE + ", -ās long, and medium elides into it: per mĕ-dĭ | (um) Ae-nē | ās iŭ-vĕ | nem tō | tum-quĕ rĕ | con-dit (15 syllables), iuvenem with consonantal i. " + AESC.format(c='1.2')),
 '826': ('quid:- pi.us:uu Ae.ne.as:--- tan.ta:-- da.bit:uu in.do.le:-uu dig.num:--', 2,
  "Aenēās: " + AE + ", -ās long; tantā is ablative with indole: quid pĭ-ŭs | Ae-nē | ās tan | tā dă-bĭt | in-dŏ-lĕ | dig-num (15 syllables). " + AESC.format(c='1.2')),
 '830': ('Ae.ne.ae:--- mag.ni:-- dex.tra:-- ca.dis:uu In.cre.pat:-uu ul.tro:--', 1,
  "Aenēae: " + AE + ": Ae-nē | ae mag | nī dex | trā că-dĭs | in-crĕ-păt | ul-tro (14 syllables), dextrā ablative; the stray closing mark of the print (rule 5b) does not affect the words. " + AESC.format(c='1.2')),
 '863': ('et:- ca.put:uu Ae.ne.ae:--- re.fe.res:uu- Lau.si.que:--u do.lo.rum:u--', 2,
  "Aenēae: " + AE + ": et că-pŭt | Ae-nē | ae rĕ-fĕ | rēs Lau | sī-quĕ dŏ | lō-rum (15 syllables). " + AESC.format(c='1.2')),
 '873': ('At.que:-e hic:- Ae.ne.an:--- mag.na:-- ter:- vo.ce:-u vo.ca.vit:u--', 2,
  "Aenēān (Greek accusative): " + AE + ", -ān long: At-qu(e) hīc | Ae-nē | ān mag | nā tēr | vō-cĕ vŏ | cā-vit (13 syllables). The scanner (cost 1.5, not flagged) split the initial Ae into A-e."),
 '874': ('Ae.ne.as:--- ag.no.vit:--u e.nim:u- lae.tus.que:--u pre.ca.tur:u--', 2,
  "Aenēās: " + AE + ", -ās long: Ae-nē | ās ag | nō-vĭt ĕ | nim lae | tus-quĕ prĕ | cā-tur (14 syllables), with the caesura after enim. " + AESC.format(c='1.2')),
 '875': (None, None, "Carrier line, checked by hand: Sīc pă-tĕr | il-lĕ dĕ | um fă-cĭ | at sīc | al-tŭs Ă | pol-lo (16 syllables), deum two syllables. The scanner's fit is correct; the entry is needed only because this line shares a unit with the half-line 10.876, which the scanner cannot fit, and a unit with an unresolved line receives no sc at all."),
 '876': ('in.ci.pi.as:-uu- con.fer.re:--u ma.num:u-', None,
  "Half-line (hemistich), one of Virgil's unfinished lines, as 10.490, 10.580 and 10.728: in-cĭ-pĭ | ās con | fer-rĕ mă | num, three feet and one syllable (– ⏑ ⏑ | – – | – ⏑ ⏑ | ×), the last syllable marked × as the end of the line (9 syllables). There is no hexameter to fit; the scanner returns UNRESOLVED. 875, in the same unit, is entered as a carrier."),
 '891': ('bel.la.to.ris:---u e.qui:u- ca.va:uu tem.po.ra:-uu co.ni.cit:-uu has.tam:--', 1,
  "Wrong quantities with the right count (cost 0.0, not flagged): bellātōris has -lā- and -tō- long and -ris short, and equī a short e: bel-lā | tō-rĭs ĕ | quī că-vă | tem-pŏ-ră | cōn-ĭ-cĭt | has-tam (16 syllables), conicit with the first syllable long (con- + iacio). The scanner made -lā- and -tō- short and -ris and e- long."),
 '895': ('Cla.mo.re:--e in.cen.dunt:--- cae.lum:-- Tro.es.que:--u La.ti.ni.que:u--h', 1,
  "Hypermetric line (as 10.781, 4.558, 5.753, 6.602, 8.228): the last -que of Latinique elides into Advolat, the first word of 896, so the line has fourteen syllables and thirteen count: Clā-mō | r(e) in-cen | dunt cae | lum Trō | ēs-quĕ Lă | tī-nī(que). Troes is two syllables, Trō-ĕs, its -es long by position before -que. The final -que is not counted and is left unmarked, the end mark × on ni. The scanner (cost 0.6, not flagged) made Troes one syllable and Latī- short."),
 '896': ('Ad.vo.lat:-uu Ae.ne.as:--- va.gi.na.que:---e e.ri.pit:-uu en.sem:--', 1,
  "Aenēās: " + AE + ", -ās long: Ad-vŏ-lăt | Ae-nē | ās vā | gī-nā | (que) ē-rĭ-pĭt | en-sem (14 syllables), vāgīnā ablative, its -que elided into eripit; Advolat also takes in the elided -que of Latinique (895, hypermetric). " + AESC.format(c='1.2')),
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
