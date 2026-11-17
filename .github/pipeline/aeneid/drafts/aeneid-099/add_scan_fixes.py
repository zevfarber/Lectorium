#!/usr/bin/env python3
"""Reviewer helper (aeneid-099): write hand scansions for XII.843-952 directly into scan-fixes.json (no other review is
running in parallel), appended in line order; keys are
f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them, and must not already be in scan-fixes.json.
A hand scansion is written compactly, one word per item, syllables split by '.', each followed by its quantity:
'-' long, 'u' short, 'e' elided (left unmarked). Foot numbers, the final x and the caesura (after word index CAES) are
put in by this script, which then checks each entry against the build's word-match rule and the validator's metre rule
and the syllable count stated in its why. Dry run unless --write."""
import os, sys, json, re
HERE = '/home/user/Lectorium/.github/pipeline/aeneid/drafts/aeneid-099'
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
fx = A.jload(os.path.join(A.HERE, 'scan-fixes.json'))
OUT = os.path.join(A.HERE, 'scan-fixes.json')
P = A.part('aeneid-099'); LL = A.lines_of(P)
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
 '847': ('u.no:-e eo.dem.que:--u tu.lit:u- par.tu:-- pa.ri.bus.que:uu-u re.vin.xit:u--', 2,
  "eodem has a long o (eōdem, ablative of idem), so it cannot stand as two shorts; its eo is one long syllable by synizesis, with uno elided into it: ū-n(o) eō | dēm-quĕ tŭ | līt pār | tū pă-rĭ | būs-quĕ rĕ | vīn-xit (15 syllables), caesura after tulit. The scanner (cost 0.0, not flagged) read e-o-dem as three syllables with a short o, a fit with 16."),
 '863': ('quae:- quon.dam:-e in:- bus.tis:-- aut:- cul.mi.ni.bus:-uu- de.ser.tis:---', 3,
  "Confirmed by hand, entered only to clear the COSTLY flag (as 12.704, 12.812): quae quōn | d(am) īn būs | tīs aūt | cūl-mĭ-nĭ | būs dē | sēr-tis (13 syllables), quondam elided, caesura after bustis. The line is spondaic in the fifth foot (culminibus desertis, dēsertis from dēsero), which is what the scanner's cost of 2.0 reflects; its parse is right."),
 '868': ('ad.rec.tae.que:---e hor.ro.re:--u co.mae:ue et:- vox:- fau.ci.bus:-uu hae.sit:--', 1,
  "Same feet and quantities as the scanner's, different syllable division (as adrectas at 12.618 and Adrexere at 12.251): adrectaeque is ad + rectae, ad-rēc-tae-que with ad long by position, not an open long a- (a-drec), which the audio would read as a long vowel: ād-rēc | taequ(e) hōr | rō-rĕ cŏ | m(ae) ēt vōx | faū-cĭ-bŭs | hae-sit (14 syllables), adrectaeque and comae elided, caesura after horrore (third-foot trochaic, as the scanner has it)."),
 '881': ('nunc:- cer.te:-e et:- mi.se.ro:uu- fra.tri:-- co.mes:uu i.re:-u per:u um.bras:--', 3,
  "frātrī has a long a by nature (frāter) and a long dative -ī, and cŏmĕs two short syllables: nūnc cēr | t(e) ēt mĭ-sĕ | rō frā | trī cŏ-mĕs | ī-rĕ pĕr | ūm-bras (15 syllables), certe elided, caesura after misero. The scanner (cost 0.8, not flagged) made fra-tri short-short and co-mes long, a false fit with the same count."),
 '887': ('Ae.ne.as:--- ins.tat:-- con.tra:-- te.lum.que:--u co.rus.cat:u--', 1,
  "Aeneas is Ae-nē-ās, three syllables (initial diphthong one syllable, ē long), as at 12.311 and 12.760: Ae-nē | ās īns | tāt cōn | trā tē | lūm-quĕ cŏ | rūs-cat (13 syllables), caesura after instat. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 14."),
 '903': ('Sed:- ne.que:uu cur.ren.tem:--- se:- nec:- cog.nos.cit:--u e.un.tem:u--', 2,
  "Confirmed by hand; the scanner's fit is taken as is. Entered only because this line shares a unit with 12.905, which the scanner cannot fit, and a unit with an unresolved line receives no sc at all (as 5.431 beside 5.432): Sēd nĕ-quĕ | cūr-rēn | tēm sē | nēc cōg | nōs-cĭt ĕ | ūn-tem (14 syllables), caesura after currentem; euntem is e-un-tem, not the diphthong eu."),
 '904': ('tol.len.tem.ve:---u ma.nus:u- sa.xum.ve:--e im.ma.ne:--u mo.ven.tem:u--', 1,
  "Confirmed by hand; the scanner's fit is taken as is. Entered only because this line shares a unit with 12.905, which the scanner cannot fit, and a unit with an unresolved line receives no sc at all (as 5.431 beside 5.432): tōl-lēn | tēm-vĕ mă | nūs sā | xūmv(e) īm | mā-nĕ mŏ | vēn-tem (14 syllables), saxumve elided, caesura after manus."),
 '905': ('gen.ua:-u la.bant:u- ge.li.dus:uu- con.cre.vit:--- fri.go.re:-uu san.guis:--', 2,
  "genua has a consonantal u (gen-wa), two syllables, the first long by position, as at 5.432 (the same half-line): gēn-wă lă | bānt gĕ-lĭ | dūs cōn | crē-vīt | frī-gŏ-rĕ | sān-guis (15 syllables), caesura after gelidus. The scanner returns UNRESOLVED because it reads ge-nu-a with a short first syllable."),
 '909': ('noc.te:-u qui.es:u- ne.qui.quam:--e a.vi.dos:uu- ex.ten.de.re:--uu cur.sus:--', 3,
  "quies is two syllables, quĭ-ēs (as 12.309 and 10.745), nocte has its short ablative -ĕ, and nēquīquam two long syllables before the elision, with ăvĭdōs short-short-long: nōc-tĕ quĭ | ēs nē | quīqu(am) ă-vĭ | dōs ēx | tēn-dĕ-rĕ | cūr-sus (15 syllables), caesura after avidos (with the trithemimeral after quies). The scanner (cost 0.0, not flagged) ran quies into one syllable and made -te, a- and -vi- long and ne-qui short, a fit with 14."),
 '919': ('Cunc.tan.ti:--- te.lum:-e Ae.ne.as:--- fa.ta.le:--u co.rus.cat:u--', 2,
  "Aeneas is Ae-nē-ās, three syllables (initial diphthong one syllable, ē long), with telum elided into it, as at 12.794: Cūnc-tān | tī tē | l(um) Ae-nē | ās fā | tā-lĕ cŏ | rūs-cat (13 syllables), caesura after Aeneas (with the trithemimeral after Cunctanti). The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 14."),
 '929': ('mons:- cir.cum:-e et:- vo.cem:-- la.te:-- ne.mo.ra:uue al.ta:-u re.mit.tunt:u--', 3,
  "lātē (adverb of lātus) has both syllables long, and nĕmŏră is short-short, its -a elided into alta: mōns cīr | c(um) ēt vō | cēm lā | tē nĕ-mŏ | r(a) āl-tă rĕ | mīt-tunt (14 syllables), circum and nemora elided, caesura after vocem. The scanner (cost 0.0, not flagged) made la-te short-short and ne-mo long, a false fit with the same count."),
 '935': ('et:- me:- seu:- cor.pus:-- spo.li.a.tum:uu-- lu.mi.ne:-uu ma.vis:--', 3,
  "seu is one syllable, the diphthong eu (as 6.880 and 9.680), and mē is long: ēt mē | seū cōr | pūs spŏ-lĭ | ā-tūm | lū-mĭ-nĕ | mā-vis (14 syllables), caesura after corpus. The scanner (cost 0.0, not flagged) split se-u into two short syllables and made me short, a fit with 15."),
 '937': ('Au.so.ni.i:-uu- vi.de.re:--u tu.a:ue est:- La.vi.ni.a:--uu con.iunx:--', 1,
  "Same feet and quantities as the scanner's, different syllable division (as 12.17 and 12.80): coniunx (con + iunx) has the i consonantal after the prefix, con | iunx, not an open long co- (co-niunx), which the audio would read as a long vowel: Aū-sŏ-nĭ | ī vī | dē-rĕ tŭ | (a) ēst Lā | vī-nĭ-ă | cōn-iunx (15 syllables), tua elided, caesura after videre (third-foot trochaic, as the scanner has it)."),
 '939': ('Ae.ne.as:--- vol.vens:-- o.cu.los:uu- dex.tram.que:--u re.pres.sit:u--', 1,
  "Aeneas is Ae-nē-ās, three syllables (initial diphthong one syllable, ē long), as at 12.311 and 12.783: Ae-nē | ās vōl | vēns ŏ-cŭ | lōs dēx | trām-quĕ rĕ | prēs-sit (14 syllables), caesura after volvens. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 15."),
}
HALF = {}
strip = lambda s: re.sub(r'[0-9–⏑×‖]', '', s)
out = {}
for n in [x for x in order if x in NEW or x in HALF]:
    if n in HALF:
        sc, why = HALF[n]; k = f"{P['book']}.{n}"; assert k not in fx, k
        assert [strip(x) for x in sc] == A.WORD_RE.findall(L[n]), (k, sc)
        seg = ' '.join(sc); assert re.findall(r'[1-6]', seg) == ['1', '2'] and seg.count('×') == 1
        assert SL.scan_line(L[n])[1] is None, k
        out[k] = {'sc': sc, 'why': why}; print(k, 'half-line', seg); continue
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
assert len(out) == len(NEW) + len(HALF)
if '--write' in sys.argv:
    for k in out: assert k not in fx, k
    fx.update(out)
    open(OUT, 'w', encoding='utf8').write(json.dumps(fx, ensure_ascii=False, indent=1) + '\n'); print('written', OUT, len(out), 'entries added')
