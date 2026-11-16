#!/usr/bin/env python3
"""Reviewer helper (aeneid-084): append hand scansions for XI.225-335 to scan-fixes.json, in line order after the last
existing key; keys are f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them.
A hand scansion is written compactly, one word per item, syllables split by '.', each followed by its quantity:
'-' long, 'u' short, 'e' elided (left unmarked), 'h' a hypermetric syllable elided into the next line (unmarked, after ×).
Foot numbers, the final × and the caesura (after word index CAES) are put in by this script, which then checks each entry
against the build's word-match rule and the validator's metre rule (half-line rule when the why starts 'Half-line') and the
syllable count stated in the why. sc None = the scanner's own fit (carrier lines). Dry run unless --write."""
import os, sys, json, re
HERE = '/home/user/Lectorium/.github/pipeline/aeneid/drafts/aeneid-084'
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
FP = os.path.join(A.HERE, 'scan-fixes.json')
raw = open(FP, encoding='utf8').read(); fx = json.loads(raw)
assert json.dumps(fx, ensure_ascii=False, indent=1) + '\n' == raw
P = A.part('aeneid-084'); LL = A.lines_of(P)
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
 '232': ('Fa.ta.lem:--e Ae.ne.an:--- ma.ni.fes.to:uu-- nu.mi.ne:-uu fer.ri:--', 1,
  "Aenēān: " + AE + ", and the Greek accusative -ān long: Fā-tā | l(em) Ae-nē | ān mă-nĭ | fēs-tō | nū-mĭ-nĕ | fer-ri (14 syllables), Fatalem elided into Aenean, caesura after Aenean. " + AESC.format(c='1.2', k=15)),
 '247': ('vic.tor:-- Gar.ga.ni:--- con.de.bat:--u I.a.py.gis:u-uu a.gris:--', 1,
  "Iapygis is four syllables, Ĭ-ā-pў-gĭs, with a vowel I (Greek Iapyx; as Iapyge at 8.710), and condebat's -băt is short before it: vic-tōr | Gār-gā | nī cōn | dē-băt Ĭ | ā-pў-gĭs | ā-gris (14 syllables), caesura after Gargani. The scanner (cost 0.0, not flagged) read Ia- as one syllable with a consonantal i, made -bat long and counted 13."),
 '251': ('Au.di.tis:--- il.le:-e haec:- pla.ci.do:uu- sic:- red.di.dit:-uu o.re:--', 2,
  "Wrong quantities with the right count (cost 0.0, not flagged): audītīs has long -dī- (audītus) and the long ablative ending -īs, and plăcĭdō short pla- and -ci-: Au-dī | tīs il | l(e) haec plă-cĭ | dō sīc | red-dĭ-dĭt | ō-re (14 syllables), ille elided into haec, caesura after haec. The scanner made -di- and -tis short and pla-, -ci- long."),
 '254': ('sol.li.ci.tat:-uu- sua.det.que:--e ig.no.ta:--u la.ces.se.re:u-uu bel.la:-u', 1,
  "suādet is two syllables, the u consonantal (sw-), as at 2.9, 4.81 and 9.340: sol-lĭ-cĭ | tat suā | dētqu(e) ig | nō-tă lă | ces-sĕ-rĕ | bel-la (15 syllables), -que elided into ignota, caesura after suadetque. The scanner (cost 0.0, not flagged) read su-a-det as three syllables and counted 16."),
 '262': ('A.tri.des:--- Pro.tei:-- Me.ne.la.us:uu-u a.dus.que:u-u co.lum.nas:u--', 1,
  "Prōtei is the Greek genitive of Proteus (Πρωτεύς, long Prō-), its -ei one syllable by synizesis; Mĕnĕlāŭs has four syllables, a and u apart (as Menelaum at 6.525): Ā-trī | dēs Prō | tei Mĕ-nĕ | lā-ŭs ă | dus-quĕ cŏ | lum-nas (15 syllables), caesura after Protei. The scanner (cost 0.0, not flagged) made Pro- short and Protei three syllables, and took -laus as one; the count came out the same but the syllables and quantities were wrong."),
 '279': ('nec:- mi.hi:uu cum:- Teu.cris:-- ul.lum:-- post:- e.ru.ta:-uu bel.lum:--', 3,
  TEU + ": nec mĭ-hĭ | cum Teu | crīs ul | lum pōst | ē-rŭ-tă | bel-lum (14 syllables), caesura after Teucris. " + TEUSC.format(c='0.0', k=15)),
 '282': ('ver.ti.te:-ue ad:u Ae.ne.an:--- Ste.ti.mus:uu- te.la:-e as.pe.ra:-uu con.tra:--', 2,
  "Aenēān: " + AE + ", and the Greek accusative -ān long: ver-tĭt(e) ăd | Ae-nē | ān stĕ-tĭ | mus tēl | (a) as-pĕ-ră | con-tra (15 syllables), vertite elided into ad and tela into aspera, caesura after Aenean. " + AESC.format(c='1.2', k=16)),
 '289': ('Hec.to.ris:-uu Ae.ne.ae.que:---u ma.nu:u- vic.to.ri.a:--uu Gra.ium:--', 2,
  "Aenēāe: " + AE + ", and the genitive -ae long; Grāium is two syllables with a consonantal i (as 10.81): Hec-tŏ-rĭs | Ae-nē | ae-quĕ mă | nū vic | tō-rĭ-ă | Grā-ium (15 syllables), caesura after manu. " + AESC.format(c='1.2', k=16)),
 '292': ('hic:- pi.e.ta.te:uu-u pri.or:u- Co.e.ant:uu- in:- foe.de.ra:-uu dex.trae:--', 2,
  "coeant is three syllables, cŏ-ĕ-ant, the ordinary reading (as 7.317, 7.546, 8.385): hīc pĭ-ĕ | tā-tĕ prĭ | ōr cŏ-ĕ | ant in | foe-dĕ-ră | dex-trae (16 syllables), caesura after prior. The scanner (cost 0.0, not flagged) preferred synizesis, coe- one syllable, and counted 15."),
 '300': ('Ut:- pri.mum:-- pla.ca.ti:--e a.ni.mi:uue et:- tre.pi.da:uue o.ra:-u qui.e.runt:u--', 1,
  "Wrong quantities with the right count (cost 1.0, not flagged): plācātī has long plā- and -cā- (plāco), and ănĭmī short a- and -ni-: Ut prī | mum plā | cāt(i) ă-nĭ | m(i) et trĕ-pĭ | d(a) ō-ră quĭ | ē-runt (15 syllables), placati elided into animi, animi into et and trepida into ora, caesura after primum. The scanner made -ca- short and a-, -ni- long."),
 '302': ('An.te:-e e.qui.dem:uu- sum.ma:-- de:- re:- sta.tu.is.se:uu-u La.ti.ni:u--', 4,
  "Wrong quantities with the right count (cost 0.0, not flagged): ĕquĭdem has short e- and -qui- (as 11.111), summā is ablative with long -ā, and dē is long: Ant(e) ĕ-quĭ | dem sum | mā dē | rē stă-tŭ | is-sĕ Lă | tī-ni (15 syllables), Ante elided into equidem, caesura after re. The scanner made e-, -qui- long and summa, de short."),
 '308': (None, None,
  "Carrier line, checked by hand: spēm sī | qu(am) ad-scī | tīs Ae | tō-l(um) hă-bŭ | is-tĭs ĭn | ar-mis (14 syllables), siquam elided into adscitis and Aetolum into habuistis, Aetolum with initial Ae- one long syllable. The scanner's fit is correct; the entry is needed only because this line shares a unit with 11.309, which the scanner cannot fit, and a unit with an unresolved line receives no sc at all."),
 '309': ('po.ni.te:-uu Spes:- si.bi:uu quis.que:-u sed:u haec:- quam:e an.gus.ta:--u vi.de.tis:u--', 5,
  "Flagged UNRESOLVED. The monosyllable quam is elided into angusta: pō-nĭ-tĕ | spēs sĭ-bĭ | quis-quĕ sĕd | haec qu(am) an | gus-tă vĭ | dē-tis (16 syllables), caesura after haec. The scanner found no fit with the elided monosyllable."),
 '321': ('ce.dat:-u a.mi.ci.ti.ae:u-uu- Teu.cro.rum:--e et:- foe.de.ris:-uu ae.quas:--', 1,
  TEU + ": cē-dăt ă | mī-cĭ-tĭ | ae Teu | crōr(um) et | foe-dĕ-rĭs | ae-quas (15 syllables), Teucrorum elided into et, caesura after amicitiae. " + TEUSC.format(c='0.0', k=16)),
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
