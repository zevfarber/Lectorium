# beowulf-fitt-23 — review, pass 1 (adversarial)

Scope: all 34 units (1557–1650). Checked every grammatical label in every note against its line, every
line cross-reference against `source/beowulf-klaeber1922.json`, every apparatus claim against the packet,
OE → `l` word by word, `l` ↔ `i`, remembered English in `i`, and renderings against the published parts
(`grep` of the root `beowulf-*.json`). Edits made by script (`units.json` in place); `t`, `ln`, `v`, `p`
untouched (verified against a copy of the original); `i` present on every unit.

Severity count: **high 0 · medium 2 · low 9** (11 changes, 17 fields).

## Changes

| line | field | sev. | what was wrong | what done |
|---|---|---|---|---|
| 1607 | l, i, n | medium | ‘sǣla ond mǣla’ given as “times and seasons”: the order is reversed against the OE and the phrase is the ready-made biblical/translation formula (rule 4). ‘sǣl’ is the season-word, ‘mǣl’ the time-word. | “seasons and times” in `l`, `i` and the note’s gloss; note adds ‘sǣl’ ‘season, fit time’, ‘mǣl’ ‘time, occasion’. |
| 1615, 1620 | l, i, n | medium | ‘ellorgǣst’ / ‘ellorgāst’ rendered “the alien spirit” (`l`) and “the alien creature” (`i`). The published parts render the compound “elsewhere-ghost” in `l` (805, 1345) and “spirit(s) from elsewhere” / “his spirit, bound elsewhere” in `i`. “Alien” is not in the lexical sense and breaks the house kenning. | `l` → “the elsewhere-ghost” (both units); `i` → “the spirit from elsewhere” (both); 1617 note’s construction gloss and definition brought in line (“elsewhere-ghost”, a spirit from elsewhere). |
| 1557 | n | low | Note asserted ‘on searwum’ = “among the war-gear” with no alternative, though the same phrase at 249 is published as “a man in war-gear”, and could describe Beowulf here. | Added the 249 parallel and why ‘among’ is preferred. |
| 1572 | l | low | `l` “turned then by the wall” while the note glosses ‘be wealle’ “along the wall” and `i` has “along the wall”. | `l` → “along the wall”. |
| 1580 | n | low | ‘lāðlicu lāc’ unparsed; the ending fits singular (fem.) or plural (neut.), and the plural would suit the fifteen dead. | Note adds that the ending fits either number. `l`/`i` singular kept. |
| 1584 | i | low | “so far that he saw Grendel lying” is not natural English. | → “to the point where he saw Grendel lying”. |
| 1584 | n | low | ‘tō ðæs þe’ chosen without reference to the published rendering at 714 (“until”). | Note adds that 714 rendered the phrase “until”. Choice (“to the point that”) kept; flagged as a guess already, and listed in cruces. |
| 1602 | n | low | Apparatus misreported: “Kemble and others print ‘wȳs[c]ton’ or ‘wīs[c]ton’”. The apparatus gives Kemble ‘wȳs[c]ton’, Thorpe and Grundtvig ‘wīs[c]ton’. | Attribution corrected. |
| 1605 | i | low | ‘heaþoswāte’ rendered “the blood of the fight”; house `i` (fitt-21 table, 1460) is “blood of battle”. | → “from the blood of battle”. |
| 1612 | i | low | “only the head and the hilt as well” — “only … as well” clashes. | → “only the head, and with it the hilt, bright with treasure”. |
| 1620 | n | low | “‘gefǣlsian’ is the verb of the cleansing of Heorot at 432 and 825”: line 432 has the simple ‘fǣlsian’. | → “at 825, and the simple ‘fǣlsian’ at 432”. |

## Findings considered and refused

