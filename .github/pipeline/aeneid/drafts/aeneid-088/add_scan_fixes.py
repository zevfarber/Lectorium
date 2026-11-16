#!/usr/bin/env python3
"""Reviewer helper (aeneid-088): write hand scansions for XI.648-724 to drafts/aeneid-088/scan-fixes-088.json (NOT to
scan-fixes.json, which another reviewer is editing; the orchestrator merges this file), in line order; keys are
f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them, and must not already be in scan-fixes.json.
A hand scansion is written compactly, one word per item, syllables split by '.', each followed by its quantity:
'-' long, 'u' short, 'e' elided (left unmarked). Foot numbers, the final x and the caesura (after word index CAES) are
put in by this script, which then checks each entry against the build's word-match rule and the validator's metre rule
and the syllable count stated in its why. Dry run unless --write."""
import os, sys, json, re
HERE = '/home/user/Lectorium/.github/pipeline/aeneid/drafts/aeneid-088'
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
fx = A.jload(os.path.join(A.HERE, 'scan-fixes.json'))
OUT = os.path.join(HERE, 'scan-fixes-088.json')
P = A.part('aeneid-088'); LL = A.lines_of(P)
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
 '657': ('I.ta.li.des:-uu- quas:- ip.sa:-u de.cus:u- si.bi:uu di.a:-u Ca.mil.la:u--', 3,
  "dīa is two syllables (dī-ă, from dīus), and decus is long by position before sibi: Ī-tă-lĭ | dēs quās | ip-să dĕ | cūs sĭ-bĭ | dī-ă Că | mil-la (16 syllables), caesura after decus. The scanner (cost 1.5, not flagged) ran dia into one syllable, counted 15 and made both syllables of sibi long to fit."),
 '659': ('qua.les:-- Thre.i.ci.ae:-uu- cum:- flu.mi.na:-uu Ther.mo.don.tis:----', 1,
  "Confirmed by hand, entered only to clear the COSTLY flag: Thrēĭcĭae is four syllables (Greek Θρηΐκιος; Greenough prints Threïcius at 6.645) and the Greek name Thermōdōn (ω) gives a spondaic fifth foot: quā-lēs | Thrē-ĭ-cĭ | ae cum | flū-mĭ-nă | Thēr-mō | dōn-tis (14 syllables), caesura after Threiciae. The scanner's parse was right; the cost is the spondaic fifth foot."),
 '662': ('Pen.the.si.le.a:-uu-u re.fert:u- mag.no.que:--e u.lu.lan.te:uu-u tu.mul.tu:u--', 1,
  "Penthĕsĭlēa is five syllables (Greek Πενθεσίλεια, -lē-ă, as Penthesilea furens at 1.491), and rĕfert has a short re-: Pen-thĕ-sĭ | lē-ă rĕ | fert mag | nōqu(e) ŭ-lŭ | lān-tĕ tŭ | mul-tu (16 syllables), magnoque elided into ululante, caesura after refert. The scanner (cost 1.5, not flagged) ran -lea into one syllable, counted 15 and lengthened re- to fit."),
 '665': ('de.i.cis:-uu Aut:- quot:u hu.mi:u- mo.ri.en.ti.a:uu-uu cor.po.ra:-uu fun.dis:--', 3,
  "dēĭcis is three syllables (dē-ĭ-cis: de + iacio, dē- long), and its -cĭs is short before the vowel of Aut; quŏt is short before humi (h makes no position): dē-ĭ-cĭs | aut quŏt hŭ | mī mŏ-rĭ | en-tĭ-ă | cor-pŏ-ră | fun-dis (17 syllables, five dactyls), caesura after humi. The scanner (cost 1.5, not flagged) read dei- as one syllable, counted 16 and made -cis long."),
 '678': ('ig.no.tis:--- et:u e.quo:u- ve.na.tor:--u I.a.py.ge:u-uu fer.tur:--', 2,
  "Ĭāpyx is a Greek name (Ἰᾶπυξ) with a vowel I, so Iapyge is four syllables, Ĭ-ā-pў-gĕ (as Iapyge at 8.710 and Iapyx at 12.391), and vēnātŏr keeps its short -or before it: ig-nō | tīs ĕt ĕ | quō vē | nā-tŏr Ĭ | ā-pў-gĕ | fer-tur (15 syllables), caesura after equo. The scanner (cost 0.0, not flagged) read Ia- as consonantal (Ja-), counted 14 and lengthened -tor."),
 '680': ('pug.na.to.ri:---e o.pe.rit:uu- ca.put:uu in.gens:-- o.ris:-u hi.a.tus:u--', 1,
  "Wrong quantities with the right count (cost 0.0, not flagged): pugnātōri has -nā- and -tō- long (-ātor, -ātōris), and ŏpĕrit has its first two syllables short: pug-nā | tōr(i) ŏ-pĕ | rīt că-pŭt | in-gens | ō-rĭs hĭ | ā-tus (15 syllables), pugnatori elided into operit, caesura after operit. The scanner made -na- and -to- short and o-pe- long."),
 '685': ('tra.i.cit:-uu et:- su.per:uu haec:- i.ni.mi.co:uu-- pec.to.re:-uu fa.tur:--', 3,
  "trāĭcit is three syllables (trā-ĭ-cit, trans + iacio, as deicis at 11.665), and its -cĭt is short before et: trā-ĭ-cĭt | ēt sŭ-pĕr | haec ĭ-nĭ | mī-cō | pec-tŏ-rĕ | fā-tur (16 syllables), caesura after haec. The scanner (cost 1.8, not flagged) read trai- as one syllable, counted 15 and lengthened -cit."),
 '691': ('cor.po.ra:-uu sed:- Bu.ten:-- a.ver.sum:--- cus.pi.de:-uu fi.xit:--', 2,
  "Wrong quantities with the right count (cost 0.0, not flagged): corpŏră has its last two syllables short (the open -a before sed), Būtēn has the long Greek -ēn (η) and āversum a long ā- (from ab): cor-pŏ-ră | sēd Bū | tēn ā | ver-sum | cus-pĭ-dĕ | fī-xit (14 syllables), caesura after Buten. The scanner made -po- and -ra long and -ten short."),
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
    open(OUT, 'w', encoding='utf8').write(json.dumps(out, ensure_ascii=False, indent=1) + '\n'); print('written', OUT)
