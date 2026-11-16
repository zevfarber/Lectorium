#!/usr/bin/env python3
"""Reviewer's edits to aeneid-091 units.json (passes 1 and 2; run once from the drafter's file).
Each edit: (unit index, field, old, new); old must occur exactly once in that field. Only l, i, n and the top-level
'about' are touched; t, ln, p, v, title, titleEn and part never. Run once (it refuses if the file has already been
edited: every old string must still be present exactly once)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
before = [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U]
top = {k: D[k] for k in ('title', 'titleEn', 'part')}

E = [
 # ---------------- medium ----------------
 # M1 60 l: 'join hands with' reads as alliance in English; 'manum committere' is to engage in combat (note and i agree)
 (32, 'l', "cease to join hands with the Teucrians.", "cease to engage your hand in combat with the Teucrians."),
 # M2 46 i: 'it mounts the higher' is close to a known published rendering of 'exsuperat magis' ("it mounts the more")
 (24, 'i', "it mounts the higher and grows worse for being treated.",
           "it only surges further, and every attempt to treat it makes the sickness worse."),

 # ---------------- low: notes, elision lists ----------------
 (8, 'n', "Elisions throughout, e.g. 'quant(um) ipse', 'm(e) impensius', 'consuler(e) atque', 'metuent(em) expendere'.",
          "Elisions 'quant(um) ipse', 'virtut(e) exsuperas', 'm(e) impensius', 'aequ(um) est', 'consuler(e) atque', 'atqu(e) omnis', 'metuent(em) expendere'."),
 (20, 'n', "Elision 'Turn(o) exstincto'.", "Elisions 'Turn(o) exstincto', 's(um) adscire'."),
 # 31: hiatus genero, arma (scan-fixes 12.31)
 (14, 'n', "Elisions 'promiss(am) eripui', 'arm(a) impia'.",
           "Elisions 'promiss(am) eripui', 'arm(a) impia'; but 'genero, arma' does not elide: the long '-o' stands before the pause in hiatus, one of Virgil's rare unelided meetings of vowels."),
 # 81: rule 5b, the note opens with the print's reading (the paragraph remark moved after it)
 (45, 'n', "A new paragraph in Greenough. The print has 'recessit.' with a full stop, then lower-case 'poscit', a misprint for a comma, corrected here: 'ubi… dedit… recessit' is a clause of time whose main verb is 'poscit'. t keeps the print and the unit runs on across the stop.",
           "The print has 'recessit.' with a full stop, then lower-case 'poscit', a misprint for a comma, corrected here: 'ubi… dedit… recessit' is a clause of time whose main verb is 'poscit'. t keeps the print and the unit runs on across the stop. A new paragraph in Greenough."),
 # ---------------- low: labels and facts ----------------
 (13, 'n', "the word repeated (anaphora) by a man explaining his weakness.",
           "the word framing the line, repeated by a man explaining his weakness."),
 (1, 'n', "'ille', 'that (well-known) lion', the hunters' famous quarry.",
          "'ille', 'that lion', pointing at the beast as if it stood before us."),
 (17, 'n', "a picture of long years of war though the fighting has lasted only days.",
           "an exaggeration of how long the war has lasted."),
 (21, 'n', "the Rutulians as Latinus's kinsmen through Amata;",
           "the Rutulians as Latinus's kin, through Turnus's tie to Amata or simply as a kindred people of Latium;"),
 (47, 'n', "'umeris' is Greenough's spelling of 'humeris'.", "'umeris', also spelled 'humeris'."),
 (45, 'n', "'Pilumno', Pilumnus, an old Italian god and Turnus's ancestor.",
           "'Pilumno', Pilumnus, an old Italian god, Turnus's grandfather (X.76)."),
 (45, 'n', "horses bred of the wind.",
           "horses bred of the wind. The name is four syllables, Ō-rī-thyi-a, and makes the fifth foot a spondee, a heavy Greek close."),
 (35, 'n', "'genas' an accusative of respect (the Greek construction, common with passive participles).",
           "'genas' an accusative of respect (the Greek construction, common with passive participles); 'flagrantis', '-is' accusative plural with 'genas', 'burning'."),
 (35, 'n', "'quoi' is Greenough's old spelling of 'cui', 'to whom'",
           "'quoi' is Greenough's old spelling of 'cui', one long syllable, 'to whom'"),
 # ---------------- low: scansion pointers (scanner's fits checked by hand and kept) ----------------
 (5, 'n', "'pater', a respectful address to the old king, who is also to be his father-in-law.",
          "'pater', a respectful address to the old king, who is also to be his father-in-law; its short last syllable is lengthened on the beat before the pause."),
 (48, 'n', "'ensemque clipeumque', double '-que'.",
           "'ensemque clipeumque', double '-que', the first '-que' lengthened on the beat, a Homeric licence."),
 (36, 'n', "'alba' agrees with 'lilia'.",
           "'alba' agrees with 'lilia'. 'ebur' has its short last syllable lengthened on the beat before the pause."),

 # ---------------- low: l ----------------
 # 57-58: 'my wretched age' repeated the noun already given ('of my old age'); 'miserae' agrees with 'senectae'
 (31, 'l', "you are the rest, my wretched age;", "you are the rest, wretched as it is;"),

 # ---------------- low: i ----------------
 # 1-4, 23 (unit 45 46), 62-63, 51 etc.: precautions against phrasing remembered from published versions
 (0, 'i', "When Turnus sees the Latins broken by the war's reverses and their courage spent, sees his own promise now called in and every eye singling him out, he blazes up unbidden, past all appeasing, and his pride rises.",
          "When Turnus sees the Latins broken by defeat in battle and their spirit failing, sees his promise now called in and every eye fixed on him, he flares up of his own accord, beyond all appeasing, and his pride rises."),
 (1, 'i', "glories in tossing the shaggy mane upon his neck,", "exults as he shakes out the thick mane on his neck,"),
 (23, 'i', "Turnus's violence is not swayed by his words in the least:", "Words do nothing at all to bend Turnus's violence:"),
 (34, 'i', "I will quit this hateful daylight together with you, and never be a captive who sees Aeneas made my son-in-law.”",
           "I will leave this light I have come to hate at the same moment as you, and I will not live on as a captive to see Aeneas become my son-in-law.”"),
 (36, 'i', "or when white lilies blush with many roses set among them:", "or as white lilies glow red when many roses are mingled with them:"),
 # 69: 'came and went' is not in 'dabat ore colores'
 (37, 'i', "such were the colours that came and went in the maiden's face.", "such were the colours the maiden's face showed."),
 (41, 'i', "for Turnus is not free to put off his death.", "for it is not in Turnus's power to put off his death."),
 # 81-84: tense brought into line with the surrounding units (historic present); 'decus' is an honour, not a prize
 (45, 'i', "When he had said this and hurried back into the palace, he called for his horses and delighted to watch them snorting before his eyes, the team that Orithyia herself gave Pilumnus as a prize, fit to outshine the snow in whiteness and the winds in speed.",
           "When he has said this and hurried back into the palace, he calls for his horses and delights to watch them snorting before his eyes, the team that Orithyia herself gave Pilumnus as a mark of honour, such as to outdo the snow in whiteness and the winds in speed."),
 (47, 'i', "Then Turnus himself fastens about his shoulders a breastplate stiff with gold and pale orichalc;",
           "Next Turnus himself puts on his shoulders a breastplate rough with gold and white orichalc;"),
 (51, 'i', "Grant me to lay low the body of that Phrygian half-man, to wrench off his breastplate and tear it with a strong hand,",
           "Grant that I may bring down the body of that Phrygian half-man, rip his breastplate from him and tear it apart with a strong hand,"),
]

for k, f, old, new in E:
    s = U[k][f]
    assert s.count(old) == 1, (k, f, old[:60], s.count(old))
    U[k][f] = s.replace(old, new)

# about: Latinus asks Turnus to pity his father, not to go home
old = "begging Turnus to spare himself and go home to his old father;"
assert D['about'].count(old) == 1
D['about'] = D['about'].replace(old, "begging Turnus to spare himself and to pity his old father far away in Ardea;")

# guards
assert [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U] == before
assert {k: D[k] for k in ('title', 'titleEn', 'part')} == top
for k, u in enumerate(U):
    assert u['l'].count('\n') == u['t'].count('\n'), k
    assert '\n' not in u['i'], k
    assert 15 <= len(u['n'].split()) <= 139, (k, len(u['n'].split()))
for lay in ('t', 'l', 'i'):
    assert sum(u[lay].count('“') for u in U) == sum(u[lay].count('”') for u in U) == 6, lay
A.jdump(D, p)
print(len(E) + 1, 'edits applied')
