# Review of iliad-115 (Iliad 17.673–761)

Two passes were made over `units.json`. Pass 1: notes (every grammatical label, every position claim, every cross-reference, note against its own l/i), then Greek → `l` word by word, then `l` ↔ `i`, then remembered English, then quotation marks, then house renderings and the `new-renderings.md` rows against `conventions.md` (Iliad table and Odyssey table) and the published units. Pass 2: a fresh read of every changed unit and a re-check of every unchanged note, plus mechanical checks (t byte-identical to the edition archive and to the original file, field order and `ln`/`v`/`p`/`mark` untouched, no backticks or ASCII quotes in notes, l and t line counts equal, quotation marks only on the first and last unit of each speech: 685 → 693, 708 → 712, 716 → 721). `t` was never touched. No modern translation was recalled; every rendering was rebuilt from the grammar and checked against the table.

**Scansion.** The packet flags 0 lines, so there was nothing to scan by hand and no metrical sentence was added to any note.

**Speech marks against the neighbour.** iliad-114 ends with 17.671b–672 and closes Menelaus' speech with ”; 17.673 therefore opens outside a speech, as the unit does. The `mark` field sits on 685, 708 and 716 only, which are the first units of the three speeches in this part; each closes on the last unit of its speech (693, 712, 721).

**Citations.** Every citation in `new-renderings.md` was looked up in the Iliad table, the Odyssey table or the published units. None had to be dropped as unverifiable; nine were wrongly or ambiguously attributed (Odyssey rows cited as Iliad numbers; Iliad 7.206 for an Odyssey row) and were corrected.

## Counts

All changes: high 2, medium 28, low 24 (total 54).  
`units.json`: high 1, medium 21, low 17.  
`new-renderings.md` rows: high 1, medium 7, low 7.

## Changes

