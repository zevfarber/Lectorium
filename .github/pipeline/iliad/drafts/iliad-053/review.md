# iliad-053 (9.114–204) — review, pass 1 (units.json; the gloss is for pass 2)

Method: notes first (every label, every "where a word stands", every cross-reference, notes against their own `l`/`i`), then Greek → `l` word by word, `l` ↔ `i`, remembered English, quotation marks and `mark`/`p`, then every stock epithet and formula against both house tables (grepped form by form, not skimmed), then every line of the part against all published Iliad and Odyssey units for shared half-lines (3-word and 4-word matches by script). All 91 lines were also run through the scanner: every line fits, the packet flags none (the flag test is UNRESOLVED / AMBIGUOUS / NO FIT), so no scansion sentence was added. `units.json` was edited in place by script (`/tmp/claude-0/-home-user-Lectorium/e20992d8-67c6-5716-90e9-2639c111d39b/scratchpad/review53.py`, plus two short follow-ups); `t` was never touched (checked: every `t` identical to the draft's and the tiling of the edition still holds). The build was not run.

Speech marks: the last unit of iliad-052 (ln 111) already closes Nestor's speech with ”, and 9.114 is narration, so nothing runs in from the previous part and nothing runs on into iliad-054 (the speech at 202–204 ends with 204 ”). The four speeches (115–160, 163–172, 197–198, 202–204) open with “ on the right unit, close with ” on the right unit, carry `mark` on the first unit and nothing stray inside; `p` is on 114, 162, 173, 182, 199 only, which are the edition's paragraphs.

Counts: **6 major, 7 medium, 9 minor, 9 nit** (31 findings, all acted on; the new-renderings.md consistency pass is counted among the minors).

## Changes

Severity: major = a house-table or shared-line departure, or a Greek → English misreading; medium = a wrong label or cross-reference, or an `i` whose force differs from the Greek or its own note; minor = a claim or wording that was loose; nit = polish.

| line · field | severity | what was wrong | what was done |
|---|---|---|---|
| 179 · `l`, `i`, `n` | major | Ὀδυσσῆϊ δὲ μάλιστα is a dative (the man charged, to be read with ἐπέτελλε), not a second target of the glance (ἐς ἕκαστον). `l` "and at Odysseus most of all" and `i` "but at Odysseus most of all" made it a glance at Odysseus. | `l` "and to Odysseus most of all"; `i` "but on Odysseus most of all"; the note now says the dative is the man charged and ἐπέτελλε is supplied again. |
| 132 · `i`, `n` | major | `i` "never went up to her bed" for ἐπιβήμεναι εὐνῆς. The Odyssey table (and odyssey-048, 10.296 and 10.342) fixes `i` "mount … bed" for the same phrase; the draft's own new-renderings row listed "mounted" as avoided, against the table. | `i` "never mounted her bed"; note quotes "mounted". |
| 185 · `l` | major | `l` "a clear lyre" for λιγείῃ φόρμιγγι. The Odyssey table fixes φόρμιγξ λίγεια (8.67) as "the clear-sounding lyre" in both layers. | `l` "a clear-sounding lyre". |
| 199 · `l`, `i`, `n`, `about` | major | τάπησι rendered "rugs". The Odyssey ships "carpets" for τάπης/τάπητες (odyssey-016, -032, -099, -117 = 4.298, 7.337, 20.150, 24.276) and the table keeps "carpets" for τάπητες, "rugs" being its word for ῥήγεα. | "purple carpets" in `l`, `i`, the note and the part's `about`. (odyssey-015 and -045 have "rug" for τάπης; published, left alone, see the refused list.) |
| 195 · `l`, `n` | major | `l` "And in just the same way" for ὣς δ’ αὔτως. The Iliad table (3.339, 7.430) fixes `l` "And just so", `i` "And in just the same way"; the draft put the `i` form in `l`. | `l` "And just so Patroclus, when he saw the men, stood up."; `i` unchanged; the note says "and just so", "in just the same way" in the free English. |
| 196 · `l`, `i`, `n` | major | The line is the Odyssey's 4.59 (τὼ καὶ δεικνύμενος προσέφη ξανθὸς Μενέλαος, odyssey-014: `l` "And to the two of them, gesturing, spoke …"). The draft did not reuse it and put an interpretation ("greeting by gesture") into `l`, which the note itself calls uncertain. | `l` "And to the two of them, gesturing, spoke swift-in-feet Achilles:" (the Odyssey's wording, name changed; "spoke" for a non-reply προσέφη also has the Iliad's 2.790 as precedent); `i` "And gesturing a welcome, Achilles, swift of foot, said to the two of them:" (the Odyssey's `i` has "toward the food"); the note names Odyssey 4.59 and says that a gesture of welcome is the lexicons' sense, not certain. |
| 201 · `l`, `i` | medium | The line is shared with odyssey-107 (22.163) and -109 (22.355): `l` "spoke to X, who was near", `i` "who was near him". The draft's `l` "he spoke, being near" can be read as the speaker being near. | `l` "who was near"; `i` "who was near him". |
| 165 · `i` | medium | `i` "chosen men" for κλητούς. "Summoned" is `l`'s word; "chosen" pre-empts 167, where Nestor reserves the choice to himself ("those whom I shall pick out"). | `i` "men called to the task"; the new-renderings row records the reason and the departure from the Odyssey's κλητός "invited" (17.386). |
| 119 · `i`, `n` | medium | `i` "I wish, in return, to make him content": ἂψ is "back, again", not a return for anything, and the note's own gloss ("back … to undo the deed") disagrees with "in return". | `i` "I wish to make him content again"; note "‘back, again’". |
| 142 (τίσω δέ μιν) · `l` | medium | `l` "as equal to Orestes" makes ἶσον an adjective; the note (and `i`) take it as the adverb "equally" with the dative. | `l` "equally with Orestes". |
| 154 · `n` | medium | τελέουσι called "contracted future of τελέω". It is the uncontracted epic form (Attic τελοῦσι). | "the uncontracted epic future of τελέω (Attic τελοῦσι)". |
| 158 (δμηθήτω) · `n` | medium | "ἀδάμαστος … comes in the next line": it is in the same line 158, in the next unit. | "in the next unit, in the same line". |
| 185 · `n` | medium | ἄρετο called "aorist middle of αἴρω". It is the aorist of ἄρνυμαι, the verb the draft's own note on 124 gives for ἄροντο. | "aorist middle of ἄρνυμαι ‘win, take for oneself’". |
| 128 · `n` | minor | The note asserted Achilles as the subject of ἕλεν as a bare fact, and "αὐτός … set against ἐξελόμην" without saying that line 129 ends on αὐτός with no stop, so the word could be read with ἐξελόμην; "literally ‘well-built’, ‘well-settled’ in the English" was unclear. | Note now gives the grammar (a third-person aorist, Agamemnon would say ἕλον, so it can only be Achilles), says the other construction is possible and not the one followed, and says ‘well-settled’ is the free English. Reading kept (see decisions). |
| 135 (εἰ δέ κεν αὖτε) · `n` | minor | Note of 138 words (validator band is 130). | Trimmed to 125 words, nothing dropped but the gloss of ἄστυ μέγα Πριάμοιο. |
| 167 · `n` | minor | ἐπιόψομαι called a future without remark, though it stands with ἂν. | "future in form, though with ἂν it works like a subjunctive". |
| 170 · `n` | minor | "appears to be another man" about the Halizonian Odius; the published parts settle it (iliad-015 ln 856, iliad-027 ln 38–42: Agamemnon kills him). | "who was killed in Book 5 and so must be another man". |
| 139 · `i` | minor | `i` dropped αὐτός ("let him choose for himself"). | "and let him choose twenty Trojan women himself, …" |
| 125 · `n` | minor | "ἠνείκαντο … ‘carried off for themselves’" against `l` "carried off for me". | "‘carried off’ as a winner does, with μοι ‘for me’". |
| 204 · `i` | minor | `i` "the dearest of men" turns the predicate φίλτατοι ἄνδρες into a partitive. | "are men most dear". |
| 202 · `n` | minor | new-renderings.md said the other ancient guess for ζωρότερον ("warmer") was "named in the note"; it was not. | The note now says another old guess is ‘warmer’. |
| new-renderings.md | minor | Several rows contradicted the unit: πιθήσας (`i` cell "gave way to"; unit says "obeyed", table 6.183 "obeying"); ἂψ row; εὐνή row ("mounted" listed as avoided); κλητούς ("invited" called merely reserved, no departure recorded); λιγείῃ φόρμιγγι; δεικνύμενος; κλισμοῖσι τάπησι; the ἀασάμην row ("kept for that tense" was inaccurate); "Departures from the Odyssey: none" (there are two). | All rows rewritten to match the units; three rows added (ὣς δ’ αὔτως, τίσω … ἶσον Ὀρέστῃ, the shared αἶψα … ἐγγὺς ἐόντα line); the Departures paragraph now lists κλητούς and μέλαθρον. |
| 115 · `n` | nit | "the plural here means the separate occasions" stated as fact. | "most likely means". |
| 116 (ἀασάμην) · `n` | nit | "αὐτός … means that he does not wait to be forced": not in the Greek. | "stresses that it is he who says so". |
| 119 · `n` | nit | λευγαλέος glossed "pitiful, wretched"; "wretched" is reserved for δύστηνος in the Odyssey table. | "pitiful". |
| 121 · `n` | nit | ὀνομήνω "a subjunctive". | "an aorist subjunctive". |
| 160 · `n` | nit | "earlier-born in birth". | "elder in birth". |
| 179 · `n` | nit | "πειρᾶν … (Attic πειρᾶν)" says nothing. | Parenthesis removed. |
| 185 · `n` | nit | δαιδαλέῃ glossed "finely wrought" against `l` "wrought" (table 4.135: `l` "wrought", `i` "finely wrought"). | "fine, wrought". |
| 193 · `n` | nit | ταφών glossed ‘astounded’; the English (and the table's τάφος) is "amazed". | ‘amazed’. |
| 204 · `n` | nit | ὑπείναι. | ὑπεῖναι. |

## The drafter's doubts, decided

- **ἀασάμην "bewildered" (kept).** The Iliad's own table has ἄτῃ ἄασας (8.237) "bewildered" and ἄτη "bewilderment" (1.412, 2.111); the Odyssey table has ἀάω · ἄτη "bewilder" · "bewilderment" (21.296–302). "Blinded" belongs to the passive ἀάσθη (4.503) and ἄασαν (10.68), different forms in different contexts, and would break the echo with ἄτας two lines up. The new-renderings avoided-cell, which said "blinded" was "kept for that tense", was corrected to say exactly this.
- **Subject of ἕλεν at 129 (Achilles, kept).** A first-person verb would be ἕλον; the only third person in the whole offer is the "him" (Achilles). The alternative (αὐτός going with ἐξελόμην across the line end) is now named in the note and not followed.
- **The dual τὼ / βάτην / εὐχομένω (182–193, kept as drafted).** The note already says what the Greek supports: two men, Odysseus one of them (192, ἡγεῖτο), the other not named; it does not pick Ajax or Phoenix, and does not make the heralds part of the dual. Not edited.
- **Odius at 170 (kept, sharpened).** See the change above; the herald is a different man because the Halizonian Odius is dead by 5.40.
- **ζωρότερον (kept "stronger").** The note hedges (usual explanation, not certain); it now names ‘warmer’ as the other old guess, as new-renderings.md claimed.
- **The 190–193 cut (correct).** Unit 190 ends at the ano teleia after αὐτοῖο, a real stop, four lines; the sentence 190–194 is five lines, so the cut at the ano teleia (mid-line 193) is the rule, not an exception.
- **The 135b–138 cut (correct).** 135b–140 is six lines, so a cut at a comma is allowed; the cut after Ἀχαιοί (138) is the strongest syntactic break (protasis and first imperative together, then the new δέ-clause 139–140). The alternative cut after ἀλαπάξαι (136) leaves the second unit four lines but splits protasis from main verb; refused as the weaker pause.

## Findings considered and refused

- "On the other hand" for αὖτε at 135 (l and i). LSJ gives it, and the shipped Odyssey renders the same εἰ δέ κεν as "But if, on the other hand," (odyssey-026). Kept.
- ἦ … ἦ at 197 taken as "either … or" (not a double question). The reading is the standard one and the note labels the words as printed. Kept.
- τοῦτον at 118 asserted as Achilles. The only reading the context allows; kept ("still unnamed").
- "great mind" (i) for μεγάλας φρένας at 184 against `l` "wits". The table fixes "wits" in `l`; `i` varies between "mind" and "sense" in published parts. Kept.
- "Eetion" against iliad-004's "Eëtion". Later parts (039, 047) ship "Eetion"; kept.
- μέλαθρον "roof" at 204 (not "rafter" of 22.239, not "palace" of 2.414). Matches the shipped odyssey-089 "beneath the roof" and the note says it stands for the hut. Kept, and listed under Departures.
- "Pherae", "Hire" etc. Latinised as the other Iliad names; kept.
- The about-text says "praying to Poseidon" while the Greek withholds the name. The note at 182 says so; a summary line may identify him. Kept.
- Scansion: the packet flags nothing. Spondaic fifth feet (126, 137, 144, 150, 155, 168) are an ordinary licence, and the scanner's other licences (131–132, 144, 166, 168, 180, 191, 197) are all normal Homeric ones (digamma, correption, lengthening before μ/λ, synizesis); no sentence added to any note.
- odyssey-015 (4.124) and odyssey-045 ship "rug" for τάπης where four other Odyssey units ship "carpets". Published; not touched here (the iliad part follows the majority and the table). Worth the owner's glance.
- odyssey-014 ships "spoke" for προσέφη where the Odyssey table says "addressed"; the Iliad part follows the shipped unit for the shared line (see 196). Owner may align either way.
- Remembered English: nothing found that arrives fully formed. Checked in particular "worth as much as many peoples", "the udder of the plough-land", "lyre and all", "mix it stronger", "set up a larger mixing-bowl", "unrelenting and unsubdued": each follows the case relations and the tables; no change.

## Second sweep (after the edits)

Re-read every unit's note against its final `l`/`i`; re-ran the mechanical checks (line count of `l` = `t`, no line break in `i`, “/” balanced and on the right units, typographic ’ only, note length 20–130 words: the two long notes are now 127 and 125, `t` unchanged, tiling of the edition intact); re-checked every Greek form quoted in a note against the unit's `t` or as a lemma; re-checked the cross-references (112, 116, 118, 158, 69, 192, 193, 4.317, 2.434, 1.328, Od. 1.148, 3.340, 3.342, 7.184, 8.73, 18.422, 4.59 all verified against the published files or the tables). Nothing further found.
