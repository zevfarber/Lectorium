# Part 8 review — pass 1

## Method
- Concatenated all 11 units' `t` fields with single spaces and diffed against the supplied
  ground-truth block character-by-character (Python, exact string equality) and independently
  recomputed its sha256: `482c76b5a842962611fe5a2b682a32d9b4750ea40f1fe69e249801ee9b7b7c7d` —
  **exact match, zero differences.** `t` fidelity is clean throughout; no ѣ/е, ъ/ь or punctuation
  drift anywhere.
- Confirmed `p:true` appears on unit 1 only, nowhere else.
- Checked every grammar claim (aorist/imperfect, periphrastic perfect, dual, vocative, case
  labels) against the actual endings, cross-checked every historical/textual claim against
  external sources where feasible, and cross-checked cross-references against the actual text of
  the cited parts (`slovo-part1.json`, `slovo-part7.json`, and the part 6 draft/glossary in this
  same `claims/` folder) rather than taking the note's word for it.
- Echo-checked the lament's most famous images (cuckoo-flight opening, wind address, Dnepr
  address, sun address, closing thirst/quiver image) against what is independently known/found of
  well-circulated English renderings (search access was heavily proxy-blocked for full texts, so
  this check relied on corroborating snippets plus the passage's well-documented reputation as the
  most anthologized lines in the poem — flagged generously per instructions).

## Blocking defects