| file | line · field | severity | what was wrong | what was done |
|---|---|---|---|---|
| units.json | 673 · n | low | Note ran 144 words, over the 130-word validator warning. | Trimmed to 114 words (dropped the restated ἀπέβη gloss and the πόδας ταχύς gloss, which new-renderings.md already carries). |
| units.json | 679 · l, i | low | Vocative διοτρεφές given as "Zeus-nurtured" / "Zeus-nurtured Menelaus"; the table (10.266, 11.819) and the neighbouring published vocatives (iliad-108, -110, -114) have "Zeus-nurtured one". | l "Menelaus, Zeus-nurtured one"; i "Menelaus, Zeus-nurtured one". |
| units.json | 679 · n | low | "εἴ που … ἴδοιτο is an optative of purpose" is not the right label (an optative after a past verb, "in case / to see whether"), and the note said "he" while i says "you" without saying why. | Relabelled as an optative after a past verb; added that the English uses the second person because the poet is addressing Menelaus. |
| units.json | 685 · l, i | low | Same vocative: "Zeus-nurtured" for διοτρεφές. | "Zeus-nurtured one" in both layers. |
| units.json | 685 · i | medium | ὄφρα πύθηαι is a purpose clause (the note says so), but i turned it into a second imperative ("come here, Zeus-nurtured; learn of grievous news"): the force of the Greek was lost and εἰ δ’ ἄγε "come now" dropped. | i: "come here now, Zeus-nurtured one, so that you may learn of grievous news, news that ought never to have happened." |
| units.json | 685 · n | medium | ἣ μὴ ὤφελλε γενέσθαι was labelled "a wish that cannot be fulfilled". It is a relative clause with ὤφελλε + infinitive ("ought not to have happened"); the unfulfilled wish is ὤφελον/ὡς ὤφελον. | Relabelled as a relative clause with the sense of ὤφελλε explained. |
| units.json | 687 · l, i, n | medium | ὀΐομαι rendered "I suspect"; the Iliad table's later rows (10.551, 11.609, 11.834, 12.66, 13.747) have "I think" for ὀΐω with an infinitive, and "suspect" is kept only where the 1.558 sense (suspicion of a wrong) is meant; nothing of that kind here. | "I think" in l, i and the note; new-renderings.md row added. |
| units.json | 689 · n | medium | "ὤριστος is ὁ ἄριστος run together … The elision keeps the line to its beat": ὤ- is crasis, not elision, and the second sentence says nothing true about the verse. | "run together by crasis"; second sentence deleted. |
| units.json | 691 · n | medium | Claim about where a word stands: "γυμνόν … stands last before the stop for emphasis". γυμνόν is the first word of line 693, held over from the clause before; that is what stresses it. | Rewritten: "it opens line 693, held over from the clause before, which stresses it." |
| units.json | 691 · n | low | "ἐπὶ νῆα ‘to a ship’ is any ship": nothing in the Greek says that. | Deleted the claim; kept "‘to a ship’". |
| units.json | 693 · i | medium | ἀτάρ ("but", which the note itself says sets the stripped body against the armour) rendered "for" in i. | i: "but Hector of the glancing helmet has the armour." |
| units.json | 694 · n | low | "a strong verb" is empty and could be read as the grammatical term. | Removed. |
| units.json | 695 · i | medium | δέ in δὴν δέ μιν … rendered "For" (causal) in i; l has "and". | i: "And for a long time speechlessness took hold of him, …" |
| units.json | 695 · n | medium | "πλῆσθεν is a dual": it is the 3rd plural aorist passive (-θεν for -θησαν); only the subject ὄσσε is dual. | "πλῆσθεν is the aorist passive ‘were filled’, plural in form although its subject ὄσσε is a dual." |
| units.json | 697 · l, i, n | medium | ἐφημοσύνη rendered "charge"; the Odyssey's published English for the same word is "behest" (odyssey-059 l and i; odyssey-080 "the whole behest"), and the Odyssey rule is to reuse unless the Iliad context forbids. The row listed "behest" as avoided without saying the Odyssey uses it. | "behest" in l, i, note; row rewritten to cite the Odyssey units. |
| units.json | 700 · n | low | Note glossed ἀγγελέοντα "about to tell the news" but l is "about to tell". | Note now "about to tell". |
| units.json | 702 · l, i, n | high | ἀμυνέμεν with the dative of a person and no thing warded off is "defend" in both layers by the table (13.464, 13.481; 9.601). l had "ward off for", and i invented an object, "ward off ruin from", that the Greek does not have. | l "to defend the worn-down companions"; i "willing to defend the worn-down companions"; note says why; row rewritten. |
| units.json | 702 · l, i | medium | οὐδ’ ἄρα ("and not then") rendered "But not" / "But your heart"; the adversative is ἀλλά at 705, so the English put a "but" in the wrong place. | l "Nor to you, …"; i "Nor was your heart, …". |
| units.json | 702 · l, i | low | Vocative "Zeus-nurtured" without "one". | "Zeus-nurtured one" in both layers. |
| units.json | 705 · l, i | medium | εἶθαρ δὲ προσηύδα, in the same half-line as published iliad-075 (12.351, "and at once spoke to them"), rendered "straight away addressed them"; "at once" is the published rendering of εἶθαρ in five of six units, and "spoke to" the published προσηύδα. | l "and stood beside the Ajaxes, running, and at once spoke to them"; i "… stood beside the Ajaxes and at once spoke to them" (also "beside" as in iliad-075); note and row follow. |
| units.json | 705 · n | low | Note glossed αὖτ’ "for his part" while l has "again". | "‘and he himself again, in turn’". |
| units.json | 708 · n | medium | Cross-reference false: "like the Odyssey’s πόδας ὠκύς of the same hero". The Odyssey has πόδας ὠκύς only of Orsilochus (13.260); Achilles' formula is the Iliad's. | "as in the standing πόδας ὠκύς." |
| units.json | 709 · l, i, n | medium | οὐδέ μιν οἴω rendered "I suspect"/"I do not suspect that he will go"; same table point as 687 ("I think"). The note also gave ‘I suspect he will not go’ while i had the negative on the main verb, so note and i disagreed. | l "I think"; i "and I do not think he will go now"; note now states the negative stands with ὀΐω though it belongs in sense to ἰέναι. |
| units.json | 712 · l | low | "ourselves at least": the published iliad-114 wording of ἀλλ’ ἄγετ’ αὐτοί περ leaves περ untranslated. | l "But we ourselves, let us plan the best cunning," |
| units.json | 712 · n | medium | Cross-reference misdescribed: said the lines differ from 17.634–635 by "‘we ourselves’ in place of ‘let us’". The difference is ἡμεῖς δ’ for ἀλλ’ ἄγετ’, and a different end. | Rewritten accordingly. |
| units.json | 715 · n | medium | Cross-reference false: "The same line stands at 17.628". 17.628 is τοῖσι δὲ μύθων ἦρχε μέγας Τελαμώνιος Αἴας (checked against the edition archive). | Note says the line stands elsewhere (published iliad-096) and that 17.628 is a related line. |
| units.json | 725 · n | medium | "βλημένῳ is the perfect participle of βάλλω": it is the aorist (the perfect would be βεβλημένος). | "an aorist participle of βάλλω, middle in form and passive in sense". |
| units.json | 727 · i | low | i added "they keep on", a clause with no Greek behind it. | Removed. |
| units.json | 732 · l | medium | l "nor did anyone dare" for οὐδέ τις ἔτλη; the table (7.151) has "no one brought himself to it" and reserves "dare" for θαρσέω, and the draft's own row listed "dared" as avoided: the row contradicted the unit. | l "nor did anyone bring himself forward darting to fight …". |
| units.json | 735 · n | medium | "οἵ γ’ is a dual": οἵ is a plural form; the dual is the participle ἐμμεμαῶτε. | Rewritten: plural in form, "the two of them" shown by the dual participle. |
| units.json | 746 (first) · n | medium | Same false "οἵ γ’ is the dual". | Same correction. |
| units.json | 746 (first) · l | low | l had "carried the corpse", reversing the Greek order that the sibling at 735 keeps ("the corpse carried") for the same words. | "So they two, eager, the corpse carried." |
| units.json | 740 · l, i, n | medium | ἀζηχὴς ὀρυμαγδός rendered "unceasing"; published iliad-091 (15.25) renders the adjective ἀζηχής "incessant" and the draft's row claimed the table has only the adverb. | "incessant" in l, i and note; row corrected. |
| units.json | 744 · i, n | low | ὁμοῦ rendered "all at once", which changes it from "together" (with weariness and sweat). | i "worn down by weariness and sweat together"; note adjusted. |
| units.json | 749 · l, i, n | medium | ἴσχει rendered "holds back"; the table (5.89–90) fixes ἰσχανάω "hold back" and ἴσχει "check", and the draft's row claimed to follow 5.90 while doing the opposite. | "checks" in l and i; note and row corrected. |
| units.json | 749 · n | low | "grievous because they are hard to stop": no Greek behind the reason. | Deleted. |
| units.json | 752 · n | low | Note stated one reading of ὀπίσσω as fact; it can also go with ἀνέεργον ("back"). | Added one sentence naming the alternative. |
| units.json | 755 · n | low | Note speaks in the first person ("I have turned", "that I take"). | Impersonal. |
| units.json | 761 · n | low | First person ("I give it as"). | Impersonal. |
| new-renderings.md | 678 · row | low | Row gave i as "takes out its life"; the unit has "takes out his life". | Row corrected. |
| new-renderings.md | 697 · row | medium | ἐφημοσύνη row recorded a departure from the Odyssey's "behest" as if it were a free choice. | Row now follows the Odyssey and says so (see 697 above). |
| new-renderings.md | 701 · row | low | Row's l column ("an evil word about to tell the news") did not match the unit ("an evil word about to tell"). | Row corrected. |
| new-renderings.md | 702 · row | high | Row recorded "ward off" / "ward off ruin" and listed "to defend" as avoided, against the table rule at 13.464. | Row rewritten to "defend" (see 702 above). |
| new-renderings.md | 679/685/702 · row | low | No row for the vocative διοτρεφές. | Row added (table 10.266, 11.819). |
| new-renderings.md | 687, 709 · row | medium | 709 row listed "I think" as avoided and cited 1.558; no row for 687. | 709 row corrected, 687 row added, both citing the Iliad rows with "I think". |
| new-renderings.md | 707 · row | medium | εἶθαρ row (see unit 705). | Row rewritten with the published units. |
| new-renderings.md | 712 · row | low | Row said "only ‘But we … at least’ for ἀλλ’ ἄγετ’ … περ"; the published line leaves περ untranslated. | Row corrected. |
| new-renderings.md | 733 · row | medium | Row's l column "nor did anyone dare" contradicted its own avoided list ("dared"). | Row now matches the unit. |
| new-renderings.md | 741 · row | medium | ἀζηχής row (see unit 740). | Row corrected. |
| new-renderings.md | 745 · row | low | κάματος row did not mention that published iliad-112 (17.385) has "toil and sweat" for καμάτῳ δὲ καὶ ἱδρῷ; the table has "weariness" (4.230, 13.711). | Citations added and the iliad-112 difference recorded; unit left as is (see refusals). |
| new-renderings.md | 747/750 · row | medium | Row said ἴσχει follows the table's "check" (5.90) while giving "holds back". | Row corrected (see 749). |
| new-renderings.md | 737 · row | medium | Citation "ἄγριος ‘savage’ (7.206)": Iliad 7.206 is νώροπι χαλκῷ; the row meant Odyssey 7.206. | Cited as 4.23 (Iliad) and Odyssey 7.206. |
| new-renderings.md | several · row | low | Odyssey rows cited without saying Odyssey: ὣς ἄρα φωνήσας ἀπέβη (4.657), κάπρος (11.131), θάνατον καὶ κῆρα (16.169), ξενίων ποθή (15.514), κίρκος (15.526), φόνος (16.379), ἀταρπιτός (17.234), κάματος (10.363); a reader would look them up in the Iliad. | All labelled "Odyssey". |
| new-renderings.md | 727 · row | low | διαρραῖσαι row did not mention published "shatter" (iliad-012) and "raze" (iliad-070). | Added, with the reason the tearing sense is kept. |

