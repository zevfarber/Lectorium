#!/usr/bin/env python3
"""Reviewer helper (aeneid-091): write hand scansions for XII.1-106 directly into scan-fixes.json (no other review is
running in parallel), appended in line order; keys are
f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them, and must not already be in scan-fixes.json.
A hand scansion is written compactly, one word per item, syllables split by '.', each followed by its quantity:
'-' long, 'u' short, 'e' elided (left unmarked). Foot numbers, the final x and the caesura (after word index CAES) are
put in by this script, which then checks each entry against the build's word-match rule and the validator's metre rule
and the syllable count stated in its why. Dry run unless --write."""
import os, sys, json, re
HERE = '/home/user/Lectorium/.github/pipeline/aeneid/drafts/aeneid-091'
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
fx = A.jload(os.path.join(A.HERE, 'scan-fixes.json'))
OUT = os.path.join(A.HERE, 'scan-fixes.json')
P = A.part('aeneid-091'); LL = A.lines_of(P)
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
 '17': ('aut:- ha.be.at:uu- vic.tos:-- ce.dat:-- La.vi.ni.a:--uu con.iunx:--', 2,
  "Same feet and quantities as the scanner's, different syllable division (as 2.519, 2.673): coniunx (con + iunx) has the i consonantal after the prefix, con | iunx, not co-niunx: aut hă-bĕ | at vic | tōs cē | dat Lā | vī-nĭ-ă | con-iunx (14 syllables), caesura after victos."),
 '26': ('sub.la.tis:--- a.pe.ri.re:uu-u do.lis:u- si.mul:uu hoc:- a.ni.mo:uue hau.ri:--', 2,
  "sublātis has a long a (sublatus) and its -tis is the long ablative plural; aperire is ă-pĕ-rī-re: sub-lā | tī-să-pĕ | rī-rĕ-dŏ | lī-sĭ-mŭl | hōc ă-nĭ | m(o) hau-rī (16 syllables), caesura after dolis. The scanner (cost 0.3, not flagged) made la- and -tis short and a-pe- long, a valid-looking line with wrong quantities."),
 '28': ('fas:- e.rat:uu id.que:-e om.nes:-- di.vi.que:--e ho.mi.nes.que:uu-u ca.ne.bant:u--', 3,
  "dīvīque has both its first syllables long and hŏmĭnesque its first two short: fās ĕ-răt | id-qu(e) om | nēs dī | vī-qu(e) hŏ-mĭ | nēs-quĕ că | nē-bant (15 syllables), caesura after omnes. The scanner (cost 0.0, not flagged) made di-vi short and ho-mi long."),
 '31': ('pro.mis.sam:--e e.ri.pu.i:-uu- ge.ne.ro:uu- ar.ma:-e im.pi.a:-uu sump.si:--', 1,
  "Hiatus: genero, arma does not elide (the long dative -ō stands before the pause), while promissam and arma elide as usual; gĕnĕrō has its first two syllables short: prō-mis | s(am) ē-rĭ-pŭ | ī gĕ-nĕ | rō ar | m(a) im-pĭ-ă | sump-sī (15 syllables), caesura after eripui. The scanner (cost 0.0, not flagged) elided genero and had to make ge-ne long."),
 '48': ('Quam:- pro:- me:- cu.ram:-- ge.ris:uu hanc:- pre.cor:uu op.ti.me:-uu pro:- me:-', 3,
  "prō and mē are long, gĕrĭs short (h makes no position before hanc): Quam prō | mē cū | ram gĕ-rĭs | hanc prĕ-cŏr | op-tĭ-mĕ | prō mē (15 syllables), caesura after curam. The scanner (cost 0.6, not flagged) made the first pro me short and ge-ris long."),
 '54': ('At:- re.gi.na:--u no.va:u- pug.nae:-- con.ter.ri.ta:--uu sor.te:--', 2,
  "rēgīna has long rē- and -gī- and a short nominative -a, and nŏvā (ablative with sorte) a short no- (as 1.522): At rē | gī-nă nŏ | vā pug | nae con | ter-rĭ-tă | sor-te (14 syllables), caesura after nova. The scanner (cost 0.0, not flagged) made re-gi short and -na, no- long."),
 '58': ('tu:- re.qui.es:uu- mi.se.rae:uu- de.cus:uu im.pe.ri.um.que:-uu-u La.ti.ni:u--', 2,
  "requiēs is three syllables, rĕ-quĭ-ēs (as requiem 4.433): tū rĕ-quĭ | ēs mĭ-sĕ | rae dĕ-cŭs | im-pĕ-rĭ | um-quĕ Lă | tī-nī (17 syllables, five dactyls), caesura after miserae. The scanner (cost 0.0, not flagged) ran requ-ies together as two syllables with a long first and counted 16."),
 '63': ('lu.mi.na:-uu nec:- ge.ne.rum:uue Ae.ne.an:--- cap.ti.va:--u vi.de.bo:u--', 3,
  "Aenēān, the Greek accusative, is three long syllables with the initial diphthong one syllable, and generum elides into it (as 11.910): lū-mĭ-nă | nec gĕ-nĕ | r(um) Ae-nē | ān cap | tī-vă vĭ | dē-bō (15 syllables), caesura after Aenean. The scanner (cost 1.2, not flagged) split A-e and shortened -ne-."),
 '65': ('fla.gran.tis:--- per.fu.sa:--u ge.nas:u- quoi:- plu.ri.mus:-uu ig.nem:--', 2,
  "quoi (= cui) is one long syllable, as cui everywhere in Virgil (as 7.692, 10.530): flā-gran | tīs per | fū-să gĕ | nās quoi | plū-rĭ-mŭs | ig-nem (14 syllables), caesura after genas. The scanner (cost 0.8, not flagged) read quo-i as two short syllables, a dactyl in the fourth foot."),
 '66': ('sub.ie.cit:--- ru.bor:uu et:- ca.le.fac.ta:uu-u per:u o.ra:-u cu.cur.rit:u--', 2,
  "subiēcit (sub + iacio) has the i consonantal after the prefix, sub | iē | cit, sub- long by position and -iē- long: sub-iē | cit rŭ-bŏr | et că-lĕ | fac-tă pĕr | ō-ră cŭ | cur-rit (16 syllables), caesura after et. The scanner (cost 0.0, not flagged) read su-bi-e-cit, four syllables, with a short -e-, and counted 17."),
 '72': ('Ne:- quae.so:-- ne:- me:- la.cri.mis:uu- ne.ve:-e o.mi.ne:-uu tan.to:--', 4,
  "Both nē and mē are long, lăcrĭmis has two short syllables, and ōmine a long o: Nē quae | sō nē | mē lă-crĭ | mīs nē | v(e) ō-mĭ-nĕ | tan-tō (14 syllables), caesura after lacrimis. The scanner (cost 0.6, not flagged) made ne me short and -cri- long."),
 '78': ('non:- Teu.cros:-- a.gat:uu in:- Ru.tu.los:uu- Teu.crum:-e ar.ma:-u qui.es.cant:u--', 4,
  "Teucros and Teucrum have the Greek diphthong eu, one long syllable (as 11.842, 11.872): nōn Teu | crōs ă-găt | in Rŭ-tŭ | lōs Teu | cr(um) ar-mă quĭ | ēs-cant (15 syllables), caesura after Rutulos. The scanner (cost 1.0, not flagged) read Te-u-cros and Te-u-crum, three syllables each."),
 '80': ('il.lo:-- quae.ra.tur:--- con.iunx:-- La.vi.ni.a:--uu cam.po:--', 1,
  "coniunx (con + iunx) has the i consonantal, two syllables, con long by position (as 2.597, 2.738): il-lō | quae-rā | tur con | iunx Lā | vī-nĭ-ă | cam-pō (13 syllables), caesura after quaeratur. The scanner (cost 0.0, not flagged) read co-ni-unx, three syllables with short co- and ni-, and counted 14."),
 '83': ('Pi.lum.no:--- quos:- ip.sa:-u de.cus:u- de.dit:uu O.ri.thyi.a:---u', 3,
  "Ōrīthyia (Greek Ōreithyia) is four syllables, Ō-rī-thyi-a, with long Ō and -rī-, so the fifth foot is a spondee (a spondaic close with a Greek name); dĕdit is short-short: Pī-lum | nō quōs | ip-să dĕ | cus dĕ-dĭt | Ō-rī | thyi-a (14 syllables), caesura after decus. The scanner (cost 0.3, not flagged) made dedit long-long and O-ri short."),
 '88': ('cir.cum.dat:--- lo.ri.cam:--e u.me.ris:uu- si.mul:uu ap.tat:-u ha.ben.do:u--', 2,
  "lōrīcam has both its first syllables long and ŭmĕrīs its first two short: cir-cum | dat lō | rī-c(am) ŭ-mĕ | rīs sĭ-mŭl | ap-tăt hă | ben-dō (15 syllables), caesura after umeris. The scanner (cost 0.0, not flagged) made lo-ri short and u-me long."),
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
