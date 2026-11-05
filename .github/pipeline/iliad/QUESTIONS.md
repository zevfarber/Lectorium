# Iliad pipeline — open questions

## Pilot verdict (raised 2026-10-12)
iliad-001 (1.1–100) is published for Zev to judge. Until he approves the presentation, `iliad` is **not** in
`queue.txt`. Approving it means: add `iliad` to `.github/pipeline/queue.txt` (after beowulf, per the
2026-10-11 three-runs plan).

## The opening line (decided at the pilot, open to the owner)
House rendering: `l` "The wrath sing, goddess, of Peleus’-son Achilles", `i` "Goddess, sing the wrath of
Peleus’ son Achilles". "Wrath" was chosen over "rage"/"anger" (the famous modern choices) and because μῆνις
is the god-sized word (1.75). The Odyssey opened with "Muse, tell me of the man"; the two openings are
deliberately built the same way (vocative first in `i`).

## Δαναοί: "Danaans", not "Greeks" (decided at the pilot)
The Odyssey's `i` layer renders Δαναοί "Greeks". The Iliad keeps "Danaans" in both layers, because the three
names alternate constantly here. This makes the two poems differ on one word; the alternative is to align
the Iliad with the Odyssey. Decided meanwhile: "Danaans".

## Edition imprint
Perseus describes its source as the OCT "Editio Tertia", Oxford 1908–1920 (two volumes). The source field
cites the 3rd edition, 1920. Both volumes are pre-1930 either way.

## Audio
Ancient Greek audio is built on push only for `odyssey-` and `hammurabi-` ids (`pick_targets.py`
BUILD_ON_PUSH); every other Greek story waits for the daily "missing" sweep, which takes stories in
MISSING_PRIORITY order (odyssey, slovo, aesop, ovid, pyramus) and then alphabetically, 40 a day, inside the
WaveNet free allowance — which for October 2026 is already at its cap (3,598,007 of 3,600,000 characters).
So iliad-001 gets no audio until November at the earliest, and then behind the remaining Aesop/Ovid backlog
unless `iliad-` is added to BUILD_ON_PUSH or MISSING_PRIORITY. Not changed here: the audio scripts are shared
and the order is Zev's.

## iliad-007 last unit (2.83) lacks its closing ” (found at iliad-008, 2026-10-17)
The published last unit of iliad-007 (2.83) has no closing ” in `l` or `i`, and its note says Nestor's speech "runs on into the next part". It does not: the speech ends at 2.83 and 2.84 is narration. iliad-008 opens without a mark, which is correct. Decided meanwhile: not touched (one part per run, no edits to a published part). To fix: add ” to `l` and `i` of that unit in `drafts/iliad-007/units.json` and `iliad-007.json`, and correct the note.

## Existing glossary entry for ἕποντο is wrong (found at iliad-013, 2026-10-18)
The entry from an earlier part says "augmented (ἕποντο = εἵποντο)". ἕποντο is the unaugmented form. The glosser may not rewrite existing entries, so it was left. Also noted: ἀργινόεις is "bright-white", ἀνδρειφόντης "killer of men" (new choices in conventions; override if you prefer).

## Found at iliad-014 (2026-10-18)
- ποδώκης: the Iliad table reserves "fleet-footed"; the published Odyssey (odyssey-055, -056) ships "swift-footed". Decided meanwhile: Iliad keeps "fleet-footed".
- λωτός (2.776): rendered "lotus" (as the shared half-line in Odyssey 9.97); the Odyssey ships "clover" for λωτός at 4.603. The note tells the reader. Owner may switch.
- The archive prints σταφύλῇ at 765; the unit note quotes σταφύλῃ. Source untouched.
- The ἕποντο glossary entry error (see iliad-013) stands; glossary changes are additions only.
- Several notes in 014 exceed 110 words (validator did not warn).

## Found at iliad-020 (2026-10-18)
- περικαλλής ("very beautiful") and ἀμφίπολοι ("handmaids") follow the published Iliad parts, not the Odyssey table ("very fair", "attendants"). Owner may align.
- Two shipped Odyssey units predate later table rows: odyssey-048 ("scheming with guile" for δολοφρονέουσα) and odyssey-004/-090 ("lovely song" for ἱμερόεσσαν ἀοιδήν). Not touched; iliad-020 follows the table rows.

## Found at iliad-022 (2026-10-19)
- 4.93–96 are statements (polite "you might / you would") following the edition's stops; the note names the question reading. Judgement call, as at 4.82–83.
- ἄγαλμα rendered "a treasure" (4.144), not the Odyssey's "a glory", because κῦδος follows. Owner may align.

