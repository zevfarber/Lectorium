# Review — kebra-nagast-ch35 (Kebra Nagast ch. 35)

Reviewer, two passes. Pass 1 on `units.json` (every grammatical label against the form, original -> `l` word by word, `l` <-> `i`, remembered English, consistency with ch. 31-34 and conventions.md). Pass 2 on `gloss.json` (every lemma and parse against the text; the 187 novel keys all present, lemma before " — " the dictionary form, `__broaden__` entries start with the old entry whole). `t` was not touched: the joined `t` still equals the packet (checked by script). No modern translation consulted.

## Counts
- Pass 1 (units.json): major 3 · moderate 15 · minor 19 (total 37)
- Pass 2 (gloss.json): major 1 · moderate 12 · minor 8 (total 21)

## Decisions on the named concerns
- **ለበይነ ልሕክም**: a personal name, Bäyna-Ləḥkəm, with dative ለ-. Grammar and context: after ወይቤሎ the addressee must follow; as a preposition ('on account of') ለበይነ would leave ልሕክም dangling and the verb without an addressee, and Joash then says እግዚእየ 'my lord' to the boy. Same name as ch. 31-32 (ልሕክም is already a published entry). units.json (l, i, note) and gloss.json now agree; the (?) on the identification was removed, the open etymology stays as in ch. 31-32.
- **ከናኦን vs Cush**: kept Canaan (the text, Genesis 9:25-27 / ch. 12 of the published parts spell the same name ከናኣን). Not Cush. The draft's note already says so. What I did change is the -ዎ of ወወሀብዎ: it is masculine, so 'they gave him (Canaan) his portion', not 'gave it (the country)'.
- **እግዚኡ ለእግዚእየ**: the grammar (anticipatory suffix + ለ- genitive: 'the lord of my lord') is right in l; who is meant is genuinely open (David in apposition, or the boy). Left both in the note, (?) added to i; the draft's stated reason for choosing was a non sequitur and was replaced.
- **ኣ-initial verbs** (ኣአኵቶ, ኣምጽእከ, ኣመጽኦ): ኣ- is Bezold's regular print of the 1cs prefix (ch. 24 ኣፈቅራ/ኣሰምክ, ch. 25-26 ኣአኵቶ, ch. 28 ኣአምር, ch. 9-12 ኣወርድ), not an irregularity. ኣመጽኦ lacks the ም of A-stem ኣምጽኦ (noted as a print slip). ኣአኵቶ: l fixed (-ኦ is 'him', not 'to-him').
- **ዘያሰምክ ዲበ እዴሁ**: reading kept ('who leans upon his hand', already marked (?)), consistent with ch. 24 ኣሰምክ 'I lean (?)'. Note rewritten: A-stem used intransitively, with the alternative (causative: 'on whose hand he leans') stated.

