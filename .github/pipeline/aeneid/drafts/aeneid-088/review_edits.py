#!/usr/bin/env python3
"""Reviewer's edits to aeneid-088 units.json (passes 1 and 2; run once from the drafter's file).
Each edit: (unit index, field, old, new); old must occur exactly once in that field. Only l, i, n are
touched; t, ln, p, v and the top-level fields never. Run once (it refuses if the file has already been
edited: every old string must still be present exactly once)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
before = [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U]
top = {k: D[k] for k in ('title', 'titleEn', 'part', 'about')}

E = [
 # ---------------- medium ----------------
 # M1 701 'Ligurum' is the ordinary third-declension genitive plural of 'Ligus, Liguris', not the old '-um' of 'Teucrum'
 (20, 'n', "'Ligurum', old genitive plural.",
           "'Ligurum', genitive plural of 'Ligus, Liguris', the ordinary third-declension ending, not the old '-um' of 'Teucrum' (690)."),
 # M2 700 'Auni' is genitive; l made it an apposition ('son, Aunus')
 (20, 'l', "of the Apennine-dweller the warrior son, Aunus,",
           "of the Apennine-dweller the warrior son, of Aunus,"),
 # M3 675 only three of the four names are Greek accusatives; 'Harpalycum' is Latin
 (9, 'n', "The four names are Greek accusatives:",
          "Three of the four names have Greek accusatives ('Harpalycum' is Latin):"),
 # M4 682 Iliad III.193 is Priam on Odysseus (shorter than Agamemnon by a head), not a mark of Agamemnon's height;
 #    the line's real model is Turnus at VII.784, the same half-line (checked in the source)
 (12, 'n', "'toto vertice supra est', 'is above by his whole head', taller than all: Homer marks Ajax and Agamemnon out the same way (Iliad III.193 and 227, from memory).",
           "'toto vertice supra est', 'is above by his whole head', taller than all: Virgil gave Turnus the same words, 'vertitur arma tenens et toto vertice supra est' (VII.784), and Homer marks Ajax out by head and broad shoulders (Iliad III.227, from memory)."),

 # ---------------- low: labels ----------------
 # L1 659 'Thermodontis' is the Latin third-declension genitive of a Greek name, not a Greek genitive (Greek -οντος); and the spondaic fifth foot
 (4, 'n', "'Thermodontis', Greek genitive.",
          "'Thermodontis', genitive of 'Thermodon' (Greek -ōn, -ontos), whose long syllables make a spondaic fifth foot, Ther-mō | dōn-tis."),
 # L2 705 'fido' takes dative or ablative
 (22, 'n', "'fido', 'trust', takes the dative ('equo').",
           "'fido', 'trust', takes the dative or the ablative; 'forti… equo' may be either."),

 # ---------------- low: elision lists ----------------
 (13, 'n', "Elision 'ill(a) exceptum'.", "Elisions 'ill(a) exceptum', 'nequ(e) enim'."),
 (17, 'n', "Elision 'Orsiloch(um) et'.", "Elisions 'Orsiloch(um) et', 'galeamqu(e) inter'."),
 (20, 'n', "Elision 'subitoqu(e) aspectu'.", "Elisions 'subitoqu(e) aspectu', 'Ligur(um) extremus'."),
 (21, 'n', "Elisions 'curs(u) evadere',", "Elisions 'Isqu(e) ubi', 'curs(u) evadere',"),
 (27, 'n', "Elisions 'virg(o) et', 'poenasqu(e) inimico', 'inimic(o) ex'.",
           "Elisions 'virg(o) et', 'frenisqu(e) adversa', 'poenasqu(e) inimico', 'inimic(o) ex'."),

 # ---------------- low: scansion pointers in n (the lines the scanner got wrong; see scan-fixes-088.json) ----------------
 (3, 'n', "'dia', 'divine', an old epithet from Ennius.",
          "'dia', 'divine', an old epithet from Ennius, two syllables, dī-a."),
 (4, 'n', "'se… refert', returns from battle.",
          "'se… refert', returns from battle; 'Penthesilea', five syllables, -lē-a (I.491)."),
 (5, 'n', "'deicis… fundis', vivid presents,",
          "'deicis', three syllables, dē-i-cis, the line all dactyls; 'deicis… fundis', vivid presents,"),
 (11, 'n', "'equo… Iapyge', 'on an Iapygian horse', from Apulia",
           "'equo… Iapyge', 'on an Iapygian horse' ('Iapyge' four syllables, I-ā-py-ge, a Greek name with vowel I, as at VIII.710), from Apulia"),
 (13, 'n', "'Hunc… exceptum… traicit', 'she catches him and runs him through',",
           "'Hunc… exceptum… traicit', 'she catches him and runs him through' ('traicit' three syllables, trā-i-cit),"),

 # ---------------- low: cross-references checked in the source ----------------
 (16, 'n', "(X.830, from memory)", "(X.830)"),
 (27, 'n', "(VII.808–811, from memory)", "(VII.808–811)"),

 # ---------------- low: i ----------------
 # 661 'seu… seu' lost in i
 (4, 'i', "in their painted armour, around Hippolyta, or when Penthesilea",
          "in their painted armour, whether around Hippolyta or when Penthesilea"),
 # 706 'Dimitte fugam': 'the horse you run on' is ambiguous English
 (23, 'i', "Send away the horse you run on;", "Give up your means of escape;"),
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
    n = len(u['n'].split()); assert 15 <= n <= 139, (k, n)
    assert '“' not in u['n'] and '”' not in u['n'], k
for lay in ('l', 'i'):
    o = sum(u[lay].count('“') for u in U); c = sum(u[lay].count('”') for u in U)
    assert o == c == 3, (lay, o, c)
A.jdump(D, p)
print('applied', len(E), 'edits')
