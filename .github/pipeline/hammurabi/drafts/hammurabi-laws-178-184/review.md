# Review (pass 1) — hammurabi-laws-178-184

Reviewer: strongest model, adversarial. units.json edited in place by script (backup of the draft kept in the scratchpad, not in the repository). 28 units, 282 words, unchanged in count; one sign key added to the shared sign glossary through `signs.py add` (SHIM, 𒋆, see below; `signs.py check`: in sync), none removed. `t` is not a field of units.json (the build makes it). Unit numbers are 0-based positions in `sentences`, with the unit's first stele line. Not run: build, validate, publish.

## Counts
Changes: 33 entries (high 0, medium 14, low 19). Several are one finding applied to several words/fields (eliša ×5 words, ŠIM ×2 glyphs).

## What was checked on the plate (Plates 52–55, PDF 319, 321, 323, 325, zoom 5–10; Harper's List of Signs, PDF 383–409, read for the signs in question)
Method: rows were located by their position against Harper's margin numerals; two-tier rows are one stele line with a sub-row, so rows = stele lines. Each recurring word was compared across its occurrences, and every sign in dispute was compared with the List of Signs (nos. 1–4 AŠ/ZU, 28 RU, 30 NA, 35 NU and NU.PAR, 40 IG, 41 ZI, 47 TIM, 60 ŠUM, 62 UG, 63 AZ, 66 DUB, 84 KU, 95 ŠIM, 99 NI/Ì, 128 GAR, 132 MA, 138 ŠU, 148 UD, 157 KAM, 171 GIG, 172 ŠI/IGI, 175 DI). Not done: a stroke-level identification of every syllabogram of every row; for rows not named below I confirmed sign-group counts and the position of every logogram, and the spellings follow Harper (whose normalised word the plates support wherever I looked) and the sign keys of the published parts for the same spelling, compared by script (every word of the draft whose spelling occurs in an earlier part has the same sign keys there, except the cases listed below).

Line division: checked by script against the packet: 158 lines, every unit's first line and every line's word count agree with Harper's lines (the only apparent mismatches are the two units that run across a column end, XXX 92 → XXXI 1 and XXXI 96 → XXXII 1, and the spaced "IGI. III. GAL" at XXXI 88). `reading` reconstructs from the glyph `tr` for every word; every glyph index is covered by exactly one morph entry; every sign key exists; no ḳ anywhere in units.json.

### The drafter's unresolved plate items, as far as the plate allows
1. **XXXI 48 iš-[ru]-uq-ši-im** — resolved. Row 48 reads LA, IŠ, UG, ŠI, IM; the curl-shaped RU that stands between IŠ and UG at XXXI 65, XXXII 5 and XXX 65 is absent. It is a scribal omission, not damage (the stele is intact there). The glyph RU is kept as [ru] (precedent: bracketed glyphs in 100-111, 127-140), the note now says plainly what the plate shows.
2. **XXX 92 sub-row** — partly resolved. The top tier has four groups (LA, IT, TA, AD); Harper's {b} before nu is right (NU opens the sub-row), and the sub-row has three groups (not four) for nu-ši-im-ma. That fits NU + ŠIM + MA (see 3) at least as well as Harper's four signs. I could not decide it on the plate, so the draft stays Harper's NU IGI IM MA and the note says UNCERTAIN, naming the alternative.
3. **TAG-for-šim (XXX 85, XXXII 19)** — resolved, drafter wrong. The sign after NU at XXX 85 is not the TAG of šum-ma (compare XXX 88, XXXI 20: a fan-like wedge group plus a boxed triangle, List no. 60). It is three-part: a box with strokes and a hook, a ▷, a striped group with hooks, which is Harper's no. 95, value šim. XXXII 19 is the same sign. Glyph changed to a new sign key SHIM (CUNEIFORM SIGN SHIM, 𒋆); tr šim and reading unchanged. The drafter's question 3 is answered; the glossary entry for TAG needs nothing.
4. **PAR in NU.PAR (XXXI 62)** — confirmed: a vertical wedge with a horizontal, standing apart from NU, as in List no. 35 (NU.PAR); BAR is the right key.
5. **NIN (XXX 61, XXXI 20)** — resolved: NIN is a two-part sign (six-sided sign + small box, as described at §127 in 127-140), then AN; SAL (six-sided sign with long tail) is on a sub-tier at XXX 61 and on the line itself at XXXI 20. No sign missing or extra.
6. **ŠU/ZU in DUMU.SAL-šu (XXXI 44, 77, XXXII 3, 16, 20)** — not resolvable: List nos. 4 (ZU) and 138 (ŠU) are both a box with strokes and a vertical, and the plate sign does not decide. ŠU kept (Harper); the form mārtišu (not mārassu) is grammatical either way. Mentioned in the owner questions already; no note change beyond that.
7. **TIM/DIM** — resolved for the sign key: Harper's no. 47 gives the value tim; TIM is right. TIM and DIM are the same character, so the built text is unaffected.
8. **Ù (XXXI 62)**, SAL before AMAR.UTU (XXXI 78, 93), KÁ.DINGIR.RA + KI (XXXI 79), IL + KAM (XXXI 91), ì-kal = NI + KAL (XXXI 13, sub-row), KÙ.BABBAR with no -im (XXXI 14), NI/Ì in Ì.BA, UG in iš-ru-uq / ku-nu-uk-kam (XXXII 5, 8), AK/GA rows: all confirmed as drafted.