- **1599 ‘brimwylf’ `i`** “the she-wolf of the sea” against the conventions table (`i` “sea-she-wolf”): refused — the published fitt-22 `i` at 1506 actually reads “the she-wolf of the sea”, and the draft matches what is published.
- **1585 ‘tō ðæs þe’ = “until” / “to where”** (local reading, Beowulf moving along the wall to where Grendel lay): plausible, but the drafter flagged the choice as a guess and listed it in cruces; not overturned, cross-reference added instead.
- **1568 `l` “she sank to the floor”** vs note “fall, fall dead”: “sank” is within the sense of ‘gecringan’; `i` has “fell dead”. Left.
- **1587 `i` “as the fight at Heorot had left him”** for ‘gescōd’ “harmed”: “left him” (lifeless) carries the result of the harm in idiom. Left.
- **1604 `i` “again”** with no ‘eft’ in the clause: “see … himself” = alive; “again” is idiomatic support, not an addition of sense. Left.
- **1604 `i` “dear lord”** vs 862 `i` “friend and lord”: no house entry for ‘winedrihten’; both idiomatic. Left.
- **1621 ‘ellorgāst’ = ‘ellorgǣst’ “with the other vowel”**: whether ‘-gǣst’ is ‘gāst’ or ‘gæst’ (guest) is disputed, but the note follows the treatment of the published parts (both rendered “elsewhere-ghost”). Left.
- **1649 ‘mid’ an adverb**: could be a postposed preposition governing ‘þǣre idese’ (“and with the lady”); the adverb reading is the one the note takes and the sense is the same. Left.
- **1641 `i` “came marching”** for ‘gongan’: “marching” suits ‘fyrdhwate’; sense not distorted. Left.
- **1639 note closer** “The size of the head matches the size of the giants’ sword”: a concrete narrative point, not an atmospheric closer. Left.
- **1600 ‘Næs’ “the plural verb and the sense decide it”**: loosely put (the point is that ‘ofgēafon’ needs an object), but not false. Left.
- **1580 note: 15 + 15 = the thirty of 123**: commentary, checked against line 123 (‘þrītig þegna’). Left.
- **1584 `l`/`i` vs 114** (“He paid them the reward for that” / “repaid them what they had earned”): consistent. No change.
- **All other line cross-references** (15, 110, 112, 113, 114, 122, 123, 194, 201, 249, 261, 312, 383, 386, 625, 673, 714, 807, 825, 833–835, 850–851, 862, 1033, 1171, 1349, 1373, 1397, 1460, 1476, 1492, 1495, 1504, 1506, 1517, 1521, 1527, 1531, 1540, 1555) verified against the source: correct.
- **Apparatus claims** (1558, 1559, 1565 fol. 164b AB, 1591 fol. 165a, 1599, 1602, 1610, 1616 fol. 165b AB, 1617, 1619, 1624–25, 1634, 1640 fol. 166a, 1644, 1650): correct apart from 1604 (fixed above).
- **Verb parses** (gefēng, gebrægd, grāpode, ðurhwōd, gecrong, gefeh, līxte, wlāt, hwearf, hafenade, sprong, þrōwade, becearf, gemealt, forbarn, swealt, þurhdēaf, oflēt, gefēgon, ālȳsed, mǣton, bǣron, træd, gewurþad) and case labels: all true of the forms in their lines.

# Pass 2 (adversarial)

Scope: all 34 units again, after pass 1's edits, in the order: note grammar against the line; OE → `l` word by word;
`l` ↔ `i`; remembered English in `i`; consistency with the published parts (grep of the root `beowulf-*.json`).
Then every entry of `gloss.json` (143 new keys + 14 `__broaden__`) against each line where its form occurs.
Pass 1's edits re-checked: ‘seasons and times’ (1607) agrees across `l`/`i`/`n`; ‘elsewhere-ghost’ / ‘spirit from
elsewhere’ agrees across the 1615 and 1620 units and with 805/1345; 1572, 1584, 1602, 1605, 1612, 1620 edits sound.
Edits by script; `t`, `ln`, `v`, `p` untouched and `i` present on every unit (checked against a copy taken before
editing). Gloss keys = `novel-forms.json` exactly; no new key is already in `beowulf-glossary.json`; every
`__broaden__` value begins with the published entry whole, then “ · ”.

Severity count — **text: high 0 · medium 0 · low 1** · **gloss: high 0 · medium 5 · low 13** (19 entries changed; lāc and lāðlicu share one row).

## Changes — text

| line | field | sev. | what was wrong | what done |
|---|---|---|---|---|
| 1567 | n | low | ‘fǣge’ “the word used of the sword’s old victims at 1527”: in this unit “the sword” is the giant sword; 1527 (‘fǣges fyrdhrægl’) is about Hrunting. | → “the word used at 1527 of the doomed men whose war-gear Hrunting had cut”. |

## Changes — gloss

