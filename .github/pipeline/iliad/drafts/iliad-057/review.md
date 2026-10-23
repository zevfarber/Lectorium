# iliad-057 (9.606–713) — reviewer, pass 1 (units only)

Severity scale: major = wrong sense, or a grammatical label or cross-reference that is false; moderate = a false label or cross-reference of smaller weight, a conflict with a house rendering or with a published line, an `l`/`i` that disagrees with its note, or a word left out; minor = polish, a loose gloss, an unneeded departure.

Method: `t` rebuilt from the packet's 108 lines and checked equal (true); `ln` checked for all 66 units; `l` has the same number of lines as `t` and `i` has none; paragraph marks `p` sit on 606, 620, 643, 656, 669, 676, 693, 710 (the eight ¶ of the packet); every speech has its `mark` and its “ ” (six speeches, opened and closed once each; 607–619, 624–642, 644–655, 673–675, 677–692, 697–709); no ASCII quotes in any field. The previous part iliad-056 ends at 605 with Phoenix's speech closed (”), and this part opens with narrative; 713 ends the book's day and opens no speech, so iliad-058 inherits no open quotation mark. Every unit whose Greek is identical to a published Iliad or Odyssey unit was compared with the published JSON by script: 606, 611, 643, 676, 686–687, 693, 695, 696 and 704 have `l` and `i` identical to the published ones (693–694a is the same unit as iliad-056's 430–431); 657 differed in `l` from odyssey-114 and was fixed (below). Cross-references were checked against iliad-001, -003, -008, -011, -017, -021, -043, -044, -045, -046, -052, -053, -054, -055, -056 and odyssey-114. Scansion flags: none, so nothing to hand-scan.

## Changes made (units.json, by script; `t`, key order and shape untouched; 26 edits in 21 units)

