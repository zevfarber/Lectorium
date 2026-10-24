# iliad-061 (Iliad 10.295–389) — review

## Pass 1

Units only (no `gloss.json` yet). Edits were made by script on `units.json`; `t` was not touched (checked: every unit's `t` is identical before and after, and the words of all units joined equal the edition's lines 295–389). Unit count stays 56. Lines below are the line the unit starts on.

Checks run: grammatical labels and positional claims in every note against the line; cross-references against the edition and the published files (2.55, 1.43, 1.234, 5.119, 6.47–50, 10.83, 10.147, 10.220, 10.343, Odyssey 13.32, 20.291, 22.392: all exist and say what the notes say); `p` against the edition's paragraph marks (295, 299, 313, 328, 332, 349, 372, 382: all correct, none missing); `ln` and the "begins/ends in the middle of line N" claims; `l` and `t` line counts equal in every unit; quotation marks (7 speeches: 303 Hector, 319 Dolon, 329 Hector, 341 Odysseus, 370 Diomedes, 378 Dolon, 383 Odysseus; 7 openings and 7 closings in each layer, `mark` on the first unit of each; the previous part ends with Diomedes' closing mark, and iliad-062 opens with narrative at 10.390); note length (all 34–92 words, none with a backtick); repeated lines against the packet (10.302, 313, 382, 384 are word for word the published `l` and `i`; 10.327, 379, 381 and 386 reuse the published wording, see 385 below); the house table checked word by word; the draft's `new-renderings.md` against the table. Scansion flags: none, so no hand scan.

