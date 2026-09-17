# Part 8 review — pass 2 (verification of pass-1 fixes + fresh pass)

## Method
- Recomputed sha256 of all 11 `t` fields joined with single spaces in Python:
  `482c76b5a842962611fe5a2b682a32d9b4750ea40f1fe69e249801ee9b7b7c7d`, word count 156, char count
  978 — **exact match** to the target on all three counts. No `t` field was touched by the fixes.
- Confirmed `p: true` appears on unit 1 only (programmatic check over all 11 units).
- Read `conventions.md`, `slovo-proem.json`, `slovo-part1.json` (models) and `slovo-part7.json`
  (for the Vseslav/wolf and «Хинова» cross-references cited in part 8's notes) and checked every
  cross-reference in part 8 against their actual text rather than taking the note's word for it.
- Used web search to independently check the «вѣтрило» = 'sail' claim and to hunt for
  word-for-word overlap between the two reworked units (3, 7) and known English renderings.
  Direct page fetches were blocked by the egress proxy for essentially every literary/reference
  domain tried (archive.org, lib.ru, en.wikisource.org, nevmenandr.net, grokipedia.com,
  moscsp.ru, skumanich.net, birchbarkpress.yolasite.com, alluringworld.com, recap.study — all
  refused); only search-snippet summaries were available, the same constraint pass 1 reported.
  Findings below are qualified accordingly.

## The 6 fixes

1. **Unit 1, «рече» → "she said" — VERIFIED.** `l` now reads "...I will fly, she said, as a
   cuckoo..." and `i` "'I will fly,' she said, 'like a cuckoo...'"; `n` still glosses «рече» as
   "(aorist, 'she said')". Tense is now consistent across `l`/`i`/`n`, matches part 1's own
   handling of the same verb (units 3, 6: "said"), and reads naturally — no stitching artifacts.

2. **Unit 3, «вѣтрило» "wind-driver" → "sail" + note rewrite — VERIFIED.** `l`: "O wind! O sail!
   why, Lord, do you blow so violently?"; `i`: "'Wind! Sail! Why do you blow so fiercely, my
   lord?'" `n` now reads: "«вѣтрило» is a second, distinct word from «вѣтрѣ»: the old term for
   'sail' ... so the line may be addressing the wind under two guises ... rather than simply
   repeating 'wind' for emphasis; both readings are found in the literature and neither is
   certain." This is now internally consistent (the fields and the note agree that вѣтрило is
   being read as its own word, "sail," and the note openly hedges rather than asserting either
   reading as settled). Reads naturally, no seams.
   - **вѣтрило = 'sail' accuracy (checklist item 6):** independently confirmed. «вѣтрило» is a
     well-attested Old East Slavic/OCS word for 'sail' (the sense survives into modern Ukrainian
     вітрило and is the standard gloss given for this very line in Russian sources); «парусъ» is
     indeed the later, borrowed term that eventually displaced it. The fix did not trade one
     unverified claim for another — this one holds up.
   - **New echo check:** could not find a verbatim match for "O wind! O sail!" or "Wind! Sail!" in
     any specific, confirmed published translation. One search-engine paraphrase surfaced the
     string "O Wind, O Sailor Wind! Why, lord, do you blow so strongly?" as if it were a specific
     rendering, but a literal-string search for that exact wording returned zero hits, so it looks
     like a summarizer paraphrase rather than a real quotable line, and I could not confirm a
     source or translator for it. Treating it cautiously: even if some such rendering exists, the
     doubled address + "why, lord, do you blow" shape is largely dictated by the source syntax
     itself (о вѣтрѣ! вѣтрило! чему, господине, насильно вѣеши?), so *some* structural
     resemblance across independent translations is close to unavoidable. The specific word choices
     that made the original flagged text risky — "wind-driver" as an agent-noun, and "with such
     force" — are both gone. I'm not raising this to a blocking defect, but flagging it as a
     residual, non-blocking watch item (see below).

3. **Unit 7, «Словутичь» Primary Chronicle citation dropped — VERIFIED.** `n` now says the name
   "outlived this poem, surviving into later East Slavic/Ukrainian folk-song tradition as
   «Славута»/«Словутиця» for the Dnepr" — no chronicle citation remains anywhere in the unit. This
   folk-tradition claim is itself real and checkable (Славута/Славутич as a folk-poetic name for
   the Dnieper, source of the modern place-name Slavutych, is well documented), so the fix
   replaced an invented-sounding citation with a defensible one rather than just deleting content.

4. **Unit 7, Dnepr address reworked — VERIFIED, and re-checked fresh for new echoes.** `l`: "you
   have broken a way through stone mountains, into the Cuman land"; `i`: "You forced a path
   through mountains of stone, out into the Cuman land." Compared against every variant of this
   line's English rendering findable via search snippets — "...thou hast pierced thy way through
   the rocky hills to the land of Polovtsi" (the specific 19th-c. rendering pass 1 named),
   "O Dnepr, famed one! / You have pierced stone hills / through the Kuman land" (another
   snippet, translator unconfirmed), and "Thou didst divide the stone mountains in the country of
   the Polovtsi" (pass 1's second citation). None share the current draft's verbs ("broken a way
   through" / "forced a path through" vs. "pierced" / "divide") or its "stone mountains" / "Cuman
   land" word choices closely enough to read as an echo. This unit is clean.

