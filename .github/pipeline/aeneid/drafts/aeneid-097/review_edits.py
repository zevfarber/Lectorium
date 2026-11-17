#!/usr/bin/env python3
"""Reviewer's edits to aeneid-097 units.json (passes 1 and 2; run once from the drafter's file).
Each edit: (unit index, field, old, new); old must occur exactly once in that field. Only l, i, n are touched;
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
 # ---------------- medium: missing elisions ----------------
 (19, 'n', "Elision 'medi(a) agmina'.", "Elisions 'perqu(e) hostis', 'medi(a) agmina'."),
 (35, 'n', "Elision 'nemor(i) imperitet'.", "Elisions 'nemor(i) imperitet', 'tot(a) armenta'."),
 (36, 'n', "'obnix(i) infigunt'.", "'obnix(i) infigunt', 'coll(a) armosque'."),
 (39, 'n', "Elision 'fat(a) imponit'.", "Elisions 'aequat(o) examine', 'fat(a) imponit'."),

 # ---------------- medium: l mistranslates a genitive as a goal (690 urbis ad muros) ----------------
 (22, 'l', "thus to the city rushes, to the walls, where most with poured",
           "thus of the city rushes to the walls, where most with poured"),

 # ---------------- medium: i, precautionary rephrasings against remembered modern versions ----------------
 (2, 'i', "“Turnus, our last hope of safety is in you: have pity on your people.",
          "“Turnus, the last of our safety lies in you: take pity on your own."),
 (9, 'i', "and a harvest of iron bristles with drawn blades:",
          "and their drawn blades bristle like a standing crop of iron:"),
 (12, 'i', "and valour that knew its own worth.", "and the courage he knew was his."),
 (16, 'i', "where god and cruel Fortune call, let us follow.",
           "let us go where the god and harsh Fortune summon us."),
 (18, 'i', "Let me, I beg you, rage out this madness first.”",
           "I beg you, let me first rage this madness through to its end.”"),
 (27, 'i', "huge as Athos, or as Eryx, or as father Apennine himself when he roars with his quivering holm-oaks and exults in lifting his snowy crown to the sky.",
           "as vast as Athos or Eryx, or as father Apennine himself, roaring with his shimmering holm-oaks and glad to rear his snow-capped head into the air."),
 (33, 'i', "chance and courage blended into one.", "luck and valour were mixed past telling apart."),
 (38, 'i', "just so did Trojan Aeneas and the Daunian hero clash with their shields; a mighty crash filled the heavens.",
           "just so did Trojan Aeneas and the Daunian hero run together shield against shield; a vast din filled the upper air."),
 (39, 'i', "Jupiter himself held up a pair of scales with the beam level and laid in them the differing fates of the two men, to see which of them the ordeal would condemn, and which side death would weigh down.",
           "Jupiter himself lifted the two pans of his balance, the pointer set true, and placed in them the separate destinies of the two, to learn which of them the struggle would doom and to which side death's weight would drag the beam."),
 (46, 'i', "once it came up against the armour made by the god Vulcan, the mortal blade shattered at the blow like brittle ice;",
           "once it met the god's armour, Vulcan's work, the blade of mortal make burst apart at the stroke as brittle ice does;"),
 (48, 'i', "weaving aimless circles this way and that;", "winding this way and that in loops that led nowhere;"),

 # ---------------- low: l ----------------
 (1, 'l', "carried on a foaming horse, Saces, by an arrow, in front,",
          "carried on a foaming horse, Saces, in front, by an arrow,"),
 (11, 'l', "Stunned was, by the varied confused image of things,",
           "Stunned was, by the varied, confused, image of things,"),
 (34, 'l', "when two, turned into hostile battle, bulls\nwith brows charge;",
           "when two, with turned, into hostile battle, bulls\nbrows charge;"),

 # ---------------- low: notes ('framing the line' where it does not; wording) ----------------
 (9, 'n', "'with drawn points', an ablative framing the line.", "'with drawn points', an ablative round 'seges'."),
 (34, 'n', "lowered against each other, framing the line.", "lowered against each other, the noun held over to the next line."),
 (42, 'n', "'in the middle of the stroke', framing the line.", "'in the middle of the stroke', round 'ardentem deserit'."),
 (48, 'n', "'different stretches of the plain', framing the line.", "'different stretches of the plain', round 'fuga petit'."),
 (23, 'n', "both peoples named, one at each end of the line.", "both peoples named, one in each half of the line."),

 # ---------------- low: rule-5b wording (723 alitur; 727 letum; Emicat; 743 orbes) ----------------
 (38, 'n', "The print has alitur, a misprint for aliter, corrected here:",
           "The print has 'alitur', a misprint for 'aliter', corrected here:"),
 (39, 'n', "'duas… lances', 'two pans', a pair of scales, framing the line.",
           "The print has a semicolon after 'letum' (727), with 'Emicat' following in capital, a misprint for a full stop, corrected here. 'duas… lances', 'two pans', a pair of scales, round 'aequato examine'."),
 (39, 'n', " The print ends the line with a semicolon but begins 728 with a capital; it is read here as the end of a sentence.", ""),
 (48, 'n', "The print has no stop after 'orbes' (743); 'enim' begins a new clause, so l and i pause there.",
           "The print has no mark after 'orbes' (743), a misprint for a stop (a semicolon is read here), corrected here: 'enim' begins a new clause."),

 # ---------------- low: scansion glosses that go with the scan-fixes ----------------
 (2, 'n', "Elision 'Turn(e) in'.", "'suprema', su- long by position before pr. Elision 'Turn(e) in'."),
 (3, 'n', "a word that sets Aeneas beside Jupiter.", "a word that sets Aeneas beside Jupiter; 'Aeneas', Ae- one long syllable."),
 (18, 'n', "'oro', 'I pray', parenthetic.", "'oro', 'I pray', parenthetic, both syllables long."),
 (22, 'n', "the preposition after the adjective.", "the preposition after the adjective; 'disiecta' is dis-iec-ta, the i a consonant after the prefix."),
 (26, 'n', "A new paragraph in Greenough.", "A new paragraph in Greenough. 'Aeneas', Ae- one long syllable."),
 (28, 'n', "each straining to see.", "each straining to see. 'Troes', two syllables, Trō-ĕs, the Greek nominative plural."),
 (29, 'n', "perfect infinitive of 'coeo', 'come together'.", "perfect infinitive of 'coeo', 'come together', four syllables, co-i-is-se."),
 (30, 'n', "'coniectis eminus hastis', an ablative absolute,", "'coniectis eminus hastis' (con-iec-tis, the i a consonant after the prefix), an ablative absolute,"),
 (38, 'n', "'Tros', 'the Trojan', a Greek nominative.", "'Tros', 'the Trojan', a Greek nominative; 'Aeneas', Ae- one long syllable; the line scans the same with either reading."),
 (41, 'n', "'exclamant', 'shout out', at the blow.", "'exclamant', 'shout out', at the blow. 'Troes', two syllables, Trō-ēs, the -es long before 'trepidi'."),
 (48, 'n', "'densa… corona', 'with a thick ring', of men.", "'densa… corona', 'with a thick ring', of men; 'Teucri', two syllables, Teu-crī."),
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
