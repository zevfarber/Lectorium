# Review — kebra-nagast-ch92-93

Method: every note label checked against the form; `l` word by word against the Geʿez; `l` against `i`; house renderings checked against the published parts (kebra-nagast-ch*.json glossaries and units). `t` verified unchanged: the joined `t` still equals the packet text (whitespace aside). Edits made by script on units.json and gloss.json.

Unit numbers are 0-based positions in `sentences` (0 = heading ch. 92, 8 = heading ch. 93).

## PASS 1 — units.json

| Unit | Field | Severity | Wrong | Done |
|---|---|---|---|---|
| 1 | l, i, n | major | ኢዮቤል ወንሖር taken as the names "Joel and Nohor". ወንሖር is ወ- + ንሖር "let us go" (the published chs. 46–48, 62–63, 82 use ንሖር so, and the known-forms entry for ወንሖር says so); ኢዮቤል is "jubilee, jubilee horn", which fits the horn-blowing that follows. The draft also contradicted the glossary entry the build would show. | "Bring the jubilee horn (?), and let us go to Zion, and there…"; l and note rewritten; (?) kept on ኢዮቤል. |
| 3 | l, i, n | moderate | በውስተ ታዕካ መንግሥት rendered "in the tent of the kingdom", though the glossary says ታዕካ is unidentified and ch. 25–26 reads it "[taʿka] of kingdom, royal palace (?)". "Tent" is ደብተራ. | l "in-inside-of [taʿka] of-kingdom"; i "in the ታዕካ of the kingdom (the royal palace or hall? (?))"; note points to ch. 25–26. |
| 3 | l | minor | ለአዋልደ ጽዮን glossed "from"; ለ- is "to/for" (marks the object or partitive). | l "to-daughters-of Zion"; note says ለ- marks the object or means "from among". i unchanged. |
| 3 | l, i, n | minor | ተውኔተ "play" against the house "revelry" (chs. 62–63). | "revelry"; note names it the house word. |
| 3 | i | minor | ንኡሳን ጸሊማን "the lesser dark-skinned ones": "lesser" is not in the text. | "the small ones, the dark-skinned (?)". |
| 3 | n | minor | ቄፋዝ called a place name without saying ch. 51–52 took it as a cloth term. | Said so; broadening added in gloss. |
| 3 | n | minor | ይከይድ note gave no grammar for the oddity (plural እለ, singular verb, no preposition). | Added; the "among whom" reading stays flagged (?). |
| 3 | n | minor | Word count "45" is 44. | Corrected. |
| 4 | l, i, n | minor | ምስፍና as "city of rule"; house (ch. 83–86) is "city of Məsfəna (?)". The draft also said "on Mount Makeda"; house is Däbrä Makeda, "the Mount of Makeda". | l "city-of Məsfəna"; i "in the city of Məsfəna (?), on Däbrä Makeda, the Mount of Makeda"; note adjusted. |
| 4 | n | moderate | "given his father's throne-name": David is Solomon's father, so Menelik's grandfather. | "the throne-name David, his grandfather's". |
| 5 | l, i, n | moderate | ወለበሓውርት left as a mystery word "(?)" in l and i; ch. 54 already reads በሓውርት as the plural of ብሔር "lands, regions", pairing with አህጉር "cities", which is exactly the parallel here. The gloss lemma ሐውርት "journey" was the glosser's guess. | l "for-lands(?)", i "for the lands (?)"; note rewritten; gloss re-lemmatised (Pass 2). |
| 5 | i | minor | "when what had been made law was completed": ፈጸመ is active "he finished", so a voice change. | "when he had finished what was made law". |
| 5 | n | minor | አንጋዲሆሙ "merchant, traveller" contradicts the earlier entry ("obscure, perhaps relatives or associates (?)"). | Note says both readings are uncertain. i keeps "traders (?)". |
| 6 | l | minor | ሞጻእተ rendered "the-boundaries-of" (plural); the word is singular. | "boundary-of". |
| 6 | l | minor | ዝውእቱ rendered "which-it" (that is ዘውእቱ); it is ዝ- "this". | "this-it". |
| 6 | l, i, n | moderate | ዕሩቃን rendered as a name "Uruqan / ʿUruqan", while the glossary says it is plural ዕሩቅ "naked" (house, chs. 21–22, 78–79). Name-forms were invented. | l "naked-ones", i "the naked ones (?)", note says ዕሩቃን is read as a people beside ጸሊማን. |
| 6 | i | minor | "by its measure" lacked a (?) though ቅሥፈት is guessed (Dillmann ቀሠፈ is "strike"). | (?) added. |
| 6 | i | minor | "its border returns to where it first began": "returns" is not in ኀበ ቀዳሚ ተወጠነ. | "is where it first began". |
| 6 | n | minor | Word count "76" is 75. | Corrected. |
| 7 | l, n | moderate | ሢመቱ ለንጉሠ parsed as construct "the-appointment-of king-of". ሢመቱ is ሢመት + -ሁ, with ለ- naming the owner after the suffix (the known entry says "anticipating"). | l "appointment-his for-king-of Ethiopia"; note explains. i unchanged. |
| 9 | n | minor | ይትዐወቅ called a passive of "አእመረ/ዐወቀ"; አእመረ is a different verb. | Only ዐወቀ (tä-stem). |
| 12 | l, i, n | moderate | ዘእምትካት read "from the first" and ዕድዉ "enemy" with no flag in l/i. House ch. 44 reads እምትካት "from of old (?)"; ዕድው in ch. 35 is "man", which does not suit ዕድዉ ለሰብእ. | l "who-from-ትካት enemy(?)"; i "from of old (?) … the enemy (?)"; note gives both facts. |
| 12 | l, i, n | moderate | ወአምጽኡ is 3mp "they brought", but l/i ran on as "he … and brought heresy". The subject shifts from Satan to a plural. | "and they brought heresy"; note records the shift. |
| 12 | l | minor | ቤተ ክርስቲያን ዘእግዚኣብሔር shown as a construct "church-of God", dropping ዘ. | "church of-God". |
| 14 | i, n | moderate | ጸራ ለጽድቅ ወጸላኤ ሠናያት turned into abstract "enmity" and "hatred", while l has "enemy / hater" and ch. 66 has ጸራ ለጽድቅ "enemies of righteousness (?)". | i "put the same into their hearts, to be enemies of righteousness and haters of good things (?)"; note rewritten. |
| 15 | l | minor | ለፈጣሪሆሙ "against-creator"; ለ- is "to/for". | "to-creator-their" (i keeps "against" for the sense). |
| 15 | l, i | minor | ይውሕኩ sense is a guess, no flag in l/i. | (?) added. |
| 16 | l, i, n | major | ይቤዝዎ parsed as 3mp "that they redeem him (impersonal plural)", and i made it passive "Adam might be redeemed". ይቤዝዎ is 3ms ይቤዝው + -ኦ, with ለአዳም naming the object, so Christ is the subject. | l "that he-redeem-him Adam"; i "so that he might redeem Adam"; note corrected. |
| 16 | l, i, n | moderate | በዕልወቱ given "from"; በ- is "in/by". "fall" was invented. | l "in-his-ዕልወት(?)"; i "in his ዕልወት (sense unknown (?))". |
| 16 | l, i, n | moderate | ወንገኒ "we confess": every published use of ገነየ (+ ለ-) is "serve, bow, praise". | l "we-bow-to(?)", i "give worship to the Holy Trinity (?)"; note says the spelling for ንግነይ is odd. |
| 16 | n | minor | Word count "47" is 46. | Corrected. |

