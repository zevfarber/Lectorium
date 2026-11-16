#!/usr/bin/env python3
"""Reviewer helper (aeneid-093): write hand scansions for XII.216-310 directly into scan-fixes.json (no other review is
running in parallel), appended in line order; keys are
f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them, and must not already be in scan-fixes.json.
A hand scansion is written compactly, one word per item, syllables split by '.', each followed by its quantity:
'-' long, 'u' short, 'e' elided (left unmarked). Foot numbers, the final x and the caesura (after word index CAES) are
put in by this script, which then checks each entry against the build's word-match rule and the validator's metre rule
and the syllable count stated in its why. Dry run unless --write."""
import os, sys, json, re
HERE = '/home/user/Lectorium/.github/pipeline/aeneid/drafts/aeneid-093'
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
fx = A.jload(os.path.join(A.HERE, 'scan-fixes.json'))
OUT = os.path.join(A.HERE, 'scan-fixes.json')
P = A.part('aeneid-093'); LL = A.lines_of(P)
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
 '230': ('ob.iec.ta.re:---e a.ni.mam:uu- Nu.me.ro.ne:uu-e an:- vi.ri.bus:-uu ae.qui:--', 1,
  "Same feet and quantities as the scanner's, different syllable division (as 2.444, 4.549): obiectare (ob + iacto) has the i consonantal after the prefix, ob | iec, not o-biec, which marked an open o long for the audio: ob-iec | tā-r(e) ă-nĭ | mām Nŭ-mĕ | rō-n(e) ān | vī-rĭ-bŭs | ae-quī (15 syllables), obiectare and Numerone elided, caesura after animam."),
 '231': ('non:- su.mus:uu En:- om.nes:-- et:- Tro.es:-u et:u Ar.ca.des:-uu hi:- sunt:-', 3,
  "Trōĕs is two syllables (Greek nominative plural, as 1.232, 9.689, 11.620), its -ĕs short before et: nōn sŭ-mŭs | ēn ōm | nēs ēt | Trō-ĕs ĕt | Ār-că-dĕs | hī sūnt (15 syllables), caesura after omnes. The scanner (cost 1.6, not flagged) ran Troes into one syllable and made the fourth foot a spondee, a fit with 14."),
 '232': ('fa.ta.les.que:---u ma.nus:u- in.fen.sa:--e Et.ru.ri.a:--uu Tur.no:--', 1,
  "Same feet and quantities as the scanner's, different syllable division: the E of Etruria is short by nature and the syllable is long only by position before tr (muta cum liquida), so it is Et-ru-ri-a, not an open long E-, which the audio would read as a long vowel: fā-tā | lēs-quĕ mă | nūs īn | fēn-s(a) Ēt | rū-rĭ-ă | Tūr-nō (14 syllables), infensa elided, caesura after manus."),
 '241': ('Qui:- si.bi:uu iam:- re.qui.em:uu- pug.nae:-- re.bus.que:--u sa.lu.tem:u--', 3,
  "requiem is three syllables, rĕ-quĭ-ĕm (qu + short i, as 4.433), not requ-iem with a long re-: Quī sĭ-bĭ | iām rĕ-quĭ | ēm pūg | nae rē | būs-quĕ să | lū-tēm (15 syllables), caesura after requiem. The scanner (cost 0.0, not flagged) took the i after qu as consonantal and fitted a line of 14."),
 '244': ('His:- a.li.ud:uu- ma.ius:-- Iu.tur.na:--e ad.iun.git:--u et:u al.to:--', 2,
  "adiungit has a consonantal i after the prefix (ad-iun-git, three syllables, ad- long by position; as 7.238 and 8.13 adiungere), with Iuturna elided into it, and maius is mai-ius, its first syllable long: Hīs ă-lĭ | ūd mā | iūs Iū | tūr-n(a) ād | iūn-gĭt ĕt | āl-tō (14 syllables), caesura after maius. The scanner (cost 0.0, not flagged) read a-di-un-git with a vowel i, a fit with 15."),
 '247': ('Nam.que:-u vo.lans:u- rub.ra:-- ful.vus:-- Io.vis:uu a.les:-u in:u ae.thra:--', 2,
  "rubra is ablative with aethra, so its -a is long, and its u is short by nature, the syllable long only by position before br (divided rub-ra so the audio keeps the u short); Iŏvis has a short o and its -is is short before ales: Nām-quĕ vŏ | lāns rūb | rā fūl | vūs Iŏ-vĭs | ā-lĕs ĭn | aeth-rā (15 syllables), caesura after rubra. The scanner (cost 1.0, not flagged) made rubra short-short and Iovis long-long."),
 '251': ('Ad.re.xe.re:---e a.ni.mos:uu- I.ta.li:uu- cunc.tae.que:--u vo.luc.res:u--', 1,
  "Same feet and quantities as the scanner's, different syllable division: Adrexere is ad + rexere, Ad-rē-xē-re, not an open long A- (the a is short), and volucres is vo-luc-res, the u short by nature and long only by position before cr: Ad-rē | xēr(e) ă-nĭ | mōs Ĭ-tă | lī cūnc | tae-quĕ vŏ | lūc-rēs (15 syllables), Adrexere elided, caesura after animos; Itali has a short I- (as 3.440, 9.133)."),
 '272': ('u.na:-u tot:u Ar.ca.di.o:-uu- con.iunx:-- Tyr.rhe.na:--u Gy.lip.po:u--', 2,
  "coniunx has the i consonantal after the prefix, con | iunx, two syllables (as 12.17, 12.178): ū-nă tŏt | Ār-că-dĭ | ō cōn | iūnx Tȳr | rhē-nă Gy̆ | līp-pō (15 syllables), caesura after Arcadio. The scanner (cost 0.0, not flagged) read co-ni-unx with a vowel i, a fit with 16."),
 '281': ('Tro.es:-u A.gyl.li.ni.que:u---e et:- pic.tis:-- Ar.ca.des:-uu ar.mis:--', 1,
  "Trōĕs is two syllables (Greek nominative plural, as 231), its -ĕs short before Agyllinique, whose A- is short: Trō-ĕs Ă | gȳl-lī | nī-qu(e) ēt | pīc-tīs | Ār-că-dĕs | ār-mīs (14 syllables), Agyllinique elided, caesura after it. The scanner (cost 1.0, not flagged) ran Troes into one syllable and made A- long."),
 '288': ('sub.i.ci.unt:-uu- in:u e.quos:u- et:- stric.tis:-- en.si.bus:-uu ad.sunt:--', 2,
  "Same feet and quantities as the scanner's, different syllable division (as 2.444, 9.553): subiciunt (sub + iacio) has the i consonantal after the prefix, sub-i-ci-unt with sub long by position, not an open long su-, which the audio would read as a long vowel: sūb-ĭ-cĭ | ūnt ĭn ĕ | quōs ēt | strīc-tīs | ēn-sĭ-bŭs | ād-sūnt (15 syllables), caesura after equos."),
 '308': ('dis.i.cit:-uu et:- spar.so:-- la.te:-- ri.gat:uu ar.ma:-u cru.o.re:u-u', 2,
  "lātē (adverb) has two long syllables and rĭgat two short ones, and disicit (dis + iacio) is dis-i-cit with dis long by position (as 11.870): dīs-ĭ-cĭt | ēt spār | sō lā | tē rĭ-găt | ār-mă crŭ | ō-rĕ (15 syllables), caesura after sparso. The scanner (cost 0.3, not flagged) made la-te short-short and ri-gat long-long, and divided di-si-cit with an open long di-."),
 '309': ('Ol.li:-- du.ra:-u qui.es:u- o.cu.los:uu- et:- fer.re.us:-uu ur.get:--', 2,
  "The same line as 10.745 and scanned as there: quies is two syllables, quĭ-ēs, and dura (nominative, with quies) has a short final a: Ōl-lī | dū-ră quĭ | ēs ŏ-cŭ | lōs ēt | fēr-rĕ-ŭs | ūr-gēt (15 syllables), caesura after quies. The scanner (cost 0.0, not flagged) read quies as one syllable and made -ra long."),
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
