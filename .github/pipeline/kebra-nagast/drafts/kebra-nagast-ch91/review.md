# Review, kebra-nagast-ch91

## Pass 1

Checked: `t` joined against the packet (identical after whitespace normalisation, 36 units, `t` and every `p` flag untouched, verified against a copy taken before the edits; `p: true` on units 0 and 1 only, matching the heading and the one body paragraph; unit 11 has 40 words, unit 12 36, unit 6 31, all under ~45, and no unit has an inner ፤ left to cut at); every grammatical label in every note against the form; original to `l` word by word; `l` to `i`; remembered English in `i` and notes; consistency with known-forms.json, conventions.md and the published parts (searched by form in all kebra-nagast-ch*.json: chs. 13-16, 21-22, 24, 25-26, 27, 35, 37, 51-52, 54, 60a, 60b, 61, 80, 81, 87, 89, 90); the house renderings of ch. 89-90 (አእምሮ 'knowledge', ልቡና 'understanding', (?) in both `l` and `i` for uncertain words). Dillmann and Budge are not available, so lexical calls stay hedged with (?). Edits by script to `l`/`i`/`n`/`about` only (json, ensure_ascii=False, indent 1). Unit numbers are 0-based positions in units.json.

### Changes

| Unit | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 4 | l, i, n | major | `i` gave ዝእብ as 'the pig' (and the note guessed 'wild boar' for ሐራዊያ). ዝእብ is the ordinary word for wolf or hyena; the pig is an inference from the cloven-hoof-no-cud reasoning, and `i` hid a different animal behind one (?). | `i` 'the wolf (?) or the ḥarawiya (?)'; note says the reasoning points to the pig of Leviticus 11:7 (?) but `i` gives what the form says; 'boar' dropped; `l` ḥarawiya. |
| 11 | l, i, n | moderate | ዘይትማሰላ ለኅሊናኪ: the note said ለ- 'marks what is matched' and glosser later calls -ላ irregular. It is ይትማሰል + the object suffix -ኣ ('it', ል + ኣ written ላ) doubled by ለኅሊናኪ, as ወደሳ ለንግሥት in ch. 90. `l` lacked 'it'. | `l` 'who-resembles-it'; note gives the parse and the cross-reference; `i` 'no one who matches your mind' (the 'nothing' was not in ዘ-). |
| 11 | l, i, n | moderate | አኮ ምክረ አንስት ባሕቱ ዘተፈጥረ ... rendered 'nor of anything made': ባሕቱ is 'but', not 'nor', and the note's (?) did not reach `l`/`i`. | `i` 'It is not the counsel of women, but (that of) whatever has been created until now (?); rather ...'; (?) in `l`; note gives the reading and why 'nor' was refused. |
| 12 | i | moderate | `i` 'cords of your understanding (?)' for አእምሮትኪ, against the house pair (አእምሮ 'knowledge', ልቡና 'understanding') and against `l` 'knowledge'. | 'cords of your knowledge'. |
| 10 | l, i, n | moderate | ተመነኑ 'were bereft (?)' / 'made poor': the published parts read ተመነነ as 'rejected, scorned' (chs. 21-22) and 'despised' (ch. 60a); 'bereft' has no support. | 'were rejected (?)' in `l`, `i`, note (citing chs. 21-22, 60a). |
| 16 | l, i, n | moderate | ሰገል rendered 'soothsayers' (a person); chs. 60b, 61, 87 have 'sorcery, divination (?)'. አስተቃስሞ ('consult for omens') and አስምኮ ('trust') were unflagged in `l`/`i` though the note says (?); ch. 89 ties ወቀስመ and ch. 60b መቃስም to ቀሰመ 'divine', and ch. 24 ኣሰምክ to ሰምከ 'lean'. | `l`/`i`: 'seeking divination (?), sorcery (?)' and 'lean on (?)'; note rewritten with those links and 'a title found in Isaiah' for ቅዱሰ እስራኤል. |
| 21 | l, i, n | moderate | ተጸወንኪያ 'took her up / bore her' from a supposed ጸወነ 'carry'. The published parts have ጸወነ 'find protection, shelter' (ch. 24, in the same wisdom chain) and ተጸወነ 'hid, took cover' (ch. 81). ጥቅመ 'gain' also dropped the (?) and the known 'help, benefit'. | 'took shelter in her (?)', 'a help to you (?)'; note cites chs. 24, 81, 54. |
| 34 | l, i | moderate | ወመኪረ 'giving good counsel' unflagged in `l`/`i` though uncertain (the form is not ምክር). | (?) in `l` and `i`. |
| 2 | l, i, n | minor | ቶራ left as 'tora' though ቶር 'wild ox' is published (ch. 35, ቶራት; ch. 25-26 'wild ox or antelope, uncertain'); the note quoted the English animal list of Deuteronomy; `l` had 'harge' (ሐ = ḥ); ወይጠል and ውዕላ both read 'ibex' without comment. | `l`/`i` 'wild ox (?)'; ḥärge; note drops the English list, cites ቶር, and says ውዕላ is kept untranslated because ibex stands for ይጠል. |
| 3 | l, i | minor | ዳሲጳዳ, ካርግልዮን (?) in `i` and note, not in `l`; 'you shall not eat'. | (?) added in `l`; 'you must not eat'. |
| 5 | n | minor | 'accusative -ኧ': not a house label. | 'accusative (ending -ä)'. |
| 6 | i | minor | 'glauqa' against `l` and the Geʿez ግላውቃ; 'shall not'. | 'glawqa'; 'must not'. |
| 7 | l, i, n | minor | (?) on ደገብያ, አቃጣን missing in `l`, on አፍዮማክን in `l` and `i`; the note said the Septuagint names are bruchos ... while also saying ደገብያ cannot be placed; 'shall not'. | (?) added; note says the Septuagint list has those names; 'must not'. |
| 9 | n | minor | 'heavenly because she is the earthly copy of a heavenly thing' stated as fact. | Hedged as my reading (?). |
| 10 | i, n | minor | ዘነሥኦሙ 'took Zion from them' with no (?) though the note leaves 'from them' open; 'the Israelites at Jerusalem' as fact. | (?) in `i`; 'as I take it'. |
| 11 | n | minor | 'as in ch. 90 (my lord, the king)' made Solomon's exception parallel to ch. 90, where the exception is the king. | 'compare ch. 90, where the exception is my lord the king'. |
| 12 | n | minor | ብሂል after አኮ ከመዝ unexplained. | Added: verbal noun of ይቤ, 'that is'. |
| 15 | l, i, n | minor | `i` 'mārit' (macron not house); ይኄይስ called '3ms of ኄሰ' (the lemma is ኀየሰ, chs. 13-16 and the known entry); 'for variety' unsupported; ሐቲተ said to take ማሪት 'as object' where ch. 60b has the pair as 'inquiry of ...'. | 'marit'; ኀየሰ; sentence on ይረትዕ/ይኄይስ made factual; ሐቲተ 'accusative or construct'. |
| 17 | l, i, n | minor | ለአዕዋም 'trees' is (?) in the known entry but not in `l`/`i`; the note quoted remembered English of Jeremiah 2:27. | (?) added; note paraphrases and adds Deuteronomy 4:28 'gods of wood and stone'. |
| 18 | i, n | minor | ተጠይሮ 'omens from birds' unflagged in `i`; the note's ተአምነ against the glossary lemma ተአመነ; ch. 60b/89 treatment not mentioned. | (?) in `i`; ተአመነ; cross-reference. |
| 19 | n | minor | Quoted remembered English of Sirach 15:2. | Paraphrased. |
| 22 | n | minor | ጸህቂያ spelling (ህ for ሐ; ቅ + ኪ run together) not remarked. | Added with ch. 37 and (?). |
| 23 | n | minor | Quoted remembered English of Proverbs 4:8. | Paraphrased. |
| 25 | l, n | minor | `l` 'she-will-leave-you' (future) against the imperfect of the form and the note; the ተ- prefix called 'the prefix of the imperfect' without saying it is spelled ተ- for ት- (ch. 24 ተሐቅፈኒ). | `l` 'leaves'; note says so and cites ch. 24. |
| 27 | l, i | minor | አጥዐየተኪ 'sweetened/made sweet': the note says the figure is uncertain (?). | (?) added. |
| 30 | l, i | minor | ተመንደብኪ 'afflicted' unflagged though the note has (?). | (?) added. |
| 31 | n | minor | ጸመመ 'be deaf' marked (?) here, but ch. 54 gives it unhedged. | (?) removed, ch. 54 cited. |
| 32 | n, i | minor | ዖርኪ 'read as ዖረ (?)': ዖረ is the 3ms of ዐወረ 'be blind' (ch. 80 አዖረ), no doubt about the form; `i` 'for ever more than the sun' lost ፈድፋደ. | Note corrected; `i` 'far more brightly than the sun, for ever'. |
| 33 | n | minor | Quoted remembered English of Sirach 1:1. | Paraphrased. |
| 34 | i | minor | 'which endure' (plural) for the feminine singular እንተ ትሄሉ. | 'which exists (?)'. |
| 35 | n | minor | ቀዋሚሃ / መጋቢሃ both glossed 'her ...' while the note says -ሃ anticipates ደብተራ; `i` leaves 'her' out. | Note says -ሃ anticipates the noun (as in ch. 25-26) or perhaps Zion (?), and why `i` omits it. |
| about | about | minor | States Menelik as fact; the unit note carries (?). | 'as I read it'. |

