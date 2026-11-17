#!/usr/bin/env python3
"""Reviewer's edits to aeneid-096 units.json (passes 1 and 2; run once from the drafter's file).
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
 # ---------------- medium: elision lists ----------------
 # 'haec' ends in -c: 'haec in' is not an elision
 (41, 'n', "Elisions 'dud(um) adgnovi', 'tequ(e) haec', 'ha(ec) in'.",
           "Elisions 'dud(um) adgnovi', 'tequ(e) haec'; 'haec in' does not elide, since 'haec' ends in a consonant."),
 # missing elisions
 (0, 'n', "Elision 'urbiqu(e) adverteret'.", "Elisions 'ment(em) Aeneae', 'urbiqu(e) adverteret'."),
 (1, 'n', "Elisions 'atqu(e) huc',", "Elisions 'Ill(e) ut', 'atqu(e) huc',"),
 (22, 'n', "'trabe… ab alta', 'from a high beam'. No elisions.",
           "'trabe… ab alta', 'from a high beam'. Elision 'nod(um) informis'."),
 (28, 'n', "Elisions 'Dardani(um) Aenean',", "Elisions 's(e) incusat', 'Dardani(um) Aenean',"),
 (28, 'n', "Greek accusative 'Aenean'.", "Greek accusative 'Aenean', Ae- one long syllable."),
 (44, 'n', "He casts about and finds none. No elisions.",
           "He casts about and finds none. Elision 'ag(o) aut', across the question mark into the next sentence."),
 (46, 'n', "Elisions 'ant(e) ipse',", "Elisions 'Vid(i) oculos', 'ant(e) ipse',"),

 # ---------------- medium: 631 half-line is a foot and a half, not two and a half feet ----------------
 (40, 'n', "two and a half feet, and the line breaks off.",
           "a foot and a half, Tūr-nŭs ăd | haec, and the line breaks off."),

 # ---------------- medium: i, possible echoes of modern versions ----------------
 (46, 'i', "calling out to me by name, go down to his death, a giant overcome by a giant's wound.",
           "crying out to me, go down to his death, a huge man felled by a wound as huge."),
 (51, 'i', "Is death so very hard a thing?", "Is dying, then, so utterly wretched?"),
 (52, 'i', "Shades of the dead, be kind to me, since the gods above have turned their favour from me!",
           "Shades below, be gracious to me, since the will of heaven is set against me!"),

 # ---------------- low: notes ----------------
 (4, 'n', "the 'tumulus' of 562, framing the line;", "the 'tumulus' of 562, framing 'medius stans';"),
 (19, 'n', "'fessis… Latinis', dative with 'accidit', 'befell the weary Latins', framing the line.",
           "'fessis… Latinis', dative with 'accidit', 'befell the weary Latins', round 'etiam fortuna'."),
 (19, 'n', "'totam… urbem', framing the second line.", "'totam… urbem', round 'luctu concussit funditus'."),
 (7, 'n', "Aeneas counting Turnus's evasions as defeat; he does not know they are Juturna's doing.",
          "Aeneas treating Turnus as a man already beaten, who keeps refusing the fight."),
 (29, 'n', "The semicolon after 'equorum' is supplied by Lectorium where the digital source dropped a mark; the lowercase 'attulit' shows Greenough did not print a full stop.",
           "The semicolon after 'equorum' was added to Lectorium's source under the pipeline's rule for missing punctuation: the Perseus text drops the mark here, and the lowercase 'attulit' shows that Greenough's sentence runs on."),
 (39, 'n', "'pugnae', with 'recedes', 'you will retire from the fight', a dative where prose would have 'ex pugna'.",
           "'pugnae' is usually taken with 'recedes', 'you will retire from the fight', a dative where prose would have 'ex pugna'; some take it with 'numero', 'in the tally of the fight'."),
 (41, 'l', "“O sister, both long since I knew you, when first by craft",
           "“O sister, both long since I recognised you, when first by craft"),
 (41, 'i', "“Sister, I knew you long ago,", "“Sister, I saw through you long ago,"),
 (13, 'n', "'Italos hostis', 'that the Italians are enemies',",
           "'Italos hostis', 'that the Italians are enemies', 'Ĭtalos' with a short I, as often in Virgil (the long vowel belongs to 'Ītalia'),"),
 (37, 'n', "'Aeneas', Ae- one long syllable.", "'Aeneas', Ae- one long syllable; 'Italis', short I again, as at 582."),
 (34, 'n', "'Atque huic', 'and to him',", "'Atque huic', 'and to him', 'huic' one syllable,"),
 (53, 'n', "'iste' with a note of contempt.", "'iste' with a note of contempt; 'istius' is is-tī-us, three syllables, the ī long."),
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