Pass 1 counts: major 2, moderate 10, minor 20.

## PASS 2 — gloss.json

| Entry | Severity | Wrong | Done |
|---|---|---|---|
| ኢዮቤል | major | "Joel (proper name)". | "jubilee, the jubilee horn (also the name Joel, not meant here) (?)". |
| ይውሕኩ | major | Lemma ውሕከ cannot be a G perfect (the pattern CəCəCä does not exist). | Lemma reconstructed as ወሐከ, entry says openly it is reconstructed and not found in the lexicon; (?) kept. |
| ይቤዝዎ | major | 3mp "impersonal plural". | 3ms subjunctive + -ዎ "him". |
| ወለበሓውርት | moderate | Lemma ሐውርት "journey" (not found elsewhere in the corpus). Ch. 54 lemma is ብሔር, "lands, regions". | Lemma ብሔር, "and for the lands, regions" (?). |
| ዘእምትካት | moderate | Stated as "from of old, from the first" without the house basis. | Aligned with ch. 30/44: ትካት "establishment, foundation"; (?) kept. |
| ዕድዉ | moderate | "enemy" unflagged though ዕድው is "man" in ch. 35. | Entry says so; "enemy" guessed from context (?). |
| በዕልወቱ | moderate | "from his perversity, fall" (በ- is not "from"; "fall" invented). | "in his ዕልወት … perhaps 'perversity'; sense unclear (?)". |
| ወንገኒ | moderate | "we confess". | "we bow to, worship", spelled ንገኒ for ንግነይ (?). |
| በርትዕት | moderate | Lemma ርትዕ (the noun); the adjective, as in the known entry ርቱዐ, is ርቱዕ. | Lemma ርቱዕ. |
| ወዕሩቃን | minor | "apparently the name of a people" without saying it is a plural adjective. | "and the naked ones … apparently a people, beside ጸሊማን (?)". |
| ይከይድ | minor | Lemma is right (house lemma ከይደ, perfect spelled ኬደ, chs. 24, 35, 55–56, 73–75, 90); I first suspected ከየደ and withdrew it. | Added a note on the perfect; (?) kept for the sense. |
| በበ፷፻ወአዋልድ | minor | Transliteration səsa; house (ch. 2–8, 62–69) is səssa. | səssa. |
| __broaden__ ቀዳሚ | minor | ኀበ ቀዳሚ ተወጠነ "where it first began" is adverbial; the old entry was only "first (adj.)". | Broadened (old entry whole + " · " + new). |
| __broaden__ ቄፋዝ | minor | The old entry (thread or cloth) does not cover "goes up to ቄፋዝ". | Broadened. |

