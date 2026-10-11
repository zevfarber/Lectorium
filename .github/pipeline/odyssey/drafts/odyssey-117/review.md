# Review — odyssey-117 (Odyssey 24.214–326), pass 1

Reviewer pass 1 of 2. Files read: conventions.md, runbook.md (section 2), packet.md, units.json, new-renderings.md; published parts in the repository root for every cross-reference. No translation consulted. `t` of all 64 units compared with the packet lines before and after: identical, untouched. `units.json` edited in place by script (indent 1, as written). Pass 2 (gloss.json) not yet run.

Totals: 0 major, 6 moderate, 12 minor (18 findings, 19 field edits).

## Changes

| line | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 216 | n | moderate | cross-reference false: "ἡμέτερόνδ’ (266)"; the word stands in 267 | changed to (267) |
| 235 | l | minor | περιφῦναι rendered "embrace" here but the same verb is "clung round" in shipped odyssey-077 (20) and -096 (416), and unit 320 and its note tie the two together | l now "kiss and cling round his own father"; i left ("embrace") |
| 244 | i | minor | "not at all unskilled" puts πάμπαν into the wrong clause (it belongs to οὐδέ τι πάμπαν, already "nothing at all" later in i) | "not unskilled" |
| 248 | n | moderate | label false: "unaugmented aorist imperative" (an imperative has no augment; the point is the old ending -εο) | now "the aorist imperative middle of ἐντίθημι, in the old ending -εο (Attic ἔνθου)" |
| 251 | n | minor | "ἕνεκα following its noun" is true but silent that γε ἄναξ stands between ἀεργίης and ἕνεκ’ | added "with γε ἄναξ between them" |
| 254 | i | minor | "on a soft bed" supplies a noun the Greek lacks (μαλακῶς is an adverb; l says "softly") | "should sleep softly" |
| 258 | n | minor | "and who is not there" asserts something the lines do not show | "and who is not named" (and "just now", from νῦν δή) |
| 261 | l (line 264) | moderate | "halls of Hades" for εἰν Ἀΐδαο δόμοισιν; the same words are "the house of Hades" in shipped odyssey-021 (831), -074 (347), -100 (208), and i here already says "house" | l now "the house of Hades" |
| 261 | i | minor | "though he was none too sound…" adds a concession that neither the Greek nor l has (the clause is bare apposition giving the reason) | "a man none too sound of judgement, for he did not dare…" |
| 271 | n | moderate | label false: "ξεινήϊα … the adjective, used as a noun" — δῶρα is expressed; ξεινήϊα is an adjective agreeing with it | rewritten: "ξεινήϊος being the adjective ‘of a guest’ agreeing with δῶρα" |
| 278 | n | minor | ἔργα called "accusative of respect"; it is the object of the participle ἰδυίας | "with ἔργα as its object" |
| 280 | i | minor | "letting his tears fall" (plural) while the note says father and son weep "in the same words" and 234's i is "let a tear fall" | "letting a tear fall" |
| 281 | n | minor | ὑβρισταί called an adjective; it is an agent noun used adjectivally | reworded; both words "describe ἄνδρες" |
| 298 (2nd unit) | n | minor | "kept to the English used wherever it stands alone" — the line stands alone nowhere in the published parts; it is the second half of a unit in odyssey-093 | "its English is the published wording of this line" |
| 304 | i | moderate | "a famous house" for κλυτὰ δώματα; table row (5.381) fixes "famous halls" in both layers, and the note itself says "famous halls" | "famous halls" |
| 320 | l | minor | "clung about" where shipped περιφύς is "clung round" (odyssey-077, -096) | "clung round" |
| 325 | l, i | moderate | "our own halls" for ἐν ἡμετέροισι δόμοισι; the same words are "in our house" in shipped odyssey-035 (254) and -090 (223, 235); "halls" is the μέγαρα word | l and i "in our house" |
| 325 | n | minor | two faults: "ἡμετέροισι … standing for his own house, as at 216" contradicts the translation "our" (the house is father's and son's); "καταπεφνεῖν … found only in the aorist" is a form and a claim not shown by this part | first clause rewritten ("the house being his and his father’s", δόμοισι "a plural for one dwelling"); second now "the aorist ‘killed’, the κατά-compound of ἔπεφνον, with reduplication" |

## Considered and refused

