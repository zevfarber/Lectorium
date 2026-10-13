# Review — hammurabi-gap-b

## Pass 1

Method: every unit read against Cuq 1918 (the page images of pp. 8–10 and 87–88: sign letters, brackets, hyphenation,
italics) and the established lines; written lines counted against the established lines of each ref (14 units: all equal;
`nl` marks fall on the first word of each line); `reading` rebuilt from glyph `tr` (all match, after row 1); every sign
key exists in signs-cuneiform.json; morph indices in range; q not ḳ (none); `python3 ../run3/signs.py check`: in sync.
Poebel's Plate XL was NOT read sign by sign (same limit as the drafter); the about and the notes say so and still do.
Disclosure: while checking the transliteration I saw Cuq's French column on the same pages (and the djvu text). I did
not use it for any wording; the findings below rest on grammar and on the printed signs.

### Changes
| # | unit · field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 1 | 9 (§97) · say, morph, l, i, n (u-pa-aṣ) | high | `uppaš` / lemma `epēšum-D` is not what the glyphs spell (u-pa-aṣ) but the Assyrian variant imported; "shall not refuse" is Cuq's gloss remembered (the drafter says it saw it) | say `upaṣ`, lemma `upaṣ`; l and i leave the verb untranslated ("not u-pa-aṣ (a verb I cannot read); he shall receive"); note says the grammar does not give the verb and that DT 81's up-pa-aš-ma may or may not be the same word |
| 2 | 3 (§92) · glyph, reading, say, morph, n | high | `[ṣibat]-za`: Cuq's page prints `[ṣibat]zu` (checked on the page image); the established line has `za` (transcription slip). `za`/"-ša" is also the wrong suffix | glyph ZA → ZU, `zu`, say `…ssu`, morph `-šu`; note says why and cites MÁŠ-zu (gap-a §66); the established file is pinned and untouched (QUESTIONS) |
| 3 | 2 (§91) · i | high | i contained restored text not on the tablet ("a shekel of silver … one-sixth and 6 grains", "[GUR(?)]") and "above" (not in the text); l had none of it | i rebuilt from l: the lost verb and lines stay gaps; "increases the interest" kept (uwattir is visible) |
| 4 | 2 · l, n | medium | l rendered `ik(?)-[kir-ma]` as a plain "refuses(?)-and" although only ik survives | l `ik(?)-[…]`, i `[refuses (?)]`, note says the verb is the editors' restoration and a guess |
| 5 | 2 · n | medium | "lines 9–11 repeat the rate of §90" stated as fact; those lines are restored | "if the editors' restorations are right …", not adopted |
| 6 | 2 · l | low | final `he-forfeits` wholly restored (only i- survives) | `he-[forfeits]` |
| 7 | 2 · say `šarri` | low | house form is šarrim (ṣimdat šarrim, laws-42-51) | `šarrim` in say and note |
| 8 | 6 (§94) · lemma utâr | medium | `u-ta-a-ar` has the u- prefix: D-stem, not G; lemma `târum` | `târum-D` (as turrim); note says D durative |
| 9 | 6 · l, i, n (uštaḫri-) | high | "he-had-it-entered(?)" is a sense from the law's summary, not from ḫerûm "dig/scratch" | l `he-had-dug(?)[-it]`, i `had (it) scratched out (?)`, note: plain sense "dig", the rest a guess |
| 10 | 6 · l, i, n (e-li-am) | medium | l "a-supplementary tablet": eliam is "upper", "supplementary" is the editors' gloss | l "an-upper tablet", i keeps "supplementary (?)", note says so |
| 11 | 6 · l, i, n (ma-la il) | medium | "as-much-as he-took(?)" reads the restored [il-ku-u]; only `il` is visible | l `il(?)[…]`, i `[he took (?)]`, note corrected |
| 12 | 6 · say `qaqqadi`, n "forbidden" | low | mimation dropped (house keeps it); "forbidden" is not in the text | `qaqqadim`; "that is, compound interest" |
| 13 | 0 (§89) · glyph E → TE | medium | `[ki-ma i-t]e(?)-šu`: the bracket falls inside the sign TE; gap-a reads `[iš-t]u` as TU; this word alone was cut to E | glyph TE, `te-šu`, say `tešu`, l, note |
| 14 | 12 (§99) · DINGIR.ME.EŠ | medium | the editors print plain `ilāni` = a logogram whose signs are unrecorded; the drafter chose DINGIR.MEŠ, but the stele (litany) writes DINGIR.DINGIR | DINGIR.DINGIR (val ilā + ni, as the litany); note says why |
| 15 | 12 · lemma `bašûm` | medium | ib-ba-šu-u is the N-stem; gap-a uses `bašûm-N` | `bašûm-N`; note names the N-stem |
| 16 | 12 · say `izuzzu` | low | 3rd plural: izuzzū (the glossary's own form) | `izuzzū`, note "3rd plural" |
| 17 | 12 · n | low | "(so under oath)" asserted; `tap-pu-tim` unflagged though Cuq prints one normalized word `tappûtim` | "perhaps meaning under oath"; TAB-BU-TIM flagged as a placeholder |
| 18 | 11 (§98) · n | low | iddâk not labelled N-stem | "the N-stem, passive, of dâkum" |
| 19 | 10 (§98) · n | low | two lost laws (Cuq's 98–99) under one number, not said | note says §98 stands for both |
| 20 | 13 (§100) · l, n | medium | "[selling] [and] receiving": `receiving` unbracketed though only ḫa-ri survives; "where" (ašar) restored but unbracketed; note "they went (where?)" | l `[selling(?)] [and] [receiving(?)]`, `[where] he-went`; note "(where) he went, he has seen" |
| 21 | 13 · n | medium | šamallim/šamallû: the note said the tablet writes a logogram; Cuq prints `šamalli-im`, `šamallû` (logogram + complement); `ḫarranim` is printed unhyphenated (logogram KASKAL?) while the established line and this unit give ḫar-ra-nim | both flagged in the note as unchecked/placeholders (glyphs left: no plate to decide) |
| 22 | 9 · l, i (bi-ša-am-ma) | medium | l "[…]-and he-has goods": the word `goods` is the restoration; `-ma` mis-glued | l `[goods]-am-ma he-has`, i `[goods]` |
| 23 | 9 · n | medium | Cuq's page prints `i-ma ḫa-ar` (two signs); the established line has `i-ma-ḫar` | noted; glyphs follow the established line (QUESTIONS) |
| 24 | 9 · i | low | "in the way that he brings it" (kīma + subjunctive is "as") | "as he brings (it)" |
| 25 | 3 · l, i | medium | l bracketed "[its-inter]est" (visible part is "its"); i "has given" unbracketed though the verb is lost | l `[interest]-its`, i `[has given]`, `its [interest]` |
| 26 | 3 · n | low | "the last words are the verb bašûm" (ib-ba is restored) | "probably", restoration named |
| 27 | 7 (§95) · i, n | medium | i invented "with a" before the ni-im fragment; note stated the missing "large measure" as fact; "Sumerogram for a measure of grain" | i drops "with a"; "(it seems) … the second half is lost"; "evidently names a measure" |
| 28 | 8 (§96) · l, i, n | medium | note "a loan made in the wrong circumstances" is not in the signs; l "for-the-loan" and "that … he-gave" overstate what is visible | note "under a condition now lost"; l `for-ḫu[…]`, `[that he-]gave`; i `[as a loan]` |
| 29 | all · reading, l, i, n (ḪAR-RA, GUR-É) | low | Sumerograms written with a hyphen; the convention is dots (`ḪAR.RA`, `GUR.É`) | changed; the editors' print kept in the note where it is cited |
| 30 | top · about | medium | "school copy of the whole code" (the packet says only a school copy); §94, §95, §96 summaries state guessed senses as findings | "of the code"; summaries softened as in rows 9, 27, 28 |

### Findings checked and kept
- **IG for uq** (bu-tu-uq-qa-am), although Cuq prints `ug`: the published parts (laws-1-10) use IG for uk/uq throughout. Kept; QUESTIONS.
- **ZIB sign** (𒍦, `signs.py check` in sync): the sign's own values line says "§91, §94" but ṣib-tam is only in §91 (§94 has ṣi-ba-tim). Cosmetic; the entry itself is the drafter's unchecked guess (printed `ṣib`, a single sign). Left as is; QUESTIONS.
- **KÙ.BABBAR-a-am, ŠE-a-am-ma … for Cuq's `kaspa-am`, `še-a-am-ma`**: the "keep every printed sign after the logogram" rule is disclosed in every note; kept.
- **ḪAR.RA = ḫubullum** (§95 spells ḫu-bu-ul-li-im then ḪAR-RA for the same loan): sound, flagged as from context; kept.
- **IGI.6.GAL = šuššum, "one-sixth and 6 še"**: the note's arithmetic (36 še of 180 = a fifth) is right; kept.
- **GIŠ.BAR say `(GIŠ.BAR)`**: unreadable by design, unknown value; kept (audio will spell it).
- **NER = KISH read ner (Harper)**, UD NER la: signs as printed; sense openly unknown; kept.
- **uṣṣap(?)** from eṣēpum "to add": hedged in l/i/n; the published glossary has eṣēpum "arrange" — glosser must broaden.
- **Partly broken syllables read as visible** (u[r], t]e, š[a, ḫ]a, i[l]): consistent with gap-a; the TE case now follows the same rule (row 13).
- **ln / p**: first unit of each law only; the lost units (92 tail, 93, 98) behave as the packet's.
- **Unit 5 `ln 93`** on a wholly lost law: kept as the packet numbers it.

### Refused
- Rewriting every "restored word" bracket in i to match l: only where the i said more than l (rows 3, 22, 25, 28); other gaps already agree.
- Changing šamallûm / ḫarranim / tappûtim glyphs to logograms: no sign list or plate is available to decide; flagged instead (rows 17, 21).
- Changing `bu-tu-uq-qa` IG to UG on Cuq's `ug`: contradicts published house practice (see above).
- Removing the "(?)" from `ṭi`, `ma`, `ni`, `ik`: reading dropped them from `reading`, the notes carry the doubt; the build has no field for it.

## Pass 2
(after gloss.json; method: units.json re-parsed and re-checked after the pass-1 edits; every gloss.json entry read against the unit that uses it and, for each broadened entry, against the entry the build will merge over; no translation opened or recalled)

### Changes
| # | where | severity | what was wrong | what was done |
|---|---|---|---|---|
| 1 | units 1, 2, 3, 9, 6 · glyph tr, reading (i-li-ik-ki, il-ki, il-te-ki-ma, il-ki-e-ma, il-ku-u₂) | high | the root of leqûm is q-; the house rule writes KI = qi₂, KU = qu₂, IG = iq in these forms (published: i-li-qi₂, il-qi₂-ma, il-qu₂-u). The draft kept Cuq's k-spellings, which put a k root into every reader-facing field | i-li-iq-qi₂, il-qi₂, il-te-qi₂-ma, il-qi₂-e-ma, il-qu₂-u₂ in glyph tr and reading; notes that cite the forms follow. (ik of nakārum and illiku of alākum are true k and stay) |
| 2 | 3 · say il-te-qi₂-ma | medium | ilteqīma: the perfect is ilteqe; with -ma it lengthens as in published ilqēma | ilteqēma |
| 3 | 2 · i | medium | "the merchant shall take" unbracketed though dam-qar is a lost word (l has it bracketed) | "[the merchant]" |
| 4 | 1 · i | low | "GUR(-É)" against l's GUR.É | GUR.É |
| 5 | 1 · say of broken words in, di-in | low | bare "in", "din" for fragments that every other broken word marks with an ellipsis | …in, …din |
| 6 | 13 · say …dūšum | low | the long ū is a guess nothing in the spelling gives | …dušum |
| 7 | 13 · n (iṭrussu) | medium | "shortened form … suffix absorbed in uz-zu" misnames the grammar: it is iṭrud + -šu with the d assimilating (-ssu) | note and gloss say so |
| 8 | gloss maḫārum (broaden) | high | the entry did not contain the published entry whole (the merged one is gap-a's "to receive: imḫur(u)"); the draft began with the litany's text and repeated "to receive" | old entry whole + new readings, and the litany's "to face, withstand" (lost in gap-a's replacement) re-added |
| 9 | gloss -šu (broaden) | medium | repeated the old entry twice ("him / it / its … · his / its …"); "after a t-sign the suffix is spelled zu" is not the rule | duplicates dropped; "after a dental the suffix is assimilated and spelled with z" |
| 10 | gloss nadānum, ṣibtum, leqûm, išûm, maḫārum, ilum, elûm (broaden) | low | the new tails re-copied the old text (nādin, ṣibtišu, ileqqi, lā īšu, mulli …) | tails trimmed to the new readings; the litany's mulli re-added to elûm because gap-a's replacement lost it; leqûm now has the q forms |
| 11 | gloss šanûm-Š | high | "šanûm to be two, to double" invents a meaning; "a -ta- element" misnames the Š perfect prefix | "to repeat, do a second time", uštašannâ named a Š-stem perfect, doubt kept |
| 12 | gloss tēḫûm-D | low | stem tense unnamed | "a D perfect" |
| 13 | gloss ḫerûm-Š | low | Š-stem tense unnamed | "Š-stem perfect" |
| 14 | gloss nakārum | low | "refuse" stood as a meaning of nakārum | "to be hostile, to deny, to dispute" |
| 15 | gloss maṭûm | low | "ma and ṭi doubtful" stated for the word; only the §95 line-4 occurrence is doubtful | said so |
| 16 | gloss GIŠ.BAR | medium | "the context shows a measure of grain" overclaims | "suggests a measure (of grain)" |
| 17 | gloss butuqqûm | low | "damage" is not in the evidence | "claim for loss" |
| 18 | gloss šamallûm | medium | "(Delitzsch: šamallû)" attributed a reading I could not check here | attribution dropped; genitive spelling ša-ma-al-li-im given |
| 19 | gloss šuššum | low | "(IGI.6.GAL šeššet še)" not a form the text has | šeššet šeʾam |
| 20 | gloss eṣēpum, alākum, kurrum, kaspum | low | uṣṣap sold as an eṣēpum form ("root of eṣēpum … add, double") on no evidence; "after ašar" with ašar restored; straight apostrophes (še’am) | uṣṣap marked a form I cannot place, link to eṣēpum a guess; "restored ašar"; šeʾam |

### Checked and kept
- All 19 new lemmas present in gloss.json, none already published; lemma names and stems (watārum-D, tēḫûm-D, ḫerûm-Š, šanûm-Š, târum-D, bašûm-N) match the forms; UNCERTAIN markings kept on nakārum, ḫerûm-Š, tēḫûm-D, šanûm-Š, GIŠ.BAR, NER, upaṣ, tappûtum, šamallûm, pašārum.
- IG tr uq for butuqqâm (published practice, as pass 1); ik for ikkir (k root).
- No ḳ in units.json or gloss.json.

### Refused
- Renaming the lemma tēḫûm-D to teḫûm-D: the verb is teḫûm, but the build keys the glossary by the lemma used in morph; the gap-a noun tēḫûm and this verb are told apart in the gloss; left, noted in QUESTIONS.
- Changing "refuses (?)" in unit 2 i: bracketed and marked (?) already.
