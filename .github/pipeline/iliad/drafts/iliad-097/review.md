# Review — iliad-097 (Iliad 15.559–652)

Reviewer: adversarial, two passes. Pass 1 read `units.json` against `packet.md`, the Iliad and Odyssey house-renderings tables, `new-renderings.md`, the neighbouring part (iliad-096, last unit) and the published Iliad/Odyssey units that share phrases with this part (checked mechanically by three-word overlap). Pass 2 read `gloss.json` against `units.json`, `novel-forms.json` and `known-forms.json`. `t` was never touched (checked by script: all 50 `t` fields identical before and after, and joined they equal the packet's 94 lines; every `ln` checked against the packet).

Severity scale: **major** = wrong text, wrong sense, or a rule broken in a way the build would publish; **moderate** = a false statement in a note or gloss, or a departure from the table or from published English; **minor** = consistency, wording, or an overclaim with no effect on the reading.

Counts: major 0 · moderate 11 · minor 16 · total 27 (pass 1: 6 moderate, 6 minor; pass 2: 5 moderate, 10 minor).

Checks that found nothing to change: all repeated lines in the packet (559, 562, 590, 591, 596, 622, 629) carry the published `l` and `i` word for word in the places the packet shows; quotation marks (Ajax 561–564, Menelaus 569–571: “ on first unit, ” on last, `mark` on both first units, no stray marks; the speech Hector ends in 096 closes there); `p` on the four ¶ units (559, 565, 572, 592); `v` on all; `l` line division follows `t` in all 50 units; no newline in any `i`; no ASCII apostrophes. No scansion flags in the packet, so no line needed a hand scan. The echoes of Iliad 4 (4.461, 4.496–498), 5.530–532, 14.17 and 4.482–483 were looked up in the published parts and the cross-references in the notes are right (4.496–497, 4.497–498 are correct as written).

## Pass 1 — units.json

| line · field | severity | what was wrong | what was done |
|---|---|---|---|
| (whole part) · `about` | moderate | Said the Argives fence the ships "with a bronze line" (the Greek and the unit say fence/bulwark); said the beast "killed a herdsman’s dog" (587: killed a dog or a cowherd); and lumped the rock, wave and lion similes together as if the Achaean line were all three (the line is the rock; Hector is the wave and the lion). | Rewrote the summary: "bronze bulwark"; "a dog or a herdsman"; the line stands like a rock, Hector falls on it like a wave on a ship and like a lion among cattle. |
| 579 · `n` | moderate | Called βλημένῳ a "perfect passive participle of βάλλω". It is the epic syncopated aorist middle participle (βλήμενος), passive in sense; the published notes (iliad-051, -065, -096) say so. | Label corrected: "the epic aorist middle participle of βάλλω, passive in sense". |
| 601 · `n` | moderate | Cited the form as "ἔμελλε"; the line has the unaugmented μέλλε. | Now "μέλλε (the unaugmented ἔμελλε) with the future infinitives …". |
| 612 · `n` | moderate | Cross-reference "as with ἔμελλε at 601" is false for the same reason (601 has μέλλε, 612 has ἔμελλεν). | Now "as with μέλλε at 601, which has no augment". |
| 618 · `l` | moderate | πυργηδόν rendered "tower-like"; the table row (13.152) fixes "tower-fashion" in `l` ("tower-like mass" is among the avoided renderings of 12.43). | `l` now "tower-fashion". |
| 618 · `l`, `i` | moderate | λιγέων ἀνέμων λαιψηρὰ κέλευθα rendered "the swift paths"; the table reserves "swift" for θοός/ὠκύς and gives λαιψηρά "quick", κέλευθα "ways"; the same phrase is published at 14.17 (iliad-086) as "the quick ways of the clear winds" / "… clear-sounding winds". | `l` "the quick ways of the clear winds"; `i` "the quick ways of the clear-sounding winds". |
| 623 · `n` | minor | Said ἀνεμοτρεφές "is a compound whose meaning is not known". The parts are plain (ἄνεμος + τρέφω) and the sense for a wave is clear; the table’s "meaning not known" belongs to the spear at 11.256 (iliad-066 says so in those terms). | Note now gives the formation and says the wave is one the wind has fed. The `l`/`i` "wind-nurtured" are unchanged. |
| 647 · `n` | minor | "σμερδαλέον ‘terribly’ is also as there" after "as at 608": πήληξ is at 608 but σμερδαλέον is at 609. | Now "as at 609". |
| 578 · `l` | minor | The repeated half-line δούπησεν δὲ πεσών is "he fell with a thud" at 4.504, 5.42, 5.540 and (as δούπησεν δὲ πεσών alone) 5.617 (iliad-026, -027, -032); `l` here read "And he thudded as he fell". | `l` now "And he fell with a thud," (`i` already agreed). |
| 585 · `l`, `i` | minor | οὐ μεῖνε θοός περ ἐὼν πολεμιστής is published at iliad-032 (5.571) as "did not stand fast" (`l`) and "did not hold his ground" (`i`); this unit had "did not stand his ground" in both. | `l` "did not stand fast"; `i` "did not hold his ground". |
| 582 · `i` | minor | τεύχεα συλήσων is published (iliad-032) as "to strip the armour"; `i` had "to strip off your armour". | `i` "to strip your armour". |
| 575 · `n` | minor | "Melanippus is the man Hector rallied" — iliad-096 says Hector rebuked him (ἐνένιπεν). | "rebuked in the last part". |

## Pass 1 — findings considered and refused

| line · field | finding | why refused |
|---|---|---|
| 565 · `i` | "already eager" for οἳ δὲ καὶ αὐτοὶ … μενέαινον drops "themselves" of `l`. | The note states the reading (they were eager before Ajax spoke); "already" is the one-word English for καὶ αὐτοί there and matches the choice at 604 (καὶ αὐτόν "already himself"). |
| 610 · `i` | "so many more men" overstates πλεόνεσσι "more men". | Bare "more men" is not English after "alone as he was"; the Greek sets Hector alone against more men, and the note says so. |
| 607 · `i` | "Foam gathered about his mouth" may be a remembered phrase, and "gathered" is not in γίγνετο. | I could not trace it to any one translation; `l` keeps the literal "a foaming came about his mouth", and the choice is in `new-renderings.md` with its reasons. Left for the owner’s verdict; a literal alternative is "Foam formed about his mouth". |
| 585 · `n` | "take fright, flee in fear" as the gloss of ἔτρεσε sits uneasily with the new rendering (which avoids "fled"). | It is a dictionary gloss, not a translation, and the unit’s `l`/`i` use "took fright" at 586, 589 and 636. |
| 618 · `n` | Names the subject of ἴσχον "the Achaeans" while 622 names the Danaans. | The Greek names no one at 618; both are the same army and the note is not wrong. |
| 641–643 · `n` | Note says ἐτέτυκτο is ‘he had been made’, `l`/`i` say "he was made". | Within a narrative of what he was, "was made" is the pluperfect of a state; no reader is misled. |
| 636–638 · segmentation | Unit 41 ends at a comma (πάντες,). | Allowed by the segmentation rule: the sentence ὣς τότ’ Ἀχαιοὶ … Ἡρακληείῃ runs five lines. |
| 652 · gloss/note | χραισμεῖν called an "aorist infinitive" in the known-forms entry; χραισμεῖν can also be the present. | Matches the published label (iliad-006, 6.587); the form is ambiguous and changing one entry would split the glossary. |
| 561 · `i` | "hearts" (plural) for ἐνὶ θυμῷ against `l` "heart". | Distributive plural after "your"; English requires it and the sense is the same. |
| 589 · `i` | "the son of Nestor" where the table row Νεστορίδης (6.33) has "son of Nestor". | The article is the English subject-noun form; the sense and word are the table’s. |

## Pass 2 — gloss.json

Mechanical checks: every one of the 85 novel forms has an entry and there are no extras; every `__broaden__` key is in `known-forms.json` and each broadened entry begins with the existing entry whole; no novel entry is 230 characters or longer; typographic ’ only; no line numbers and no "here". The 403 known forms were read against their uses in this part.

| key · field | severity | what was wrong | what was done |
|---|---|---|---|
| βλημένῳ | moderate | "perf. part. pass. … (= Attic βεβλημένος)": it is the aorist middle participle with passive sense (βλήμενος), and the published glossary entries for βλήμενος/βλήμενον say so. | Entry now "aor. part. mid. in form with passive sense, masc. dat. sg., epic syncopated βλήμενος (= Attic βληθείς)". |
| κύματά | moderate | Parsed "neut. nom. pl."; in κύματά τε τροφόεντα it is the object of μένει, so accusative (nom./acc. are identical). | "neut. nom./acc. pl.". |
| ἔδει | moderate | Parsed "impf. 3 sg." and glossed ’devoured’; in the lion simile (βοῦν ἔδει, between the presents ὁμοστιχάει and the aorist ὑπέτρεσαν) it is the present, as the unit’s `l`/`i` ("devours") take it. | "pres. 3 sg., epic (= Attic ἐσθίει), in a simile: ’eats, devours’". |
| __broaden__ μένε | moderate | The added reading said "elided (μένε = ἔμενε)": μένε in τὸ γὰρ μένε is the unaugmented imperfect, not an elision. | "elided" removed from the added reading. |
| __broaden__ πλεῖστον (added) | moderate | The known entry covers only the adverb ’most, above all’; at 616 πλεῖστον is masc. acc. sg. agreeing with ὅμιλον (’the thickest throng’). The glosser did not broaden it. | Added to `__broaden__`: the old entry whole + " · also masc. acc. sg., agreeing with ὅμιλον: ’thickest, greatest’ (πλεῖστον ὅμιλον ’the thickest throng’)". |
| πάλτο | minor | Entry pinned to the passage ("of a man thrown off balance") and silent that the sense is disputed. | Rewritten: ’swung, was flung’; of a man at a shield’s rim ’stumbled’ (sense disputed). |
| βλοσυρῇσιν | minor | Gave "grim, fierce, shaggy" without saying the meaning is uncertain (the conventions require it, and the note and the table say so). | "grim (sense uncertain; also glossed fierce, shaggy)". |
| ἀπαίνυτο | minor | Named an Attic equivalent "ἀπήνυτο" that does not exist. | Replaced by "unaugmented epic form (no Attic equivalent)". |
| ἐπικρήνειε | minor | The Attic equivalent was garbled ("ἐπικράναι-"). | "epic -ήν- (Attic -άν-)". |
| ἐτύχησε | minor | "(+ gen.)" only; in the line (τόν … ἐτύχησε) the object is accusative. | "+ gen. or acc.". |
| ἐξάλμενος | minor | Translation ’leaping out’ for an aorist participle. | ’having leapt out’. |
| θορόντα | minor | "(= Attic θορόντα)" names an equivalent identical to the form. | Removed. |
| __broaden__ λαιψηρὰ | minor | Added reading gave ’swift (paths)’; the table’s word is "quick" and "swift" is reserved (and the unit now reads "quick ways"). | ’quick (ways)’. |
| __broaden__ ἄριστα | minor | Added reading gave ’the finest (armour)’; `l` is "best armour". | ’the best (armour)’. |
| __broaden__ θηρὶ (added) | minor | The known entry reads "after ἐοικώς: ’to a beast’"; at 633 θηρὶ is the dative with μαχέσσασθαι. | Added to `__broaden__`: old entry whole + " · also masc. dat. sg., with μαχέσσασθαι: ’with a beast’". |

### Pass 2 — findings considered and refused

| key | finding | why refused |
|---|---|---|
| κτεῖν | Parsed "aor. 3 sg."; κτεῖνε could equally be the imperfect. | The two coincide in form; the line is narrative and "killed" is the sense either way. |
| ὑφ | Known entry gives ’under’ for ὑφ’ Ἕκτορι; this is the dative of agent after ἐφόβηθεν. | The literal ’under’ is the sense `l` uses ("under Hector"); the agent reading is already in the broadened ὑπὸ entry and the unit note explains it. |
| χραισμεῖν | "aor. inf." (see pass 1). | Same reason. |
| ἀήτη | "(= Attic ἀήτης)" is the same spelling but for the final ς. | It is the form the edition prints and the point is the missing ς; the entry says "epic form in -η". |
| βαθέης, μέσσῃσιν, μόρσιμον, ἐβάλοντο, ἐμβάλοι, ἰδέσθαι, ὑπαί, μάχεσθαι, τῇ, ὑπὸ, ἀρὴν | Broadened readings checked against the lines (ὕλης, ἐν μέσσῃσιν ὀρούσας, μόρσιμον ἦμαρ, ἐν θυμῷ … ἐβάλοντο, ἵνα … ἐμβάλοι, μένε … ἰδέσθαι, ὑπαὶ νεφέων, ἄλκιμος … μάχεσθαι, τῇ … ἐνί, ὑπὸ … βίηφιν, Θέτιδος … ἀρήν). | All true of the line; no change. |

## Notable for the LOG

- No scansion flags in the packet; nothing hand-scanned.
- Several repeats checked beyond the packet’s list: the half-lines shared with Iliad 4.496–498 (Odysseus’ cast), 4.461/4.504 (death formulae), 5.530–532, 13.152/14.17 (πυργηδόν, "quick ways of the clear-sounding winds"), 15.589–590; the English of this part now agrees with the published wording at each.
- Two house-table departures corrected (πυργηδόν "tower-fashion"; λαιψηρά "quick"); no new departures from the Odyssey table remain.
- The `about` summary had three factual slips (fixed).
- Left for the owner: "Foam gathered about his mouth" (607), which might be a remembered phrase.
