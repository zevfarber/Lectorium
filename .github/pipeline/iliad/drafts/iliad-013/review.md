# Review — iliad-013 (Iliad 2.569–675)

Two passes over `units.json` (107 lines, 57 units), then a check of `gloss.json`. All edits were made by script, `t` untouched (checked: every unit's `t` is identical to the original and joins to the archive text; `p` marks fall on the eleven ¶ lines; no `mark`, no quotation marks, none expected: there is no speech in the stretch and no speech runs in from or out into the neighbouring parts). Cross-references were checked against `source/iliad-monro-allen1920.json` line by line (516, 524, 532, 534, 537, 538, 540, 545, 548, 552, 559, 563, 568, 601, 1.25, 1.306, 2.169, 2.356, 2.496, 2.502, 2.510 and the in-part ones), the house renderings against both conventions tables and iliad-012, and the Odyssey glossary for κητώεσσαν.

Severity: **high** = the English or a note says something false about the Greek, or contradicts its own `l`/`i`; **medium** = a wrong grammatical label, wrong cross-reference, or a departure from a fixed house rendering; **low** = wording or precision, house consistency of small weight.

## Changes — units.json

| line | field | sev | what was wrong | what was done |
|---|---|---|---|---|
| 620 | l, i, n | high | Ἀκτορίωνε was rendered "the two Actor’s-sons" / "the two sons of Actor" in the same sentence that says the two are sons of Cteatus and of Eurytus: the English contradicted itself, and the note said the dual "names the fathers". | l "the two of Actor’s line"; i "the pair of Actor’s line"; note now says the dual is a patronymic from Actor, the leaders are sons of Cteatus and Eurytus, not of Actor himself, and the Greek does not say how the line runs. |
| 591 | n | medium | "ἔναιον … ends 593 and governs the names after it": false; two of its objects (Κυπαρισσήεντα, Ἀμφιγένειαν) stand before it in 593, and which verb takes Θρύον and Αἰπύ is open. | Note says it governs the two names before it and those of 594 after it, and that Θρύον and Αἰπύ could go with either verb (the English gives them to the first). Also shortened to stay under the note limit; "ἐϋκτίμενον" now cited as the one of 569. |
| 610 | n | medium | "as in 509, where the form is βαῖνον": βαῖνον stands in 510 (the unit begins at 509). | "as at 510". |
| 638 | l, i, n | medium | ἡγεῖτο (ἡγέομαι) rendered "was leader … was leader of": the table (ἡγεμονεύω / ἡγέομαι, 2.527, 2.567) fixes ἡγέομαι at l "was leading", i "led", and ἡγεμονεύω at "was leader"; iliad-012 2.567 follows it. | l "was leading Thoas"; i "Thoas … led the Aetolians"; note gloss "was leading". |
| 650 | n | medium | "repeats 645 with the leader’s verb in the singular": 645 (ἡγεμόνευεν) is singular too; the only change is the lost final ν. | Note: the first half returns to 645, δουρὶ κλυτὸς ἡγεμόνευε, verb without its final ν, singular though two men are named, as at 563. |
| 661 | n | medium | "τράφ’ is ἐτράφη, the unaugmented aorist passive": the elided form is τράφε (an intransitive aorist), not ἐτράφη. | "τράφ’ is the elided τράφε, an unaugmented aorist of τρέφω in its intransitive sense". |
| 668 | n | medium (pass 2) | κατέχευε called "unaugmented": it is augmented (κατ-έ-χευε). | "the epic augmented aorist of καταχέω (Attic κατέχεε)". |
| 671 | l, n | medium | κάλλιστος rendered "the most beautiful man" in `l`; the table (11.239, 11.310) fixes κάλλιστος at l "the fairest", i "the most beautiful". | l "the fairest man"; note "κάλλιστος is ‘fairest, most beautiful’, as in the Odyssey". |
| 576 | n | low | "τῶν is ‘of these’, and ἑκατὸν νηῶν … is the genitive after ἦρχε": τῶν agrees with νηῶν ("of these hundred ships"). | Note says so. `l` ("Of these, of a hundred ships") left as it stands. |
| 583 | n | low | glosses ἔφαλον "on the sea" while `l`/`i` and iliad-012 use "by the sea" (and 638’s note sets ἀγχίαλον against "by the sea"). | "ἔφαλον ‘by the sea’". |
| 631 | l | low | ἦγε rendered "was bringing" while the same imperfect of ἄγω (ἄγε 580 and 671, ἄγεν 654) is "brought" in `l` here and in iliad-012 (2.557 ἄγεν). One tense, one rendering. | l "But Odysseus brought the great-hearted Cephallenians," (the drafter’s new-renderings row for ἄγω still lists "was bringing"; that file was not touched). |
| 632 | n | low | "οἵ ῥ’ is ‘and those who’": there is no "and"; `l`/`i` say "who". | "οἵ ῥ’ is ‘who’". |
| about | about | low | "Meges brings forty from the Echinae": the Greek names Dulichium and the Echinae. | "from Dulichium and the Echinae". |

New-renderings rows now out of date (drafter’s file, not edited): the Ἀκτορίωνε row (now l "the two of Actor’s line", i "the pair of Actor’s line"), the ἄγω row (l "brought" throughout), and a κάλλιστος row would say l "the fairest" / i "the most beautiful" (table 11.239).

## Changes — gloss.json (glosser’s file, checked in pass 2)

All 254 new entries and 17 `__broaden__` entries were checked against the line; every `__broaden__` value begins with the existing entry whole; every novel form has an entry and none is extra; no entry is over 229 characters (the long ἂν/ὃ broadenings are the old entry plus additions); no ASCII apostrophe.

| key | sev | what was wrong | what was done |
|---|---|---|---|
| ἦγε | medium | "impf. 3 sg., unaugmented (= ἦγε)": ἦγε is the augmented form (the unaugmented one is ἄγε). | "impf. 3 sg., augmented: ’led, brought’". |
| ἀκτορίωνε | medium | "son of Actor … ’the two sons of Actor’" (the reading dropped at 620). | "of Actor’s line (patronymic); masc. nom. dual: ’the two of Actor’s line’". |
| ἔμβαινον | low | "augmented (ἐν-έ-βαινον)": unproven; the form as printed is not ἐνέβαινον and the note makes no such claim. | augment claim removed: "impf. 3 pl.". |
| κάμειρον | low | masc.; city names in -ος (Λίνδος, Λύκαστος, Φαιστός) are given fem. in the same file. | "fem. acc. sg.". |
| ἐδύσετο | low | "(= Attic ἔδυ)": ἔδυ is the intransitive root aorist; ἐδύσετο "put on" matches ἐδύσατο. | "epic ἐδύσετο (= Attic ἐδύσατο)". |
| κοίλην | low | pinned to a line ("κοίλην Λακεδαίμονα, i.e. ringed by hills") and an unsupported gloss. | "κοῖλος — hollow; adj., fem. acc. sg.". |
| χαλκίδα (broaden) | low | added reading was bare prose ("also Chalcis, a town of Aetolia"). | "· also Χαλκίς — Chalcis, a town of Aetolia; fem. acc. sg.". |
| σφι | low | lemma σφι beside the existing σφιν = "σφεῖς". | "σφεῖς — they; epic encl. dat. pl. σφι: ’to/for them’ (= Attic αὐτοῖς)". |

## Line 651, hand-scan

Μη-ρι-ο-νης τἀ-τά-λαν-τος Ἐ-νυ-α-λί-ῳ ἀν-δρει-φόν-τῃ is 17 syllables as written. A hexameter needs 16 here, so: feet 1–3 are dactyls (Μηριο· νηςτἀτά· λαντοςἘ), foot 4 is νυ-α-λίῳ with -ιῳ run together by synizesis (one syllable) and the υ counted long (the scanner finds two scansions of equal cost: υ long / α short, or the reverse), foot 5 is the spondee ἀν-δρει, foot 6 φόν-τῃ. Both flags are real: the spondaic fifth foot, and the synizesis/lengthening in Ἐνυαλίῳ. The unit’s note already says, in one sentence, that the line is metrically irregular as transmitted, that the fifth foot is a spondee, and that Ἐνυαλίῳ is scanned with synizesis; kept unchanged.

## Findings considered and refused

- **651 note wording on the scansion** — confirmed true by the hand-scan above; no change.
- **659 `i` "whom he had brought" against `l` "brought for himself"; 665 `i` "had threatened" against `l` "threatened"** — the English pluperfect gives the order of events (the wife was fetched before the son was reared; the threat came before the flight); the same licence is taken in iliad-012. Left.
- **624 ἄνακτος "agreeing with" Ἀγασθένεος** — Ἀγασθένεος and Αὐγηϊάδαο are both genitives in apposition, so ἄνακτος does agree with Ἀγασθένεος whichever of the two it sits beside; `l` and `i` are consistent. Left.
- **641 `l` "alive" for ἦσαν / ἔην** — the note says the verbs mean "were alive, existed"; `i` drops "alive" at the second verb. Left.
- **674 "Danaans" against the Odyssey’s "Greeks" in `i`** — the Iliad convention (Δαναοί "Danaans" in both layers) is binding; the validator’s warning is expected.
- **616–617 ὅσσον … ἐφ’ … ἐέργει** — the note already says the construction is compressed and the English one reading; nothing more can be claimed.
- **ἐϋκτιμένας "well-built, well-founded" in gloss.json** — repeats the existing ἐϋκτίμενον entry; the glossary keeps entries in step, and the note and `l`/`i` keep "well-built" (ἐΰκτιτος is the "well-founded" one). Left.
- **Glossary entries that say "agreeing with X" or "epithet of Y"** — contextual, but no line number or "here"; left.
- **Pre-existing glossary entry ἕποντο** says "augmented (ἕποντο = εἵποντο)"; ἕποντο is the unaugmented form. It is from an earlier part and the glosser may not rewrite existing entries: flagged for the owner, not touched (the unit notes say "unaugmented", correctly).
- **Known-form ἄγε entry** gives only "led" for the imperfect; the part uses "bring". Same lemma, same parse, the meaning is covered by the entry for ἄγεν ("lead, take, bring"); no broadening.
- **Note lengths** — 591 now 127 words, 671 113, 620 104, 612 110: inside the validator’s 20–130 band (it warns only outside it). Nothing cut further.
- **Remembered English** — checked every `i` for phrases that arrive fully formed ("killer of men", "the equal of …", "fighters at close quarters", "rich in flocks", "scion of Ares", "the sea that has the look of wine"): each is a table or new-renderings choice built from the grammar. Nothing found.

## Counts

Pass 1: 12 findings fixed in units.json (1 high, 6 medium, 5 low counting `about`). Pass 2 (fresh read of all 57 units, then the gloss): 1 more in units.json (668, medium), 8 in gloss.json (2 medium, 6 low). Totals: **1 high, 9 medium, 11 low = 21 changes**; 12 findings refused with reason.
