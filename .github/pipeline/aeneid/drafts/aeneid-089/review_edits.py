#!/usr/bin/env python3
"""Reviewer's edits to aeneid-089 units.json (passes 1 and 2; run once from the drafter's file).
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
 # M1 757 'Tiburtum' is third-declension (Tiburs, Tiburtis) with -um for -ium, not the old -um for -orum
 (14, 'n', "'Tiburtum', genitive plural of 'Tiburtes', the people of Tibur (Tivoli), with the old short ending '-um'.",
           "'Tiburtum', genitive plural of 'Tiburs, Tiburtis', 'man of Tibur' (Tivoli), with '-um' for the more usual '-ium' (not the old '-um' for '-orum' of 'deum')."),
 # M2 741-744 concitat (concito) and concitus (participle of concieo) are not the same verb
 (7, 'n', "'concitat… concitus', the same verb twice.",
          "'concitat… concitus', two words of one family ('concito' and the participle of 'concieo'), 'spurs… roused'."),
 # M3 798 'Notos' is an ordinary second-declension accusative plural, not a Greek accusative
 (32, 'n', "'Notos', Greek accusative plural of 'Notus', the south wind.",
           "'Notos', accusative plural of 'Notus', the south wind, a Greek name with ordinary Latin endings."),
 # M4 834-835 incurrunt has three subjects; it is not 'a singular subject with a plural verb'
 (49, 'n', "'incurrunt… omnis copia', a singular subject with a plural verb, because the host is many men (agreement by sense); 'densi', plural for the same reason.",
           "'incurrunt', plural for its three subjects, 'omnis copia', 'duces' and 'alae'; 'densi', masculine plural, agrees by sense with the men of the host, not with the feminine 'copia'."),
 # M5 773 l attached 'Gortynian' to the bow; 'Gortynia' goes with 'spicula'
 (21, 'l', "was shooting shafts, from a Lycian, Gortynian, horn-bow;",
           "Gortynian shafts was shooting from a Lycian horn;"),
 # M6 747 i 'the arms and the man' is the best-known English opening of the poem; the house I.1 l is 'Arms and a man'
 (9, 'i', "carrying the arms and the man;", "carrying arms and a man;"),
 # M7 831 set piece (= XII.952): 'crying out against its lot' doubles 'cum gemitu' and is not 'indignata';
 #    'passed' loses 'fugit'. l: 'down under the shades' for the accusative of motion, after the house IV.660 l.
 (47, 'i', "and life, crying out against its lot, passed with a groan into the world of shades.",
           "and life, bitter at its going, took flight with a groan down among the shades."),
 (47, 'l', "and life with a groan takes flight, chafing, beneath the shades.",
           "and life with a groan takes flight, chafing, down under the shades."),
 (47, 'n', "'indignata', 'resenting', unwilling to leave a young body before its time.",
           "'fugit', the present, 'takes flight' (the metre wants a short 'u'; the perfect is 'fūgit'). 'indignata', 'resenting', unwilling to leave a young body before its time."),

 # ---------------- low: elision lists ----------------
 (29, 'n', "The speech ends at 793. No elisions.", "The speech ends at 793. Elision 'remeab(o) inglorius'."),
 (33, 'n', "Elisions 'converter(e) animos', 'cunct(i) ad'.", "Elisions 'Erg(o) ut', 'converter(e) animos', 'cunct(i) ad'."),
 (47, 'n', "(XII.952). No elisions.", "(XII.952). Elision 'paulat(im) exsolvit'."),
 (48, 'n', "The shout is both grief and rage. No elisions.", "The shout is both grief and rage. Elision 'ver(o) immensus'."),

 # ---------------- low: labels, facts, cross-references ----------------
 # 725 'hominum sator atque deorum' as an Ennian title is unverified; Virgil's own use at I.254 is checked in the source
 (0, 'n', "Jupiter, an Ennian title that renders Homer's 'father of men and gods'.",
          "Jupiter, the title Virgil gave him at I.254, a Latin form of Homer's 'father of men and gods'."),
 # 735 'adloquitur' has the prefix ad-, not in-
 (5, 'n', "(the prefix 'in-' kept unassimilated, as in 'adloquitur' at 821)",
          "(the prefix 'in-' kept unassimilated, as 'ad-' is in 'adloquitur' at 821)"),
 # 750 V.438 checked in the source
 (11, 'n', "('tela exit', V.438, from memory)", "('tela… exit', V.438)"),
 # 754 'arrectis' is orthography only; conventions: do not note
 (12, 'n', "'with scales raised'; the Latin Library spells it 'arrectis'.", "'with scales raised'."),
 # 759 'again and again' overstated; VIII.499 checked in the source
 (15, 'n', "and Virgil calls them so again and again.",
           "and Evander's prophecy calls them so ('O Maeoniae delecta iuventus', VIII.499)."),
 # 768 Cybelus attested by Greenough's 'Cybeli' at III.111; Chloreus scansion pointer (scan-fixes 11.768)
 (20, 'n', "'sacer Cybelo', 'sacred to Cybelus', the mountain",
           "'sacer Cybelo', 'sacred to Cybelus' (dative; 'Cybeli' at III.111), the mountain"),
 (20, 'n', "'Chloreus', two syllables, 'eu' a Greek diphthong.",
           "'Chloreus', two long syllables, Chlō-reus, 'eu' a Greek diphthong."),
 # 773 'torquebat' of a bow: shooting
 (21, 'n', "'torquebat', 'was whirling, hurling'.", "'torquebat', 'was whirling, sending', here of shooting."),
 # 800 scansion pointer (scan-fixes 11.800)
 (33, 'n', "the '-is' accusative plural, 'keen'.", "the '-is' accusative plural, 'keen', scanned ā-crīs, both long."),
 # 827 misprint notes in the house form of aeneid-041/042 (the print's reading quoted with its mark)
 (45, 'n', "The last words of Camilla's speech, 'Iamque vale', 'and now farewell', the ordinary leave-taking of Romans at a grave as well as in life. The speech closes here, though the print sets its closing mark after a space, joined to the next word (see the next unit); l and i close the speech after 'vale.'. No elisions.",
           "The print has 'vale. ”Simul', a misprint for 'vale.” Simul', corrected here. The mark closing Camilla's speech is set after a space and joined to the next word, so t keeps the print and the mark stands at the head of the next unit, while l and i close the speech after 'vale.'. 'Iamque vale', 'and now farewell', is the ordinary Roman leave-taking, in life and at a funeral (Aeneas to the dead Pallas, 'aeternumque vale', XI.98). No elisions."),
 (46, 'n', "The print has 'vale. Simul' with the closing double mark joined to 'Simul', a misprint for the mark set straight after 'vale.', corrected here;",
           "The print has 'vale. ”Simul', a misprint for 'vale.” Simul', corrected here;"),

 # ---------------- low: l ----------------
 (4, 'l', "A woman, scattered, drives you, and these columns turns!", "A woman the stragglers drives, and these columns turns!"),
 (12, 'l', "and with raised bristles with scales and hisses with its mouth,", "and bristles with raised scales and hisses with its mouth,"),
 (24, 'l', "Trojan, or that in captured she might parade herself in gold,", "Trojan, or that in captured she might parade herself, gold,"),
 (26, 'l', "we worshippers press our steps on the many coal,", "we worshippers press our steps on much live coal,"),
 (28, 'l', "(for me other deeds glory\nwill bring):", "(for me the other glory\ndeeds will bring):"),
 (29, 'l', "let this dread, by my wound, if only plague\nfall, struck, I will return inglorious to my father's cities.”",
           "if only this dread, by my wound, plague\nfall, struck down, I will return inglorious to my fathers' cities.”"),
 (30, 'l', "Heard him, and of the prayer that should succeed a part,\nPhoebus granted in his mind, a part into the winged scattered breezes:",
           "Heard, and of the prayer Phoebus that should succeed a part\ngranted in his mind, a part into the winged he scattered breezes:"),

 # ---------------- low: i ----------------
 (0, 'i', "was not watching these things with unheeding eyes as he sat on high on the summit of Olympus:",
          "is not watching all this with unheeding eyes as he sits on high on the summit of Olympus:"),
 (2, 'i', "among the slaughter and the giving ranks,", "among the slaughter and the ranks giving way,"),
 (17, 'i', "Wherever the maiden carried herself in her fury through the midst of the ranks, Arruns followed close and silently traced her tracks;",
           "Wherever the maiden has carried herself in her fury through the midst of the ranks, there Arruns follows close and silently traces her tracks;"),
 (18, 'i', "where she came back victorious and withdrew her step from the foe, there the young man stealthily turned aside his swift reins.",
           "where she comes back victorious and withdraws her step from the foe, there the young man stealthily turns aside his swift reins."),
 (20, 'i', "sacred to Mount Cybelus and once its priest,", "sacred to Mount Cybelus and once a priest,"),
 (21, 'i', "was hurling Cretan arrows from a Lycian bow;", "was shooting Cretan arrows from a Lycian bow;"),
 (34, 'i', "She alone was not aware of", "She herself was not aware at all of"),
 (42, 'i', "now the cruel wound is ending me,", "now the cruel wound is making an end of me,"),
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
    assert sum(u[lay].count('“') for u in U) == sum(u[lay].count('”') for u in U) == 3, lay
A.jdump(D, p)
print(len(E), 'edits applied')
