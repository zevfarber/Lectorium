# Slovo pipeline — run log

2026-09-14 15:58 UTC · part 2 · STOPPED before drafting. Step-1 verification found part 2's
`chars`/`sha256` in `parts.json` don't match the text its own `opens`/`ends` cut from
`source-1800.txt` (word count matches; chars 1518 vs recorded 1519; sha256 mismatch). Parts
0,1,3–10 all verified clean against the same method; the whole poem still tiles exactly with
part 2's boundaries, so the text/cut points are trusted, only the recorded metadata is off.
Nothing drafted, nothing published, no other files touched. Details in QUESTIONS.md.

2026-09-14 18:01 UTC · part 2 · 15 units, 177 glossary keys · 2 review passes. Pass 1 found 8 units echoing Nabokov 1960 (incl. 'Fierce Bull Vsevolod') — rewrote fresh from OES; also fixed a false Stribog date (988→980), a vocative error, a missing paragraph marker, header/glossary drift.

2026-09-15 07:05 UTC · part 3 · 14 units, 205 glossary keys · 2 review passes. Echo-checked Gorislavich, plowmen/ravens, black-earth/blood, wine-feast lines — clean. Fixed validate_slovo.py gate 3 (paragraph-start check; parts 3-7 share one paragraph, no p:true) — see QUESTIONS.md.

2026-09-16 01:11 UTC · part 4 · 13 units, 216 glossary keys · 2 review passes. Fixed a false grammar claim, a wrong glossary lemma, 3 case-label errors. Echo-checked grass/tree opening, women's lament, Kobyak battle, saddle-exchange — clean. вступилъ/обида mismatch, жиръ kept flagged, not emended.

2026-09-16 07:16 UTC · part 5 · 15 units, 193 glossary keys · 2 review passes + fixes. Echo-checked Golden Word opening, dream imagery, closing line (reworded) — clean. Fixed dual/plural glossary errors, a false Sharukan-death claim, a Хинова part6/7 mislabel. Dense dark-places passage.

2026-09-16 13:30 UTC · part 6 · 30 units, 273 glossary keys · 2 review passes + fixes. Echo-checked Golden Word continuation, Volga/Don hyperbole, Chaga/Koshchei price line, prince roll-call, refrain, "six-winged ones" — clean. Fixed 6 defects: false dual claim, wrong part1 cross-ref, misquoted refrain spelling, 2 silently-resolved cruxes, self-contradictory note.

2026-09-16 19:40 UTC · part 7 · 19 units, 248 glossary keys · 2 review passes + echo-check pass, fixes at each stage. Pass 1 fixed 10 defects (wrong part6 spelling cross-ref, false-confidence crux claims, a вонзить mistranslation, an oversegmented unit, geography error on Dudutki, 2 famous-phrase echoes, a wrong Boyan-count). Pass 2 clean. Echo-check flagged 3 more phrase-level risks (St. Sophia bells couplet, Nemiga "winnowing soul from body", Boyan proverb closing) — all reworded; also fixed a glossary typo inherited from part6 (`бологомъ` mixed Cyrillic/Latin) and a wrong themselves/himself gloss. See QUESTIONS.md re: the same typo still live in published part6.

2026-09-17 01:17 UTC · part 8 · 11 units, 117 glossary keys · 2 review passes + fixes. Echo-checked cuckoo opening, Wind/Dnepr/Sun addresses, thirst close — reworked Wind and Dnepr lines (close to known renderings). Fixed рече tense, false chronicle cite, overclaimed лады/ладѣ case.

2026-09-17 07:22 UTC · part 9 · 22 units, 222 glossary keys · 2 review passes + fixes. Echo-checked "Игорь спитъ, Игорь бдитъ" triad, Donets/Igor dialogue, Gzak-Konchak riddle — clean (recall-based, no verbatim matches to known renderings). Pass 1 fixed a l/i polarity contradiction (unit "Не тако ли... Стугна"), merged 3 speech-tags wrongly split from their quotes at a colon, 2 mixed-script tr typos.

2026-09-17 13:05 UTC · part 10 (final) · 10 units, 76 glossary keys · 2 review passes + fixes. Echo-checked return/Pirogoshcha/toast/Amen lines, reworked toast & lands/towns i. Fixed grammar labels, content drift, cross-ref, stripped process-asides from n. Text phase complete; DONE for next run.
