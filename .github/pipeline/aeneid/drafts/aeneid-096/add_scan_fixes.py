#!/usr/bin/env python3
"""Reviewer helper (aeneid-096): write hand scansions for XII.554-649 directly into scan-fixes.json (no other review is
running in parallel), appended in line order; keys are
f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them, and must not already be in scan-fixes.json.
A hand scansion is written compactly, one word per item, syllables split by '.', each followed by its quantity:
'-' long, 'u' short, 'e' elided (left unmarked). Foot numbers, the final x and the caesura (after word index CAES) are
put in by this script, which then checks each entry against the build's word-match rule and the validator's metre rule
and the syllable count stated in its why. Dry run unless --write."""
import os, sys, json, re
HERE = '/home/user/Lectorium/.github/pipeline/aeneid/drafts/aeneid-096'
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
fx = A.jload(os.path.join(A.HERE, 'scan-fixes.json'))
OUT = os.path.join(A.HERE, 'scan-fixes.json')
P = A.part('aeneid-096'); LL = A.lines_of(P)
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
 '554': ('Hic:- men.tem:-e Ae.ne.ae:--- ge.ne.trix:uu- pul.cher.ri.ma:--uu mi.sit:--', 2,
  "Aeneae (dative) is Ae-nē-ae, three syllables (initial diphthong one syllable, ē long), as Aeneas at 12.311, and mentem elides into it: Hīc mēn | t(em) Ae-nē | ae gĕ-nĕ | trīx pūl | chēr-rĭ-mă | mī-sit (14 syllables), caesura after Aeneae. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 15."),
 '562': ('duc.to.res:--- tu.mu.lum.que:uu-u ca.pit:u- quo:- ce.te.ra:-uu Teu.crum:--', 2,
  "Teucrum is two syllables, Teu-crum, the Greek diphthong eu (as Teucros at 12.506), and quō (adverb, 'whither') is long: dūc-tō | rēs tŭ-mŭ | lūm-quĕ că | pīt quō | cē-tĕ-ră | Teu-crum (15 syllables), caesura after capit. The scanner (cost 0.6, not flagged) split Te-u into two syllables and shortened quo, a fit with 16."),
 '580': ('Ae.ne.as:--- mag.na.que:--e in.cu.sat:--- vo.ce:-u La.ti.num:u--', 1,
  "Aeneas is Ae-nē-ās, three syllables (initial diphthong one syllable, ē long), as at 12.311; magnā (ablative with voce) and incūsat are long, so the first four feet are spondees: Ae-nē | ās māg | nāqu(e) īn | cū-sāt | vō-cĕ Lă | tī-num (13 syllables), magnaque elided, caesura after magnaque. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 14."),
 '613': ('Dar.da.ni.um:-uue Ae.ne.an:--- ge.ne.rum.que:uu-e ad.sci.ve.rit:--uu ul.tro:--', 1,
  "One of the two lines Greenough brackets as spurious, scanned as it stands. Aenean (Greek accusative, -ān) is Ae-nē-ān, three syllables (initial diphthong one syllable, ē long), and Dardanium elides into it; adsciverit is ad-scī-vĕ-rĭt (ad + scisco): Dār-dă-nĭ | (um) Ae-nē | ān gĕ-nĕ | rūm-qu(e) ād | scī-vĕ-rĭt | ūl-tro (15 syllables), caesura after Aenean. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 16."),
 '618': ('com.mix.tum:--- cla.mo.rem:--e ad.rec.tas.que:---e im.pu.lit:-uu au.res:--', -1,
  "Same feet and quantities as the scanner's, different syllable division (as adlapsa at 12.319 and abrupto at 12.451): adrectas is ad + rectas, ad-rēc-tās with ad long by position, not an open long a- (a-drec), which the audio would read as a long vowel: cōm-mīx | tūm clā | mō-r(em) ād | rēc-tās | qu(e) īm-pŭ-lĭt | aū-res (13 syllables), clamorem and adrectasque elided; no caesura is marked, as in the scanner's parse."),
 '623': ('At.que:-e huic:- in:- fa.ci.em:uu- so.ror:uu ut:- con.ver.sa:--u Me.tis.ci:u--', 3,
  "huic is one syllable, the diphthong ui, long (as Huic at 12.488): Ātqu(e) huīc | īn fă-cĭ | ēm sŏ-rŏr | ūt cōn | vēr-să Mĕ | tīs-ci (15 syllables), atque elided, caesura after faciem. The scanner (cost 0.0, not flagged) read hu-ic as two short syllables, a fit with 16."),
 '628': ('In.gru.it:-uu Ae.ne.as:--- I.ta.lis:uu- et:- proe.li.a:-uu mis.cet:--', 1,
  "Aeneas is Ae-nē-ās, three syllables (initial diphthong one syllable, ē long), as at 12.311, and Italis has a short I (Ĭtalus, as Itali at 1.109 and Italos at 12.582; the long vowel belongs to Ītalia): Īn-grŭ-ĭt | Ae-nē | ās Ĭ-tă | līs ēt | proē-lĭ-ă | mīs-cet (15 syllables), caesura after Aeneas. The scanner (cost 1.0, not flagged) split Ae- in two and made Ī-tā- long, a false fit with the same count."),
 '642': ('ad.spi.ce.ret:-uu- Teu.cri:-- po.ti.un.tur:uu-- cor.po.re:-ue et:u ar.mis:--', 1,
  "Teucri is two syllables, Teu-crī, the Greek diphthong eu (as Teucros at 12.506): ād-spĭ-cĕ | rēt Teu | crī pŏ-tĭ | ūn-tūr | cōr-pŏ-r(e) ĕt | ār-mis (15 syllables), corpore elided, caesura after Teucri. The scanner (cost 0.0, not flagged) split Te-u into two short syllables, a fit with 16."),
 '648': ('Sanc.ta:-e ad:- vos:- a.ni.ma:uue at.que:-e is.ti.us:--- nes.ci.a:-uu cul.pae:--', 4,
  "istius is ĭs-tī-ŭs, three syllables with the long ī of the genitive (not run together by synizesis), and anima is ă-nĭ-mă: Sānct(a) ād | vōs ănĭ | m(a) ātqu(e) īs | tī-ūs | nēs-cĭ-ă | cūl-pae (14 syllables), Sancta, anima and atque elided, caesura after atque. The scanner (cost 1.5, not flagged) made a-ni- long and ran is-tius into two syllables, a fit with 13."),
}
# 631 is a half-line: written directly, checked by the validator's half-line rule
HALF = {'631': (['1Tur–nus⏑', 'ad⏑', '2haec×'],
  "Half-line (hemistich), one of Virgil's unfinished lines: Tūr-nŭs ăd | haec, a dactyl and one syllable (– ⏑ ⏑ | –), the last syllable marked × as the end of the line. There is no hexameter to fit; the scanner returns UNRESOLVED.")}
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
