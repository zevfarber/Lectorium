#!/usr/bin/env python3
"""Reviewer helper (aeneid-089): write hand scansions for XI.725-835 directly into scan-fixes.json (no other review is
running in parallel), appended in line order; keys are
f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them, and must not already be in scan-fixes.json.
A hand scansion is written compactly, one word per item, syllables split by '.', each followed by its quantity:
'-' long, 'u' short, 'e' elided (left unmarked). Foot numbers, the final x and the caesura (after word index CAES) are
put in by this script, which then checks each entry against the build's word-match rule and the validator's metre rule
and the syllable count stated in its why. Dry run unless --write."""
import os, sys, json, re
HERE = '/home/user/Lectorium/.github/pipeline/aeneid/drafts/aeneid-089'
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
fx = A.jload(os.path.join(A.HERE, 'scan-fixes.json'))
OUT = os.path.join(A.HERE, 'scan-fixes.json')
P = A.part('aeneid-089'); LL = A.lines_of(P)
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
 '747': ('ar.ma:-u vi.rum.que:u-u fe.rens:u- tum:- sum.ma:-e ip.si.us:--u ab:u has.ta:--', 2,
  "Confirmed by hand, entered only to clear the COSTLY flag: ipsīus has its middle i long (the usual quantity of the pronoun genitive), summa is elided into it, and ab is short before hasta (h makes no position): ar-mă vĭ | rum-quĕ fĕ | rēns tūm | summ(a) ip | sī-ŭs ăb | has-ta (15 syllables), caesura after ferens. The scanner's parse is right; the cost is the elision and the long -ī-."),
 '768': ('For.te:-u sa.cer:u- Cy.be.lo:uu- Chlo.reus:-- o.lim.que:--u sa.cer.dos:u--', 2,
  "Chlōreus is a Greek name (Χλωρεύς) of two long syllables, Chlō-reus, with eu one diphthong (as Teucri, Eurus); Cybelō is the dative with long -ō: For-tĕ să | cēr Cy̆-bĕ | lō Chlō | reūs ō | līm-quĕ să | cēr-dōs (15 syllables), caesura after Cybelo. The scanner (cost 0.8, not flagged) read Chlo-re-us as three syllables with a short Chlo-, counted 16 and put a dactyl in the third foot."),
 '800': ('con.ver.te.re:---e a.ni.mos:uu- a.cris:-- o.cu.los.que:uu-u tu.le.re:u-u', 1,
  "Wrong quantities with the right count (cost 0.0, not flagged): ācrīs (accusative plural of ācer) has both syllables long, and ŏcŭlōs its first two short: con-ver | tē-r(e) ă-nĭ | mōs ā | crīs ŏ-cŭ | lōs-quĕ tŭ | lē-re (15 syllables), convertere elided into animos, caesura after animos. The scanner made a-cris short and o-cu long."),
 '813': ('sub.ie.cit:--- pa.vi.tan.tem:uu-e u.te.ro:uu- sil.vas.que:--u pe.ti.vit:u--', 2,
  "subiēcit (sub + iacio): the i after the prefix is consonantal, sub | iē | cit, so sub is long by position, iē has its long perfect vowel and -cit is long by position before pavitantem (cf. 2.37 subiectis, 2.721 subiecta): sub-iē | cit pă-vĭ | tant(em) ŭ-tĕ | rō sil | vās-quĕ pĕ | tī-vit (15 syllables), pavitantem elided into utero, caesura after utero. The scanner (cost 0.0, not flagged) read su-bi-e-cit with a vowel i and a short e, counting 16."),
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