### Findings refused

1. Unit 0 `i` 'On what may be eaten': a heading, matches the earlier heading form. Refused.
2. Unit 2 `i` 'the kid or gazelle' for ጠሊ (house: 'kid, young goat'): the Deuteronomy list makes 'gazelle' possible; both are given. Refused.
3. Unit 2 ሐርጌ, ዓርጋ, ድስክነ, ዝራት: cannot be improved without Dillmann; hedged. Refused.
4. Unit 3 ዳሲጳዳ 'hare', ካርግልዮን 'coney': the Septuagint equations (dasypous, choirogryllios) are sound and hedged. Refused.
5. Units 6-7 Greek bird and locust names: each is flagged (?) in the note and `i`; I cannot do better. Refused.
6. Unit 5 `i` 'among them' for ወእምኔሁ ('from it'): the antecedent is ማይ, collective sense; the note shows the Geʿez. Refused.
7. Unit 8 ዘይሰርር 'creeps' (?): the known entry has 'flies' and 'speeds'; the note hedges. Refused.
8. Unit 9 ንጹሕ/ርኩስ, ፍርሀተ 'practise the fear of God': 'practise' is the plain rendering of ወትግበሩ. Refused.
9. Unit 11 ዘትትመሐፀኑ 'put your trust in (?)': fits ch. 51-52 'take refuge'. Refused.
10. Unit 13 `i` 'This is not good': drops 'thus' (ከመዝ); the note shows the Geʿez and later units carry 'thus' in `l`. Refused.
11. Unit 26 አስተፍሥሐተኪ 'causative-tä stem': the label means the ʾastä- stem, as in ch. 90 pass 2. Refused.
12. Unit 27 አጥዐየተኪ from ጥዕየ 'be sweet': no better candidate. Refused, hedged.
13. Unit 35 ዳዊት = Menelik: carried by ch. 87-90 and the known entry; the note already gives (?). Refused.
14. Unit 12 `i` 'cords' for አሕባል: published as 'cords' in the known entry. Refused.

