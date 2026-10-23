# iliad-051 (8.469–565) — review, pass 1 (units.json)

Method: every note checked label by label against its line; Greek to `l` word by word; `l` to `i`; the English
checked against the house-renderings tables (Iliad and Odyssey) and against every shipped Iliad and Odyssey
unit that shares a word or phrase with these lines (3-word overlap search); quotation marks and `p`/`mark`
checked by script and against the neighbouring parts (iliad-050 ends on Hera’s closing ”; iliad-052 opens with
a narrative `p` unit). `t` was not touched (verified identical to the committed file, same unit count). Edits were
made by script; the file keeps its original layout and has no trailing newline, as before.

Counts: 24 changes — high 4, medium 7, low 13. 17 findings considered and refused (below).

Severity: high = contradicts a binding table row or a shipped identical formula, or `l`/`i` disagree in sense;
medium = a false grammatical label or cross-reference, or `i` not following its own note; low = polish, precision,
length.

## Changes (line · field · severity · what was wrong · what was done)

| Line | Field | Sev | Wrong | Done |
|---|---|---|---|---|
| 565 | l, i, n | high | ἐΰθρονον Ἠῶ was “fine-throned”, with “fair-throned” listed as avoided. The Odyssey table (odyssey/conventions.md, ἐύθρονος Ἠώς, 6.48) fixes “fair-throned Dawn” and four shipped Odyssey units use it (odyssey-076, -086, -090, -095); odyssey-090 even has the same ἐΰθρονον Ἠῶ μίμνειν. The new row claimed a new rendering for a word the table already has. | `l` “for fair-throned Dawn were waiting”; `i` “waited for fair-throned Dawn”; note now says “fair-throned Dawn, the Odyssey’s house rendering (ἐΰ- ‘fair’)”. |
| 477 | l, i, n | high | σέθεν δ’ ἐγὼ οὐκ ἀλεγίζω is the same half-line as 1.180 (iliad-002), shipped as “but of you I do not care” / “I do not care about you”, ἀλεγίζω “care for” (also 1.160). The draft used “take no heed of” and called “care for” too soft. The “heed” of 1.180 belongs to ὄθομαι, and the Odyssey’s ἀλέγω is “heed”, which stays at 8.483. | `l` “but of you I do not care / being incensed,”; `i` “and I do not care about you in your anger,”; note says ‘care for’ and points to 1.180. 8.483 ἀλέγω left as “take no heed”. |
| 551 | l, i, n | high | ἀπήχθετο was “had become hateful” / “became hateful”. The Iliad table fixes ἀπήχθετο as “was hateful” (6.140, 6.200, 9.300) and lists “became hateful” among the renderings avoided on purpose (the aorist is inceptive, the note says so); iliad-020, -037, -054 follow it. The draft recorded a departure with no reason the table had not already weighed. | `l` “for very much to them was hateful sacred Ilium,]”; `i` “for sacred Ilium was very hateful to them,”; note: ‘become hateful to’, which takes the house word ‘was hateful’. |
| 500 | l, n | high | `l` “but before this darkness came, which now has saved…” makes πρίν a conjunction with no main verb (and adds “this”); `i` reads πρίν as the adverb (“darkness came before that”), as the note itself says. `l` and `i` disagreed, and the note’s “before (this) darkness came” contradicted its “πρίν is an adverb”. | `l` “but earlier darkness came, which now has saved most of all”; note: πρίν is an adverb, ‘before, earlier’, so the clause is ‘but earlier darkness came’, before the Trojan hope could come true. |
| 513 | i, n | medium | `l` and the note take ὥς τις … πέσσῃ as a purpose clause (“so that someone … may digest”); `i` turned it into a free-standing wish (“no, let one of them at least have…”), adding “no” and losing the “so that”, so `i` did not follow the note. | `i` “but so that one of them at least may have a missile to nurse even at home, … so that another too may hate…”; note says the main verb is left out and gives it (‘let them not go aboard at ease, but so that …’). |
| 548 | l, n | medium | ἔρδον was “sacrificed” in `l`; every shipped `l` for ἔρδω says “offer” (1.315 “offered”, the same formula ἕρδον … τεληέσσας ἑκατόμβας, iliad-004; 2.306 “were offering”, iliad-010; table row ἔρδεσκες 13.350 “used to offer”). The row’s claim that “offered” is avoided has no support. | `l` “[and they offered to the immortals complete hecatombs]”. `i` “sacrificed” kept (iliad-010’s `i` has “sacrificing”; see refused list). Note: ἔρδω ‘do’, which with a sacrifice means ‘offer’ (as at 1.315); “sacrificed” gives the sense. |
| 503 | n | medium | “λύσαθ’ is λύσασθε, the aorist middle imperative”. False: λύσαθ’ is λύσατε elided, the τ becoming θ before the rough breathing of ὑπέξ; the verb is aorist active (“unyoke”). | Note corrected. |
| 508 | n | medium | “εὐρέα is the uncontracted form of εὐρεῖα” — false; εὐρέα is the neuter plural of εὐρύς (agreeing with νῶτα). | Note: “εὐρέα is the neuter plural of εὐρύς ‘broad’.” |
| 557 | n | medium | “ἔφανεν is ἔφανε with its preverb apart” — the form is the epic third-person plural (for ἐφάνησαν), agreeing with πᾶσαι σκοπιαί, not the singular. | Note corrected. |
| 494–496 | n | medium | “τῷ ‘on it’ is the dative of the relative pronoun for the spear” — τῷ is the article used as a pronoun, not a relative. | Note: “the article used as a pronoun”. |
| 552 | n | medium | “The line Ἴλιος ἱρή … is 4.47” — wrong line: Ἴλιος ἱρή is 4.46 and 8.551; the repeated line is καὶ Πρίαμος … Πριάμοιο, 8.552 = 4.47. | Note: “The line καὶ Πρίαμος … Πριάμοιο (552) is 4.47 and has the same English.” (English checked identical to iliad-021.) |
| 477 | n | low | “The sentence goes on through the next four lines”: it runs to 483. | “through line 483”. |
| 470 | i | low | “if you wish it”: the shipped English for ὄψεαι αἴ κ’ ἐθέλῃσθα is “if you wish” (iliad-024, odyssey-100). | “if you wish”. |
| 473 | l | low | “Peleus’-son” for Πηλεΐωνα; the four shipped `l`s (1.197, 2.188, 2.769, 9.179) and the table row have “son of Peleus” (“Peleus’-son” is kept for Πηληϊάδεω). | “the fleet-footed son of Peleus”. |
| 473 | n | low | ὄρθαι described only as an “epic aorist infinitive … intransitive” without saying what makes it so. | “the epic aorist middle infinitive of ὄρνυμι”. |
| 478 | l | low | “Hyperion the Sun”; the Odyssey table row for Ὑπερίονος Ἠελίοιο (12.263) has `l` “the Sun Hyperion”. | “the rays of the Sun Hyperion”. |
| 478 | n | low | νείατα glossed “lowest, furthest down”; “furthest” is on the row’s avoided list. | “lowest, undermost”. |
| 489 | n | low | Note said “a space showed through of the dead”; `l` has “the ground”. | “the ground showed through of the dead”. |
| 494 | n | low | “Line 495 stands in an earlier part”: the reused English covers 494b–495 (6.319–320), and “propping himself” differs from `l`/`i` “leaning” (iliad-008 has “Leaning on it”). | Cross-reference corrected; “‘leaning’”. |
| 498 | l | low | “the ships destroying” for the aorist participle ὀλέσας; “Ilios, the windy one” where iliad-019 ships “to windy Ilios” for the same προτὶ Ἴλιον ἠνεμόεσσαν. | “the ships having destroyed”; “to windy Ilios”. |
| 538 | i | low | “were as surely immortal … , and honoured as Athena and Apollo are honoured, as this day brings evil”: the correlative “as surely … as” is a clause apart and the closing “as” can be read with “honoured”. | Reordered: “…honoured as Athena and Apollo are honoured, as surely as this day brings evil to the Argives.” |
| 549 | l | low | “bore up into heaven”: “up” is not in the Greek (the row avoids “up to heaven”). | “bore into heaven”. `i` keeps “up from the plain”. |
| about | about | low | “feast” (the Trojans sacrifice; no feast is said) and “bread” for σῖτον. | “do as he says and sacrifice”; “food”. |
| 470, 473, 478, 489, 494, 513, 548 | n | low | Notes over the 110-word guide (118, 147, 120, 116, 127, 122, 123 words). | Tightened to 104, 112, 102, 107, 113, 113, 112. Units 473, 494, 513 and 548 stay a few words over because the content is needed. Unit 551’s note grew from 106 to 111 with the corrections above. |

