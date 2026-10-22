# Review — kebra-nagast-ch66

## Pass 1

Mechanical checks passed with no change needed: `t` joined equals the packet Geʿez exactly; p flags correct (heading and first body unit only; the packet has two paragraphs); every unit ends at ። ፤ ፨ (unit 4 at 63 words and unit 12 at 47 have no ፤ inside to cut at); every word form is in known-forms or novel-forms. After the fixes, l has one token per Geʿez word in every unit.

Unit numbers are 0-based positions in `sentences` (0 = heading).

| Unit | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| about | about | minor | "psalms" uncapitalised. | Capitalised. |
| 1 | n | minor | ስዉር ነገር read as adjective + noun with no hedge, though ስዉር could be a noun. | Hedged in the note. |
| 3 | n | minor | Note said the saying was "quoted from memory of the sense", i.e. remembered wording stood behind the rendering. | Reworded as an allusion rendered from the Geʿez only. |
| 3 | n | minor | Suffix of አሐንጾ labelled -ዎ; after a consonant it is -o (-ዎ is the form after the vowel, as in ንሥትዎ). | Corrected the label. |
| 4 | l | moderate | ዘአልቦ glossed as two l-tokens ("in-whom not-is"), shifting every later token against the words; ዘ- is "which" in the house entry (ዘአልቦ "which has not"). | One token, "which-not-is". |
| 4 | l | minor | እንዘ ይብል (two words) merged into one token "saying", against the word-by-word rule; known entries: እንዘ "while", ይብል "he says". | Two tokens "while he-says". |
| 4 | l | major | ዐውዳ parsed as a 3mp verb "they surround it" (ዐወደ + -ሃ). A 3mp perfect + -ሃ would not look like ዐውዳ, and the published entry for ዐውዳ is the noun ዐውድ + -ሃ, "around her" (preposition). | Follows the published entry: "around-it". |
| 4 | n | major | Note labelled ዐውዳ a verb ዐውደ + suffix. | Relabelled as noun + suffix used as preposition. |
| 4 | n | moderate | Note and l said "in whom" (singular antecedent) but i said "among whom", making the plural believers the antecedent. | Note states the antecedent; i fixed to match (see i). |
| 4 | n | minor | i "took many wives" departs from l "multiplied women" without saying so. | Note now says the English is idiomatic. |
| 4 | n | moderate | "-ሎ" taken as "his" (it is "to him"); አፍቅሮ called an accusative verbal noun though the form is the infinitive; the published entry reads it as imperative + him, not reconciled. | Rewritten with the correct labels and the clash with the published entry stated. |
| 4 | n | moderate | "Thigh" came from remembered Song text, not the word, and i stated it without (?). | Note says so; (?) added in i. |
| 4 | i | minor | "through ... of them": በእንተ is "because of" and nothing in the Geʿez gives "of them"; the obscure ወበአምስሎ clause had no (?) in i. | "because of beauty and loveliness", (?) on the obscure clause. |
| 4 | i | moderate | "among whom" makes the plural believers the antecedent; ዘ is singular and follows ቦቱ "in him". Also the "neither ... nor" pairing re-cut the Geʿez, which repeats ወአልቦ before ቈላፈ, አረማዌ, ገብረ and ነባሬ with ወ- only before አይሁዳዌ and አግዓዜ. | "in whom there is no ..." with the printed grouping. |
| 4 | i | major | "surround it" (wrong parse of ዐውዳ); "thigh" unmarked; "60" in digits against the "Sixty" of the next unit; ያነብር "he places" turned into "with a sword at". | Rewritten: "are around it", "placing ... (?)", "sixty". |
| 5 | n | moderate | "Broken plurals in -ት" is a mislabel: these are -āt/-ān suffix plurals, none is a broken plural in -ት. | Relabelled; the alternative reading of ጻድቃን added. |
| 5 | i | minor | Note says the verb የአብይዎ is uncertain (?); i did not. | (?) added. |
| 6 | l | minor | "the-scriptures": the article is not in the Geʿez and the known entry is "books". | "books". |
| 6 | i | moderate | "rightly cuts" sits too close to remembered English (the note cites 2 Timothy 2:15); ዘርቱዕ "which (is) right/straight" is not plainly an adverb. | Rebuilt from the grammar, (?) added. |
| 6 | n | moderate | Note justified "rightly" from a remembered English phrase. | Reworded; adverb/adjective left open. |
| 6 | n | minor | Echo of Song of Songs 3:8 stated flatly from memory. | Hedged. |
| 7 | l | minor | ምስካብ is "bed, couch" in a published entry; the unit also has ዐራት "bed", so "resting place" breaks house usage. | "couch-his". |
| 7 | i | minor | "its" against l "his" (-ሁ); "resting place" (see l). | "his couch". |
| 7 | n | minor | "Construct form ... with -ተ" is garbled: ዐራት already ends in ት; the construct is marked by the vowel. | Corrected. |
| 7 | n | minor | Followed the l change. | Note updated. |
| 7 | n | minor | i "as" for በ- unexplained. | Explained. |
| 8 | l | minor | እንዘ ይብል merged into one token (word count 8 against 9). | Two tokens. |
| 8 | i | minor | መጾረ is flagged (?) in the note but not in i. | (?) added. |
| 10 | i | moderate | i opens "For", but the note itself says the sentence has no እስመ or ወ and is a plain restatement. | "For" removed. |
| 11 | i | moderate | "liken it to the word of David" leaves "it" without an antecedent: ለ- on ለቃለ ዳዊት marks the object doubled by -ዎ (the house pattern, and the note’s own reading of the same construction in unit 15). | "liken the word of David". |
| 11 | n | moderate | Note labelled the ለ- of ለቃለ ዳዊት "to", contradicting its own label of the same construction in unit 15. | Relabelled. |
| 12 | l | minor | ሀቦ is imperative + -ኦ "him" (published entry); l dropped the suffix. | "give-him". |
| 12 | i | major | (1) l has "follow(?)" for ይድኅርዎ but i has "(praise?)", a word that comes from remembered Psalm wording, not from the verb; the note admits Psalm 72:15 as its source. (2) -ኒ "also" on ለነዳያኒከኒ dropped. (3) "he shall sprout" against l "it-shall-sprout". (4) ምስማከ unmarked in i. | "follow (?)" (the verb as it stands); "also"; "it"; (?) on "support". |
| 12 | n | major | Note rested the guess for ይድኅርዎ on the English Psalter; ምስማከ was explained from the Psalm text, not the word, and contradicted the published entry unmentioned; ወየሐዩ, ዘልፈ, አሚረ and comparative እም- were unexplained. | Rewritten; missing labels added. |
| 13 | l | minor | መልከ ጼዴቅ is two words but one l-token (14 tokens for 15 words). | Two tokens. |
| 13 | i | moderate | "priest for ever" drops the suffix -ሁ of ካህኑ (l says "priest-his") and fixes ለዓለም as "for ever" though the house entry also has ለዓለም as the owner after an anticipating suffix; "in the order of" reads as remembered English where በከመ is "according to". | "his priest ... (?)", "according to". |
| 13 | n | moderate | "Probably the priest" has no grammatical basis (-ሁ is the possessive). | Rewritten with the real ambiguity. |
| 13 | n | minor | Verb given as ነሥሐ/ነስሐ; the published entry is ነስሐ. | House spelling. |
| 13 | n | minor | Name split not explained. | Added. |
| 14 | l | minor | ወዘይመስሎ is one word, two l-tokens. | One token. |
| 14 | l | minor | ዘተነበየ one word, two tokens. | One token. |
| 14 | l | minor | ውስተ ርእሰ two words in one token. | Two tokens. |
| 14 | l | minor | ዘተናገረ one word, two tokens. | One token. |
| 14 | i | moderate | "of whom he spoke" turns ዘተናገረ (relative "which/what he spoke") into a relative on Solomon, against l "which he-spoke". | Rebuilt as direct speech with "in what he spoke". |
| 14 | n | minor | Note did not label the suffix of ይመስሎ and explained the loose end only vaguely. | Added. |
| 15 | l | moderate | l had a placeholder "in-.." for በመኵሴ; ለ- of ለክርስቶስ left unmarked against the house "to-" convention; በ- of በሰሎሞን labelled "to" (it is "in/with"). | Geʿez word kept in l; "to-Christ", "with-Solomon". |
| 15 | i | minor | Note says "in name" is not a lexical result (?); i did not. | (?) added. |
| 15 | n | minor | በሰሎሞን explained as "to". | Clarified. |
| 16 | l | minor | ለአይሁድ rendered "the-Jews", dropping the object-marking ለ- (cf. unit 3 "to-Jews"). | "to-Jews". |
| 16 | i | minor | Note flags ጸራ ለጽድቅ (?); i did not. | (?) added. |
| 16 | n | minor | Claimed an "Ethiopian tradition" on no ground in the packet. | Limited to what the text says. |
| 17 | i | moderate | "he was a king, the son of David, a king and prophet; he too was ..." says the same of Solomon twice; the Geʿez has "king" for Solomon, "king and prophet" after ዳዊት, then ወለሊሁኒ "and himself also". | Reordered so the first "king and prophet" belongs to David (ambiguity noted). |
| 17 | n | moderate | Structure of the opening not explained. | Added. |
| 17 | n | moderate | አምሳለ labelled "plural in the accusative"; it is the singular (published entry: construct/accusative). | Relabelled. |
| 17 | n | minor | Outside claim stated without hedge. | Hedged. |

