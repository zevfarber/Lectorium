# iliad-003 (Iliad 1.206–311): review

Reviewer pass 1 (every grammatical label and cross-reference in every note checked against the line; Greek → `l` word by word; `l` ↔ `i`; remembered English; quotation marks, `mark` and `p`; house tables; new-renderings rows) and pass 2 (the whole file re-read after the edits, and `gloss.json` checked parse by parse against the lines). Sources used: the Greek, the Iliad and Odyssey conventions and house tables, the published Odyssey units, `iliad-001.json` and `iliad-002.json` as English precedent (every unit was run against all of them for shared words and clauses, since the packet lists only whole-line matches). No modern translation consulted or recalled. `units.json` edited in place by script; `t` untouched (checked: every `t` identical to the pre-review file, and the units still concatenate to the packet's 106 lines, 800 words). `gloss.json` existed at pass two and was corrected in place.

Counts, `units.json` (and its `about`): 23 changes (2 high, 11 medium, 10 low), touching 34 fields; plus 4 edits to `new-renderings.md`.
Counts, `gloss.json`: 15 changes (1 high, 10 medium, 4 low): 14 entries corrected and 1 missing broadening added.
Total: 38 changes (3 high, 21 medium, 14 low).

Severity: high = identical Greek given different English from a published unit, or a note or gloss that states something false about a form; medium = house-table or Iliad-internal inconsistency, a note contradicting its own `l`/`i`, a wrong claim about what a cross-reference or the poem says, or a gloss that mislabels or omits a use; low = precision, particle force, polish.

## Changes: `units.json`

| line · field | severity | what was wrong | what was done |
|---|---|---|---|
| 297 · l, i, n | high | ἄλλο δέ τοι ἐρέω, σὺ δ’ ἐνὶ φρεσὶ βάλλεο σῇσιν is published four times in the Odyssey (odyssey-055 ln 454, -079 ln 281 and 299, -087 ln 548) as `l` "And another thing to you I will say, and you in your own mind lay it:" / `i` "And I will tell you something else; lay it up in your own mind:". The draft (σῇσι without the ν) renders it afresh ("Another thing I will tell you, and you in your mind put it" / "I will tell you something else, and you lay it up in your mind"). The packet did not list it (whole-line matches only, and the final ν differs). | `l` and `i` replaced by the Odyssey's wording; note says the line is word for word one in the Odyssey (apart from the final ν), and glosses ‘in your own mind’, σός ‘your own’. |
| 308 · n | high | "προέρυσσεν is the imperfect of προερύω". The doubled-σ form is the epic aorist (ἔρυσσα); an imperfect would be εἴρυον. The gloss (aorist) and the note disagreed. | Note: "the aorist (with the epic doubled σ) of προερύω ‘draw forth’". |
| 303 · l, i, n | medium | αἶψά οἱ αἷμα κελαινὸν ἐρωήσει περὶ δουρί is published (odyssey-081 ln 441) as "Quickly his blood, dark, will gush around our spear" / "Quickly his dark blood will gush about our spear"; the house table fixes "quickly" for αἶψα. The draft had "at once", and "about" in `l`, "around" in `i`. | `l` "quickly your dark blood will gush around the spear." `i` "quickly your dark blood will gush about my spear." Note: αἶψα is ‘quickly’. |
| 219 · i | medium | ἦ καί rendered "He spoke, and" in `i`. The Odyssey fixes `i` "So he said, and" for ἦ ῥα καί (8.416; table) and ships it for the bare ἦ καί (odyssey-070 ln 494, -105 ln 431, -106 ln 8). The new-renderings row presented the departure as new. | `i` "So he said, and held …"; `l` ("He spoke, and") already matched; row changed and the precedent named. |
| 245 · l, i, n | medium | ὣς φάτο … ποτὶ δὲ σκῆπτρον βάλε γαίῃ is published of Telemachus (odyssey-005 ln 80) as "down the staff he dashed to the ground" / "dashed the staff to the ground". The draft had "threw" in `l`, "flung" in `i`. | `l` "and down the sceptre he dashed to the ground", `i` "dashed the sceptre to the ground" (σκῆπτρον stays "sceptre", the Iliad's word from iliad-001); note says "‘dashed down’ (the Odyssey has the same clause of Telemachus)". |
| 267 · l | medium | ἐκπάγλως is "terribly" in both layers in the Odyssey (odyssey-025 ln 339, -055 ln 436); the draft's `l` had "terrifyingly" (the row cited only the adjective's "terrifying"). | `l` "terribly"; row rewritten (ἔκπαγλος itself stays "terrifying"). |
| 211 · l, i | medium | ὡς ἔσεταί περ is published (odyssey-104 ln 212) as `l` "just as it will be" / `i` "just as it shall be"; the draft had `l` "as it shall be" / `i` "just as it will be", close to a swap. | `l` "just as it will be", `i` "just as it shall be"; row updated to name the Odyssey unit. |
| 277 · l, n | medium | σκηπτοῦχος βασιλεύς is "sceptre-holding king" in `l` in the Odyssey (odyssey-022 ln 7); the draft had "sceptre-bearing". | `l` and the note's gloss changed to "sceptre-holding" (`i` already "sceptred"). |
| 308 · l | medium | `l` "put" for βῆσε, against its own note ("made go on board") and against iliad-002 ln 142, where βήσομεν is "make go" in `l`. | `l` "made go, for the god,". |
| 223 · n | medium | "λῆγε is the imperfect of λήγω, as at 210": the form at 210 is the imperative (λῆγ’); "as at 210" read as the same form. | Note: "the verb of the command at 210". |
| 237 · n | medium | Note glosses νῦν αὖτε as ‘but now in turn’; `l` is "and now in turn" and the Greek has no ἀλλά: note contradicted its own `l`. | "‘now in turn’". |
| 240 · n | medium | Note glosses ἦ ποτε as ‘surely some day’; `l` has "Truly". | "‘truly some day’" (see also the `i` change below). |
| 212 · n | medium | "the promise Athena is swearing will be fulfilled": she does not swear; the oath is Achilles' at 233. | "What follows, the promise of gifts, is what Athena says will be fulfilled." |
| 277 · i | low | "never has a share of honour equal to other men’s": ὁμοίης has no comparand in the Greek; the English supplied one. | "never has an equal share of honour." |
| 211 · n | low | ὀνείδισον has no object in the Greek; `l` and `i` both supply "him". | One sentence added: the Greek gives no object; ‘him’, Agamemnon, is supplied. |
| 210 · n | low | "since the blade is half out": the poet says only that the sword was being drawn (1.194); "half" is an invention. | "since he has already begun to draw the sword". |
| 228 · n | low | "arming for war and lying in ambush": the Greek is λόχον ἰέναι, "go to an ambush". | "going to an ambush". |
| 229 · i | low | ἦ rendered "Surely" in `i` against "Truly" in `l` and against iliad-002 (ln 154, 169), where the review made ἦ "truly" in `i`. | "Truly it is far better". |
| 232 · l, i | low | ἦ γὰρ ἂν … "for surely / For surely" beside "Truly" at 229 in the same speech. | Both layers "truly". |
| 240 · i | low | "Surely some day" against `l` "Truly" (same particle, same speech). | "Truly some day". |
| 254 · i | low | ὦ πόποι ἦ μέγα: `i` dropped ἦ ("Ah, a great grief"), `l` had "truly". | "Ah, truly a great grief". |
| 247 (Nestor) · l, i, n | low | ἀνόρουσε rendered "stood up"; the Odyssey ships "sprang up" / "started up" / "leapt up" throughout (odyssey-009, -021, -070, -077); the note itself said "sprang up, stood up". | "sprang up" in `l`, `i` and the note. |
| about · | low | "Agamemnon will tear his heart out": ἀμύξεις θυμόν is "tear at your heart" in remorse, not a violent act. | "will tear at his own heart in rage". |

## Changes: `gloss.json`

| form · field | severity | what was wrong | what was done |
|---|---|---|---|
| αἰχμητὴν (290) | high | "predicate accusative with an infinitive": it is the predicate of ἔθεσαν (εἰ δέ μιν αἰχμητὴν ἔθεσαν), not of any infinitive. | "predicate accusative (’made him a spearman’)". |
| ἦ (219, known form) | medium | The known entry has "truly, surely … interrogative"; 219 is ἦ καί, ἦ from ἠμί "he said", a use the entry does not cover and the glosser did not broaden. | `__broaden__` added: old entry whole, then " · also ἠμί — say; impf. 3 sg. ἦ ’he said’, in ἦ καί, ἦ ῥα". |
| ἐστὸν (259) | medium | "3 dual: ’the two are’": the line addresses the two kings, "you two are" (2 dual; the 3 dual is the same form). | "pres. 2 dual (3 dual is the same): ’you two are’". |
| εἵνεκα (214, 298) | medium | "postposed prep.": true at 214, false at 298 (εἵνεκα κούρης precedes its noun). | "prep. + gen., often after its noun". |
| καλέσαντο (270) | medium | "(-αντο for -αν)": the aorist middle 3 pl. ends in -αντο regularly; nothing is substituted. | Phrase removed. |
| σχέθε (219) | medium | "root aorist (= ἔσχε)": σχέθον is the thematic aorist with epic -θ-, not a root aorist. | Parse corrected. |
| περὶ (236, 258 ×2, 287, 303) | medium | Missing the use at 258 (περὶ … ἐστέ, "surpass", adverb in tmesis with εἰμί). | Added. |
| ἀπίης (270) | medium | Sense stated as fact; the note and new-renderings row say it is uncertain (ancient "far-off", "Apian" the other view); the glossary rule is that an uncertain word says so. | "(ancient explanation; sense uncertain, ’Apian’ is another view)". |
| ἀταρτηροῖς (223) | medium | "harsh, grievous, baleful" stated as fact; the word is rare, origin unknown, ancient gloss "harmful, mischievous". | "harsh, harmful, mischievous (ancient gloss; meaning uncertain, origin unknown)". |
| ὀρεσκῴοισι (268) | medium | "mountain-dwelling" stated as fact; the unit's `l` is "mountain-bedded" and the row says the explanation is traditional. | "lying on the mountains, of the mountains (traditional explanation; meaning uncertain)". |
| φηρσὶν (268) | medium | "centaur": the Greek does not name the Centaurs (the unit's note and row say so). | "wild beast (Aeolic form of θήρ); in Homer used of the Centaurs". |
| χαλκὸς (236) | low | "here also the bronze blade": "here" is forbidden in an entry. | "also a bronze blade". |
| πειρίθοόν (263) | low | "Pirithous" against the house spelling "Peirithous" in both layers (Odyssey table). | Spelling conformed. |
| κεχολωμένον (217) | low | "agreeing with an unexpressed ’me’": the unexpressed subject of the infinitive is general ("one"), Achilles speaking of himself. | "agreeing with the unexpressed subject of an infinitive". |
| ἐΐσας (306) | low | Meaning given without the uncertainty that the note records for ships. | "(of ships, sense uncertain)"; "trim" dropped. |

All other 323 entries (including the 16 other broadenings, each checked to be the old entry whole plus " · " and the new reading) were checked against every line they occur in and left unchanged. Format checks passed: every entry under 230 characters, typographic ’ only, no line numbers, no "here" (after the χαλκὸς fix; "this here" in the ὅδε entries is the dictionary gloss of ὅδε).

## new-renderings.md
- ἦ καί: `i` column now "So he said, and", with the Odyssey precedent named.
- ἀταρτηροῖς ἐπέεσσιν: added that the Odyssey ships "reckless" for the vocative ἀταρτηρέ of a man (odyssey-007), a different use, so it is not carried over.
- ἐκπάγλως: `l` now "terribly", with the Odyssey units named and "terrifyingly" listed as avoided.
- ὡς ἔσεταί περ: columns changed to the Odyssey's wording (odyssey-104), noted.
- Checked every other row against the units: all match.

## Checked and found correct (no change)
- `t`/packet identity; `ln` of every unit (including units that begin mid-line: 208, 247, 271, 282, 308); `p` on exactly the eight ¶ lines (206, 215, 219, 223, 245, 285, 292, 304); the six speeches (Athena 207–214, Achilles 216–218, Achilles 225–244, Nestor 254–284, Agamemnon 286–291, Achilles 293–303): `mark` on the first unit of each, “ on that unit and ” on the last in both `l` and `i`, no quotation marks elsewhere, `l` line division equals `t` line division in every unit; iliad-002's last unit (1.205) ends with ”, so this part opens outside a speech, and it ends (311) outside a speech.
- Notes: all 69 within the 25–110 word band.
- Packet-flagged lines: none. The scanner also reports spondaic fifths at 216, 226, 232, 250 and 291 (regular, not flagged by the packet) and routine licences; nothing irregular, so no note needed adding.
- Whole-line repeats in the packet (206 = odyssey-064 / -002 etc., 209 = iliad-002 ln 195, 212 = odyssey-105, 253 = iliad-001 ln 73, 285 = iliad-002 ln 130) are exact; 215 and 292 follow the reply-formula rows; "Greeks" is absent from both layers; Achaeans/Danaans/Argives used consistently; γέρας "prize" / "prize of honour" at 276.
- Grammar labels in every note checked against the line, including παύσουσα, πίθηαι, πρὸ … ἧκε, ἕλκεο, ἴσχεο, εἰρύσσασθαι, κεχολωμένον, ἔκλυον (gnomic), βεβήκει, θωρηχθῆναι, τέτληκας, λωβήσαιο, φύσει/λέλοιπεν/ἀναθηλήσει, εἰρύαται, ἀμύξεις, ἐφθίαθ’, τράφεν, γηθήσαι/κεχαροίατο/πυθοίατο, the dual forms at 257–259 and 304, ξύνιεν, μαχέοιτο, ἔμμορε, γείνατο, ἐθέλει with four infinitives, ὀΐω with the future infinitive, ἀφέλεσθε/δόντες, φέροις/ἀνελών, ἐρωήσει, προέρυσσεν (now aorist), βῆσε, εἷσεν; line-position claims (210 vs 224 λῆγε; the "next unit/line" statements at 247, 259, 286, 306) and cross-references (195, 196, 103, 204, 210, 25, 73, 130, 159, 203, 217, 231, 233, 251, 266, 207) all true.

## Considered and refused
- **ἦ γάρ κεν … at 293: `i` drops ἦ and γάρ** ("I should be called miserable and worthless"): kept; the force is carried by the conditional and the speech opening, as with γάρ dropped in iliad-002 (123).
- **"But obey me" (259)**: the `l` has no "me"; kept, since the pronoun is supplied from Nestor's speaking and the next lines (273) say "my word".
- **ὀνείδεα "reproaches" in `l`, "insults" in `i` (290)**: kept; the Odyssey itself uses both for the word (odyssey-029, -086).
- **ἐριζέμεναι "strive" against the Odyssey's "vie"**: kept; the Odyssey's "vie" is for contests of skill, here the verb is quarrelling with a ruler, and "strife" is already fixed for ἔρις at 210.
- **"leaves and branches … will put forth" (234, `l`): "leaves" could read as a verb**: kept; the following "will put forth" settles it and `i` has the same noun.
- **ναὶ δὴ ταῦτά γε … without "at least" (286)**: the Odyssey's own units differ (odyssey-016 and -089 keep "at least", -098 does not); this follows -098.
- **ὀΐω "I think" (289, 296)**: kept; the Odyssey table's "I suppose / I suspect" is for specific lines (22.140–165), and iliad-001/002 and the Odyssey units use "think".
- **ἀθερίζω "slight" against the Odyssey's "make light of" (261)**: kept; different context (a statement about being treated with respect) and no shared clause.
- **"sceptre" against the Odyssey's "staff" (245)**: kept; the Iliad's σκῆπτρον is "sceptre" from iliad-001 and the table; only the verb was conformed.
- **ἀταρτηροῖς "harsh" against the Odyssey's "reckless"**: kept; "reckless" fits a person, not words, and the row now records the reason.
- **"the lack of Achilles" (240)**: kept (table row ποθή); it is built from the Greek's noun, not a remembered phrase.
- **"bulwark" (284 `i`)**: kept; an `i` choice for ἕρκος that the row records, built from the sense of the noun.
- **δειλός "miserable" with the note "‘cowardly’ is also in play" (293)**: kept; the Odyssey table fixes "miserable" and bars "cowards"; the note discusses the sense, not the rendering.
- **"grieving as you may" (241 `i`)** for ἀχνύμενός περ: kept; the concessive περ is carried.
- **`i` omits "too" for καί at 249 and drops "indeed" at 211**: particle force carried by word order; no change in sense.
- **"had not yet ceased" (`i`) against "not yet ceased" (`l`) at 224**: kept; both read the imperfect as a state.
- **Glossary "drunkard" for οἰνοβαρής, "cowardly, wretched" for δειλός, "Greeks" in the Ἀχαιοί/Ἀχιλλεύς entries**: kept; the glossary is lexical, the existing entries use these words, and the avoidance of "drunkard", "cowards" and "Greeks" applies to the translation layers.
- **οἷον "masc. acc. sg." (263)**: kept; the standard analysis (agreeing with the first name of the list), and the note says it introduces the names.
