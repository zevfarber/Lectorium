# Part 6 review — pass 1

## Method
- Re-extracted part 6 from `source-1800.txt` using the `opens`/`ends` strings in `parts.json`,
  whitespace-normalised (NFC). Result: 397 words, 2461 chars, sha256
  `d589e127dff2b0d909b381b10e6f8036a786dc1beadfa70572ac2066526d08c8` — matches `parts.json` exactly.
- Concatenated all 30 units' `t` fields with single spaces, NFC-normalised, and diffed
  character-by-character against that extraction: **byte-identical, zero differences.**
- Confirmed no unit carries `p:true`, and confirmed against the source that part 6 opens
  mid-paragraph (the text immediately preceding `А уже не вижду...` is Svyatoslav's «Се ли
  створисте моей сребреней сѣдинѣ!» with only a single space between them, no paragraph break) —
  so the absence of `p:true` anywhere in the draft is correct, not an omission.
- Checked unit boundaries against the source's own punctuation: 30 units end in `.`/`!`/`?`
  at real sentence breaks; the two internal `!` marks (units 9, 20) are vocative addresses
  followed by lower-case continuations in the print, correctly kept inside one unit rather than
  split. No mis-segmentation found.
- Checked every aorist/dual/vocative claim against the actual endings, checked every historical
  identification, and cross-checked cross-references against the actual text of the cited parts
  (part 1, part 5) rather than taking the note's word for it.

## Blocking defects

1. **Unit 13 — false grammatical claim: `плаваша` is not a dual form.**
   Note says: *"плаваша is a dual aorist ('the two [helmets] swam'), grammatically marking the
   pair."* This is wrong. Throughout this project's own files, 3rd-dual aorist consistently ends
   in **-ста** (слѣтѣста, помѣркоста, погасоста, поволокоста, погрузиста — all in slovo-part5.json,
   all glossed "aorist, dual"), while 3rd-plural aorist ends in **-ша** (ркоша, прострошася, both
   glossed "aorist 3pl" in the same file). `плаваша` ends in -ша, i.e. it is a **plural** aorist
   form, agreeing with the grammatically plural noun `шеломы` (a true dual nominative would be
   `шелома`, not `шеломы`). `ваю` is correctly identified as a true dual pronoun, but the verb
   itself is not dual — the note conflates the two. This is the same "plural ending used of a
   two-person referent" phenomenon the project already documents correctly elsewhere (part 5's
   `одолѣсте`/`проліясте`, this draft's own unit 28 `расхытисте`), and it should be described the
   same way here instead of mislabeled "dual."
   **Fix:** rewrite to something like: *"ваю is a true dual ('of you two'); плаваша carries the
   plural aorist ending (cf. рекосте, расхытисте elsewhere in this part) — грамматически it agrees
   with the plural шеломы, not a dual form, though it still refers to the pair's own helmets."*

2. **Unit 21 — factually wrong cross-reference to part 1.**
   Note says: *"Continues the falcon-image already used of Boyan (proem) and of **Vsevolod's
   Kurians (part 1)**."* Checked against `slovo-part1.json`: the Kurians are compared to **grey
   wolves** — «сами скачють акы сѣрыи влъци въ полѣ» ("they themselves leap like grey wolves in
   the field"), part 1 unit 14, glossed there as "the recurring wolf-simile." The falcon image in
   part 1 (unit 10, «Не буря соколы занесе...») is glossed there as "Igor's warriors" generally, not
   Vsevolod's Kurians specifically, and it isn't attached to Vsevolod at all. The claim is simply
   false on both counts.
   **Fix:** either drop the parenthetical, or correct it to something defensible, e.g. "Continues
   the falcon-image already used of Boyan (proem) and of Igor's own warriors (part 1) ... note that
   part 1's Kurians are pictured as wolves, not falcons."

3. **Unit 30 — misquotes the earlier refrain spelling, contradicting its own draft.**
   Note says the two earlier occurrences (units 15, 19) were *"both printed without it [ъ],
   «Святославлича»"* — i.e. with the vowel "о" retained. But the actual print (confirmed against
   `source-1800.txt` and against units 15/19's own `t` fields) is **«Святславлича»** — missing both
   the "о" after "т" *and* the "ъ". Unit 15's own note gets this right ("printed «Святславлича» —
   without the о after т and without ъ"); unit 30's note contradicts it by silently reinserting the
   "о". Since this whole note exists specifically to make a checkable claim about exact 1800
   spelling, the error defeats its purpose.
   **Fix:** change unit 30's note to quote «Святславлича» (matching unit 15's note and the actual
   `t` fields of units 15/19), not «Святославлича».