| Line | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 607 | `l` | moderate | γεραιέ (vocative) was "old man" in `l`; the house table (Odyssey 14.131, shipped at odyssey-067) has "aged one" in `l`, "old man" in `i` | `l` now "Phoenix, father, aged one, Zeus-nurtured one" |
| 607 | `n` | minor | followed from the above: note glossed γεραιέ as ‘old man’ only | now "γεραιέ is ‘aged one’ (‘old man’ in the free line)" |
| 607 | `n` | minor | "οὔ τί με … χρεώ is ‘there is no need of me’" reads as a genitive of the person; the construction is accusative of the person, genitive of the thing | now "‘there is no need for me’" |
| 608 | `n` | minor | "νηυσὶ κορωνίσιν has the epic dative plural": the epic ending belongs to νηυσί (ναῦς); κορωνίσιν is an ordinary third-declension dative | now "νηυσί is the epic dative plural of ναῦς, and κορωνίσιν ‘curved’ agrees with it" |
| 612 | `l` | minor | φέρων χάριν was "bringing favour"; the house row (5.211, 5.874) is "bringing a favour" | now "bringing a favour" |
| 612 | `i` | moderate | "by weeping and grieving as you do a favour to the hero" was ambiguous ("as you do" reads as a comparison, not as the participle φέρων); ὀδυρόμενος is "lament" in the table (2.315), not "weep" | now "with lamenting and grieving, bringing a favour to the hero, the son of Atreus;" |
| 620 | `n` | moderate | μεδοίατο called an "aorist optative"; μέδομαι has no aorist, and -οίατο is the present optative middle | "the present optative of μέδομαι" |
| 622 | `l` | moderate | μετὰ μῦθον ἔειπε: μῦθον was left out of `l` (the note called it the object); iliad-019 (3.303) has "a speech spoke" | `l` now "…son of Telamon, a speech spoke:" (`i` unchanged, as in iliad-019) |
| 622 | `n` | minor | "μῦθον … ‘a word’" | "‘a speech’", to agree with `l` and iliad-019 |
| 632 | `l` | minor | ἐδέξατο was "has accepted"; new-renderings.md and the table row for the gnomic aorist (ἀπέτισαν, 4.161) give the simple past in `l` | now "accepted" |
| 638 | `l` | moderate | ἔξοχ’ (ἔξοχα) was "beyond others"; the Iliad table row ἔξοχα (5.61, shipped at iliad-027) is "above all others" in both layers | `l` now "seven, above all others the best," |
| 638 | `i` | moderate | "the best there are by far" for the same ἔξοχα | now "seven women, the best above all others," |
| 638 | `n` | minor | gloss ‘beyond the rest’ | ‘above all others’ |
| 639 | `i` | minor | "So put a gracious heart…": σὺ δέ is continuing/contrastive ("but you"), not consequential; "So" added a force the Greek lacks | "Now put a gracious heart…" |
| 640 | `n` | minor | "the Odyssey uses it [κήδιστοι] of nearest kin and companions": odyssey-038 has kin by marriage (son-in-law, father-in-law), odyssey-047 a closest companion | now "of kin by marriage and of a closest companion" |
| 649 | `i` | moderate | "go and report the news plainly" for ἀγγελίην ἀπόφασθε; the same two words are published at 9.421 (iliad-055) as "declare the news", and ἀπαγγεῖλαι is "report" at 626 in this part | now "But as for you, go and declare the news;" (`l` already agreed) |
| 654 | `i` | moderate | "eager though he is for battle, will hold himself back around my hut": `i` took μάχης with μεμαῶτα, while `l` and the note take it with σχήσεσθαι ("from battle"); note and `i` disagreed | now "…eager though he is, will hold himself back from battle around my hut and my black ship." |
| 657 | `l` | minor | "and led the way Odysseus." where odyssey-114 (ln 370) has the identical Greek unit with `l` "and led Odysseus." (validator would warn; no Iliad reason to depart) | now "and led Odysseus." (`i` was already identical) |
| 658 | `i` | moderate | δμῳῇσι was "maidservants" in `i`; house table δμῳαί is "maidservants" in `l`, "maids" in `i` (Odyssey 6.69, 6.99; Iliad 9.477 "the maids") | now "…his companions and the maids to spread…" |
| 660 | `i` | moderate | same word, same fault | now "The maids obeyed…" |
| 664 | `n` | moderate | "παρκατέλεκτο is παρακατέλεκτο with the first α dropped": it is the final α of παρα- that is lost (παρ-κατ-) | "with the final α of παρα- dropped" |
| 666 (second unit) | `l` | minor | "Σκῦρον … αἰπεῖαν … πτολίεθρον": `l` made "steep" qualify "city" ("the steep city of Enyeus") while the note and `i` (rightly) make αἰπεῖαν agree with Σκῦρον | `l` now "having taken steep Scyros, the city of Enyeus." |
| 670 | `n` | moderate | "compare Odyssey 4.4": the other δειδέχατο passage is Iliad 4.4 (iliad-021, ln 3–4), not the Odyssey (the Odyssey has δειδέχαται at 7.71, a different form) | "compare Iliad 4.4" |
| 690 | `n` | minor | "αὖθ’ is αὖτε ‘in turn’" stated as fact; with the rough breathing of ὃ the elided form may equally be αὖθι ‘there’ (as at 9.427) | now "(or αὖθι ‘there’; the free line gives both)" |
| 704 | `n` | minor | "ὡς ἂν ἐγὼ εἴπω ‘as I shall say’" disagreed with `l` ("as I may say") and with the published note at 2.139 (aorist subjunctive with ἄν) | "‘as I may say’" |
| 713 | `n` | moderate | "it also stands at 7.482": 7.482 is κοιμήσαντ’ ἄρ’ ἔπειτα καὶ ὕπνου δῶρον ἕλοντο (iliad-045); only the second half is shared | "its second half also closes 7.482, after κοιμήσαντ’ ἄρ’ ἔπειτα" |

Totals: major 0, moderate 13, minor 13 (26 edits).

For the caller (files I was told not to touch): new-renderings.md now disagrees with the units in four rows and needs the same four edits before its rows are copied into the table: ἄττα row, `l` "Phoenix, father, aged one, Zeus-nurtured one" (and the avoided-list may add "old man" for `l`); ἀπόφασθε row, `i` "declare the news" (delete "report the news plainly", and say it follows iliad-055 at 9.421); ἔξοχον ἄλλων row, add 9.638 ἔξοχα with "above all others" in both layers (house row 5.61); φονῆος/ἐδέξατο row already says "accepted" in `l`, so it is now correct. (No row is needed for ὅττι τάχιστα; see refused 3.)

