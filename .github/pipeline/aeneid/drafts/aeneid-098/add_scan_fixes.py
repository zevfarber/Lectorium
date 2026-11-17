#!/usr/bin/env python3
"""Reviewer helper (aeneid-098): write hand scansions for XII.746-842 directly into scan-fixes.json (no other review is
running in parallel), appended in line order; keys are
f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them, and must not already be in scan-fixes.json.
A hand scansion is written compactly, one word per item, syllables split by '.', each followed by its quantity:
'-' long, 'u' short, 'e' elided (left unmarked). Foot numbers, the final x and the caesura (after word index CAES) are
put in by this script, which then checks each entry against the build's word-match rule and the validator's metre rule
and the syllable count stated in its why. Dry run unless --write."""
import os, sys, json, re
HERE = '/home/user/Lectorium/.github/pipeline/aeneid/drafts/aeneid-098'
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
fx = A.jload(os.path.join(A.HERE, 'scan-fixes.json'))
OUT = os.path.join(A.HERE, 'scan-fixes.json')
P = A.part('aeneid-098'); LL = A.lines_of(P)
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
 '746': ('Nec:- mi.nus:uu Ae.ne.as:--- quam.quam:-- tar.da.ta:--u sa.git.ta:u--', 2,
  "Aeneas is Ae-nē-ās, three syllables (initial diphthong one syllable, ē long), as at 12.311: Nēc mĭ-nŭs | Ae-nē | ās quām | quām tār | dā-tă să | gīt-ta (14 syllables), caesura after Aeneas. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 15."),
 '760': ('Ae.ne.as:--- mor.tem:-- con.tra:-- prae.sens.que:--u mi.na.tur:u--', 1,
  "Aeneas is Ae-nē-ās, three syllables (initial diphthong one syllable, ē long), as at 12.311; contrā (adverb) has its long -ā: Ae-nē | ās mōr | tēm cōn | trā prae | sēns-quĕ mĭ | nā-tur (13 syllables), caesura after mortem. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 14."),
 '762': ('ex.ci.su.rum:---e ur.bem:-- mi.ni.tans:uu- et:- sau.ci.us:-uu ins.tat:--', 1,
  "excīsūrum (future participle of excīdo, ex + caedo, supine excīsum) has both -cī- and -sū- long, its -um elided into urbem, and mĭnĭtans has two short syllables: ēx-cī | sū-r(um) ūr | bēm mĭ-nĭ | tāns ēt | saū-cĭ-ŭs | īns-tat (14 syllables), caesura after urbem. The scanner (cost 0.0, not flagged) made -ci- and -su- short and mi-ni- long, a false fit with the same count."),
 '770': ('sed:- stir.pem:-- Teu.cri:-- nul.lo:-- dis.cri.mi.ne:--uu sac.rum:--', 2,
  "Teucri is two syllables, Teu-crī, the Greek diphthong eu (as Teucros at 12.506 and Teucri at 12.744); sacrum is divided sac-rum, its short a long by position before the mute and liquid (as suprema, sup-rē-ma, at 12.653): sēd stīr | pēm Teū | crī nūl | lō dīs | crī-mĭ-nĕ | sāc-rum (13 syllables), caesura after Teucri. The scanner (cost 0.0, not flagged) split Te-u into two short syllables, a fit with 14."),
 '772': ('Hic:- has.ta:-e Ae.ne.ae:--- sta.bat:-- huc:- im.pe.tus:-uu il.lam:--', 3,
  "Aeneae (genitive) is Ae-nē-ae, three syllables (initial diphthong one syllable, ē long), with hasta elided into it; the -bat of stabat is lengthened in the arsis of the fourth foot at the sense pause and the hephthemimeral caesura (h does not make position), as erat hoc at 7.174: Hīc hās | t(a) Ae-nē | ae stā | bāt hūc | īm-pĕ-tŭs | īl-lam (13 syllables), four spondees for the spear stuck fast, caesura after stabat. The scanner (COSTLY 2.1) split Ae- in two, a fit with 14."),
 '783': ('ro.bo.ris:-uu Ae.ne.as:--- Dum:- ni.ti.tur:-uu a.cer:-u et:u ins.tat:--', 1,
  "Aeneas is Ae-nē-ās, three syllables (initial diphthong one syllable, ē long), as at 12.311: rō-bŏ-rĭs | Ae-nē | ās Dūm | nī-tĭ-tŭr | ā-cĕr ĕt | īns-tat (15 syllables), caesura after Aeneas (at the full stop). The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 16."),
 '788': ('Ol.li:-- sub.li.mes:--- ar.mis:-- a.ni.mis.que:uu-u re.fec.ti:u--', 1,
  "Same feet and quantities as the scanner's, different syllable division (as sublatis at 12.26, sublapsa at 12.686): sublimes is sub-lī-mes with sub long by position, not an open long su- (su-bli), which the audio would read as a long vowel: Ōl-lī | sūb-lī | mēs ār | mīs ă-nĭ | mīs-quĕ rĕ | fēc-ti (14 syllables), caesura after sublimes."),
 '792': ('ad.lo.qui.tur:-uu- ful.va:-- pug.nas:-- de:- nu.be:-u tu.en.tem:u--', 1,
  "Same feet and quantities as the scanner's, different syllable division (as 4.8, 8.372 and 10.228): adloquitur is ad-lŏ-quĭ-tur with ad long by position, not an open long a- (a-dlo), which the audio would read as a long vowel: ād-lŏ-quĭ | tūr fūl | vā pūg | nās dē | nū-bĕ tŭ | ēn-tem (14 syllables), caesura after fulva."),
 '793': ('Qua:- iam:- fi.nis:-u e.rit:u- con.iunx:-- Quid:- de.ni.que:-uu res.tat:--', 3,
  "coniunx (con + iunx) has the i consonantal after the prefix, con | iunx, two syllables, con long by position (as 12.80, 12.272): Quā iām | fī-nĭs ĕ | rīt cōn | iūnx Quīd | dē-nĭ-quĕ | rēs-tat (14 syllables), caesura after erit. The scanner (cost 0.0, not flagged) read co-ni-unx, three syllables with short co- and ni-, a fit with 15."),
 '794': ('In.di.ge.tem:-uue Ae.ne.an:--- scis:- ip.sa:-e et:- sci.re:-u fa.te.ris:u--', 1,
  "Aenean is Ae-nē-ān, three syllables (initial diphthong one syllable, ē long, Greek accusative -ān), with Indigetem (Īn-dĭ-gĕ-tem) elided into it, as 12.63: Īn-dĭ-gĕ | t(em) Ae-nē | ān scīs | īps(a) ēt | scī-rĕ fă | tē-ris (14 syllables), caesura after Aenean. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 15."),
 '803': ('ven.tum:-e ad:- sup.re.mum:--e est:- Ter.ris:-- a.gi.ta.re:uu-u vel:u un.dis:--', 3,
  "Same feet and quantities as the scanner's, different syllable division and caesura: suprēmum has a short u (from super), its first syllable long by position before the mute and liquid, divided sup-rē-mum (as suprema at 12.653), not an open long su- that the audio would read as a long vowel; the main caesura falls at the full stop after est: vēnt(um) ād | sūp-rē | m(um) ēst Tēr | rīs ă-gĭ | tā-rĕ vĕl | ūn-dis (14 syllables), ventum and supremum elided."),
 '808': ('Is.ta:-u qui.dem:u- qui.a:uu no.ta:-u mi.hi:u- tu.a:uu mag.ne:-u vo.lun.tas:u--', 4,
  "quia is two short syllables, quĭ-ă, not one by synizesis (as 2.84, 5.231, 8.650): Īs-tă quĭ | dēm quĭ-ă | nō-tă mĭ | hī tŭ-ă | māg-nĕ vŏ | lūn-tas (17 syllables, five dactyls), caesura after mihi. The scanner (cost 0.6, not flagged) contracted quia to one long syllable and made the second foot a spondee, a fit with 16."),
 '812': ('sta.rem:-e a.ci.e:uu- tra.he.rem.que:uu-e i.ni.mi.ca:uu-e in:- proe.li.a:-uu Teu.cros:--', -1,
  "Confirmed by hand, entered only to clear the COSTLY flag (as 12.704): stār(em) ă-cĭ | ē tră-hĕ | rēm-qu(e) ĭ-nĭ | mīc(a) īn | proe-lĭ-ă | Teu-cros (16 syllables), starem, traheremque and inimica elided; acie is the ablative with long -ē, Teucros has Greek eu as one syllable, and in is long before pr. The scanner's fit (COSTLY 2.0, no caesura marked because the penthemimeral after traheremque falls on an elision) is right."),
 '816': ('ad.iu.ro:--- Sty.gi.i:uu- ca.put:uu im.pla.ca.bi.le:---uu fon.tis:--', 1,
  "adiuro (ad + iuro) has the i consonantal after the prefix, ad-iū-rō, three long syllables, ad long by position (as adiungit at 12.244): ād-iū | rō Stў-gĭ | ī că-pŭt | īm-plā | cā-bĭ-lĕ | fōn-tis (15 syllables), caesura after Stygii. The scanner (cost 0.0, not flagged) read a-di-u-ro with a vowel i and short di- and u-, a fit with 16."),
 '824': ('neu:- Tro.as:-- fi.e.ri:uu- iu.be.as:uu- Teu.cros.que:--u vo.ca.ri:u--', 2,
  "Teucrosque has Greek eu as one long syllable, Teu-crōs-que (as Teucros at 12.506), and Trōăs (Greek accusative plural, short -ăs) has its last syllable long by position before fieri, whose fĭ- is short: neū Trō | ās fĭ-ĕ | rī iŭ-bĕ | ās Teū | crōs-quĕ vŏ | cā-ri (15 syllables), caesura after fieri. The scanner (COSTLY 2.0) split Te-u into two short syllables, a fit with 16."),
 '827': ('sit:- Ro.ma.na:--u po.tens:u- I.ta.la:uu- vir.tu.te:--u pro.pa.go:u--', 2,
  "Rōmānă has long Rō- and -mā- (nominative, short -a, with propago), and Ĭtălā (ablative with virtute) a short I-: sīt Rō | mā-nă pŏ | tēns Ĭ-tă | lā vīr | tū-tĕ prŏ | pā-go (15 syllables), caesura after potens. The scanner (cost 0.0, not flagged) made Ro- and -ma- short and -na po- long, a false fit with the same count."),
 '829': ('Ol.li:-- sub.ri.dens:--- ho.mi.num:uu- re.rum.que:--u re.per.tor:u--', 1,
  "Same feet and quantities as the scanner's, different syllable division (as sublatis at 12.26): subridens is sub + ridens, sub-rī-dens with sub long by position, not an open long su- (su-bri), which the audio would read as a long vowel: Ōl-lī | sūb-rī | dēns hŏ-mĭ | nūm rē | rūm-quĕ rĕ | pēr-tor (14 syllables), caesura after subridens."),
 '836': ('sub.si.dent:--- Teu.cri:-- Mo.rem:-- ri.tus.que:--u sa.cro.rum:u--', 1,
  "Teucri is two syllables, Teu-crī, the Greek diphthong eu (as 12.744): sūb-sī | dēnt Teū | crī Mō | rēm rī | tūs-quĕ să | crō-rum (13 syllables), caesura after Teucri (at the full stop). The scanner (cost 0.0, not flagged) split Te-u into two short syllables, a fit with 14."),
 '837': ('ad.i.ci.am:-uu- fa.ci.am.que:uu-e om.nis:-- u.no:-e o.re:-u La.ti.nos:u--', 2,
  "Same feet and quantities as the scanner's, different syllable division (as subiciunt at 12.288 and inicit at 9.553): adiciam (ad + iacio) has the i consonantal after the prefix, written once, so it is ad-ĭ-cĭ-am with ad long by position, not an open long a- (a-di), which the audio would read as a long vowel: ād-ĭ-cĭ | ām fă-cĭ | ām(que) ōm | nīs ūn(o) | ō-rĕ Lă | tī-nos (15 syllables), faciamque and uno elided, caesura after omnis."),
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