### Outside units.json (for the second pass)

All handled in pass 2 below: ዘይትማሰላ parse; ፈሪሀ lemma (ch. 27 ፈሪህ); ተመነነ sense; ሰገል and አስተቃስሞ, አስምኮ; ተጸወነ; ዖረ / ዐወረ; አንጽሐ root; ወይባርክ jussive (needs a broadening).

### Counts (pass 1)

major 1, moderate 7, minor 24 (32 table rows; some rows cover several fields or words); refused findings: 14.

## Pass 2

Checked: all 153 novel entries and the 14 broadenings in gloss.json against the edited units' `t`/`l`/`i`/`n` (lemma is the dictionary form; person, number, gender, stem; suffix labels; proclitics; meaning against `i`; Geʿez quoted inside entries); coverage (303 distinct word forms in the part: every one is in gloss.json or known-forms.json, none in both, none stray; the 153 novel keys all kept); lemma spellings and senses searched by lemma in all published kebra-nagast glossaries. No 'dual' appears anywhere; every 2fs verb is said to the Queen and carries -ኪ; the suffix labels -ኣ/-ኦ/-ዎ/-ኖ/-ሙ/-ሁ check against the forms (including the new ዘይትማሰላ = ይትማሰል + -ኣ). The glosser's three flagged inferences: ወውዕላ→ወዕል accepted, with the extra hedge on the final -ኣ (it is a plausible lemma, ወዕል 'ibex', not in the published parts; ወ + ወዕላ run together); ፈሪሀ→ፍርሀት rejected (ch. 27 already has ፈሪሀ as the construct of ፈሪህ 'fear', and the published lemma is ፈሪህ); ወመኪረ→መከረ kept as lemma but marked (?) with 'counsellor' named as the other possibility. Edits by script (json, ensure_ascii=False, indent 1); 153 novel keys, valid JSON.

