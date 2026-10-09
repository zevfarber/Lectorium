# review-106 — adversarial review of draft-106 (Odyssey 22.1–100)

`t` untouched: asserted equal, unit by unit, to the pre-review copy of `units.json`, and the units' `t` joined in order was re-derived from the pinned source (`odyssey_lib.lines_of`) and reproduces lines 1–100 exactly; every `ln` re-derived from character offsets and correct. Edits applied by scripts (`review_106_apply.py` asserted-substring replacement, `review_106_quotes.py` apostrophe retypeset; both kept in the reviewer's scratchpad, not in the repository), plus four hand-made whole-note rewrites (22.35, 22.96, 22.89, 22.83), all with `ensure_ascii=False, indent=1`. Build and validator were not run (instruction). Mechanical checks run by hand-written equivalents: `l` line count = `t` line count in every unit; no `\n` in `i`; no `?`, backtick or ASCII apostrophe in any note, `l` or `i`; note length 25–130 words in all 58 units (the draft had 22.35 at 142 words, a validator WARN; fixed); quotation marks 6 opening and 6 closing in both `l` and `i`, one speech each at 22.5–7, 22.27–30, 22.35–41, 22.45–59, 22.61–67, 22.70–78, none left open at the end of the part (22.100 introduces a speech that begins in the next part, as the published 14.22 does); `p` on exactly Murray's twelve paragraph openings (22.1, 8, 27, 31, 35, 42, 45, 60, 68, 70, 79, 89); `mark` on the first unit of each of the six speeches. Carry-over: the last unit of `odyssey-105` (the armed Telemachus) closes its speech with ” and nothing is open at 22.1.

Scansion: the packet flags no line (`Scansion flags: none`), so there was nothing to scan by hand and no irregularity sentence was added.

Repeated lines checked character for character against the published parts (the packet and a scan of all 105 published stories): 22.60 = `odyssey-034` 8.165 = `odyssey-088` 18.14, whole unit, `l` and `i` identical; 22.64 = `odyssey-063` 13.192, `l` and `i` of the line identical inside 22.61; 22.100 = `odyssey-014`/`odyssey-087`, `l` identical, the `i` clause "and, standing close beside him, spoke winged words" identical. The half-line μετὰ δὲ μνηστῆρσιν ἔειπεν (22.4 = `odyssey-103` 21.151) had a different `l`; fixed below. No other line or half-line of the part stands in a published part (checked by line and by unit).

## Pass 1 — Greek → `l` → `i`, notes, cross-references, marks

Severity: high = a false grammatical claim or a mistranslation a reader would learn as fact; medium = misleading or imprecise note, departure from a house row, `l`/`i` disagreement; low = polish.

