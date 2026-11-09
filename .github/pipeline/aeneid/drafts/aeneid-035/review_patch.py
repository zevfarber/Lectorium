#!/usr/bin/env python3
"""Reviewer's patch for aeneid-035 (passes 1 and 2). Edits l / i / n of units.json by exact-substring
replacement; never touches t. Run after make_units.py (which regenerates units.json from its own text).
Also adds the hand scansions to ../../scan-fixes.json (idempotent)."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(HERE, 'units.json')
D = json.load(open(P, encoding='utf8')); S = D['sentences']; log = []
T0 = [u['t'] for u in S]
def rep(idx, field, old, new):
    s = S[idx][field]
    if s.count(old) != 1: sys.exit(f'unit {idx} {field}: {old[:60]!r} occurs {s.count(old)} times')
    S[idx][field] = s.replace(old, new); log.append((idx, field))

# ---- U0 (387-388)
rep(0,'n',"'Viridante toro… herbae': 'viridante' is a present participle ('viridare', 'to grow green'), agreeing with 'toro', and 'herbae' is a genitive of definition, 'a couch made of grass', an ablative of place, 'on the greening grass-couch'.",
 "'Viridante toro… herbae': 'toro' is an ablative of place, 'on the couch'; 'viridante' is a present participle ('viridare', 'to grow green') agreeing with it; and 'herbae' is a genitive of material, 'a couch of grass', so 'on the greening grass-couch'.")
# ---- U1 (389-391)
rep(1,'n',"'Heroum' is an old genitive plural in -um (you'll see this constantly), partitive after the superlative 'fortissime', 'bravest of heroes';",
 "'Heroum' is the genitive plural of 'heros' (the ordinary form of this word, not the old '-um' for '-orum' of 'superum' or 'divom'), partitive after the superlative 'fortissime', 'bravest of heroes';")
# ---- U2
rep(2,'n',"Eryx was a Sicilian king, a son of Venus (so a half-brother of Aeneas), killed by Hercules in a bout at the foot of the mountain that bears his name; here he is called a god, as a hero honoured after death.",
 "Eryx was a Sicilian king and a son of Venus (so a half-brother of Aeneas); Entellus tells at 410–414 how he fought Hercules. Here he is called a god, presumably as a son of Venus honoured on the mountain that bears his name (the text does not say).")
# ---- U7
rep(7,'n',"'Iuventas' is Virgil's form of 'iuventa'.","'Iuventas' is the abstract noun 'youth', a by-form of 'iuventa' (the word used at 430).")
# ---- U8 (399-400): condition label; rule 5b note
rep(8,'n',"(a mixed condition, 'if I were as I was, I would then not have come')","(a mixed condition: 'if I now had that youth (as I once had it), I would not have come forward')")
rep(8,'n',"This is the main clause of the condition:","The print has 'moror. ”Sic', the closing mark of the speech set after the full stop and joined to the next word, a misprint for 'moror.” Sic' (as it stands it looks like a new opening). t keeps the print, because t must match the pinned source; l and i close the speech after 'moror.', where the sense ends it. This is the main clause of the condition:")
rep(8,'n'," Misprint: Greenough prints the closing mark of the speech after the full stop and attached to the next word (moror. ”Sic), so the speech seems to open again; the sense is that the speech ends at 'moror.', and 'Sic deinde locutus' is narrative. t keeps the print as it stands, and the closing mark in l and i sits after 'moror.'"," 'Sic deinde locutus' is narrative.")
# ---- U9
rep(9,'n',"'Locutus' is the perfect participle","The mark ” before 'Sic' is the misprinted closing mark of the speech that ended at 'moror.' (see the note on the previous unit). 'Locutus' is the perfect participle")
# ---- U11 (404-405): l keeps the hyperbaton septem / terga boum
rep(11,'l',"of so great oxen the huge seven\nhides, with lead sewn in and iron, were stiff.","of so great the huge seven\nhides of oxen, with lead sewn in and iron, were stiff.")
# ---- U12
rep(12,'n'," Greenough prints 'omnes', 'all'; the Latin Library has the same word in another form ('omnis')."," ")
S[12]['n'] = S[12]['n'].rstrip()
# ---- U26
rep(26,'n'," (Greenough's spelling; the usual 'bracchia')","")
# ---- U33 (439-442)
rep(33,'n',"'Sedet… circum' is 'sits round', that is, besieges ('circum' set after its noun); 'montana castella' is 'hill-forts', 'sub armis' 'under arms'.",
 "'Sedet… circum castella' is 'sits round the forts', that is, besieges ('circum' is the preposition with 'castella'; the adjective 'montana' stands before the verb, apart from its noun); 'montana castella' is 'hill-forts', 'sub armis' 'under arms'.")
# ---- U36
rep(36,'i',"Entellus spent his strength upon the wind and then, heavy as he was,","Entellus flung his strength away on empty air and then, heavy as he was,")
# ---- U45
rep(45,'n',", 'te' being understood.",".")
# ---- U46
rep(46,'n'," Greenough's 'vires' (the Latin Library prints the other spelling 'uiris') is the same word; there is no change of sense.","")
# ---- U47 (467): echo; rule 5b note
rep(47,'i',"Yield to a god.”","Give way before a god.”")
rep(47,'n',"'Cede' is the imperative of 'cedo'","The print has 'deo. ”Dixitque', the closing mark after the full stop and joined to the next word, a misprint for 'deo.” Dixitque' (as it stands it looks like a new opening). t keeps the print, because t must match the pinned source; l and i close the speech after 'deo.'. 'Cede' is the imperative of 'cedo'")
rep(47,'n'," Misprint: as at 400, Greenough prints the closing mark after the full stop and attached to the next word (deo. ”Dixitque), so it seems to open a fresh speech. The speech ends at 'deo.'; t keeps the print as it stands, and the closing mark in l and i sits here.","")
# ---- U48
rep(48,'n',"'Dixitque' is narrative","The mark ” before 'Dixitque' is the misprinted closing mark of Aeneas's speech (see the note on the previous unit). 'Dixitque' is narrative")
# ---- U49
rep(49,'n'," Greenough's 'naves' (Latin Library 'nauis') is the same word.","")
# ---- U50
rep(50,'n',"the comrades being summoned to receive the loser's consolation gifts;","the comrades being summoned (the text does not say by whom) to receive what are evidently the loser's consolation gifts;")
# ---- U52
rep(52,'n',"'Hic' is an adverb, 'here', 'at this point'.","'Hic' is most simply an adverb, 'here', 'at this point' (it could also be the pronoun, 'this man, the victor').")
# ---- U53
rep(53,'n',"without any mark in the print around it (the print has no mark there; the sense runs on)","the print gives it no commas, and the speech runs straight on")
# ---- U54 (477-480)
rep(54,'l',"He spoke, and opposite stood the face of the bullock facing him,\nwhich stood by, the gift for the fight, and the hard, drawn back,\nhe poised, with his right hand, between the middle horns, the gloves,",
 "He spoke, and opposite he stood the face of the bullock facing him,\nwhich stood by, the gift for the fight, and the hard\nhe poised, with right hand drawn back, between the middle horns, the gloves,")
rep(54,'i',"then, rising to his full height, he dashed","then, standing tall, he dashed")
rep(54,'n',"and 'media inter cornua' is 'between the horns', 'inter' set after its noun.","and 'media inter cornua' is 'between the middle horns', with 'inter' placed between its adjective and its noun.")
rep(54,'n'," Greenough's 'adstabat' (Latin Library 'astabat') is the same word.","")
# ---- U55 (481)
rep(55,'n',"'Sternitur' is the present passive","The print has 'sternitur' with a small letter after the full stop at the end of 480, a misprint for 'Sternitur'; t keeps the print, because t must match the pinned source. 'Sternitur' is the present passive")
rep(55,'n'," Misprint: Greenough prints 'sternitur' with a small letter after the full stop at the end of 480, where a capital is expected; t keeps the print as it stands.","")
# ---- U57 (483)
rep(57,'i',"“Eryx, in place of Dares's death I pay you this better life in full;","“Eryx, for the death of Dares I pay you this life, a worthier one, in full;")
# ---- U58 (484)
rep(58,'i',"here, a victor, I lay down my gloves and my art.”","and here, as victor, I put by my gloves and my craft.”")

assert [u['t'] for u in S] == T0, 't changed'
for i, u in enumerate(S):
    assert u['t'].count('\n') == u['l'].count('\n'), f'unit {i}: l line count'
json.dump(D, open(P, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print(len(log), 'text edits applied; t untouched')

# ---- scansion: hand fits that override the shared scanner (scan-fixes.json)
FX = os.path.abspath(os.path.join(HERE, '..', '..', 'scan-fixes.json'))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
fx = json.load(open(FX, encoding='utf8'))
NEW = {
 "5.410": (["1Quid–","si–","2quis–","caes–3tus–","ip–4si–us⏑","et⏑","5Her–cu⏑lis⏑","6ar–ma×"],
  "Ipsius with its -sī- long, three syllables (genitive in -īus): Quid sī | quis caes | tus ip | sī-us et | Her-cu-lis | ar-ma (14 syllables, two dactyls). The scanner (cost 2.6) took 'sius' as one syllable and then needed et- long before Her-, but h does not make position, so et is short; the dactyl sī-ŭs ĕt is the fit."),
 "5.417": (["1Sed–","si–","2nos–tra⏑","Da⏑3res–‖","haec–","4Tro–i⏑us⏑","5ar–ma⏑","re⏑6cu–sat×"],
  "Troius is three syllables, Trō-ĭ-ŭs, as in the published aeneid-007: Sed sī | nos-tră Dă | rēs haec | Trō-ĭ-ŭs | ar-mă rĕ | cū-sat (15 syllables, three dactyls). The scanner (cost 0.8) made it Tro-ius with a long 'ius' before a vowel, which nothing allows."),
 "5.418": (["1id–que⏑","pi⏑2o–","se⏑det⏑","3Ae–ne–4ae–","pro⏑bat⏑","5auc–tor⏑","A⏑6ces–tes×"],
  "Aeneae is Ae-nē-ae, three syllables, with Ae- a diphthong and no elision (pĭō does not elide before the long Ae-): Id-quĕ pĭ | ō sĕ-dĕt | Aē-nē | ae prŏ-băt | auc-tŏr Ă | cēs-tēs (16 syllables, four dactyls). The scanner (cost 1.2) split Ae- in two (A-e-ne-ae), as at 5.282, 5.286."),
 "5.422": (["1et–","mag–2nos–","mem–3bro–rum","ar–4tus–","mag–na","5os–sa⏑","la⏑6cer–tos×que"],
  "Hypermetric line (Virgil's -que elided into the exuit that opens 423): et mag | nos mem | bro(rum) ar | tus mag(na) | os-sa la | cer-tos (que). Thirteen metrical syllables, one dactyl (os-sa-la); the final -que is not counted and is left unmarked (elided into 'exuit'), the end mark × on tos. The scanner returns UNRESOLVED because it has no hypermetric option."),
 "5.432": (["1gen–ua⏑","la⏑2bant–","vas–3tos–","qua⏑tit⏑","4ae–ger⏑","an⏑5he–li⏑tus⏑","6ar–tus×"],
  "Genua has consonantal u (gen-wa), two syllables, the first long by position: gen-wa lă | bant vas | tos quă-tĭt | ae-gĕr ăn | hē-lĭ-tŭs | ar-tūs (16 syllables, four dactyls). The scanner returns UNRESOLVED because it reads ge-nu-a with a short first syllable. (An-hē-li-tus has its first syllable short: n+h is one consonant.)"),
 "5.450": (["1Con–sur–2gunt–","stu⏑di⏑3is–‖","Teu–cri","4et–","Tri–5na–cri⏑a⏑","6pu–bes×"],
  "Teu- is one long syllable (Greek eu), as at 5.293 and 3.352; -cri elides into et: Con-sur | gunt stŭ-dĭ | is Teu | (cr)et Tri | nā-crĭ-ă | pū-bes (14 syllables, two dactyls; Trinacria with na- long before cr-, as in aeneid-022). The scanner (cost 0.0, so not flagged) split Teucri into Te-u-cri and made it 15."),
 "5.461": (["1Tum–","pa⏑ter⏑","2Ae–ne–3as–‖","pro–4ce–de⏑re⏑","5lon–gi⏑us⏑","6i–ras×"],
  "Aeneas is three syllables, Ae-nē-ās: Tum pă-tĕr | Aē-nē | ās prō | cē-dĕ-rĕ | lon-gĭ-ŭs | ī-ras (15 syllables, three dactyls). The scanner (cost 1.2) split Ae- in two (A-e-ne-as) and made it 16, as at 5.282, 5.286."),
}
src = {l['n']: l['t'] for l in A.lines_of(A.part('aeneid-035'))}
strip = lambda s: re.sub(r'[0-9–⏑×‖]', '', s)
for k, (sc, why) in NEW.items():
    ln = int(k.split('.')[1]); words = A.WORD_RE.findall(src[ln])
    assert [strip(x) for x in sc] == words, (k, [strip(x) for x in sc], words)
    seg = ' '.join(sc); body = re.sub(r'[^0-9–⏑×]', '', seg); fp = re.findall(r'\d([–⏑×]+)', body)
    syl = len(re.findall(r'[–⏑×]', seg))
    assert re.findall(r'[1-6]', seg) == list('123456') and 12 <= syl <= 17 and seg.count('×') == 1, (k, fp, syl)
    assert all(f in ('–⏑⏑', '––') for f in fp[:5]) and fp[5] in ('–×', '⏑×'), (k, fp)
    fx[k] = {"sc": sc, "why": why}
open(FX, 'w', encoding='utf8').write(json.dumps(fx, ensure_ascii=False, indent=1))
print(len(NEW), 'scan-fixes entries written')
