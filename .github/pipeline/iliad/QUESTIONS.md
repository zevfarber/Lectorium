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
