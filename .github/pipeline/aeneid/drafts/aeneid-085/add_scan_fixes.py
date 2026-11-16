#!/usr/bin/env python3
"""Reviewer helper (aeneid-085): append hand scansions for XI.336-444 to scan-fixes.json, in line order after the last
existing key; keys are f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them.
A hand scansion is written compactly, one word per item, syllables split by '.', each followed by its quantity:
'-' long, 'u' short, 'e' elided (left unmarked), 'h' a hypermetric syllable elided into the next line (unmarked, after ×).
Foot numbers, the final × and the caesura (after word index CAES) are put in by this script, which then checks each entry
against the build's word-match rule and the validator's metre rule (half-line rule when the why starts 'Half-line') and the
syllable count stated in the why. sc None = the scanner's own fit (carrier lines). Dry run unless --write."""
import os, sys, json, re
HERE = '/home/user/Lectorium/.github/pipeline/aeneid/drafts/aeneid-085'
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
FP = os.path.join(A.HERE, 'scan-fixes.json')
raw = open(FP, encoding='utf8').read(); fx = json.loads(raw)
assert json.dumps(fx, ensure_ascii=False, indent=1) + '\n' == raw
P = A.part('aeneid-085'); LL = A.lines_of(P)
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
 '361': ('pro.i.cis:-uu O:- La.ti.o:uu- ca.put:uu ho.rum:-e et:- cau.sa:-u ma.lo.rum:u--', 2,
  "proicis is three syllables, prō-ĭ-cĭs, the i of the root a vowel after the prefix (as reice, rē-ĭ-ce, Eclogue 3.96): prō-ĭ-cĭs | Ō Lă-tĭ | ō că-pŭt | hōr(um) et | cau-să mă | lō-rum (16 syllables), horum elided into et, caesura after Latio. The scanner (cost 1.5, not flagged) took proi- as one syllable and lengthened -cis before the vowel of O."),
 '373': (None, None,
  "Carrier line, checked by hand: ster-nā | mur cam | pīs ĕ-tĭ | am tū | sī-quă tĭ | bī vis (14 syllables), tibī with its final syllable long. The scanner's fit is correct; the entry is needed only because the unit 373-375 contains 11.375, a half-line the scanner cannot fit, and a unit with an unresolved line receives no sc at all."),
 '374': (None, None,
  "Carrier line, checked by hand: sī pă-trĭ | ī quid | Mar-tĭs hă | bēs il | l(um) as-pĭ-cĕ | con-tra (15 syllables), illum elided into aspice. The scanner's fit is correct; the entry is needed only because the unit 373-375 contains the half-line 11.375 (see 11.373)."),
 '375': ('qui:- vo.cat:uu', None,
  "Half-line (hemistich), one of Virgil's unfinished lines, as 10.580 and 10.728: quī vŏ-căt, a long syllable and two short, the last marked × as the end of the line (3 syllables), ending Drances' speech. There is no hexameter to fit; the scanner returns UNRESOLVED. 373 and 374, in the same unit, are entered as carriers."),
 '383': ('Proin.de:-u to.na:ue e.lo.qui.o:-uu- so.li.tum:uu- ti.bi:uu me.que:-u ti.mo.ris:u--', 2,
  "ēlŏquĭō is four syllables with a short -lo- (ē + loquor): Proin-dĕ tŏ | n(a) ē-lŏ-quĭ | ō sŏ-lĭ | tum tĭ-bĭ | mē-quĕ tĭ | mō-ris (17 syllables), Proinde two syllables by synizesis, tona elided into eloquio, caesura after eloquio. The scanner (cost 0.0, not flagged) made -lo- long and ran -quio into one syllable; the count came out the same but the syllables and quantities were wrong."),
 '389': (None, None,
  "Carrier line, checked by hand: Ī-mŭs ĭn | ad-ver | sōs quid | ces-sās | an tĭ-bĭ | Mā-vors (14 syllables). The scanner's fit is correct; the entry is needed only because the unit 389-391 (An tibi Mavors… semper erit?) contains 11.391, a half-line the scanner cannot fit, and a unit with an unresolved line receives no sc at all."),
 '390': (None, None,
  "Carrier line, checked by hand: ven-tō | s(a) in lin | guā pĕ-dĭ | bus-quĕ fŭ | gā-cĭ-bŭs | is-tis (15 syllables), ventosa elided into in, linguā ablative. The scanner's fit is correct; the entry is needed only because the unit 389-391 contains the half-line 11.391 (see 11.389)."),
 '391': ('sem.per:-u e.rit:uu', None,
  "Half-line (hemistich), one of Virgil's unfinished lines, as 2.346 and 10.728: sem-pĕr ĕ | rĭt, a dactyl and one syllable (– ⏑ ⏑ | ×), the last marked × as the end of the line (4 syllables). There is no hexameter to fit; the scanner returns UNRESOLVED. 389 and 390, in the same unit, are entered as carriers."),
 '434': ('Quod:- si:- me:- so.lum:-- Teu.cri:-e in:- cer.ta.mi.na:--uu pos.cunt:--', 3,
  TEU + ": Quod sī | mē sō | lum Teu | cr(i) in cer | tā-mĭ-nă | pos-cunt (13 syllables), Teucri elided into in, caesura after solum. " + TEUSC.format(c='0.6', k=14)),
 '440': ('il.le:-u li.cet:u- Vo.bis:-- a.ni.mam:uue hanc:- so.ce.ro.que:uu-u La.ti.no:u--', 2,
  "Wrong quantities with the right count (cost 0.0, not flagged): vōbīs has both syllables long and ănĭmam both short: il-lĕ lĭ | cēt vō | bīs ă-nĭ | m(am) hanc sŏ-cĕ | rō-quĕ Lă | tī-no (16 syllables), animam elided into hanc, caesura after Vobis. The scanner made Vo- and -bis short and a-, -ni- long."),
 '442': ('de.vo.vi:--- So.lum:-e Ae.ne.as:--- vo.cat:uu et:- vo.cet:uu o.ro:--', 2,
  "Aenēās: " + AE + ", and the nominative -ās long: dē-vō | vī sō | l(um) Ae-nē | ās vŏ-căt | et vŏ-cĕt | ō-ro (14 syllables), Solum elided into Aeneas, caesura after Aeneas. " + AESC.format(c='1.2', k=15)),
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
