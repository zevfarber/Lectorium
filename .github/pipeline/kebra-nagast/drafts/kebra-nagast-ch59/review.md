# Review — kebra-nagast-ch59 (ch. 59, "The Egyptian Envoy's Report")

Adversarial review, two passes, both applied to the draft files by script
(`scratchpad/pass1.py`, `scratchpad/pass2.py`). Dillmann was not available offline, so every
reading that rests on guesswork keeps its `(?)`. No modern translation was opened. The units'
`t` was not touched: the join of all 15 `t` still reproduces the packet's Geʿez exactly
(checked by script, whitespace aside). Both JSON files re-parse.

Sources used for consistency: `conventions.md`, `runbook.md`, `../run3/RUNBOOK.md`,
`kebra-nagast-ch1.json` (register) and the published siblings, above all ch. 49–50, 53, 54,
55–56 and 57–58, which narrate the same journey and the same flying cart.

---

## PASS 1 — units.json

### Major

| unit | field | what was wrong | what was done |
|---|---|---|---|
| 0 | l, i, n | The heading was misparsed. `ሐተቶ` was taken as a verbal noun ("questioning-of") and `ኀበ` was flagged as the least clear word, possibly an error for በእንተ. But the heading has exactly the shape of chs. 49, 53, 54: ኀበ 'where' + perfect verb, and ch. 23's published entry parses `ዘሐተቶ` as ሐተተ + -ኦ 'him'. ለግብጻዊ is then the object named after the suffix (as ባረኮ … ለወልዱ, ch. 49). | l → "59. Where he-questioned-him to-the-Egyptian, servant-of Pharaoh."; i → "Chapter 59: Where he questioned the Egyptian, Pharaoh's servant"; note rewritten, naming the parallel headings and the object-doubling ለ-, and saying that the unnamed subject is Solomon. The ኀበ (?) is withdrawn — it is the house reading of three published headings. |
| 7 | n | "ነፉስ 'wind' (?) is not a form I can place … flagged." The form is already glossed in the published parts (chs. 51–52, 55–56, 57–58: "ነፋስ — wind (noun; spelled ነፉስ)") and is in this part's `known-forms.json`. A reader is told the draft is ignorant of a word the project settled three parts ago. | Note now states that ነፉስ is the printed spelling of ነፋስ as in those chapters, and that በሰረገላ ነፉስ is "a cart of wind (?)", the flying cart of chs. 51–58. |
| 8 | l | `ወማኅፈድ ስምዐ ኮኑ` was rendered "and-fortress-of witness became", making ማኅፈድ the construct of ስምዕ. ማኅፈድ is not in the construct (that is ማኅፈደ, later in the same unit), and ስምዐ is the accusative predicate of ኮኑ. | l → "… in-cities and-tower witness became …"; note explains ስምዐ ኮኑ as accusative predicate + 'they became'. |
| 11 | n | `ዘአንጽሑ` was given the root "ጸሐየ/ጻሕ-type" and was said to carry "-ሁ 'it'". The verb is the causative of ነጽሐ 'be clean, pure', and it has no object suffix at all (ዘ- + አንጽሑ, 3mp perfect). | Note corrected on both points; l changed from "which-sanctified-it for-you your-fathers" to "which-sanctified for-you your-fathers". |

### Moderate

