#!/usr/bin/env python3
"""Reviewer's edits to aeneid-090 units.json (passes 1 and 2; run once from the drafter's file).
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
 # M1 848-849: the misprint notes in the rule-5b house form used for 827 in aeneid-089 (note opens with the print's reading)
 (5, 'n', "The lament closes here. Greenough's print sets the closing mark after a space, joined to the next word, 'Fuit', as at 827; t keeps the print, and l and i close the speech after 'merita.'.",
          "The print has 'merita. ”Fuit', a misprint for 'merita.” Fuit', corrected here. The mark closing Opis's lament is set after a space and joined to the next word, as at 827, so t keeps the print and the mark stands at the head of the next unit, while l and i close the speech after 'merita.'."),
 (6, 'n', "The mark at the head of t belongs to the speech just ended (see the previous unit); l and i carry none.",
          "The print has 'merita. ”Fuit', a misprint for 'merita.” Fuit', corrected here; the mark at the head of t belongs to the speech just ended, so l and i carry none."),
 # M2 910 l: English order made Aeneas the subject of 'adgnovit'
 (29, 'l', "so savage Aeneas recognised Turnus in arms", "so Turnus recognised savage Aeneas in arms"),
 # M3 904-905 n: 'ingressus' as finite contradicted l ('both overcomes… and…'), the double -que of exsuperatque… silvaque
 (27, 'n', "'ingressus', 'having entered', may be taken as a finite verb with 'est' left out, so that '-que' on 'exsuperat' joins it to what follows.",
           "'ingressus', 'having entered', a participle; then 'exsuperatque… silvaque', the double '-que', 'both surmounts… and comes out'. Some take 'ingressus' as 'ingressus est', with the first '-que' joining 'exsuperat' to it."),
 # M4 852-853 l: 'se' (object of sistit) was rendered as the intensive 'herself'
 (7, 'l', "Here the goddess herself first with swift swoop, most beautiful,\nsets, and Arruns",
          "Here the goddess first with swift swoop, most beautiful,\nsets herself, and Arruns"),

 # ---------------- low: elision lists ----------------
 (12, 'n', "Elisions 'un(a) Arruns', 'haesitqu(e) in'.", "Elisions 'stridor(em) aurasque', 'un(a) Arruns', 'haesitqu(e) in'."),
 (13, 'n', "'atqu(e) extrema', 'campor(um) in'.", "'atqu(e) extrema', 'oblit(i) ignoto', 'campor(um) in'."),
 (21, 'n', "'accipe(re) orantis'", "'acciper(e) orantis'"),
 (22, 'n', "Elisions 'exclus(i) ante', 'lacrumantumqu(e) ora'", "Elisions 'Exclus(i) ante', 'ant(e) oculos', 'lacrumantumqu(e) ora'"),
 (29, 'n', "Elisions 'Laurentiaqu(e) agmina', 'saev(um) Aenean'.", "Elisions 'Laurentiaqu(e) agmina', 'saev(um) Aenean', 'flatusqu(e) audivit'."),
 (31, 'n', "Elision 'urb(em) et'.", "Elisions 'ant(e) urbem', 'urb(em) et'."),

 # ---------------- low: labels, facts, quotations ----------------
 # 848: Greenough prints 'volnere' at XI.591
 (5, 'n', "'quicumque sacrum violarit vulnere corpus'", "'quicumque sacrum violarit volnere corpus'"),
 # 838, 886: participial gen. pl. in -um is the poets' form, not a Greenough spelling
 (1, 'n', "Greenough's old genitive plural of the participle in '-um' for '-ium'", "the poets' genitive plural of the participle in '-um' for '-ium'"),
 (21, 'n', "two genitive plurals in Greenough's old '-um' for '-ium'", "two genitive plurals in the poets' '-um' for '-ium'"),
 # 844: 'umerus' is the better spelling (L&S), not a Greenough peculiarity
 (3, 'n', "'umero', Greenough's spelling of 'humero', 'shoulder'.", "'umero', 'shoulder', also spelled 'humero'."),
 # 847: the genitive agrees with an understood 'tui', not with the nominative subject of 'patieris'
 (4, 'n', "'famam… inultae', 'the repute of (one) unavenged', the genitive agreeing with the 'you' implied in 'patieris':",
          "'famam… inultae', 'the repute of (one) unavenged': 'inultae' is genitive, agreeing with 'tui', 'of you', understood with 'famam':"),
 # 855, 875: orthographic Latin Library differences are not noted (conventions; as 089 L8)
 (9, 'n', "'dirige', 'direct'; the Latin Library spelling 'derige' is the same word.", "'dirige', 'direct'."),
 (16, 'n', " The Latin Library spells 'quadripedumque', the same word.", ""),
 # 868-869: the verb is 'fugit… fugiunt… fugit', not 'fugit' three times
 (14, 'n', "with 'fugit' repeated three times in two lines (868–869)", "with 'fugit… fugiunt… fugit', the verb three times in two lines (868–869)"),
 # 858: scansion pointer (scan-fixes 11.858)
 (11, 'n', "'Threissa', 'the Thracian woman', the Greek form,", "'Threissa', 'the Thracian woman', the Greek form, three syllables (Thrē-is-sa),"),

 # ---------------- low: l ----------------
 # 838: 'medio' agrees with 'clamore', not with the young men
 (1, 'l', "And as, far off, in the midst of the young men, amid the shouting of them raging,",
          "And as, far off, in the midst of the raging young men's shouting,"),
 # 906-907: 'are borne' (feruntur) stood in the 907 line
 (28, 'l', "So both to the walls, swift, with all their\ncolumn are borne,", "So both to the walls, swift, and with their whole are borne\ncolumn,"),

 # ---------------- low: i ----------------
 (4, 'i', "now at the very end of death;", "now at the very point of death;"),
 (23, 'i', "they make do for iron,", "they make wood do the work of iron,"),
 # 910: 'saevum' goes with 'Aenean' (the note: 'savage in arms')
 (29, 'i', "Turnus too recognised Aeneas in his savage armour", "Turnus too recognised Aeneas, savage in his armour,"),
 # 915: i had one subject entrenching 'by the walls'; the note (and 'moenia vallant') has the walls ringed with ramparts
 (31, 'i', "they pitch camp before the city and entrench themselves by the walls.", "they pitch camp before the city, and the walls are ringed with ramparts."),
 # 875 (= VIII.596): precaution against a stock rendering of the famous line
 (16, 'i', "and the hooves of the galloping horses shake the crumbling plain.", "and the galloping horses' hooves batter the crumbling plain."),
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
for lay in ('t', 'l', 'i'):
    assert sum(u[lay].count('“') for u in U) == sum(u[lay].count('”') for u in U) == 2, lay
A.jdump(D, p)
print(len(E), 'edits applied')