### Changes

| Item | Severity | What was wrong | What was done |
|---|---|---|---|
| gloss ፺፩ | moderate | The part before ' — ' was 'spoken ተስዓ ወአሐዱ ...', so the lemma shown in the popup was not the numeral; published form is '፳፩ — 21, spoken ... ; chapter number (numeral)' (also ʾ in ʾäḥädu). | '፺፩ — 91, spoken ተስዓ ወአሐዱ (täsʿa wä-ʾäḥädu) ''ninety-one''; chapter number (numeral)'. |
| gloss ዘይትማሰላ | moderate | 'the ending -ላ is irregular (?)': it is ይትማሰል + -ኣ '3fs it' (ል + ኣ written ላ), doubled by ለኅሊናኪ. | Parse rewritten. |
| gloss ተመነኑ | moderate | 'bereft, made poor': no support; chs. 21-22, 60a have 'rejected, scorned / despised'. | 'rejected, scorned (?)', sense cited. |
| gloss ሰገል | moderate | 'soothsayer, diviner (collective)': a person; chs. 60b, 61, 87 have 'sorcery, divination (?)'. | Replaced. |
| gloss አስተቃስሞ | moderate | 'consulting omens ... root uncertain': ch. 89 and ch. 60b tie ቀሰመ / መቃስም to 'divine'. | 'seeking divination (?)', perhaps ʾastä- stem of ቀሰመ. |
| gloss አስምኮ | moderate | lemma አስምከ, 'relying, taking refuge' with no source; ch. 24 and later parts have the ʾa-stem አሰመከ beside ሰምከ 'lean'. | Lemma አሰመከ, 'leaning on, relying (?)'. |
| gloss ተጸወንኪያ | moderate | 'took her up, bore her' from ጸወነ 'carry, bear'; the published sense is 'shelter, protect' (ch. 24), ተጸወነ 'hid' (ch. 81). | 'you took shelter in her (?)'. |
| gloss ፈሪሀ | moderate | lemma ፍርሀት (glosser's own inference); ch. 27 has the construct ፈሪሀ of ፈሪህ 'fear'. | Lemma ፈሪህ, ch. 27 cited, related to ፍርሀት. |
| gloss ቶራ | moderate | 'unidentified animal': ቶር 'wild ox, bull' is published (ቶራት, ch. 35; ch. 25-26 'wild ox or antelope'). | Lemma ቶር, 'wild ox, or an antelope (?)'. |
| gloss ወአንጻሕኪ | moderate | 'causative of ጽሕ': no such root; the verb is the ʾa-stem of ንጽሐ (cf. ንጹሕ). | Corrected. |
| gloss ዖርኪ | moderate | lemma ዖረ, sense (?): ዖረ is the 3ms of ዐወረ 'be blind' (ch. 80 አዖረ 'blinded'), published unhedged. | Lemma ዐወረ; (?) removed. |
| gloss ወመኪረ | moderate | 'verbal noun, accusative, of መከረ' stated flatly; the form is not ምክር. | Marked (?), 'counsellor' named as the alternative. |
| broaden ወይባርክ (new) | moderate | Known entry 'and he will bless'; unit 11 needs 'and may he bless' (jussive, written alike), which the note says. | Old entry whole + ' · and may he bless (jussive ...)'. |
| gloss ወውዕላ | minor | Parse unexplained; the glosser's reading needs a hedge. | 'ወ- + ወዕል with a final -ኣ (accusative or collective) (?)'. |
| gloss አሰሰልኪ | minor | 'quadriliteral' asserted. | 'perhaps the ʾa-stem of ሰሰለ (chs. 24, 61) rather than a quadriliteral (?)'. |
| gloss ወነሠትኪ | minor | Sense 'tore down' with no tie to the published ነሠተ 'take away, seize'. | Tie added. |
| gloss ጸህቂያ | minor | Spelling (ህ for ሐ, ቅኪ run together) unremarked. | Added with ch. 37. |
| gloss ወኢተኀድገኪ | minor | 'imperfect' without saying ተ- stands for ት-; `i` puts it in the past. | Added (ch. 24 ተሐቅፈኒ). |
| gloss ጸመምኪ | minor | (?) although ch. 54 gives ጸመመ 'be deaf' without one. | (?) removed, ch. 54 cited. |
| gloss ማእመሬ | minor | Root not given. | 'agent noun of አእመረ'. |
| gloss ወበበ፮ | minor | 'sədsətu' against the published 'sədstu' (ch. 23). | Aligned. |
| broaden ወይጠል (new) | minor | Known entry says ወ is part of the word; here the list joins groups with ወ-, so ወ- + ይጠል is possible (as the unit 2 note says). | Old entry whole + ' · ... (?)'. |

### Findings refused (with reasons)

1. ወጠሊ 'kid, gazelle': house is 'kid, young goat', but `i` carries both and the Levitical list allows 'gazelle'. Left.
2. ወዝራት 'perhaps the giraffe (Hebrew zemer)': hedged. Left.
3. Greek-derived bird and locust entries (ጊጳ, ኤልያጣን, ግሪጳ, ግላውቃ, ለሮን, አሮድዮን, ኢብን, ቀጣራቃጤን, ሂጳጳ, ክራድዮን, ጳርፋርዮና, አፍዮማክን, አቃጣን, ቃቃኖን): the equations are standard Septuagint ones and hedged where doubtful. Left.
4. ዘነሥኦሙ, ዘትትመሐፀኑ, ወትርጒምናሁ, ተጠይሮ (broadening): each states its own doubt. Left.
5. ተአምኖ lemma ተአመነ against ተአምነ (ch. 13-16): both are published; this follows ch. 51-52. Left.
6. ተኀረይክሙ lemma ተኀርየ: matches ch. 87. Left.
7. ቀዋሚሃ, መጋቢሃ, ለደብተራሁ, ዳዊት (known): known entries; the Menelik reading is already carried. Left.
8. ዘቦ, ዘንተኬ, ዘአፍቀርኪያ, ወአበዊነሰ, ወዘኒ and other regular forms: person, number, stem and suffix checked, no change.
9. The source-slip entries አ, መ, ምሳሊሆሙ, በከ: correct as printed. Left.
10. The Septuagint etymologies ዳሲጳዳ and ካርግልዮን: hedged. Left.

### Counts (pass 2)

major 0, moderate 13, minor 9 (22 table rows); findings refused: 10 (groups).

### Remaining cruxes

ዝእብ / ሐራዊያ (wolf or pig, and the unplaced ሐራዊያ); the animal names ሐርጌ, ቶራ, ድስክነ, ዓርጋ, ዝራት, ወውዕላ and the ይጠል / ወ- question; the bird and locust names; ማሪት; ተጠይሮ ('augury'); አስተቃስሞ / ሰገል / አስምኮ; ተጸወነ ('took shelter'); ተመነኑ ('rejected'); ዘትትመሐፀኑ; ዘነሥኦሙ ('from them'); ወመኪረ; ዘተፈጥረ ... ባሕቱ reading in unit 11; ጸህቂያ spelling; ኢተኀድገኪ tense; ዳዊት as Menelik; ተመንደብኪ.
