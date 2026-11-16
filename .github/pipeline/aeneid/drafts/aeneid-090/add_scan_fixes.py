#!/usr/bin/env python3
"""Reviewer helper (aeneid-090): write hand scansions for XI.836-915 directly into scan-fixes.json (no other review is
running in parallel), appended in line order; keys are
f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them, and must not already be in scan-fixes.json.
A hand scansion is written compactly, one word per item, syllables split by '.', each followed by its quantity:
'-' long, 'u' short, 'e' elided (left unmarked). Foot numbers, the final x and the caesura (after word index CAES) are
put in by this script, which then checks each entry against the build's word-match rule and the validator's metre rule
and the syllable count stated in its why. Dry run unless --write."""
import os, sys, json, re
HERE = '/home/user/Lectorium/.github/pipeline/aeneid/drafts/aeneid-090'
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
fx = A.jload(os.path.join(A.HERE, 'scan-fixes.json'))
OUT = os.path.join(A.HERE, 'scan-fixes.json')
P = A.part('aeneid-090'); LL = A.lines_of(P)
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
 '842': ('sup.pli.ci.um:-uu- Teu.cros:-- co.na.ta:--u la.ces.se.re:u-uu bel.lo:--', 1,
  "Teucros has the Greek diphthong eu, one long syllable (as Teucros at 7.547, 10.22, 11.116), and cōnāta has both its first syllables long (cōnor): sup-plĭ-cĭ | um Teu | crōs cō | nā-tă lă | ces-sĕ-rĕ | bel-lo (15 syllables), caesura after Teucros. The scanner (cost 0.0, not flagged) read Te-u-cros as three syllables and made co-na- short, counting 16."),
 '858': ('di.xit:-u et:u au.ra.ta:--- vo.lu.crem:uu- Thre.is.sa:--u sa.git.tam:u--', 2,
  "Threïssa is three syllables, Thrē-is-sa, as at 1.316; vŏlucrem has a short first syllable, and -lu- stays short before cr: dī-xĭt ĕt | au-rā | tā vŏ-lŭ | crem Thrē | is-să să | git-tam (15 syllables), caesura after aurata. The scanner (cost 1.5, not flagged) took Threissa as two syllables and had to lengthen vo- and -lu-, counting 14."),
 '870': ('dis.iec.ti.que:---u du.ces:u- de.so.la.ti.que:----u ma.ni.pli:u--', 1,
  "Same quantities as the scanner's, different syllable division (as 2.608, 1.128): disiecti (dis + iacio) has the i consonantal after the prefix, dis | iec | ti, not di-siec-ti: dis-iec | tī-quĕ dŭ | cēs dē | sō-lā | tī-quĕ mă | nī-plī (14 syllables), caesura after duces; -ni- of manipli long by position before pl."),
 '872': ('Nec:- quis.quam:-e ins.tan.tis:--- Teu.cros:-- le.tum.que:--u fe.ren.tis:u--', 2,
  "Teucros has the Greek diphthong eu, one long syllable (as 842): Nec quis | qu(am) ins-tan | tīs Teu | crōs lē | tum-quĕ fĕ | ren-tis (13 syllables), quisquam elided into instantis, caesura after instantis. The scanner (cost 0.0, not flagged) read Te-u-cros as three syllables, made the third foot a dactyl tis-Te-u and counted 14."),
 '890': ('ar.ie.tat:-uu in:- por.tas:-- et:- du.ros:-- ob.i.ce:-uu pos.tis:--', 2,
  "arietat is three syllables with consonantal i, ar-yĕ-tat (as ariete at 7.175), ar- long by position; dūros has a long u; obice (ob + iacio) has the i consonantal after the prefix, so ob- is long by position (as 2.444, 4.549): ar-yĕ-tăt | in por | tās et | dū-rōs | ob-ĭ-cĕ | pos-tis (14 syllables), caesura after portas. The scanner (cost 1.3, not flagged) read a-ri-e-tat as four syllables with a long a- and made du- short."),
 '904': ('cum:- pa.ter:uu Ae.ne.as:--- sal.tus:-- in.gres.sus:--u a.per.tos:u--', 2,
  "Flagged COSTLY 2.0, and wrong: Ae-nē-ās is three long syllables, the initial diphthong one syllable (as 1.170, 1.180): cum pă-tĕr | Ae-nē | ās sal | tūs in | gres-sŭs ă | per-tos (14 syllables), caesura after Aeneas. The scanner split A-e and shortened -ne-, counting 15."),
 '908': ('ac:- si.mul:uu Ae.ne.as:--- fu.man.tis:--- pul.ve.re:-uu cam.pos:--', 2,
  "Ae-nē-ās is three long syllables, the initial diphthong one syllable (as 904): ac sĭ-mŭl | Ae-nē | ās fū | man-tīs | pul-vĕ-rĕ | cam-pos (14 syllables), caesura after Aeneas. The scanner (cost 1.2, not flagged) split A-e and shortened -ne-, counting 15."),
 '910': ('et:- sae.vum:-e Ae.ne.an:--- ad.gno.vit:--- Tur.nus:-u in:u ar.mis:--', 2,
  "Aenēān, the Greek accusative, is three long syllables with the initial diphthong one syllable, and saevum elides into it: et sae | v(um) Ae-nē | ān ad | gnō-vit | Tur-nŭs ĭn | ar-mis (13 syllables), caesura after Aenean. The scanner (cost 1.5, not flagged) split A-e and shortened -ne-, counting 14."),
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
