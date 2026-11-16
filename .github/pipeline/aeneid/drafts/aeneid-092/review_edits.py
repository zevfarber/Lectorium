#!/usr/bin/env python3
"""Reviewer's edits to aeneid-092 units.json (passes 1 and 2; run once from the drafter's file).
Each edit: (unit index, field, old, new); old must occur exactly once in that field. Only l, i, n and the top-level
'advisory' are touched; t, ln, p, v, title, titleEn, part and about never. Run once (it refuses if the file has already
been edited: every old string must still be present exactly once)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..')))
import aeneid_lib as A
p = os.path.join(HERE, 'units.json'); D = A.jload(p); U = D['sentences']
before = [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U]
top = {k: D[k] for k in ('title', 'titleEn', 'part', 'about')}

E = [
 # ---------------- medium ----------------
 # M2 170: saetigeri is masculine (saetiger, -era, -erum), so suis is not a sow
 (27, 'l', "of a bristly sow the young", "of a bristly swine the young"),
 (27, 'i', "the young of a bristly sow", "the young of a bristly swine"),
 (27, 'n', "'saetigeri fetum suis', 'the young of a bristly sow', a piglet:",
           "'saetigeri fetum suis', 'the young of a bristly swine', a piglet ('saetigeri' is masculine, so 'sus' is the boar or simply 'pig', not a sow);"),
 # M3 211: 'gesture' is a Latin form (vocative of gesturus); what is wrong is sense and metre
 (45, 'n', "'gesture' is not Latin and breaks the metre,",
           "'gesture' makes no sense here and breaks the metre,"),

 # ---------------- low: l ----------------
 # L1 121-122: 'portis' is in the second line; 'from the full / columns' misread as 'from the full columns'
 (5, 'l', "Forth comes the legion of the Ausonians, and, javelin-armed, from the full\ncolumns pour themselves, gates.",
          "Forth comes the legion of the Ausonians, and, javelin-armed, from the full\ngates the columns pour themselves out."),
 # L2 140-141: 'honorem' stands in 140, not 141
 (11, 'l', "presides (this to her the king of the air on high\nJupiter, for her maidenhood snatched away, hallowed as an honour):",
           "presides (this to her the king of the air on high, as an honour,\nJupiter, for her maidenhood snatched away, hallowed):"),
 # L3 158: 'or do you stir up' reads as a question
 (21, 'l', "or do you stir up war and shake loose the framed treaty:",
           "or you, stir up war and shake loose the framed treaty:"),

 # ---------------- low: notes ----------------
 # L4 139: diva and dea are two words, not two forms of one
 (11, 'n', "two forms of the word set side by side.", "two words for 'goddess' set side by side."),
 # L5 140-141: the honour paid is the rule over waters (her immortality is spoken of only at 878-879)
 (11, 'n', "Jupiter had violated her and paid her with immortality.",
           "Jupiter had violated her and gave her this honour in return."),
 # L6 148: Ardea is a likely reading, not a certainty
 (14, 'n', "'tua moenia', 'your walls', Ardea, the city of Turnus and his sister.",
           "'tua moenia', 'your walls', most likely Ardea, the city of Turnus and his sister."),
 # L7 166-169: the sentence begins at 161 (reges ... procedunt), as the unit's own note says further on
 (26, 'n', "The sentence begun at 166 runs to 171; it is cut at the comma.",
           "The sentence begun at 161 runs on to 171; it is cut at the comma."),
 # L8 174: missing elision
 (28, 'n', "Elision 'Ill(i) ad'.", "Elisions 'Ill(i) ad', 'paterisqu(e) altaria'."),
 # L9 177: quam is a relative pronoun, not a noun
 (30, 'n', "'quam propter', 'on account of which', the preposition after its noun.",
           "'quam propter', 'on account of which', the preposition after its object."),
 # L10 181: scansion pointer (the scanner's fit is right)
 (31, 'n', "'fontisque fluviosque', double '-que', 'both springs and rivers';",
           "'fontisque fluviosque', double '-que', 'both springs and rivers'; the first '-que' counts long before 'fl-', at the beat of the second foot (as 'ensemque', 12.89);"),
 # L11 185: Iulus is three syllables here too (scan-fixes 12.185)
 (32, 'n', "'cedet… agris', 'will withdraw from the land'.",
           "'cedet… agris', 'will withdraw from the land'; 'Iulus' has three syllables, I-u-lus, as at 110."),
 # L12 210: missing elision
 (45, 'n', "The oath ends here. No elisions.", "The oath ends here. Elision 'ol(im) arbos'."),
 # L13 213-214: the phrase is parted across the line-end, it does not frame a line
 (47, 'n', "'rite sacratas… pecudes', 'the victims duly consecrated', its words framing a line.",
           "'rite sacratas… pecudes', 'the victims duly consecrated', its words parted across the line-end."),
 # L14 118: 'portable braziers' is more than can be checked
 (3, 'n', "'focos', 'hearths', portable braziers for the sacrificial fire.",
          "'focos', 'hearths', fires for the sacrifice, set beside the altars."),
 (3, 'i', "were making ready fire-pans in the middle", "were making ready hearth-fires in the middle"),
 # L15 123: the Etruscans sailed with Aeneas in Book X (he won them in Book VIII)
 (6, 'n', "the Etruscan allies who came to Aeneas in Book X.", "the Etruscan allies who sailed with Aeneas in Book X."),

 # ---------------- low: i, precautions against remembered phrasing ----------------
 # L16 115
 (2, 'i', "and breathe daylight from their raised nostrils:", "and blow the daylight out through their lifted nostrils:"),
 # L17 140
 (11, 'i', "an honour that Jupiter, high king of heaven, conferred on her",
           "an honour that Jupiter, the king who reigns in the heights of the sky, conferred on her"),
 # L19 192-193 (pass 2): 'sollemne' is customary, established; 'by right' drifted from l and n
 (36, 'i', "keep the sovereignty that is his by right;", "keep the sovereignty that long custom has made his;"),
 # L18 156
 (20, 'i', "“This is no time for tears,” said Saturnian Juno.", "“Tears do not suit this hour,” said Saturnian Juno."),
]

for k, f, old, new in E:
    s = U[k][f]
    assert s.count(old) == 1, (k, f, old[:60], s.count(old))
    U[k][f] = s.replace(old, new)

# M1 advisory: 140-141 is the poet's parenthesis, not Juno's words
adv = D['advisory']
old = "In a few words Juno recalls that Jupiter took Juturna's maidenhood and gave her rule over pools and rivers in return (140–141), and speaks of the other Latin women who went to his bed (143–144)."
new = "In a parenthesis just before Juno speaks, the poem says that Jupiter took Juturna's maidenhood and gave her rule over pools and rivers in return (140–141); Juno then speaks of the other Latin women who went to his bed (143–144)."
assert adv['lede'] == old
adv['lede'] = new

# guards
assert [(u['t'], u['ln'], u.get('p'), u.get('v')) for u in U] == before
assert {k: D[k] for k in ('title', 'titleEn', 'part', 'about')} == top
for k, u in enumerate(U):
    assert u['l'].count('\n') == u['t'].count('\n'), k
    assert '\n' not in u['i'], k
    assert 15 <= len(u['n'].split()) <= 139, (k, len(u['n'].split()))
for lay in ('t', 'l', 'i'):
    assert sum(u[lay].count('“') for u in U) == sum(u[lay].count('”') for u in U) == 6, lay
A.jdump(D, p)
print(len(E) + 1, 'edits applied')
