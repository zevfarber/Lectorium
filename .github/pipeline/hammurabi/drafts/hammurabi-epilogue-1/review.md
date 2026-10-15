# Review (pass 1) — hammurabi-epilogue-1 (Col. XL 1 – XLI 74)

Reviewer: adversarial pass 1. Edited `units.json` in place by script (json load/modify/dump, `ensure_ascii=False`, indent 1; round-trip of the untouched file was byte-identical). `python3 ../run3/signs.py check`: in sync (no sign added). Nothing committed, built or published.

## Counts

Change entries (one per field edited): **72** — high 12, medium 28, low 32. Several entries are one finding touching `l`/`i`/note/`say`/lemma together, so the number of distinct findings is smaller (about 12 high: the aḫī idiom [4 entries], the Zarpanitum sign [3], AN = Anum [4], iršiā [3], the xl 17 label/form fixes [3]).

## What I did on the plates

Method: Harper PDF pp. 357–367 at zoom 6–10, crops row by row; counted the sign groups of each ruled line against the glyphs, and compared every distinctive sign across lines (the same sign must look the same wherever it recurs: GIŠ xl 22/44/48 and xli 2; AN-star xl 22/40/63/86; LUGAL xl 77/79/xli 62; URU xl 47/63/79; MU xl 43/61; KI vs NA kites; IN xl 78/79; the GAL pair; MI after SAG). Harper’s List of Signs (PDF p. 409, nos. 177–191) for TUK (no. 187) and zar (no. 183).

**Confirmed on the plate (no change needed):** the 13 linecheck lines — xl 22 (i-na GIŠ.TUKUL da-an-nim: I NA GIŠ TUK, then DA AN NIM on the second row); xl 40 (AN GAL GAL); xl 43 (PA LU, mu ša al, second row li mu um); xl 44 (ša, GIŠ, PA, šu); xl 47 (a na URU ia; URU is the box sign also at xl 63 and xl 79); xl 64 (URU, ša, AN on the first row; ù, AN-determinative, EN, KID on the second row); xl 79 (LUGAL ša IN LUGAL URU: five signs, the IN is the same ≋+triangle as in u-ki-in xl 78; the “+” of Harper’s šar+alim is not a ligature); xl 84 (… AN UD); xl 86 (ša AN ù KI: the AN is the star, the KI the pointed-bottom sign, not the NA kite); xli 7 (ALAN ia, then LUGAL MI ŠA RI IM on the second row); xli 49 (AN AN E RI BU UD); xli 51 (one wide sign, then É SAG ÍL LA); xli 62 (LUGAL ša i na KALAM: five signs). Also xl 83 (U UL I NA: the last sign is the NA kite, so Harper’s “(=ša)” is a real carver’s slip), xl 20–21 (the [pi] of u-[pi]-it-ti and the [u] of [u]-si-am are drawn in outline; the other signs of both lines are drawn whole), xl 26 (five signs i na IGI GAL im), xl 61 (NU TUK NU MU SU: TUK = Harper no. 187 “ku, tuk”, a box with horizontal strokes), xli 60 (the first sign is A, carver’s slip for ṢA as Harper says), xl 8 (u ša AZ bi tu).

**Line division against the plate:** the three spots the transcription doubted are all settled by the ruled lines: xl 65–69 (65 ri-ši-šu, 66 u-ul-lu-u, 67 i-na Esagila, 68 and 69 each one ruled line with a second row), xl 90–94 (five ruled lines; 94 has the second row šu-mi i-na da-mi-iq-tim), xli 25–33 (25 a-na a-wa-at, 26 Marduk be-li-šu, 27 uš-ta-ak-ti + it-ma on a second row, 28, 29, 30, 31 ik-šu-ud, 32, 33 be-li-šu u-ti-ib one line). My reproduction of the validator’s line check (hooks.stele_lines against the units): 168 stele lines, 168 covered, same 30 lines below 0.85 similarity as before (all logograms Harper writes as words, confirmed above). (Those doubts were the transcriber’s, not Harper’s; the notes had attributed them to Harper’s “apparatus” — corrected.)