## Considered and refused

1. **8.548 `i` “sacrificed”** (against the shipped `i` “offered” at 1.315): iliad-010 ships “sacrificing” for ἕρδομεν in `i`, and `i` uses the natural English for a sacrifice; only `l` must stay literal. Kept.
2. **8.507 / 8.547 σῖτον “food”** (the table has σῖτον “bread” at 9.216): the Odyssey ships “food” and “bread” by context; here the stores are brought from the town for men and fires, not a table-setting. Kept (caller may wish to see the 9.216 row).
3. **8.565 μίμνον “were waiting for”** (5.94 “stand against”): the exact formula ἐΰθρονον Ἠῶ μίμνειν is “wait for … Dawn” in odyssey-090; 5.94 is with a foe. Kept.
4. **8.532 “the Tydeus’-son”** (some shipped units say “Tydeus”): the majority of shipped `l`s are “Tydeus’-son”; the article is idiomatic after εἴ κέ μ’ ὁ. Kept.
5. **8.527–528 κῆρες “death-fates”** (2.834 has “death-spirits”): different context; the Odyssey (23.332) and the row at 4.11 give “fate of death”. Kept.
6. **8.480–481 `l` “lies around”, 8.521 “let a watch be”**: supplied copulas in `l` are the house habit; no word is added that the Greek does not imply. Kept.
7. **8.520 “womenfolk”** (possible remembered English): the note ties it to θηλύτεραι without a comparison and the word is a plain English rendering of “the female part of the household”; no phrase has arrived whole. Kept.
8. **8.558 “bursts open”**, 8.559 “glad in his wits / in his mind”: literal for ὑπερράγη and γέγηθε φρένα, and consistent with the shipped “glad in her mind” (odyssey-027). Kept.
9. **8.545–547 note “were getting themselves wine” beside `l` “they got”**: the note names the Greek imperfect; `l`/`i` match the shipped iliad-045 “got themselves wine”. Kept.
10. **8.508–511 `l` “through the night”, `i` “in the night” for διὰ νύκτα**: both fair; `i` is the idiom. Kept.
11. **8.498 `i` “Just now I thought”** for νῦν ἐφάμην: `l` “Now I said”, note says ‘just now I said (to myself)’; the future infinitive makes “thought” safe. Kept.
12. **8.489–491 `i` “leading them away … to the eddying river”** for ἀγαγὼν … ἔπι: acceptable for the aorist participle with ἐπί; kept.
13. **8.524 ὃς μέν … τὸν δ’** (ὅς read by `l` as a relative “the word that”): the note already sets the μέν … δέ contrast; `i` “this word … the other” carries it. No change.
14. **8.551 the merged unit has no `p`** (553 begins a paragraph) and the unit stays merged, as instructed; the note says so. Kept.
15. **Scansion**: the packet flags none; no line was found irregular on a hand scan of the lines with elision or unusual forms (8.527 ἐξελάαν, 8.558 ὑπερράγη, 8.494 ἑνδεκάπηχυ, 8.552), so no scansion sentence was added.
16. **Quotation marks**: “ on 470 and 497 (`mark` on both), ” on 482–483 and 538–541; none stray. 469 is narrative; iliad-050’s last unit closes Hera’s speech with ”; iliad-052 opens with narrative and `p`. Nothing to change.
17. **8.512 `i` omits μάν, 8.470 omits δή**: both are carried in `l`; particles of this weight are not required in `i`. Kept.