| line | field | sev | what was wrong | what I did |
|---|---|---|---|---|
| 22.8 | n | high | "ὀϊστός is the arrow in the singular, as ἰός is in line 3": line 3 has ἰῶν (genitive plural) and ὀϊστούς (plural); ἰός is not singular there. | "a second word for 'arrow', beside ἰός (ἰῶν in line 3), and it is singular here". |
| 22.15 | n | high | "ἤλυθ' is the unaugmented aorist ἤλυθε": ἤλυθε carries the augment (root ἐλυθ-; the η is ε + ἐ). The recurring drafter slip. | "the aorist ἤλυθε (Attic ἦλθε), with its augment". |
| 22.34 | n | high | "προσέφη is the unaugmented aorist": προσ-έ-φη has the augment, and the published notes call it the imperfect of πρόσφημι. | "the imperfect of πρόσφημι 'speak to'". |
| 22.60 | n | high | Same false label. | "the imperfect 'addressed'". |
| 22.88 | n | high | "ἔχυτ' is the unaugmented aorist middle of χέω": ἔχυτο is augmented (ἐ-χυτο). | "ἔχυτ' is ἔχυτο, the aorist middle of χέω 'pour' with its augment, here with a passive sense". |
| 22.89 | n | high | "Ὀδυσῆος and κυδαλίμοιο are genitives in -οιο": Ὀδυσῆος is the Homeric genitive of Ὀδυσσεύς in -ῆος; only κυδαλίμοιο is in -οιο. | Each form now has its own label. |
| 22.1 | n | medium | μετὰ δὲ … ἔειπεν called tmesis: μετά governs the dative μνηστῆρσιν ('among the suitors'), as the published note on the same half-line (`odyssey-103`) says; the claim also set up a false "tmesis again" at 22.19. | "μετά with the dative μνηστῆρσιν is 'among the suitors', and ἔειπεν is an epic aorist of εἶπον 'said'". |
| 22.6–7 | n | medium | εἴσομαι: the note put σκοπὸν ἄλλον as object of 'find out' without saying that this strains the sense, and that the accusative sits naturally with εἶμι 'go at'; τύχωμι (subjunctive in -μι) unexplained. | Both readings stated with "which is meant is not certain"; the rendering still follows 'find out'; τύχωμι's ending explained. |
| 22.11 | n | medium | "μέμβλετο is for μέμελε(το)": no such form; it is the reduplicated past form (from μέμλετο) with β grown between μ and λ. | Rewritten. |
| 22.12 | l, i, n | medium | δαιτυμόνεσσι rendered "men at the feast" / "men feasting"; the house row for δαιτυμών (17.605) is "banqueters" and the neighbours (`odyssey-031`, 033, 087) say "banqueters". | "among banqueting men" in `l`, `i` and the note's gloss. |
| 22.19 | n | medium | "ἀπὸ … ὦσε and ἀπὸ … χεῦεν are tmesis again": the first ἀπό is the preposition of εἷο ('away from himself'), so it cannot also be a preverb; "again" pointed at the 22.1 claim withdrawn above. | First ἀπό goes with εἷο; ἀπὸ … χεῦεν is the tmesis, defined here. |
| 22.19 | i | medium | "sent the food spilling on the ground" for ἀπὸ δ' εἴδατα χεῦεν ἔραζε, a half-line that recurs at 22.85 ("spilled the food on the ground"): the repeated half-line must keep one English. | "and spilled the food on the ground". |
| 22.83 | l | medium | Same half-line: `l` "poured to the ground" against "poured out to the ground" at 22.19. | "poured out to the ground". |
| 22.83 | i | medium | "the sword dropped from his hand": ἧκε is transitive with Eurymachus as subject; `i` made the sword the subject. | "he let the sword fall from his hand". |
| 22.31 | i | medium | `l` "they said", `i` "they thought" for φάσαν. | "since they said he had killed the man without wishing to". |
| 22.45 | l, i | medium | αἴσιμα rendered "fitting"; the house row for αἴσιμα (7.310, 'in due measure') keeps the family of αἶσα, and the note itself says 'in due measure'. | "in due measure" in `l` and `i`; note adjusted ("you have said what is in due measure"). |
| 22.45 | i | medium | "If you are indeed Odysseus of Ithaca, now come, then …": εἰλήλουθας is the perfect 'you have come'; `i` read "come" as an imperative and dropped the perfect. | "If you have indeed come as Odysseus of Ithaca, then you have said what is …". |
| 22.68 | n | medium | λύτο called "aorist passive": it is the root-aorist middle form with passive sense. | "the unaugmented aorist of λύω, in the middle form with passive sense" (the shipped glossary entry for λύτο is left, additions only). |
| 22.75 | n | medium | ἀπώσομεν called "the future" after εἴ κε; εἰ κε takes a short-vowel subjunctive (the shipped κε entry lists both), and the form is ambiguous. | "a short-vowel subjunctive (ἀπώσομεν could also be read as a future)". |
| all notes; 22.61 l, i | n, l, i | medium | 857 ASCII apostrophes in the notes (Greek elision marks, English quotes, possessives) and "father's" in `l` and `i`; published parts 004 onward use typographic ‘ ’ and ’ (the drafts and published parts 104–105 do), the elision mark in Greek is U+2019. | Retypeset by script: ‘ at an opening quote, ’ elsewhere; 61 fields changed; checked that no opening quote is left unclosed. |
| 22.1 | l | low | "he spoke" against the published `l` "he said" for the identical half-line (`odyssey-103`). | "he said" (`i` already identical: "and he spoke among the suitors"). |
| 22.6–7 | i | low | "hit" for βάλεν and "strike" for τύχωμι, the reverse of `l`; αὖτε dropped. | "Now again there is another mark, one that no man has yet struck; I shall find out whether I can hit it". |
| 22.17 | i | low | "lurched" adds violence to ἐκλίνθη. | "bent over to one side". |
| 22.21 | i | low | "lay fouled" turns the imperfect passive φορύνετο into a state. | "were fouled". |
| 22.21b | i, n | low | `i` "hall" and "along" against `l` "house" and "toward" for κατὰ δώμαθ'/κατὰ δῶμα and ποτί; note asserted arms hang on the walls (not in the Greek). | "house", "toward"; note now "looking for weapons, as the next line shows". |
| 22.28 | n | low | σῶς "the adverb or adjective": a note should commit. | Adjective agreeing with ὄλεθρος. |
| 22.31 | n | low | ἴσκεν: did not say that 'say' would also fit. | Added "(the dictionaries give both senses, and either would fit; 'suppose' is taken)". |
| 22.35 | mark | low | "Odysseus speaks" on a reply to the suitors; 22.61 and `odyssey-088`/091 use "answers". | "Odysseus answers". |
| 22.35 | n | low | 142 words (validator WARN above 130); παρευνάζεσθε 'you lay beside' given with no word that the form (unaugmented imperfect) looks the same as a present. | Trimmed to 126 words; the ambiguity stated; "(Odysseus speaking of himself)" dropped. |
| 22.41 | n | low | "line 33 with the tense moved": the person also moves (σφιν → ὑμῖν) and νῦν replaces ὡς δή. | "with the person and tense moved". |
| 22.54 | l | low | "and you spare" reads as a statement; φείδεο is an imperative. | "and you, spare". |
| 22.54 | n | low | "Eurymachus describes the suitors as Odysseus' own people": stated as fact. | "Here 'your people' means the suitors, whom Eurymachus presents as Odysseus' own subjects." |
| 22.55 | i, n | low | `i` "and we" against `l` "but we" for ἀτάρ; "probably … which the Greek does not say" self-contradictory. | "but we"; "the sense may be … but the Greek does not say so". |
| 22.70 | mark | low | Second speech of Eurymachus marked "Eurymachus speaks"; the precedent for a second speech by the same speaker (`odyssey-034`) is "speaks again", and the formula has δεύτερον αὖτις. | "Eurymachus speaks again". |
| 22.78 | l, i | low | `l` "quickly" against note 'soon'; `i` "will soon be shooting" for a potential optative. | `l` "soon"; `i` "would soon be shooting". |
| 22.79 | i | low | "sprang at Odysseus" while the note ties ἆλτο to line 2 (`l`/`i` "leapt"). | "leapt at Odysseus". |
| 22.83 | l | low | "let go" for ἧκε χαμᾶζε; the published `odyssey-078` has "let fall to the ground". | "the sword he let fall to the ground" (note: ἵημι 'let go, let fall'). |
| 22.91 | i | low | "was too quick for him" is a stock idiom (suspect as remembered) for φθῆ 'got in first'. | "forestalled him" (rebuilt from the verb; `l` has "anticipated"). |
| 22.96 | n | low | ἀνελκόμενον taken as masculine (describing Telemachus) with no word that the neuter form could agree with ἔγχος; note 132 words. | Caveat added; "(from προπρηνής)" dropped to bring it to 130. |

