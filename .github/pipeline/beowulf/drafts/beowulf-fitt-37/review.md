# Review of beowulf-fitt-37 (lines 2694–2751), units.json

Method: every unit's `t` (never touched; checked identical to the draft after both passes), `l`, `i`, `n` read against the packet's lines and apparatus, the Klaeber source for every cross-reference, and the published parts (fitt-36, fitt-01, and by grep the root `beowulf-*.json`). All edits made by script; file still valid JSON, same keys, same indent. No modern translation consulted. `gloss.json` did not exist at review time, so no gloss parse could be checked in pass 2.

## Pass 1 — changes

| line | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 2713 | l | high | `l` made `bealonīð(e)` the subject ("bale-malice welled, poison within") while the note, the crux list and the restored dative ending make `attor` the subject and `bealonīðe` a dative ("with baleful malice"). | `l` now "that in his breast, with bale-malice, poison welled within." |
| 2713 | i | high | Same: "baleful malice was welling … venom inside him" has the malice as subject. | "that venom was welling up within his breast with baleful malice." |
| 2694 | l | medium | `l` rendered "I [heard] that … showed", a finite clause with "that", but the construction is accusative + infinitive (`eorl … cȳðan`), as the note itself says. | "I [heard] at the need the people-king’s upright earl show courage …" |
| 2697 | n | medium | Said "three clauses with ‘þæt’" but listed the `þǣr` clause as one, left out the third `þæt` (`þæt ðæt fȳr ongon`), and called the first word of `þæt ðæt` "the first ‘ðæt’" (it is `þæt`, conjunction; `ðæt` is the article). | Rewritten: the `þǣr` clause, then three `þæt` clauses, each named; `þæt` conjunction, `ðæt` article. |
| 2697 | i | medium | "for he struck … so that the sword sank in": `for` makes the striking the reason, but the note and `l` have `þæt hē … slōh` as a result clause. | Recast as a result chain, "so that he struck … and the bright plated sword sank in, and the fire began to die down". |
| 2697 | i | low | "inlaid" for `fǣted`, while `l` and the note say "plated". | "plated". |
| 2706 | n | medium | Note claimed Kemble emended MS `abreoten` to `ābroten` here. The packet's apparatus has no entry at 2707 and Klaeber marks nothing; the claim is unsupported at this line. | Removed; `ābroten` now simply "the participle of ‘ābrēotan’, ‘destroy, kill’". |
| 2706 | n | low | "‘ellen’ is the subject, ‘ferh’ the object" stated as fact; both are neuter, so the forms do not decide. | Says the forms do not decide and that this is a reading. |
| 2711 | n | medium | Said the relative clause `þē him … geworhte` stands "between subject and verb"; in the line it stands after `ongon` and before the infinitives `swelan ond swellan`. | "between ‘ongon’ and its two infinitives". |
| 2720 | l | medium | `l` ran "the famous prince, the thane exceedingly good, his friend-lord, laved…" so that the nominative subject `þegn … till` read as one more object. | Reordered with dashes so the thane is plainly the subject and `winedryhten` the object: "Him then with hands — the sword-gory one, the famous prince — the thane, exceedingly good, laved with water, his friend-lord, battle-sated, and unfastened his helm." |
| 2720 | n | low | `hilde` called a dative; the form is genitive/dative alike and `sæd` can take the genitive. | Says "a genitive or dative form … ‘sæd’ can take the genitive". |
| 2725 | n | medium | `dæghwīla` called a genitive plural object of `gedrogen`; the verb takes the accusative and the form is both. | "an accusative plural, which has the same form as the genitive plural". |
| 2725 | n | low | "Grundtvig’s transcript": the apparatus has `Gru. tr.` = his translation. | "Grundtvig’s translation". |
| 2724 | n | low | Note glossed `wælblēate` "deadly-wretched" while `l` says "slaughter-wretched". | "slaughter-wretched". |
| 2727 | n | low | Note said "exceedingly near"; `l`/`i` and the published rendering of the same words at fitt-34 (2420) are "immeasurably near". | Note now "immeasurably near", with the cross-reference to fate at 2420 (see pass 2 for the line number). |
| 2729 | i | medium | "to a son" for `suna mīnum` (possessive lost); "if it had been granted" (pluperfect) against `l` "if it were so granted" and the present-time wish `Nū … wolde`. | "to my son"; "if it were granted me". |
| 2729 | l | low | `wurde` ("become" in the note) rendered "come". | "should become". |
| 2732 | n | low | Said the fifty-winters count is at 2208; the clause starts at 2208 and the words are on 2209. | "2208–09". |
| 2739 | i | low | "deadly wounds" for `feorhbennum`; house rendering is "mortal wounds" (table, crux list). | "mortal wounds". |
| 2743 | l | low | "Now you quickly go" reads as an indicative; `geong` is imperative. Also "hoary stone" against the published `under hārne stān` (fitt-35 2553) "hoar stone". | "Now go you quickly … under the hoar stone". |
| 2743 | n | low | Matching change: "hoar stone" with reference to the earlier phrase. | Done. |
| 2743 | n | low | "two more verbs: ‘swefeð’ and the participles …" is one verb and two participles. | Corrected. |
| 2747 | i | medium | "the kingdom I have held so long" turns preterite `hēold` into a perfect. | "the kingdom I held so long." |
| 2694 | n | low | "Klaeber prints ‘[gefrægn]’ in brackets because the formula … is usual" gave the wrong cause (the brackets mark Kemble's supplying of it). | Reworded. |

## Pass 2 — changes

Re-read every edited unit, re-checked all line-number cross-references against the Klaeber source, re-ran the `t` and schema check.

| line | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 2727 | n | medium | My pass-1 cross-reference "fate at 2419" was wrong: `wyrd ungemete nēah` is line 2420. | "2420". |
| 2743 | n | medium | My pass-1 cross-reference "the phrase of 2552" was wrong: `under hārne stān` is line 2553. | "2553". |
| 2747 | i | low | "so that after that wealth of treasure I may" ran together; commas set off the adjunct. | Commas added. |

Cross-references verified true: 2745 (Wīglāf named), 2680 (Nægling bursts), 2677–80, 2705, 2675 (`mǣges`), 2462 (Wedra helm of Hrēðel), 2410 (`eorðsele`), 1679 (`enta ǣrgeweorc`), 1661, 1826–27, 1079, 2208–09, 2721 and 2739 (Zupitza's mark), 2694 (`æt þearfe`), apparatus readings (Kemble, Thorpe, Sievers, Holthausen, Grundtvig, Kluge, Rieger, Grein, Scheinert, E./E. Sc., Thorkelin transcripts A/B). The dot-below `ọ` of `morðọrbealo` is the only one in the part, so "first and only" is true and the explanation is present.

## Findings considered and refused

- 2711 l "had earlier wrought": simple preterite + `ǣr` rendered as pluperfect; idiomatic equivalence, note says the same. Kept.
- 2717 l "held" for present subjunctive `healde`: sequence of tense after past `seah`; the note names the subjunctive. Kept.
- 2724 l/i "over his wound" where the OE has no possessive: the wound is Beowulf's, the note says "the wound" and explains `ofer`. Kept.
- 2747 i "eagerly" for `gearo` ("ready"): idiomatic for the readiness to look; the note gives "ready". Kept.
- 2702 l "drew the slaughter-knife" while the note says dative-instrumental `wæll-seaxe`: English cannot show it; the note states the case and the variant `-seax`. Kept.
- 2713 nominative alternative (`bealonīð` as subject): the restored `-e` and the note's choice make the dative the reading; both the apparatus and crux list agree. Kept as dative.
- 2729 i omits `swā` ("so granted"): force carried by the conditional. Kept.
- 2720 i "weary of battle" for `hilde sædne`: `sæd` is "sated, weary"; note gives "sated". Kept.
- 2706 i "the two of them together": renders `bēgen` and `hī`; dropping `þā` is minor. Kept.
- 2732 i "ruled" for `hēold`: published fitt-31 2208 also gives "ruled". Kept.
- 2709 l/i `sylfes dǣdum`, 2736 `bād` + genitive, 2741 `Waldend fīra` "Wielder/Ruler of men" (matches fitt-24 1661), 2738 `searonīðas` "cunning-hatreds" (matches fitt-09/18), 2705 `Wedra helm` (matches fitt-35), 2723 `winedryhten` "friend-lord" (matches fitt-23 `winedrihten`), 2747 `lēodscipe` "people-realm" (matches fitt-31): consistent with published renderings; no change.
- 2715 note "‘sess’ related to ‘session’": cognate at root; harmless. Kept.
- Beyond `units.json` (not edited, reported): `known-forms.json` and the published glossary hold `ābroten — … Kemble's emendation of the manuscript's abreoten`, and `crux-notes.md` repeats it for 2707; true of 1598 perhaps, but the packet gives no such apparatus at 2707. The glosser should not carry it to this line.

## Counts

- Pass 1: 24 changes — high 2, medium 9, low 13.
- Pass 2: 3 changes — high 0, medium 2, low 1.
- Total: 27 changes — high 2, medium 11, low 14.

## Gloss check

Method: every novel entry (70) and every `__broaden__` entry (31) in `gloss.json` read against each line where the form occurs and against the current `units.json` `l`/`n`; keys compared with `novel-forms.json` and `known-forms.json` (all 70 novel keys present and no extras; all broadened keys exist in `known-forms.json`); each broadened entry checked to begin with the old entry whole, then ` · `; all new text scanned for line numbers, "here", and any Kemble claim. Edited by script; file still valid JSON, same shape. No modern translation or glossary consulted. units.json untouched.

### Changes

| form | severity | what was wrong | what was done |
|---|---|---|---|
| dæghwīla | medium | Parsed as genitive plural object of `gedrogen`; the verb takes the accusative and the unit note reads an accusative plural (same form as the genitive plural). | "accusative plural, object of gedrogen, the genitive plural having the same form". |
| gedrogen | medium | "takes the genitive"; the unit note takes `dæghwīla` as its accusative object. | "takes the accusative". |
| gelenge | medium | Parsed as "dative singular neuter, with līce, agreeing with lond" (a leftover of the old shape); in the line `gelenge` is the adjective agreeing with `yrfeweard` and `līce` is its dative complement. Also "of the same kin" not in the note. | Rewritten: adjective, nominative singular masculine, agreeing with yrfeweard, takes the dative (līce gelenge 'belonging to the body'). |
| hilde (broaden) | medium | Known entry gives only accusative/dative; the unit note reads `hilde` with `sædne` as a genitive or dative, so the line had no fitting reading. | Added under `__broaden__`: old entry whole, ` · `, "hild — battle (feminine, genitive or dative singular, with sædne; hilde sædne 'sated with battle')". |
| beaduscearp | low | "agreeing with wæll-seaxe", but `wæll-seaxe` is dative and the adjective is uninflected nominative/accusative (agrees with the relative `þæt`, the neuter seax). | "nominative or accusative singular neuter, uninflected, agreeing with the neuter noun seax". |
| biter | low | Same as beaduscearp. | Same fix. |
| ferh | low | Stated as fact "accusative singular, object of wræc"; the unit note says the forms do not decide subject/object. | "nominative or accusative singular". |
| sædne | low | "with hilde in the dative"; the note says genitive or dative. | "genitive or dative". |
| wælblēate | low | Still carried "deadly-wretched", which review pass 1 removed from the unit. | Dropped; "slaughter-wretched" only. |
| mǣlgesceafta | low | "found only here": pinned to the line (convention), and the rarity claim is the note's wording about the poem, not verifiable for the whole corpus. | "a rare word, the sense a guess". |
| hwēne | low | Asserted "instrumental of hwōn" as fact; nothing in the packet or note supports the derivation. | "cf. hwōn 'little'". |
| geweorc (broaden) | low | New reading said "object of seah"; the object of `seah` here is governed by `on` (the note and the `on` entry say so). | "accusative singular, after on; seah on enta geweorc". |
| handa (broaden) | low | New reading asserted "the old -a form" of the dative plural, unsupported; the old entry already gives handa as a dative singular. | "dative plural, the ending -a standing for -um, though a dative singular would have the same form". |
| hēold (broaden) | low | New reading's meaning list omitted "kept" although its example is "kept my own well". | Meaning now "held, ruled; kept". |

Counts: 14 changes — high 0, medium 4, low 10.

### Findings refused (entries kept)

- ābroten / Kemble: `gloss.json` has no `ābroten` entry and no entry anywhere mentions Kemble's emendation, so nothing carries the unsupported claim to 2706–07. The old `known-forms.json` entry for ābroten is not touched (additions only; the reader's existing entry stands, and the claim is not repeated).
- andlongne, wīshycgende, ðeôn, swegle (incl. "heavenly"), worlde, geweorces: guesses already marked as guesses in the entries and the notes. Kept.
- since (broaden): new reading is nearly a repeat of the old instrumental dative; harmless, not wrong. Kept.
- ðæt / þæt / fāh / fǣted / gebrǣd / gewēold / gecynde / heafolan / mǣges / byrnan / gesæt / on / stānbogan / eorðan / wurde / ðās / mīn / sōhte / unriht / līf / geong / wīglāf / swegle / mæge / lēodscipe / wunde (broaden): each new reading checked against every occurrence in the part (þæt: 2699, 2700, 2701, 2709, 2713, 2714, 2716, 2726, 2747, 2749 covered by the old conjunction/demonstrative plus the new relative at 2704; mīn: 2742 and 2750 covered by the old readings, 2737 by the new); all fit, old entries intact. Kept.
- Novel entries (all others, e.g. attor, bealonīðe, benne, bīo, cēnðu, gefyldan, gelafede, onspēon, sibæðelingas, sigehwīla, sīðast, wund, wītan): case, number, gender, tense, mood, lemma and meaning agree with the unit notes at every occurrence (ongon 2701/2711, wund 2711/2746 both listed). Kept.
