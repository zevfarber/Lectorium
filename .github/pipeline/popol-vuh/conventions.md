# K'iche', *Popol Vuh* — conventions (pilot, 2026-10-26)

First Mayan text in Lectorium. Zev chose the Ximénez manuscript over Brasseur's printed edition, and
manuscript letters with a modern-letters toggle (2026-10-26).

## Edition of record

**The manuscript itself**: Newberry Library, Ayer MS 1515, the only surviving copy of the K'iche'
text, in the hand of Fray Francisco Ximénez (Chichicastenango, c. 1701–03), K'iche' in the left
column, his Spanish in the right. Read from the Library of Congress / World Digital Library images
(`loc.gov/item/2021668226`, IIIF `service:gdc:gdcwdl:wd:l_:19:99:5:wdl_19995:ayer_ms_1515_vol_2_NNNN`;
the text starts at image 0009 = fol. 1r). No one owns the manuscript's text.

Second witness, for checking only: **Brasseur de Bourbourg, *Popol Vuh: le livre sacré* (Paris,
1861)**, archive.org `Ayer_F1465_P814_1861` (OCR in `_djvu.txt`). Brasseur respells the K'iche'
(q for k', g for q', k for q, hyphenated morphemes) and normalises; he is never the text. Later
editions (Schultze Jena 1944, Recinos, Edmonson, Tedlock, Christenson, Sam Colop) are in copyright and
are not consulted for wording.

## What the text looks like

- **Ximénez's spelling, kept**: c/qu for /k/ and often /q/; v for u and w (`vbi`, `vleu`, `vinac`);
  z for s; h for j; b for b'; double vowels for a glottal stop (`vbinaam`, `caam`, `cool`).