## Findings considered and refused

1. 669 `l`/`i` end with a comma where `t` ends with a full stop, and the next unit's English begins with a capital. Refused: the units are tapped separately; the comma marks the continuation the note already names, and it is the published wording of iliad-044 for the same clause.
2. 620 `i` "So he spoke, and nodded…" against iliad-006's "So he said, and … nodded" for ἦ καί. Refused: the Odyssey row for the same signal line (21.431) is "So he spoke, and nodded with his brows", and the table allows both; the drafter's choice is recorded in new-renderings.md.
3. 658/621 `i` "as quickly as they could" for ὅττι τάχιστα, against the Odyssey table's "as quickly as possible". Refused: the Iliad row at 4.193 puts "as … as you can" in `i` and "as quickly as possible" in `l`, which is exactly what this unit does.
4. 650 μεδήσομαι "think of" / "give a thought to" against the table's μεδέσθω "be mindful of". Refused: "be mindful of bloody war" does not stand in English; the departure is recorded in new-renderings.md and the note glosses the verb as ‘be mindful of’.
5. 680 φράζεσθαι "take counsel" against 9.251's "plan how" (φράζευ ὅπως). Refused: ἐν Ἀργείοισιν ("among the Argives") asks for the counsel sense, and iliad-055 at 9.347 has "take counsel" for φραζέσθω; both renderings are already in the published part.
6. 645 `i` "after my own heart" for κατὰ θυμόν may be a ready-made idiom. Refused with a flag: it is a literal calque (κατά + accusative "according to", θυμός "heart"), is not the wording of any translation I know of, and the drafter listed it with the rejected alternatives; the owner may prefer "to my liking".
7. 646–647 ἀσύφηλον not parsed (adverbial or agreeing with με). Refused: the note says the sense is not known and makes no grammatical claim; `l` "disgracefully" is the drafter's recorded choice.
8. 607 the note calls διοτρεφές "the stock epithet of kings". Refused: the table has διοτρεφέες βασιλῆες (2.445, 3.480) and the vocative διοτρεφές (9.229), so the claim is shown by published parts.
9. 615 "the old rule of friends and enemies" in the note. Refused: cultural gloss, not a claim about where a word stands or about the rest of the poem.
10. 692 `l` "will he lead him" and `i` "take him" for ἄξει, against 9.429. Refused: they are the published wording of iliad-055 at 429, only the person changed.
11. 663 `i` drops αὐτάρ ("But"). Refused: `l` carries it; the free line may drop a connective that adds no sense.
12. 693 and 710–711 ἀγασσάμενοι "amazed" vs "in admiration". Refused: the two senses are named in the notes at both places, 693 repeats iliad-056's English for the same words, and 711 repeats iliad-045.
13. 608 "τετιμῆσθαι … Διὸς αἴσῃ": `i` "lot", `l` "portion" — matches the table (αἶσα 1.416). No change.
14. 674 "ἀπέειπε" ‘refused’ against iliad-045's "delivered" at 7.416. Refused: the note already distinguishes the two verbs, and the context (ἦ … χόλος δ’ ἔτ’ ἔχει) fixes ‘refused’; 9.431 in iliad-056 has the same meaning.
15. 684–685 `i` "He said, too, that he would advise the others…" against iliad-055's first-person English at 9.417. Refused: the change of person is stated in the note and is the only departure; the rest of the line is the published wording.

Pass 2 (gloss.json) is not done here.


# iliad-057 (9.606–713) — reviewer, pass 2 (gloss.json)

Method: all 119 entries of `gloss.json` (99 novel forms plus 20 `__broaden__`, the novel set equal to `novel-forms.json`) were checked against the line each form stands in and against `units.json` (as corrected in pass 1): case, tense, mood, voice, particles, Attic equivalent, article-forms as pronouns, ὅς possessive/relative, homographs. Every `__broaden__` entry was checked by script to be the old `known-forms.json` entry whole + " · " + the new reading. Format checked by script: every novel entry under 230 characters, no ASCII apostrophe, no line numbers, no "here". Every known form that occurs in the part was then read against its existing entry for a use the entry does not cover. `units.json` was not touched (no note contradicts a gloss). Edited in place by script; before the edit gloss.json had 99 novel + 20 broaden entries, after it has 99 + 27.

