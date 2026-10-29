# iliad-101 (Iliad 16.210–305) — review, pass 1

Scope of pass 1: grammar truth of every note, Greek → `l`, `l` ↔ `i`, remembered English, quotation marks and `mark`/`p`, flagged lines, cross-references, and the new-renderings file against the house table. The gloss (pass 2) does not exist yet. `t` was not touched (checked by script before writing). No modern translation was opened or recalled; "cheer", "cast" and "in a close mass" below come from the conventions table, not from any English version.

Scansion flags: none in the packet, so no hand scan and no metrical sentence added.

Mechanical checks that passed: the six whole-unit repeats (16.210, 16.215, 16.238, 16.273–274 with its one comma difference, 16.275's first line) carry the published `l` and `i` word for word; `l` has the same line count as `t` in every unit; no straight quotes, no "Greeks", no newline in `i`; speech marks: Achilles’ prayer opens on unit 233 (`mark: Achilles prays`) and closes on unit 246 (”); Patroclus’ speech opens on unit 269 (`mark: Patroclus speaks`) and closes on unit 273 (”); the speech before 210 closes on the last unit of iliad-100 (”), and no speech is open at 305; `p` falls on 210, 249, 257, 275, 278, 284, the six ¶ of the packet; every `ln` matches the line where the unit begins; cross-references checked against the packet and parts.json (5.470, 13.155, 13.131–133, 6.112, 1.411–412, 1.455, 2.333–334, 12.470–471, 8.557–558, 14.507 are all true).

## Changes

Line · field · severity · what was wrong · what was done

| Line | Field | Severity | Wrong | Done |
|---|---|---|---|---|
| 16.215 | `n` | moderate | Said each accusative stands "after" its verb; in ἀνέρα δ’ ἀνήρ the accusative stands before its subject. A false claim about where a word stands. | Now: ἀσπίδ’ and κόρυν after their verb, ἀνέρα before its subject. |
| 16.222 | `l` | moderate | δαιδαλέης rendered "finely wrought"; the table fixes `l` "wrought" and `i` "finely wrought" for δαιδαλέος (4.135, 6.418, 17.32, and the Odyssey). | `l` now "fair, wrought,". |
| 16.222 | `n` | minor | Gloss ‘fair, finely wrought’ no longer matched `l`. | Now ‘fair, wrought’. |
| 16.227 | `i` | minor | "no one else … used to drink … or poured libation": the second verb lost the iterative (σπένδεσκε, like πίνεσκεν). | "or used to pour libation". |
| 16.232 | `n` | minor | "The subject … is Achilles, or what he was doing": λανθάνω with an accusative of the person needs a person as subject. | "The subject is not stated; it is Achilles." |
| 16.235 | `n` | minor | σοί left unexplained although both `l` ("your") and `i` ("around you … your") use it. | Added one clause saying σοί marks whose interpreters they are. |
| 16.241–242 | `l`, `i`, `n` | moderate | θάρσυνον rendered "embolden". The table keeps θαρσύνω "cheer" (Odyssey 12.360; Iliad 4.183, 4.233, 13.767); "embolden" is reserved for θάρσυνος (13.823, 16.70). No new-renderings row recorded the departure. | "cheer for him the heart within his wits" (`l`), "cheer the heart in his mind" (`i`), gloss in `n` to ‘cheer’. |
| 16.248 | `n` | minor | Note glossed μοι ‘to me’, but `l` has "for me". | ‘for me’. |
| 16.275–276 | `l`, `i`, `n` | moderate | ἀολλέες rendered "in a body". The table fixes "in a close mass" in both layers (5.498, 12.78); only 12.443 departs. | "in a close mass" in `l`, `i` and the gloss. |
| 16.284 | `l`, `i`, `n` | moderate | ἀκόντισε rendered "hurled". The table fixes ἀκοντίζω "cast" (4.490, 4.496, 4.498) and lists "hurled" as avoided; 13.402 is "cast with his shining spear". | `l` "first cast with his shining spear", `i` "the first to cast his shining spear", gloss ‘cast a spear’. |
| 16.294–295 | `l` | minor | "with a wondrous uproar": the published `l` for θεσπεσίῳ ὁμάδῳ (13.797) is "with wondrous uproar" (the article is only in `i`). | `l` now "with wondrous uproar". |
| — | `about` | minor | "the cup that only Zeus is ever poured to from" is muddled and says less than 16.225–227. | "the cup from which no one else drinks and from which wine is poured to no god but Zeus". |

Count: 0 severe, 5 moderate (16.215, 16.222, 16.241, 16.275, 16.284), 6 minor (16.227, 16.232, 16.235, 16.248, 16.294, `about`; the 16.222 `n` follow-on is counted with its moderate).

## new-renderings.md against conventions.md (file not edited; for the drafter or caller)

1. ἀολλέες row (16.276): says "in a body" in both layers and avoids "in a mass". That is now wrong twice: the units say "in a close mass" and the table’s main rows (5.498, 12.78) already fix that. Delete the row, or replace it with a note that 12.443 ("all together" / "in a body") is the outlier.
2. οὔλων ταπήτων row (16.224): the Iliad table already has οὖλος "ruinous" (2.6, 5.461, 5.717; the row for οὐλομένην). The row should say that this is the other word, οὖλος "woolly, thick" (Odyssey χλαῖναι οὖλαι, 19.225), so that a later reader does not "correct" it to "ruinous".
3. τοῖχον "a wall" (16.212): the table already has τεῖχος "wall" (7.436). Two Greek words with one English; the row should say so as other rows do. Minor.
4. ἕρκος "enclosure" (16.231): departs in `l` from the table’s "fence" (1.283, 15.566); declared with a reason. Accepted.
5. πυκινός `i` "close-set" / "dense" (16.212, 16.298): departs from `i` "solid" in the rows at 3.202 and 4.392; declared with a reason, `l` keeps "solid". Accepted.
6. κερτομέοντες `i` "teasing": departs from the Odyssey’s "mocking" (8.153); declared with a reason. Accepted.
7. ἐρωή "respite": departs from "rush"/"force" (4.542, 11.357); declared with a reason. Accepted.
8. ἀνένευσε "refused with a sign" with an object, against "signed a refusal" for the object-less ἀνένευε (6.311, 21.129); declared with a reason. Accepted.
9. No row exists for θάρσυνον or ἀκόντισε, and none is needed now that both follow the table.
10. The "Follows the table unchanged" row is otherwise true (checked each item that has a table row: μητίετα, ἀρηΐφιλοι, μεγαλήτωρ, ἱπποκορυσταί, ἄαπτοι, μῶλον Ἄρηος, ἀγών, θεσπεσίῳ ὁμάδῳ [after the `l` fix], μέγα φρονέοντες, κραδίην καὶ θυμόν).

## Findings considered and refused

- ἀνέῳγε (16.221) called "imperfect": formally it can be read as a pluperfect used as a past. Both readings are in the grammars and I cannot show the note false; left.
- 16.237 `i` "as once you heard … and honoured me": reads a little loosely beside the published `i` of 16.238 ("and further, even now"), but 16.238 must stay identical to 1.455 and the ἠμέν … ἠδ’ pairing is explained in the note. Left.
- λαὸν Ἀχαιῶν `i` "the people" (16.237): the table row at 2.450 has `i` "the army". Line 237 is the same Greek as 1.454, which shipped "people" in both layers, and the rule is to reuse the published wording. Left; the table has two rows that disagree (1.454 as shipped vs 2.450), which is for the caller to harmonise.
- 16.211 `l` "more closely": "closely" is supplied for μᾶλλον beside "fitted"; harmless and the note says μᾶλλον goes with the verb.
- 16.239–240 `i` "my companion": the Greek has no "my"; the note says so. Kept.
- 16.305 νεῶν called "a second epic form": it is also the ordinary Ionic–Attic genitive; the note’s wording is loose but not false.
- 16.271 τιμήσομεν called an aorist subjunctive in short-vowel form: the standard grammar for ὡς ἄν + -σομεν; a future indicative reading gives the same English. Left.
- 16.236 ἴψαο "aorist middle of ἴπτω": word for word the published note at 1.454; left for consistency (any change belongs to a later pass over iliad-005).
- Remembered English: "stood their ground" (16.305), "who sleep on the ground" (16.235), "wayside wasps" (16.259) and "drew breath again" (16.302) were each checked against the Greek parts; the first three rebuild from the elements named in the notes, the last is the published wording. No phrase looked imported whole.
- Notes at 16.257, 16.278 and 16.284 do not mention that a paragraph begins there; the runbook does not ask for it and `p` is set. Left.
- Scansion: no flagged lines.

## For pass 2

Waiting on `gloss.json`. Specific things to check against the line when it exists: ἄρθεν (ἀραρίσκω, not ἀείρω), ἀμφεφόβηθεν, ἐριδμαίνωσιν, ἀνιπτόποδες, χαμαιεῦναι, ὑποφῆται, ἀολλέες, δίηται, the possessive ὅς in οἷσι τέκεσσι and ἣν ἄτην (kept apart from the relative), σόον, and τῷ at 16.241 (both readings in the note).

## Pass 2 — gloss.json

Checked: all 70 novel entries against their lines and against the units; the 18 `__broaden__` entries each begin with the old entry whole (checked by string prefix against known-forms.json) and add only a new reading; every token of every `t` has a key in gloss.json or known-forms.json (none missing, none in both); format: no ASCII apostrophe or backtick, no left quote, no line numbers, no "here", all novel entries under 230 characters. The four forms the glosser flagged: τιμήσομεν (changed); εἴδοντο, ἀνέῳγε and τιθεῖσι (kept, see below).

### Changes to gloss.json

| Form | Severity | Wrong | Done |
|---|---|---|---|
| θάρσυνον | moderate | ’embolden!’ against the table’s θαρσύνω "cheer" (and the unit now says "cheer"). | ’cheer!’ |
| τιμήσομεν | moderate | "fut. indic. … used as a short-vowel aor. subj." mixes two analyses; the unit’s note says short-vowel aor. subj. | "1 pl. aor. subj. in the short-vowel form (or fut. indic.), in a purpose clause with ὡς ἄν". |
| ἐξεχέοντο | moderate | "(= Attic ἐξεχοῦντο)": χέω does not contract in Attic; ἐξεχέοντο is the same form. A false Attic equivalent. | Equivalent removed: "impf. 3 pl. mid., uncontracted". |
| ἐχέοντο | moderate | Called "unaugmented" (the initial ἐ- is the augment, χέ- the stem), gave the same false Attic form, and called ἐκ a tmesis preverb when it governs νηῶν. | "impf. 3 pl. mid., uncontracted". |
| οἷσι (broaden, new) | moderate | The glosser left the known entry (relative only) untouched, but οἷσι τέκεσσι (16.265) is the possessive ὅς, which the runbook says to keep apart. | Added " · also possessive ὅς, ἥ, ὅν: ’his own, its own’; neut. dat. pl. (οἷσι τέκεσσι ’its own young’)". |
| ἄραρον (broaden, new) | minor | Known entry says "transitive"; at 16.214 it stands with no object. | Added " · also intrans.: ’were fitted together’ (without an object)". |
| ἀνένευσε | minor | Parse said "ν-movable" of a form printed without ν. | Removed. |
| ἐξαπονέεσθαι | minor | "with future force after a verb of granting or refusing" is asserted without support and the note does not say it. | Replaced with ’to come back’. |
| παρά (broaden) | minor | "παρά … κιών = παρακιών" names a compound that is not a Homeric form. | "(παρά … κιών): ’passing by’". |
| μάχην (broaden) | minor | Tail "(driven away)" unclear. | "(thrust or driven away)". |

Count for pass 2 in gloss.json: 0 severe, 5 moderate, 5 minor. The broaden entries are now 20 (the 18 plus οἷσι and ἄραρον).

### Parses checked and kept

- τιθεῖσι: epic 3 pl. pres. of τίθημι (= τιθέασι), subject the boys; the participle reading (dat. pl. of τιθείς) does not fit the line. Kept.
- εἴδοντο: 3 pl. aor. middle of εἶδον with active sense, as the note says. Kept.
- ἀνέῳγε: "pluperfect in form, aorist in sense" is the more careful label. Gloss kept; the unit’s note (16.221) said "imperfect" and now says "a past form … (formally a pluperfect, used as a simple past)", so the two agree (units.json, one `n` field).
- ἀνθίσταντο "were resisting, held their ground", ἔστιχον "2nd aor. (or impf.)", ἄρθεν (ἀραρίσκω): acceptable as written.
- Known entries that I checked for coverage and found adequate: πάρα (prep. + dat. after its noun, covers νηῒ πάρα), ἕτερον (neut. "one thing"), τετυγμένον (neut. nom.), ἤ and ἦ, μάχης (separation with ἐξαπονέεσθαι is covered by the ἐξαποδίωμαι reading), κιών (existing "aor. part." left alone; additions only).
- The known entry ἀκόντισε still glosses ’hurled’ (a dictionary gloss, not the English layer); not rewritten, per the "never rewrite" rule.

### new-renderings.md

The three fixes from pass 1 are applied: the ἀολλέες row now reads "in a close mass" and names 12.443 as the outlier; the οὔλων ταπήτων row says this is the other οὖλος, not "ruinous"; the τοῖχον row says "wall" is shared with τεῖχος (7.436).

### Totals for the whole review (pass 1 + pass 2)

0 severe, 10 moderate (5 in units, 5 in gloss.json), 11 minor (6 in units, 5 in gloss.json).