## Changes

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 321 | `i` | major | ἅλιος σκοπός was "a scout in vain". The table fixes σκοπός as "lookout" in both layers (2.792) and reserves "scout" for ἐπίσκοπος (10.38; the same part has ἐπίσκοπος "scout" at 341), so two Greek words got one English word. | `i`: "a lookout in vain". `l` already had "lookout". |
| 370 | `l`, `i`, `n` | major | κιχήσομαι (κιχάνω) was "overtake" / "catch". The table's κιχάνω is "reach" (3.290, 5.187, 6.228), and 6.228 turns down "overtake" and "catch up with" by name. | `l`: "I shall reach you"; `i`: "I shall reach you with my spear"; note: "‘reach, overtake’" became "‘reach’". |
| 376 (unit τὼ δ’ ἀσθμαίνοντε) | `l`, `i`, `n` | major | κιχήτην (same verb) was "came up with" / "came up with him", the other rendering the table turns down. Also `i` began with a capital after a semicolon. | `l`: "reached him"; `i`: "the two reached him, panting, and took hold of his hands;" (lower case); note: "‘reached, came up with (him)’" became "‘reached (him)’". |
| 376 (unit χλωρὸς ὑπαὶ δείους) | `n` | major | Note said the unit "begins in the middle of line 376". It is the first words of 376 (the dot at the end of 375 closes the previous unit). A false positional claim. | Note now says "The unit is the first words of line 376, to the raised dot." |
| 321 | `n` | moderate | ἀνάσχεο was glossed "(the sceptre of the speaker, as in an oath)". The speaker is Dolon; the sceptre is Hector's, held by the one who swears (as the next unit says). | "(Hector is to hold up the sceptre while he swears)". |
| 365 | `i`, `n` | moderate | ἐπευξάμενος was "vaunt" in `i`. The table's `i` for this verb in a taunt is "cries out in triumph" (5.119) and "in triumph" (Odyssey 22.286); "vaunt" is the `l` word. | `i`: "could be first to cry out in triumph that he had struck the man"; note adds that this is the free English. `l` ("vaunt") kept. |
| 325 | `i` | minor | που was "surely" in `i`, "presumably" in `l`; "surely" asserts more than the Greek. | `i`: "are presumably about to take counsel". The last line of the unit keeps the English of 10.147 otherwise. |
| 344 | `i` | minor | `i` began with a lower-case "but" after the full stop that ends the previous unit. | "But let us first let him go past us a little way across the plain;". |
| 385 | `i` | minor | The second line is 10.83, published in iliad-058 as "in the murky night, when other mortals sleep"; the unit had "through the murky night" and its note says it takes the English of that line. (The packet's rule is the published wording as far as the sentence allows.) | `i`: "in the murky night when other mortals sleep". `l` already identical to the published `l`. |
| 351 | `n` | minor | "ends at the raised dot, in the middle of line 352": ἡμιόνων· is the first word of 352. | "after the first word of line 352". |
| 303 | `n` | minor | "the line above the unit names him" (the speaker is named in the previous unit, 302, not in a line "above"). | "the unit before it names him". |

## Findings considered and refused

| Where | Finding | Why refused |
|---|---|---|
| 299, ἀγήνορας "manly" / "proud" | Departs from the Odyssey's "lordly" (μνηστῆρες ἀγήνορες). | The Iliad table fixes ἀγήνωρ as "manly" / "proud" (9.699 and θυμὸς ἀγήνωρ at 10.220, published); the departure is recorded in `new-renderings.md`. Kept. |
| 314, "a divine herald" (`l`) against "the divine herald" (`i`) | Article differs between the layers. | The table's Ταλθύβιον θεῖον κήρυκα is "the divine herald" in `i`; `l` is literal. The Greek has no article either way. Kept. |
| 314/318, ῥα τότε "then" in `l`, "now" in `i` | Force of τότε. | Idiomatic in `i`; τότε still reads as the point in the story. Kept. |
| 302, 313, 382, 384 and Odyssey-shared lines | Compared `l` and `i` letter for letter with the published units. | All identical (302 to 2.55, 313 to 3.95, 382 to the Odyssey, 384 to Odyssey 1.169). No change. |
| 313 `i`/`l` end in ";" though `t` ends in "." and 302/318 etc. end in ":" | Punctuation differs from `t`. | Required by the validator's repeat rule (published strings exactly); the note on 313 already says so. Units 3, 49 and 51 likewise. |
| 336 `i`, "he was never to come back" | "never" for οὐδ’ … ἔμελλεν. | The draft chose it in `new-renderings.md` ("he was never to … carry word"); the note says the line looks ahead to what is fated. Kept. |
| 329 `i`, "ride behind these horses" | ἐποχήσεται is "ride on", with the dative. | In `i` for a chariot team this is the ordinary English and the note gives the literal "ride on". Kept. |
| 363 `i`, "the city-sacker" | Table has "sacker of cities" for Ὀϊλῆϊ πτολιπόρθῳ. | iliad-010 (Ὀδυσσεύς, ὃ πτολίπορθος) and the Odyssey (odyssey-081) use "the city-sacker" for Odysseus; consistency with that is kept. |
| 360–361, καρχαρόδοντε, κεμάς, ἐπείγετον; 365 ἔμελλε; 354 δοῦπον | Checked for conflicts with the table. | None: new rows, or the table's own ("crash"). |
| 321 ἀνάσχεο "hold up" against the table's "hold out" / "bear up" (1.586) | Same verb, different rendering. | Different sense (physical object, the sceptre); the table's 7.412 ἀνέσχεθε "held up" supports it. Recorded in `new-renderings.md`. Kept. |
| 332 ὀροθύνω "roused" against ὄρνυμι "rouse" | Possible overlap with table rows. | ὀροθύνω has no row, and ἀποστρέψοντας, δουρηνεκές and λαιψηρά (355–358) have none either; "roused" is the verb's plain meaning and the unit's context (Hector rouses Dolon) differs from every ὄρνυμι row. Kept. |
| 380 (in 378–381) | The note says 380 is 6.49 "with ὔμμιν for τοι". | True (checked against the edition: τῶν κέν τοι at 6.49, τῶν κ’ ὔμμιν here), and the English is the published `l`/`i`. No change. |
| 389 note, "Dolon's answer opens the next part" | Cross-reference to an undrafted part. | True of the edition: 10.390 is "τὸν δ’ ἠμείβετ’ ἔπειτα Δόλων" and iliad-062 starts at 10.390. Kept. |

## For the drafter's `new-renderings.md` (not edited by the reviewer)

Two rows no longer match `units.json` after the fixes above: κιχάνω ("overtake" / "came up with" now "reach"), and ἅλιος σκοπός (`i` now "a lookout in vain"), and ἐπεύχομαι (`i` now "cry out in triumph").

## Counts

Major 4, moderate 2, minor 5 (11 changes in total, 10 units touched).

## Pass 2

`gloss.json` (118 new forms, 16 broadened forms from the glosser, 6 more added here) was checked entry by entry against the line in `units.json` and `packet.md`: lemma, meaning, case, number, gender, tense, mood, voice, the Attic equivalent of each Homeric form, homographs, agreement of the meaning with the English in `l` and `i` and with the house table (`conventions.md` from line 56 and `../odyssey/conventions.md`), and the entry rules (under 230 characters, typographic ’ only, no line numbers, no "here", not pinned to a line). Every text word has an entry (new, known or broadened); the 118 keys equal `novel-forms.json`. All 16 `__broaden__` entries begin with the old entry whole (compared with `known-forms.json`) and each new reading is needed and true to its line. `units.json` was skimmed again (labels in all 56 notes, repeated-unit English, quotation marks, `p`, `mark`): no change needed. `t` untouched.

### Changes to `gloss.json`

| Form | Severity | Was | Now |
|---|---|---|---|
| κιχήτην | major | "come up with, overtake, reach … ’the two came up with (him)’" (both renderings the table turns down; units say "reached him") | "come upon, find, reach … ’the two reached (him)’" |
| ἀνάσχεο (new `__broaden__`) | major | known entry gives only ’endure!’ (1.586); here it is "hold up the sceptre" (the table’s ἀνέχω "hold up", 7.412) and the entry did not cover it | old entry whole + " · also of an object held out, aor. imper. 2 sg. mid.: ’hold up’ (τὸ σκῆπτρον ἀνάσχεο ’hold up the sceptre’)" |
| γίγνετ (new `__broaden__`) | moderate | known entry reads γίγνετ’ only as present γίγνεται; the note and both English layers take it as a past tense (γίγνετο) | old entry whole + " · also impf. 3 sg. mid., elided (γίγνετ’ = γίγνετο): ’came about’ …" |
| βαλέειν (new `__broaden__`) | moderate | known entry "throw, cast, let fall"; 368 is "strike" ("that he had struck") | old entry whole + " · also ’strike, hit’ (ἐπευξάμενος βαλέειν ’vaunting that he had struck’)" |
| ἐΰξου | moderate | "masc. gen. sg." (it agrees with δουρός, neuter δόρυ) | "neut. gen. sg." |
| ἀγαμεμνονέην | moderate | "epic -έην (= Attic -έαν)" (wrong Attic form; the sister entry κτιδέην has -ῆν) | "epic uncontracted -έην (= Attic -ῆν)" |
| οὗτός (`__broaden__`) | minor | second reading quoted ’here is some man’ (the word "here"; the line and `l` say "this is some man") | ’this is some man’ |
| ἔλασσον | minor | "(= Attic ἐλάττων)" (a neuter adverb needs the neuter) | "(= Attic ἔλαττον)" |
| αὐτὸν (new `__broaden__`) | minor | known entry has no plain-pronoun use without a preposition; 345 is "take him" | old entry whole + " · also plain personal pronoun, direct object with no preposition: ’him’ (αὐτὸν ἐπαΐξαντες ἕλοιμεν …)" |
| ἂν (new `__broaden__`) | minor | known entry covers ἂν = ἀνά only before δ’ and in tmesis; 298 is ἂν νέκυας | old entry whole + " · also ἂν = ἀνά before ν, prep. + acc.: ’up through’ (ἂν νέκυας …)" |
| ἂμ (new `__broaden__`) | minor | known entry says ἂμ is assimilated before π only; 298 has ἂμ φόνον | old entry whole + " · also ἂμ before φ, prep. + acc.: ’up through’ (ἂμ φόνον …)" |

### Findings considered and refused

| Where | Finding | Why refused |
|---|---|---|
| __broaden__ entries over 230 characters (μὴ 454, ἔπι 728, νύκτα 542 etc.) | Length rule. | The rule is for new entries; a broadened entry is the old entry whole plus the new reading, and several old entries already exceed 230 (27 in `known-forms.json`, longest 1288). |
| μεμηκώς "bleat (of a deer)" | The hunted animal is "deer or hare". | The bleating belongs to the deer (κεμάς); the note says "the hunted animal" loosely and the entry is true. Kept. |
| ἡγήτορες (known: nom. pl. "subject of ἧντ’") | Pinned to another line. | The parse (nom. pl.) covers 301; the pinning is in an old entry that may not be rewritten. |
| ἡμετέρῃσιν (known: "agreeing with χερσίν") | At 342 it agrees with νήεσσιν. | The case, number, gender and Attic form are right for both uses; not a second reading. |
| δοῦπον (known "thud, booming sound") against `l`/`i` "crash" | Meaning differs from the English. | The table has both "crash" (4.455) and "thud" (9.573); an old entry may not be rewritten and the gloss is not wrong. |
| τὸ (πάρος), τις after μή, ἐπί, ὥς τε, ὑφ’, ἦ, ἤ, ἠὲ, κεν, ὃ before an epithet, χερσί, βοῶν and the other known forms | Checked each known entry against every use in the part. | Each already lists the reading used here (e.g. τὸ πάρος "as before", μή τις "lest any", ὥς τε "like, as", ἦ "or"/interrogative). No broadening needed. |
| δωσέμεν "in the oath", διώκειν "after ὁρμήθησαν", οὖρα "subject of πέλονται" and similar | Entries mention the governing word of this part. | Naming the construction is the house style (known entries do the same), no line number or "here" appears, and the parse is general to the form. Kept. |
| ἐβάλλετο, ἐνώμα, ἐπευξάμενος, βουλεύειν, μὴ, πυθέσθαι, τοῖς, χειρῶν, ἔπι, ἠέ, μέν, ὑπαί, ὅσσόν, ἔλθοι, νύκτα, οὗτός (the glosser’s 16) | Each new reading checked against its line and the English. | All correct (voice, case, construction, meaning agree with `l` and `i`); only οὗτός needed the one fix above. |
| The other 112 new entries | Parse, Attic equivalent, gender, meaning checked. | Correct apart from the five fixes above; meanings agree with the table (ζωγρέω "take alive", λαός "people, army", ἀγήνωρ "manly, proud", ἐπείγω "press hard", νωμάω "wield, ply", φθάνω "be first", ἐπίσκοπος "scout", σκοπός "lookout", κιχάνω "reach" after the fix). |
| units.json second skim | Labels in the notes, repeated-unit English, quote marks. | No error found beyond pass 1 (γίγνετ’ as an imperfect in the note at 375 is now supported by the glossary). |

### Counts (pass 2)

Major 2, moderate 3, minor 6 (11 changes, all in `gloss.json`; `units.json` unchanged).