## Changes made (gloss.json)

| Form | Severity | What was wrong | What was done |
|---|---|---|---|
| ἀσύφηλον | moderate | "disgraceful, insulting (sense uncertain)" put the guess first and the doubt in a bracket; the note on the unit says the sense is not known. "masc. acc. agreeing with an object" was vague (the only object is με) | now "sense not known; the traditional gloss is ’insulting, disgraceful’; neut. acc. sg. used adverbially: ’disgracefully’ (or masc. acc., predicative with a person)" |
| ἀπέχθηαι | moderate | no Attic equivalent given (rule for Homeric forms); voice missing ("aor. subj. 2 sg." — it is middle, from the thematic aorist of ἀπεχθάνομαι/ἀπέχθομαι) | "aor. subj. 2 sg. mid., open epic -ηαι (= Attic ἀπέχθῃ), in a negative purpose clause after ἵνα μή: ’that you not become hateful’" |
| ἐείσαο | moderate | mood not stated ("aor. 2 sg. mid."); the form is the aorist indicative (εἴδομαι ‘seem’, not the ἵημι/εἶμι ‘rush’ aorist ἐείσατο) | "aor. indic. 2 sg. mid. … + inf.: ’you seemed (to)’"; lemma and augment remark kept (they are true) |
| κήδιστοί | minor | "bound by ties of care" was loose and departed from the Odyssey glossary's κήδιστοι (superl. of κήδιος, from κῆδος); the use is predicative with ἔμεναι | "closest-tied, nearest and dearest (superl. of κήδιος, from κῆδος ’care, tie’); masc. nom. pl., predicative with ἔμεναι" (agrees with the unit note "closest-tied") |
| σύγχει | moderate | called "uncontracted epic σύγχει (= Attic συγχέε)": self-contradictory (the spelling is the shortened one, the Attic form συγχέε is the open one) | "epic σύγχει (= Attic συγχέε), after μή: ’do not confuse!’" |
| πληθύος | moderate | "partitive after ἐκ" is false: πληθύος is what ἐκ governs, standing before its preposition (ἐκ πληθύος Δαναῶν); it is not a partitive genitive | "object of ἐκ though the preposition may stand after it: ’from the throng’" |
| τεθνηῶτος | minor | gender and voice missing ("perf. part. gen. sg.") though the form agrees with masc. παιδός | "perf. part. act. masc. gen. sg." |
| ἐνυῆος | minor | "king of Scyros" is not in the text, which says only that Achilles took Scyros, "the city of Enyeus" | "a lord of Scyros, whose city Achilles took" |
| σίτου | minor | "gen. of the thing one is filled with" (the verb is τέρπω, "take one’s fill of", not "fill") | "gen. of the thing one takes one’s fill of" |
| δῶρον (broaden) | moderate | the new reading said ὕπνου δῶρον is "dependent on a gen."; it is the genitive ὕπνου that depends on δῶρον | "object, with a dependent gen.: ’the gift (of sleep)’" |
| λίσσεσθαι (broaden) | moderate | new reading ’that you had begged’ is the opposite of the line (μὴ ὄφελες … λίσσεσθαι, "would that you had not begged") | "in an unfulfilled wish, negated by μή: ’that you had not begged’" |
| μάχης (broaden) | moderate | new reading "governed by μεμαώς: ’eager for (battle)’" contradicts the unit (pass 1 settled that μάχης goes with σχήσεσθαι: `l`, `i` and note all say "from battle") | replaced by "of separation, with σχήσεσθαι: ’from battle’ (or governed by μεμαώς: ’eager for battle’)"; the alternative is kept only as an alternative, the unit's reading first |
| ᾗ (broaden) | moderate | the quoted example "τῆς ᾗ ἐτίομεν" dropped μιν (not the text); "of the condition one is in: ’in which’" did not match the unit (`l` "with which", `i`/note "in which, with which") | "relative, of the means or condition: ’in which, with which’ (τῆς ᾗ μιν … ἐτίομεν ’with which we honoured him’)". Possessive ὅς is correctly absent (ᾗ cannot agree with φιλότητος, and the old possessive reading is kept apart) |
| τῆς (broaden) | minor | example "τῆς φιλότητος" is not the word order of the line (φιλότητος … τῆς) | "(φιλότητος … τῆς ’that friendship’)" |