## Changes (unit · field · severity · what was wrong · what was done)
| unit | field | severity | what was wrong, what was done |
|---|---|---|---|
| U4 (XXX 82) | words[7].glyphs[5].sign | medium | TAG (šum) used for the -šim sign; plate shows Harper no. 95 ŠIM (three-part sign: boxed wedge, ▷, striped group), a different sign from the TAG of šum-ma; glyph changed to SHIM (added to the sign glossary with signs.py), tr šim kept |
| U25 (XXXII 15) | words[7].glyphs[3].sign | medium | TAG (šum) used for the -šim sign; plate shows Harper no. 95 ŠIM (three-part sign: boxed wedge, ▷, striped group), a different sign from the TAG of šum-ma; glyph changed to SHIM (added to the sign glossary with signs.py), tr šim kept |
| U4 (XXX 82) | n | medium | note followed the sign change |
| U25 (XXXII 15) | n | medium | note followed the sign change |
| U3 (XXX 76) | words[9].say | medium | leqûm has a weak last radical: its present plural is ileqqû (published 153-169, 170-177 write ileqqûma / ileqqû), not ileqqū; the draft’s “plural -ū” long vowel was the strong-verb pattern |
| U3 (XXX 76) | n | medium | note followed the say change |
| U2 (XXX 70) | words[2].say | low | elīša -> eliša: published parts (127-140, 141-152 and the glossary entry for eli) write eliša / elišu, short i; followed, difference noted for QUESTIONS.md |
| U2 (XXX 70) | n | low | note spelling elīša -> eliša (as the say) |
| U6 (XXXI 3) | words[6].say | low | elīša -> eliša: published parts (127-140, 141-152 and the glossary entry for eli) write eliša / elišu, short i; followed, difference noted for QUESTIONS.md |
| U6 (XXXI 3) | n | low | note spelling elīša -> eliša (as the say) |
| U11 (XXXI 29) | words[2].say | low | elīša -> eliša: published parts (127-140, 141-152 and the glossary entry for eli) write eliša / elišu, short i; followed, difference noted for QUESTIONS.md |
| U11 (XXXI 29) | n | low | note spelling elīša -> eliša (as the say) |
| U12 (XXXI 35) | words[7].say | low | elīša -> eliša: published parts (127-140, 141-152 and the glossary entry for eli) write eliša / elišu, short i; followed, difference noted for QUESTIONS.md |
| U12 (XXXI 35) | n | low | note spelling elīša -> eliša (as the say) |
| U22 (XXXI 93) | words[4].say | low | elīša -> eliša: published parts (127-140, 141-152 and the glossary entry for eli) write eliša / elišu, short i; followed, difference noted for QUESTIONS.md |
| U22 (XXXI 93) | n | low | note spelling elīša -> eliša (as the say) |
| U0 (XXX 61) | n | medium | “women dedicated to a god” stated as fact for the whole part (the šugītum of §183–184 is not said to be dedicated); reworded |
| U0 (XXX 61) | n | low | plate result added: NIN is a two-part sign (as at §127), SAL is on a sub-tier; unresolved drafter item settled |
| U0 (XXX 61) | n | low | alternative reading of the SAL before zikrum not mentioned |
| U5 (XXX 88) | n | low | perfect label for uṭṭibbū stated flatly although the form (uṭ-ṭi-ib-bu, doubled b) is not the regular D perfect |
| U5 (XXX 88) | n | medium | drafter’s unresolved XXX 92 item: plate shows 3 groups on the sub-row (ši, im, ma / nu, šim, ma); left as Harper’s four signs but marked uncertain in the note |
| U8 (XXXI 16) | l | medium | “to-another” made šaniam a dative; apālum takes the person paid as its object (tamkāram ippalū, 141-152), so accusative “another” |
| U8 (XXXI 16) | i | medium | “nor shall she use them to pay another” added “use them” and a sense (settling a debt) the grammar does not give; now “pay another (with them) (?)”; “her heirs are her brothers alone” turned the abstract ablūssa into persons, now “her heirship belongs to her brothers alone” |
| U8 (XXXI 16) | n | medium | note followed l/i; label of šaniam fixed, uncertainty widened to the verb form |
| U14 (XXXI 43) | n | low | drafter’s XXXI 48 [ru] item resolved on the plate (no RU: scribal omission, not damage); note said only “no sign” |
| U15 (XXXI 49) | n | low | a-ba = abim is marked UNCERTAIN at §158 and in 170-177; uncertainty dropped here |
| U16 (XXXI 56) | i | low | “after her” added to the second clause; not in warkassa ša aḫḫīšama (l); removed (as in U19) |
| U17 (XXXI 60) | l | low | l said “has-offered-up”, an interpretation; iššīma is našûm “to lift” (note); l made structural |
| U17 (XXXI 60) | n | low | drafter’s PAR/BAR item resolved against Harper’s sign list |
| U21 (XXXI 84) | n | medium | “owes no service on it” and “outright” (about) assumed the exemption attaches to her share; the text says only ilkam ul illak |
| U21 (XXXI 84) | n | medium | invented rationale (her share is free of the service her brothers’ shares carry) removed; nothing in the grammar supports it |
| U23 (XXXII 2) | n | low | šugītum not marked uncertain, as in 127-140 |
| about | about | medium | “Seven laws on women who belong to a god” overstated (šugītum); §180 “a woman of this kind” was vague (it names kallātum or zikrum, not NIN.AN); §182 “outright” and “performs no fief-duty on it” asserted what the text does not say; §183 omitted the sealed tablet; §178 “brothers inherit” and “may let the land” were loose against ileqqûma / inaddinma ana errišim; all re-worded from the units |