1. **Unit 3 — `l`/`i` silently contradict the unit's own note on «вѣтрило».**
   `n` states flatly: *"«вѣтрило» intensifies «вѣтрѣ» (an emphatic doubling, 'Wind! Wind!') rather
   than naming something distinct from the wind itself."* But `l` renders it "wind-driver" and `i`
   renders it "O Wind-driver!" — both treat вѣтрило as a distinct agent-noun (something that
   *drives* wind, i.e. closer to the word's other attested sense "sail"), which is exactly the
   "something distinct from the wind" reading the note just said this passage does *not* support.
   The fields and the note assert two different, incompatible analyses of the same word.
   **Fix:** either drop "wind-driver" for a rendering that is transparently just intensified
   "Wind" (e.g. "O Wind! O Wind!"), or, if "wind-driver"/sail-adjacent sense is intended after all,
   rewrite the note to say so instead of denying it.

2. **Unit 3 — `i` echoes a famous modern rendering of the wind address.**
   `i`: *"'O Wind! O Wind-driver! Why, my Lord, do you blow with such force?'"* This reproduces the
   distinctive doubled-vocative-plus-question shape of the best-known English renderings of this
   line (a repeated "Wind, Wind!" address immediately followed by "why, lord, do you blow" — this
   exact call-and-question pattern is closely associated with Nabokov's widely anthologized
   version). Given this is explicitly the most famous couplet of the most famous passage in the
   poem, the resemblance is too close to be coincidental register convergence.
   **Fix:** rework the vocative structure from the Old East Slavic alone (e.g. avoid the paired
   "O Wind! O ___!" exclamation shape), the way parts 2, 6 and 7 were reworked for comparable
   echoes (see LOG.md).

3. **Unit 7 — unverified, likely false claim that «Словутичь» is attested in the Primary
   Chronicle.** `n` says the epithet is *"an epithet for the river also found elsewhere in Old
   Rus' writing (e.g. the Primary Chronicle)."* No corroborating attestation of «Словутичь»/
   «Слутич» in the Повесть временных лет turned up on checking; the epithet's afterlife is
   documented mainly in later East Slavic/Ukrainian folk-song tradition ("Славута"/"Словутиця"),
   not demonstrably in the Primary Chronicle itself. This reads as a specific, checkable citation
   invented to lend false certainty to an otherwise fine observation (that «Словутичь» outlived
   this poem as a name for the Dnepr).
   **Fix:** drop the Primary Chronicle citation, or replace it with the defensible claim — the
   epithet's survival in later folk tradition — without naming a specific chronicle unless a real
   citation can be produced.

4. **Unit 7 — `i` echoes a famous modern rendering of the Dnepr address.**
   `i`: *"'You have cut clean through rocky mountains, straight across the land of the
   Polovtsians.'"* This is very close in both image-selection and word choice ("rocky
   mountains"/"stone mountains" + "land of the Polovtsi(ans)") to long-circulated English
   renderings of this exact line ("...thou hast pierced thy way through the rocky hills to the
   land of Polovtsi" / "Thou didst divide the stone mountains in the country of the Polovtsi").
   This is precisely the phrase-pattern the task brief calls out by name as a known risk for this
   unit.
   **Fix:** rework independently from the Old East Slavic (e.g. avoid the "cut clean through
   rocky mountains ... land of the Polovtsians" collocation as a fixed unit).

5. **Unit 10 — false/overclaimed grammar-case identity between «лады» and «ладѣ».**
   `n` calls «ладѣ» here *"one more small, real orthographic inconsistency of the 1800 print for
   the same word and case"* as unit 4's «лады» (which that unit's own note calls genitive
   singular). But under regular Old East Slavic a-stem declension, **-ы marks genitive singular**
   while **-ѣ marks dative/locative singular** — these are two different cases, not an orthographic
   variant of one case, the same distinction the draft itself correctly draws elsewhere (e.g. unit
   7's note on «Путивлю городу» vs. «въ Путивлѣ», explicitly labelled dative vs. prepositional/
   locative). Since «лада»'s own declension is already flagged as contested in unit 4, asserting
   "same word and case" here adds an unflagged, non-obvious grammatical claim on top of an
   already-open crux.
   **Fix:** either hedge explicitly ("«ладѣ» looks like a different case-ending from unit 4's
   «лады» under the regular a-stem paradigm, though both are taken to carry the same sense..."),
   or justify the case-identity claim (e.g. if «лада» is being treated as a soft/jā-stem noun,
   whose paradigm would put genitive singular at -ѣ, say so explicitly), rather than presenting it
   as settled orthographic noise.

6. **Unit 1 — `l`/`i` render aorist «рече» as present tense, contradicting the note and the
   project's own precedent.** `n` glosses «рече» explicitly: *"(aorist, 'she said')"* — but both
   `l` ("I will fly, she says...") and `i` ("'I will fly,' she says...") use the present tense.
   Besides contradicting the note in the same unit, this breaks with `slovo-part1.json`'s own
   established handling of the identical word: part 1 units 3 and 6 both render «рече» as "said"
   (past), matching its aorist gloss there. Conventions also specify that `l` "keeps the aspect
   and mood visible," which a silent tense-shift undoes.
   **Fix:** render «рече» as "she said" in `l` (and, if a present-tense parenthetical is wanted
   for `i`'s immediacy, say so explicitly in the note rather than leaving the aorist gloss to imply
   otherwise).

## Non-blocking observations
- Units 1, 3, 7, 8, 9 all render «рано» (lit. "early") as "at early dawn" in `i`. This is a
  defensible idiomatic gloss and applied consistently rather than cherry-picked, but it does add a
  specific time-of-day claim ("dawn") the word itself does not assert on its own. Worth a second
  look against the "never adding content not in l/the source" guideline, though not blocking.
- Unit 8's note dates the Svyatoslav/Kobyak campaign to "1183 ... recorded in the Hypatian
  Chronicle" — this matches the annal year the Hypatian Chronicle itself places the campaign
  under; note that several modern chronologies (reconciling the chronicle's dating conventions)
  place the actual events in 1184. Not wrong as stated (it is explicitly tied to the chronicle's
  own year), but worth a parenthetical for readers checking against a modern timeline.

## Checked and found clean (no defects)
- Verbatim `t` text against the supplied ground truth: exact character-for-character match,
  sha256-verified.
- `p:true` correctly appears on unit 1 only.
- Dark places kept genuinely open, appropriately hedged in both `n` and `l`/`i`: незнаемь's
  attachment (unit 1), «на своею не трудною крилцю» (unit 4), «лады»/«лады вои» (unit 4, with the
  case caveat above), «лучи» vs «луки» and «тули затче» (unit 11) — none silently resolved with
  invented certainty.
- Cross-references verified against the actual cited parts: Yaroslavna as daughter of Yaroslav
  Osmomysl of Galich, met in part 6 (`Галичкы Осмомыслѣ Ярославе...`); «Хиновьскыя»/«Хинова» tied
  correctly to part 6 unit 22's «Хинова»; the Kurian "cradled under helmets" image in part 1
  correctly tied to «лелѣючи»/«лелѣялъ»/«възлелѣй»; Vseslav's wolf-transformation in part 7
  correctly used as the "sinister" counterpoint to Yaroslavna's benign cuckoo-wish; Svyatoslav of
  the Golden Word correctly identified as spanning parts 5–6.
- Historical claims check out: Svyatoslav Vsevolodovich's real 1183/84 campaign that defeated and
  captured Kobyak (unit 8); chronicle-attested thirst afflicting Igor's army before its final
  defeat (unit 11).
- Periphrastic-perfect, aorist, vocative and imperfect claims elsewhere (units 2, 5, 6, 7, 8, 9,
  11) all check out against the actual word forms.
- `i` register throughout is real, lightly elevated English, never childish, and (aside from the
  two echo cases above) doesn't add unsupported content.

6 blocking defects found: two internal self-contradictions between `l`/`i` and `n` (units 1's
«рече» tense and 3's «вѣтрило» sense), two echoes of well-known modern English renderings (units 3
and 7), one unverified/likely-false external citation (unit 7's Primary Chronicle claim), and one
overclaimed grammatical-case identity compounding an already-open crux (unit 10).