**Not done:** every syllabogram of all 168 lines was not matched shape by shape; common syllabograms were checked by group count per ruled line and by consistency of recurring signs, and the rows I looked at in detail (xl 1–10, 17–29, 40–49, 59–64, 65–69, 75–94; xli 1–7, 20–36, 48–62) agreed with the drafter’s keys in group count and in every recurring distinctive sign. SIG₄ and ALAN stay TENTATIVE (Harper’s glossary gives no spelling; no Unicode font that matches Harper’s autograph is available here to compare shapes).

## Changes

Unit numbers are 0-based positions in `units.json`, with the stele line.

| unit | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| #0 (xl 1) | n | low | Cross-reference wrong: li-i-a-um is in the litany (the prologue has ri-i-a-um, “shepherd”). | replaced |
| #1 (xl 6) | l | low | `l` reordered the adjectives (“a-firm right-conduct”, “good guidance”); original order is noun + adjective in both phrases. | now: the-land right-conduct firm and guidance good caused-to-take-hold. |
| #1 (xl 6) | i | medium | “and by which he made …” added an instrumental the grammar does not give: ušaṣbitu is a second verb of the same ša-clause with Hammurabi as subject (the object of ukinnūma is the judgments, not of this verb). | now: and caused the land to take hold of a firm right way and good leadership. |
| #1 (xl 6) | n | low | “the apparatus” is the transcriber’s note on Harper’s print, not Harper’s own; wording made accurate. | replaced |
| #1 (xl 6) | n | low | Added Harper’s actual gloss and the litany parallel that supports the rendering and the Š-verb analysis. | replaced |
| #2 (xl 9) | n | low | Cross-reference wrong: the phrase is in the litany, not the prologue. | replaced |
| #3 (xl 11) | n | low | Miscount: the verbs are in the very next unit (xl 15). | replaced |
| #4 (xl 15) | l | high | aḫī was glossed “side … cast aside” as an idiom “of my own”; it is aḫum “arm” + -ī “my”, i.e. the idiom aḫšu iddi “he let his arm drop” (= was idle) already published at §44, §53, §56. | now: not I-was-careless; my-arm not I-let-drop. |
| #4 (xl 15) | i | high | English “I did not cast them aside” is wrong; same idiom as the published aḫšu iddi (“was idle”). | now: I was not careless, and I did not let my arm drop (I was never idle). |
| #4 (xl 15) | n | high | Note rebuilt around the idiom (see `i`). | note rewritten (see units.json) |
| #5 (xl 17) | n | high | Three label/consistency errors fixed in one rewrite: ešteʾi is the G perfect, not a “Gt stem”; upettī → upetti (1st-person preterite of a III-weak D, short, like ubelli); wāštūtim → waštūtim (the note disagreed with `say`). Also: the plate’s first sign is an outline (restoration), so “looks the same as u-še-” did not support Harper; added the litany parallel for nūram and the link to xl 6. | note rewritten (see units.json) |
| #5 (xl 17) | words[5].say | medium | 1st-person preterite of a III-weak D verb is short (compare ubelli, xl 32); final -ī is only for the possessive. | upettī -> upetti |
| #5 (xl 17) | words[2].morph[0].lemma | medium | The form is the perfect of the G stem (house convention: perfects are labelled by their stem, cf. uštabši; Harper I,2), not a Gt stem; plain lemma šeʾûm “to seek” (new key, distinct from šeʾum “grain” and šeʾûm-Gtn). | šeʾûm-Gt -> šeʾûm |
| #6 (xl 22) | n | low | Plate check: second sign = Harper no. 187; first = GIŠ as at xl 44, 48. | replaced |
| #6 (xl 22) | n | low | Zamama is in the litany, not the prologue. | replaced |
| #7 (xl 26) | n | low | Cross-reference wrong (litany). | replaced |
| #7 (xl 26) | n | low | The apparatus is the transcriber’s, not Harper’s; plate confirmed. | replaced |
| #8 (xl 30) | n | low | “to go out (of a fire)” was not in Harper and is not needed; his gloss given. | replaced |
| #8 (xl 30) | n | low | Cross-reference wrong: uṭīb is the litany’s verb; the prologue has the infinitive ṭubbim. | replaced |
| #8 (xl 30) | n | low | Tidied the sentence after the cross-reference fix. | replaced |
| #11 (xl 42) | i | medium | Previous unit’s `i` already ends “…called me, and”, so “and I, the shepherd who keeps them safe” doubled the “and”; “keeps them safe” added an object (mušallimum is a bare noun/participle); the nominal sentence (anākuma) made explicit with “I am”. | now: I am the shepherd, the protector, whose scepter is straight; |
| #14 (xl 53) | n | low | Said what Harper’s entry actually lists. | replaced |
| #15 (xl 57) | n | medium | Label: Harper’s III,2 is the Š perfect (uš-ta-pṣir); house convention labels perfects by their stem (uštabši = bašûm-Š). | replaced |
| #15 (xl 57) | words[2].morph[0].lemma | medium | Same. | paṣārum-Št -> paṣārum-Š |
| #17 (xl 63) | n | high | `say` “Anim” is a genitive; AN is a subject of ullû (nominative Anum, as the prologue spells it). Note also misreported Harper (“his glossary refers it to Anu”): his ilu entry lists xl 64; his Anu entry does not. | replaced |
| #17 (xl 63) | words[4].say | high | Genitive in a nominative slot; see note. | Anim -> Anum |
| #17 (xl 63) | words[4].glyphs[0].val | high | Same. | Anim -> Anum |
| #17 (xl 63) | n | medium | “Harper’s division is provisional / needs a human check” was the transcriber’s doubt about the print, misattributed to Harper; checked on the plate and confirmed. | replaced |
| #18 (xl 68) | n | low | “3rd person plural” is the wrong label for -ā (dual / fem. pl.); added the prologue parallel and the plate confirmation of the line division. | replaced |
| #22 (xl 84) | n | low | The two forms Harper lists are in the prologue and the litany respectively. | replaced |
| #23 (xl 89) | n | high | Form misidentified: ir-ši-a cannot be iršiam (“-am” is not written); it is 3rd fem. plural iršiā, with uṣurātūa “my designs” as plural subject. | replaced |
| #23 (xl 89) | n | low | Follows the change above. | replaced |
| #23 (xl 89) | words[7].say | high | Same. | iršiam -> iršiā |
| #24 (xl 93) | n | medium | The doubt was the transcriber’s; plate shows one ruled line with a sub-row, so xl 90–94 are five lines as divided. | replaced |
| #29 (xli 12) | n | medium | “li + ikallim” is not a D form (D preterite is ukallim); the precative of the D is li-kallim. | replaced |
| #29 (xli 12) | n | low | Obscure closing sentence replaced. | replaced |
| #31 (xli 20) | l | medium | `l` carried an invented “(let-him-say)”; -mi is the quotative particle only. | now: “Hammurabi”-(quoted) the-lord who like a-father begetting to the-people is, |
| #31 (xli 20) | i | medium | `i` inserted “(let him say)” in the wrong place; the verb “let him say” is liqbīma at xli 40, after the quotation. The quotation now opens here and closes at xli 37 (as the note says). | now: “Hammurabi is a lord who is like a father, a begetter, to the people, |
| #31 (xli 20) | n | low | Pointed to where the verb actually is. | replaced |
| #32 (xli 25) | n | medium | Label (III,2 = Š perfect, cf. uštabši) and spelling (his entry is katatu, written with t as the lemma is). | replaced |
| #32 (xli 25) | n | medium | Transcriber’s doubt misattributed to Harper; plate confirms the division. | replaced |
| #32 (xli 25) | words[4].morph[0].lemma | medium | Label, see note. | katātum-Št -> katātum-Š |
| #34 (xli 32) | n | low | Spelling as printed in the litany unit. | replaced |
| #34 (xli 32) | n | low | Plate confirmed; not Harper’s own doubt. | replaced |
| #35 (xli 34) | words[7].say | low | `say` disagreed with the note (išīm) and with xl 27 (išīmam). | išim -> išīm |
| #35 (xli 34) | n | low | Aligned with the corrected `say`. | replaced |
| #36 (xli 37) | n | medium | `say`/note “ušteššir” has a doubled š the spelling uš-te-še-ir does not show (uš-te-še-ir = uštēšir); label made the house one (perfect). | replaced |
| #36 (xli 37) | words[2].say | medium | Same. | ušteššir -> uštēšir |
| #37 (xli 39) | l | medium | `l` showed the noun reading (“the-pronouncement(?)”) while `i` and the note chose the adverb reading; made `l` agree with `i`. | now: firmly(?) let-him-say-and, |
| #37 (xli 39) | i | medium | “solemnly” had no basis; “firmly” follows the adverb reading of danītam from dannum that the note says was chosen. | now: let him say it firmly (?), and |
| #37 (xli 39) | n | low | Note aligned with `l`/`i`. | replaced |
| #38 (xli 41) | n | high | ZA + AR was wrong: the plate (xl 43 and xli 56) shows one sign, Harper’s no. 183 “zar”; two glyphs misrepresent the name’s signs. | replaced |
| #38 (xli 41) | n | low | Said which stem/mood. | replaced |
| #38 (xli 41) | words[4] (Zarpanitum) | high | Two glyphs ZA + AR on the plate there is ONE sign (Harper no. 183 zar): xl 43 / xli 56. | glyphs ZA,AR,PA,NI,TUM -> ZA(tr Zar),PA,NI,TUM; reading {d}Za-ar-… -> {d}Zar-… |
| #38 (xli 41) | i | low | Doubled “and” (the previous `i` already ends “, and”). | removed leading “and” |
| #39 (xli 48) | l | medium | `l` “the-utterances(?)” gave a meaning that is not Harper’s and that the note admits is a guess. | now: the-protective-spirit, the-guardian-spirit, the-gods entering Esagila, the-brickwork of-Esagila, the-igirrû(?) daily, |
| #39 (xli 48) | i | medium | “its utterances” was the drafter’s own recollection of a usual sense, contrary to the sole-source rule; Harper’s gloss given, the word left unresolved. | now: May the protective spirit, the guardian spirit, the gods who enter Esagila, the brickwork of Esagila, and the igirrê (Harper: “dreams, plans”; unclear), each day |
| #39 (xli 48) | n | low | Plate: one wide sign, as wide as É. | replaced |
| #39 (xli 48) | n | medium | Remembered sense removed. | replaced |
| #40 (xli 54) | i | medium | “speak well of me” added a verb (qabûm) and an object (“me”) that the grammar does not contain: lidammiqū is D of damāqum with no object. | now: may they show favor before Marduk my lord and Zarpanitum my lady. |
| #40 (xli 54) | n | medium | “li + idammiqū” is not a D form (D has u-); label corrected. | replaced |
| #40 (xli 54) | n | medium | Note aligned with new `i`. | replaced |
| #40 (xli 54) | words[4] (Zarpanitum) | high | Two glyphs ZA + AR on the plate there is ONE sign (Harper no. 183 zar): xl 43 / xli 56. | glyphs ZA,AR,PA,NI,TUM -> ZA(tr Zar),PA,NI,TUM; reading {d}Za-ar-… -> {d}Zar-… |
| #41 (xli 59) | l | low | `l` “of-the-offspring of-days” followed the drafter’s gloss of ṣātum, not Harper’s. | now: for the-after, the-future of-days, for whenever: |
| #41 (xli 59) | n | medium | “offspring, what comes after” was not in Harper; his gloss is “future time, eternity”. | replaced |
| #41 (xli 59) | n | low | Long ā unsupported and collides with mātum “land”. | replaced |
| #41 (xli 59) | words[5].say | low | Same. | mātīma -> matīma |
| #41 (xli 59) | words[5].morph[0].lemma | low | Same. | mātīma -> matīma |
| #43 (xli 68) | i | medium | `i` “the judgments of the land that I gave, the decisions of the land that I made” has a doubled “of the land” pairing I recognise from older printed translations (verbatim-overlap flag), and “made” for aprusu (“I decided”) is off; rebuilt from the grammar. | now: and let him not change the verdicts that I gave for the land or the rulings that I decided for it. |
| #44 (xli 73) | i | low | “wipe out” vs “efface” in xl 89 / this note: one verb, one rendering. | now: Let him not efface my designs. |
| about | about | medium | “Harper’s division is provisional” was the transcriber’s doubt, wrongly attributed, and the plate settles it; the Zarpanitum doubt is resolved on the plate. | rewritten |
| about | about | medium | Follows the new `i` of xli 54. | speak well of him -> show favor |