- **Line 279, flagged AMBIGUOUS.** Hand scan: τέσ-σα-ρας | εἰ-δα-λί | μας ἃς | ἤ-θε-λεν | αὐ-τὸς ἑ | λέσ-θαι = D D S D D S, a regular hexameter with masculine caesura (after μας). The scanner's two readings differ only in the unknown quantities of the rare εἰδαλίμας (α, ι) and of ἃς, all costing 0. The irregularity is not real; no sentence added to the note.
- **Closing ” after 326.** Correct. The pinned source prints 327 as a new paragraph opening Laertes’ reply (τὸν δ’ αὖ Λαέρτης ἀπαμείβετο…), so Odysseus’ speech ends at 326. Opening ” on 214: odyssey-116's last unit (213) is narrator’s text with no speech open. Quote marks and `mark` fields on all five speeches (214, 244, 281, 303, 321) are balanced and sit on the first/last units; `p` falls exactly on the seven ¶ lines.
- **Line 248 (no stop).** Source lacks the mark; `t` left as is, per instruction. **Also found: line 286.** The source has no stop after ἀγαθῇ (`καὶ ξενίῃ ἀγαθῇ ἡ γὰρ θέμις`), and unit 34 ends there and unit 35 begins there, so that cut falls at a clause boundary with no printed mark. `t` left; for the lead to decide whether it needs rule 5 of the pipeline README.
- **ἀλωή “plot” / ὄρχατος “orchard”.** Accepted. Separates two words the table had run together (6.293 shipped “orchard”, 7.122 “vineyard”, 2.191/11.193 “vineyard plot”); the note says so; “plot” is the common core.
- **κυνέη l “helmet”, i “cap”.** Accepted: a goatskin κυνέη on a farmer is a cap, the note states it. It does depart from the table row at 22.102 etc., which lists “cap” as avoided (that row concerns armour and is unshipped); all shipped κυνέη are “helmet”. Flagged for the lead.
- **κνημῖδες l “greaves”, i “leg-guards”.** Accepted: “greaves” keeps the link to shipped ἐυκνήμιδες “well-greaved”; the note explains.
- **ἀρτίφρων “apt-minded” / “of sound judgement”.** Accepted: “-minded” is reserved for the -φρων epithets (this is one), and the i avoids “sound-minded” (ἐχέφρων), “prudent” (πεπνυμένος).
- **μένος “strength” (l) / “surge of feeling” (i).** Accepted: matches the table (“strength”, 13.387, 11.270) and the note says what it is.
- **χλαῖνα / φᾶρος both “cloak”.** Accepted: χλαῖνα “cloak” is the table; φᾶρος καλόν is “a fine cloak” at 3.467; the note says the garments differ.
- **ῥαπτός “stitched” (l) / “patched” (tunic, i).** Left: the sense follows ἀεικέλιον and the note says “stitch”; the row records the choice. Low risk.
- **ἐϋκτιμένη ἀλωή l “well-built”, i “well-tilled”.** Left; note and row explain; i follows sense, l follows 214.
- **i 261 drops που (“perhaps”) in “whether he is still alive”.** Left; force is small and l keeps it.
- **Remembered English.** Searched i for ready-made phrasing (“dark cloud of grief”, “I am that very man”, “threw his arms around”, “sharp surge”); each is rebuilt from the l and the grammar, and none is distinctive. No change.
- **Cross-references checked and true:** 4.117 and 4.119 in odyssey-015 (24.238 and the “last line” claim); the Mentes line 1.185 in odyssey-002 (Athena as Mentes speaks); δίκη of servants/mortals/gods in odyssey-066, -053, -092; Antinous ἰθὺς … Τηλεμάχοιο in odyssey-007; ἀτασθαλίαι in the proem; 234/280, 256/287, 258/297, 265/324 parallels; 309 vs 322 “fifth”/“twentieth”; πλάγχθη 1.2.
- **Reused lines (24.238, 239, 256, 265, 268, 271–272, 287, 297, 298, 302, 308, 310, 322):** l and i match the published wording wherever the whole unit or a whole line repeats; 24.274–275 agree in wording with shipped 14.323 (odyssey-041).

## For the lead: rows of new-renderings.md that now disagree with units.json (file not edited by the reviewer)

- εὑδέμεναι μαλακῶς: `i` now "should sleep softly" (was "should sleep on a soft bed"); "bed" now belongs in the avoided column.
- τὸν δ’ ἠμείβετ’ ἔπειτα πατὴρ κατὰ δάκρυον εἴβων: `i` now "Then his father, letting a tear fall, answered him:".
- κύσσε δέ μιν περιφὺς ἐπιάλμενος: `l` now "He kissed him, having clung round him, having leapt upon him, and spoke to him:"; its justification should cite shipped "clung round" (odyssey-077, -096) and 24.236 `l` "cling round".
- κυνέη row (αἰγείη κυνέη): add that "cap" departs from the 22.102 table row's avoided "cap" and why.