Totals: 5 major, 18 moderate, 32 minor (55 changes).

## Findings refused

- Unit 12 note, "Psalm 72, verses 1-2 and 10-17": the span may be 15-17 (with 10-14 skipped), but checking needs the Psalter text, which I do not consult. Left; the note already says verses are skipped.
- Unit 5 i, "the faithful" for ወመሀይምናን against "believers" in l and the published entry: both are fair renderings of one word; left.
- Unit 4 length (63 words, no ፤ inside) and unit 12 (47 words): conventions allow no cut without a ፤; left whole.
- Unit 17 note on the four books (Proverbs, Ecclesiastes, Song of Songs, Wisdom): outside the text; kept but hedged (see table).
- Gloss entries: not reviewed here (no gloss.json yet). Pass to the glosser: ዐውዳ should broaden to the unit-4 use; ምስማከ should become "support (?)"; አፍቅሮ is also the infinitive; ያነብር, ሀሎ, ካህኑ ለዓለም, ዘአልቦ and አምሳለ have new uses.

## Unresolved (Dillmann unavailable)

ሐለየ, መጾረ, መንቅዕቱ, ወበአምስሎ, ያልይ, የአብይዎ, ይድኅርዎ, ምስማከ, መኵሴ, ጸራ ለጽድቅ, ካህኑ ለዓለም (his priest for ever or priest of the world), the grouping of ወልደ ዳዊት ንጉሥ ወነቢይ in unit 17, and ንሥትዎ (unit 3). All are hedged (?) in the notes and, now, in i.