## For the drafter’s file (not edited here)

`new-renderings.md` has rows now out of step with the corrected units and should be fixed before its rows are copied
into the conventions table: ἐΰθρονος Ἠώς (use “fair-throned”, the Odyssey row), ἀλεγίζω (“care for” as at 1.180;
ἀλέγω stays “heed”), ἀπήχθετο (“was hateful”), ἔρδω (l “offered”), πρὶν κνέφας ἦλθε (l “but earlier darkness came”),
ποδώκης Πηλεΐων (l “son of Peleus”), αὐγή row (l “the Sun Hyperion”), νείατα row (avoided “furthest” is fine).

## Pass 2 (gloss)

Method: every novel parse in `gloss.json` checked against the Greek line in `units.json` (case, tense, mood, voice, number, lemma, Attic equivalent, homographs, ’ only, no line numbers, under 230 characters); every known form in `known-forms.json` checked against each place it stands in this part; each `__broaden__` entry checked as old entry whole + ` · ` + new reading, and the new reading looked up in the line; meanings checked against the current `l`/`i`/`n`. `units.json` not touched. All 19 existing `__broaden__` entries are old-whole + new and each new use is in the part; no change to them.

Counts: 14 changes — high 0, medium 7, low 7. 6 findings refused.

### Changes (form · severity · what was wrong · what done)