Missing broadenings added (known forms whose existing entry does not cover the use in this part):

| Form | Severity | Gap | New reading added |
|---|---|---|---|
| ἂν | moderate | ἂν with an infinitive in reported speech (καὶ δ’ ἂν … ἔφη παραμυθήσασθαι); no such reading existed, and the unit note relies on it | "modal particle ἄν with an infinitive in reported speech, keeping the ’would’ of the direct words" |
| ὅ | moderate | εἰς ὅ κ’ … μένῃ means "as long as" (unit `l`, `i`, note); the entry gave only "until" | "εἰς ὅ κε + pres. subj. of duration: ’as long as’" |
| κατὰ | moderate | κατὰ θυμόν = "after one’s heart" (unit `i`); the entry's only κατὰ θυμόν is ’in heart’, a different construction | "+ acc., ’according to, after’ (κατὰ θυμόν ’after one’s heart’)" |
| ὥς | minor | ὥς μ’ … ἔρεξεν, "how he treated me", after μνήσομαι; no plain "how" with an indicative | "ὥς before the enclitic με … after a verb of remembering: ’how’" |
| ἐάσομεν | minor | entry says "+ acc. and inf."; the line has the accusative alone | "+ acc. alone: ’leave be’" |
| πυκινὸν | minor | λέχος is neuter; the only reading for solid things was "masc. acc. sg." | "neut. acc. sg., agreeing with λέχος: ’solid’" |
| τιμῆς | minor | entry covers the partitive genitive after ἔμμορε only; the line has the genitive of the thing needed after χρεώ | "gen. of the thing needed, after χρεώ" |

Counts of changes by severity: major 0, moderate 12, minor 9 (21 entries touched: 9 novel, 5 existing broadens corrected, 7 broadens added).

## Findings considered and refused

1. τῆς/ᾗ (630): kept as the glosser has them. τῆς is the article-as-pronoun before its relative (the old "force of a relative: ’of which’" reading would make τῆς and ᾗ two relatives, so the demonstrative is the right one to add); ᾗ is the dative of the relative, not the possessive ὅς (a possessive would need to agree with φιλότητος and could not follow τῆς), so no homograph is wanted. Only the wording and quotations were fixed (above).
2. μένῃ: kept unchanged. Both readings are true (608 duration after εἰς ὅ κε, 701 alternative question after ἤ κεν … ἦ κε) and joined by " · ".
3. ἀσύφηλον: no stronger lemma or gender claim was made; the entry now says the sense is unknown and offers both parses without choosing.
4. ἐλέξατο under λέχομαι while λέξεο is under λέγω (II) and κατελέξατο under καταλέγομαι: the three lemmas are copied from the Odyssey glossary, where they stand and are true as lemmas; not harmonised.
5. ταύτης (known entry "agreeing with γενεῆς"): the line has it agreeing with τιμῆς; the existing text only pins an example, the form-level parse (fem. gen. sg. of οὗτος) is true. Not broadened.
6. τῇσι (ἐπὶ τῇσι), ἐθέλῃσιν (after ἢν, entry says "after αἴ κεν"), ἐκέλευσε (no infinitive in 660), ἀγαθόν, τὸ (706): the existing entries describe the form correctly and their stated contexts are examples, not limits. Not broadened.
7. αἱματόεντος "epic -όεντος", ἄωτον "nap, flock", τῇδέ and κεῖνός "accented before enclitic γε": loose or conventional but not false; left.
8. ἐξερέεινεν, κατέλεκτο, κατελέξατο, κήδιστοι-type entries copied from the Odyssey glossary: checked against the Iliad line and left as they are, apart from κήδιστοί above.
