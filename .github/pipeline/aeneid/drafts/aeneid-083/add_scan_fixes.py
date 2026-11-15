#!/usr/bin/env python3
"""Reviewer helper (aeneid-083): append hand scansions for XI.100-224 to scan-fixes.json, in line order after the last
existing key; keys are f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them.
A hand scansion is written compactly, one word per item, syllables split by '.', each followed by its quantity:
'-' long, 'u' short, 'e' elided (left unmarked), 'h' a hypermetric syllable elided into the next line (unmarked, after ×).
Foot numbers, the final × and the caesura (after word index CAES) are put in by this script, which then checks each entry
against the build's word-match rule and the validator's metre rule (half-line rule when the why starts 'Half-line') and the
syllable count stated in the why. sc None = the scanner's own fit (carrier lines). Dry run unless --write."""
import os, sys, json, re
HERE = '/home/user/Lectorium/.github/pipeline/aeneid/drafts/aeneid-083'
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
FP = os.path.join(A.HERE, 'scan-fixes.json')
raw = open(FP, encoding='utf8').read(); fx = json.loads(raw)
assert json.dumps(fx, ensure_ascii=False, indent=1) + '\n' == raw
P = A.part('aeneid-083'); LL = A.lines_of(P)
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
AESC = "The scanner (cost {c}, not flagged) split the initial Ae into A-e."
TEU = "Teu- is the Greek diphthong eu, one long syllable (as Teucri at 3.601 and 11.92)"
TEUSC = "The scanner (cost {c}, not flagged) split Teu- into Te-u and counted {k} syllables."
NEW = {
 '100': ('Iam.que:-e o.ra.to.res:---- a.de.rant:uu- ex:- ur.be:-u La.ti.na:u-u', 1,
  "Wrong quantities with the right count (cost 0.0, not flagged): ōrātōrēs has long ō- and -rā- (from ōro), and ădĕrant has short a- and -de- (ad + ĕram): Iam-qu(e) ō | rā-tō | rēs ă-dĕ | rant ex | ur-bĕ Lă | tī-na (14 syllables), Iamque elided into oratores, caesura after oratores. The scanner made o- and -ra- short and a-, -de- long."),
 '106': ('Quos:- bo.nus:uu Ae.ne.as:--- haud:- as.per.nan.da:---u pre.can.tis:u--', 2,
  "Aenēās: " + AE + ", -ās long: Quōs bŏ-nŭs | Ae-nē | ās haud | as-per | nan-dă prĕ | can-tis (14 syllables). " + AESC.format(c='1.2')),
 '111': ('o.ra.tis:--- E.qui.dem:uue et:- vi.vis:-- con.ce.de.re:--uu vel.lem:--', 3,
  "Wrong quantities with the right count (cost 0.0, not flagged): ōrātĭs has long ō- and -rā-, and ĕquĭdem short e- and -qui-, so the only fit lengthens -tis in the arsis of the second foot at the sense pause after the question (as se at 1.314, erat at 7.174): ō-rā | tīs ĕ-quĭ | d(em) et vī | vīs con | cē-dĕ-rĕ | vel-lem (14 syllables), equidem elided into et. The scanner made -ra- and -tis short and E-, -qui- long."),
 '115': ('Ae.qui.us:-uu huic:- Tur.num:-- fu.e.rat:uu- se:e op.po.ne.re:--uu mor.ti:-u', 2,
  "Wrong syllable division (cost 0.0, not flagged): Aequius is Ae-quĭ-ŭs, initial Ae- one long syllable and qu a single consonant, and huic is one syllable: Ae-quĭ-ŭs | huic Tur | num fŭ-ĕ | rat s(e) op | pō-nĕ-rĕ | mor-ti (15 syllables), se elided into opponere, caesura after Turnum. The scanner divided Aequ-ius and hu-ic; the quantities happen to come out the same, but the syllables (and the audio) were wrong."),
 '116': ('Si:- bel.lum:-- fi.ni.re:--u ma.nu:u- si:- pel.le.re:-uu Teu.cros:--', 2,
  TEU + ": Sī bel | lum fī | nī-rĕ mă | nū sī | pel-lĕ-rĕ | Teu-cros (14 syllables), caesura after finire. " + TEUSC.format(c='1.4', k=15)),
 '120': ('Di.xe.rat:-uu Ae.ne.as:--- Il.li:-e ob.sti.pu.e.re:-uu-u si.len.tes:u--', 1,
  "Aenēās: " + AE + ", -ās long: Dī-xĕ-răt | Ae-nē | ās Il | l(i) ob-stĭ-pŭ | ē-rĕ sĭ | len-tes (15 syllables), illi elided into obstipuere. " + AESC.format(c='1.2')),
 '134': ('per:- sil.vas:-- Teu.cri:-- mix.ti.que:--e in.pu.ne:--u La.ti.ni:u--', 2,
  TEU + ": per sil | vās Teu | crī mix | tī-qu(e) in | pū-nĕ Lă | tī-ni (13 syllables, four spondees and a dactyl in the fifth foot), -que elided into inpune, caesura after Teucri. " + TEUSC.format(c='0.0', k=14)),
 '148': ('At:- non:- E.van.drum:--- po.tis:uu est:- vis:- ul.la:-u te.ne.re:u-u', 4,
  "Wrong quantities with the right count (cost 0.0, not flagged), as 11.55: nōn is long and Ēvandrum has long Ē- (Greek eu): At nōn | Ē-van | drum pŏ-tĭs | est vīs | ul-lă tĕ | nē-re (14 syllables), caesura after est. The scanner made non and E- short and po- long."),
 '161': ('re.sta.rem:--e ut:- ge.ni.tor:uu- Tro.um:-- so.ci.a:uue ar.ma:-u se.cu.tum:u--', 2,
  "Troum is two syllables, Trō-um (genitive plural of Tros), its -um long by position before socia; genitor has short ge- and -ni-: rē-stā | r(em) ut gĕ-nĭ | tor Trō | um sŏ-cĭ | (a) ar-mă sĕ | cū-tum (15 syllables), restarem elided into ut and socia into arma, caesura after genitor. The scanner (cost 1.5, not flagged) made Troum one syllable and ge-, -ni- long (14 syllables)."),
 '162': ('ob.ru.e.rent:-uu- Ru.tu.li:uu- te.lis:-- A.ni.mam:uue ip.se:-u de.dis.sem:u--', 1,
  "Wrong quantities with the right count (cost 0.0, not flagged): tēlīs has long tē- and -īs, and ănĭmam short a- and -ni-: ob-rŭ-ĕ | rent Rŭ-tŭ | lī tē | līs ă-nĭ | m(am) ip-sĕ dĕ | dis-sem (16 syllables), animam elided into ipse, caesura after Rutuli. The scanner made te- and -lis short and A-, -ni- long."),
 '164': ('nec:- vos:- ar.gu.e.rim:-uu- Teu.cri:-- nec:- foe.de.ra:-uu nec:- quas:-', 2,
  TEU + ": nec vōs | ar-gŭ-ĕ | rim Teu | crī nec | foe-dĕ-ră | nec quās (14 syllables), caesura after arguerim. " + TEUSC.format(c='0.0', k=15)),
 '168': ('du.cen.tem:--e in:- La.ti.um:uu- Teu.cros:-- ce.ci.dis.se:uu-u iu.va.bit:u--', 2,
  TEU + ": dū-cen | t(em) in Lă-tĭ | um Teu | crōs cĕ-cĭ | dis-sĕ iŭ | vā-bit (15 syllables), ducentem elided into in, caesura after Latium. " + TEUSC.format(c='0.0', k=16)),
 '170': ('quam:- pi.us:uu Ae.ne.as:--- et:- quam:- mag.ni:-- Phry.ges:uu et:- quam:-', 2,
  "Bracketed line. Flagged COSTLY 2.2. Aenēās: " + AE + ", -ās long; Phrўgĕs has two short syllables (Greek nominative plural): quam pĭ-ŭs | Ae-nē | ās et | quam mag | nī Phrў-gĕs | et quam (14 syllables), caesura after Aeneas. The scanner split the initial Ae into A-e and counted 15 syllables."),
 '175': ('Tur.ne:-u Sed:u in.fe.lix:--- Teu.cros:-- quid:- de.mo.ror:-uu ar.mis:--', 2,
  TEU + "; quid is long by position before demoror: Tur-nĕ sĕd | in-fē | līx Teu | crōs quid | dē-mŏ-rŏr | ar-mis (14 syllables), caesura after infelix. " + TEUSC.format(c='0.0', k=15)),
 '184': ('iam:- pa.ter:uu Ae.ne.as:--- iam:- cur.vo:-e in:- li.to.re:-uu Tar.chon:--', 2,
  "Aenēās: " + AE + ", -ās long: iam pă-tĕr | Ae-nē | ās iam | cur-v(o) in | lī-tŏ-rĕ | Tar-chon (14 syllables), curvo elided into in. " + AESC.format(c='1.2')),
 '186': ('mo.re:-u tu.le.re:u-u pa.trum:u- sub.iec.tis.que:---e ig.ni.bus:-uu a.tris:--', 2,
  "Consonantal i after the prefix: subiectis is sub-iec-tis, three syllables, sub- long by position before the consonant i: mō-rĕ tŭ | lē-rĕ pă | trum sub | iec-tīs | qu(e) ig-nĭ-bŭs | ā-tris (15 syllables), -que elided into ignibus, caesura after patrum. The scanner (cost 0.0, not flagged) read su-bi-ec-tis with a vowel i and counted 16 syllables."),
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
