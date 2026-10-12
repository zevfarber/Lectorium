# Review — hammurabi-gap-a

## Pass 1

Method: every unit read against Kohler–Ungnad II pp. 34–36 (page images, upright / italic / brackets), Ungnad's
Vorbemerkungen (column lists of the fragments, PDF p. 7), Ungnad's autographs (Fragment I cols. II–III, Fragment II
col. I viewed; the Assyrian plates Rm. 277 / DT 81 NOT viewed); written lines compared with the established lines
(all 10 units: line counts equal, nl marks fall on the first word of each line); `reading` rebuilt from glyph `tr`
(all match); every sign key exists in signs-cuneiform.json; every note contains its siglum; morph indices checked.
Sign-by-sign identity on the plates was NOT completed: the small Susa drawings do not allow it at the available
resolution; I confirmed row/line layout and the few distinctive signs only. The about now says so.

### Changes
| # | unit · field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 1 | top · about | medium | "about five columns" erased; Ungnad (Vorbemerkungen) says the last seven (XVII–XXIII) | changed to seven, with Ungnad's count |
| 2 | top · about | low | Ashurbanipal's copies "twelve hundred years" after Hammurabi (it is ≈1100) | "more than a thousand years" |
| 3 | top · about | medium | §66 summary "the dates pay the silver" misstates the law | rewritten: owner takes the dates, pays silver and interest per the tablet, keeps the surplus |
| 4 | top · about | medium | claimed "the signs are read on Ungnad's autographs" — overstated (drafter could not read all) | now says signs follow the transliteration, checked on the autographs only where legible |
| 5 | top · about | low | "one complete law, §71" (it is partly restored) | "nearly whole" |
| 6 | 0 · morph (i-ip-pa-al-ma) | high | `-ma` pointed at glyph index 5 (word has 5 glyphs: out of range) | apālum [0–3], -ma [4] |
| 7 | 0 · morph (3× DAM.GÀR-im/-am) | low | the complement glyph left outside any morph | tamkārum covers [0,1,2] |
| 8 | 0 · say iqbīšum | medium | iqbi (short final vowel) + -šum = iqbišum; also the published form | iqbišum |
| 9 | 0 · say ileqqēma | low | published parts say ileqqīma for the same spelling | ileqqīma (house form) |
| 10 | 0 · l | low | "as-the-mouth-of" dropped the `ša` | "that-of-the-mouth-of his-tablet" |
| 11 | 0 · n | medium | ṣibat-zu: MÁŠ identification only the drafter's | note now gives the evidence (stele spells ṣi-ba-zu §51; Ungnad prints it as one word like his logograms) and keeps it unconfirmed |
| 12 | 0 · n | low | isiršuma (esērum "to press") had no support stated | note says the sense is from context, Ungnad's gloss thin |
| 13 | 1 · n | medium | "column I" of Rm. 277: Ungnad's list gives XVII 9–32 as column II | note corrected (established `ref` left as pinned, says col. I) |
| 14 | 1 · n | medium | note said all four lines are italic/Rm. 277; line 25 (ša ina kirîm) is upright = Susa | note says so |
| 15 | 1 · n | low | "ileqqe" | "ileqqi" (house form) |
| 16 | 2 · n | medium | same column error | corrected to column II |
| 17 | 2 · l, i | low | tēḫûšu "adjoining plot" is Ungnad's guess ("so wohl") but rendered flat | marked (?) |
| 18 | 3 · n | medium | packet/ref glosses "they will give him"; grammar: i-na-di-iš-šum = inaddin + šum, singular (the published parts have the same inaddiššum) | l/i keep "he shall give him"; note states why plural is wrong; ref string untouched |
| 19 | 3 · l, i | low | "he shall give" is built from restored ina- | bracketed [he-shall-] |
| 20 | 4 · say itēšu | medium | published parts say itêšu | itêšu (word and note) |
| 21 | 4 · i | medium | "If a man gives" — the text has no awīlum | "If someone gives" |
| 22 | 4 · n | low | ša išammu could be "he who buys" | note states both |
| 23 | 5 · l | low | "he-builds" from i-te- only | (?) added |
| 24 | 8 · i | high | "[he said]" invented, not in l or text | removed |
| 25 | 8 · i, morph | medium | final `am` carried lemma kaspum and "silver (?)" only from the editor's [kasp]am(?) | morph emptied; "[silver (?)]" bracketed |
| 26 | 8 · l | low | "work!" for epuš (epēšum "do, make") in a "transparent" l | "make!" (i keeps "Work (?)") |
| 27 | 8 · n | low | "imperative of danānum" | "D-stem imperative" |
| 28 | 9 · l, i | high | the final verb [itelli] is wholly lost, and "the house" in line 5; rendered as if read | brackets added in l and i |
| 29 | 9 · n | medium | undisclosed: aš-bu-u[m] is Peiser's conjecture (Ungnad's fn. 2); page prints ú-[še-zu-ú] where the pinned text has ṣu; itelli wholly restored | all added to the note |