- **The colonial (Parra) letters** are printed with their Unicode forms: ꜩ (tz), ꜯ (tz'),
  ꜭ (k'), ꜭh (ch'), ꜫ (q'). In Ximénez's cursive the cuatrillo ꜭ looks like a g, the tresillo ꜫ like
  a 3/ɛ or a q, and the tz' is the tz ligature with a small comma. Where the hand is ambiguous,
  Brasseur's transliteration (his q = ꜭ, g = ꜫ) decided; Brasseur is unreliable as a text and was used only to choose between letters. tz' is printed only where the word is a
  known tz' word and the comma is consistent with the hand.
- **Unmarked ejectives stay unmarked**: Ximénez writes `calah` (q'alaj), `ramac` (ramaq'), `Quiche`
  (K'iche'). The text shows what he wrote; the modern toggle supplies the mark.
- **Word division, punctuation, capitals and quotation marks are ours.** Ximénez runs particles into
  words across line breaks and punctuates lightly. Capitals: sentence start and names (including the
  divine titles Vꜭux Cah, Vꜭux Vleu, Vꜭux Cho, Vꜭux Palo).
- **His corrections are taken in**: `xevi`, written above the line with a caret, is printed in place
  and the note says so.

## The modern-letters toggle (ꜩ→tz)

Each unit carries `mt`: one modern ALMG spelling per word token, in order. The reader shows `mt[wi]`
in place of each word when the toggle is on; tapping still looks up the manuscript form. Rules:
respell every letter (ꜩ→tz, ꜯ→tz', ꜭ→k', ꜭh→ch', ꜫ→q', v→u/w, z→s, h→j, b→b'); supply an
unmarked ejective or glottal stop **only where the word is certain** (K'iche', uk'u'x, q'equm,
aq'ab', ub'i', winaq, ja', che'); a word whose modern form is uncertain is respelled letter for
letter and nothing is restored. A conversion function would get k/q and the ejectives wrong, which is
why the data is per word.

## Sectioning

The manuscript's own divisions: Ximénez's paragraphs and his marginal numbers, and the capitalised
headings (ARE V XE OHER…, ARE V ꜨIHOXIC VAE). Parts are episodes, ids `popol-vuh-NNN`. The pilot is
fol. 1r–2v line 1: the preamble and the making of the earth, ending `…rutzinic vbanatahic cumal.`
just before the animals (`Ta xquinohih chic vchicopil huyub…`).

## Segmentation

Prose with a strong couplet structure. The tap-unit is the sentence, cut at Ximénez's full stop or
our full stop/semicolon; a long litany of names is cut at a syntactic joint (the pilot cuts the
creators' names after `qui bi,`). Couplets are never split across units. `p: true` follows
Ximénez's paragraphs and headings.

## The two English layers

- `l` follows K'iche' order and shows the morphology with hyphens where it carries meaning
  (`we-shall-write`, `its-planting-place`, `they-said`); possessive prefixes appear as `its-`/`their-`.
- `i` is real English, lightly elevated, never archaic for its own sake. **Couplets stay couplets**
  in `i` — the doubling is the poetry ("the Builder and the Shaper", "in the darkness, in the night").
- Names stay K'iche' in English (Hunahpu, Xpiyacoc, Xmucane, Tepeu, Q'ucumatz, Huracan); epithets are
  translated (Heart of Sky, Heart of Earth, Builder, Shaper, Bearer, Begetter, Thunderbolt).

## House renderings — fixed before drafting

| K'iche' (MS) | `l` | `i` | avoided |
|---|---|---|---|
| Ꜯacol, Bitol | Builder, Shaper | the Builder and (the) Shaper | Framer and Former, Maker and Modeler, Creator and Former |
| Alom, Ꜭaholom | Child-Bearer, Son-Begetter | the Mother of children and the Father of sons | Bearer and Begetter, She Who Bears / He Who Begets |
| Vꜭux Cah / Vꜭux Vleu | Heart of-Sky / Heart of-Earth | Heart of Sky / Heart of Earth | Heart of Heaven |
| Tepeu | Sovereign | Tepeu | — |
| Ꜫucumaꜩ | Quetzal-Serpent | Q'ucumatz | Sovereign Plumed Serpent, Gucumatz |
| Caculha | Thunderbolt | Thunderbolt | Lightning (for the name) |
| Chipi Caculha / Raxa Caculha | Youngest Thunderbolt / Green Thunderbolt | same | Newborn, Sudden |
| oher ꜩih | old word | the ancient word | — |
| Popo Vuh | Council Book | the Popol Vuh | — |
| ilbal | seeing-instrument | the means of seeing | — |
| queꜫum, aꜫab | darkness, night | the darkness, the night | — |
| zaquil | white / light | the clear light | — |
| ꜭazlem, vinaquirem | life, creation | life, all that is made | — |
| Iyom, Mamom | Midwife, Grandfather | the Midwife, the Grandfather | Grandmother of Day |
| Maꜩanel, Chuquenel | Keeper, Coverer | Keeper and Coverer | Protector, Shelterer |
| Ah Raxa Laꜫ / Ah Raxa Ꜩel | He-of Green Plate / He-of Green Bowl | He of the Green Plate / He of the Green Bowl | Lord of the Green Plate |
| chuꜭhaxic | it-is-said | as they are called / as it is said | — |
| naual | spirit-power | spirit power | genius, magic |

## Notes (`n`)

What a tutor would point at: the morphology a reader will meet again (x- completive, ca-
ongoing, x(chi)- future, chi optative, ergative v-/r-/qui-/ca- against absolutive xe-, -ibal,
agent nouns, positionals, the plural e and -ac and tac, relational nouns with person prefixes like
ruꜭ, cuꜭ), the couplet, the manuscript letter, and the cultural fact. Quote K'iche' bare in the MS
spelling, English glosses in single quotes. Where a word's meaning is disputed the note says so in
plain words and the renderings say "inferred" or "guess". Names: what is known, and no more.

## Sole-source rule and lexical aids

Draft from the manuscript, with Ximénez's own Spanish column, his *Tesoro de las tres lenguas*, and
Brasseur 1861 as public-domain meaning checks; Basseta's and Coto's colonial vocabularies where
reachable. Modern dictionaries may be consulted for meanings (a dictionary entry is a meaning, not a
rendering). Modern Popol Vuh translations (Tedlock, Christenson, Recinos/Goetz–Morley, Edmonson,
Sam Colop) stay closed; an English phrase that arrives fully formed is suspect and is rebuilt from the
K'iche'.

## Pronunciation and audio

`langCode: null`. Convention: modern K'iche' values for the modern-alphabet spelling (stress final,
ejectives as written, glottal stop where marked). Audio later, after a voice round with Zev.

## Glossary

Work-level `popol-vuh-glossary.json`. Keys: the lowercased manuscript forms as tokenized (ꜩ etc.
included). Values: `modern form — meaning; morphology`.

Tz is always printed ꜩ: Ximénez writes the tz ligature throughout (Ꜫucumaꜩ, Maꜩanel, vꜩ).
