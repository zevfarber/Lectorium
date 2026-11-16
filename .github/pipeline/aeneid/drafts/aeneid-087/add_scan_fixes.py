#!/usr/bin/env python3
"""Reviewer helper (aeneid-087): append hand scansions for XI.532-647 to scan-fixes.json, in line order after the last
existing key; keys are f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them.
A hand scansion is written compactly, one word per item, syllables split by '.', each followed by its quantity:
'-' long, 'u' short, 'e' elided (left unmarked), 'h' a hypermetric syllable elided into the next line (unmarked, after ×).
Foot numbers, the final × and the caesura (after word index CAES) are put in by this script, which then checks each entry
against the build's word-match rule and the validator's metre rule (half-line rule when the why starts 'Half-line') and the
syllable count stated in the why. sc None = the scanner's own fit (carrier lines). Dry run unless --write."""
import os, sys, json, re
HERE = '/home/user/Lectorium/.github/pipeline/aeneid/drafts/aeneid-087'
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
FP = os.path.join(A.HERE, 'scan-fixes.json')
raw = open(FP, encoding='utf8').read(); fx = json.loads(raw)
assert json.dumps(fx, ensure_ascii=False, indent=1) + '\n' == raw
P = A.part('aeneid-087'); LL = A.lines_of(P)
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