Pass 1 count: 39 rows — 6 high · 14 medium · 19 low. Fields changed in `units.json` overall: 81 (in 58 units, counting every note retypeset by the batched typography row).

## Pass 1 — findings considered and refused

- **εὖχος** (`l` "a boast", `i` "the triumph"): kept. The note ties the two ('boast', the right to claim a success); "glory" is turned down for κῦδος and "renown" for κλέος in the house table; the new row is internally consistent.
- **ἀάατος** (22.5, `l` "harmless", `i` "which does the suitors no harm"): kept. It is exactly the house row for the same phrase at 21.91; the note says the meaning is not known and names the other guess.
- **σῖτος / εἴδατα**: both "food" in `i`, kept: the row says so, `l` keeps them apart ("food" / "viands"), and the note at 22.21 explains σῖτος.
- **πείρατα ὀλέθρου** ("the limits of destruction", 22.33 and 22.41): kept; both lines identical in `l` and `i`; the rope image sits in the note only, as the new row requires.
- **ἀρεσσάμενοι κατὰ δῆμον** ("having made amends throughout the land"): kept as the new row; the note admits the construction is elliptical.
- **ἴσκεν**: "supposed it so" / "imagined" kept; see the low note change above.
- **Comma-cut units** 22.35–38 | 39–40 (sentence 35–40 is six lines), 22.49–51 | 52–53 (five lines), 22.55–58a | 58b–59 (the sentence from ἀτὰρ ἄμμες runs about four and a half lines): all three exceed four lines, and each cut falls where the main clause is complete (γυναῖκα, Κρονίων, ἀποδώσομεν). Kept. The cut at 22.38 could also fall at 22.36 or 22.37, but then the second unit would be five lines of participles; not better.
- **εἶπας "the aorist of λέγω"**: lexicon shorthand, accepted; the shipped entry will say εἶπον.
- **ἔδονται "(Attic ἔδομαι)"** (22.30): the lemma is shown, the form is the same in Attic; accepted.
- **οἶος "he alone speaks, since the others are struck with fear"** (22.44): a reading from the two lines before; accepted.
- **ὑπεμνάασθε "the ὑπο- carrying the sense of underhand dealing"** (22.38): the lexical gloss 'woo secretly'; accepted.
- **My own provisional finding** that παρευνάζεσθε was wrongly given as a past tense: withdrawn. The unaugmented imperfect is identical to the present, and its neighbours κατεκείρετε and ὑπεμνάασθε are imperfects; the note now says so (low row above).
- **ἀνιάζων, ἀκαχμένον, περιρρηδής, δολιχόσκιον, ἀμφικύπελλον, ἐϋκτιμένης, ἐύξοον, χλωρὸν δέος, αἰπὺς ὄλεθρος, νέμεσις, ὑπερβασίη, κήρ, φίλον ἦτορ, ἀάπτους**: each checked against its house row (or the published neighbour) and found to agree (sometimes after the table's own `l`/`i` split); no change.
- Phrases in `i` suspected as remembered ("pale fear" is the house row; "winged words" is the house row; "doubled over", "let fly an arrow", "in anguish of heart") were rebuilt from the grammar in the notes and left, except "was too quick for him" and "lurched" above.

## Pass 2 — whole edited file re-read; `gloss.json` checked

The whole edited `units.json` was re-read (all `l`, `i`, and every changed note); no note contradicts its `l`/`i` after the edits. Then every one of the 119 novel entries and the 26 broadenings in `gloss.json` was checked against its line(s), and the 363 known-form entries against their uses here. Format re-checked: all entries have the shape `lemma — meaning; parse`, typographic ’ only, no backtick, none over 230 characters; all 26 broadenings begin with the shipped entry whole.

| form (line) | field | sev | what was wrong | what I did |
|---|---|---|---|---|
| γυμνώθη (1) | entry | high | "= Attic ἐγυμνώθη, same form": the Homeric form has no augment (γ- initial), so it is not the same form. | "aor. pass. 3 sg., unaugmented (= ἐγυμνώθη), with middle sense". |
| εἴρυτο (90) | entry | high | "aor. 3 sg. mid. … 'drew'": εἴρυτο is the pluperfect (the aorist is εἰρύσσατο, 79); `l` says "had drawn". | "plpf. 3 sg. mid. … 'had drawn'; the same letters can also belong to ἐρύομαι 'guard'". |
| κατέκτανες (29) | entry | medium | "root aorist stem κτάν-": ἔκτανον is the thematic second aorist; the root aorist is ἔκτα(ν). | "epic 2nd aorist stem κτάν-". |
| κατακτεῖναι (32) | entry | medium | "complementing ἐθέλοντα": it is the infinitive in indirect statement after φάσαν, with ἐθέλοντα agreeing with the understood subject; meaning given as 'to kill'. | "in indirect statement after φάσαν: 'to have killed'". |
| ἀνελκόμενον (97) | entry | medium | "neut. acc. sg., agreeing with ἔγχος": contradicts `l`, `i` and the note (accusative describing Telemachus). | "masc. or neut. acc. sg.: 'pulling out, being drawn out'". |
| ἀπώσομεν (76) | entry | medium | "fut. 1 pl. … (= Attic ἀπωσόμεθα-type)": no such Attic equivalent (the Attic future is ἀπώσομεν); mood ambiguous after εἴ κε, and `l` takes it as subjunctive. | "short-vowel aor. subj. or fut. indic., with εἴ κε: 'we may thrust back, we shall thrust back'". |
| σῖτός (21) | entry | medium | Gloss 'bread'; the house rendering (and `l`/`i`) is 'food'. | "'food'". |
| ἀρεσσάμενοι (55) | entry | medium | Gloss 'having appeased' is the rendering the new row turns down here (reserved for 8.396). | "appease, satisfy, make amends … 'having made amends'". |
| εἴσομαι (7) | entry | medium | No mention of the disputed second reading (future of εἶμι) that the unit note states; pinned gloss "(whether I hit)". | "οἶδα … 'I shall know, find out' · also possibly the future of εἶμι 'go': 'I shall go at' (disputed)". |
| αὐχένος (16) | entry | medium | "epic -ος (= Attic αὐχένος, same form)": nothing epic about the regular genitive. | Removed. |
| παντὶ (94) | broadening | medium | Known entry gives only the substantive 'to everyone'; here it agrees with μετώπῳ ('all of'). | Added to `__broaden__`: old entry whole + " · also agreeing with a noun: 'whole, all of' (παντὶ μετώπῳ …)". |
| παρευνάζεσθε (37) | entry | low | "pres. 2 pl." only; the unit note takes it as the unaugmented imperfect (identical form). | "pres. 2 pl. mid., or impf. without augment". |
| δίε (96) | entry | low | Contained "here" (barred by the runbook); aorist asserted though the lexica treat the tense as aorist or imperfect. | "past 3 sg. (aor. or impf.) …; with περί 'greatly' and μή 'lest'". |
| ἐκχεύατ' (3) | entry | low | Attic equivalent given as ἐξέχεε (the active), not the middle. | "= Attic ἐξεχέατο". |
| ἐπίηλεν (49) | entry | low | Lemma spelt ἐπιάλλω; the unit note and LSJ have ἐπιϊάλλω. | Lemma respelt. |
| ὠκυμόρων (75) | entry | low | "epic -ων": the genitive plural of a two-ending adjective is not epic. | Removed. |
| ἀντίσχεσθε (74) | entry | low | Lemma "ἀντέχομαι (aor. ἀντίσχω)": not an LSJ lemma; 'the tables' pinned. | "ἀντέχω … (mid. ἀντέχομαι); aor. imper. mid. 2 pl.: 'hold up before you'". |
| 22.89 | n | low | After the εἴρυτο correction: "a form of ἐρύομαι" was vague. | "a pluperfect of ἐρύω 'draw', 'had drawn'". |
| 22.83 | n | low | ἧκε glossed only 'let go' beside the new `l` "let fall". | "'let go, let fall'". |

Pass 2 count: 19 rows — 2 high · 9 medium · 8 low (17 `gloss.json` entries touched: 16 novel entries corrected, 1 broadening added; 2 unit notes adjusted to match).

## Pass 2 — considered and refused

- Entries that say "agreeing with X" or quote the line's phrase in the gloss (many of the 119): house practice in the shipped glossary; the instruction against pinning is read as "no line numbers, no 'here'", which the entries obey.
- μέμβλετο "plpf. 3 sg.": kept; consistent with the note's "reduplicated past form".
- νέμεσιν "righteous anger, retribution … 'indignation'": the lexical gloss, not the rendering; kept.
- ἀάατος "traditionally 'unharmed, free from ruin'": the lexical gloss; the entry says the meaning is uncertain; kept.
- στήθεσφιν "gen. or dat." with "(= Attic στήθους)": acceptable.
- ἴσκεν "(= Attic ἔλεγεν)": acceptable.
- The 26 broadenings: all verified (old text whole, new reading true of the line); the broadening of μετά (22.10 'in the hands') and the corrected note at 22.4 (preposition, not tmesis) agree with each other.
- Known entries checked for coverage and found sufficient: κε/κέ/κεν/κ (the shipped entry already lists the subjunctive/future ambiguity after εἴ κε, supporting the ἀπώσομεν fix), ἐπί (tmesis at 22.75), ὑπό (tmesis 22.42), ὄφρα/ὄφρ' (optative purpose), ἔχωμεν (hortatory), εἴ, τῷ, τιν', τοι, μή, ἐκ, ἀνά, ἀπό.
