# Part 6 review — pass 2 (final)

## Method
- Re-read `conventions.md`, `parts.json`, `slovo-proem.json`, `slovo-part1.json`, `slovo-part5.json`,
  the current 30-unit draft, and `part6-review1.md`.
- Independently re-extracted part 6 from `source-1800.txt` (whitespace-normalised) using the
  `opens`/`ends` strings in `parts.json`. Result: **397 words, 2461 chars, sha256
  `d589e127dff2b0d909b381b10e6f8036a786dc1beadfa70572ac2066526d08c8`** — matches `parts.json`
  exactly.
- Concatenated all 30 units' `t` fields (single spaces, whitespace-normalised) and diffed against
  that extraction programmatically: **exact match, zero differences.** None of the six fixes
  touched any `t` field.
- Confirmed no `p: true` anywhere (still correct — part 6 opens mid-paragraph, as pass 1 established
  and this pass re-confirms from the raw source line).
- Pulled the actual paragraph line from `source-1800.txt` directly (not via the JSON files) and
  located the three refrain occurrences by eye to check unit 30's claim independently of any derived
  file.

## Re-verification of the 6 fixes — all hold

1. **Unit 3 (мужаимѣся).** Concatenating the print's own three pieces from `t` — "му" + "жа" +
   "имѣся" — gives м-у-ж-а-и-м-ѣ-с-я = **мужаимѣся**, letter for letter matching what the note now
   quotes. Fixed correctly; no residual ъ/ѣ mismatch.

2. **Unit 7 (Urim/Rimov hedge).** `i` now reads "the men of Urim — probably Rimov — cry out," which
   preserves the uncertainty the note asserts two sentences later ("plausible but far from
   certain"). No contradiction remains; `l` still correctly keeps "Urim" untranslated.

3. **Unit 13 (плаваша).** Confirmed against this project's own established paradigm: true 3rd-dual
   aorists in `slovo-part5.json` end in **-ста** (слѣтѣста, помѣркоста, погасоста, поволокоста,
   погрузиста), and true masc. o-stem duals take **-a** (два **сокола**, cf. the dual analysis of
   ваю/самаю/соколома throughout part 5) — so a genuine dual of шеломъ would be **шелома**, not
   шеломы. `шеломы` (ending -ы, matching the plural instrumental/accusative pattern seen elsewhere
   in this very part, e.g. unit 9's «Донъ шеломы выльяти», unit 12's «живыми шереширы») is
   grammatically plural, and `плаваша` (-ша) matches the project's own documented 3rd-plural aorist
   ending (побѣгоша, прегородиша in part 1). The rewritten note's claim is correct: `ваю` is a true
   dual, `плаваша` is not. (Minor, non-blocking stylistic note: the note's "cf. рекосте, расхытисте"
   cites 2nd-person -сте plural forms as comparanda for a 3rd-person -ша plural form — different
   person, different ending, same general "plural-not-dual" phenomenon. This is loose but not false;
   I would not hold up gating for it.)

4. **Unit 17 (времены → "times", not "weights").** `l` now reads "hurling times through the clouds,"
   matching `t`'s printed «времены» exactly, with the бремены/"weights" reading confined to `n`
   as the note itself promises. No silent emendation remains in `l`.

5. **Unit 21 (falcon/wolf cross-reference).** Checked against `slovo-part1.json` directly: unit 14
   there gives Vsevolod's Kurians the **wolf** simile («сами скачють акы сѣрыи влъци въ полѣ»,
   glossed "the recurring wolf-simile"), and unit 10 gives the **falcon** image to Igor's warriors
   generally («Не буря соколы занесе...», glossed "Igor's warriors"). The fixed note now says
   exactly this — falcon image continues from part 1's Igor's-warriors passage, and part 1's Kurians
   are wolves, not falcons. Confirmed true on both counts.

6. **Unit 30 (Святславлича vs Святъславлича).** Pulled the raw paragraph text from
   `source-1800.txt` directly and located all three refrain occurrences by eye:
   - unit 15's position: "...буего **Святславлича**!" (no о, no ъ)
   - unit 19's position: "...буего **Святславлича**." (no о, no ъ)
   - unit 30's position: "...буего **Святъславлича**." (ъ present, о still absent)
   This confirms, independently of the draft's own `t`/`tr` fields, that the fixed note is now
   correct: units 15/19 print «Святславлича» and unit 30 prints «Святъславлича» — matching unit
   15's own note and matching `tr`'s Svjatslavliča/Svjatŭslavliča distinction. Defect resolved, and
   consistent across `t`, `tr`, and `n` in all three units.

## Fresh full pass — no new or missed blocking defects found

- Re-checked every historical identification (Yaroslav Vsevolodovich of Chernigov d. 1198 vs.
  Yaroslav Osmomysl of Galich r. 1153–1187; Vsevolod "Big Nest"; Vladimir Glebovich d. 1187; Rurik
  and David Rostislavich; Roman Mstislavich; Konchak; the Olgovichi; Ingvar/Vsevolod/three
  Mstislavichi of Volhynia) against known chronicle facts — all check out, and every disputed
  identification (Уримъ, шереширъ, папорзи, Деремела, Хинова, "three Mstislavichi") stays properly
  hedged in both `n` and, where relevant, `l`/`i`.
- Re-checked all internal cross-references by unit number after the renumbering implied by the
  fixes (units 1↔16, 9↔28, 20↔28, 21↔part 1) — all point to the correct unit and accurately describe
  its content.
- Re-verified the dual/plural verb-form claims throughout (Вступита = 2nd dual imperative for 2
  addressees; расхытисте = plural aorist for a group of 5, correctly not called dual; ваю
  consistently a true dual pronoun) — all correct.
- No case of a flagged dark place being silently resolved with invented certainty remains anywhere
  in `l` or `i` (the two cases pass 1 found, units 7 and 17, are now fixed; no third instance
  surfaced on this pass).
- No `t`-field drift, no segmentation change, no new `p: true`, glossary out of scope for this
  sentence-only draft file (as in pass 1).

No blocking defects found on this pass, new or residual.

## Verdict: **READY**

All six pass-1 defects are genuinely fixed, verified independently against the source text and
against `slovo-part1.json`/`slovo-part5.json` rather than taking the fix summary on faith, and the
mechanical concatenation check still passes exactly. The one item noted above (unit 13's "cf."
comparanda mixing persons) is a stylistic looseness, not a factual error, and does not block gating.
The draft is ready to gate.