## Pass 2 still to do

Read gloss.json against the lines; recheck `l`/`i`/`n` once more after the glosser; re-verify quotes and `t` after any further edit.

---

# Pass 2 (reviewer, adversarial; units.json, gloss.json, new-renderings.md)

Files read: runbook.md section 2, the entry-format and notes sections of conventions.md, packet.md, units.json, gloss.json, known-forms.json, novel-forms.json, new-renderings.md. No translation or lexicon consulted. Notes since pass 1: rule 5 applied (· added after θυμῷ at 248 and ἀγαθῇ at 286 in the source; packet.md is older and lacks those two marks, otherwise `t` equals the packet text exactly). `t` of all 65 units compared before and after my edits by script: identical, untouched. The split 248 | 249–250 is sound: the 248 note no longer mentions αὐτόν σ’, the 249–250 note opens on it, `l` line counts equal `t` line counts in every unit, and the English of both fits (“do not harbour anger in your heart:” / “it is you yourself who are not well cared for, …”).

Totals, pass 2: 0 major, 4 moderate, 22 minor.

## Changes

| line | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 227 | l, i, n | moderate | ῥυπόωντα was attached to Laertes (note: “agreeing with τόν in 226”; l “and filthy, he was clad in”). It is accusative singular and ἕστο is finite with Laertes as its subject, so it can only agree with χιτῶνα (a nominative ῥυπόων would be needed for the man); it is the first of three describers of the tunic | n rewritten (agrees with χιτῶνα beside ῥαπτόν, ἀεικέλιον); l “and he was clad in a filthy tunic,”; i “He wore a filthy, patched, unseemly tunic, …”. Consistent with the broadened gloss entry (masc. acc. sg., agreeing with χιτῶνα) |
| gloss ἀγνοιῇσι | gloss | moderate | “aor. subj. 3 sg.” with “Attic ἀγνοήσῃ”: the form is the present subjunctive of ἀγνοιέω (stem ἀγνοιε- + ῃ, with -σι); an aorist would show -σ- before the ending | “pres. subj. 3 sg., epic ending -ῃσι (= Attic ἀγνοῇ)” |
| gloss χαρίζεο | __broaden__ | moderate | existing entry has only “pres. imper. 2 sg.”; 283 is not an imperative (unit note and `l` “you were giving freely”) | added “ · also impf. 2 sg. mid., unaugmented (= Attic ἐχαρίζου): ‘you were giving freely’ …”, old entry whole |
| gloss κατέπεφνον | __broaden__ | moderate | existing entry “aor. 3 pl.”; 325 is first person singular (Odysseus: “I killed”) | broadened with “ · also aor. 1 sg.: ‘I killed’”; note on 325 now says first person singular |
| 235 | n | minor | note glossed περιφῦναι “to throw his arms round” while `l` (pass 1) says “cling round” | “to cling round, that is to embrace” |
| 267 | n | minor | note said the plural ἡμέτερος “is used for ‘my’” while `l` and `i` both say “our house” | “‘to our house’, the plural ἡμέτερος being used by a single speaker of his own house, as at 216” |
| 267 | n | minor | “ἵκετο is the unaugmented aorist”: the known-forms entry says augmented or not depends on the metre, which the note does not show | “the aorist of ἱκνέομαι ‘come’” |
| 283 | n | minor | “because he thinks their recipient will not come back to repay them” (unshown, and not what 284–286 say) | “because, as the next lines show, he believes the guest who received them cannot repay them” |
| 286 | n | minor | ἡ (and the missing ἐστί) not explained, though 255 explains the same phrase | added “ἡ is the article used close to ‘that’, as in 255, with ἐστί left out” |
| 294 | i | minor | “… as he lay on the bed, closing his eyes as was fitting” moves ὡς ἐπεῴκει from the wailing (so `l`) to the closing of the eyes, and adds “lay” | “wail for her own husband on the bed, as was fitting, closing his eyes;” |
| 304 | n | minor | “the three genitives all go with υἱός”: only Ἀφείδαντος depends on υἱός; Πολυπημονίδαο and ἄνακτος agree with it | rewritten accordingly |
| 313 | n, i | minor | μίξεσθαι is a future infinitive (like διδώσειν) but was glossed without tense; `i` “give each other” supplies a reciprocal the Greek does not have | n “future middle of μίγνυμι”; i “and give splendid gifts” |
| 320 | n | minor | note said “having clung about” (pass 1 changed `l` to “clung round”) and called περιφύς “used without an object”; μιν of κύσσε is its object | “having clung round (its object is the μιν of κύσσε)” |
| gloss πολύδωρος | gloss | minor | “(of a bride brought with many gifts)” contradicts the note, which says the Greek does not say who gave the gifts | “whether she brought gifts or was given them is not known” |
| gloss ἐπιάλμενος | gloss | minor | “= Attic ἐπαλόμενος”: the Attic compound of ἐφάλλομαι is ἐφαλόμενος (aspirate) | corrected |
| gloss ἐπήριτος | gloss | minor | “perhaps ‘chosen’” is a guess against the note “meaning not known” | “meaning unknown” |
| gloss σικανίης | gloss | minor | “a name of Sicily” asserted from outside the text | “a place-name (taken to be Sicily)” |
| gloss ἐκίχεις | gloss | minor | check requested: the form has a primary-looking ending on a past stem, so “impf. or aor. type” is the safe parse; kept κιχάνω, now said so | “past 2 sg. (impf. or aor. type), epic; cf. aor. ἔκιχον”. Note on 284 (“in the past tense”) agrees |
| gloss χεύατο | gloss | minor | “‘poured over himself’” pins the entry to this passage | “aor. 3 sg. mid., unaugmented (= ἐχεύατο)” |
| gloss δέδετο | __broaden__ | minor | existing “plpf. pass. … ‘was bound’”; 229 is a middle with accusative, in tmesis | added the middle reading |
| gloss θυμαλγέα | __broaden__ | minor | existing “masc. acc. sg.”; 326 is fem. acc. sg. with λώβην | added |
| gloss αὐτοῦ | __broaden__ | minor | no existing reading for the plain genitive pronoun after ἰθύς (241) | added |
| gloss ἐπακοῦσαι | __broaden__ | minor | existing “(+ gen.)”; 262 takes the accusative ἔπος | added “ · also + acc.” |
| gloss ἀμφιπολεύειν | __broaden__ | minor | existing “inf. of purpose”; 244 is a defining infinitive after ἀδαημονίη | added |
| gloss μίξεσθαι | __broaden__ | minor | existing reading only “after ἔμελλε”; 313 is after ἐώλπει, with ξενίῃ | added |
| 325 | n | minor | (merged with κατέπεφνον above) person of the verb not stated | stated |