### Findings checked and kept
- **ṣibat-zu as MÁŠ+ZU**: kept, disclosed (row 11). Not confirmable on the plate.
- **kiṣri as KA.SAR** (law 78): matches Ungnad's footnote 3 ("KA.SAR"); kept.
- **suluppî as KA.LUM**: Ungnad's own (glossary: "stets ideogr. KA.LUM"); `tr` ZÚ on the KA sign follows the modern reading, note says so; kept.
- **Law 70**: singular (see row 18).
- **Law 78 line 8**: page prints úmi^mi[-šú] (bracket before -šú) against pinned `i-na ûmi-šu`; the unit follows the page (UD + mi, no -šu). Pinned lines unchanged. Line 13 (úmi[^mi-šú]) likewise: UD only. Also pinned DT 81 col. III ref says XIX 25–42, Ungnad's list says 25–41 (ref untouched).
- **Partly broken syllables adopted as visible** (aš-bu-u[m], wa-ṣ[a-am], a[š-šum], i-l[i-ki], [n]i, e[l], [iš-t]u, i-r[i-a-ab]): accepted — the editor's bracket falls inside the sign, so part of it is on the tablet; each is flagged in its note. Not confirmed on the Assyrian plates.
- **tēḫûšu**: Ungnad's glossary "angrenzendes Stück … so wohl"; lemma tēḫûm kept, now (?) in l/i.
- **bašûm-N** vs the published lemma `bašûm` for the same form ibbaššû: kept (N-stem is correct; compare bašûm-Š).
- **il-kam as IL + GA(kam)**: same as laws-26-41; kept.
- Law 76 sign doubts (at, da, iš, uš, bi, am) are Ungnad's own question marks and are noted as such.

### Refused
- Removing the "(?)"-heavy i of unit 8: it is honest about an unclear passage.
- Converting l's "and" to "or" in grain/silver/goods lists: l is literal, i follows the house "grain or sesame".
- Renaming esērum to eṣērum: Ungnad writes s; sense uncertain; left.
- Changing established refs ("Rm. 277 col. I", "XIX 25–42", "they will give him"): pinned, untouched; reported.

### Not verified
Sign identity on the plates (all units); Rm. 277 and DT 81 autographs not viewed; whether MÁŠ, KAM (as GA) and the Susa-II doubtful signs are right.

### Lemma names
None renamed. New lemmas for the glosser: apālum, bašûm-N, esērum, kiṣrum, mala, malûm, nabalkattum, suluppû, šubalkutum, tarkibtum, tēḫûm, and the suffixes -ka, -kum, -šum.

## Pass 2

