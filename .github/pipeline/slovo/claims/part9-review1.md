# Part 9 review — pass 1

Reviewed against `conventions.md`, `slovo-proem.json`, `slovo-part1.json`, `slovo-part8.json`
(the models), `parts.json`, `source-1800.txt`, and `part9-draftnotes.md`.

**Source-text check (item 1):** the 25 units' `t` fields, concatenated with single spaces,
reproduce `source-1800.txt`'s part-9 span character-for-character (verified programmatically:
sha256 of the whitespace-normalised span = `924b413c9...3a43e3f6`, matches `parts.json`, and the
draft's own concatenation is byte-identical to that span, 1925 chars / 301 words). **No `t`
defects.** Paragraph check (item 7) also re-derived independently: `source-1800.txt` has a blank
line immediately before "Прысну" and immediately after "Половецкомъ." and **none** inside that
span — part 9 is genuinely one source paragraph, so `p: true` on unit 1 only is correct.

## Blocking defects

1. **Unmet echo-check on the part's three highest-risk passages (units 3, 11–12, 20–25)
   — conventions.md "Translation provenance."** Every prior part's `LOG.md` entry records an
   explicit echo-check pass against known translations for that part's famous lines (part 2 found
   and fixed 8 Nabokov echoes; parts 5–8 each list specific phrases checked). No such pass is
   logged for part 9, and `part9-draftnotes.md` only offers a blanket assurance ("No modern
   English translation was consulted... built fresh") rather than a demonstrated phrase-by-phrase
   check. This part contains three of the poem's most anthologized passages — the "Игорь спитъ,
   Игорь бдитъ" triad (unit 3), the Donets/Igor dialogue (units 11–12), and the Gzak–Konchak
   falcon riddle (units 20–25) — which the task brief itself flags as high-risk. I have no web
   access to compare directly, so I cannot confirm or clear specific lines, but per house process
   this part should not ship without the same documented echo-check every other part received,
   with particular attention to unit 3's "Igor sleeps, Igor keeps watch" phrasing and unit 21/23's
   "gilded arrows" / "falcon-chick" wording, which have very few natural English phrasings and are
   the likeliest to coincide with a well-known rendering by accident.
   **Fix:** run and log an explicit echo-check pass (as in every other part's `LOG.md` entry)
   before publishing; reword anything that turns out to match a known translation too closely.

2. **Unit 14 — `l` and `i` give opposite readings of "Не тако ли."** `l` = "Was it **not thus**...
   [with] the river Stugna having a poor stream..." (i.e. affirms the description that follows,
   "thus" = "so/likewise"). `i` = "Was it **not otherwise**... with the river Stugna" (i.e. denies
   the description that follows, "otherwise" = "differently/unlike"). "Thus" and "otherwise" are
   near-antonyms; a reader comparing the two fields side by side gets contradictory signals. The
   note's own gloss ("`Не тако ли`, 'was it not [rather] thus,' i.e. 'unlike you'") tries to have
   it both ways and doesn't resolve which reading is intended. Given the note explicitly frames
   this as a contrast with the Donets' kindness (matching `i`), `l` is the one out of step.
   **Fix:** make the two consistent. Either (a) revise `l` to carry the same contrastive sense,
   e.g. `l`: "Was it not otherwise, [Igor] said, [with] the river Stugna — having a poor stream,
   having swallowed up others' streams, and scattered its rills upon the thicket?" — or (b) if the
   polarity is itself genuinely unsettled in the scholarship (plausible, given «тако» most
   literally just means "so/thus"), say so explicitly in the note instead of asserting one
   confident reading while `l`/`i` silently disagree.

3. **Units 20/22/24 are isolated speech-tags split off from their quotations, against this
   part's own established pattern and the model files' pattern.** In the source, each of
   "Млъвитъ Гзакъ Кончакови: аже соколъ..." / "Рече Кончакъ ко Гзѣ: аже соколъ..." / "И рече
   Гзакъ къ Кончакови: аще его..." is **one** period-bounded sentence (13, 15, and 26 words
   respectively — nowhere near the "60+ words" threshold conventions.md gives for splitting at a
   colon). The draft splits each at the colon into a bare 3–5-word tag unit (20, 22, 24) plus the
   quote (21, 23, 25). This breaks the 12–30-word guidance for no textual reason and, worse, is
   inconsistent with how this *same draft* handles the identical pattern two units earlier — unit
   11 ("Донецъ рече: Княже Игорю!...") and unit 12 ("Игорь рече, о Донче!...") both correctly keep
   tag and quote fused as one unit — and with the model files: part 1's "И рече ему Буй Туръ
   Всеволодъ: одинъ братъ..." and part 8's three "...аркучи: о вѣтрѣ!..." /"...аркучи: о
   Днепре..." /"...аркучи: свѣтлое..." units all keep a short speech-tag fused with the quote that
   follows it, never isolated.
   **Fix:** merge unit 20 into 21, 22 into 23, 24 into 25 (concatenating `t`/`tr`/`l`/`i`/`n`
   accordingly), giving three units of 13, 15 and 26 words — all inside the 12–30 target. (Re-index
   the remaining units after the merge.)