## Considered and refused

| where | finding | reason |
|---|---|---|
| 673 i/l | Pronoun switching between the eagle ("it") and the hare ("him/his") in i, and "at it / it rushed" in l. | Greek has ὅν/μιν/αὐτῷ in the same order; l is the literal layer and i is clear in context. No change. |
| 697 l | l "was he neglectful" where published iliad-049/-081 have the verb "did not neglect". | The genitive object cannot be kept in l with the verb ("of Menelaus’ behest did he neglect" is not English); the adjective form keeps the genitive and the word order. i has "did not neglect", as published. |
| 705 l | "sent up" for ἀνῆκεν. | ἀνα- is in the verb; "released" and "urged" belong to other uses (iliad-007, 6.256). Recorded in the row. |
| 725 l/i | "charged straight" for ἴθυσαν while published iliad-026 and -076 have "rushed". | The table row for ἰθύει (11.552) fixes "charges straight on"; the earlier parts predate it. Not this part's to change. |
| 744 l/i | "weariness and sweat" against iliad-112's "toil and sweat" (17.385). | Table 4.230 and 13.711 (κάματός τε καὶ ἱδρώς "weariness and sweat") back "weariness". The difference is flagged in the row; iliad-112 is another part. Worth a look by whoever reviews iliad-112. |
| 727 l/i | "tear apart" for διαρραῖσαι although published parts have "shatter" and "raze". | Those are for a wall and a town; for dogs and a boar the tearing sense is the right one. Recorded in the row. |
| 740 i | "of horses and of spearmen" drops ἀνδρῶν. | αἰχμητάων is in apposition to ἀνδρῶν; "spearmen" carries both, and l has "of men, spearmen". The row says so. |
| 687 n | "θεός … understood to be Zeus" as an over-reading. | Hedged ("understood"), the usual reading, and the note does not put it in the translation. |
| 697 n | "left behind, it seems, so that he can run lightly". | Hedged inference, not stated as grammar; harmless. |
| 749 l/i | "making it stray" (l) against "making them stray" (i). | The note explains: the object is the current, and i gives the plural for πᾶσι. |
| Throughout | conventions.md line 24: "No quotation marks round speeches, as in Murray". | The brief for this review, the neighbouring published parts (iliad-114 opens its speech with “ and closes with ”) and every earlier unit of the Iliad all use “ ”; the opening/closing marks and the mark field were checked against that practice. The convention line is out of date, not the unit. |
| Throughout | Possibly "mixed" punctuation: units 4–6 and 15–16 carry no quotation marks. | Correct: the marks go only on the speech's first and last unit; mid-speech units have none. |
| t | Splits of t mid-line (e.g. 687–689, 693, 709). | Checked against the edition archive: concatenated t equals 17.673–761 exactly, ¶ flags fall on 673, 694, 700, 715, 722, 735 only, and `ln` is right for every unit (718 and the two 746 units start mid-line). |
| Out of scope | gloss.json and odyssey-forms.json give ὤφελλε a second parse "ὀφέλλω — increase"; odyssey-forms.json has it only as "increased". | Not units.json or review.md, so left; the verb in 17.686 is ὀφείλω ("ought"). Passed to the caller. |