| form | severity | what was wrong | what done |
|---|---|---|---|
| τέρποντ | medium | Parsed impf. ’they took delight’; the unit’s note says τέρποντ’ is for τέρπονται and `l`/`i` are present (“take delight”). | Now pres. 3 pl. mid., elided (= τέρπονται), ’they take delight’. |
| μεγαλήτορες | medium | Glossed “great-hearted, high-spirited”, the two renderings the table turns down (reserved for μεγάθυμος / ὑπέρθυμος); `l`/`i` say “great-spirited”. | “great-spirited, high in courage”; quote ’great-spirited (Trojans)!’. |
| πυρὰ (broaden) | medium | Entry says acc. pl. only; at 551, 560 and 562 it is the nominative subject (πυρὰ … καίετο / φαίνετο). | Added “ · also neut. nom. pl., subject: ’fires’ …”. |
| τόσσα (broaden) | medium | Entry says acc. pl.; here it agrees with nominative πυρά. | Added “ · also neut. nom. pl., agreeing with πυρά: ’so many’ …”. |
| ἄλλο (broaden) | medium | Entry says acc. sg.; in οὐ σέο κύντερον ἄλλο it is the subject (nom.). | Added “ · also neut. nom. sg., subject of an unexpressed verb …”. |
| τρῶες (broaden) | medium | Entry nom. pl. only; 497 and 523 are vocative address. | Added “ · also masc. voc. pl., in address: ’Trojans!’”. |
| ἐπίκουροι (broaden) | medium | Entry nom. pl. only; 497 is vocative (“Trojans, Dardanians and allies”). | Added “ · also masc. voc. pl., in address: ’allies!’”. |
| εἴσω (broaden) | low | Entry covers adv. and prep. with a genitive only; here it follows an accusative (οὐρανὸν εἴσω). | Added “ · also postpositive, with an acc., ’into’ …”. |
| μάχωνται (broaden) | low | Entry reads ’until they fight’ (with κεν); here it is ὅτ’ ἂν … μάχωνται, ’when’. | Added the ὅτ’ ἂν, ’when they fight’ reading. |
| ὄβριμος (broaden) | low | Entry pinned to “epithet of Ares”; here it is Hector’s. | Added “ · also epithet of Hector: ’mighty’”. |
| κηρεσσιφορήτους | low | “death-spirits” where `l` has “death-fates”, `i` “fates of death”. | “the fates of death”. |
| ἔρδον | low | Gloss “perform … ’they were performing’”, but the sense in `l`/`i` is the sacrificial “offered”. | “do, perform; of a sacrifice, offer”; ’they were offering’. |
| ἄρουραν | low | “plowland” against the house British spelling (“plough-land”, “armour”). | “ploughland”. |
| ἐνθένδε | low | “from here” trips the no-“here” rule (lexical, not deictic, but avoidable). | “from this place, hence”. |

### Considered and refused

1. **αὐτούς “also plain pronoun, ’them’”**: not a use in this part, but the same lexeme and a true reading, harmless; kept.
2. **ἀπώσεται “or short-vowel aor. subj.”**: both parses are possible for the form and the note and the κέ broaden already cite both; kept.
3. **ἐς (known) at 536 ἐς αὔριον**: entry “into, to; + acc.” covers the temporal “to”; the novel αὔριον entry carries ’until tomorrow’. Not broadened.
4. **ἔναρα “object of φέροι”** (here the verb is φέρωμαι): pinned to another passage but not wrong of the form; known entries are only broadened for a new reading.
5. **μέσφ’, νείατα: no Attic equivalent named**: no Attic word exists for either (μέσφα, νείατος are epic only); naming ἕως or ἔσχατος would be a guess.
6. **ποιήσατο ’made for herself’** (here Hector, “held an assembly”): the verb and form are the same, the quoted English is an example; not a new reading.