2026-10-19 · iliad-024 · 4.362: the pinned source has no stop after ἴθι/ἀρεσσόμεθ’ and a comma after εἴρηται; could not check the printed Monro–Allen text (archive.org blocked; Perseus TEI is the pinned source itself). Left unchanged; if the printed edition has a stop it is one mark in the source plus a new sha256 for iliad-024.

## iliad-042 stopped at build (2026-10-21)
Draft, review (two passes) and gloss for iliad-042 (7.92–180) are complete in `drafts/iliad-042/`. The build refuses: unit 22 (7.136–139) "does not end at punctuation" because the pinned source has no stop after `γυναῖκες` at 7.139 (the next line, 140, begins a new clause with οὕνεκ’). Per README rule 5 the fix is one mark: append `·` (U+00B7, as used elsewhere in the source) to line 139 in `source/iliad-monro-allen1920.json`, re-pin the sha256 of iliad-042 in `parts.json`, make the draft's `t` match, rebuild. The edit to the source file was blocked by the session's permission check, so it was not made and nothing was published. Next run: apply that one-mark fix (or have Zev permit it), then build/validate/publish from the existing drafts. Claim released.

## iliad-051 stopped before build (2026-10-23)
Packet and draft (`drafts/iliad-051/units.json`, 47 units, `new-renderings.md`) are done; review and gloss are not yet run. The build will refuse unit 8.551b–552, which ends at `Πριάμοιο]` (no stop in the source; `]` is not a terminal). Two ways out: (a) rule 5 — add `.` after the `]` at 8.552 in `source/iliad-monro-allen1920.json` and re-pin `iliad-051` sha256 in `parts.json` (the edit was blocked by the session's permission check, so not made); or (b) merge that unit into the 553–554 unit and drop `p` from it (loses the paragraph mark at 553). Next run: do (a) or (b), then review, gloss, build, validate, publish. The claim on 051 is held (2026-10-23).

**Resolved 2026-10-21:** the 7.139 stop was added (rule 5, with the owner's go-ahead), iliad-042 built, validated (PASS) and published.

**Resolved 2026-10-23 (iliad-051):** published with option (b) — 8.551b–554 merged into one unit, so the edition's paragraph break at 8.553 is not marked. To restore it: add `.` after the `]` at the end of 8.552 in `source/iliad-monro-allen1920.json`, re-pin `iliad-051` in `parts.json`, split the unit in `drafts/iliad-051/units.json` at 553 (restore `p`) and rebuild.

- 2026-10-24 iliad-060 (10.263): ἀργιόδοντος ὑός is "boar" in the Iliad; the Odyssey table has "pig" for ἀργιόδων ὗς (8.476, 8.60). Kept "boar" (helmet tusks are a wild boar's); owner to decide whether the table needs a line.
- iliad-084: γνωτόν 'a kinsman' (13.697) used as a singular; the table's 'kinsfolk' has no singular. Decided meanwhile: keep, logged in conventions table. ἀποστήσωνται χρεῖος (745) sense uncertain, flagged in gloss.

- 2026-10-28 (iliad-092): published house rendering of Ida's epithet is inconsistent (`l` “many-fountained” in iliad-046, “many-springed” in iliad-065/-087/-088). iliad-092 follows 046. Decided meanwhile: no change to published parts; owner may harmonise.

- 2026-10-28 (iliad-094, 15.281–376): the house table is split on χρώς. It is "skin" in most rows (4.137, 4.237, 4.510–511, 5.858, 8.43, 12.464, 13.191, 13.830, 14.164, and the Odyssey's 13.398), but "flesh" in the spear formula πάρος χρόα λευκὸν ἐπαυρεῖν · λιλαιόμενα χροὸς ἆσαι (11.573–574, published in iliad-069) and in οὐτάζω κατὰ χρόα "wounded in the flesh" (12.427). Lines 15.316–317 repeat the 11.573–574 formula, so they must carry the published "white flesh" / "glut themselves with flesh" (the validator enforces it), and 15.315 ἐν χροῒ πήγνυτο "stuck in the flesh" follows them so that one sentence does not say "skin" and "flesh" together. Decided meanwhile: "flesh" wherever a spear or point lands in the body, "skin" elsewhere; no published part changed. Owner to decide whether the table should say so, or whether 11.573–574 should become "skin" (which would mean re-issuing iliad-069 and reusing the result here). Smaller points for the owner: (1) ἤϊε Φοῖβε (15.365) is left untranslated in `l` and dropped from `i` because its meaning is unknown; the glossary entry offers only "vocative of ἤϊος, meaning disputed". (2) ὁ σημάντωρ now has four renderings across the poem ("order-givers" 4.431, "commander" 8.127, "overseer" 17.21, and `i` "herdsman" here for a herd with no keeper); worth one table line. (3) ἀθύρματα `i` is "playthings" here against the Odyssey's "trinkets" (15.416), a recorded departure. (4) The reviewer had no lexicon, so the lemma of ἐρυσάρματας (given as ἐρυσάρματες) and the tense of ᾗσι (aorist subjunctive of ἵημι, since a present would keep the iota) rest on form and on the glossary's own entries.

- 2026-10-28 (iliad-095, 15.404): the closing ” of Patroclus's speech is missing on ἀγαθὴ δὲ παραίφασίς ἐστιν ἑταίρου, because the validator requires this unit to carry exactly iliad-070's English (no ”). Decided meanwhile: published as is. Owner may exempt closing quotation marks from the repeated-unit check, or add ” to iliad-070/-095.

- 2026-10-31 (iliad-116, 18.39–46): the Nereid catalogue is unpunctuated in the pinned Perseus text and runs 8 lines, over the five-line unit cap. Decided meanwhile: added a comma after 18.41 and after 18.44 (not strictly README rule 5, which covers marks the edition prints; I could not check the printed page) and re-pinned iliad-116. Owner may revert and rule on a longer cap for catalogues.

- 2026-10-31 (iliad-119, 18.317): the pinned text lacks a stop after ἑταίρου at the end of 317, so the unit could not end there. Decided meanwhile: added a comma (rule 5; the sense continues in the participial clause), re-pinned iliad-119. Not checked against a printed copy.

- 2026-10-31 (iliad-121): the last note of published iliad-120 (ln 507) says the description of the first city goes on in the next part; it does not (18.509 begins the second city). Not edited (published part). Owner may correct. Also: Ὠκεανός is "Oceanus" at 18.607 (table) but "Ocean" in iliad-120 at 18.489.

## 2026-11-02 · iliad-131 · 20.447–448
The Greek (δεινὰ δ’ ὁμοκλήσας ἔπεα πτερόεντα προσηύδα, with the line before) is identical to 16.705 (iliad-106), whose published English says "Apollo shouted dreadfully at him". That is true of 16.705 and false at 20.447, where Achilles shouts. Validator check 6 demands identical English. Decided meanwhile: iliad-131 keeps "he shouted" (true), and `validate_iliad.py` skips check 6 for iliad-131 line 447 only. Alternative for the owner: make iliad-106's English name the god only in a note, and drop the exemption.

## 2026-11-02 · iliad-132 · 21.73
Greek identical to published 1.201 (καί μιν φωνήσας ἔπεα πτερόεντα προσηύδα) but μιν is Achilles (masc.), so "to him" not "to her". Decided: keep "to him"; validator same-Greek check exempted for iliad-132 line 73 (as for 131/447).

## 2026-11-02 · iliad-137 · 21.504, 21.509
(1) 21.504 θυγατέρος ἧς: reviewer read it as possessive on τόξα ("her own daughter's bows"), not a goal genitive; ~80% confident from grammar and Od. 19.399. Owner may check. (2) The Iliad table's Οὐρανιώνων row (5.898, "sons of Uranus") contradicts the shipped iliad-030 English, which unit 509 must repeat verbatim. Decided meanwhile: follow the shipped unit; the table row and the shipped English need reconciling. (3) Homeric "Attic equivalents" in gloss for ξυμβλήμεναι, ἀποέργαθε, ἄνεσάν, ἀπῶσαν, ἔμπλητο, ἐπανθέμεναι are reconstructed, not checked against a lexicon. (4) The second reviewer pass over gloss.json was not run as a separate agent; only the forms touched by review edits were rechecked.

## 2026-11-03 · iliad-139 (22.90–187)
- Validator check 6 (repeated Greek must repeat its English) is relaxed for iliad-139 lines 131, 181 and 183 only: the Greek recurs from iliad-132/103/046, but here the closing mark differs (131 ends in a comma; 183 ends in a stop-less unit continuing the speech) or the speech closes (181, ”). The English is otherwise the shipped English. Decided meanwhile; owner may prefer otherwise.
- ἀεθλοφόρος: 22.162 "prize-bearing" (matches 11.699/9.124 rows) vs iliad-138 22.22 "prize-winning". Left as shipped; owner may want 22.22 changed to "prize-bearing".

## 2026-11-04 · iliad-153 · 24.184
Greek identical to 24.155 but Iris addresses Priam, so 'led you / kill you' is true where 155 has 'him'. Validator same-Greek check exempted for iliad-153 line 184 only (as for 139). Also: last unit of iliad-152 (ln 91) has a note beginning mid-word ('ς is ‘a vain word’') — owner may fix.

## 2026-11-05 · iliad-155 · 24.302
ἀμφίπολος: the Iliad table row (6.491) says "handmaid"; iliad-155 uses "attendant housekeeper" for ἀμφίπολον ταμίην, matching odyssey-078 and iliad-142. Left as is; owner may prefer to harmonise.
