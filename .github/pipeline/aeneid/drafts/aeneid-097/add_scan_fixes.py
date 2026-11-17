#!/usr/bin/env python3
"""Reviewer helper (aeneid-097): write hand scansions for XII.650-745 directly into scan-fixes.json (no other review is
running in parallel), appended in line order; keys are
f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them, and must not already be in scan-fixes.json.
A hand scansion is written compactly, one word per item, syllables split by '.', each followed by its quantity:
'-' long, 'u' short, 'e' elided (left unmarked). Foot numbers, the final x and the caesura (after word index CAES) are
put in by this script, which then checks each entry against the build's word-match rule and the validator's metre rule
and the syllable count stated in its why. Dry run unless --write."""
import os, sys, json, re
HERE = '/home/user/Lectorium/.github/pipeline/aeneid/drafts/aeneid-097'
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
fx = A.jload(os.path.join(A.HERE, 'scan-fixes.json'))
OUT = os.path.join(A.HERE, 'scan-fixes.json')
P = A.part('aeneid-097'); LL = A.lines_of(P)
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
 '653': ('Tur.ne:-e in:- te:- sup.re.ma:--u sa.lus:u- mi.se.re.re:uu-u tu.o.rum:u--', 4,
  "suprēma has its first syllable long by position before the mute and liquid pr (divided sup-rē-ma, so the audio does not read an open long u, as Etruria at 12.232), and salus is să-lūs: Tūrn(e) īn | tē sūp | rē-mă să | lūs mĭ-sĕ | rē-rĕ tŭ | ō-rum (15 syllables), Turne elided, caesura after salus (at the colon). The scanner (cost 0.6, not flagged) made su- and pre- short and ma- and sa- long, a false fit with the same count."),
 '654': ('Ful.mi.nat:-uu Ae.ne.as:--- ar.mis:-- sum.mas.que:--u mi.na.tur:u--', 1,
  "Aeneas is Ae-nē-ās, three syllables (initial diphthong one syllable, ē long), as at 12.311: Fūl-mĭ-năt | Ae-nē | ās ār | mīs sūm | mās-quĕ mĭ | nā-tur (14 syllables), caesura after Aeneas. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 15."),
 '678': ('Stat:- con.fer.re:--u ma.num:ue Ae.ne.ae:--- stat:- quid.quid:-u a.cer.bi:u-e est:-', 3,
  "Aeneae (dative) is Ae-nē-ae, three syllables (initial diphthong one syllable, ē long), as at 12.311, and manum elides into it: Stāt cōn | fēr-rĕ mă | n(um) Ae-nē | ae stāt | quīd-quĭd ă | cērb(i) ēst (14 syllables), manum and acerbi elided, caesura after Aeneae. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 15."),
 '680': ('am.pli.us:-uu Hunc:- o.ro:-- si.ne:uu me:- fu.re.re:uue an.te:-u fu.ro.rem:u--', 2,
  "ōrō has both syllables long (ōro, from ōs), sĭnĕ (imperative of sĭno) both short, mē long and fŭrĕrĕ three shorts, its last elided: ām-plĭ-ŭs | hūnc ō | rō sĭ-nĕ | mē fŭ-rĕ | r(e) ān-tĕ fŭ | rō-rem (16 syllables), caesura after oro. The scanner (cost 0.6, not flagged) shortened o-ro and me and lengthened si- and fu-re-, a false fit with the same count."),
 '686': ('pro.lu.it:-uu aut:- an.nis:-- sol.vit:-- sub.lap.sa:--u ve.tus.tas:u--', 2,
  "Same feet and quantities as the scanner's, different syllable division (as adlapsa at 12.319, abrupto at 12.451, sublatis at 12.26): sublapsa is sub + lapsa, sub-lāp-sa with sub long by position, not an open long su- (su-blap), which the audio would read as a long vowel: prō-lŭ-ĭt | aūt ān | nīs sōl | vīt sūb | lāp-să vĕ | tūs-tas (14 syllables), caesura after annis."),
 '687': ('fer.tur:-u in:u ab.rup.tum:--- mag.no:-- mons:- im.pro.bus:-uu ac.tu:--', 2,
  "Same feet and quantities as the scanner's, different syllable division (as abrupto at 12.451): abruptum is ab + ruptum, ab-rūp-tum with ab long by position, not an open long a- (a-brup), which the audio would read as a long vowel: fēr-tŭr ĭn | āb-rūp | tūm māg | nō mōns | īm-prŏ-bŭs | āc-tu (14 syllables), caesura after abruptum."),
 '689': ('in.vol.vens:--- se.cum:-- dis.iec.ta:--u per:u ag.mi.na:-uu Tur.nus:--', 1,
  "disiecta (dis + iacio) has the i consonantal after the prefix, dis-iec-ta, both first syllables long by position (as disiecit, conventions): īn-vōl | vēns sē | cūm dīs | iēc-tă pĕr | āg-mĭ-nă | Tūr-nus (14 syllables), caesura after secum. The scanner (cost 0.0, not flagged) read di-si-ec-ta with a vowel i, a fit with 15."),
 '697': ('At:- pa.ter:uu Ae.ne.as:--- au.di.to:--- no.mi.ne:-uu Tur.ni:--', 2,
  "Aeneas is Ae-nē-ās, three syllables (initial diphthong one syllable, ē long), as at 12.311: Āt pă-tĕr | Ae-nē | ās aū | dī-tō | nō-mĭ-nĕ | Tūr-ni (14 syllables), caesura after Aeneas. The scanner (cost 1.2, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 15."),
 '704': ('Iam:- ve.ro:-e et:- Ru.tu.li:uu- cer.ta.tim:--e et:- Tro.es:-u et:u om.nes:--', 3,
  "Confirmed by hand, entered only to clear the COSTLY flag (as 9.811): Iām vē | r(o) ēt Rŭ-tŭ | lī cēr | tāt(im) ēt | Trō-ĕs ĕt | ōm-nes (14 syllables), vero and certatim elided, caesura after Rutuli. Troes is two syllables (Greek nominative plural, -ĕs short before et), as the scanner reads it; the scanner's parse (COSTLY 2.2) is right."),
 '709': ('in.ter:-- se:- co.i.is.se:uu-u vi.ros:u- et:- cer.ne.re:-uu fer.ro:--', 3,
  "coiisse (perfect infinitive of coeo) is four syllables, cŏ-ĭ-īs-se, the first i a vowel (from eo, ii), not a consonant: īn-tēr | sē cŏ-ĭ | īs-sĕ vĭ | rōs ēt | cēr-nĕ-rĕ | fēr-ro (15 syllables), caesura after viros. The scanner (cost 0.6, not flagged) ran co-iis-se into three syllables with a long co-, a fit with 14."),
 '711': ('pro.cur.su:--- ra.pi.do:uu- con.iec.tis:--- e.mi.nus:-uu has.tis:--', 1,
  "coniectis (con + iacio) has the i consonantal after the prefix, con-iec-tis, all three syllables long: prō-cūr | sū ră-pĭ | dō cōn | iēc-tīs | ē-mĭ-nŭs | hās-tis (14 syllables), caesura after rapido. The scanner (cost 0.0, not flagged) read co-ni-ec-tis with a vowel i, a fit with 15."),
 '723': ('non:- a.li.tur:uu- Tros:- Ae.ne.as:--- et:- Dau.ni.us:-uu he.ros:--', 3,
  "Scanned as printed (alitur, a misprint for aliter; both are ă-lĭ-, and the last syllable is long by position before Tr- either way). Aeneas is Ae-nē-ās, three syllables (initial diphthong one syllable), and Tros one: nōn ă-lĭ | tūr Trōs | Ae-nē | ās ēt | Daū-nĭ-ŭs | hē-rōs (14 syllables), caesura after Aeneas. The scanner (cost 1.5, not flagged) split Ae- in two and read A-e-ne as a dactyl, a fit with 15."),
 '729': ('al.te:-- sub.la.tum:--- con.sur.git:--- Tur.nus:-u in:u en.sem:--', 1,
  "Same feet and quantities as the scanner's, different syllable division (as sublatis at 12.26 and abrupto at 12.451): sublatum is sub-lā-tum with sub long by position, not an open long su- (su-bla), which the audio would read as a long vowel: āl-tē | sūb-lā | tūm cōn | sūr-gīt | Tūr-nŭs ĭn | ēn-sem (13 syllables), caesura after sublatum."),
 '730': ('et:- fe.rit:uu ex.cla.mant:--- Tro.es:-- tre.pi.di.que:uu-u La.ti.ni:u--', 2,
  "Trōēs is two syllables (Greek nominative plural, as 1.524 and 9.689), its -es long by position before tr-, and trĕpĭdi has two short syllables: ēt fĕ-rĭt | ēx-clā | mānt Trō | ēs trĕ-pĭ | dī-quĕ Lă | tī-ni (15 syllables), caesura after exclamant. The scanner (cost 0.0, not flagged) ran Troes into one syllable and made tre-pi long-long, a fit with 14."),
 '744': ('un.di.que:-ue e.nim:u- den.sa:-- Teu.cri:-e in.clu.se.re:---u co.ro.na:u--', 2,
  "Teucri is two syllables, Teu-crī, the Greek diphthong eu (as Teucros at 12.506), its -i elided into inclusere; ĕnĭm has its -nim long by position before d-, and densā is the long ablative: ūn-dĭ-qu(e) ĕ | nīm dēn | sā Teū | cr(i) īn-clū | sē-rĕ cŏ | rō-na (14 syllables), undique elided, caesura after densa. The scanner (cost 0.0, not flagged) split Te-u into two short syllables, a fit with 15."),
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
