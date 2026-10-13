# Review, pass 1 — hammurabi-laws-141-152

Reviewer: adversarial pass 1. Backup of the drafter's file: `/tmp/claude-0/s/units-141-152.bak.json`.
Units are numbered U0–U38 in file order (U0 = §141 first unit XXIII 33 … U38 = §152 first unit XXV 52, U39 = XXV 59).

## What was checked
- Structure: 40 units; `ln`/`p` only on the first unit of each of the twelve laws (141–152, units 0, 5, 10, 12, 15, 18, 22, 23, 27, 29, 33, 38); `col`/`line` of every unit agrees with its `nl` count and with the next unit's start; all 182 of Harper's lines are present, and the words on every line match Harper's word count (script check, no mismatch); `nl` is on the first word of each new line after the unit's first, never on a glyph.
- Mechanics (script): every glyph `sign` exists in signs-cuneiform.json; every word's `morph` covers every glyph exactly once; `reading` reconstructs from the glyph `tr`s (the only differences are the determinatives {meš}/{šal}/{giš}, which carry `tr` "" by convention, as in the published parts); no ḳ anywhere in reader-facing fields.
- Plates 37–42 (PDF 289–299) rendered at zoom 3–6 and read for: the É signs (XXIII 41 É-za against XXIV 8 bi-za, which is BI; XXIV 79, XXV 2/6/12), the SAL / SAL+KUR groups (XXIII 54–57), A.ŠÀ / GIŠ+SAR / É with no endings (XXV 12), ku-nu-uk-kam and iš-ru-uk-šim (IG as uk, same choice as laws-1-10 §5), the SAL KUR + plural marks of amâti (XXIV 58), the first sign group of XXIV 65 (TAG + MA, so šum-ma, Harper's "šuma" is a misprint), DI in ḫi-di-tam (XXIII 67), the DAM.GÀR row (XXV 60). The line layout of the plates (two-row boxes for the long lines) agrees with Harper's line division. Every other sign was checked for presence and plausibility against the line's sign count, not drawn out one by one; no sign was found wrong.
- Grammar of every note, original → `l` word by word, `l` ↔ `i`, consistency with the published parts (127–140, 112–126, 42–51, 52–65, 26–41, 1–10, gap-a/b) and conventions.md house renderings. No modern translation opened or consulted.

## Changes made (unit · field · severity · what was wrong · what done)

| # | Unit | Field | Sev | Wrong | Done |
|---|------|-------|-----|-------|------|
| 1 | U4 (§141, XXIII 56) | n | high | Last two sentences said the first wife "is not mentioned again: she has the full position, and the second woman is a servant-wife" — the reverse of the grammar. zinništum šī is the misbehaving wife, who stays *like a slave-woman*; the šanītam the husband takes is the new wife. | Replaced by a correct statement: she is not divorced, she stays in the house in a slave-woman's rank, the second woman becomes the wife. |
| 2 | U2 (§141, XXIII 44) | l, i | medium | ezēbum rendered "leave"/"let her go" while the published §137–138 render the same verb (izzibši, ezēbim) "divorce" ("he shall divorce her", "to divorce his face"). The same form izzibši was "let her go" in U2 and "divorce" in U25. Also "divorce-money" where §139 has "divorce payment" (uzubbûm), and "says" for the perfect iqtabi while U3 has "has not said". | l: "I-divorce-her", "he-shall-divorce-her", "her-divorce-payment". i: "If her husband has said, “I divorce her,” he shall divorce her; nothing shall be given to her for her journey (?) or her divorce payment." |
| 3 | U3 (§141, XXIII 52) | l, i | medium | Same: "not I-leave-her"; i "has not said" now matches U2. | l: "not I-divorce-her"; i re-set with the same quotation as U2 ("I divorce her"). |
| 4 | U25 (§148, XXIV 75) | l | medium | l "not he-shall-leave-her" against i "shall not divorce"; published l uses "divorce". | l: "not he-shall-divorce-her". |
| 5 | U17 (§145, XXIV 40) | l, i, n | medium | uštamaḫḫar (Št of maḫārum) rendered "shall-rank-equal / shall not rank equal with the wife": not the form's sense, and inconsistent with §146 uštatamḫir "has made herself equal". | l: "she-shall-make-herself-equal"; i: "That šugītum shall not make herself equal to the wife."; note says the Št is reflexive and matches §146. |
| 6 | U15 (§145, XXIV 28) | l, i | medium | ušaršīšuma rendered "she has not given him sons" / "caused-him-to-get"; the published §137 renders the same verb "caused-him-to-have" / "has provided him with". | l: "she-caused-him-to-have-and"; i: "she has not provided him with sons". |
| 7 | U26 (§148, XXIV 80) | say, n | medium | `say` uššabma, while the note says the b "is said and written m" (Harper uš-ša-am-ma): the two contradict. | `say` uššamma; note now says the b becomes m before -ma and the form is said uššamma. |
| 8 | U33 (§151, XXV 26–34) | i, n | medium | "has had a tablet deposited": "deposited" is not in uštēzib (Š of ezēbum "to leave"); invented sense. | i and note: "has had a tablet left (as a record)" — grammar kept, the sense left to the note. |
| 9 | U29 (§150, XXV 10) | l, i | medium | "sealed deed" for kunukkam; laws-1-10 §5 (same word, same sign group) has "sealed document". | "sealed document" in l and i. |
| 10 | U37 (§151, XXV 50) | say, n | medium | `say` ḫubullīša with a long ī; U35 has ḫubullišu and the case vowel before a suffix is short (cf. bītiša). | `say` ḫubulliša; the note's quotation of it corrected the same way. |
| 11 | U21 (§146, XXIV 56) | l, say, n | low | l "slavery" against i "the mark of slavery" (the note itself says Harper's sense is "slavery", later dictionaries "slave-mark"); `say` and note had a hyphen "išakkanši-ma" (syllabic words carry none). | l: "the-slave-mark (?)"; `say` išakkanšima; note spelling the same. |
| 12 | U1, U16, U30, U31 (glyphs) | role | low | The pronominal suffix signs za (É-za), šu (É-šu), ša (DUMU{meš}-ša, DUMU-ša) were `comp`; the published parts mostly give suffix signs `phon` (É-ti-šu, É-ša, DUMU{meš}-ša in 127–140) and keep `comp` for case endings (SAL-tim, KUR-um). | Changed those four glyphs to `phon`. SAL-tim (U17) stays `comp`. |
| 13 | U9 (§142, XXIV 5) | n | low | "ittallak … doubling the l for 'going away'" — vague; the form is the Gtn present of alākum (as the note on ittanaššiši, U26, already calls the Gtn). | Reworded: Gtn (iterative) present of alākum, the code's form for "she shall go away". |
| 14 | U7 (§142, XXIII 66) | n | low | Last sentence (two rows on the plate, stray mark under the fourth sign) is apparatus clutter and confusing in a reader-facing note. | Removed. |
| 15 | about | about | low | "divorce-money" (house: divorce payment); "and she stays on as a servant" left it unclear who stays. | "divorce payment"; "while she stays on in his house as a servant" (she = the first wife). |

Counts: high 1, medium 9, low 5 (15 change entries; entry 12 covers four glyphs).

## Findings refused (with reason)
- U13, U24, U25, U34 i: the added "and"/"but"/lowercase "if" joining protasis clauses that the Akkadian chains without a conjunction. It is the English needed to read a long šumma chain; l stays literal. Kept.
- U35, U37 i: singular "creditor" against the plural verb iṣabbatu in l ("they-shall-seize"). The note already says the plural verb is odd and the number UNCERTAIN; "his creditor shall not seize his wife" is the sense the law needs. Kept.
- U8, U10 i: "goes out and about (?)" adds "and about" that is not written. Kept: the (?) and the note say it is a guess at waṣī/waṣiat; a bare "goes out" would mislead less, but the owner's rule is "say it is uncertain", and it is said.
- U0/U1: `uzappaḫ` "neglects" and `zikiltam izakkil` "plays the fool": Harper's glosses, flagged in the notes as superseded/uncertain. Kept.
- U2 note: "(a stative or imperative ezib with -ša)" is an odd analysis of ezibša (-ša is normally the suffix "her" on a noun), but the note already marks the verb form UNCERTAIN and the quoted sense "I divorce her" is the one the context fixes. Kept, not rewritten without a source.
- U14 `imaggarūšu`: -šu for the dative -šum (magārum "to agree to him"); Harper writes šu and the note glosses "him". Kept as printed.
- U28 `ušallamšimma` Harper's missing hyphen: matches the published §137 treatment. Kept.
- U29/U1 ku-nu-uk-kam KA for kam: matches laws-1-10 §5 (KA:kam). On this plate (XXV 15) the last sign looks more like a lozenge than KA; the published part made the same choice, so the sign key is kept for consistency and the question is left for the owner (see unresolved).
- U20/U22 "sell" for ana kaspim nadānum: l keeps "give … for silver"; i's "sell" is the sense and the note says so. Kept.

## Unresolved (for the second pass / owner)
- ku-nu-uk-kam, last sign (XXV 15): KA key with value kam inherited from laws-1-10; the plate may show the KAM sign instead. Same question affects the published part; not changed here.
- DAM.GÀR (XXV 60): the drafter's note that the plate row may carry a phonetic complement stays UNCERTAIN; the glyphs are left as DAM + GÀR with no complement.
- The glossary (gloss.json) does not exist yet; the lemmas in `morph` are unchecked against it (second pass).

---

# Review, pass 2 — hammurabi-laws-141-152

Reviewer: adversarial pass 2. Backups: `/tmp/claude-0/s/units-141-152.pass2.bak.json`, `/tmp/claude-0/s/gloss-141-152.pass2.bak.json`, `/tmp/claude-0/s/review-141-152.pass2.bak.md`. Plates 37–42 (PDF 289–299) rendered at zoom 3 and cropped at 5–10x; Harper's printed glossary and his English were read from the PDF text layer to check what the notes say "Harper" gives (his English only as a check on the notes' statements about him, never for wording).

## What was checked
- gloss.json, by script and by hand: all 19 new entries are genuinely new (none overlaps an earlier glossary); every lemma used in the units has an entry; all 29 `__broaden__` entries (the brief said 32; the file has 29) are the latest published holder's entry WHOLE + " · " + new reading (holders: 127–140, 112–126, 100–111, 11–25, gap-a, litany). Every form quoted in the 48 entries was looked up in the units: all occur, with the grammar label of the unit note. The 56 lemmas not broadened have old entries that cover this part's uses.
- The 22 linecheck lines on the plate (below), the pass-1 edits (glyph roles for the pronominal suffix signs; `say` changes uššamma, ḫubulliša; l/i changes), and the full checklist: grammar labels in every note, original → l word by word, l ↔ i, remembered English, house renderings, q not ḳ (no ḳ in the built file), l ↔ i tenses.

## The 22 linecheck lines, confirmed on the plate
XXIII 56, 73, XXIV 15, 49 (SAL + ši + i: SAL is the head-and-tail sign, same shape as in XXV 1, 26, 36, 44, 53); XXIII 57 and XXIV 16, 45, 49 (SAL + KUR = GEME₂); XXIV 10 (SAL, šu, a, ti); XXIV 18, 60 (DUMU + ME + EŠ: the TUR sign followed by the two plural marks); XXIV 38 (a, na, É, šu: the nested-box É); XXIV 54, 63 (a, na, KÙ, BABBAR: the two lines show the identical four signs); XXIV 79 (É in third place); XXV 1, 26, 36, 44, 53 (SAL after TAG-MA / LA-MA / Ù-TAG-MA / zinništum ši-i); XXV 12 (A, ŠÀ, GIŠ, SAR, É: five groups, É last); XXV 21 (a, na, DUMU, ša). All agree with the glyphs, with the two exceptions below, which stay open. Also looked at: e-zi-ib-ša (XXIII 45, 53) ends in the ša sign (the X-crossed sign of mu-ti-ša), not ši.

## Changes made (unit · field · severity · what was wrong · what done)

| # | Unit | Field | Sev | Wrong | Done |
|---|------|-------|-----|-------|------|
| 1 | U29 (§150, XXV 15) | glyph | medium | ku-nu-uk-kam ended in KA with value kam (inherited from laws-1-10). The last sign on the plate is the small crosshatched lozenge, the same sign as the KAM of na-aš-pa-kam (XX 11, laws-112-126, where the owner question of 2026-10-13 is recorded). | Glyph 4 is now KAM; note says the sign is the lozenge KAM and not KA. laws-1-10 not touched (QUESTIONS.md entry of 2026-10-13 already covers it; this part now follows 112–126). |
| 2 | U1, U8, U10 | l | medium | ušamṭa / ušamṭaši (Š of maṭûm, III-weak: the present ends in -â, the preterite in -i; the signs spell -a) rendered in l as "has-belittled" while the i says "belittles" and the parallel uzappaḫ is a present. | l: "she-belittles", "he-belittles-her". |
| 3 | U1, U8 | n | medium | U1: "the textbook form would end in -i" as if the -a were irregular; it is the present. U8: "he has belittled her". | Notes say present (ušamṭâ), vowel still UNCERTAIN; "he belittles her". |
| 4 | U9 (§142, XXIV 5) | n | medium | pass 1 labelled ittallak "Gtn (iterative)". ittallak is the Gt present of alākum (the Gtn present is ittanallak). | "Gt-stem present … not the Gtn, whose present would be ittanallak". The Gtn of ittanaššiši (U26) is correct and stays. |
| 5 | U0 (§141) | n | medium | "Harper’s glossary gives zikiltu … and zakālu": his glossary files them as šikiltu and šakālu (his text spells z). | Note and entries say so (lemmas stay in z, following the signs; uncertain). |
| 6 | U2 | n | medium | "(a stative or imperative ezib with -ša: “(I) leave her”)" is not a coherent analysis, and "certain from the clause after it" overstates. | The note says the form is UNCERTAIN because the object "her" on a verb is normally -ši; the sense is fixed by the clause that follows. izzibši "he shall divorce her" (was "let her go"), "divorce payment" (was "divorce-money"), and Harper’s "on her departure" for ḫarrānša added. |
| 7 | U32 (§150, XXV 24) | n | medium | aḫim read as aḫûm "outsider" with no word that Harper reads it as aḫum "brother" ("but to a brother she may not"). | Harper’s reading stated; ours marked UNCERTAIN. |
| 8 | U35, U37 | say, n | low | iṣabbatu said short although the note calls it a plural (-u); the house rule is long ū for the plural (ibaqqarūši, ippalū). | `say` iṣabbatū; notes quote it so. |
| 9 | U7 | n | low | "īšu … in the present" (īšu is a 3rd-person form read as a present). | Reworded. |
| 10 | U25 | n | low | "he shall not leave her" against i "divorce". | "divorce her". |
| 11 | U24 | i | low | "he may take her": "her" could be read as the sick wife. | "to take another woman, he may take her". |
| 12 | U19 | n | low | "perfect (with the t of the perfect after the Š-stem’s š) of maḫārum “to be equal”": label and sense disagree with the Št entry. | "Št-stem perfect of maḫārum (“to face, be level with”)". |
| 13 | gloss, new | zikiltum, zakālum | low | Harper’s glossary said to give z-forms. | His š-lemmas named. |
| 14 | gloss, new | maṭûm-Š | medium | "the textbook form would end in -i, so the vowel is UNCERTAIN" (present vs preterite not told); "he has belittled her". | Present ušamṭâ, "he belittles her"; the vowel still UNCERTAIN. |
| 15 | gloss, new | parāsum-N | low | bare ipparras listed as a met form (only ipparrasma occurs). | ipparrasma first; ipparras as the present. |
| 16 | gloss, new | ezēbum-Š | medium | uštēzib given the unqualified sense "to have deposited (a document)": that is the context’s sense, not the Š-stem’s (šūzubum is "to save, rescue"). | Marked UNCERTAIN, with the reason. |
| 17 | gloss, broaden | -šu | low | "before -ma or with the same assimilation: aššassu": aššassu has no -ma. imaggarūšu "on a verb, him" (it is the dative, Harper writes -šu for -šum). | Fixed both. |
| 18 | gloss, broaden | ezēbum | low | izzibši "he shall let her go" (unit: divorce); ezibša not flagged for -ša. | "he shall divorce her"; -ša/-ši remark. |
| 19 | gloss, broaden | aḫāzum | low | "a permission when set beside a prohibition" (pinned to the §144–145 pair); iḫḫazu (U34) missing. | General statement of the permission; iḫḫazu added; iḫuzma "he took, and". |
| 20 | gloss, broaden | nadānum | low | "preterite iddin (id-di-in-ma) “has given”" repeats the old text (iddinma). | Cut; inaddin of a woman and inaddišši kept, with the sale sense. |
| 21 | gloss, broaden | ṣabātum | low | iṣabbatu short (see 8). | iṣabbatū. |
| 22 | gloss, broaden | mārum | low | "plural mārī “sons” (DUMU{meš})" repeats the old entry. | Only mārūša, mārīša added. |
| 23 | gloss, broaden | bēlum, eli, bītum, aššatum | low | New text repeated the old: bēl ḫubullim "creditor"; the example ḫubullum elišu ibašši (also under bašûm); "construct, É" and aššassu/aššatišu. | Trimmed to what is new (bēl with suffixes; elišu/eliša/elišunu; bīt awīlim, bīssa, bītišu; aš-ša-zu spelling). |
| 24 | gloss, broaden | alākum | medium | "Gtn present ittallak" (see 4). | "Gt present ittallak … the Gtn would be ittanallak". |
| 25 | gloss, broaden | ḫarrānum | low | Harper’s own "on her departure" absent. | Added. |

Counts, pass 2: high 0, medium 9 (entries 1, 2, 4, 5, 6, 7, 14, 16, 24; 3 is the note half of 2), low 16. Pass 1 plus pass 2 together: high 1, medium 18, low 21.

## Findings refused / left (with reason)
- zikiltum/zakālum lemmas kept in z: they follow the signs of the text (zi-ki-il-tam, i-za-ak-ki-il); Harper’s š-spelling is stated in the entries. Renaming the lemmas would rewrite the unit morphs for a root that is UNCERTAIN anyway.
- "support" for ittanaššiši (U26), "plays the fool", "may take" etc.: each is built from the grammar and explained in the note (našûm "carry", the Gtn "keep carrying"); they coincide with ordinary English for the sense, not with any translation known to the reviewer. Kept.
- U6 "in her babtum (?)": the babtum question is kept open (Harper “defects”, the later "ward"), as in §112–126.
- Old entries not broadened though this part uses them in a slightly new way: šarākum (išrukšim "he gave as a gift", old: ištarak "give away, hand over"), mutum, uzubbûm: the old texts cover the use. Left.
- Pass 1's refused items stand (and-joins in i, singular "creditor", "out and about (?)", ul imaggarūšu -šu, ušallamšimma hyphen).

## Unresolved (owner / later pass)
- XXIV 58 (it-ti GEME₂{meš} amâti): the plate shows SAL, KUR and then two signs, a lozenge and a three-stroke sign, which do not look like the ME + EŠ of XXIV 18 and 60 (EŠ there is the fan/chevron sign). The count of signs agrees with our six glyphs, so the glyphs stand and the note keeps the plural signs UNCERTAIN; the true plural spelling here is not settled.
- XXV 60 (DAM.GÀR i-ip-pa-lu): the plate row shows about nine groups where we have six glyphs; a phonetic complement (-ra-am) is likely but not read. Glyphs unchanged; the note says UNCERTAIN.
- laws-1-10 §5 kunukkam still ends in KA (published); QUESTIONS.md of 2026-10-13 already carries the question for the later correction pass.
- ezibša (XXIII 45, 53): the plate ends in the ša sign, so Harper’s ša is right, but the analysis stays UNCERTAIN.
- pymupdf: `python3` on this box is /usr/local/bin/python3 without pymupdf; `/usr/bin/python3 ../run3/page.py` works (pymupdf installed there).

## Build and validate (after pass 2)
`python3 ../run3/r3.py build hammurabi hammurabi-laws-141-152` → BUILT hammurabi-laws-141-152: 40 units (one WARN: the 22 linecheck lines, now confirmed above).
`python3 ../run3/r3.py validate hammurabi hammurabi-laws-141-152` → PASS (same WARN only).
