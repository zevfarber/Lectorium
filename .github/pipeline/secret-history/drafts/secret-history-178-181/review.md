# Review, pass 1 — secret-history-178-181 (§§178–181)

Reviewer worked from the Ming glosses, Shiratori's text, the conventions and the published parts only. No modern translation opened or recalled; no Naka Michiyo consulted. Edits made by `/tmp/claude-0/-home-user-Lectorium/b5a26a7b-03ab-5301-93c7-a4cc39b48176/scratchpad/review178_181.py` (plus one one-line gloss reword, noted at the end of that script); `units.json` edited in place; a pre-review copy is in the scratchpad as `units.pre-review1.json`. Unit numbers are 0-based positions in `sentences` (U0 = "ede üges-tür …", U73 = "Araγai irežü …"). Word numbers are packet indices.

## Checks that passed (no change)
- t: every unit's `t` equals the packet romanisation joined by single spaces; 518 words in 74 units, none missing or doubled, `p` on the first unit of §§178, 179, 180, 181.
- Word 4 `"Ai! Soiluγ!` (one Han word 唉-莎亦魯黑, rom with a space): fine. `bare()` strips only edge punctuation, so the reading is "唉-莎亦魯黑 Ai! Soiluγ" and `R.tokens` yields `ai` and `soiluγ`, both in novel-forms; the glyph `tr` keeps the printed text. Cosmetic only; the word is one entry, with two morphs. Not changed.
- Every lexical morph's bracketed Ming gloss reproduces the packet gloss (split brackets on compound words are partial but exact), except word 340 (below).
- Names against the house/published forms (Wang Qan, To'oril, Toqto'a, Sükegei-Jegün, Arqai-Qasar, Qachi'un, Achiq-Shirun, Nekün-Taishi, Charaqai-Linggu, Bartan-Ba'atur, Sacha, Taichu, Qutula Qahan, Bilge-Beki, Tödögen): consistent.

## Changes

| Unit | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| U9 | i, n | moderate | "made the Qan, my father, part from me" reversed the ablative: ečige-dēče is the one parted *from*; min-u after it is "my" (as in Qān ečige-de min-u, U32), and "the sight of me" supplied an object that is not there. | i: "unable to bear the sight, made me part from my father the Qan"; note says who parts and whose sight are unstated. |
| U36 | i, n | moderate | The genitive qojar-un ("of the two") was made the subject ("Tumbinai and Charaqai-Linggu seized Oqda"), against the draft's own morph; "Deġü keġekü" quote nested in single marks. | i: "Oqda, of Tumbinai and Charaqai-Linggu, the two, came, carried off as a slave" (passive flagged in the note as mine; bilažu is active, agent unsaid). |
| U1 | i, l, n, morph w6 | moderate | qaγačaqu-ju: the Ming has 麽 and the published parts (§§154–157 ögkü-jü, §§165–168 žokiqu-ju) read -ju after a participle as a question; the draft's own note said "the Ming 麽 marks the question" in U14/U67, yet here made it a finite "is". | Read as a question ("Am I parting from my own son?"); -ju morph reglossed. |
| U2 | n, morph w9 | minor | Hirižekü-jü has the same shape (Ming 有, no 麽). | Kept as statement, note and morph now say it may be a question too. i: "drifted from the whole affair" → "parted from the affair" (the Ming says 分離, "parted"; "whole" and "drifted" were not in it). |
| U20 | i, n | moderate | i asserted "Of the senior line" for deġere-eče (Ming 上 處, "from above"); n said the sons "are named in the next unit", but published §§43–54 make Sacha and Taichu sons of Qutuqtu-Yürki, not of Bartan. | i: "From above: the sons of Bartan-Ba'atur --"; note says the relation to Sača, Taiču is not settled. |
| U35 | i, n | moderate | "as to a younger brother" has no "as" in the text; deġü-de is in apposition to Toγ̇oril. | i: "to the younger brother To'oril"; note corrected. |
| U39 | n | moderate | Said -u is the genitive "after a stem ending in a vowel"; Kirsaγ̇an ends in n. | Note: genitive after n, printed without Shiratori's usual (n); morph w272 reglossed to match. |
| W70 (U11) | morph, n | moderate | uγdarun analysed as an invented stem "uγda-" though the Ming 被飮 and word 65 uγ̇uqu give uγ̇u- "drink" + passive -γda-. | Morph rebuilt as uγ̇u- + -γda- + -run; note says "was served" is my reading of the passive. |
| U11 | i | minor | "because I rose first" made a causal clause out of -run "when". | "When I rose first and was served first, you were jealous of me." |
| U66 | i, n | moderate | "tacking himself on to a sheep's tail": "himself" is not in žübčižü qonin-u seġül (Ming 續着 "continuing"). | "goes about adding on to the sheep's tail"; note says so. |
| U6 | i | minor | "catching it in" — kižü is Ming 盛着 "filling, holding", and l says "putting". | "putting it into a small birch-bark pail". |
| U12 | n | minor | qoroqun Ming 費的 reads as a participle; with baradqun a converb there is no finite verb, which the note did not say. | Note says "have you wasted" supplies one and is a guess. i unchanged. |
| U14 | n | minor | i folds tebčižü and gesü (both "cast off" in the Ming) into one verb without saying so. | Note added. |
| U15 | l | minor | "against-ing-u" is not English for 對付着. | "dealing-with-u". |
| U32 | i | minor | "Father Qan, my father" was redundant for Qān ečige-de min-u; "old ties" added a noun the Ming (厭舊 "tire of the old") lacks. | "my father the Qan"; "tire of the old". |
| U53, U70 | i, n | minor | "retainers" for nököd; published parts use "companions". "sent (them) off" supplied an object for ilebe. | "companions"; "sent it off" (the message, as in U7, U12, U34). |
| U63 | n | minor | "(the speaker, Chinggis, is not named)" was confusing. | Note says Senggum is the speaker (ügülerün: at word 448 directly precedes the quote at 449); "he" is Chinggis, unnamed. |
| U64 | i, n | minor | "yet did he not also say …" added "yet" and "also"; the Ming 麽 is on the second ese-ü keġekü büleġe (473) only. | i trimmed; note says this one may be a plain statement ("he never said"). |
| U65 | i | minor | Stray opening single quote. | Removed. |
| U68 | i | minor | "seen through" is stronger than uqaγdaba 可覺了 "was perceived", and l says "perceived". | "have been perceived". |
| U8 | n | minor | "each carrying -da only on the second" unclear. | Reworded. |
| U22 w153, U27 w184 | morph | minor | jadažü and abčiražü glossed "-žu converb (back-vowel form)" though written -žü. | "written -žü here, though the stem is back-vowel". |
| U47 w345 | morph | minor | naidažu gloss "envy" under Ming 疾惡 "loathe". | Gloss says Ming 疾惡 "hate". |
| U48/U51 w355, w377 | morph | minor | žoboγ̇an called -γ̇a- "causative", žoboγ̇ažu called the same -γ̇a- "stem formative": inconsistent. | Both: žoboγ̇a- "suffer hardship" (with 敎 "cause" at 355), converb endings separate. |
| U47 w340 | morph | minor | Ming gloss bracket respelled 其間; the packet prints 其閒. | Restored 其閒. |
| about | text | minor | "Senggum's angry answer": "angry" is not in the text. | "Senggum's answer". |
| all quoted units | l, i | moderate | Quotation marks: outer quotes were single in i and mostly absent in l; mid-speech units re-opened a quote (U16, U18, U24, U48, U49, U65); published parts use double marks in both l and i. | l and i now carry double marks at Shiratori's openings and closings (U1–2, U3–4, U7, U9–12, U14–34, U36–42, U44–53, U54–60, U63–68, U70); single marks only for inner quotes (U17, U18–19, U21–23, U36, U40, U50–51, U63–65); no re-opening mid-speech. Two places are mine, flagged in notes: the close of the §180 speech before keġežü (U42; Shiratori prints none) and the quote opened at U69 after his mark at 477. |

