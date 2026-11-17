#!/usr/bin/env python3
"""Reviewer helper (aeneid-095): write hand scansions for XII.441-553 directly into scan-fixes.json (no other review is
running in parallel), appended in line order; keys are
f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them, and must not already be in scan-fixes.json.
A hand scansion is written compactly, one word per item, syllables split by '.', each followed by its quantity:
'-' long, 'u' short, 'e' elided (left unmarked). Foot numbers, the final x and the caesura (after word index CAES) are
put in by this script, which then checks each entry against the build's word-match rule and the validator's metre rule
and the syllable count stated in its why. Dry run unless --write."""
import os, sys, json, re
HERE = '/home/user/Lectorium/.github/pipeline/aeneid/drafts/aeneid-095'
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
fx = A.jload(os.path.join(A.HERE, 'scan-fixes.json'))
OUT = os.path.join(A.HERE, 'scan-fixes.json')
P = A.part('aeneid-095'); LL = A.lines_of(P)
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
 '443': ('An.theus.que:--- Mnes.theus.que:--u ru.unt:u- om.nis.que:--u re.lic.tis:u--', 2,
  "Confirmed by hand, entered only to clear the COSTLY flag: Antheus and Mnestheus are each two syllables, An-theus and Mnēs-theus, the Greek diphthong eu (as Mnestheus at 12.384), and the -que of Antheusque is long by position before Mn-: Ān-theus | quē Mnēs | theus-quĕ rŭ | ūnt ōm | nīs-quĕ rĕ | līc-tis (14 syllables), caesura after ruunt. The scanner's parse (COSTLY 3.0) is right."),
 '451': ('Qua.lis:-u u.bi:ue ad:- ter.ras:-- ab.rup.to:--- si.de.re:-uu nim.bus:--', 3,
  "Same feet and quantities as the scanner's, different syllable division (as adlapsa at 12.319): abrupto is ab + rupto, ab-rup-tō with ab long by position, not an open long a- (a-brup), which the audio would read as a long vowel: Quā-lĭs ŭ | b(i) ād tēr | rās āb | rūp-tō | sī-dĕ-rĕ | nim-bus (14 syllables), ubi elided, caesura after terras."),
 '481': ('Haud:- mi.nus:uu Ae.ne.as:--- tor.tos:-- le.git:uu ob.vi.us:-uu or.bes:--', 2,
  "Aeneas is Ae-nē-ās, three syllables (initial diphthong one syllable, ē long), as at 12.311: Haud mĭ-nŭs | Ae-nē | ās tōr | tōs lĕ-gĭt | ōb-vĭ-ŭs | ōr-bes (15 syllables), caesura after Aeneas. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 16."),
 '482': ('ves.ti.gat.que:---u vi.rum:ue et:- dis.iec.ta:--u per:u ag.mi.na:-uu mag.na:--', 2,
  "disiecta has the i consonantal after the prefix, dis-iec-ta (dis + iacio), as disiectas at 2.608: vēs-tī | gāt-quĕ vĭ | r(um) ēt dīs | iēc-tă pĕr | āg-mĭ-nă | māg-na (15 syllables), virum elided, caesura after et. The scanner (cost 0.0, not flagged) read di-si-ec-ta with a vowel i and a short di-, a fit with 16."),
 '483': ('vo.ce:-u vo.cat:u- Quo.ti.ens:uu- o.cu.los:uu- con.ie.cit:--u in:u hos.tem:--', 2,
  "coniecit has the i consonantal after the prefix, con-iē-cit (con + iacio, perfect with long ē), as at 2.545 and 7.456: vō-cĕ vŏ | cāt quŏ-tĭ | ēns ŏ-cŭ | lōs cōn | iē-cĭt ĭn | hos-tem (16 syllables), caesura after Quotiens. The scanner (cost 0.0, not flagged) read co-ni-e-cit with a vowel i and a short co-, a fit with 17."),
 '491': ('Sub.sti.tit:-uu Ae.ne.as:--- et:- se:- col.le.git:--u in:u ar.ma:--', 1,
  "Aeneas is Ae-nē-ās, three syllables (initial diphthong one syllable, ē long), as at 12.311: Sub-stĭ-tĭt | Ae-nē | ās ēt | sē cōl | lē-gĭt ĭn | ar-ma (14 syllables), caesura after Aeneas. The scanner (cost 1.8, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 15."),
 '505': ('Ae.ne.as:--- Ru.tu.lum:uu- Su.cro.nem:--e e.a:uu pri.ma:-u ru.en.tis:u--', 1,
  "Aeneas is Ae-nē-ās, three syllables (initial diphthong one syllable, ē long), and Sucronem elides into ea (nominative, short -a): Ae-nē | ās Rŭ-tŭ | lūm Sū | crō-n(em) ĕ-ă | prī-mă rŭ | en-tis (15 syllables), caesura after Rutulum. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 16."),
 '506': ('pug.na:-u lo.co:u- sta.tu.it:uu- Teu.cros:-- haud:- mul.ta:-u mo.ran.tem:u--', 2,
  "Teucros is two syllables, Teu-crōs, the Greek diphthong eu (as Teucros at 1.304): pūg-nă lŏ | cō stă-tŭ | īt Teu | crōs haud | mūl-tă mŏ | ran-tem (15 syllables), caesura after statuit. The scanner (cost 0.0, not flagged) split Te-u into two shorts, a fit with 16."),
 '507': ('ex.ci.pit:-uu in:- la.tus:uu et:- qua:- fa.ta:-u ce.ler.ri.ma:u-uu cru.dum:--', 3,
  "quā (adverb, 'where') and fāta both have a long first vowel, and ce- of celerrima is short: ēx-cĭ-pĭt | īn lă-tŭs | ēt quā | fā-tă cĕ | lēr-rĭ-mă | crū-dum (16 syllables), caesura after et. The scanner (cost 0.0, not flagged) made qua and fa- short and ce- long, a false fit with the same count."),
 '515': ('no.men:-u E.chi.o.ni.um:u-uu- ma.tris.que:--u ge.nus:u- Pe.ri.di.ae:uu--', 1,
  "Echionium is Ĕ-chī-ŏ-nĭ-ŭm, five syllables, with long ī as in Echīon (Ovid, Met. 3.126), and nomen's final syllable is short before the vowel: nō-mĕn Ĕ | chī-ŏ-nĭ | ūm mā | trīs-quĕ gĕ | nūs Pĕ-rĭ | dī-ae (16 syllables), caesura after Echionium. The metre requires Peridīae with a long ī (the name is known only from this line). The scanner (COSTLY 3.8) made E- long and chi short and ran -nium into one syllable, a fit with 15."),
 '526': ('Ae.ne.as:--- Tur.nus.que:--u ru.unt:u- per:- proe.li.a:-uu nunc:- nunc:-', 2,
  "Aeneas is Ae-nē-ās, three syllables (initial diphthong one syllable, ē long), as at 12.311: Ae-nē | ās Tūr | nūs-quĕ rŭ | ūnt pēr | proē-lĭ-ă | nūnc nunc (14 syllables), caesura after ruunt. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 15."),
 '528': ('pec.to.ra:-uu nunc:- to.tis:-- in:- vol.ne.ra:-uu vi.ri.bus:-uu i.tur:--', 2,
  "tōtīs has both syllables long and volnera is vŏl-nĕ-ră: pēc-tŏ-ră | nūnc tō | tīs īn | vōl-nĕ-ră | vī-rĭ-bŭs | ī-tur (15 syllables), caesura after totis. The scanner (cost 0.0, not flagged) made to-tis short-short and -ne-ra long-long, a false fit with the same count."),
 '529': ('Mur.ra.num:--e hic:- a.ta.vos:uu- et:u a.vo.rum:u-e an.ti.qua:--u so.nan.tem:u--', 2,
  "atavos is ă-tă-vōs (at + avus, both a's short), so Murranum must have a long second syllable and hic counts long before the vowel: Mūr-rā | n(um) hīc ă-tă | vōs ĕt ă | vō-r(um) ān | tī-quă sŏ | nan-tem (15 syllables), Murranum and avorum elided, caesura after atavos. The scanner (cost 0.0, not flagged) made Mur-ra-hic a dactyl and a-ta- long, a false fit with the same count."),
 '535': ('Il.le:-u ru.en.ti:u-e Hyl.lo:-- a.ni.mis.que:uu-e im.ma.ne:--u fre.men.ti:u--', 2,
  "Hiatus after Hyllo: its -ō stays long in the strong place of the third foot and does not elide before animisque (ănĭmis has two short syllables): Īl-lĕ rŭ | ēn-t(i) Hȳl | lō ă-nĭ | mīs-qu(e) īm | mā-nĕ frĕ | men-ti (15 syllables), ruenti and animisque elided, caesura after Hyllo. The scanner (cost 0.0, not flagged) elided Hyllo and made a-ni- long, a false fit with the same count."),
 '538': ('Dex.te.ra:-uu nec:- tu.a:uu te:- Gra.ium:-- for.tis.si.me:--uu Cre.theu:--', 3,
  "Confirmed by hand, entered only to clear the COSTLY flag: Graium is two syllables, Grā-ium, with consonantal i (as 10.81 and 11.289), and Cretheu, the Greek vocative, is two, Crē-theu, the diphthong eu: Dēx-tĕ-ră | nēc tŭ-ă | tē Grā | ium fōr | tīs-sĭ-mĕ | Crē-theu (15 syllables), caesura after te. The scanner's parse (COSTLY 2.0) is right."),
 '540': ('Ae.ne.a:--- ve.ni.en.te:uu-u su.i:u- de.dit:uu ob.vi.a:-uu fer.ro:--', 2,
  "Aenea (ablative, final -ā long) is Ae-nē-ā, three syllables (initial diphthong one syllable, ē long): Ae-nē | ā vĕ-nĭ | ēn-tĕ sŭ | ī dĕ-dĭt | ōb-vĭ-ă | fer-ro (16 syllables), caesura after sui. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 17."),
 '553': ('nec:- mo.ra:uu nec:- re.qui.es:uu- vas.to:-- cer.ta.mi.ne:--uu ten.dunt:--', 3,
  "requies is three syllables, rĕ-quĭ-ēs (as quies at 12.309, quĭ-ēs): nēc mŏ-ră | nēc rĕ-quĭ | ēs vās | tō cēr | tā-mĭ-nĕ | ten-dunt (15 syllables), caesura after requies. The scanner (cost 0.0, not flagged) ran requies into two syllables, requ-ies, with a long first, a fit with 14."),
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