## Pass 1 — changes (units.json)
| unit / key | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| unit 1 | n | moderate | note called ያሰምክ 'causative' and then glossed it as a plain non-causative 'rests/leans'; the two statements contradict, and the two possible referents of 'his' were not told. | rewrote the note: A-stem, intransitive as in ch. 24, both referents stated, marked (?). l and i (already (?)) unchanged. |
| unit 2 | i | minor | i 'carriages' for ሰረገላት, but l and the glossary say 'chariots' (Dillmann currus). | i -> 'chariots'. |
| unit 3 | i | moderate | i dropped the negation of ወኢእመ ('and if not') into a plain 'or whether' and added 'at any rate', which is in neither the Geʿez nor l. | i: 'whether you are his son or, if not, his brother (?)'; 'at any rate' removed. |
| unit 3 | n | minor | note leaked workflow ('already glossed'). | reworded. |
| unit 3 | n | minor | note's own rendering again lost the ኢ- of ወኢእመ. | matched the new i. |
| unit 3 | n | minor | -ከ here is the 2ms perfect ending of ኮነ, not an object suffix; the gloss.json entry had it right, the note did not. | note corrected. |
| unit 4 | n | minor | mislabelled the ለ- of ይቤለኒ as '-ሎ-'. | corrected. |
| unit 4 | n | moderate | note said the ወ falls only before the last noun; the Geʿez has ወ before ዕረፍት, ተድላ and ሐሤት (the gloss keys ወበዕረፍት, ወበተድላ confirm it). | note corrected to the actual distribution. |
| unit 5 | l | moderate | l put 'to-him' on the -ኦ of ኣአኵቶ, but -ኦ is the accusative 'him' (አኰተ is transitive; the ለ- belongs to God); published ch. 25-26 has 'I-thank-him' and the same gloss. | l -> 'I-thank-him to-God'. |
| unit 5 | n | minor | note called the ኣ- 'irregular' and reserved it (?), though published parts (ch. 24, 25-26, 28) use and gloss the same ኣ- as the 1cs prefix, even this very word. | note rewritten to the house reading. |
| unit 6 | n | minor | note's lemma ሰፈወ disagrees with the gloss.json lemma ሴፈወ. | note aligned to ሴፈወ. |
| unit 6 | i | minor | 'wait on' means 'serve'; l has 'I-wait-for-him' and the verb is ሴፈወ 'hope for, await'. | i -> 'wait for'. |
| unit 7 | n | moderate | the name/preposition question was left half-open: the note flagged 'the identification (?)' although the grammar and context decide it, and the gloss entry hedged too. units.json (name) and gloss.json (name, but marked (?)) were close but the reasoning was missing and the (?) wrongly suggested the preposition was live. | decided: personal name with dative ለ-, reasoning stated in the note; l and i ('to Bäyna-Ləḥkəm') kept; gloss.json entry made to agree (see pass 2). |
| unit 7 | n | minor | Jehoiada was the priest who raised king Joash, not his father (his father was Ahaziah). | corrected. |
| unit 10 | n | moderate | -ዎ read as 'it' (the country) against the drafter's own admission that it is masculine; the country is feminine (ነጸርዋ two words earlier), so -ዎ is 'him' (Canaan) and ክፍሎ the accusative object. gloss.json already said 'gave him', so units and gloss disagreed. | note, l and i changed to 'gave him/Canaan his portion'; ከናኦን kept (not Cush); gloss agrees. |
| unit 10 | l | moderate | see note (-ዎ = Canaan). | 'it' -> 'him'. |
| unit 10 | i | moderate | i 'judged' is not in the Geʿez (ነጸርዋ 'looked at her'; l has 'looked-at'); and 'gave it ... as his portion' followed the wrong -ዎ. | i: 'saw it as'; 'gave Canaan his portion, to him and to his seed forever'. |
| unit 12 | i | moderate | i 'to its end' contradicts l and the text (ርእሰ ዐውደ ዓመት 'head of the year's cycle', which is the turn of the year); it imported the end-of-year wording of Deuteronomy 11:12. | i follows the Geʿez; note still names the Deuteronomy echo. |
| unit 13 | n | moderate | note's reasoning was a non sequitur ('David is Solomon's lord, since Solomon is my lord') and claimed to keep one reading while i is open between the two. | note rewritten honestly. |
| unit 13 | i | minor | a crux presented in i without the (?) the note's own uncertainty calls for. | (?) added. |
| unit 15 | i | moderate | same 'to its end' error as unit 12. | corrected. |
| unit 16 | i | moderate | 'grown by' is invented: the Geʿez has only ከይዶሙ በእግር 'they treading with the foot'; the Deuteronomy 11:10 irrigation sense is the drafter's inference and was in i unmarked. | i literal, marked (?). |
| unit 16 | n | minor | 'a form with a 3mp ending' is vague; ከይዶሙ is the Geʿez gerund (ከይዶ / ከይዶሙ). | named the form. |
| unit 17 | l | major | ትኄይሱነ was parsed as 3fs ትኄይስ + -ነ, but the -ሱ- is the plural vowel: 3fs + -ነ would be ትኄይሰነ. It is 2mp 'you surpass us' (ኀየሰ with accusative), the pleonastic እምኔነ following. | l, i, note and gloss corrected. |
| unit 17 | i | major | see l. | as l. |
| unit 17 | n | major | same error, in the note. | note corrected. |
| unit 18 | l | minor | ለ- marks the object here; house practice (ch. 33 'summoned-him to-Tamrin') glosses it 'to-', and the note itself says 'mark the objects'. | 'of-' -> 'to-'. |
| unit 18 | i | minor | ልጐታተ is a guess in note and gloss but i carried no (?). | (?) added. |
| unit 19 | l | moderate | አስተፋጢንየ is a 1cs gerund (ending -የ) of አስተፋጠነ 'make haste', recognizable; the draft left the Geʿez in l and called the form unreadable. | l and i give 'hastening / in haste' with (?). |
| unit 19 | i | moderate | Geʿez word left unrendered in i. | see l. |
| unit 19 | n | moderate | see l. | note rewritten. |
| unit 19 | n | minor | 'the text's habit' hedge; it is the house-attested spelling of the 1cs prefix. | reworded. |
| unit 20 | n | minor | ዕደው is the plural of ዕድው, not of ብእሲ (the gloss entry has it right). | corrected. |
| unit 20 | n | minor | formation was left 'unclear' though እሊአሁ is the regular plural possessive. | named. |
| unit 24 | n | minor | 'quirk' wrong, and the missing ም (A-stem would be ኣምጽኦ) went unmentioned. | reworded. |
| unit 25 | i | minor | l 'O-my-chief' (ሊቅ) vs i 'my lord', which is the rendering of እግዚእ everywhere else in the part. | i -> 'my chief'. |
| unit 28 | i | minor | 'lost the thread' is a modern idiom for 'erred' (l: 'erred what they-say'). | reworded. |

