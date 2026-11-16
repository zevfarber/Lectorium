#!/usr/bin/env python3
"""Reviewer's edits to aeneid-085 units.json (passes 1 and 2; run once from the drafter's file).
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
 # D1 'exosa' is itself the participle (of the defective 'exodi'); there is no deponent 'exosus'
 (41, 'n', "'exosa', perfect participle of the deponent 'exosus', 'having hated', active in sense.",
           "'exosa', 'hating', the participle of the defective verb 'exodi', active in sense."),
 # D2 nothing in the line shows the gender of 'dies' ('multa' is the neuter object, as the note itself says)
 (38, 'n', "'dies', feminine here, 'time, the passing of days'.",
           "'dies', 'time, the passing of days', the subject."),
 # D3 'his onerat dictis... iras': he loads the angers with these words; l had 'with these weighs down words'
 (1, 'l', "rises and with these weighs down words and heaps up angers:",
          "rises, and with these loads, words, and heaps up angers:"),
 # D4 425 'variisque': doubtful reading; note no longer opens with the rule-5b formula, and names the other reading
 (38, 'n', "The print has 'variisque', which is hard to construe; the Latin Library reads 'variique', 'and the toil of varied, changeable time'. The print is kept, read as 'with its varied turns'; either way the sense is the same.",
           "'variisque', as printed, is hard to construe; the Latin Library reads 'variique', 'and the toil of varied, changeable time', and some texts are said to read 'variusque', 'and varied toil'. The print is kept, read as 'with its varied turns'; the sense is the same either way."),

 # ---------------- low: speech marks and the rule-5b note ----------------
 # 399: a nested quotation, handled as 084's 252-293 (single marks in l/i); not a 5b misprint, so no 'The print has' opening
 (25, 'n', "The print has an opening double mark before 'Nulla' and no closing mark anywhere; Turnus is quoting Drances' words of 362 back at him, and the reading text marks just those three words as a quotation within his speech.",
           "Drances' words of 362, thrown back at him by Turnus. The print sets an opening double mark before 'Nulla' and closes nothing here; l and i give just these three words in single marks, a quotation inside the speech, as at XI.252–293."),
 # 442: rule-5b note opens with the house formula
 (43, 'n', "The print has an opening double mark before 'devovi', a stray mark, since no new speech begins here; it is left out of the reading text.",
           "The print has '“devovi', a misprint for 'devovi', corrected here: the opening mark is stray, since Turnus's speech runs on and no new one begins."),
 # 413: lowercase after a question mark is Greenough's habit (I.583, VI.845), as LOG records for 6.845
 (32, 'n', "The print sets a question mark after 'regressum' and goes on with a small 'oremus'. This is not a clear misprint: Greenough lets the three 'si'-clauses rise to an indignant question before the answer, so it is kept as printed, and the reading text marks the turn with a dash.",
           "The print sets a question mark after 'regressum' and goes on with a small 'oremus', Greenough's habit after a question (as at I.583 and VI.845): the 'si'-clauses rise to an indignant question before the answer. It is kept as printed, and the reading text marks the turn with a dash."),

 # ---------------- low: notes ----------------
 # elision lists
 (0, 'n', "Elisions 'ide(m) infensus', 'obliqu(a) invidia', 'op(um) et'.",
          "Elisions 'ide(m) infensus', 'obliqu(a) invidia', 'stimulisqu(e) agitabat', 'op(um) et'."),
 (3, 'n', "Elisions 'auspici(um) infaustum', 'dic(am) equidem'.",
          "Elisions 'auspici(um) infaustum', 'dic(am) equidem', 'consediss(e) urbem'."),
 (6, 'n', "Elision 'veniamqu(e) oremus'.", "Elisions 'ips(um) obtestemur', 'veniamqu(e) oremus'."),
 (30, 'n', "Elisions 'Numqu(am) animam', 'dextr(a) hac', 'pector(e) in'.",
           "Elisions 'Numqu(am) animam', 'dextr(a) hac', 'tec(um) et', 'pector(e) in'."),
 (32, 'n', "Elision 'nequ(e) habet'.", "Elisions 'nequ(e) habet', 'pac(em) et'."),
 (33, 'n', "the courage the Latins used to have. No elisions.",
           "the courage the Latins used to have. Elision 'Quamqu(am) O'."),
 (40, 'n', "'florentis', '-is' accusative plural. No elisions.",
           "'florentis', '-is' accusative plural. The second line repeats VII.804 word for word. Elisions 'Volscor(um) egregia', 'equit(um) et'."),
 (42, 'n', "Elision 'Ib(o) animis'.", "Elisions 'Ib(o) animis', 'pari(a) induat'."),
 # 336-337 'stimulis... amaris' frame the verb, not the line-end
 (0, 'n', "'stimulis… amaris', 'with bitter goads', framing the line-end.",
          "'stimulis… amaris', 'with bitter goads', framing the verb."),
 # Servius attribution from memory, unchecked: softened
 (1, 'n', "his father was obscure, or unknown (Servius takes it either way).",
          "his father was obscure, or unknown; the words allow either."),
 # 'adicias' in a request to the king is jussive, not potential
 (5, 'n', "'adicias', potential or jussive subjunctive;", "'adicias', jussive subjunctive, a polite command;"),
 # 'fugae fidens': the allusion to IX.815-818 is an interpretation, not the plain sense
 (4, 'n', "'fugae fidens', 'trusting in flight', a sneer: Turnus escaped from inside the camp only by leaping into the Tiber (IX.815–818).",
          "'fugae fidens', 'trusting in flight', a sneer, perhaps glancing at his escape from inside the camp by a leap into the Tiber (IX.815–818)."),
 # 'Sat funera': 'sat' as an indeclinable adjective; 'genitive understood' was muddled
 (11, 'n', "'Sat', short for 'satis', 'enough', with the genitive understood or simply adverbial.",
           "'Sat', short for 'satis', 'enough', standing as an indeclinable adjective with 'funera'."),
 # 'adversum' can go with 'pectus' as well as 'hostem'
 (12, 'n', "'aude', 'dare'; 'adversum… in hostem', 'against the enemy opposite'.",
           "'aude', 'dare'; 'adversum' goes with 'pectus', 'your breast turned to face him', or with 'hostem', 'the enemy opposite'."),
 # the Latins' burials are 203-212, not 182-224 (182-202 are the Trojans', 213-224 the mourning in the city)
 (13, 'n', "The Latins have just been burying their dead under truce (182–224).",
           "The Latins have just been burying their dead under truce (203–212)."),
 # 115-118: Aeneas said Turnus should have faced him, not that he would 'rather have met' Turnus
 (14, 'n', "Aeneas, who said he would rather have met Turnus in single combat (115–118).",
           "Aeneas, who said Turnus should have fought it out with him alone (115–118)."),
 # cross-references worth giving (checked in the source)
 (27, 'n', "Troy fell twice, to Hercules in Laomedon's time and to the Greeks.",
           "Troy fell twice, to Hercules in Laomedon's time and to the Greeks (Numanus's 'bis capti Phryges', IX.599)."),
 (28, 'n', "'Larissaeus', from Larissa in Thessaly, Achilles' country.",
           "'Larissaeus', from Larissa in Thessaly, Achilles' country; the pair echoes II.197, 'Tydides… Larisaeus Achilles'."),

 # ---------------- low: l construal and layout ----------------
 (0, 'l', "with sidelong envy and with goads was driving bitter,", "with sidelong envy and with goads was driving, bitter ones,"),
 (2, 'l', "what the fortune of the people brings, but to say they mutter.",
          "what the fortune of the people brings, but to say it they hesitate, muttering."),
 (8, 'l', "Turnus, together with peace's sole inviolable pledge.", "Turnus, and at the same time peace's sole inviolable pledge."),
 (21, 'l', "tongue and in feet fleeing those", "tongue and in those runaway feet of yours"),
 (26, 'l', "of the Dardanian and to your own affairs.", "the Dardanian, and to your own affairs."),
 (35, 'l', "but if even for the Trojans with much glory has come", "but if even to the Trojans, with much, glory has come,"),

 # ---------------- low: i ----------------
 # 'surgit' is in 342 and unit 340-342's i already has 'he rose'; unit 336-339 had it too
 (0, 'i', "Then Drances rose, hostile as ever, a man whom", "Then Drances, hostile as ever, a man whom"),
 (12, 'i', "then be bold and carry your breast confidently against the enemy who faces you.",
           "then be bold, and bear your breast confidently to face the enemy."),
 (29, 'i', "Or then, when the scheming villain pretends", "Or take the times when the scheming villain pretends"),
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
    assert '“' not in u['n'] or k == 43, k
for lay in ('l', 'i'):
    o = sum(u[lay].count('“') for u in U); c = sum(u[lay].count('”') for u in U)
    so = sum(u[lay].count('‘') for u in U); sc = sum(u[lay].count('’') for u in U)
    assert o == c == 2 and so == sc == 1, (lay, o, c, so, sc)
A.jdump(D, p)
print('applied', len(E), 'edits')
