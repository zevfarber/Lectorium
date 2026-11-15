#!/usr/bin/env python3
"""Reviewer's edits to aeneid-083 units.json (passes 1 and 2; run once from the drafter's file).
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
 # D1 wrong cross-reference: at VIII.116 it is Aeneas who holds out the olive branch, to Pallas
 (0, 'n', "as in Evander's welcome of the Trojans (VIII.116)",
          "as when Aeneas held one out to Pallas on reaching Pallanteum (VIII.116)"),
 # D2 'quod' clause is not the subject; i turned the fact ('that I linger') into a condition ('If')
 (46, 'n', "a 'quod' clause as subject: 'vitam moror'",
           "a 'quod' clause stating a fact, which 'causa' then accounts for: 'as for my lingering, your right hand is the reason'. 'vitam moror'"),
 (46, 'i', "If I drag out a life that I hate now that Pallas is dead, your right hand is the reason, which, as you see, owes Turnus to a son and to a father.",
           "That I still drag out a life I hate, now that Pallas is dead, has one reason: your right hand, which, as you see, owes Turnus to a son and to a father."),
 # D3 'loosed by grief, which had choked it' contradicts itself
 (31, 'n', "'via… vocis', 'the way of the voice', loosed 'dolore', 'by grief', which had choked it.",
           "'via… vocis', 'the way of the voice', 'vix tandem… laxata', 'scarcely at last loosed'; 'dolore', 'for grief', ablative of cause with 'vix': grief had choked it."),
 # D4 'miserae' agrees with 'Primitiae', not with 'iuvenis'; l attached it to the young man
 (34, 'n', "'iuvenis', genitive, with 'miserae'.",
           "'iuvenis', genitive, 'of the young man'; 'miserae', 'wretched', agrees with 'Primitiae'."),
 (34, 'l', "First-fruits of the young man wretched, and of war close at hand",
           "First-fruits of the young man, wretched ones, and of war close at hand"),

 # ---------------- low: notes ----------------
 (6, 'n', "Elision 'm(e) exanimis'.",
          "'oratis' has its last syllable lengthened at the pause after the question, where the metre needs a long (ō-rā | tīs ĕ-quĭ-…). Elision 'm(e) exanimis'."),
 (9, 'n', "poetic plural; the words frame the line-end.", "poetic plural, split across the line-end."),
 (12, 'n', "'vixet', Greenough's 'vixet', a syncopated form of 'vixisset', 'he would have lived', an old form Virgil keeps once here: the pluperfect",
           "'vixet', a syncopated (shortened) form of 'vixisset', 'he would have lived', an old form: the pluperfect"),
 (13, 'n', "dative with the compound verb, framing the line.", "dative with the compound verb, the two words enclosing 'supponite'."),
 (24, 'n', "the two-bladed axe, framing the line-end.", "the two-bladed axe, the two words enclosing the second half of the line."),
 (31, 'n', "The Latin Library and many editors read 'Pallante reposto', 'Pallas having been laid on the bier';",
           "The Latin Library reads 'Pallante reposto', 'Pallas having been laid on the bier' (so too, from memory, most modern texts);"),
 (32, 'n', "'Palla' is the Greek vocative of 'Pallas'.",
           "'Palla' is the Greek vocative of 'Pallas', its final -a long here, as the metre shows."),
 (37, 'n', "'obruerent', imperfect subjunctive, 'would that",
           "'obruerent', imperfect subjunctive where prose would have the pluperfect, 'would that"),
 (41, 'n', "without them, 'alio' means 'than this one'",
           "without them, 'non alio' means 'with no other (funeral) than this one'"),
 (45, 'n', "Aeneas, now king of the Trojans and the Etruscan alliance.",
           "Aeneas, king of the Trojans and now leader of the Etruscan alliance."),
 (50, 'n', "the Etruscan commander, Aeneas's ally since Book VIII.",
           "the Etruscan commander, whose alliance was offered in Book VIII and sealed in Book X (X.153–154)."),
 (59, 'n', "'miseri… Latini', framing the line.", "'miseri… Latini', enclosing 'diversa in parte'."),
 (63, 'n', "beyond telling apart, framing the line-end.", "beyond telling apart, split across the line-end."),
 (68, 'n', "'multa… fama', 'much renown', framing the last line.",
           "'multa… fama', 'much renown', the two words enclosing 'virum meritis sustentat'."),

 # ---------------- low: l construal and layout ----------------
 (11, 'l', "it was fitting to have met, weapons:", "it was fitting to clash, weapons:"),
 (21, 'l', "to carry up on shoulders Trojan will be", "to carry up on shoulders, Trojan ones, will be"),
 (25, 'l', "of so great a forerunner grief,", "of so great, the forerunner, a grief,"),
 (52, 'l', "three times the grieving of the funeral fire", "three times the grieving, of the funeral, fire"),
 (55, 'l', "Here others spoils from the slain stripped Latins", "Here others spoils, from the slain, stripped, Latins"),
 (60, 'l', "the rest and of confused a huge slaughter heap", "the rest, and, of confused, a huge, of slaughter, heap"),
 (61, 'l', "vying with frequent shine fires the fields.", "vying, with frequent, shine, with fires, the fields."),
 (65, 'l', "the dire curse war, and Turnus's wedding:", "the dire they curse, war, and Turnus's wedding:"),

 # ---------------- low: i accuracy and echo recasts ----------------
 (33, 'i', "yet I knew well how strong is the pull of fresh glory in arms, and how sweet the honour of a first battle.",
           "yet I knew well what power new glory in arms has, and the honour, so sweet, of a first battle."),
 (65, 'i', "and boys robbed of their fathers,", "and boys robbed of their parents,"),
 (5, 'i', "“What undeserved misfortune, Latins, has entangled you in so great a war,",
          "“Latins, what fortune you never deserved has caught you up in so great a war,"),
 (49, 'i', "Meanwhile the Dawn had brought out her kindly light for unhappy mortals, bringing back with it work and toil:",
           "Meanwhile Dawn had lifted her life-giving light over suffering mortals, and with it brought back their tasks and their toil:"),
 (52, 'i', "Three times they ran round the burning pyres, girt in gleaming armour;",
           "Three times, belted in their shining armour, they ran their course round the burning pyres;"),
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
for lay in ('l', 'i'):
    o = sum(u[lay].count('“') for u in U); c = sum(u[lay].count('”') for u in U)
    assert o == c == 3, (lay, o, c)
A.jdump(D, p)
print('applied', len(E), 'edits')
