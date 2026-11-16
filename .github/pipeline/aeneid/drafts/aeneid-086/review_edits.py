#!/usr/bin/env python3
"""Reviewer's edits to aeneid-086 units.json (passes 1 and 2; run once from the drafter's file).
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
 # D1 505 'prima' cannot be feminine: the subject of 'temptare' is accusative 'Me', so a feminine would be 'primam';
 #    'prima' is neuter plural with 'pericula'
 (22, 'n', "'prima', feminine again, 'the first'.",
           "'prima' is neuter plural with 'pericula', 'the first dangers of war': a feminine 'first' would have to be 'primam', agreeing with 'Me'."),
 (22, 'l', "Me allow first with my hand to try the dangers of war;",
           "Me allow with my hand to try the first dangers of war;"),
 (22, 'i', "Let me be the first to put my hand to the hazards of war, while",
           "Let me put my hand to the first hazards of war, while"),
 # D2 480 'tanti, oculos' is hiatus, not elision (the line has no fit with the elision)
 (13, 'n', "Elisions 'summasqu(e) ad', 'tant(i) oculos'.",
           "Elision 'summasqu(e) ad'. 'tanti, oculos' is not elided: 'tanti' keeps its long -i in hiatus at the pause and the main caesura (as 'Samo hic', I.16)."),
 # D3 492 'fugit' is perfect (fūgit, as the metre requires), not present
 (18, 'n', "'qualis', 'such as', answering Turnus.",
           "'qualis', 'such as', answering Turnus. 'fugit' is perfect, 'fūgit' (the metre needs the long u), the instant of breaking loose; the presents 'tendit… emicat' follow."),
 (18, 'l', "just as when, his tethers broken, flees the stalls",
           "just as when, his tethers broken, has fled the stalls"),

 # ---------------- low: rule-5b notes open with the print's reading ----------------
 (5, 'n', "The print encloses the whole of 459, 'ait' and 'Turnus' included, in marks, opens a second time before 'cogite', and joins the closing mark to 'Nec' at 461: misprints for a speech that runs 'Immo… O cives… ruunt.' with 'ait… adrepto tempore, Turnus' outside it, corrected here.",
          "The print has '“Immo, ait, O cives adrepto tempore, Turnus,”', with 'ait' and 'Turnus' inside the marks, a second opening mark before 'cogite', and 'ruunt. ”Nec' at 461 (as 'vale. ”Nec', 11.98): misprints for a speech 'Immo… O cives… ruunt.' with 'ait… adrepto tempore, Turnus' outside it, corrected here."),
 (6, 'n', "The print sets a second opening mark before 'duc' at the start of 464, a misprint, since Turnus's speech is already running from 463; corrected here, with 'he says' set outside the marks.",
          "The print has '“duc, ait, et Rutulos' at the start of 464, a misprint (as '“Ite, ait,' at 11.24) for 'duc,” ait, “et Rutulos', corrected here: Turnus's speech is already running from 463 and only breaks off for 'ait'."),

 # ---------------- low: notes ----------------
 # elision lists
 (6, 'n', "Elision 'Volus(e) armari'.", "Elisions 'Volus(e) armari', 'Volscor(um) edice'."),
 (31, 'n', "Elision 'siv(e) instare'.", "Elisions 'summoqu(e) in', 'siv(e) instare'."),
 # 460 'cogite concilium' throws back Latinus's 'cogere concilium' (304; checked)
 (5, 'n', "'cogite… laudate', mocking imperatives;",
          "'cogite… laudate', mocking imperatives, 'cogite concilium' throwing back Latinus's own 'cogere concilium' (304);"),
 # VII.670-672: Coras and Catillus are Argive twins from Tibur, named after their brother Tiburtus (checked)
 (7, 'n', "Coras and his brother Catillus, Argive founders of Tibur, appeared in the catalogue of Book VII (from memory, about 670–677).",
          "Coras and his twin Catillus, Argive warriors from Tibur, the town named after their brother Tiburtus, appeared in the catalogue of Book VII (670–677)."),
 (28, 'n', "'the band of Tiburtus', founder of Tibur and brother of Coras and Catillus: the men of Tibur.",
           "'the band of Tiburtus', the brother of Coras and Catillus after whom Tibur is named (VII.671): the men of Tibur."),
 # cross-references checked in the source
 (3, 'n', "(Turnus himself 'arma amens fremit' at VII.460, from memory)", "(Turnus himself 'arma amens fremit' at VII.460)"),
 (13, 'n', "(VI.93, from memory)", "(VI.93)"),
 # 469 'pater' lengthened in the third-foot arsis
 (9, 'n', "'pater', a title of respect for the king.",
          "'pater', a title of respect for the king; its last syllable is lengthened at the pause in the third foot, a licence Virgil allows at the caesura."),
 # 487 aenis trisyllabic; tense sequence misdescribed (horrebat, imperfect, comes first)
 (17, 'n', "'aenis… squamis', 'with bronze scales', scale-armour;",
           "'aenis… squamis', 'with bronze scales', scale-armour, 'aenis' three syllables, a-e-nis;"),
 (17, 'n', "The tenses move from pluperfect to imperfect to the vivid present 'exsultat… praecipit';",
           "Imperfects ('horrebat', 'fulgebat') and pluperfects ('incluserat', 'adcinxerat') give way to the vivid present 'exsultat… praecipit';"),

 # ---------------- low: l ----------------
 # 475 'cinxere' is the verb, not an adjective 'ringed garland'
 (12, 'l', "Then the walls with a varied ringed garland", "Then the walls, with a varied garland, ringed"),
 # 487-488 'squamis' is the ablative with 'horrebat', not its object
 (17, 'l', "he bristled scales, and his calves", "he bristled, scales, and his calves"),
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
    assert ('“' not in u['n'] and '”' not in u['n']) or k in (5, 6), k
for lay in ('l', 'i'):
    o = sum(u[lay].count('“') for u in U); c = sum(u[lay].count('”') for u in U)
    assert o == c == 7, (lay, o, c)
A.jdump(D, p)
print('applied', len(E), 'edits')