| unit | field | what was wrong | what was done |
|---|---|---|---|
| — | about | "Solomon's messenger, an Egyptian governor sent by Pharaoh" — he is Pharaoh's envoy, not Solomon's; the phrase contradicts itself. | Rewritten: "An Egyptian governor, sent to Solomon by Pharaoh, reports …"; "chariots" → "carts" to match the published parts. |
| 1 | n | The subject of ወኀለፈ/ወረከበ was guessed as "the man sent to look for the Ethiopians (?)". Ch. 58 ends with Solomon himself rising to follow the trail, so Solomon is the likelier subject. | Note now reads "Solomon himself, who in ch. 58 rose and set out after the Ethiopians (?)", and points out that the subject shifts inside the unit (the governor arrives and bows). |
| 1 | l | `መኰንነ` glossed in l as "governor-of", i.e. a construct; it is the accusative object of ረከበ, with the partitive እመኳንንተ following. | l → "one governor from-governors-of Egypt"; note says "accusative of መኰንን". |
| 1 | i | "gifts and goods of every kind" silently dropped ምስሌሁ 'with him' and over-read ምሉእ. | i → "with gifts and a full store of goods with him"; the (?) on the sense is kept in the note. |
| 2 | l | "And-hastened him to-question-him Solomon the-king" renders the single suffix -ኦ twice and breaks the word-by-word order. | l → "And-hastened-him to-question Solomon the-king …". |
| 2 | n | The -ኦ of ወአፍጠኖ was explained as "a loose 'on his part'/object marker". It is the object of the accusative infinitive ሐቲተ, drawn onto the governing verb. | Note rewritten accordingly (hedge dropped, the construction is regular). |
| 2, 5, 6 | l, i | `ሰብአ ኢትዮጵያ` was "people-of Ethiopia" / "any Ethiopians" / "those Ethiopians"; the published parts (ch. 57–58, ch. 55) render it "men of Ethiopia", and the known entry for ሰብአ gives 'men of'. | All three brought to "men-of Ethiopia" / "the men of Ethiopia" / "these men of Ethiopia". |
| 2 | n | `ይግዕዙ` after እንዘ was unlabelled in the note but called a subjunctive in the gloss; after እንዘ it is the imperfect. The lemma also differed between note (ግዕዘ) and gloss (ገዐዘ). | Note gives "እንዘ 'while' + the imperfect" and the lemma ገዐዘ (?), matching the corrected gloss. |
| 4 | n | "ኣየድዐከ is an uncertain form (?) … the root is not clear to me and this is flagged for the glosser." The verb is አይድዐ 'make known, announce' (root y-d-ʿ). | Note now parses it as 1cs imperfect of አይድዐ + -ከ, with the printed first-order ኣ- flagged (?) instead of the whole word. |
| 5 | i | "those Ethiopians you ask about" for ዘትብል ('of whom you say/speak'; the known entry is "what you say"). | i → "these men of Ethiopia of whom you speak". |
| 6 | l, i | "Takazi" for ተከዚ; the published parts (chs. 53, 57–58) spell it "Takkaze". | Both changed to Takkaze; the note cites those chapters for the oddity of the Takkaze standing in Egypt, instead of re-opening it as a fresh (?). |
| 6 | l, i, n | `ዕንዚራት` rendered "horns" and glossed "horns/pipes (?)"; the published parts render ዕንዚራ/ዕንዚራት "harp(s)" (chs. 38–39, 55–56). | l "with-harps", i "sounding their harps (?)", and the note states the real tension honestly: the published sense is a stringed instrument, while ነፍሐ 'blow' would suit a wind instrument, so the instrument stays uncertain (?). |
| 6, 7 | l, i | `ሰረገላት` / `በሰረገላ ነፉስ` rendered "chariots" and "a wind-borne chariot". For this vehicle the published siblings (chs. 49–50, 51–52, 53, 55–56, 57–58, and the known entry "በሰረገላ — in a cart") say "cart", and "wind-borne" is a free rendering of the house "cart of wind (?)". | "in-carts" / "racing in carts"; "in-cart-of wind" / "a cart of wind (?) like this". Note names the house rendering. |
| 9 | l, i | `ማርያነ` was left in Geʿez in l but turned into "the Egyptian elders (?)" in i, so the popup and the English disagree about a word the draft itself calls undecidable. | Both now keep "ማርያን (?)", the way chs. 51–52 and 55–56 keep ጽግነት, ውውዓ, ቤሎንቶስ. |
| 9 | n | Only one reading of ገነውተ was offered (subject of ሐተቱ), though the construct form leaves the case open and the object reading ("they questioned the priests … and they said to us") is at least as good. | The alternative is now stated, with the observation that the sense is unchanged. |
| 9 | n | "the tradition that the Ark's tablets were given from heaven (Exodus 25)" — Exodus 25 is the command to build the ark, not a descent from heaven; the allusion as printed is wrong. | Replaced with the book's own heavenly Zion and the pattern "shown on the mountain" (Exodus 25:40). |
| 14 | l | `ለእግዝእትነ` rendered "our-lady" in l, losing the ለ- that the note itself explains as the object marker. | l → "to-our-lady". |