## Pass 2 — changes (gloss.json)
| unit / key | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| gloss ይትቀበሎ | entry | minor | suffix named -ሎ 'him'; it is the accusative -ኦ (the note and the Geʿez ይትቀበል+ኦ). | -ሎ -> -ኦ. |
| gloss ለበይነ | entry | moderate | entry still hedged with (?) and described the form as 'Dillmann's preposition ለበይነ', an invented preposition shape; the preposition is በይነ and the ለ- is the dative. | reworded to agree with units.json, (?) dropped; lemma kept በይነ as in the published glossary. |
| gloss ወመርቄ | entry | minor | first-person 'not in Dillmann as I recall' in a reader-facing popup. | removed. |
| gloss ይትካፈሉ | entry | moderate | lemma ተካፍለ is not a Geʿez form (ፍ 6th order); the verb is ተካፈለ, as the unit note spells it. | lemma corrected. |
| gloss ስፍሕት | entry | moderate | lemma ስፍሕ invented; the adjective is ስፉሕ. | lemma corrected. |
| gloss ወረሓብ | entry | moderate | lemma ረሓብ is not a dictionary form; the adjective is ርሑብ and the note itself is divided between 'broad' and 'famine'. | lemma ርሑብ, alternative named, (?). |
| gloss ትውሕዝ | entry | moderate | lemma ወሕዘ (with 6th-order ሕ) is not a perfect form; the verb is ወሐዘ. | lemma corrected. |
| gloss ወይውሕዝ | entry | moderate | same lemma error. | corrected. |
| gloss ይውሕዙ | entry | moderate | same lemma error. | corrected. |
| gloss ወሀየላተ | entry | minor | 'from memory' in a reader-facing popup. | removed phrase, (?) kept. |
| gloss ከይዶሙ | entry | moderate | parse 'verbal noun ከይድ + -ሙ?' invents a form; ከይዶሙ is the 3mp gerund. | parse corrected. |
| gloss ብክሙ | entry | minor | lemma ቦ with '-ክሙ' is wrong: ብክሙ is the preposition በ with the 2mp suffix; ቦ 'there is' is itself በ + ሁ. | lemma በ. |
| gloss ትኄይሱነ | entry | major | 3fs parse contradicted by the -ሱ-; see units 17. | parse corrected. |
| gloss ሣረረታ | entry | moderate | parse '3ms perfect' with a feminine subject (ጥበብ, and the ት of the form); 'from memory' in popup. | 3fs; 'from memory' removed. |
| gloss ወአጽንዐቶ | entry | moderate | parse '3ms perfect'; the ት of -ቶ is the 3fs ending (subject ጥበብ). | 3fs. |
| gloss ልጐታተ | entry | minor | lemma ልጓት does not match the plural ልጐታት nor the note (ልጐት). | lemma ልጐት. |
| gloss አስተፋጢንየ | entry | moderate | 'unclear ... perhaps my haste' mis-named the -የ as a possessive; it is the 1cs gerund ending. | parse corrected. |
| gloss ወለእሊአሁ | entry | minor | lemma 'እሊአሁ' / 'formation unclear' though it is the plural of ዚአሁ. | lemma ዚአ, formation named. |
| gloss ኣመጽኦ | entry | minor | missing ም not mentioned. | added. |
| gloss ወየኀጥኡ | entry | moderate | lemma ኀጥአ is not a perfect form (ጥ 6th order); the verb is ኀጠአ. | lemma corrected. |
| gloss ዘያሰምክ | entry | minor | 'causative-looking' hedge vs the unit note; made to agree with note and ch. 24. | reworded. |

