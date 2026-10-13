# Review, pass 1 — hammurabi-laws-127-140

Reviewer pass 1 of 2. `units.json` was edited in place by script (backup of the drafter's version kept outside the repo). 33 units, 175 stele lines, 310 words. Counts of the changes below: **3 high, 19 medium, 15 low** (37 rows). Units are cited as `[k]` = index in `sentences`, with col/line.

## What was checked and found sound
- Line division: every one of Harper's 175 lines (XXI 25 – XXIII 32) starts a unit or carries `nl` on its first word; no `nl` falls inside a Harper line; every unit's `col`/`line` equals the line its first word stands on (checked by script against packet.md; XXII 75 'u lu' = one word ulu).
- `reading` reconstructs from the glyph `tr` values in all 310 words; no ḳ except one in a note (fixed, row 18).
- Harper's plates (PDF 281–291) were read for: XXI 26, 40, 60; XXII 5, 19–20, 23, 46, 49, 74; XXIII 19, 27, 30 (details below). The remaining signs are not each re-read on the plate: they rest on Harper's transliteration, checked against his List of Signs for every sign value that has a published key (consistent), and on the published parts' keys (IG for uk/ik/iq, GISH for iz/iṣ, UD for ut/tam, A2 for it/id, TAG for šum, DUMU{meš} as TUR + ME + ESH, KU3.UD for KÙ.BABBAR, all as in §112–126 / §100–111).
- Verbatim-overlap check against remembered modern renderings: three phrases that matched a familiar English rendering word for word were rebuilt (rows 8–10 "taken captive", 14 "husband of her choice", 15 "go free"); "shave off half of his hair" was loosened (row 25). No other overlap found. `they shall bind them and throw them into the water` is kept: it is the grammar word for word (ikassûšunūtima … ana mê inaddûšunūti).

## Plate findings (the three added signs, GI/ge, ŠAL.NIN.AN, logograms)
- **XXI 26 (ŠAL.NIN.AN):** the line shows E, LI, then a hexagon sign followed by a small boxed-wedge sign (together NIN), then AN. Compared at the same scale with XVIII 36 (§110, ŠAL.NIN.AN), where an extra hexagon with a long tail stands in front of the NIN.AN group: that extra sign (ŠAL, as in zinništum at XXI 40 and the ŠAL determinative at XXII 74) is **not** at XXI 26. Harper's `e-li NIN.AN` is right, and the published §110 note already says Harper has it "standing alone at XXI 26". Unit [0] changed to NIN.AN.
- **XXII 74 (šu-ge-tim):** the ŠAL determinative (hexagon with long tail) is there; the fifth sign has the box + hooked wedge + long bar + fan shape of Harper's List no. 122 (gi, GE) — not no. 42 (gi, the H-shaped sign with fan). No. 122 is the sign keyed GI4 in §110 (MAL.GE.A). Unit [23] changed from GI to GI4.
- **TIR** (XXIII 19): the line opens with the Winkelhaken stack plus grid sign of List no. 145 (tir). Consistent.
- **SUR** (XXII 20, iṣ-ṣur-ma): third sign has the pointed-right shape of List no. 167 (ṣur). Consistent.
- **KAB** (XXI 60, u-kab-bil-ši-ma): second sign of five matches List no. 46 (kab); BIL is the diamond-and-cross composite of no. 82. Consistent.
- **Logograms in linecheck.md, confirmed on the plate:** SAL (zinništum) at XXI 40 (hexagon + tail, then ši, i) and XXII 23; {d}ÍD at XXII 5 (AN, a gap, A, then the boxed ENGUR sign); URU-šu at XXII 49 (box-sign at line start, šu at line end); DUMU + MEŠ at XXII 46 (DUMU at the left of the first sub-line, MEŠ at its right end); I = a single wedge at XXIII 27. The others in linecheck.md (XXII 18, 35, 51, 54, 58, 68, 75, 80; XXIII 2, 4, 7, 18, 31) were not re-read individually; they are the same signs, and Harper's printed word (zinništum, ali-šu, mârê, kaspam, ⅓) is exactly what those logograms stand for.
- **XXII 12–18 damage:** the plate hatches XXII 13–15 (only the last sign or two of each line survive) and draws Harper's restored signs in outline on 12 and 16–18. The note on unit [12] now says exactly this.

## Changes
| # | Unit · field | Sev | What was wrong | What was done |
|---|---|---|---|---|
| 1 | [2] XXI 35, [3] XXI 42, [5] XXI 54, [7] XXI 68, [17] XXII 37, [20] XXII 57, [32] XXIII 30 · `ln`, `p` | high | Seven laws (§128, 129, 130, 131, 135, 136, 140) had no `ln` and no `p`, so no § chip would be made for them. | Added `ln` 128, 129, 130, 131, 135, 136, 140 and `p: true`. |
| 2 | [0] XXI 25 · word 3, `n` | high | A glyph SAL (ŠAL) was added before NIN.AN; the plate (XXI 26) has no ŠAL there, and the note admitted the group was "taken from the parallel rather than checked sign by sign". | Word is now NIN.AN (NIN + AN, val ugbabtum on NIN, one morph); `n` rewritten with the plate comparison to XVIII 36. |
| 3 | [23] XXII 73 · word 3 glyph 2, `reading`, `n` | high | šu-ge-tim keyed GI (List no. 42); the plate shows no. 122 (gi, GE) = GI4. | Glyph GI → GI4, `tr` gi₄, reading `{šal}šu-gi₄-tim`; note names no. 122 and §110's GE. |
| 4 | [7] XXI 68 · word 4 lemma, `n` | med | ubbiršima labelled D-stem of bârum "the same verb as ubâr in §126"; it is abārum (ubburum), the verb of ubbirma in §1 (published glossary abārum), and §126's ubâr is bârum. | Lemma bârum → abārum; note corrected. |
| 5 | [7] · word 11 lemma, `n` | med | lā iṣṣabit called "a form that looks active", UNCERTAIN; iṣṣabit is the N-stem preterite (inṣabit), a plain passive, matching the sense. | Lemma ṣabātum → ṣabātum-N; note rewritten (iṣṣabit N preterite, ittaṣbat N perfect). |
| 6 | [4] XXI 50 · words 4 and 8 `say`, `n` | med | ubalaṭ labelled D-stem but written with a single l; the D present is uballaṭ (compare ugallabū, ukabbilšima in this part). | `say` uballaṭ ×2; note changed throughout. |
| 7 | [9] XXI 77 · word 8 `say`, `n` | med | `say` ittarṣima and note "ittarṣ, N-stem passive": Harper's it-ta-ri-iṣ-ma is ittariṣma (N preterite); ittarṣi- is not a form. The note also did not say that it-ta-aṣ-ba-at is the perfect. | `say` ittariṣma; note: N preterite (a passive), and the perfect named. |
| 8 | [11] XXII 7 · `i`, `n` | med | iššalilma called the N-stem "perfect" (it is the preterite; the perfect would be ittašlil); `i` "taken captive" is the familiar English phrase, not built from šalālum "to carry off". | Note: N preterite; `i` "has been carried off", note adds "(here, taken away as a captive)". |
| 9 | [15] XXII 27 · `i`, `n` | med | Same two points; the note also said the first line of §133 was "lost to damage and restored", which is not so (the damage starts at XXII 12). | `i` "carried off"; note reworded. |
| 10 | [17] XXII 37 · `i` | med | "before he came back" states as plain fact a sense the note calls UNCERTAIN; "ana pānīšu" is only "before him"; "taken captive" as above. | `i` "has been carried off … before his return (?)"; note adds that "before him" says nothing about a return. |
| 11 | [13] XXII 18 · `n` | med | (a) Numbering: "the standard numbering counts it as the second half of §133" is outside knowledge; (b) iṣṣurma called the perfect; naṣārum is an I-n verb and iṣṣur is the preterite (inṣur); (c) īterub called "the Gt perfect": it is the G perfect (the -ta- infix does not make it Gt); (d) ṣur "not checked on the plate". | Rewritten: §133A decision (below), preterite, "the perfect: the perfect has the -ta- after the first sign", ṣur = List no. 167, matches the plate. |
| 12 | [20] XXII 57 · `n` | med | iddīma called "the perfect"; it is the preterite (iddi + ma; perfect would be ittadi). | "preterite". |
| 13 | [25] XXIII 2 · `l`, `i`, `n` | med | urtabbû read as passive "they have been brought up": the u-prefix D-stem is active; urtabbi + subjunctive -u after ištu = "she has brought up". The note said a new sentence begins here, but the unit before ends in -ma. First-person "not clear to me". | `l` "after her-children she-has-brought-up"; `i` "she shall bring up her children. After she has brought up her children,"; note rewritten (still UNCERTAIN, impersonal). |
| 14 | [27] XXIII 12 · `i` | med | "the husband of her choice" is the stock English rendering of mūt libbiša (overlap red flag); the l is "of her-heart". | `i` "the husband of her heart (the man she likes) shall take her as wife." |
| 15 | [6] XXI 61 · `i` | med | "that woman shall go free" departs from the house rendering of ūtaššar (conventions: "he shall be released") and is a stock phrase. | `i` "that woman shall be released." |
| 16 | [22] XXII 68 · word 1 `say` | med | ālišu (genitive) for URU-šu, object of izīrū after aššum; units [18] and [20] have ālšu. | `say` ālšu. |
| 17 | [24] XXII 80, [26] XXIII 6, [29] XXIII 18, [30] XXIII 22, [31] XXIII 25, [32] XXIII 30 · morph lemma | med | The dative "to her" (-šim: inaddiššim, utarrūšim, ušallamšimma, inaddinūšimma) was filed under lemma -šum "to him". | Lemma -šim in all of them (new glossary entry needed). |
| 18 | [24] · word 8 `say`, word 3 lemma, `n` | med | `say` kirêm (Harper's spelling) where the genitive is kirîm (published parts, gap-a); ḳ in a note (house rule q); the lemma šeriktum disagreed with the q reading the part uses. | `say` kirîm; note says Harper reads q (še-ri-iq-ta-ša) and modern editions k; lemma šeriqtum. |
| 19 | [29] XXIII 18 · word 5 lemma | low | Same lemma šeriktum. | šeriqtum. |
| 20 | [12] XXII 12 · `n` | med | Damage description unverified and in the first person ("as far as I can tell"). | Replaced with the plate-checked description (hatched 13–15, outlines on 12 and 16–18). |
| 21 | [14] XXII 23 · `l` | med | ukannūšima's -ši "her" missing in `l`. | `l` "they-shall-convict-her-and". |
| 22 | [2] XXI 35 · `i`, `n` | med | `i` "drawn up" is not in "iškun" (l: "set"); note called the riksātum "written contracts" (not in the word) and said aššat is spelled with the SAL sign "here" (it is spelled aš-ša-at in syllables; SAL spells aššatim only at XXII 75). | `i` "has not set down her contracts"; "written" removed; SAL sentence corrected. |
| 23 | `about` | med | "a marriage without written contracts", "a betrothed woman", "taken captive" (none in the text; "betrothed" in particular is not there). | Reworded to match the units. |
| 24 | [12], [13], [16], [17], [20] · `i` | low | "another man's house" adds "man's"; the text has bītim šanîm "another house". | "another house". |
| 25 | [1] XXI 30 · `i` | low | "shave off half of his hair" supplies "hair" and sounds like the stock rendering; the word is muttassu "his half". | "shave half (of his hair)." |
| 26 | [3] XXI 42 · `n` | low | "u-tu-lim two lines below (XXI 72)": it is thirty lines on. | "at XXI 72 (§131)". |
| 27 | [5] XXI 54 · `i`, `n` | low | "still living" (no "still" in the text); the kab sign "not checked on the plate". | "is living"; kab = List no. 46, matches the plate. |
| 28 | [8] XXI 74 · `n` | low | "her own household, to her husband's house" contradicts itself. | "sends her back home." |
| 29 | [10] XXII 4 · word 2 `val`, `l` | low | val Nārum where the word is accusative Nāram (§1–10 write val = form); l "the River-god" where the published parts say "the divine River". | val Nāram; l "the-divine-River". |
| 30 | [18] XXII 46, [19] XXII 51 · `n` | low | "Harper notes/says" about a blot and a faint dot: these are the transcription's observations of the scan, not Harper's. | "In the scan …". |
| 31 | [19] · words 3, 7, 8 `say`, `n` | low | ḫāwirīša, abīšunu long ī against the house short i (published abišu, elišu, warkišu, bītišu); illaku for a plural (illakū). | ḫāwiriša, abišunu, illakū. |
| 32 | [5] abiša, [6] sūniša, [9] eliša, [20] warkišu, [29] tirḫatiša, [30] abiša · `say` (and the notes that cite them) | low | Same long-ī against the house short i. | Shortened. |
| 33 | [21] XXII 64 · `l`, `i`, `n` | low | Protasis verbs as a present ("comes back and takes hold") for perfects, unlike [18]/[20]. | "has come back and has taken hold"; note explains iṣṣabat (the t of the perfect taken into the ṣ). |
| 34 | [26] XXIII 6 · `n` | low | "not of the husband's estate as a whole" is not in the words. | Cut to what the words say. |
| 35 | [29] · `n` | low | "tir not checked on the plate". | tir = List no. 145, matches the plate (XXIII 19). |
| 36 | [30] XXIII 22 · `n` | low | ublam: "the -u subjunctive dropped before -am"; the ventive -am takes the place of -u. | Reworded. |
| 37 | [32] XXIII 30 · `n` | low | muškēnum "the middle class of the code"; the published glossary says "the code's second rank". | "the code's second rank". |

## The §133A decision
Kept as the drafter had it: unit [13] (XXII 18–22) and [14] (XXII 23–26) carry no `ln` and no `p`; they ride under §133, so the chips run 127–140 and the title and `part` ("§127–140") stand. The packet's own headings do split it off as "§133A", so the note now says only that: Harper's headings call it §133A, here it carries no number of its own. The "standard numbering" claim was removed (outside knowledge, not Harper). If the build or validator insists on a number, do not repeat 133 (that would make a second §133 chip); the alternative is `p: true` without `ln` on unit [13], only if a visible paragraph break is wanted. No build was run.

## Findings refused or left, with reasons
- [0] `i` "has had a finger pointed at": kept. ušatrīṣ is Š (causative), so "has made a finger point/has had a finger pointed" is the grammar; the note explains it.
- [0] "another man's wife" in `i`: kept; aššat awīlim is "a man's wife", and the accuser is a man, so "another" is the reading of the sentence, not an addition to a word.
- [4] "the wife's husband" for bēl aššatim: kept; the note says it is "the owner of the wife".
- [3] utūlim (u-tu-lim) and itūlim (i-tu-lim): the two spellings are kept as printed (flagged in the notes), lemma itūlum.
- [17] ana pānīšu: kept as UNCERTAIN, now marked in `i` too.
- [25] urabbâ (u-ra-ab-ba): form left UNCERTAIN as the drafter said; I cannot rebuild the ending from the grammar.
- [19] ḫāwirum "husband": left as the drafter has it (uncertain, flagged).
- [23] ušaršušu and šugītum: left UNCERTAIN as flagged.
- [22] innabitu (N of nabātum) and [20] ittabit: left, flagged uncertain.
- Not edited because outside `units.json`: the shared sign glossary entries for TIR, SUR and KAB still say "identification not checked on the plate" (now checked: List nos. 145, 167, 46, plates XXIII 19, XXII 20, XXI 60), and the published glossary entry for ugbabtum says "written ŠAL.NIN.AN" — true for §110, not for §127 (XXI 26 has NIN.AN only).

## For the glosser / second pass
- New lemma: `-šim` "to her, for her (dative -šim)". `ugbabtum` entry to be broadened ("written ŠAL.NIN.AN at §110, NIN.AN alone at §127"). `abārum` broadened with ubbiršima. `ṣabātum-N`, `ṣabātum` (iṣṣabat, iṣṣabtūšu: perfect), `uballaṭ` under `balāṭum-D`. `šeriqtum` (not šeriktum). `šugītum` spelled šu-gi₄-tim.
- Second pass to re-check: units [12], [13] n; [25] n (urtabbû); [23] n (no. 122); and that the validator accepts ln/p on the seven added units.

---

# Review, pass 2 — hammurabi-laws-127-140

Reviewer pass 2 of 2. `units.json` and `gloss.json` edited in place by script (backups outside the repo). Lexical checks used Kohler–Ungnad II (1909, in `source/witnesses/kpu-vol2_djvu.txt`: their syllabic text of §127–140 and their glossary) as a sense aid only, plus the published parts' glossaries; no modern translation was opened. Plate re-check: Plate 34 (PDF 283), XXI 51–53 (aššassu uballaṭ / ù šarrum / ARAD-zu uballaṭ): the line-53 opening sign is a composite with a dotted triangle, consistent with ARAD; nothing contradicts Harper's print. Pass 1's plate findings (NIN.AN without ŠAL, GI4 at XXII 74) were not re-opened. All 33 units, 310 words: every lemma in the units resolves to gloss.json or a published glossary; no gloss.json entry is unused; the three `__broaden__` bases (`ugbabtum` from §100–111, `abārum` and `ṣabātum` from §112–126; `zittum` from §52–65) were checked by script: each equals the latest published entry whole + ' · ' + the new reading.

Counts of the pass-2 changes: **0 high, 17 medium, 23 low** (40 rows; K–U = Kohler–Ungnad II).

| # | Unit / lemma · field | Sev | What was wrong | What was done |
|---|---|---|---|---|
| 1 | [2] · `n` | med | iḫuzma called "the perfect"; iḫuz is the preterite (perfect has -ta-). | "preterite", with the perfect named. |
| 2 | [3] · `n` | low | "as in §112 ff." for the N-stem passive: no such earlier gloss. | Cut. |
| 3 | [4] · `n` | low | Duplicated "Harper prints wara-zu…" sentence; "the king's man" stated as fact. | Tidied; the servant is "understood to be" the wife's partner, "the text says only 'his servant'". |
| 4 | [5] · `n` | med | "The woman is betrothed or married into another household but has not yet lived with her husband": nothing in the words (the text says aššat awīlim, in her father's house). | Replaced with what the text says. Stray ";" / capital fixed. |
| 5 | [6] · `n` | low | iṣṣabtūšu not named as the perfect; ūtaššar "set free" against the house "released". | Perfect named; "released". |
| 6 | [9] · `n` | low | N-stem of tarāṣum stated without hedge. | "read from the form and the sense (UNCERTAIN as a form)". |
| 7 | [7] [10] [18] [19] [27] · `say`, `n`; lemma `mūtum` (gloss + all morphs) | med | Husband is mutum (short u; K–U's glossary separates it from mūtum "death"; their text has mutiša, mussa, mut libbiša). The part wrote mutiša but mūssa, mūt, and lemma mūtum: inconsistent, and the gloss said "not mūtum death" while keying mūtum. | `say` mussa (×2), mut; lemma mutum; notes follow; [7] says why. New house spelling: mutum, mutiša, mussa, mut. |
| 8 | [12] [13] · `n`, `l`, `i`; gloss `pagrum` | med | pagarša ("her person") is Harper's restoration in brackets; K–U restore NÍG.GA-ša "her property" at the same place (also a restoration). The part presented "her person" as the sense. | Notes say both are restorations; `l`/`i` carry (?); gloss marked UNCERTAIN, "a restoration". |
| 9 | [15] · `n` | low | "the stone preserves all of this law" is not shown by anything checked. | "carries no brackets in Harper's transliteration". |
| 10 | [16] · `n` | low | "when the husband has left her without food": not in the words. | "when there is no food in his house". |
| 11 | [20] · `i` | med | "after he has gone" supplies a verb; the text has warkišu "after him". | "and his wife, behind him, has entered another house". |
| 12 | [23] · `n` | med | "Harper's šugêtum" (Harper prints šu-ge-tim); "usually taken as a kind of priestess" is outside knowledge; ušaršušu analysed as "-šu may belong to the verb". | Reworded; ušaršušu = ušarši + subj. -u + -šu "him" (Š of rašûm, double accusative), ending UNCERTAIN; added that Harper prints one a-na only. |
| 13 | [26] · `say`, `n`; lemma `ṣittum` | med | ṣittum is "remainder"; the word is zittum "share" (published §52–65 has zittum; K–U glossary has zittam kīma aplim ištēn under zittum, ZI read zi). | `say` zittam, lemma zittum (published lemma), note gives Harper's ṣi-it-tam; `__broaden__` zittum added. |
| 14 | [27] · `n` | low | "they (the heirs)": no subject is written. | "(not named)". |
| 15 | [29] · `n` | low | tirḫatum "the gift the groom gives" stated flat. | "(understood as the groom's gift)". |
| 16 | `about` ×3 | low | "half his hair" and "borne children by another man" go beyond the words; pagarša not listed as shaky. | "half (of his hair)"; "in the other house"; pagarša added to the list. |
| 17 | `muttatum` | med | "also the front of the head": unsupported. | Cut; entry says the halved thing is understood in §127. |
| 18 | `itūlum` | med | ittatīlma glossed "she has lain" (§130: the man lies). | "he has lain, and"; notes both spellings i-tu-lim/u-tu-lim. |
| 19 | `ṣabātum-N` | low | iṣṣabit glossed "he was caught" (§131: "she"); doubled sentence. | Fixed. |
| 20 | `kasûm` | low | Lemma stated flat though the unit note says the verb is not certain. | "(probable, not certain)". |
| 21 | `kabālum-D` | med | "root meaning 'to be bound, lame'" unsupported; ukabbilšima has accusative -ši, not -šim. | Root claim cut; "to bind, hold fast, force"; UNCERTAIN kept. |
| 22 | `tarāṣum-N` | low | ittariṣma glossed "has been pointed" (preterite); no uncertainty mark. | "was pointed (at)"; UNCERTAIN. |
| 23 | `šalālum-N` | low | "taken captive" in gloss (units were changed in pass 1). | "carried off (as booty; said of a man taken away)". |
| 24 | `akālum` | low | Garbled example ("ina bītišu akālum, with the construct akālim"). | Example is ša akālim ibašši. |
| 25 | `ḫāwirum` | med | "a variant spelling of the same word as mūtum" unsupported (K–U's glossary has ḫāʾirum "the first husband a girl marries"). | Rewritten, UNCERTAIN, sense at §135 given. |
| 26 | `zêrum` | med | "the subject's number is written plural-form ū": the -ū is the subjunctive -u + -ma, not a plural. | Rewritten (izīr + -u + -ma); "they hated" dropped. |
| 27 | `nabātum-N` | low | Vague; now says what is read from the form. | Rewritten, UNCERTAIN kept. |
| 28 | `munnabtum` | low | "(fem.)" and "N-stem participle" not supported. | "a noun formed from nabātum, understood from the sense". |
| 29 | `šugītum` | med | "a woman of rank in the household, a kind of wife or priestess": unsupported; "Harper reads it šugītum" (he prints šu-ge-tim). | Rewritten, UNCERTAIN, only what the law shows. |
| 30 | `rašûm-Š` | low | -šu glossed "to him" (it is accusative "him"). | Fixed; ending UNCERTAIN. |
| 31 | `šeriqtum` | med | "the gift of the bride's father" not in the text; q vs k not marked. | Meaning rests on §138 (ša ištu bīt abiša ublam); Harper q / later k; UNCERTAIN in form. |
| 32 | `-šim` | med | Entry said ukabbilšima "has the same ending written -ši-ma": it is the accusative -ši (published `-ši`). | Sentence replaced by "not the accusative -ši of ukabbilšima and ubbiršima". |
| 33 | `__broaden__` `abārum` | med | New reading called "D-stem with -šim 'her'": ubbiršima has -ši. | Rebuilt by script from the published base + corrected reading. |
| 34 | `__broaden__` `ṣabātum` | low | New forms iṣṣabtūšu (perfect plural) and iṣṣabat missing from the published entry (pass 1 asked for them). | Added (base + ' · '). |
| 35 | `__broaden__` `zittum` | low | New (see 13). | Added. |
| 36 | `aplum` | low | "a share like an heir's" belongs to the phrase, not the word. | "heir, son as heir"; ab/ap sign noted. |
| 37 | `ḫīrtum` | low | "the spouse chosen in marriage": unsupported. | Cut. |
| 38 | `tirḫatum` | low | "made by the groom" stated flat. | "understood as the groom's gift". |
| 39 | `uzubbûm` | low | "uzubbîm 'of divorce-payment'": the form is the genitive after ana. | "ana uzubbîm 'as a divorce payment'", UNCERTAIN kept. |
| 40 | `ṣittum` key | med | Entry removed (renamed zittum, row 13). | Key removed from gloss.json. |

## Left, with reasons
- [0] ugbabtum (NIN.AN): kept per conventions (always UNCERTAIN, never nadītum). K–U's glossary reads the group NIN.AN as a class of priestess (entum): noted for QUESTIONS.md, not adopted.
- [4] "then the king shall let his servant live too": the l keeps the paratactic two clauses; the i reads the second as the apodosis. Left; grammar permits both.
- [20] ittabit (G perfect) vs [22] innabitu (N): kept; K–U's glossary lists the former under a different stem; the classification stays flagged.
- [25] urabbâ / urtabbû: kept UNCERTAIN as pass 1 left them; K–U print urabbâ and urtabbû.
- [13]/[14] carry no `ln` (pass 1's §133A decision): not changed.
- Per-sign plate re-reads beyond XXI 51–53 not repeated; pass 1's reads stand.

## For QUESTIONS.md
- Published `kânum-D` entry (§42–51) calls uktīn "perfect"; it is the preterite (here and there).
- Published glossaries have no `mutum`; the house spelling is now mutum / mutiša / mussa / mut (short u). Earlier parts, if they use mūtum "husband", should be checked.
- K–U restore "her property" (NÍG.GA-ša) for Harper's pagarša at §133; the note and gloss flag it.