## Findings refused or left as drafted (with the reason)

- **#0 ukīnūma / `say`** (u-ki-in-nu-ma could be ukinnūma, with the D-stem’s doubled n): left. The note analyses it as ukīn + subjunctive -u, the same normalization the part uses at xl 78 (u-ki-in = ukīn); both are defensible and the spelling cannot settle it.
- **#14 attabbalšināti “Gt (Harper I,2)”**: left. Harper’s I,2 is ambiguous between a perfect and a Gt present; the form attabbal (doubled b, present-tense shape) is more plausibly Gt/present than perfect, and the English “I carried them” does not depend on it. Lemma tabālum kept unlabelled as in the published parts.
- **#28 lištassīma “Gt”**: left. As a precative (li-) it can only be built on a preterite, and the Gt preterite is the shape written; the note’s analysis stands.
- **#14 aḫḫiša**: left untranslated and flagged. Harper’s glossary lists it with aḫḫūša/aḫḫīša “his/her brothers”, which does not fit; nothing in the grammar or Harper offers a better reading, and I will not guess.
- **#5 ūsam / nūram (xl 21)**: kept Harper’s reading with Winckler’s as the alternative. The plate cannot decide: the first sign is an outline (restoration either way) and the next two signs are whole SI and AM as Harper has them. The litany parallel (mušēṣi nūrim) is now cited so the reader can weigh it. See open questions.
- **#21 šāninam ul īša (xl 82–83)**: left as drafted. The plate confirms Harper’s form (…UL I NA, with the NA a real carver’s slip for ŠA); “īša” stays unexplained (one would expect īšu) and the English “in power I have no rival” is flagged. I could not improve on it from the grammar.
- **#21 LUGAL.URU `say` šar ālim with “city-kings” in `i`**: left; it is the litany’s published treatment (LUGAL.URU-lim, `say` šar ālim, `i` “city-kings”) and is marked uncertain there.
- **#6 GIŠ.TUKUL tr TUKUL on the TUK sign**: left (TENTATIVE, now with the Harper no. 187 identification in the note). The Sumerogram’s second sign could be a different TUKUL sign that looks alike; nothing in Harper settles it.
- **#20/#27 ALAN, #39 SIG₄**: left TENTATIVE (identified by shape/sense only; Harper’s glossary gives no spelling for ṣalmu “statue” at xl 76 and xli 6 and none for libittu). No sign added.
- **#24 lemma damqum for damiqtim**: left; it is the published lemma for the same form, and the note says it is the noun use.
- **#19 / #43 purussê as “decisions”, dīn as “case(s)/judgments”**: kept in #19 (consistent with the part’s “just decisions”, xl 1). #43 was reworded only for the overlap flag, not for sense.
- **#23 mušazziqam / #44 ušazziq “efface”**: kept Harper’s gloss (nazāqu III “to cut off, efface, destroy”), as the note says; Harper’s own first entries for the root (nazāqu I “cut off, separate”) show the sense is not firm, so the English remains uncertain, which the note says.
- **#39 ilāni ērībūt Esagila**: left with its UNCERTAIN flag (ērībūt a noun or a participle).
- **#10, #20 p flags and ln**: left: `p: true` falls on the new paragraphs of sense (xl 1, 9, 40, 70; xli 3, 59) and `ln` = the stele line, as the epilogue convention says.
- **“wide of eye” for IGI.GÁL (xl 26 note)**: left; it paraphrases Harper’s “broad of vision”.
- **Dropped aḫḫiša from `i`**: left, as the note says why.