## Pass 2

Checked: every gloss entry against every occurrence of its form (lemma, meaning, parse); all 8 `__broaden__` entries start with the known-forms entry reproduced exactly plus ' · '; every novel form is glossed; units re-checked (t joined equals the packet, 331 words, l one token per word in all 18 units, p flags, unit endings). Unit numbers 0-based.

| Item | Severity | What was wrong | What done |
|---|---|---|---|
| gloss ቈላፈ | moderate | Lemma ቈላፊ, but the form is an accusative in -ä (ቈላፊ would give ቈላፌ, like አረማዌ). | Lemma ቈላፍ, accusative stated, lemma hedged (?). |
| gloss በኆልቈ | minor | Lemma was the construct ኆልቈ, not the dictionary form. | Lemma ኆልቍ, construct noted. |
| gloss ለክርስቶስ | moderate | Only the possessor use (unit 7); unit 15 uses it as the object of ወያመስልዎ. | Second reading added. |
| gloss ጸራ (+ unit 16 n) | moderate | "plural/accusative ጸራ" is not a plain accusative (that would be ጸረ). | Parse hedged (?) in both. |
| gloss ለያልይ | minor | Called ሐለየ 'dream'; ሐለየ is 'meditate', 'dream' is ሐለመ. | Corrected. |
| gloss አረማዌ, ወአይሁዳዌ, ነባሬ, ወአግዓዜ | minor | Accusative (after አልቦ) not stated; the -ዌ/-ሬ/-ዜ endings are accusatives of -ī nouns. | Added. |
| gloss መንቅዕቱ (+ unit 4 n) | minor | -ቱ does not fit መንቅዕ + -ሁ (cf. ዐራቱ, ሢመቱ from nouns in -ት). | Lemma flagged uncertain (?) in both. |
| gloss ሥኖን | minor | Ending -ኖን unexplained. | Said so (?). |
| gloss እኁዛነ | minor | Plain "participle"; the pattern is the passive-form participle (as ቡሩክ). | Relabelled. |
| gloss መጾረ | minor | Accusative (object of ገብረ) not stated. | Added. |
| gloss ወልዲ | minor | Suffix labelled -ዪ; the ending is -ዲ, i.e. -ī. | Corrected. |
| gloss ለአይሁድ | minor | Unit 16 use (object of ያስተኀፍርዎሙ) missing. | Added. |
| unit 1 n | minor | ብሂል called verbal noun of ይቤ; the verb is ብህለ (known entry). | Corrected. |
| broaden ምስማከ | minor | Project jargon ("the corpus glosses") in a popup. | Reworded; old entry intact. |
| broaden ገብረ (new) | minor | Known entry has 'servant' in the construct; unit 4 uses it as accusative 'slave' after አልቦ. | Added. |
| broaden ፀብአ (new) | minor | Known entry only accusative; unit 5 has 'war of Satan'. | Added (?). |
| broaden ለወልደ (new) | minor | Known entry says ለ- marks the object; unit 12 is dative 'to the son of'. | Added. |
| broaden ለጽድቅ (new) | minor | Known entry explains ለ- by a preceding suffix; unit 16 has none. | Added (?). |

Totals: 0 major, 4 moderate, 13 minor (17 changes). Nothing found in units.json beyond the three note fixes.

Refused: ነሠተ for ንሥትዎ, ላሕይ, አምሳል for ወበአምስሎ, አበየ for የአብይዎ, መላጼ, በሊኅ, መኵሴ (no Dillmann; already hedged (?), no better lemma available). ሰማዕት as plural (hedged). ፍካሬ 'construct' left. Pass 1 refusals stand.

Unresolved: the lexical items above, ሐለየ, ያልይ, ካህኑ ለዓለም, ንጉሥ ወነቢይ grouping in unit 17.