## Checked and left (not changed)

- **All 103 novel entries** and **18 existing __broaden__ entries** checked parse by parse against the lines. Every old entry is kept whole, followed by “ · ” (verified by script against known-forms.json). All novel entries: under 230 characters (longest 108), typographic ’ only, no line numbers, no “here”; the keys equal novel-forms.json exactly.
- **ἕσσαι** (perf. mid./pass. 2 sg. = Attic εἷσαι, “you are clad in unseemly things”): correct, and the note on 249–250 agrees. **ῥυπόωντα** broadened entry (masc. acc. sg., agreeing with χιτῶνα): correct, and now agrees with the note.
- **ἀλωῇ** keeps “orchard, vineyard plot”, the same wording as the existing ἀλωῆς entry. **εἰδαλίμας** keeps the lemma εἰδαλίμη and the “uncertain” flag (cannot be checked without a lexicon). **ἔχε** broaden example “wore a cap” left (the sense is the example, not the unit’s `l`).
- **Notes 1–64 re-read fresh**: every label checked against the form and line. No further change. Cross-references re-checked (216 vs 267/325; 227 vs 242; 240; 251 vs 257; 256/287; 258/297; 298; 299 vs 308; 309 vs 322; 234 vs 280; 265 vs 324). Quote marks: “ opens on 214, 244, 281, 303, 321; ” closes on 218, 279, 301, 314, 326; `mark` and `p` as in pass 1. Reused lines (24.238, 239, 256, 265, 268, 271–272, 287, 297, 298, 302, 308, 310, 322) still match the published wording.
- **Line 279** (flagged AMBIGUOUS): pass-1 scansion stands; no sentence added.

## new-renderings.md updated to agree with units.json

- εὑδέμεναι μαλακῶς: `i` “should sleep softly”; “on a soft bed” moved to avoided.
- 24.280 formula: `i` “Then his father, letting a tear fall, answered him:”.
- 24.320 κύσσε … περιφύς: `l` “clung round”; justification cites shipped “clung round” (odyssey-077, -096) and 24.236 `l` “cling round”.
- αἰγείη κυνέη: now says “cap” departs from the 22.102 κυνέη row (which lists “cap” as avoided) and why.
- ἐν λεχέεσσιν: `i` “on the bed”. μίξεσθαι … διδώσειν: `i` “give splendid gifts”.

## Status

Pass 2 complete. Nothing outstanding for the lead except: packet.md still shows 248 and 286 without the · (stale, harmless); build and validate not run by the reviewer.
