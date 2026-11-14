#!/usr/bin/env python3
"""Reviewer helper (aeneid-074): append hand scansions for X.185-275 to scan-fixes.json, in line order after
the last existing key; keys are f"{book}.{label or n}" as build_aeneid.py and validate_aeneid.py make them. Checks each entry against the build's word-match rule and the
validator's metre rule (half-line rule when the why starts 'Half-line'). Dry run unless --write."""
import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
import scan_latin as SL
FP = os.path.join(A.HERE, 'scan-fixes.json')
raw = open(FP, encoding='utf8').read(); fx = json.loads(raw)
assert json.dumps(fx, ensure_ascii=False, indent=1) + '\n' == raw
P = A.part('aeneid-074'); LL = A.lines_of(P)
L = {str(l.get('label', l['n'])): l['t'] for l in LL}
order = [str(l.get('label', l['n'])) for l in LL]
own = lambda n: SL.scan_line(L[n])[1]
EU = "has Greek eu as one long syllable"
NEW = {
 '189': (['1Nam–que⏑', 'fe⏑2runt–', 'luc–3tu–‖', 'Cyc–4num–', 'Pha⏑e⏑5thon–tis⏑', 'a⏑6ma–ti×'],
  "Phaethontis is Pha-e-thon-tis, four syllables (Greek Φαέθων; Lewis & Short Phăĕthōn), as at 5.105, not Phae-thon-tis with ae a diphthong: Nam-quĕ fĕ | rūnt lūc | tū Cyc | num Phă-ĕ | thon-tĭs ă | mā-ti (15 syllables). The scanner's fit (cost 0.0, not flagged) read ae as a diphthong and gave the line fourteen syllables; the metre allows both, the word does not."),
 '217': (['1Ae–ne–2as–', 'ne⏑que', 'e⏑3nim–‖', 'mem–4bris–', 'dat–', '5cu–ra⏑', 'qui⏑6e–tem×'],
  "Aenēās: Ae- is one long syllable, and neque is elided before enim: Ae-nē | ās nĕ-qu(e) ĕ | nim mem | bris dat | cū-ră quĭ | ē-tem (14 syllables). The scanner (COSTLY 2.2, flagged) split the initial diphthong into A-e, a fit with 15."),
 '225': (['1qua–rum–', '2quae–', 'fan–3di–‖', 'doc–4tis–si⏑ma⏑', '5Cy–mo⏑do⏑6ce–a×'],
  "Cymodocea (Greek Κυμοδόκεια, from κῦμα) is Cȳ-mŏ-dŏ-cē-a, five syllables, with the same quantities as Cymodoceque at 5.826; doctissimă is nominative, its -a short: quā-rum | quae fan | dī doc | tis-sĭ-mă | Cȳ-mŏ-dŏ | cē-a (14 syllables). The scanner (COSTLY 1.5, not flagged) lengthened -si- and -ma, shortened Cy-, and ran -cea into one syllable."),
 '228': (['1tum–', 'sic–', '2ig–na–rum', '3ad–lo⏑qui⏑4tur–‖', 'Vi⏑gi⏑5las–ne⏑', 'de⏑6um–', 'gens×'],
  "Wrong quantities with the right count (cost 0.3, not flagged). ignārum has a long a (in- + gnarus), and adlŏquĭtur short -lo-qui- (loquor): tum sīc | ig-nā | r(um) ad-lŏ-quĭ | tur Vĭ-gĭ | lās-nĕ dĕ | um gens (15 syllables). The scanner made igna- long-short and -loqui- long-long."),
 '229': (['1Ae–ne–2a–', 'Vi⏑gi⏑la', '3et–‖', 've–4lis–', 'im–5mit–te⏑', 'ru⏑6den–tis×'],
  "Wrong quantities with the right count (no flag). Aenēā, Greek vocative (Αἰνεία), has Ae- one syllable and long -nē- and -ā (as Quid miserum, Aenea, laceras, 3.41): Ae-nē | ā Vĭ-gĭ | l(a) et vē | līs im | mit-tĕ rŭ | den-tis (14 syllables), caesura after et. The scanner made -ne-a short-short and Vi-gi- long-long."),
 '253': (['1tur–ri⏑ge⏑2rae–que', 'ur–3bis–‖', 'bi⏑iu⏑4gi–que', 'ad–', '5fre–na⏑', 'le⏑6o–nes×'],
  "biiugi is bĭ-jŭ-gī, the second i consonantal and bi- short, as at 5.144; frēna has a long e, and leōnes is three syllables: tur-rĭ-gĕ | raequ(e) ur | bīs bĭ-jŭ | gīqu(e) ad | frē-nă lĕ | ō-nes (15 syllables); urbis and urbes scan alike. The scanner (COSTLY 1.5, not flagged) lengthened bi- and iu-, shortened fre-, and ran leo- into one syllable."),
 '260': (['1Iam–que', 'in–', '2cons–pec–3tu–‖', 'Teu–4cros–', 'ha⏑bet⏑', '5et–', 'su⏑a⏑', '6cas–tra×'],
  "Teucros " + EU + ": Iam-qu(e) in | cōn-spec | tū Teu | crōs hă-bĕt | ēt sŭ-ă | cas-tra (14 syllables). The scanner (cost 0.0, not flagged) split eu into Te-u, a fit with 15."),
 '263': (['1Dar–da⏑ni⏑dae', '2e–', 'mu–3ris–‖', 'spes–', '4ad–di⏑ta⏑', '5sus–ci⏑tat⏑', '6i–ras×'],
  "Wrong quantities with the right count (no flag). Dardanidae has short -da-ni- (Dardanus), the -ae elided before the preposition ē, and mūris is long: Dar-dă-nĭ | d(ae) ē mū | rīs spēs | ad-dĭ-tă | sus-cĭ-tăt | ī-ras (15 syllables). The scanner made Dar-da-ni- long-long-long and e mu- short-short."),
}
strip = lambda s: re.sub(r'[0-9–⏑×‖]', '', s)
out = dict(fx)
for n in [x for x in order if x in NEW]:
    sc, why = NEW[n]
    if sc is None: sc = own(n)
    k = f"{P['book']}.{n}"; assert k not in fx, k
    assert [strip(x) for x in sc] == A.WORD_RE.findall(L[n]), (k, sc, A.WORD_RE.findall(L[n]))
    seg = ' '.join(sc); feet = re.findall(r'[1-6]', seg); syl = len(re.findall(r'[–⏑×]', seg))
    if why.startswith('Half-line'):
        assert feet == list('123456'[:len(feet)]) and 0 < len(feet) < 6 and seg.count('×') == 1, k
    else:
        body = re.sub(r'[^0-9–⏑×]', '', seg); fp = re.findall(r'\d([–⏑×]+)', body)
        assert feet == list('123456') and 12 <= syl <= 17 and seg.count('×') == 1, (k, feet, syl)
        assert all(f in ('–⏑⏑', '––') for f in fp[:5]) and fp[5] in ('–×', '⏑×'), (k, fp)
    m = re.search(r'(\d+) syllables', why); assert m and int(m.group(1)) == syl, (k, syl)
    out[k] = {'sc': sc, 'why': why}
    print(k, syl, ' '.join(sc))
assert len(out) == len(fx) + len(NEW)
if '--write' in sys.argv:
    open(FP, 'w', encoding='utf8').write(json.dumps(out, ensure_ascii=False, indent=1) + '\n'); print('written')
