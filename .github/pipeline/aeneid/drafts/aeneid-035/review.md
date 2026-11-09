# aeneid-035 review (V.387–484) — adversarial reviewer, two passes

Method: pass 1 read every unit's `t`, `l`, `i`, `n` against the Latin and the grammar (every label checked against the form in that line); hand-scanned every line the packet flags (5.389, 5.410, 5.422, 5.432) and every line with Greek eu, initial Ae-, consonantal i after a prefix, or hiatus, then all other lines against the scanner's output (syllable by syllable, position across word boundaries). Pass 2 re-read every edited unit, re-checked line counts (`l` has the same line count as `t` in all 59 units), speech marks (6 “ and 6 ” in each of `t`, `l`, `i`; speeches 389–393, 394–400, 410–420, 465–467, 474–476, 483–484), `ln` and `p` flags (the seven paragraph starts 387, 406, 410, 424, 437, 461, 474 all carry `p`), and simulated the build's scansion step (scanner + `scan-fixes.json` + the validator's foot checks: all 98 lines have a hexameter `sc`, none without).

`t`, `ln` and `p` are untouched (asserted in the script). Edits to `l`/`i`/`n` were made by `review_patch.py` (exact-substring replacements with asserts) run after `make_units.py`; `make_units.py` was not edited, so if it is re-run, run `review_patch.py` after it (the script is idempotent for scan-fixes, not for units: re-run only on a freshly generated `units.json`). `gloss.json` was not touched.

## Severity counts

Definition (as for 034): major = a false grammatical label, or Latin mistranslated in `l`, or a scanner fit that is wrong; medium = misleading or unsupported claim, `l`/`i` disagreement, remembered echo, rule 5b note, or a line the build cannot take without a hand entry; low = polish.

- Major: 9 (4 text, 5 scansion)
- Medium: 11 (9 text, 2 scansion)
- Low: 13 (all text)

## Changes: text

Major
1. U1 (389–391) note: `heroum` was called "an old genitive plural in -um (you'll see this constantly)". It is the ordinary genitive plural of `heros`, not the archaic -um for -orum of `superum`/`divom`. Fixed, with the contrast stated.
2. U33 (439–442) note: `circum` was said to be "set after its noun". In `sedet circum castella` it stands before `castella`; the adjective `montana` is what stands apart (before the verb). Fixed.
3. U54 (477–480) note: `media inter cornua` was said to have `inter` "set after its noun". `inter` sits between its adjective and its noun. Fixed.
4. U54 `l`: "opposite stood the face of the bullock" made `ora` the subject of `stetit`; `ora` is the accusative governed by `contra`. Now "opposite he stood the face of the bullock facing him"; the second and third lines also re-cut so that `reducta` goes with `dextra` ("with right hand drawn back"), not with the gloves.

Medium
5. U0 note: `herbae` was called "a genitive of definition … an ablative of place" in one breath. Now: `toro` ablative of place, `viridante` agreeing, `herbae` a genitive of material.
6. U2 note: Eryx "killed by Hercules in a bout at the foot of the mountain" and "a hero honoured after death" are not in the Latin; now only what 410–414 supports (he fought Hercules), and the "god" hedged ("presumably as a son of Venus honoured on his mountain; the text does not say").
7. U8 (399–400) note: the mixed condition was glossed "if I were as I was, I would then not have come", which says nothing. Now "if I now had that youth (as I once had it), I would not have come forward".
8. U8, U47, U55 notes (rule 5b): the drafter's "Misprint: Greenough prints …" tails are now the opening sentence of each note, in the rule's form ("The print has X, a misprint for Y"). They cover `moror. ”Sic` (400), `deo. ”Dixitque` (467) and the small-letter `sternitur` after a full stop (481). `t` must keep the print (the build checks that the units join to the pinned source), so the notes say "t keeps the print, because t must match the pinned source", and `l`/`i` close the speeches after `moror.` and `deo.` as before. Companion sentences added at the head of the U9 and U48 notes (the stray ” at the start of their `t`). Needs a decision by the owner/orchestrator: to make the reader show the corrected text, the source's closing marks at 5.400 and 5.467 and the capital at 5.481 would have to be moved by the missing-punctuation route (re-pin of the part's `sha256`) or logged in QUESTIONS.md; I did not touch the source or QUESTIONS.md.
9. U57 `i` and U58 `i`: remembered echoes of familiar English versions ("in place of Dares's death I pay you this better life"; "I lay down my gloves and my art"). Rephrased: "for the death of Dares I pay you this life, a worthier one, in full"; "and here, as victor, I put by my gloves and my craft."
10. U52 note: `Hic victor` stated flatly to be the adverb; hedged ("most simply an adverb … could also be the pronoun, 'this man, the victor'"). (The `l`/`i` are unchanged: they read the adverb.)