## Findings refused (nothing changed)
- **ኵላ** (unit 13): I suspect ኵላ is ኵሉ + -ሃ 'all of it' rather than a 'variant of ኵሉ fem.', but the published known-forms entry says 'variant form ኵላ, accusative'; reusing the published entry is the rule, and the translation is unaffected. Left; worth a broaden in a later firing if confirmed in Dillmann.
- **ከናኦን -> Cush (unit 10)**: refused; the text says Canaan, the draft translates what is written and says so.
- **ንንዑ, ተዓይን, ሰገም, መርቄ, ደደክ, አስሐትያ, ወአዳም, ጸዳል (as land-name), ጊሜ**: unidentifiable by me against Dillmann without guessing; the draft marks each (?) and leaves Geʿez in the English. Not 'fixed' with an invented sense.
- **ቶራተ 'wild oxen', ሀየላተ 'ibexes'**: could not verify the 'wild'/'ibex' senses; kept with the draft's (?) on ሀየላተ only.
- **እምነ እምከ (unit 8)**: the reading 'than your mother' matches the published እምነ 'than' entry; no better parse found.
- **ዘንከሪ 1cp 'we dig' in l vs 'one digs' in i (unit 15)**: a deliberate, noted generalizing shift; kept.
- **ሣረረታ, ወአጽንዐቶ 'suffix -ታ/-ቶ'**: the ት is the 3fs ending and the suffix is -ኣ/-ኦ strictly, but ch. 33-34 names the joined -ቶ/-ታ as the suffix; followed the house.
- **'Gt' for ተንሥአ, ተነድፈ**: house label for the ተ- stem; kept.
- **ይሬእይዎ 'lengthened first vowel' (unit 28)**: loose but not wrong enough to spend a change on.
- **'chief of his might' / 'messenger of King Solomon's might' renderings (units 0, 7, 18)**: consistent with each other and flagged in unit 0's note; kept.
- **ነዋኅተ 'long, deep'**: Dillmann 'long'; 'deep' is the draft's contextual gloss for wells, left with the (?).
- **ረሓብ in unit 10 i/l**: left as a Geʿez word in l with the alternatives in i, both marked.
- **'fine garments' (unit 20 i) for ሠናየ አልባሰ**: fine.