## Disclosure (sole-source rule)

While probing the PDF text layer at the start I printed the first 200 characters of four pages; one of them (PDF p. 116) showed the opening of Harper’s own English translation of §281 (a different part). It was not used. Harper’s glossary (PDF pp. 168–212) was used for the entries named in the notes. No modern translation was opened; where I recognised a possible overlap (xli 68 “the judgments of the land … the decisions of the land”), the English was rebuilt from the grammar (see #43). I also recognised no other distinctive rendering in the part’s `i`.

## House renderings worth recording in conventions.md

- `aḫī ul addi` “I did not let my arm drop (I was never idle)” — the same idiom as `aḫšu iddi` (§44, §53, §56); aḫī = aḫum “arm” + -ī.
- AN alone as subject = `Anum` (prologue, litany, xl 64): never a genitive Anim; Harper’s ilim noted.
- `rēʾûm mušallimum` “the shepherd, the protector”; `išīm` “he decreed” (šâmum, “to fix”); `uṭīb` “has gladdened / made good”, šīr mātim uṭīb “made the land prosper” (as the litany’s šīr nišī uṭīb).
- Perfects of Š are labelled with their stem (Harper’s III,2 = Š perfect): `uštapṣiršināti`, `uštaktitma`, `uštēšir` (not Št); ešteʾi = G perfect of šeʾûm (lemma `šeʾûm`).
- `ay` before a preterite = “may (it) not” (xl 89, xli 68, 73); 3rd fem. plural -ā in `iršiā`.
- `ṣalmīya ALAN-ia` “my statue”; `šar mīšarim` “King of Justice”; `LUGAL.URU` šar ālim “city-kings” (as the litany).
- Zarpanitum is written with the one sign Harper’s List no. 183 (zar): shown as ZA with tr Zar (TENTATIVE), reading `{d}Zar-pa-ni-tum`.
- Quotation opened by -mi and closed by the last clause (xli 20–37): `i` carries only the quotation marks; the introductory verb is liqbīma, xli 40.
- `lidammiqū` “may they show favor”; `danītam` “firmly (?)”; `ṣāt ūmi` “the future of days” (Harper’s satu); `matīma` “whenever”.
- `GIŠ.TUKUL` kakkum “weapon”: GIŠ (wide, two long bars) + TUK (Harper 187). `igirrê` left with Harper’s gloss.

## Open questions for QUESTIONS.md

1. xl 21 ūsam (Harper) or nūram (Winckler): the first two signs cannot be told apart on the plate (outline + SI-like); the litany’s mušēṣi nūrim favours nūram. Kept ūsam, flagged.
2. xl 82–83 `līʾūti šāninam ul īša`: form (īša for īšu?) and subject unexplained.
3. xl 54 `aḫḫiša`: no reading found.
4. xli 48 `igirrê`: Harper “dreams, plans”; the line (five powers speaking before Marduk) makes it unclear; and `ērībūt`.
5. xli 39 `danītam`: noun (Harper “inscription, code”) or adverb; kept “firmly (?)”.
6. Zarpanitum sign: Harper no. 183 “zar” has no matching entry in our sign list; a ZAR sign (or a ZA+AR ligature) may need adding by someone who can compare a font.
7. SIG₄ (xli 51) and ALAN (xl 76, xli 7) are shape/sense matches only; GIŠ.TUKUL’s second sign = Harper 187 (TUK) unconfirmed as TUKUL.
8. `šâmum` collision in the glossary: gap-a’s entry for the key `šâmum` says “to buy” while laws-1-10 has `šâmum-buy` “a homonym of šâmum ‘to fix destinies’”; this part uses `šâmum` for “to fix, decree” (xl 27, xli 34), so the old gap-a gloss should be moved to `šâmum-buy`.
9. “Harper’s apparatus” in earlier notes: the doubts about line division (xl 65–69, 90–94, xli 25–33) came from the transcription of the print, not from Harper; no earlier part may have the same wording — worth a grep.

## Lemmas used that are not in earlier parts’ glossaries (54; for the glosser)

Keys as in `units.json` (the forms met in brackets):


`kīnum` (kīnam), `rīdum` (rīdam), `ṣabātum-Š` (ušaṣbitu), `rēʾûtum` (rēʾūssina), `-šina` (rēʾūssina), `šulmum` (šulmim), `šeʾûm` (ešteʾišināšim), `-šināšim` (ešteʾišināšim/ušēṣišināšim), `waštum` (waštūtim), `petûm-D` (upetti), `kakkum` (kakkim), `talāmum-Š` (ušatlimūnim), `līʾūtum` (līʾūti/līʾūtim), `elîš` (elîš), `šaplîš` (šaplîš), `balûm-D` (ubelli), `aburrum` (aburrī), `rabāṣum-Š` (ušarbiṣ), `galātum-D` (mugallitam), `-šināti` (attabbalšināti/ušaršišināti/uštapṣiršināti), `ṣillum` (ṣillī), `tarāṣum` (tariṣ), `utlum` (utlīya), `nemēqum` (nemēqīya), `paṣārum-Š` (uštapṣiršināti), `ekûtum` (ekûtam), `elûm-D` (ullû), `dīānum` (dīānim), `šūqurum` (šūqurātim), `narûm` (narûya), `ṣalmum` (ṣalmīya), `watārum-Š` (šūturu), `našqum` (našqā), `šanānum` (šāninam), `kibītum` (kibīt), `wapûm-Št` (lištēpi), `nazāqum-Š` (mušazziqam/ušazziq), `ay` (ay), `zakārum-N` (lizzakir), `šaṭrum` (šaṭram), `šasûm-Gt` (lištassīma), `napāšum-D` (linappišma), `katātum-Š` (uštaktitma), `irnittum` (irnitti), `danītum` (danītam), `Zarpanītum` (Zarpanītum), `karābum` (likrubam), `šēdum` (šēdum), `libittum` (libit), `egirrûm` (igirrê), `ūmišam` (ūmišam), `damāqum-D` (lidammiqū), `ṣātum` (ṣāt), `matīma` (matīma).

Notes for the glosser: `šeʾûm` “to seek” (ešteʾi, G perfect; distinct from `šeʾum` “grain” and `šeʾûm-Gtn`); `paṣārum-Š`, `katātum-Š` are Š perfects (Harper III,2); `Zarpanītum` ({d}Zar-pa-ni-tum, one sign); `danītum` carries Harper’s gloss “inscription, code” with the adverbial use as the reading chosen; `egirrûm` Harper “dreams, plans”, unclear here; `ṣātum` Harper’s satu “future time, eternity”; `matīma` (not mātīma); `aḫum` (arm, side) is an existing key used for aḫī at xl 15 — add the form aḫī to it.

## Pass 2 — gloss.json (54 new entries + 23 `__broaden__`)

Checks: every morph lemma in `units.json` equals a gloss key or an earlier part's key (none missing, none unused, no new key clashes with an earlier one); every `__broaden__` entry must be the latest published holder's entry whole + ' · ' + the new reading; each new entry read against the form, stem name and the final `l`/`i`.

| entry | severity | what was wrong | what was done |
|---|---|---|---|
| `__broaden__` ina, -šu, -ma, nadûm, alākum, išûm, rašûm, bašûm, qabûm, lā (10 entries) | high | Built on an older holder's entry, so the latest published holder's text (e.g. laws-278-282's ina/-ma/lā, laws-258-277's bašûm, laws-241-257's išûm) would have been dropped when merged. | Each rebuilt as the latest holder's entry whole + ' · ' + the new reading; the other 13 already complied. All 23 now verified by script. |
| `__broaden__` ana | low | “ana mātīma” (unit `say` is matīma). | → “ana matīma”. |
| `__broaden__` šâmum | medium | Reader-facing “FLAG: … should be separated” text inside a gloss. | Removed; the collision stays in QUESTIONS (below). |
| `balûm-D` | low | “to go out (of a fire)”, not in Harper (removed from the note in pass 1); tense unanalysed. | Harper's I “to destroy”, II “to extinguish”; “preterite, 1st person”. |
| `napāšum-D` | medium | “li- + inappiš”: not a D form. | “li- + nappiš + -ma (precative of the D)”. |

Refused: `šasûm-Gt` / `wapûm-Št` / `nazāqum-Š` kept as units have them; `tarāṣum` “label not settled” kept (honest); `ṣātum`, `egirrûm`, `danītum`, `Zarpanītum` entries match the pass-1 units. No invented modern forms found in the other 49 entries; stem names agree with the lemma suffixes (Š perfects `paṣārum-Š`, `katātum-Š`; G perfect `šeʾûm`).

Pass 2 counts: high 1 (the broaden entries), medium 2, low 2.

Build and validate (from the work folder): `r3.py build` → BUILT hammurabi-epilogue-1: 45 units; `r3.py validate` → one WARN (the 13 linecheck lines, all confirmed on the plate in pass 1) and **PASS**. `signs.py check`: in sync.
