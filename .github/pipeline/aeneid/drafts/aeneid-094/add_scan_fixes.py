#!/usr/bin/env python3
"""Reviewer helper (aeneid-094): write hand scansions for XII.311-440 directly into scan-fixes.json (no other review is
running in parallel), appended in line order; keys are
f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them, and must not already be in scan-fixes.json.
A hand scansion is written compactly, one word per item, syllables split by '.', each followed by its quantity:
'-' long, 'u' short, 'e' elided (left unmarked). Foot numbers, the final x and the caesura (after word index CAES) are
put in by this script, which then checks each entry against the build's word-match rule and the validator's metre rule
and the syllable count stated in its why. Dry run unless --write."""
import os, sys, json, re
HERE = '/home/user/Lectorium/.github/pipeline/aeneid/drafts/aeneid-094'
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
fx = A.jload(os.path.join(A.HERE, 'scan-fixes.json'))
OUT = os.path.join(A.HERE, 'scan-fixes.json')
P = A.part('aeneid-094'); LL = A.lines_of(P)
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
 '311': ('At:- pi.us:uu Ae.ne.as:--- dex.tram:-- ten.de.bat:--u i.ner.mem:u--', 2,
  "Aeneas is three syllables, Ae-nē-ās (initial diphthong one syllable, ē long), as at 1.305, which opens the same way: Āt pĭ-ŭs | Ae-nē | ās dex | trām tēn | dē-băt ĭ | nēr-mem (14 syllables), caesura after Aeneas. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 15."),
 '319': ('ec.ce:-u vi.ro:u- stri.dens:-- a.lis:-- ad.lap.sa:--u sa.git.ta:u-e est:-', 2,
  "Same feet and quantities as the scanner's, different syllable division: adlapsa is ad + lapsa, ad-lap-sa with a short a long by position, not an open long a- (a-dlap-sa), which the audio would read as a long vowel (as Adrexere at 12.251): ēc-cĕ vĭ | rō strī | dēns ā | līs ād | lāp-să să | gīt-t(a) ēst (14 syllables), sagitta elided, caesura after stridens."),
 '323': ('nec:- se.se:-e Ae.ne.ae:--- iac.ta.vit:--- vul.ne.re:-uu quis.quam:--', 2,
  "Aeneae is Ae-nē-ae, three long syllables, with sese elided into it (as 1.128): nēc sē | s(e) Ae-nē | ae iac | tā-vīt | vŭl-nĕ-rĕ | quis-quam (13 syllables), caesura after Aeneae. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 14."),
 '324': ('Tur.nus:-u ut:u Ae.ne.an:--- ce.den.tem:--e ex:- ag.mi.ne:-uu vi.dit:--', 2,
  "Aenean is Ae-nē-an, three syllables (initial diphthong one syllable, ē long, as 1.260): Tūr-nŭs ŭt | Ae-nē | ān cē | dēn-t(em) ēx | āg-mĭ-nĕ | vī-dit (14 syllables), cedentem elided, caesura after Aenean. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 15."),
 '349': ('qui:- quon.dam:-- cas.tra:-e ut:- Da.na.um:uu- spe.cu.la.tor:uu-u a.di.ret:u--', 4,
  "Danaum is three syllables, Dă-nă-ūm, both a's short (Greek Δαναοί), not Dā-naum with synizesis: quī quōn | dām cās | tr(a) ūt Dă-nă | ūm spĕ-cŭ | lā-tŏr ă | dī-ret (15 syllables), castra elided, caesura after Danaum. The scanner (cost 0.0, not flagged) ran -naum into one syllable and lengthened Da-, a fit with 14 (its known preference for synizesis in Danaum, as 1.30)."),
 '355': ('sis.tit:-u e.quos:u- bi.iu.gis:uu- et:- cur.ru:-- de.si.lit:-uu at.que:-u', 2,
  "biiugis is bĭ-jŭ-gīs, three syllables, the second i consonantal, as biiugos at 10.575, 10.587 and 10.595: sīs-tĭt ĕ | quōs bĭ-jŭ | gīs ēt | cūr-rū | dē-sĭ-lĭt | at-que (15 syllables), caesura after biiugis. The scanner (cost 1.5, not flagged) ran bi-iu together into one long syllable, a fit with 14."),
 '362': ('Huic:- co.mi.tem:uue As.by.ten:--- con.iec.ta:--- cus.pi.de:-uu mit.tit:--', 2,
  "coniecta has the i consonantal after the prefix, con-iec-tā (con + iacio; coniectā ablative, its -a long), as coniunx at 12.272: Huic cŏ-mĭ | t(em) Ās-by | tēn cōn | iēc-tā | cūs-pĭ-dĕ | mit-tit (14 syllables), comitem elided, caesura after Asbyten. The scanner (cost 0.0, not flagged) read co-ni-ec-ta with a vowel i, a fit with 15."),
 '371': ('Non:- tu.lit:uu in.stan.tem:--- Phe.geus:-- a.ni.mis.que:uu-u fre.men.tem:u--', 2,
  "Phegeus (Greek Φηγεύς) is two syllables, Phē-geus, with the Greek diphthong eu and a long Phē-, as at 5.263: Nōn tŭ-lĭt | īn-stān | tēm Phē | geus ă-nĭ | mīs-quĕ frĕ | mēn-tem (15 syllables), caesura after instantem. The scanner (cost 0.8, not flagged) split eu into e-u and made Phe- short, a fit with 16."),
 '372': ('ob.ie.cit:--- se.se:-e ad:- cur.rum:-e et:- spu.man.ti.a:--uu fre.nis:--', None,
  "obiecit has the i consonantal after the prefix, ob-iē-cit (ob + iacio, perfect with long ē), as obiectare at 12.230: ōb-iē | cīt sē | s(e) ād cūr | r(um) ēt spū | mān-tĭ-ă | frē-nis (13 syllables), sese and currum elided. The scanner (cost 0.0, not flagged) read o-bi-e-cit with a vowel i and a short o-, a fit with 14."),
 '377': ('Il.le:-u ta.men:u- cli.pe.o:uue ob.iec.to:--- con.ver.sus:--u in:u hos.tem:--', 3,
  "Same feet and quantities as the scanner's, different syllable division (as obiectare at 12.230): obiecto has the i consonantal after the prefix, ob-iec-tō with ob long by position, not an open long o- (o-biec), which the audio would read as a long vowel: Īl-lĕ tă | mēn clĭ-pĕ | (o) ōb-iēc | tō cōn | vēr-sŭs ĭn | hos-tem (15 syllables), clipeo elided, caesura after obiecto."),
 '384': ('in.te.re.a:-uue Ae.ne.an:--- Mnes.theus:-- et:- fi.dus:-u A.cha.tes:u--', 1,
  "Aenean is Ae-nē-an, three syllables (initial diphthong one syllable, ē long), with interea elided into it, and Mnestheus is two, Mnēs-theus, the Greek diphthong eu: īn-tĕ-rĕ | (a) Ae-nē | ān Mnēs | theus ēt | fī-dŭs Ă | chā-tes (14 syllables), caesura after Aenean. The scanner (COSTLY 2.7) split Ae- in two and read A-e-ne as a dactyl, a fit with 15."),
 '391': ('Iam.que:-e a.de.rat:uu- Phoe.bo:-e an.te:-e a.li.os:uu- di.lec.tus:--u I.a.pyx:u--', 4,
  "Iapyx (Greek Ἰᾶπυξ) is three syllables, Ĭ-ā-pyx, with a vowel I, as Iapyge at 8.710 and 11.678 and Iapygis at 11.247, so the fifth foot is a dactyl: Iām-qu(e) ă-dĕ | rāt Phoe | b(o) ānt(e) ă-lĭ | ōs dī | lēc-tŭs Ĭ | ā-pyx (15 syllables), Iamque, Phoebo and ante elided, caesura after alios. The scanner (COSTLY 2.0) read Ia- as one syllable with a consonantal I, a fit with 14."),
 '399': ('Ae.ne.as:--- mag.no:-- iu.ve.num:uue et:- mae.ren.tis:--u I.u.li:u--', 1,
  "Aeneas is Ae-nē-ās, three syllables (initial diphthong one syllable, ē long), and Iuli is three, Ĭ-ū-lī, with a vowel I (as Iulum at 1.709): Ae-nē | ās māg | nō iŭ-vĕ | n(um) ēt mae | rēn-tĭs Ĭ | ū-lī (14 syllables), iuvenum elided, caesura after magno. The scanner (COSTLY 3.2) split Ae- in two and ran Iu- into one syllable."),
 '419': ('am.bro.si.ae:-uu- su.cos:-- et:u o.do.ri.fe.ram:u-uu- pa.na.ce.am:uu-u', 1,
  "Confirmed by hand, entered only to clear the COSTLY flag: ambrosiae is four syllables (ἀμβροσία, short o) and panaceam four, Greek πανάκεια with long ē: ām-brŏ-sĭ | ae sū | cōs ĕt ŏ | dō-rĭ-fĕ | rām pă-nă | cē-am (16 syllables), caesura after sucos. The scanner's parse (COSTLY 2.0) is right."),
 '420': ('Fo.vit:-u e.a:u- vol.nus:-- lym.pha:-- lon.gae.vus:--u I.a.pyx:u--', 2,
  "Iapyx is three syllables, Ĭ-ā-pyx, with a vowel I (as 12.391), and ea is the ablative, ĕ-ā: Fō-vĭt ĕ | ā vōl | nūs lym | phā lōn | gae-vŭs Ĭ | ā-pyx (14 syllables), caesura after volnus. The scanner (COSTLY 2.0) read Ia- as one syllable with a consonantal I and made the fifth foot a spondee, a fit with 13."),
 '425': ('Ar.ma:-u ci.ti:u- pro.pe.ra.te:uu-u vi.ro:u- Quid:- sta.tis:-u I.a.pyx:u--', 3,
  "Iapyx is three syllables, Ĭ-ā-pyx, with a vowel I (as 12.391), so stātis keeps its short -is before it: Ār-mă cĭ | tī prŏ-pĕ | rā-tĕ vĭ | rō quĭd | stā-tĭs Ĭ | ā-pyx (16 syllables), caesura after viro. The scanner (COSTLY 2.0) read Ia- as one syllable with a consonantal I and made the fifth foot a spondee, a fit with 15."),
 '427': ('Non:- haec:- hu.ma.nis:--- o.pi.bus:uu- non:- ar.te:-u ma.gis.tra:u--', 2,
  "hūmānis has both vowels long and ŏpĭbus is short-short: Nōn haec | hū-mā | nīs ŏ-pĭ | būs nōn | ār-tĕ mă | gis-trā (14 syllables), caesura after humanis. The scanner (cost 0.6, not flagged) made -ma- short and o-pi- long, a false fit with the same count."),
 '428': ('pro.ve.ni.unt:-uu- ne.que:uu te:e Ae.ne.a:--- me.a:uu dex.te.ra:-uu ser.vat:--', 3,
  "Aenea (Greek vocative, final -ā long) is Ae-nē-ā, three syllables, with te elided into it: prō-vĕ-nĭ | ūnt nĕ-quĕ | (te) Ae-nē | ā mĕ-ă | dēx-tĕ-ră | ser-vat (16 syllables), caesura after Aenea. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl."),
 '438': ('Tu:- fa.ci.to:uu- mox:- cum:- ma.tu.ra:--e a.do.le.ve.rit:uu-uu ae.tas:--', 3,
  "mātūra has both vowels long and adolēverit is ă-dŏ-lē-vĕ-rit: Tū fă-cĭ | tō mōx | cūm mā | tū-r(a) ă-dŏ | lē-vĕ-rĭt | ae-tās (15 syllables), matura elided, caesura after cum. The scanner (cost 0.0, not flagged) made ma-tu- short and a-do- long, a false fit with the same count."),
 '440': ('et:- pa.ter:uu Ae.ne.as:--- et:u a.vun.cu.lus:u-uu ex.ci.tet:-uu Hec.tor:--', 2,
  "The line is 3.343 with excitet for excitat, scanned as there: Aeneas is Ae-nē-ās, three syllables: ēt pă-tĕr | Ae-nē | ās ĕt ă | vūn-cŭ-lŭs | ēx-cĭ-tĕt | Hec-tor (16 syllables), caesura after Aeneas. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 17."),
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