NEW = {
 '540': ('Pri.ver.no:--e an.ti.qua:--- Me.ta.bus:uu- cum:e ex.ce.de.ret:--uu ur.be:--', 1,
  "Wrong quantities with the right count (cost 0.0, not flagged): antīquā has long ī and the long ablative ā, and Mĕtăbus two short syllables (as 564, which the scanner gets right): Prī-ver | n(o) an-tī | quā Mĕ-tă | bus c(um) ex | cē-dĕ-rĕt | ur-be (14 syllables), Priverno elided into antiqua and cum into excederet, caesura after antiqua. The scanner made an-tĭ-quă a dactyl and Mē-tā long."),
 '550': ('tar.da.tur:--- ca.ro.que:--e o.ne.ri:uu- ti.met:uu Om.ni.a:-uu se.cum:--', 2,
  "Wrong quantities with the right count (cost 0.0, not flagged): cārō has both syllables long (cārus, dative -ō) and ŏnĕrī two shorts before the long dative -ī: tar-dā | tur cā | rō-qu(e) ŏ-nĕ | rī tĭ-mĕt | Om-nĭ-ă | sē-cum (15 syllables), caroque elided into oneri, caesura after oneri. The scanner made cā-rō short-short and ŏ-nĕ long-long."),
 '583': ('ae.ter.num:--- te.lo.rum:--e et:- vir.gi.ni.ta.tis:-uu-u a.mo.rem:u--', 1,
  "Wrong quantities with the right count (cost 0.0, not flagged): aeternum is not elided (telorum begins with a consonant), tēlōrum has both first syllables long and virgĭnĭtātis short -gi-ni-: ae-ter | num tē | lō-r(um) et | vir-gĭ-nĭ | tā-tĭs ă | mō-rem (14 syllables), telorum elided into et, caesura after telorum. The scanner made tē-lō short and -gĭ-nĭ- long."),
 '585': ('mi.li.ti.a:-uu- ta.li:-- co.na.ta:--u la.ces.se.re:u-uu Teu.cros:--', 1,
  "Teu- is the Greek diphthong eu, one long syllable (as 11.116, 11.164, 11.449): mī-lĭ-tĭ | ā tā | lī cō | nā-tă lă | ces-sĕ-rĕ | Teu-cros (15 syllables), militiā ablative with long ā, tālī and cōnāta long, caesura after tali. The scanner (cost 0.8, not flagged) split Teu- into Te-u, counted 16 syllables and made tā-lī short-short and lă- long to fit."),
 '608': (None, None,
  "The scanner's fit is correct (checked by hand: Iam-qu(e) in | trā iac | tum tē | lī prō | gres-sŭs ŭ | ter-que (13 syllables)); the entry is needed only because this line shares a unit with 609 (substiterat:), a hypermetric line the scanner cannot fit, and a unit with an unresolved line receives no sc at all."),
 '609': ('sub.sti.te.rat:-uu- su.bi.to:uue e.rum.punt:--- cla.mo.re:--u fu.ren.tis.que:u--h', 2,
  "Hypermetric line (as 4.558, 8.228, 9.650, 10.895): the last -que of furentisque elides into exhortantur, the first word of 610, so the line has sixteen syllables and fifteen count (15 syllables counted): sub-stĭ-tĕ | rat sŭ-bĭ | t(o) ē-rum | punt clā | mō-rĕ fŭ | ren-tīs(que), subito elided into erumpunt, caesura after erumpunt. The final -que is not counted and is left unmarked, the end mark × on -tis. The scanner cannot elide across a line end and returned UNRESOLVED."),
 '610': (None, None,
  "The -que of furentisque (609) elides into ex-: ex-hor | tan-tŭr ĕ | quōs fun | dunt sĭ-mŭl | un-dĭ-quĕ | tē-la (15 syllables). The scanner's fit is correct; the entry is needed because this line shares a unit with 609, a hypermetric line the scanner cannot fit, and a unit with an unresolved line receives no sc at all."),
 '619': (None, None,
  "Flagged COSTLY 2.0; confirmed by hand, entered only to clear the flag: rē-ĭ-cĭ | unt par | mās ĕt ĕ | quōs ad | moe-nĭ-ă | ver-tunt (15 syllables). reiciunt is four syllables with a long first syllable (written for reiiciunt, the consonantal i after the prefix lengthening re-), as reice at Eclogue 3.96 and proicis at 11.361. The scanner's parse is right."),
 '620': ('Tro.es:-u a.gunt:u- prin.ceps:-- tur.mas:-- in.du.cit:--u A.si.las:u--', 2,
  "Wrong count (cost 0.0, not flagged): Trōĕs is two syllables (Greek nominative plural, as 1.232, 9.689, 10.895), its -ĕs short before agunt, and ăgunt has a short a: Trō-ĕs ă | gunt prin | ceps tur | mās in | dū-cĭt Ă | sī-las (14 syllables), caesura after princeps; Ăsīlas as 10.175. The scanner ran Troes into one syllable and lengthened a-, a fit with 13."),
 '640': ('vol.vi.tur:-uu il.le:-e ex.cus.sus:--u hu.mi:u- Ca.til.lus:--u I.ol.lan:u--', 3,
  "Flagged COSTLY 2.0, and wrong: Iollan is three syllables, Ĭ-ol-lan, with a vowel I (as Iollas in Eclogues 2.57 and 3.76), and Cātillus has a long first syllable (it opens 7.672, Catillusque acerque Coras): vol-vĭ-tŭr | il-l(e) ex | cus-sŭs hŭ | mī Cā | tĭl-lŭs Ĭ | ol-lan (15 syllables), ille elided into excussus, caesura after humi, -lus short before the vowel. The scanner read Iol- as one syllable, a fit with 14."),
 '642': ('de.i.cit:-uu Her.mi.ni.um:-uu- nu.do:-- cui:- ver.ti.ce:-uu ful.va:--', 1,
  "deicit is three syllables, dē-ĭ-cit (dē + iacio, as 8.428 and 10.753), and its -cit is short before the vowel of Herminium: dē-ĭ-cĭt | Her-mĭ-nĭ | um nū | dō cui | ver-tĭ-cĕ | ful-va (15 syllables), cui one syllable, caesura after Herminium. The scanner (cost 1.8, not flagged) read dei- as one syllable and made -cit long, a fit with 14."),
 '643': ('cae.sa.ri.es:-uu- nu.di.que:--e u.me.ri:uu- nec:- vul.ne.ra:-uu ter.rent:--', 2,
  "Wrong quantities with the right count (cost 0.0, not flagged): nūdī has both syllables long (nūdus, nominative plural -ī) and ŭmĕrī two shorts before the long -ī, as umero at 575: cae-să-rĭ | ēs nū | dī-qu(e) ŭ-mĕ | rī nec | vul-nĕ-ră | ter-rent (15 syllables), nudique elided into umeri, caesura after umeri. The scanner made nū-dī short-short and ŭ-mĕ long-long."),
 '644': ('tan.tus:-u in:u ar.ma:-u pa.tet:u- La.tos:-- huic:- has.ta:-u per:u ar.mos:--', 3,
  "huic is one long syllable, as always in Virgil (as 5.849, 8.631, and 554 here): tan-tŭs ĭn | ar-mă pă | tēt Lā | tōs huic | has-tă pĕr | ar-mos (15 syllables), caesura after patet. The scanner (cost 0.0, not flagged) split huic into hŭ-ĭc and read the fourth foot tōs hŭ-ĭc as a dactyl, a fit with 16."),
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