## Findings refused or confirmed unchanged (with reason)
- `ŠA.GA` as GAR + GA (tr ŠA): kept, as in 153-169 and 170-177 (Harper's reading); the modern reading of the logogram is a different one, noted by the 170-177 note pattern, not repeated here.
- `A.ŠÀ`, `{giš}KIRI₆`, `DUMU.SAL-šu`, `KÙ.BABBAR`, `{d}AMAR.UTU`, `KÁ.DINGIR.RA{ki}` val slices (Mar/duk, Bāb/ilim, mārt, kasp): kept; the published parts split the vals the same way.
- `ugbabtum` for NIN.AN, `zinništum` for SAL, `aššat` for SAL before Marduk, `kallātim` for {šal}É.GI₄.A, `qadištam`: kept as marked UNCERTAIN; no better reading from permitted sources. The modern class names (nadītum etc.) are not used.
- `ana ilim iššīma` "has dedicated": kept in `i`, UNCERTAIN in the note.
- `ušamziši / uštamziši` (lemma mazûm-Š, UNCERTAIN): the verb remains unidentified; kept; `i` says "has not let her have" with the note flagging it.
- `kīma emūq zittiša` rendered "in proportion to her share" in §178–179 but "in proportion to the means of her father's house" in §184: both are acceptable renderings (emūq "strength" is in `l`), consistent within the house list. Kept.
- `i` of U13 "any claim" (ul ibaqqarūši): the "any" is English idiom for ul + present; l shows "not shall-claim". Kept.
- `i` "and" at the head of U1/U2/U11: asyndeton in Akkadian, English needs it; as in 170-177 review. Kept.
- Plural -ū long in `ibaqqarūši`, `išarraqūšima`, `inaddinūši(ma)`, `ittadnūšimma`, `uṭabbū`, `uṭṭibbū`: strong or II-weak verbs (the plural -ū is long); kept.
- `uṭabbū` (present D of ṭâbum): the form is as Harper writes it; I could not improve it from permitted sources; left.
- `aḫ-hu-ša` (XXXI 41): Harper's plain h read as a print slip for ḫu, as drafted (the ḪU shape matches XXX 80, 88); kept.
- `zittam` for Harper's ṣi-it-tam (XXXI 53): kept as drafted (ZI tr ṣi, as 127-140 / 170-177).
- Remembered English: none found in `i`. The phrases "to whomever it pleases her", "has gone to his fate", "have the use of it as long as she lives", "the fief-duty" are house renderings; "a wife of Marduk", "a sealed tablet", "ration" are built from the signs/grammar in the notes. No verbatim overlap with a recalled modern rendering was recognised.
- `q` not `ḳ`: confirmed in every reader-facing field; Harper's ḳ only in packet.md.

## Observations for the owner / later passes (not changed here; other files)
- Published 26-41 writes il-kam with GA (tr kam) in IL + GA; the plate here (XXXI 91) shows the KAM sign. 153-169 writes ku-nu-uk-kam with IG; XXXII 8 here shows UG. Worth a check of those parts' plates.
- Published parts that write -šim words from Harper's "šim" with TAG (if any) may share the ŠIM mistake; not searched.
- elīša vs eliša: the project uses the short i; the correct OB form may be elīša (long). Followed the published parts; record in QUESTIONS.md.
- Glosser: new lemma list as the drafter gave it, minus nothing; `leqûm` entry should take "ileqqûma (i-li-qu₂-ma)"; the lemma for `šaniam` is šanûm; the sign glossary now has SHIM.

## Still uncertain (for the second pass / the owner)
- XXX 92 sub-row: NU IGI IM MA (Harper) or NU ŠIM MA (three groups on the plate).
- ŠU vs ZU in DUMU.SAL-šu.
- Not every syllabogram of every row identified at stroke level (see "Not done").
- The classes of woman (NIN.AN, SAL, zikrum, kallātim, qadištum, NU.PAR, šugītum), ušamziši, uppal, uṭṭibbū's exact form, ittanaššiši "supporting", ilkam ul illak (reason unstated).

# Review (pass 2) — hammurabi-laws-178-184

Reviewer: strongest model, adversarial. units.json and gloss.json edited in place by script. Not run: build, validate, publish; nothing committed. Counts of changes: high 0, medium 3, low 8.

## Checked
- units.json, every note: grammatical labels (preterite, perfect, present plural, Gtn, D/Š stems, subjunctive -u, construct, accusative/genitive), `l` against the original word by word, `l` against `i`, remembered English in `i`, house renderings (conventions.md through 170-177), q not ḳ (no ḳ in units.json or gloss.json), `say` against `reading`, glyph roles and `val` of every logogram line against the published parts (NIN.AN, SAL, DUMU.SAL-šu, {šal}É.GI₄.A, ŠA.GA É a-ba, IGI.3.GAL, {d}AMAR.UTU, KÁ.DINGIR.RA{ki}, KÙ.BABBAR, DINGIR). Pass 1's edits (ŠIM, ileqqûma, šaniam, U21 note, about) were re-read and stand.
- Plate: only a spot check of Plate 52 (PDF 319, XXX right-hand block, the ŠIM / sub-row lines) at zoom 6–8; I could not map the rows to Harper's numerals reliably enough to add anything to pass 1, so no new stroke-level reading is claimed. Rows not read at stroke level in pass 1 remain so (see its "Not done").
- gloss.json, every entry: each quoted form exists in units.json with that spelling (script: all broaden and new entries); the 24 original `__broaden__` entries were verified by script as the latest published holder's entry WHOLE (latest by `seq` in parts.json) + " · " + new reading, and each new reading was checked against this part's usage.

## Changes (unit/entry · field · severity · what was wrong · what was done)
| unit / entry | field | severity | what was wrong, what was done |
|---|---|---|---|
| U7 (XXXI 9), U16 (XXXI 56), U18 (XXXI 66) | l | medium | `l` said "she-shall-have-the-use-of(-it)", an interpretation; the model (170-177) keeps `l` literal, "she-shall-eat" (ikkal, akālum), the sense going in `i` and the note; changed to "she-shall-eat" |
| zikrum-priestess (lemma in units U0, U9, U14, gloss.json, new-lemmas.json) | lemma | medium | the lemma name asserted "priestess" for a class the notes call unknown; renamed zikrum-class in units, gloss and new-lemmas; entry reworded |
| ugbabtum (__broaden__) | new reading | medium | "read as its own word, not as part of the title" was self-contradictory (it described the SAL as read and as unread); rewritten: NIN.AN read ugbabtum as before, UNCERTAIN; the following SAL is not part of the title and is left unread |
| šarāqum-give | text | low | "with the RU lost on the plate" contradicted pass 1 (RU omitted by the scribe, stele intact); changed to "left out by the scribe" |
| qadištum | text | low | "a class of woman dedicated to a god" stated a function the text does not give; now "the holy one", from qadāšum, class of woman |
| NU.PAR | text | low | "a second class of dedicated woman" likewise; "dedicated" removed |
| ŠE.BA, Ì.BA, SIG.BA | label | low | "Sumerogram, untranslated" contradicted the ration glosses given; now "Sumerogram, Akkadian word not read" |
| apālum (__broaden__) | new reading | low | "present, the vowel pattern unusual" mislabelled uppal; now "taken as a present (a G present would be ippal; the u- is unexplained)", matching the note |
| irrišum (__broaden__, added) | new entry | low | published entry had irrissu only; irrissa (ir-ri-za) "her tenant" added, old entry whole |
| ṭâbum (__broaden__, added) | new entry | low | published entry did not cover stative ṭābu "(that) is pleasing" used six times; added, old entry whole |
| zikrum-class | text | low | "named beside the priestess in §178–180" made exact: beside the ugbabtum (§178–179) and the kallātim (§180) |

## Refused / kept
- `SAL-sign` "read by some later editions as a class of priestess": hedged, UNCERTAIN, and the same flag is in the published §40 note; kept.
- uṭabbū / uṭṭibbū as D-stem present / perfect of ṭâbum: the regular D present would be uṭabbab(ū) and the perfect form is unclear; both are already marked UNCERTAIN in the notes and glossary; kept, no better reading from permitted sources.
- mazûm-Š: verb unidentified, UNCERTAIN in note, glossary and i; kept.
- `kīma` gloss "in proportion to", `-ma` "only", `kunukkum`, `mārtum`, `izuzzum`, `aššatum`, `ilkum`, `mutum`, `kallatum`: new readings true to the units; no change.
- Entries for -ša, -šim, zittum, abum, warkatum, eli, leqûm, alākum cover this part's forms generally; no broadening needed.

## Still open
- Stroke-level reading of every syllabogram (pass 1 and 2); XXX 92 sub-row NU IGI IM MA vs NU ŠIM MA; ŠU vs ZU in DUMU.SAL-šu; the classes of woman; eliša vs elīša (project spelling followed).
- Owner list for conventions.md: `šaniam ul uppal`, `kīma emūq …`, `ana ilim iššīma`, `ilkam ul illak` as in drafter-notes.