## Doubts the drafter flagged, checked and kept
- **§181 words 449–477 (U63–U68).** The speaker is Senggum (word 448 "ügülerün:" opens the quote at 449). That "he" is Chinggis and that this is a charge of double-talk is a reading, not a fact; the Ming 幾時 might equally make "keli" a rhetorical "when did he ever …". Kept as the drafter's tentative reading, notes say so.
- **U14–15 gesü, ileġü-ü, žüqažü-u.** Kept; no better grammar available from the Ming (要弃/棄 for gesü; 對面/對付着). The -ü/-u endings stay "uncertain force".
- **U21–22 jada-.** Both readings ("unable to say" / "could not bring it about") are in the note; the English "(bring it about)" in brackets stays.
- **U18 Qān-lu.** Kept "just as"; -lu is uncertain and the note says so.
- **U19 aγsa-γ̇ar, deġe-re-eče (U20).** aγsa-γ̇ar kept; deġe-re-eče kept at "from above" (see U20 above).
- **§178 toli, onuči, kižü, ilebe.** toli left untranslated in l and "his own little finger" in i; kept, the note says it is a guess. onuči "notch-cutting" kept. kižü "putting into" kept (U6). ilebe "sent" kept, in line with the glossary and context (a pail and a speech that is "given to my son").
- **qoroqun/baradqun (U12).** Kept as converbs per the Ming; both the command reading and the participle reading remain open; the note now says so.
- **U44–U45 deġeltü/ničügün.** Kept ("born clothed" / "born bare"); the Ming says no more.
- **U71 eme köġün.** Kept "the wife and son" (Ming 妻 子, two persons); "wife's son" cannot be excluded by the grammar.
- **Toγ̇oril = Wang Qan** (U35, U71): consistent with published §§100–104 and §§105–108; kept.

## Findings refused
- Rewriting U40 ("Jegei-Qungtaqar's son is To'oril … — you.") to a vocative reading: both parse; the drafter's note already covers the second či.
- Replacing "packed up" for šiγažu (U29–31): Ming 擠 "squeeze"; the note already calls it uncertain.
- Changing "Alas!" for the two cries at U1: the Ming gives only (發喘); the note says so.
- Changing the unit segmentation: breaks follow Shiratori's stops and the natural clauses; U14–U34 (one speech) is long but each unit is a readable clause; no merge or split needed.
- Re-deciding hirižekü-jü as a question: only the Ming 麽 on the first supports it.

## Remaining doubts for pass 2 / the glosser
- Glossary entries for jada-, -ju/-jü (now "question particle after a participle" in U1; keep the entry broad), naida- (Ming 疾惡 as well as 妒), žoboγ̇a-, uγ̇u- (passive uγdarun), kižü (ki- "put in"), and deġe-re-eče are drafter-uncertain.
- U64 ese-ü: question or "never said".
- U42: the §180 speech has no closing mark in Shiratori; the closing before keġežü is the reviewer's.