5. **Unit 10, «ладѣ»/«лады» case-identity claim hedged — VERIFIED.** `n` now reads: "...though its
   ending (-ѣ, looking dative/locative) differs from unit 4's -ы (there read as genitive); whether
   this is a further spelling inconsistency of the 1800 print for the same case, or a genuine case
   shift, is not settled — unit 4's own case reading is itself contested...". This correctly
   surfaces the -ѣ/-ы distinction pass 1 flagged instead of asserting identity, and doesn't
   overreach in the other direction either (it doesn't newly assert a case *difference* as fact —
   it says the question is open). Consistent with unit 4's own hedged note.

6. **Unit 8, Hypatian Chronicle 1183 vs. reconciled 1184 — VERIFIED.** `n` now reads: "...dated
   1183 in the Hypatian Chronicle's own annal year (some modern reconciled chronologies place it
   in 1184)...". Matches pass 1's suggested parenthetical exactly in substance.

## Fresh pass — units 2, 4, 5, 6, 9, 11 (untouched by the fixes)

Checked every grammar claim against the actual forms, every historical/etymological claim for
plausibility, every cross-reference against the cited parts, and every `i` for register and for
echo risk against the passage's other famous images (the sun address, the closing thirst/quiver
image — both explicitly part of the "most anthologized lines" pass 1 flagged as worth checking).

- **Unit 2** («омочю»/«утру», Каяла, «жестоцѣмъ»): grammar claims (perfective non-past = future
  sense) correct; Kayala's unresolved identity properly hedged; «жестоцѣмъ» reading ("battered,"
  not "cruel") reasonably argued, not overclaimed. Clean.
- **Unit 4** (Хиновьскыя, «на своею не трудною крилцю», «лады»): «Хиновьскыя»/«Хинова»
  cross-reference to part 6 confirmed consistent; the crux phrase and «лады» case/etymology both
  properly hedged with named alternative readings, not resolved with invented certainty; the -ы
  genitive-singular reading is consistent with the a-stem paradigm invoked to correct unit 10.
  Clean.
- **Unit 5** (Wind's range, «лелѣючи»): imperfect «бяшетъ» claim matches the same word's gloss in
  the proem's own glossary; the «лелѣючи»/«лелѣялъ»/«възлелѣй» chain cross-referenced to unit 8
  and to part 1's «възлелѣяны» — confirmed against part 1's actual text ("подъ шеломы
  възлелѣяны"). Clean.
- **Unit 6** («ковылію», «развѣя»): ковыль = feather-grass/Stipa is correctly identified; «развѣя»
  as aorist is plausible and consistent with the poem's other vowel-stem aorists. Clean.
- **Unit 9** (Sun address, «къ Путивлѣ», «тепло и красно еси»): short-form neuter predicate
  adjective claim is grammatically sound (слъньце is neuter); the «къ Путивлѣ» vs. unit 3/7's
  «въ»/dative variants is presented as a plausible print slip, appropriately hedged, not asserted.
  Checked "bright, thrice-bright sun ... warm and fair" against search snippets for other
  renderings ("thrice-light sun," warm-to-all paraphrases); no verbatim overlap found. Clean.
- **Unit 11** (closing thirst/quiver image): «лучи»/«луки» and «тули затче» cruxes both still
  presented as genuinely open, matching pass 1's own "checked clean" list; aorist claims for
  «съпряже»/«затче» are plausible. Checked "fused their rays with thirst ... sealed their quivers
  shut" against search snippets of other renderings (a Patton translation surfaced: "bows...warped
  with thirst," "quivers...closed up with misfortune") — different verbs and imagery, no overlap.
  Clean.

No false grammar claims, no unverified/invented history claims, no childish `i`, and no
prematurely-resolved dark place found in any of these six units.

## Newly found defects
None rise to blocking. One residual, non-blocking watch item carried over from the fix-2 review:

1. **(Non-blocking) Unit 3 — the reworked wind address's doubled-vocative shape ("O wind! O
   sail!" / "'Wind! Sail!...'") is still structurally similar to at least one wind-address
   rendering surfaced in search (unconfirmed source/translator, and the exact string returned no
   hits when searched verbatim, so it may be a summarizer paraphrase rather than a real quotable
   line). The specific word choices that made the original draft risky ("wind-driver," "with such
   force") are gone, and the doubled-address-plus-question shape is largely forced by the source
   syntax itself, so this isn't the same kind of concrete, checkable echo pass 1 found. Worth a
   final human read-through against Nabokov's actual 1960 text if/when a copy is at hand, but not
   blocking on the evidence available under the current network restrictions.

## Checked and found clean (beyond the 6 fixes)
- Verbatim `t` fidelity: exact sha256 match, 156 words, 978 characters.
- `p: true` on unit 1 only.
- Cross-references verified against `slovo-part7.json`'s actual text: Vseslav's wolf-transformation
  (units 11–14 of part 7) as the sinister counterpoint to Yaroslavna's cuckoo-wish; part 1's
  «възлелѣяны» ("cradled under helmets") tied correctly to part 8 unit 5's «лелѣючи» chain.
- All dark places in the untouched units remain genuinely open, not resolved with invented
  certainty.
- `i` register throughout is real, lightly elevated English, never childish.

CLEAN — ready to gate.
