# Review — secret-history-237-241 (§§237–241)

Adversarial review, two passes, on the strongest model. Files read: conventions.md, runbook.md, run3/RUNBOOK.md, packet.md, units.json, gloss.json, novel-forms.json, known-forms.json, secret-history-glossary.json, the pilot and the published parts 218–236 (and the grep of earlier ones) for consistency. No modern translation opened or recalled.

## Counts of findings by severity

| Pass | critical | major | moderate | minor |
|---|---|---|---|---|
| 1 (units.json) | 0 | 3 | 25 | 45 |
| 2 (gloss.json, and a second look at the edited units) | 0 | 0 | 4 | 6 |

A finding that recurs in several fields (for example one wrong Ming gloss quoted in the note and in the morph) is counted once; its other rows are marked "same" below.

## What was checked, and how

- **Morph / word alignment (the glosser's worry).** Not misaligned. In `packet.md` and in the source JSON, `žer žebseg` (index 378) and `hulaγ̇an buqa-jin` (358, 380) are each ONE source word (one Han string, one Ming gloss) whose romanization happens to contain a space; `hooks.assemble` consumes `units[k].words` strictly by count against `part_words`, so one `words` entry per packet index is exactly right, and the draft has one entry each (two lemmas in the entry for `žer žebseg`, three morphs in the entry for `hulaγ̇an buqa-jin`). Verified by script: (a) all 58 units' `t` equal the source romanization at the consumed indices and the units consume 476 of 476 words; (b) for every word, the bracketed Ming gloss at the end of every morph that carries one equals the packet's Ming gloss at that index, so no word is shifted by one anywhere, including the `hoγtočin … kirügedeġülžü` stretch (indices 386–388) and `bariγda- | žuγ̇u` (443/444, two source words, correctly two entries). No change made.
- Every grammatical label in every note and morph gloss against the form; every Ming quotation in a note or morph gloss against the packet gloss of the word it is attached to (script plus reading); original → `l` word by word; `l` ↔ `i` sense and force; quotation marks in `l` against Shiratori's and in `i` against the note; lemma spelling against the glossary heads (script); house renderings (conventions.md, published 200–236) for names, žarliγ bolba, aγ̇ulža-, -(i)jan.
- Build and validate were run from the work folder after both passes: `build` printed `BUILT secret-history-237-241: 58 units`, `validate` printed `PASS`, and neither printed any WARN. The build outputs (story file, glossary merge, stories.json) were then reverted with git so that the real build in the next step starts from a clean tree. Important for that step: `hooks.assemble` only adds glossary keys that are not yet in `secret-history-glossary.json`, so a build run before a later edit of `gloss.json` would silently keep the stale entry; build once, after the last edit.

## Pass 1 — units.json (every change)

| Unit | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| U0 word 4 | morph | minor | morph quotes Ming 追趕, which belongs to another occurrence, not this word (Ming 追襲着) | dropped 追趕 |
| U0 | i | minor | "came back" adds a direction irebe (Ming 來了) does not have | "came" |
| U3 word 27 | morph | moderate | morph splits üžeg- + -sen, against oluγsan in the same unit (olu- + -γsan) and the later house analysis üže- + -gsen (208-210) | üže- + -gsen |
| U3 | i | minor | "when the clouds clear … when the ice has gone" is a stock English shape and "has gone" is not in arilžu (aril- "clear"); possible remembered English | rebuilt from the grammar: "as the clouds clear … as the ice clears", "finding" for olu- |
| U4 | n | minor | note does not say which genitive form this is or why | named the form (after n) |
| U5 word 49 | morph | moderate | genitive label "after r" on deġel-ün; the stem ends in l (the glosser entry itself says "after l") | "after l" |
| U5 | n | minor | note quotes Ming 處 for hürtesün-eče; the word's Ming is 碎裁帛行 | Ming 行 |
| U5 word 51 | morph | minor | lemma olu- + -γ̇asu against the glossary entry for oluγ̇asu (ol- + -uγ̇asu) and the parallel γaruγ̇asu (γar- + -uγ̇asu) in U47 | ol- + -uγ̇asu, as the glossary |
| U6 | i | major | "he said, and came" makes the Idu'ut the speaker and traveller; the speech is the two envoys' report (U2, U4 note: the envoys speak, the Idu'ut is "I" inside it), and öčižü "reporting" (Ming 奏着) was dropped | "they said, reporting it, and came" |
| U6 | n | major (not counted again) | (same finding as above) (same finding) the note did not say who the subject is | added a sentence naming the envoys as subject |
| U7 | n | minor | note quotes Ming 說著 for ügüležü; the word's Ming is 話 | Ming 話 |
| U8 word 71 | morph | minor | label "let us" against l/i "I will give" and the note's own reading | "let me (us)" |
| U9 | n | minor | Ming misquoted (abuγ̇ad is 將來了) | corrected |
| U11 | i | moderate | i makes aγ̇ulžaba passive ("was received by"); the Ming 拜見 is active (to pay respects, call on), l has the neutral "had-an-audience" | "paid his respects to" |
| U11 | n | minor | note repeats the passive "to be received" | aligned with the new i |
| U11 word 104 | morph | minor | morph gloss "be received" (passive) | active sense |
| U13 | n | moderate | note supplies "the year 1207", which nothing in the packet or the permitted sources gives | removed the Gregorian year |
| U13 | n | moderate | reader-facing note carries an instruction to the glossary ("the glossary will need the decision") | rewritten as a plain remark to the reader |
| U15 | n | minor | i has "came with ten thousand Oirat"; the note did not say "with" is supplied | added the remark |
| U16 | l | moderate | l scrambles Oirad-tur(i)-jan (Oirat + to + own) into "own-for-Oirat": order reversed and "for" for dative -tur; house l puts -jan last ("heroes-own") | "Oirat-to-own" |
| U16 word 135 | morph | moderate | reflexive split as separate "-(i)" + "-jan"; conventions (227-229) keep it as one morph -(i)jan | one morph -(i)jan, and "to, with" for -tur |
| U16 | n | minor | plain line drops the dative -tur without saying so | added the remark |
| U17 word 147 | morph | moderate | morph -γ̇ad leaves the u of oroγ̇ul-u-γ̇ad unexplained, against abuγ̇ad (-uγ̇ad) in the same part |  |
| U17 | n | minor | "the glossary's earlier use" is pipeline talk in a reader note | "an earlier part" |
| U18 | i | minor | "Yedi" against house practice (names with Shiratori J keep J: Jekü, Jesünge, Jeje'er) | "Jedi" |
| U18 word 153 | morph | minor (not counted again) | (same finding as above) | same |
| U19 | i | moderate | passive "were received by" for aγ̇ulžaba (see U11) | "paid their respects to" |
| U19 word 170 | morph | minor (not counted again) | (same finding as above) | same |
| U20 | i | moderate | name Töġeles written "Töges" in i (and in morph/glossary): ġ is g, the l is lost | "Tögeles" |
| U20 word 176 | morph | moderate (not counted again) | (same finding as above) | same |
| U21 | n | minor | Ming misquoted (the word has 千每的; 千戶每的 is another occurrence) | corrected |
| U21 word 186 | morph | moderate | genitive label "after r" on tümed-ün; the stem is tümed (the plural -d) | "after d" |
| U23 | l | moderate | l has a closing quotation mark Shiratori does not print (l mirrors his marks; the note says he prints none), and "own-Oirat" reverses -jan | closing mark removed; "Oirat-own" |
| U23 word 209 | morph | moderate | reflexive split as separate "-(i)" + "-jan" (see word 135) | one morph -(i)jan |
| U23 word 210 | morph | moderate | morph and note give the Ming 統 / 敎統着 for this word; its Ming is 引着 (the 統 belongs to an earlier occurrence), so "command" was unsupported here | Ming 引着, "lead, guide" |
| U23 | n | moderate | note quotes Ming 敎統着; note does not say the opening mark in i is moved or that the subject is supplied | corrected and added both remarks |
| U23 | i | moderate | "he" after U22 ("He presented them", = Jüchi) reads as Jüchi; the favour and the speech are Chinggis's; the supplied subject was not marked | "[Chinggis]" in square brackets (house practice for supplied words) |
| U24 | i | moderate | "his son" with no antecedent in the plain line (in-ü refers to Quduqa Beki); name spelled "Chechegen" though the Han 扯扯亦格 and Čečeigen have the i | "Quduqa Beki's son"; "Checheigen" |
| U24 | n | minor | note did not say whose | added |
| U24 word 217 | morph | minor | spelling | spelling |
| U25 | n | major | note says the previous unit "makes Quduqa Beki the giver"; it makes him the one favoured (U23) and contradicts the U24 note and the plain lines | corrected |
| U28 word 234 | morph | moderate | genitive label "after r" on Köġüd-ün (stem köġüd) | "after d" |
| U29 | n | minor | Ming misquoted | corrected |
| U29 | n | minor | Ming 蹤 belongs to another occurrence; here 道子 | corrected |
| U29 | n | minor | Ming misquoted | corrected |
| U31 | i | minor | "made it a decree" against house "So it was decreed / he issued the decree" for žarliγ bolba | house wording |
| U31 | n | moderate | note says Shiratori prints the marks only partly and that i places the opening; both marks are printed and i follows them | corrected |
| U33 | n | minor | Ming misquoted | corrected |
| U34 | n | minor | Ming 人口 belongs to another occurrence | corrected |
| U34 word 285 | morph | minor (not counted again) | (same finding as above) | same |
| U34 | n | minor | kürčü left out of i without a word | remark added |
| U35 | l | moderate | berke here has the Ming 深 "deep"; "dense" rests on the Ming 艱難 of another occurrence | "deep" |
| U35 | i | moderate (not counted again) | (same finding as above) | "deep" |
| U35 | n | moderate (not counted again) | (same finding as above) Ming misquoted (艱難 belongs to another occurrence) and "dense" unsupported | corrected |
| U35 | n | minor | Ming misquoted for jabuqun | corrected |
| U35 word 294 | morph | moderate (not counted again) | (same finding as above) morph gloss "dense (Ming 艱難)" against the word's Ming 深 | corrected |
| U35 word 292 | morph | minor | Ming 晩 is üde's; žilda here is 夕 | corrected |
| U36 | n | minor | Ming misquoted | corrected |
| U41 | l | minor | l carries an opening quotation mark; Shiratori prints none here (the note says so) | removed |
| U41 | l | minor | closing mark likewise | removed |
| U41 | n | moderate | Ming misquoted: this word has 嚴 行 (剛硬 is from another occurrence) | corrected |
| U41 word 333 | morph | moderate (not counted again) | (same finding as above) morph gloss says Ming 剛硬 against the word's 嚴行 | corrected |
| U42 word 349 | morph | moderate | genitive label "after r" on čerig-ün (stem ends in g) | "after a consonant" |
| U42 | n | minor | Ming misquoted for jabuqu | corrected |
| U42 word 355 | morph | minor | "to" against l and i "at/in the passes" | "at, in" |
| U42 word 357 | morph | moderate | "-žeġül-" lumped as one causative; elsewhere in this part (ürgeġülžü, kirügedeġülžü) the causative is -ġül- | split into -že- (uncertain) + -ġül- |
| U42 | n | moderate | note follows the lumped analysis | aligned with the morphs |
| U43 word 358 | morph | minor | lemma spelled hulaγ̇an; the glossary (and conventions: plain γ where the glossary has it) writes hulaγan | hulaγan |
| U46 word 380 | morph | minor | lemma spelled hulaγ̇an; the glossary (and conventions: plain γ where the glossary has it) writes hulaγan | hulaγan |
| U39 word 321 | morph | minor | lemma Boγ̇orču; the glossary head is Boγorču | Boγorču |
| U42 word 351 | morph | minor | lemma qaraγ̇ul; the glossary head for qaraγ̇ul-un is qaraγul | qaraγul |
| U44 word 363 | morph | moderate | genitive label "after r" on čerig-ün | "after a consonant" |
| U44 | n | minor | calls the Han character 你 "the Ming"; it is the transcription, not the gloss | corrected |
| U44 word 368 | morph | minor (not counted again) | (same finding as above) | corrected |
| U46 | l | minor | l drops the causative -ġül- of kirügedeġülžü (Ming 敎鋸着), while ürgeġülžü is "making-carry" | "having-had-sawn" |
| U47 | i | minor | i drops erüge "smoke-hole", which l and the note keep | smoke-hole restored |
| U47 | n | minor | Ming misquoted for qurimlan | corrected |
| U48 | i | minor | i says "with"; the note (and the Mongol: dative -dur) reads "at her place" | "at … 's" |
| U49 | i | minor | superlative "fairest" for γoγ̇astan (Ming 美每有, no superlative) | "fair" |
| U50 word 431 | morph | minor | Ming misquoted (this bolun has 做) | corrected |
| U53 | n | minor | note does not say that the quotation marks in i are supplied | remark added |
| U55 | l | major | l has "Tumad hundred" for žaγ̇un Tumad-i: order reversed and the accusative -i dropped | "hundred Tumad-(object)" |
| U55 | n | minor | Ming 百 is not bracketed in this word | corrected |

## Pass 2 — gloss.json (every change)

| Unit | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| töġeles | gloss.json | moderate | name written "Töges" (ġ is g; the l is lost) | "Tögeles" |
| jedi | gloss.json | minor | "Yedi" against house practice for Shiratori J in names | "Jedi" |
| čečeigen-i | gloss.json | minor | spelling drops the i of Čečeigen / 扯扯亦格 | "Checheigen" |
| aγ̇ulžaba | gloss.json | moderate | passive "be received / was received" for the active Ming 拜見 | active sense, as in the corrected morph and i |
| erbegežeġülžü | gloss.json | moderate | entry lumps -žeġül- as one causative; the causative elsewhere in the part is -ġül-; now matches the corrected morphs | split |
| botoqui-tarqun-dur | gloss.json | minor | entry pinned to this line ("her place"); entries are to be general to the form | general |
| berke | gloss.json | moderate | known entry (hard, severe, difficult; Ming 艱難) does not cover berke with Ming 深 "deep forest"; the reader would see "difficult" under a deep-forest line | broadened (old entry whole + " · " + new reading) |
| žilda | gloss.json | minor | known entry rests on Ming 晩 or 悅; here the Ming is 夕 | broadened (old entry whole + " · " + new reading) |
| irgen-dür | gloss.json | minor | known entry says only "among the people, in the folk"; here the sense is "to / against the people" | broadened (old entry whole + " · " + new reading) |
| uduridun | gloss.json | minor | known entry rests on Ming 敎統着 (command); here the Ming is 引着 | broadened (old entry whole + " · " + new reading) |

## Findings refused (not changed), with the reason

1. **Glosser's report of morph/word misalignment** (`žer žebseg`, `hulaγ̇an buqa-jin`, `hoγtočin…kirügedeġülžü`): refused as a non-finding; see "What was checked" — verified by index and by Ming-gloss match.
2. **U29 `sai` ("just") left out of `i`**: `i` "Setting out from home" does not show Ming 纔; the note says why sai is read "just", and an idiomatic "just setting out" would be worse English. Left.
3. **Separate `-(i)` + `-jer` / `-jar` in the instrumentals** (U2, U13, U22, U35, U43, U46): the published parts mix `-(i)-jer`, `-(i)jar` and `-jer`; no house rule exists, and the draft is consistent within the part. Only the reflexive `-(i)jan`, which conventions (227–229) do fix, was changed.
4. **U31 `čima-da` split `-ma-da`**: the known glossary entry treats čima-da as či + dative on the oblique stem; the morph follows it. Left.
5. **`l` spelling of names (Jüči, Bo'orču, Chinggis)**: published parts mix Shiratori's and English forms in `l` (e.g. Bo'orchu in 208–210, Boγ̇orču-to in 218–223); `Chinggis` is the established `l` form. Left.
6. **U6 note "the four sons of Chinggis already named"**: an inference, not a claim about the page, and the sons are named in earlier published parts. Left.
7. **U20 `i` "from the Shibir … and the Bajigid on"** and the U20 note's "beginning with the first-named": awkward, but the note already marks the sense as doubtful and nothing in the Ming decides it. Left.
8. **U36 `qaraγ̇ul-a` "by" with active verbs**: the note already says the scouts are the doers and the known entry covers the dative of agent; left as a flagged doubt.
9. **U44 as a whole** (counted men, rods): the note admits it is a guess and `i` follows the Ming word by word. Left.
10. **`Qaṅγas` → "Qangqas", `Ursud` → "Ursut", `Oirad` → "Oirat", `Kirgisud` → "Kirghiz", `Önggüd`**: consistent with house practice (Qongqotan, Qanghar-Qan, Önggüd) and with the English spellings of the peoples; left.
11. **U1 note on Idu'ut being later a title**: outside knowledge, but marked "nothing in this text says so". Left.
12. **U18 note: `Digin` as a title**: marked "probably", Ming gives 人名. Left.
13. **U7 `i` "sent back an answer, he said"** merges ilerün and ügüležü; the note defends the reading. Left.
14. **`oluγsan` (olu-) against the glossary head `ol-` of oluγ̇asu**: the glossary itself has both; the morph keeps olu- for oluγsan. (oluγ̇asu was brought to the glossary head ol- + -uγ̇asu, see pass 1.)
15. **Broadening `qataṅγuj-a` for Ming 嚴**: the known entry's sense (hard, stern) fits; no broadening needed.
16. **Remembered English**: apart from the U3 simile (rebuilt), no phrase in `i` read as remembered; the rest follow the grammar and the house wording of earlier parts.
