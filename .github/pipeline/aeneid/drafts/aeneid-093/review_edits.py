#!/usr/bin/env python3
"""Reviewer's edits to aeneid-093 units.json (passes 1 and 2; run once from the drafter's file).
Each edit: (unit index, field, old, new); old must occur exactly once in that field. Only l, i and n are touched;
t, ln, p, v, title, titleEn, part and about never. Run once (it refuses if the file has already been edited:
every old string must still be present exactly once)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
before = [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U]
top = {k: D[k] for k in ('title', 'titleEn', 'part', 'about')}

E = [
 # ---------------- medium: Itali/Italas have a short I- (the scanner is right; 3.440, 5.703, 9.133) ----------------
 (14, 'n', "'Italas' has its first syllable lengthened, as 'Italia' does in verse.",
           "'Italas' has a short first syllable, I-ta-las (only 'Italia' lengthens its I- in verse)."),
 (16, 'n', "'Itali', with its first syllable long in verse, Ī-ta-li.",
           "'Itali', with a short first syllable, I-ta-li, as at 246."),
 (38, 'n', "'Itali', with the first syllable long, as at 251.",
           "'Itali', with a short first syllable, as at 251."),

 # ---------------- low: notes ----------------
 # 219: the prefix keeps its d: ad-ju-vat
 (2, 'n', "a-dju-vat, the first syllable long.", "ad-ju-vat, the first syllable long by position."),
 # 225: 10.563-564 'ditissimus agri qui fuit' need not be Volcens; say only what is certain
 (4, 'n', "Camers appears at 10.562–563 as the son of great-hearted Volcens, the richest landowner of the Ausonians.",
          "Camers appears at 10.562–564, 'magnanimo Volcente satum', son of great-hearted Volcens."),
 # 241: Qui picks up the Laurentines and Latins of 240; requies pugnae is an objective genitive
 (13, 'n', "'Qui', 'those who', the antecedent left out.",
           "'Qui', 'they who', a connecting relative: the Laurentines and Latins just named."),
 (13, 'n', "'pugnae' a genitive of separation, 'rest from'.", "'pugnae' an objective genitive, 'rest from'."),
 # 247: scansion pointer (scan-fix 12.247)
 (15, 'n', "'aethra' a Greek word for the bright sky.",
           "'aethra' a Greek word for the bright sky; 'rubra' is ablative with it, its -a long."),
 # 259: 6.46 and 11.464 have 'ait', not 'inquit'
 (19, 'n', "breaking into the speech, as at 6.46 and 11.464.", "breaking into the speech, as 'ait' does at 6.46 and 11.464."),
 # 278: the comma cannot be checked against Greenough's page; it is kept as printed
 (28, 'n', "Greenough's comma after the first 'pars' is not needed for the sense,",
           "The comma printed after the first 'pars', kept here, is not needed for the sense,"),
 # 280: Laurentum is the consonant-stem genitive, not the old -um for -orum; Troes pointer (scan-fix 12.281)
 (29, 'n', "'Laurentum' the old '-um' genitive plural.", "'Laurentum' the genitive plural of 'Laurens', '-um' for '-ium'."),
 (29, 'n', "'densi', 'massed'.", "'densi', 'massed'. 'Troes', two syllables, as at 231."),
 # 285: keep 118's focos as 092's review left it (hearths, not portable braziers)
 (31, 'n', "'focos', the braziers set up at 118.", "'focos', the hearths for the sacrificial fire set up at 118."),
 (31, 'i', "the mixing-bowls and the fire-pans.", "the mixing-bowls and the hearths."),
 # 288: syllable division
 (33, 'n', "su-bji-ci-unt.", "sub-ji-ci-unt."),
 # 294: telo ... trabali frames 'orantem multa', not the whole line (Messapus stands first)
 (36, 'n', "'with a weapon like a beam', framing the line;", "'with a weapon like a beam', framing 'orantem multa';"),
 # 298: at 6.228 Corynaeus gathers the bones into an urn
 (39, 'n', "and one buries Misenus at 6.228:", "and one gathers Misenus's bones into an urn at 6.228:"),
 # 304: sic rigido latus ense ferit is five words
 (42, 'n', "told in four plain words", "told in five plain words"),
 # 309-310: conduntur is not 'are closed' (the note itself sets it against 10.746 clauduntur); quies pointer;
 # i brought into line with the published 10.745-746 and out of 'eyes ... eyes'
 (45, 'l', "sleep; into eternal are closed his lights, night.", "sleep; into eternal are laid away his lights, night."),
 (45, 'n', "'ferreus', three syllables, fer-re-us.", "'ferreus', three syllables, fer-re-us; 'quies', two, qui-es."),
 (45, 'i', "A hard rest, an iron sleep, weighs down his eyes; his eyes are shut in everlasting night.",
           "A hard stillness, an iron sleep, pressed on his eyes, and their light was laid away in a night without end."),

 # ---------------- low: i (tense kept past through the narrative; one stiff phrase; one precaution) ----------------
 (0, 'i', "the fight had long been seeming unequal", "the fight had long seemed unequal"),
 (1, 'i', "as they see more closely that the two do not meet on equal strength.",
          "as they saw more closely that the two did not meet on equal strength."),
 (2, 'i', "Turnus himself adds to the feeling,", "Turnus himself added to the feeling,"),
 (2, 'i', "and so do his wasted cheeks", "and so did his wasted cheeks"),
 (4, 'i', "she plunges, knowing well what she is about, sowing rumours of every kind, and speaks these words:",
          "she plunged, knowing well what she was about, sowing rumours of every kind, and spoke these words:"),
 (13, 'i', "Men who had been hoping that they would now have rest from fighting and safety for their fortunes now want arms, pray that the treaty may be undone, and pity Turnus for his unfair lot.",
           "They, who had been hoping that they would now have rest from fighting and safety for their fortunes, now wanted arms, prayed that the treaty might be undone, and pitied Turnus for his unfair lot."),
 (14, 'i', "To this Juturna adds something greater still, and gives a sign from high heaven; none ever did more to confound Italian minds or deceived them more with its marvel.",
           "To this Juturna added something greater still, and gave a sign from high heaven; no sign ever threw Italian minds into deeper confusion, or deceived them more surely with its marvel."),
 (24, 'i', "the cornel shaft whistles as it flies, and cuts the air unerringly.",
           "the cornel shaft whistled as it flew, and cut the air unerringly."),
 (20, 'i', "poor people,", "you wretched men,"),
 # precaution against stock phrasing ('live on men's lips')
 (9, 'i', "and his name will live on men's lips:", "and pass, a living man, from mouth to mouth:"),
]

for k, f, old, new in E:
    s = U[k][f]
    assert s.count(old) == 1, (k, f, old[:60], s.count(old))
    U[k][f] = s.replace(old, new)

# guards
assert [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U] == before
assert {k: D[k] for k in ('title', 'titleEn', 'part', 'about')} == top
for k, u in enumerate(U):
    assert u['l'].count('\n') == u['t'].count('\n'), k
    assert '\n' not in u['i'], k
    assert 15 <= len(u['n'].split()) <= 139, (k, len(u['n'].split()))
A.jdump(D, p)
print(len(E), 'edits applied')