Low
11. U7 note: "`iuventas` is Virgil's form of `iuventa`" (it is the ordinary noun); now "a by-form of `iuventa` (the word used at 430)".
12. U11 `l`: `boum` moved back to follow `terga` as in the Latin ("of so great the huge seven / hides of oxen …"), showing the `septem / terga boum` hyperbaton across the line break.
13. U12 note: `omnes`/`omnis` Latin Library remark removed (morphology, conventions: ignore).
14. U26 note: `brachia`/`bracchia` remark removed (orthography).
15. U36 `i`: "spent his strength upon the wind" (an echo-risk wording) -> "flung his strength away on empty air".
16. U45 note: "`te` being understood" removed (`animum` is the object; nothing is understood).
17. U46 note: `vires`/`uiris` remark removed (orthography).
18. U47 `i`: "Yield to a god." -> "Give way before a god." (`l` keeps "Yield to a god.").
19. U49 note: `naves`/`nauis` remark removed.
20. U50 note: "the comrades being summoned to receive the loser's consolation gifts" stated as fact; now "(the text does not say by whom) … what are evidently the loser's consolation gifts".
21. U53 note: the muddled "(the print has no mark there; the sense runs on)" about `inquit` is now "the print gives it no commas, and the speech runs straight on".
22. U54 `i`: "rising to his full height" repeated U34's phrase; now "standing tall".
23. U54 note: `adstabat`/`astabat` remark removed.

## Changes: scansion (`scan-fixes.json`, 7 entries added, each checked with the validator's own foot test and word-match test)

Scanner wrong (major):
- 5.410: `ipsius` taken as one syllable, which forced `et` long before `Her-` (h makes no position, so `et` is short; the scan was impossible, cost 2.6). Fixed to ip-sī-us | et, a dactyl (`sī` long, the -īus genitive).
- 5.417: `Troius` read Tro-ius with a long `ius` before a vowel. Fixed to Trō-ĭ-ŭs (three syllables, as in the published aeneid-007).
- 5.418: `Aeneae` split Ae- in two (A-e-ne-ae). Fixed to Ae-nē-ae (as 5.282, 5.286).
- 5.450: `Teucri` split Te-u-cri (cost 0.0, not flagged). Fixed to one long syllable Teu- (as 5.293); `Trinacria` keeps na- long before cr- (as in aeneid-022).
- 5.461: `Aeneas` split Ae- in two (A-e-ne-as). Fixed to Ae-nē-ās.

Unresolved (medium):
- 5.422: a hypermetric line (the final -que of `lacertosque` elides into `exuit`, 423). Hand fit with 13 metrical syllables and the last -que unmarked; the end mark × on `tos`. The validator accepts the form (13 syllables, one × , feet `––`×4, `–⏑⏑`, `–×`).
- 5.432: `genua` has consonantal u (gen-wa), the first syllable long; the scanner could find no fit.

Hand-scanned and found correct, no entry (refused): 5.389 (`Entelle heroum`: the -le elides, he-ro-um with long -um by position before `quondam`; the scanner's fit is the standard scansion, the cost is for the elision and the hiatus). Also checked and agreeing with the scanner: 5.402 `proiecit` (pro-iē-cit, consonantal i), 5.414 `Alciden` and `suetus` (sue- one syllable), 5.421 `reiecit`, 5.470 `eiectantem`, 5.420 `Troianos`, 5.444 `venientem` (four syllables), 5.458 `requies` (read as two syllables with a long first; the other reading, rĕ-quĭ-ēs, also makes a hexameter, so the audio vowel length of `re-` is uncertain), 5.468 `genua` (three syllables there, the last elided into `aegra`), 5.481 `humi`, 5.442 `urguet` (two syllables), and every line with Ae- (415, 419, 424, 452, 456, 468, 480) or Greek eu (474 `Teucri`), and every hiatus and elision across a verse (e.g. 393 `Trinacriam, et spolia illa`, 438, 443, 445, 462, 470, 476, 483).

## Doubtful quantities left as scanned (for QUESTIONS.md)

5.393 `Trinăcriam` (na- short) against 5.450 `Trinācria` (na- long before cr-): the same word scanned both ways, as in earlier parts; 5.389 `hērōum`; 5.395 `ĕnīm` with a long final in `sed enim`; 5.411 `hōc` long before a vowel; 5.458 `requies` (see above); 5.467 `dĭremit` (short first syllable; the metre allows no other); 5.469 `ūtroque` (u long by muta cum liquida); 5.413 and 5.480 `cerēbro` (re- lengthened before br-). Audio quantities may be off there; none checkable against public-domain sources.

## Refused findings

- Unit 7 ends at a comma (397–398 `… illa iuventas,`): it is Greenough's punctuation and `t` may not change; the build accepts a comma end. Kept.
- `t` carries the stray ” at the head of units 9 and 48 and the lowercase `sternitur`: not touchable by the reviewer (see change 8).
- The `inquit` parenthesis at 474 prints without commas: a missing-punctuation case under rule 5 (source fix, re-pin); not touched.
- Drafter's `l` for U1 (`tantane … dona sines?`), U6, U13, U20, U31: word-order choices that keep the Latin order and are true; no change.
- Two Latin Library variants noted in the packet whose note-remarks were removed (see 13, 14, 17, 19, 23) are orthography/morphology only; no sense-changing variant is present in this part.
- No other remembered echoes found in `i` beyond those rephrased; none of the pilot's set-piece lines occurs in 387–484 (`Cede deo`, `Nate dea` and the speeches at 389–393, 394–400, 410–420, 465–466, 474–476 and 483–484 were checked).