4. **Unit 17 — the literal (`l`) field silently resolves a flagged crux, contradicting its own note.**
   `l` reads: *"...hurling **[weights]** through the clouds..."* — but `t` prints «времены»
   ('times'), and the note explicitly says: *"времены ('times') sits oddly... it is often read as a
   print corruption of бремены ('loads, weights')... we keep the 1800 print's wording in t and flag
   the difficulty rather than silently emend it."* The `l` field does exactly what the note says it
   won't do: it silently substitutes the disputed emendation ("weights") for the actual printed word
   ("times") with no bracket-flag of the substitution itself. This is inconsistent with the
   project's own precedent (part 5 keeps `l` genuinely literal on comparable cruxes, e.g. rendering
   `сошлю` as "I will not send" rather than the proposed emendation "were borne off", with the
   emendation confined to the note).
   **Fix:** make `l` literal to the print, e.g. "...hurling times through the clouds..." (odd-sounding
   on purpose, as the note explains), and keep the бремены/"weights" reading only in `n`.

5. **Unit 7 — the idiomatic (`i`) field asserts a disputed identification as fact, contradicting its own note.**
   `i` reads: *"See how **the men of Rimov** cry out under Polovtsian sabers..."* — stated flatly,
   with no hedge. But the note for the same unit says: *"«Уримъ» is a genuine dark place... The
   identification is plausible but far from certain, and **we flag it rather than assert it**."*
   The `i` field does assert it, as settled fact, directly contradicting the note two sentences
   later. `l` correctly keeps the untranslated "Urim."
   **Fix:** soften `i` to keep the uncertainty visible, e.g. "See how the men of Urim — probably
   Rimov — cry out under Polovtsian sabers..." or simply keep "Urim" untranslated in `i` as `l` does.

6. **Unit 3 — the note's "standard reading" doesn't match the very print it just quoted.**
   Note quotes the print as «му жа имѣся» (with **ѣ**, confirmed against `source-1800.txt`), then
   two clauses later gives "the standard reading" of the same word as «мужаимъся» (with **ъ**,
   not ѣ) with no acknowledgement that a letter has changed. Concatenating the print's own three
   pieces gives "мужаимѣся" (ѣ preserved), not "мужаимъся". Whatever the correct scholarly
   reconstruction is, the note as written is self-contradictory — it changes a letter from its own
   quoted evidence without saying so, which reads as either a transcription slip or an invented
   reconstruction dressed up as "the standard reading."
   **Fix:** either quote the reconstruction as «мужаимѣся» (matching the print's own letters), or,
   if the ъ-form is genuinely the attested scholarly emendation, say explicitly that the standard
   reading also changes ѣ→ъ and why, rather than silently presenting a different string as if it
   were the same one.

## Checked and found clean (no defects)
- Verbatim `t` text against source: exact match, no character-level drift anywhere.
- No `p:true` anywhere, correctly, since part 6 opens mid-paragraph.
- Segmentation/unit boundaries against source punctuation: correct throughout.
- Dark places kept genuinely open: шереширы, папорзи, Деремела, Хинова — all properly hedged in
  both `n` and (unlike units 7 and 17 above) in `l`/`i` too.
- Historical identifications: Yaroslav Vsevolodovich of Chernigov vs. Yaroslav Osmomysl of Galich
  correctly kept distinct; Vsevolod "Big Nest" of Suzdal, Rurik/David Rostislavich, Vladimir
  Glebovich, Roman Mstislavich, Konchak, the Olgovichi, and the Ingvar/Vsevolod/three-Mstislavichi
  Volhynian identification (explicitly and appropriately hedged, and consistent with the
  mainstream scholarly reading) all check out against known chronicle facts.
- Refrain dual/plural verb forms elsewhere (Вступита = 2nd dual imperative for exactly 2 addressees;
  Загородите = 2nd plural imperative for 5 addressees; расхытисте = plural aorist ending for 5,
  correctly *not* called dual) are all correctly analyzed.
- No echoes of famous modern renderings found rising above what the project's own established
  glossary choices already force (e.g. "iron regiments" for плъкы matches part 1's own established
  glossary entry, not a borrowing from a modern translator).
- `i` present and distinct from `l` on every unit; none are childish or add unsupported content
  (aside from the two false-certainty cases flagged above, which are precision problems, not
  content-invention problems).

Six blocking defects found: two false/self-contradictory grammar or textual claims (units 3, 13),
one wrong cross-reference to another part (unit 21), one misquoted spelling contradicting the
draft's own unit 15 (unit 30), and two cases of a flagged "dark place" being silently resolved with
invented certainty in `l` or `i` while the note itself says it won't be (units 7, 17).