Pass 2 counts: major 3, moderate 6, minor 5.

Checked and left (no change):
- ዕድው lemma: kept; it is the house lemma (ch. 35).
- አሚን (ወበአሚነ): kept; it matches the house entry (ch. 69, "faith, belief, from አምነ (?)").
- ከየደ / ከይደ: see above.
- Numerals: ተስዓ ወክልኤቱ, ተስዓ ወሠለስቱ, ምእት ወሠላሳ, ስሳ ምእት, ሠለስቱ checked for form and transliteration; they match the house numeral entries.
- ወትትኃለፍ: lemma ኀለፈ kept; the "tä-stem" parse is the glosser's, and the house has no earlier entry. Left with (?).
- ወትወርድ, ወተዐርግ, ወተዐዲ: the 3fs prefix is spelled ተ- (ተዐርግ for ትዐርግ); the parses are right.
- ወፌኔቄንሃ, አቤልሃ, ይባሶ, ብዕዛ, ሊባ, ቢሲስ, አስኔት, ኬቤሬኔዮን, ሲፋላ, ዛውል, ታርሞን: no basis to change; (?) kept.
- Not changed: ሠረቃዊ "eastern" and ሞጻእት (both plausible, and nothing in the corpus contradicts them).

## Refusals (findings not acted on)

1. Cut the long units at a mark other than ። ፤ ፨ (units 3, 6, 16 run 44, 75, 46 words). Refused: the runbook ends units only at those marks and none occurs inside them; the notes already say so.
2. Re-lemmatise ትትኃለፍ as a ተ- form (ተኃለፈ) to match ይትገበር → ተገብረ. Refused: I could not confirm that dictionary form, so the real G lemma ኀለፈ stays with (?).
3. Change "they believed" (unit 11) to "he believed". Refused: the draft's note already names the singular/plural mismatch with (?).
4. Remove "among whom" from unit 3's i. Refused: I have no better reading; it stays flagged (?).
5. Supply a dictionary-grade lemma for መስመረ, አግዋረ, ቅሥፈቱ, ዘእምትካት sense. Refused: unattested to me, with (?) retained.

## Unresolved (?) after review

Unit 1 ኢዮቤል "jubilee horn"; unit 2 ዘውእቱ ቅብአ መንግሥት as gloss; unit 3 ብዕዛ, በበ፷፻ "six thousand", ቄፋዝ, ታዕካ መንግሥት, እለ ይከይድ clause, ጸሊማን "small ones"; unit 4 ምስፍና as a name; unit 5 አላዳስ, በሓውርት "lands", አንጋዲሆሙ; unit 6 Liba/Saba, Bisis, Asnet, ዕሩቃን, Kebereneyon, Phenuel/Sifala, አግዋረ ገነት, መስመረ እክል, ፌኔቄንሃ, Zawl, ቅሥፈቱ "measure"; unit 9 Hebrew month name absent; unit 11 "they believed"; unit 12 ዘእምትካት, ዕድዉ "enemy"; unit 13 ይባሶ, ‑ሃ on አቤልሃ; unit 14 ጸራ ለጽድቅ; unit 15 ይውሕኩ (lemma and sense); unit 16 በዕልወቱ, ንገኒ.