| entry | sev. | what was wrong | what done |
|---|---|---|---|
| fāge | medium | Parsed “dative singular neuter, agreeing with since”: ‘since’ is the dative; ‘fāge’ agrees with ‘þā hilt’ (so the unit note). | → accusative plural agreeing with þā hilt; since an instrumental dative. |
| hilt | medium | “neuter, accusative singular”: with the neuter noun (‘þæt hilt’ elsewhere) ‘þā hilt’ is plural, as the 1572 and 1612 notes say. | → accusative plural with þā, the plural used of a single hilt. |
| meodowongas | medium | “meadow … the floor of the mead-hall”: the word is the open ground about the hall (unit note), and ‘meadow’ (from ‘mǣd’) is unrelated. | → “mead-plain, the open ground about a mead-hall … not related to ‘meadow’”. |
| fāg (broaden, new part) | medium | “nominative singular neuter, agreeing with lagu”: ‘lagu’ is masculine (the draft’s own ‘lagu’ entry says so); neuter only fits ‘wæter’. | → “nominative singular, agreeing with lagu and wæter”. Old entry untouched. |
| bend | medium | “accusative plural … ‘the bonds of frost’” against the unit’s `l` and note (‘the frost’s bond’, singular; masc. i-stem acc. sg. is ‘bend’). | → “accusative singular or plural; forstes bend ‘the frost’s bond’”. |
| hildegicelum | low | “here” in an entry, and “the sword’s blood dripping”: it is the blade that melts. | → “of a blade melting away like ice”. |
| sǣla | low | “sǣla ond mǣla ‘times and seasons’” left behind by pass 1’s change to “seasons and times”. | Brought in line. |
| lāc, lāðlicu | low | Committed to plural while the unit renders singular and the note allows both. | → plural if neuter, singular if feminine. |
| sētan | low | “Klaeber’s emendation”: the apparatus gives it to Grein (Gr.2), Klaeber prints it. | → “Grein’s emendation, printed by Klaeber”. |
| wīston | low | “wiston ‘knew’ would also fit” contradicts the note (it clashes with ‘ne wēndon’). | → “some take the form as wiston ‘knew’”. |
| fracod | low | ‘hilderince’ called a dative of respect; it is the dative of the person. | → “with a dative of the person”. |
| mægenbyrþenne | low | “the ending is irregular”: ‘-byrþenne’ is the regular gen./dat. sg. of a feminine ō-stem. | Removed; → “with gefeah, in apposition to sǣlāce”. |
| snottre | low | “cf. ‘snotty’ in the older sense ‘clever’”: no such sense or link. | cf. removed. |
| eardas | low | “cf. ‘earth’”: ‘eard’ and ‘eorþe’ are different words. | cf. removed. |
| lagu | low | “cf. ‘lake’”: ‘lake’ is from Latin ‘lacus’. | cf. removed. |
| gesceaft | low | “cf. ‘shaft’ in the sense of what is shaped”: false link. | → “related to scieppan ‘shape, create’”. |
| geworhte (broaden, new part) | low | “the relative clause with a past subject”: meaningless. | → “in a relative clause: ðāra þe hē geworhte ‘of those that he wrought’”. |
| wrǣtlīc (broaden, new part) | low | “neuter, in apposition to wlitesēon”: it is attributive, and ‘wlitesēon’ is feminine (the draft’s own entry). | → “nominative singular feminine, agreeing with wlitesēon”. |

## Findings considered and refused

- **‘ellorgǣst’ gloss “alien spirit”** while pass 1 removed “alien” from `l`/`i`: the published glossary entries ‘ellorgāst’ and ‘ellorgǣstas’ both lead with “alien spirit”; the draft entry matches the shared glossary, which may not be rewritten. Left.
- **`hafað` broaden contains “here”**: the word is in the published old entry, which must be kept whole. Left.
- **Pronouns for God uncapitalised in 1607 (“he who has power”, “he is the true Lord”)**: the published parts are mixed (“He” at 109/1057, “he”/“his” at 316 and 955 `l`). No house rule. Left.
- **British spellings (honour, armour, labour, coloured)**: the published parts mix both (honour ×14 / honor ×39; armour in fitt-22). No rule. Left.
- **1607 `n` “Metod … met first at 110”**: line 110 is the first ‘Metod’ (the unit starts at 109). Correct.
- **‘hrā’ “cf. ‘raw’”, ‘frome’ “cf. ‘frim’”, ‘offerede’ “the reading is Klaeber’s”**: loose or vacuous but not false enough to change. Left.
- **‘forbarn’ lemma ‘forbyrnan’ (gloss) vs ‘forbeornan’ (note)**: two spellings of one verb. Left.
- **Multi-occurrence forms** (bil, monige, slōh, būton, eal ×4, hēafod ×2, tō ×7): each occurrence is covered by the new or old parts of the entry. No change.
- **All other text** (grammar labels, OE → `l`, `l` ↔ `i`, cross-references 15–1556, apparatus claims, house renderings Higelāces þegn, heorðgenēatas, goldwine gumena, winedrihten, holmclif, hringmǣl, tō þæs þe at 714, Metod = Measurer/Lord): checked, no further error found.