Method: every gloss.json entry (13 new lemmas, 6 `__broaden__`) checked against its use in units.json and the established text
(source/established/hammurabi-gap-a.json), and against the glossary as the build merges it (`merged_inline_glossary`: the published
parts' entries). Units re-read for labels in notes against forms, l against i, l against i vs the established lines, published-part
consistency (`say` forms checked against the five published parts). No modern translation opened or recalled.

### Changes
| # | unit / entry · field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 1 | gloss `__broaden__` wabālum · whole entry | high | the old text was exact, but the lemma is wrong for this part and the new readings were not used here (itbalam, ublam, ublū are not in this part): ta-ba-al is tabālum "take away", which the published parts already have as its own lemma (laws-42-51 §49, `tabal`) | broaden entry deleted; unit 0 `tabal` re-lemmatised wabālum → tabālum (published entry covers the imperative) |
| 2 | gloss `__broaden__` watārum · old text | high | old text given was not the published entry ("to exceed; Š-stem — mušāter … ušāterūšu …"); a broaden over a wrong old text would have overwritten the real entry | rebuilt as exact old + ' · ' + new reading |
| 3 | gloss `__broaden__` wašābum · new reading | high | glosser's constructed phrase "aššum wāšbum" does not exist in the established text (it reads a[š-šum] … wa-aš-ša-[ba-am], the object wāšbam, and is broken) and gave the nominative; "participle" unqualified | phrase removed; reading now "wāšbum (participle, contracted) “the dweller, the tenant” (a conjectured reading, aš-bu-u[m])" |
| 4 | gloss `__broaden__` bašûm, epēšum, ūmum · new readings | medium | bašûm: example fine, kept; epēšum: "to build" stated flat though only i-ip / ite… survive; ūmum: "before his days are full" is interpretation, not the literal | epēšum marked (?) with the broken-verb caveat; ūmum gives ūmī “days” and the literal "in his days not full"; bašûm unchanged beyond the exact old text |
| 5 | gloss tarkibtum | medium | "completed fitting-out, from rakābum" presented as a derivation | marked UNCERTAIN, "perhaps"; sense a guess |
| 6 | gloss nabalkattum, šubalkutum | high | root named "balākutum" (invented): the verb is the quadriliteral nabalkutum (root BLKT); ušbalakatūnim labelled "preterite? plural" (a question mark in place of a label; the form is present 3rd plural + ventive) | root corrected to BLKT / nabalkutum; šubalkutum "present, 3rd plural, with ventive -nim"; both stay UNCERTAIN |
| 7 | gloss esērum, kiṣrum | medium | context-derived senses not marked as uncertain | prefixed UNCERTAIN |
| 8 | gloss suluppû | low | "genitive/accusative form as printed" (the noun is collective, plural in use); "written ZÚ.LUM, or KA.LUM" blurred which is which | rewritten: collective noun, oblique case; ZÚ.LUM today, KA.LUM in Ungnad |
| 9 | gloss mala, -ka, apālum, -šum, -kum, malûm, bašûm-N | low | "whatever amount of" (stray gloss); "-ka / -ka" circular; apālum bare; -šum/-kum/malûm labels loose; ibbaššû "present, plural" kept but now "3rd plural" | tightened; no sense changed |
| 10 | 4 · say ītelli (and note, 9 note) | medium | published parts say ītelli for i-te-el-li (§35, §37) | ītelli in word and in the two notes |
| 11 | 4 · say īšu | medium | i-šu said išû; published (laws 1-10) lā īšu, and the clause is singular | īšu |
| 12 | 8 · l | high | "be-firm!" for dannin: a D-stem imperative is "make firm" (i already said so); l mislabelled the stem | "make-firm!" |
| 13 | 0 · l, i, n (tarkibtim) | medium | "the-putting-in-order" rendered flat, no word in the published parts; the note never mentioned the doubt | (?) added in l and i; note says it is a guess from context |
| 14 | 2 · l, i | medium | "he-builds-and" / "builds a house and" read as if on the tablet: only i-ip survives, the rest is the editor's | "he-builds(?)[-and]"; "builds (?) a house [and]" |
| 15 | 6 · n | low | "riābum, as in §8 and §23": iriab is in §8 and §53 in the published parts | §53 |
| 16 | 8 · n | low | nidītum "the word of the field laws, §42–47": the published parts have it at §61 | "met in §61 for a plot left lying" |

### Findings checked and kept
- **elûm, šâmum, bīšum, nadānum, ilkum, pûm, kirûm, tamkārum, ṣibtum, nidītum, itûm, waṣûm-Š, danānum-D and the other known lemmas**: published entries cover their use here; no broaden needed (the glosser's list was right in leaving them out).
- **bašûm-N** as a new lemma beside published `bašûm` (same form ibbaššû in the published parts is filed under `bašûm`): kept, N-stem is the right label; compare bašûm-Š.
- **-šum as its own lemma** although the published `-šu` entry mentions -šum as dative: kept, because the morph here uses lemma -šum.
- **ūmi (UD-mi / UD, -šu lost)** said ūmi: the surviving signs only; the plural form ūmī-šu is in the gloss.
- **wāšbum** (aš-bu-um): kept as the unit's reading; participle contracted from wāšibum; conjectural (Peiser via Ungnad fn. 2, as the note says).
- Pass-1 refusals stand (esērum not renamed eqērum/eṣērum; refs left as pinned).

### Refused
- Shortening the three very long notes (units 0, 4, 9): they carry the first-occurrence teaching and the disclosures; the WARN stays.
- Rewriting the i of unit 8 to remove the speech quotes: honest enough with the (?)s.

### Build / validate
`build`: BUILT, 10 units. `validate`: PASS, 0 errors. `signs.py check`: in sync. 3 WARNs "n is very long" (accepted, see above); 24 WARNs "ours X vs established Y — confirm on the autograph": every one is a logogram versus Ungnad's Akkadian spelling (kaspam = KÙ.BABBAR, bîtim = É) or a bracketed restoration deliberately not adopted as signs; none is a mismatch of visible signs.

### New house renderings (for conventions.md)
`ša pî ṭuppišu` "according to his tablet"; `bēl kirîm` "the owner of the orchard"; `tamkārum šū ul immagar` "that merchant shall not agree"; `bīt ilkim` "a house that carries fief-duty"; `ina mimma ša iddinu ītelli` "he forfeits whatever he gave"; `bītum ana bēlīšu itâr` "the house returns to its owner"; `ina ūmīšu lā malûtim` "before his days are full" (l: "in his days not full"); `tabal` "take away!" (lemma tabālum); `ītelli` (not itelli), `īšu` (not išû).
