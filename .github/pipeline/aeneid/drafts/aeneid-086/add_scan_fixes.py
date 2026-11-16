#!/usr/bin/env python3
"""Reviewer helper (aeneid-086): append hand scansions for XI.445-531 to scan-fixes.json, in line order after the last
existing key; keys are f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them.
A hand scansion is written compactly, one word per item, syllables split by '.', each followed by its quantity:
'-' long, 'u' short, 'e' elided (left unmarked), 'h' a hypermetric syllable elided into the next line (unmarked, after ×).
Foot numbers, the final × and the caesura (after word index CAES) are put in by this script, which then checks each entry
against the build's word-match rule and the validator's metre rule (half-line rule when the why starts 'Half-line') and the
syllable count stated in the why. sc None = the scanner's own fit (carrier lines). Dry run unless --write."""
import os, sys, json, re
HERE = '/home/user/Lectorium/.github/pipeline/aeneid/drafts/aeneid-086'
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
FP = os.path.join(A.HERE, 'scan-fixes.json')
raw = open(FP, encoding='utf8').read(); fx = json.loads(raw)
assert json.dumps(fx, ensure_ascii=False, indent=1) + '\n' == raw
P = A.part('aeneid-086'); LL = A.lines_of(P)
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
AESC = "The scanner (cost {c}, not flagged) split the initial Ae into A-e and counted {k} syllables."
TEU = "Teu- is the Greek diphthong eu, one long syllable (as 11.116, 11.164)"
TEUSC = "The scanner (cost {c}, not flagged) split Teu- into Te-u and counted {k} syllables."
NEW = {
 '446': ('cer.tan.tes:--- cas.tra:-e Ae.ne.as:--- a.ci.em.que:uu-u mo.ve.bat:u--', 2,
  "Aenēās: " + AE + ", and the nominative -ās long: cer-tan | tēs cas | tr(a) Ae-nē | ās ă-cĭ | em-quĕ mŏ | vē-bat (14 syllables), castra elided into Aeneas, caesura after Aeneas. " + AESC.format(c='1.2', k=15)),
 '449': ('in.struc.tos:--- a.ci.e:uu- Ti.be.ri.no:uu-e a:- flu.mi.ne:-uu Teu.cros:--', 1,
  TEU + ": in-struc | tōs ă-cĭ | ē Tĭ-bĕ | rīn(o) ā | flū-mĭ-nĕ | Teu-cros (15 syllables), Tiberino elided into the preposition ā, caesura after acie. The scanner (cost 0.6, not flagged) split Teu- into Te-u and counted 16 syllables, making flū- short and -mi- long to fit."),
 '472': ('Dar.da.ni.um:-uue Ae.ne.an:--- ge.ne.rum.que:uu-e ad.sci.ve.rit:--uu ur.bi:--', 1,
  "Aenēān: " + AE + ", and the Greek accusative -ān long: Dar-dă-nĭ | (um) Ae-nē | ān gĕ-nĕ | rum-qu(e) ad | scī-vĕ-rĭt | ur-bi (15 syllables), Dardanium elided into Aenean and generumque into adsciverit, caesura after Aenean. " + AESC.format(c='1.2', k=16)),
 '480': ('cau.sa:-u ma.li:u- tan.ti:-- o.cu.los:uu- de.iec.ta:--u de.co.ros:u--', 2,
  "Hiatus after tanti at the sense pause and the main caesura (no elision before oculos; with it there is no fit with natural quantities), as Samo hic at 1.16: cau-să mă | lī tan | tī ŏ-cŭ | lōs dē | iec-tă dĕ | cō-ros (15 syllables), tantī keeping its long ī in the third arsis; dēiecta has consonantal i (dē-iec-ta). The scanner (cost 0.0, not flagged) elided tanti and made the o- and -cu- of ŏcŭlos long."),
 '487': ('Iam.que:-e a.de.o:uu- ru.ti.lum:uu- tho.ra.ca:--e in.du.tus:--u a.e.nis:u--', 2,
  "aenis is three syllables, ă-ē-nis (as 1.295, 1.449 and 8.22): Iam-qu(e) ă-dĕ | ō rŭ-tĭ | lum thō | rā-c(a) in | dū-tŭs ă | ē-nis (15 syllables), Iamque elided into adeo and thoraca into indutus, caesura after rutilum. The scanner (cost 0.0, not flagged) took ae as a diphthong, counted 14 syllables and made the rŭ- and -tĭ- of rutilum long."),
 '511': ('Ae.ne.as:--- ut:- fa.ma:-u fi.dem:u- mis.si.que:--u re.por.tant:u--', 3,
  "Wrong quantities with the right count (cost 1.0, not flagged): Aenēās has -nē- and -ās long (" + AE + "), fāmă is nominative with a short -ma, and fĭdem has a short fi-: Ae-nē | ās ut | fā-mă fĭ | dem mis | sī-quĕ rĕ | por-tant (14 syllables), caesura after fidem. The scanner made -ne- and -as short and -ma and fi- long."),
 '512': ('ex.plo.ra.to.res:----- e.qui.tum:uu- le.vi.a:uue im.pro.bus:-uu ar.ma:-u', 0,
  "Wrong quantities with the right count (cost 0.0, not flagged): explōrātōrēs has every syllable long and ĕquĭtum its first two short: ex-plō | rā-tō | rēs ĕ-quĭ | tum lĕ-vĭ | (a) im-prŏ-bŭs | ar-ma (15 syllables), levia elided into improbus, caesura after exploratores. The scanner made -plo- and -ra- short and e- and -qui- long."),
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