### Minor

| unit | field | what was wrong | what was done |
|---|---|---|---|
| 3 | i, n | "answered him and said to the king" renders the one suffix -ኦ twice; the note did not mention that ለንጉሥ doubles it. | i → "answered and said to the king"; note explains the doubling and that ንጉሥ is a vocative without ኦ. |
| 5 | n | The note did not say which king owns the city. | Added: the king here is Pharaoh. |
| 5, 8 | n | The lemma of 'enter' was written በአ in the notes but ቦአ in the glossary. | Notes unified to ቦአ (the glossary's and Dillmann's dictionary form). |
| 6 | n | "ሠሉስ … 'three days ago' is the alternative (?)" — ch. 57–58 already fixes ሠሉስ (ዕለት) as Tuesday. | Weak alternative dropped; the note cites ch. 57–58 and explains እንተ as the feminine relative agreeing with ዕለት. |
| 7 | n | "ርእይዎሙ (ርእየ + -ሙ)" — the suffix is -ዎሙ. | Corrected. |
| 8 | n | "ተሰብሩ … T-stem of ሰብረ" — the lemma is ሰበረ (as in the gloss). | Corrected. |
| 10 | i | "when it entered" for the Ark, where units 12 and 14 say "she". | → "when she entered". |
| 11 | n | "ጥበብ 'wisdom' (fem?)" — the published glossary states "noun, fem." | Hedge removed, with the published glossary named. |
| 12 | n | ተናገረ called "the reciprocal T-stem"; the stray -አ of ሰማይኒአ was called unclear with no cross-reference. | "T-stem of ነገረ 'to tell'"; the ch. 36 precedent (ወሀበነአ) is cited and the (?) kept. |
| 13 | n | No allusion named, though the reproach is a close echo. | Added "cf. Isaiah 42:8, 'my glory I give to no other' (?)". |
| 14 | n | Lemma given as ክህለ where the published entry has ከህለ; the infinitive given as ነሢአ where the gloss has ነሢኦት. | Both aligned to the published/gloss forms. |
| 0 | i | Heading rendered "Chapter 59. The questioning of …", where the published headings are "Chapter N: …". | Brought to the published shape (see Major, unit 0). |
| 6–10, 12 | i | The envoy's speech is one long quotation, but only units 4, 5, 11 and 13 carried quotation marks, and the priests' words inside it used the same single quotes as the envoy's. | Each continuing unit now opens with `'`, and speech inside speech (units 7, 9, 10) is in double quotes, as ch. 36 does. |

### PASS 1 findings refused

- **ሐተቶ as a verbal noun** (the drafter's reading): refused. Ch. 23's published entry parses the identical form as perfect + -ኦ, and the heading pattern ኀበ + perfect (+ ለ- object) is established by chs. 49, 53, 54.
- **Identifying ተከዚ with the Nile, or emending ፈለገ ምስር**: refused. Chs. 53 and 57–58 keep the printed geography and flag it; this part now does the same, with the (?) kept.
- **Resolving ማርያነ to "diviners/magicians"**: refused — no Dillmann, no internal evidence; left in Geʿez with (?).
- **Rendering ክብር as "honour" in unit 13**: refused; "glory" keeps the link to the book's title word ክብረ ነገሥት, which the note makes.
- **Making ማኅፈድ "temple" outright**: refused. The published sense is 'tower (?)'; "a building of the idols, a temple tower or precinct (?)" is as far as the evidence goes.
- **Naming Menelik or the Queen of Sheba in `i`**: refused — the Geʿez of this part names neither.
- **Dropping the (?) on ቃህራ = Cairo**: refused; the identification is obvious but unverified here, so the hedge stays.

---

## PASS 2 — units.json and gloss.json

Coverage was checked by script first: all 169 distinct forms of the part are accounted for by
`novel-forms.json` + `known-forms.json`; every one of the 65 novel forms has an entry; no entry
glosses a form absent from the text; every entry has the `<lemma> — <meaning> (<grammar>)`
shape. The faults were in the lemmas and the parses, not in the coverage.

### Major

| entry | field | what was wrong | what was done |
|---|---|---|---|
| ሐተቶ | lemma, parse | "ሐተት — questioning, inquiry (verbal noun of ሐተተ … form uncertain (?))". The popup would show a dictionary form the text does not have, for a plain perfect + object suffix (cf. the published ዘሐተቶ, ch. 23). | → "ሐተተ — he questioned him, examined him (3ms perfect, G, ḥ-t-t + -ኦ '3ms him'; the object is named after it by ለ-, ለግብጻዊ)". |
| ገብረ | __broaden__ | Missing altogether. The published entry carried in `known-forms.json` is "ገብረ — make, do (3ms perfect)", which is simply wrong for ገብረ ፈርዖን 'servant of Pharaoh' — a reader tapping the word in the heading would be told it is a verb. | Added under `__broaden__`, old entry whole + " · " + the new reading: "… · here the noun ገብር 'servant' in the construct state, ገብረ ፈርዖን 'servant of Pharaoh'". |
| ዘአንጽሑ | parse | "causative of ጸሐ/ንጽሐ" — neither is the verb; and the meaning implied an object suffix the form does not have. | → "ዘ- relative + 3mp perfect, causative of ነጽሐ 'be clean, pure'; no object suffix — the object is the antecedent of ዘ-". |
| ኣየድዐከ | lemma | "አየድዐ" is the imperfect stem, not a dictionary form, and the root was left unknown. | → "አይድዐ — … (1cs imperfect አየድዕ + -ከ '2ms to you'; root y-d-ʿ 'know'; the first-order ኣ- is as printed) (?)". |

### Moderate

| entry | field | what was wrong | what was done |
|---|---|---|---|
| ይግዕዙ | grammar | "3mp subjunctive" — after እንዘ Geʿez has the imperfect. | → "3mp imperfect after እንዘ"; the (?) on the lemma ገዐዘ kept. |
| ወይረውጹ | lemma | "ረወጸ", a form the published parts do not use; ch. 51–52's note gives ሮጸ. | → "ሮጸ — and they run, race (ወ- + 3mp imperfect, G, r-w-ṣ)". |
| በዕንዚራት | meaning | "with lyres/horns … harp, lyre or a blown instrument (?)" — looser than, and partly contrary to, the published entries for ዕንዚራ/ዕንዚራት ("harp", a stringed instrument). | Aligned to the house rendering, with the ነፍሐ 'blow' difficulty stated inside the entry and the (?) kept. |
| በሰረገላት | meaning | "in chariots", against the published rendering of this vehicle. | → "in carts, chariots (… 'cart' is the published parts' rendering for the Ethiopians' vehicle)". |
| ገነውተ | lemma | "ገነው" is an invented singular. | → "ገነውት (?)", the attested plural, with the singular declared uncertain and the verb ገነወ 'to serve' offered as background (?) — the way chs. 51–52 and 55–56 treat unknown lemmas. |
| ማርያነ | lemma, meaning | "ማሪ — elders, chiefs (?)" — an invented lemma plus a guessed meaning presented first. | → "ማርያን (?) — ማርያን (?) of Egypt (… unidentified — perhaps 'leaders, elders', perhaps a class of priests or diviners) (?)", following the published ውውዓ / ጽግነት / ቤሎንቶስ pattern. |
| ወአፍጠኖ | parse | "the suffix -o is unclear (?)". | → "-ኦ 'him', the object of the following infinitive ሐቲተ" (hedge withdrawn). |
| ለግብጻዊ | grammar | "to/of the Egyptian (ለ- + adjective/noun)" left the syntax of the heading unexplained, where ለ- is the object marker doubling ሐተቶ. | Rewritten to say so. |
| ወማኅፈድ, __broaden__ ወማኅፈደ | meaning | "precinct"/"shrines of the idols" asserted beyond the published 'tower (?)'. | Both aligned: 'tower (?)', with "a building of the idols, a temple tower or precinct" as the hedged contextual sense. Old published text of the broadened entry kept whole before the " · ". |
| ፶፱ | format | "፶፱ — numeral 59 — chapter number · spoken …" uses two em-dashes and is not the shape the recent published parts use for chapter numbers; the transliteration "täsʿätu" also breaks the convention (4th order = a; ch. 49–50 has täsʿatu). | → "፶፱ — 59, spoken ኀምሳ ወተስዐቱ (ḫämsa wä-täsʿatu) 'fifty-nine'; chapter number (numeral)", the shape of ፶፫/፶፬/፶፯ in chs. 53, 54, 57–58. |

### Minor

| entry | field | what was wrong | what was done |
|---|---|---|---|
| ዘለአኮ, ወመልእክቶ | parse | The suffix was called "-ሁ … written ለአኮ / -ቶ"; before these endings the suffix is -ኦ. | Both now give -ኦ with the written form. |
| ወምሉእ | meaning | "and full, of every kind" put a contextual guess into the general entry. | → "and full, filled (ወ- + adjective, passive participle of መልአ 'be full')"; the 'of every kind' reading stays in the unit note with its (?). |
| ይትናገረክሙ | grammar | "Gt reciprocal-stem" overstates; the verb is simply the T-stem of ነገረ used for 'speak'. | → "T-stem of ነገረ 'to tell'". |
| ሰማይኒአ | note | The stray -አ was called a possible scribal addition with no precedent given. | The ch. 36 precedent (ወሀበነአ) is now cited; (?) kept. |

### PASS 2 findings refused

- **Re-lemmatizing ቦአ to በአ** (to match the drafter's notes): refused — ቦአ is the dictionary form; the notes were corrected instead.
- **Broadening `እስከ`** for እስከ ለዓለም 'for ever': refused; the published entry "until, as far as (preposition)" plus the published ለዓለም 'for ever' covers the phrase.
- **Broadening `ለእግዚኣብሔር`** for the anticipatory-possessor use (ታቦተ ሕጉ ለእግዚኣብሔር, ሰብአ ቤቱ ለእግዚኣብሔር): refused; the entry already begins "of/to God".
- **Broadening `ስምዐ`, `ሠሉስ`, `ነፉስ`, `ኀበ`, `እንተ`, `ኮኑ`, `ታቦተ`, `በሰረገላ`**: refused one by one — each published entry already covers this part's use (checked against `known-forms.json`).
- **Flattening ገነውተ to "priests" and ማርያነ to "elders"** without a hedge: refused; Dillmann is not available offline and the conventions require that uncertain words be said to be uncertain.
- **Changing ታድኅነክሙ / ትበውእ / ትሰመዩ**: inspected and found correct (3fs imperfect causative; 3fs imperfect; 2mp T-stem passive) — no change.

---

## Unresolved `(?)` forms and readings after both passes

Carried forward honestly, mostly for want of Dillmann:

1. `ገነውተ` — plural ገነውት (?); singular and dictionary form unknown.
2. `ማርያነ` — ማርያን (?) wholly unidentified; left in Geʿez in `l` and `i`.
3. `ዕንዚራት` — "harps (?)" by the house convention, but ነፍሐ 'blow' fits a wind instrument.
4. `ማኅፈድ` / `ወማኅፈደ` — 'tower (?)'; the contextual "temple tower, precinct" is a guess.
5. `ይግዕዙ` — lemma ገዐዘ (?).
6. `ኣየድዐከ` — parse settled, the printed first-order ኣ- still unexplained (?).
7. `ነፉስ` — the printed spelling of ነፋስ; "of wind, airy" (?) as in chs. 51–52, 55–56, 57–58.
8. `ሰማይኒአ` — the final -አ (?), as ወሀበነአ in ch. 36.
9. `ምሉእ ንዋይ` — "a full store of goods / goods of every kind" (?).
10. `ቃህራ` — Cairo (?).
11. `ተከዚ` beside `ፈለገ ምስር` — the Takkaze standing in Egypt; the Nile (?).
12. Unit 1, the unnamed subject of ወኀለፈ / ወረከበ — Solomon (?).
13. Unit 7, the unnamed addressees of ይቤልዎሙ (?).
14. Unit 8, ተቀጥቀጡ plural beside the singular ማኅፈደ (?).
15. Unit 9, whether ገነውተ አማልክት is the subject or the object of ወሐተቱ (?).
16. Unit 14, the unexpressed subject of ይክል ነሢኦታ ("how could one take her") (?).
17. The two scriptural echoes offered as echoes only: Exodus 25:40 (unit 9), Ephesians 2:19
    (unit 12), Isaiah 42:8 (unit 13) — all marked (?).