4. **Unit 21 `tr` — stray Cyrillic letter.** The transliteration line reads `аže sokolŭ kŭ gnězdu
   letitŭ, ...` — the first character is Cyrillic а (U+0430), not Latin a (U+0061). `tr` must be
   pure Latin script (it's "a reading aid for the Cyrillic"); a mixed-script leak like this will
   look broken to a reader and won't round-trip correctly through any Latin-only tooling/search.
   **Fix:** change to `aže sokolŭ kŭ gnězdu letitŭ, sokoliča rostrěljaevě svoimi zlačenymi
   strělami.` (Latin a). (If units 20/21 are merged per defect 3, apply the fix to the merged
   unit's `tr`.)

5. **Unit 23 `tr` — same stray-Cyrillic bug.** `tr` reads `аže sokolŭ kŭ gnězdu letitŭ, a vě
   sokolca oputaevě krasnoju diviceju.` with the same Cyrillic а in first position.
   **Fix:** change to `aže sokolŭ kŭ gnězdu letitŭ, a vě sokolca oputaevě krasnoju diviceju.`
   (Latin a). (If units 22/23 are merged per defect 3, apply the fix to the merged unit's `tr`.)

6. **Unit 13 `tr` — vowel mistransliterated.** `t` has "Чрьнядьми на **ветрѣхъ**." with a plain
   е (not ѣ) in "ветрѣхъ," but `tr` renders it "Črĭnjadĭmi na **větrěxŭ**." — treating that е as
   if it were ѣ. Per convention only ѣ maps to ě; plain е maps to e (except word-initial, which
   this is not — it's mid-word after "в"). This looks like the drafter's eye slipping to the
   familiar root вѣтръ ("wind," spelled with ѣ, used repeatedly in part 8) rather than transliterating
   the actual printed word.
   **Fix:** change `tr` to `strežaše e gogolemŭ na vodě, čajcami na strujaxŭ, Črĭnjadĭmi na
   vetrěxŭ.` (single e, not ě, in "vetrěxŭ").

## Non-blocking watch items

- **Unit 5's note says Ovlur is "spelled Овлуръ here, Влуръ two sentences on."** By source-sentence
  count (period-bounded), «Влуръ» (unit 10) is actually the *third* sentence after the one ending
  in «разумѣти.» (unit 5), not the second — there are two full intervening sentences (units 6, and
  the long unit 7–9 sentence). Doesn't affect the translation; tighten to "a few sentences on" or
  recount, at the drafter's discretion.
- Units 1, 4, 6, 7, 15, 16, 18, 20, 22, 24 fall below the 12-word guidance. For all of these except
  20/22/24 (covered above as a blocking defect) the short length matches a genuinely short,
  independently period- or colon-bounded sentence in the source (e.g. unit 4 "Комонь въ полуночи."
  is a complete sentence on its own, matching this part's own note calling it the poem's most
  notoriously truncated line) — not a segmentation problem, just a short source sentence. No fix
  needed.
- Grammar/dual claims (претръгоста = 3rd-dual aorist for Igor+Ovlur; рострѣляевѣ/опутаевѣ/нама/наю
  = 1st/dat./acc. dual for Gzak+Konchak) all check out against the actual OES paradigm and are
  correctly kept as two distinct, non-conflated pairs, matching `part9-draftnotes.md`'s own summary.
- History claims (1093 Stugna/Rostislav drowning per the Primary Chronicle; Vladimir Igorevich as
  the "falcon-chick" hostage who later married a daughter of Konchak's; the Dnepr-vs-Stugna naming
  wrinkle) are all stated with hedges appropriate to what's actually recoverable, and check out
  against standard chronicle history — no overclaiming found.
- Dark places (Комонь въ полуночи; Князю Игорю не быть; стругы ростре на кусту; the стугою/Стугна
  pun) are all flagged as uncertain rather than resolved with invented confidence, consistent with
  house style.
- No `v: true`, no `\n` inside any `t`, glossary correctly absent (glosser runs separately) — all
  clean.
