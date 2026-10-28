# Review, pass 1 — kebra-nagast-ch102

Checks run by script: units' `t` joined == packet Geʿez (identical, 4331 chars); every unit ends at ። ፤ or ፨; only units 0 and 1 carry `p` (the packet has a heading and one paragraph); every text word is covered by known-forms or gloss.json; novel-forms == gloss keys. No `t` was touched. Edits were made by script (json load/modify/dump, ensure_ascii=False). Units are numbered 0-38 in file order.

## Changes to units.json

| Unit | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 5 | n | major | Said ገሰሳ has an ending that "does not match" እደዊነ and called it a scribal slip. ገሰሳ is the regular 3fp perfect and እድ is feminine, so it agrees. (The gloss already had it right; the note contradicted it.) | Note rewritten: 3fp perfect, agrees with እድ. |
| 5 | l | moderate | "that-touched our-hands" lost the plural subject. | "that-they-touched our-hands". |
| 5 | n | moderate | ለብዉኬ called "the plural imperative of ለበወ". The printed vowels (lä-bə-wu) fit neither the plural imperative (ልበዉ) nor the perfect, and gloss.json called it "2ms". | Parse stated as a guess, no false label (gloss changed to match). |
| 5 | n | minor | ኮነ ክፍልነ explained as "feminine/abstract ክፍል, unmarked agreement". ክፍል takes 3ms ኮነ without comment. | "agreeing with ክፍል". |
| 6 | i | minor | "this which he said means that" adds a verb "means" the Geʿez does not have. | "And this that he said: Christ became the ransom of all; and we too believe in him." |
| 7 | l, i, n | major | ኀበርነ parsed as 3ms perfect + "us". With a 3ms verb the form would be ኀበረነ. The printed ኀበርነ is the 1cp perfect, "we were joined/united", which fits the fellowship theme of unit 5. i had "he joined us to himself". | l "and-we-were-joined by-his-grace"; i "...and we have been united by his grace"; note rewritten. Gloss changed. |
| 7 | i | moderate | "In the beginning was the Word, and the Word was with God" is the English John 1:1 as remembered. The Geʿez is ቀዳሚሁ ቃል ውእቱ ("...he is Word"). | Rebuilt from the grammar: "In the beginning he was the Word, and that Word was with God." |
| 8 | n | minor | Note said "the sense is 'the Word was God'" while l and i correctly keep the Geʿez order (God is the Word). | Note now says the Geʿez has God as subject. |
| 12 | l, i, n | moderate | The relative እንተ is fem. but አፍቀሮ is 3ms + -ሁ, so the subject cannot be the love ("which loved"); it is God who loved. | l "which he-loved-him, the-man"; i "the love with which he loved humankind"; note says why. |
| 12 | i | minor | ዐውከኩ is flagged (?) in the note but i asserts "were thrown into confusion". | (?) added in i. |
| 13 | n, l | moderate | ተቀኒዎ called a verb made from ቅንዋት "nails" and marked (?). It is the other way round: ቀነወ "pierce, nail" is a verb and ቅንዋት derives from it. | Note corrected; (?) dropped from l. Gloss changed (13, 17). |
| 14 | i | moderate | "arms" asserted although እራሑ is unidentified, and the note and l mark it (?). | (?) added in i. |
| 14 | i, n | moderate | "despite the greatness" adds a concessive force; l and Geʿez say "in" (በ-). | i "in the greatness of his eternal divinity"; note explains that "despite" may be meant but is not said. |
| 15 | i | minor | "feeble creature of earth": "creature" added; house rendering of መሬታዊ is "earthly one". | "the feeble earthly one". |
| 16 | l, i, n | major | ሰሪቦ ብሒአ left untranslated in l (Geʿez in the English line) and guessed as "hungering and thirsting". ብሒእ is "vinegar" in the published glossary and ሰረበ "he drank, sipped" in published ch. 98b. | l and i: "Fasting, sipping vinegar, crowned with a crown of thorns"; note rewritten; gloss ሰሪቦ fixed. |
| 16 | n | minor | "gerund of ጸመ". | ጾመ. |
| 17 | n | moderate | ተቀነወ "from ቅንዋት, (?)" — see unit 13. | "tä-stem of ቀነወ"; (?) dropped. |
| 20 | i, n | moderate | i added "else" and "as he knows himself"; the note admitted the addition. l and i must agree in force. | i "And as for him, there is no one who knows him, for he is the maker of all." |
| 21 | i | minor | Opens "For" for ወሶበሰ ("And if/when ... indeed"). | "And if they had known...". |
| 22 | n | minor | ሎሙ "= ለ + -ሆሙ"; it is ለ + -ሙ. | Corrected. |
| 23 | i | moderate | "Light from Light, God from God, Son from the Father" is the English creed as remembered; the Geʿez is ዘእም- "that is from". | "light that is from light, God that is from God, the Son that is from the Father". Note says so. |
| 23 | n | minor | ያመስሉ derived from "አመሰለ"; gloss has አምሰለ. | Note uses አምሰለ (causative of መሰለ). |
| 24 | l | moderate | l "above the-Most-High" but i "above the heights" (and the note says the Most High would be odd). | l "above that-which-is-high". |
| 24 | i | minor | "our refuge": no pronoun in the Geʿez. | "the refuge (?)". |
| 24 | n | minor | "closing the first long paragraph": the packet has one paragraph. | "run of argument". |
| 25 | l, i, n | moderate | l "in-eloquent(?)", i "of surpassing speech", note "exalted word": three different readings of በሊኀ ቃል; ሊኀ is not a word. | One reading, flagged: ሊኀ possibly a misprint for ሊቀ "chief-of"; l "in-chief(?)-of word", i "foremost in speech (?)". Gloss changed. |
| 25 | i | minor | "upholder of all"; known entry for አኃዜ is "holder, seizer". | "holder of all". |
| 25 | n | minor | Psalm reference "45:4 (Greek 44:4)" mixes numberings; the comeliness line is English 45:3 = Greek 44:4. | "45:3 (Greek 44:4)". |
| 28 | l, i, n | major | ጽድቅ rendered "truth" in l, i and note, in the order of the remembered Psalter ("truth, meekness, righteousness"); the house rendering is "righteousness" and the note quoted the English verse. | "righteousness and uprightness and meekness"; the quoted English removed from the note. |
| 28 | n | moderate | All three verbs called imperatives; ታሰራሕ has the ታ- of the 2ms imperfect (and the gloss said so). | Note separated imperatives (አርትዕ, ንገሥ) from the imperfect/jussive. |
| 28 | i | minor | "Go forward rightly" did not match l "Go-straight". | "Go straight (?)". |
| 29 | l, i | moderate | ያምጽእዎሙ is a 3mp jussive (gloss agrees) but l/i had it as an imperative "Bring them". | "let-them-bring-them" / "Let them bring them before me and strike them down (?)". |
| 29 | n | minor | "57 words"; there are 56. | Fixed. |
| 31 | n | minor | "‑ዮሙ / ‑ቶሙ are -ሆሙ 'their'": the suffix is -ሙ. | Corrected. |
| 32 | n | minor | "causative of ነጸሐ"; the root is ንጽሐ (gloss correct). | Corrected. |
| 35 | i, n | moderate | ወይቤ በግብር "he said it in deed" stated flatly; the alternative "he said in the Acts" (cf. በግብረ ሐዋርያት in unit 6, just after the Acts quotation) is at least as likely. | (?) in i; alternative added to note. |
| 36 | n | moderate | አብዲ and ወሐቀዩ said to be unparseable. አብዲ is plausibly አብዱ (-ዲ for -ዱ as in ኢይፈቅዲ, unit 29); ሐቀዩ is a regular 3mp perfect of a III-y verb ሐቀየ. | Notes say so, with (?). Glosses changed. |
| 37 | l, i, n | moderate | "who has been with his Father, and his Holy Spirit..." made the Spirit a second subject of the 3ms ይነብር, and "has been" for stative ሀሎ. | "the one who is with his Father and his Holy Spirit, the giver of life to all". |
| 0 | n | minor | "The title is ours": the heading is in the source (only the part title is ours). | "The heading is part of the source text." |
| 4 | n | minor | "the next unit makes plain" that ገብረ is the verb; the object in the same unit does. | Fixed. |

## Changes to gloss.json

| Key | Severity | What was wrong | What was done |
|---|---|---|---|
| ወኀበርነ | major | Parse "3ms + us" (see unit 7). | 1cp perfect "we were joined". |
| ሰሪቦ | major | "uncertain... thirsting"; ignores published ሰረበ "he drank, sipped". | ሰረበ — sipping, drinking. |
| ወተቀኒዎ, ተቀነወ | moderate | Called denominatives of ቅንዋት. | Tä-stem of ቀነወ "pierce, nail". |
| ወሐቀዩ | moderate | "corrupt... not found as a verb" as the lemma slot (popup would show "corrupt"). | ሐቀየ — gnash (?). |
| አብዲ | moderate | Lemma slot "corrupt". | አበደ, read as አብዱ (?). |
| ወይ, ቤ | moderate | Lemma slot "corrupt word-division". | Lemma ብህለ, "and he said (...split by a stray wordspace) (?)". |
| ለብዉኬ | moderate | "2ms imperative G", contradicting the note's "plural", and not matching the vowels. | Marked as an uncertain form. |
| እራሑ | moderate | Invented lemma እራሕ "arm(s)". | Unidentified noun (?), possibly for እደዊሁ. |
| ፈላሴ | moderate | "ending -ሴ is odd". It is the accusative/construct in -ē like ገባሬ. | Parse stated; word still (?). |
| በሊኀ | moderate | Invented lemma ሊኅ "eloquence". | ሊኀ unidentified (?), possible ሊቀ. |
| አምዕዑኒ | moderate | Lemma አምዐ for a form with doubled ዐ (root ʾ-m-ʿ-ʿ), inconsistent with the note. | አምዐዐ, flagged. |
| ማሕየዌ | minor | Muddled "giver-of-life-of". | "life-giver-of (construct)". |
| ወንዜንወክሙ | minor | "G" stem for ዜነወ. | "1cp imperfect". |
| ተገድፈ, ተክዕወ | minor | Lemmas misspelled (ገድፈ, ከዐወ). | ገደፈ, ክዕወ. |
| ዘኣፍቀርክዎሙ | minor | ዘ- as "those whom" only. | "that which, those whom". |
| ንብኪዮሙ | minor | Suffix given as -ሙ; it is -ዮሙ. | Fixed. |
| __broaden__ | minor | Known entries that did not cover this part's use. | Added (old entry + " · " + new) for ክፍለ, ሐመ, ሕማም, ኀሳረ, ላሕዩ, ፈድፋደ, ርኵስ. The two existing broadenings (ቀዳሚ, እምነ) checked and kept. |

## Findings refused

- Unit 29 is 56 words (over ~45) but has no ፤; the rule cuts only at a ፤ and a unit may end only at ። ፤ ፨. Kept whole, as the drafter said.
- Unit 1 "tä-stem has an active sense here" for ተነበየ: harmless (deponent), left.
- Unit 12 / 36 treatment of ዐውከኩ (1cs form after plural እለ) and ኢይፈቅዲ / አብዲ as scribal: agrees with the form; left with (?).
- Unit 6 "gospel of Jesus Christ" (l has no "of"): standard apposition rendering; l shows the juxtaposition. Left.
- Unit 11 "third glory" read as the Spirit: already (?) in the note; left.
- Unit 13 ዕልወት "disobedience": known entry says "perversity (?)"; published ch. 2-8 gives "transgression, perversity". Rendering is within range; left.
- Unit 16/17 ኀሳር "insult": kept in i, with the broadened gloss marked (?).
- Unit 18 closing sentence of the note ("he bore it by choice, so that it was for us") is interpretation, not grammar; left.
- Unit 23 ፈላሴ "Sojourner" capitalized with (?): left.
- ጠይቅ as imperative (unit 9): matches the known entry.
- Glosses for ኢይፈቅዲ, ዐውከኩ, ተረግዘ, ይርግዝዎሙ, ፀራ, አሕፃከ, ምስካይ, መሴስይ, ያስተሴንዮ, ታሰራሕ, ኅብራ, ገኒየ, አፅምኡኒኬ: lemmas cannot be checked without Dillmann; all already carry (?) and none contradicts the text; left.


# Pass 2 — kebra-nagast-ch102 (fresh eyes)

Checked independently: all notes' labels, original → l word by word, l ↔ i, remembered English, house renderings against the 72 published parts (their glossaries were searched for each doubtful lemma), every gloss lemma and parse, and each `__broaden__` entry (all nine keys are in known-forms.json; each is the old entry whole + ' · ' + new reading). `t` untouched (verified identical to the pass-1 file); novel-forms == gloss keys.

## Changes to units.json

| Unit | Field | Severity | What was wrong | What was done |
|---|---|---|---|---|
| 18 | l | moderate | ያሐዝኖ (causative, "grieves him") rendered passive "he-is-grieved"; the object -ኖ was lost and l contradicted the note | "it-grieves-him" |
| 36 | l, i, n | moderate | ኅብራ ወግብራ given "nature ... works"; published ch. 17-20 / 98a / 64-65 render the same phrase/word as "form, colour, kind" and "making" | l "its-form(?) and-its-making"; i "whose form (?) and making"; note says so |
| 36 | n | moderate | አጽምአ as lemma of አፅምኡኒኬ; published ch. 28 has አጽምዐ (and ጸምአ is "thirst") | አጽምዐ |
| 36 | n | minor | ሰሚዖሙ glossed "+ -ሆሙ"; the suffix is -ሙ (known entry) | corrected |
| 12 | n | moderate | ገኒየ called "a gerund"; the ending is not the gerund -ዖ and the gloss said "verbal noun / accusative" | note and gloss say: form of ገነየ, verbal noun or gerund-like, uncertain |
| 12 | i | minor | "fell away" is a verb the Geʿez lacks (እምጽድቅ is the complement of ዐውከኩ); ገኒየ (?) not carried into i | "thrown into confusion (?) away from righteousness ... refused to submit (?)" |
| 14 | n | minor | ሕማም called "accusative"; the accusative -ä is not written | "cognate object (accusative ending not written)" |
| 17 | n | minor | ተጽዕለ / ጸዐለ "scorned" given as certain; published ch. 13-16 calls the root's sense uncertain; ጸረፈ vs the text's ፀ and the gloss's ፀረፈ | (?) added; ፀረፈ |
| 16, 18 | n | minor | same ጸዐለ-family sense stated flatly | (?) added |
| 16 | n | minor | ተከልለ vs gloss lemma ተከለለ | note harmonized to gloss |
| 17 | i | minor | "master of death" vs l "ruler-of" | "ruler of death" |
| 11 | i | minor | "as it was said exactly" turns relative ዘ- into a comparison, and "shows the Holy Spirit" | "who was spoken of exactly" |
| 8 | i | minor | ወይ ቤ is (?) in l and note but not in i | (?) added |
| 7 | n | minor | ቀዳሚሁ (John 1:1) not explained though l drops the -ሁ | one clause added, hedged |
| 5 | n | minor | ወንዜንወክሙ "1st plural of ዜነወ" with no tense | "imperfect" |
| 21 | n | minor | Remembered English of 1 Cor 2:8 in quotes; እመ claimed to mark "the result clause" as fact | quote removed; the claim marked (?) |
| 10, 22, 26, 27, 29, 30, 34 | n | minor | Remembered English verses quoted in notes (John 1:3, Luke 23:34, Ps 45:2, Ps 35:12, Isa 29:13, Deut 32:28, Acts 7:53); same fault pass 1 fixed in unit 28 | quotes removed, citations kept; unit 26's "pronoun changed" claim (from the remembered verse) replaced by what the Geʿez shows |
| 29 | n | moderate | ፀራ called "the construct plural of ፀር"; no such plural exists | stated as a read form, not the ordinary plural (?) |
| 29 | i | minor | ይረትዕ and ኢተሰጥዉኒ are (?) in note/gloss but flat in i | (?) added |
| 30 | n | minor | አምዐዐ (published parts use አምዐ, "uncertain stem"); suffix of ኣቀንኦሙ called -ሆሙ (it is -ሙ); lemma አቀንአ vs gloss አቅንአ; ህጉል vs gloss ሕጉል | all four harmonized |
| 31 | n | minor | ወፈደዮሙ "+ -ሆሙ"; suffix is -ሙ | corrected |
| 33 | n | minor | ኀርየ vs known lemma ኀረየ | corrected |
| 34 | n | minor | እበዶሙ "+ -ሆሙ"; suffix is -ሙ | corrected |
| 25 | n | minor | አስተሰንየ vs gloss አስተሠነየ | harmonized |
| 37 | n | minor | ጸወረ; the known lemma is ጾረ | ጾረ |
| 37 | i | minor | "carry it" adds an object the Geʿez does not give | "carry it (?)" |
| 37 | n | minor | ወየዐርግ መንበር ለሳብዕ ሰማይ read one way only | alternative added (?) |

## Changes to gloss.json

| Key | Severity | What was wrong | What was done |
|---|---|---|---|
| አሕፃከ | major | Lemma ሕፅ is not a word found elsewhere; published ch. 96a has ሐጽ "arrow" | lemma ሐጽ, spelling variant noted |
| አፅምኡኒኬ | moderate | "of ጸምአ?" links 'listen' to ጸምአ "thirst"; published lemma is አጽምዐ | lemma አጽምዐ |
| ኅብራ | moderate | "nature, form (?)", lemma ኅብር; published uses ሕብር "colour, form, kind" | ሕብር, "form, kind, colour (?)" |
| ወያአምር, ዘያአምሮ | moderate | "G" stem for አእመረ (a-stem; the known entry says causative) | "a-stem of ʿ-m-r" |
| አምዕዑኒ | moderate | Invented lemma አምዐዐ; published parts (ch. 2-8, 44, 46-48) use አምዐ "uncertain stem" | አምዐ, stem uncertain |
| ገኒየ | moderate | "verbal noun / accusative" asserted as a parse | made tentative |
| ተጽዕለ | moderate | Lemma ጽዕለ (no such verb); the root is ጸዐለ | "tä-stem of ጸዐለ", sense uncertain |
| ወጽዕለተ, ወጸዐልዎ | minor | "scorn" unhedged though the root's sense is uncertain (published ch. 13-16) | (?) added |
| ታሰራሕ | minor | Lemma አሰርሐ spelled with ሰ beside "ሠርሐ" in the same entry (and in published parts) | አሠርሐ |
| አርትዕ | minor | "go straight" for a causative stem | "make straight, set right (?)" |
| ወከንቶ | minor | Etymology "ከንት 'empty'" unverifiable | removed |
| ዘሀሎ | minor | "has been" for a stative perfect (pass 1 corrected i only) | "who is" |
| ወመላኬ | minor | note has (?), gloss none; published ch. 40 has (?) | (?) added |

## Findings refused

- ተከሊሎ lemma ተከለለ vs ተከልለ: both give ተከሊሎ; the note was harmonized to the gloss, no more.
- መላኪ: real in published ch. 40 ("Dillmann's መላኪ (?)"); kept.
- ተፀርፈ lemma with ፀ: published ch. 13-16 and 76a use ፀረፈ; kept (note harmonized).
- ተሰጥወ, ረገዘ, አጽነነ, ዐወከ, ሐቀየ, አበደ-as-አብዱ, ፈላሲ, ምስካይ, መሴስይ: cannot be checked without Dillmann; all already (?) and consistent with the text; left. (ፈላሲ and ምስካይ also occur in published parts.)
- ወይትመሐፀኑ "entrust" for መሐፀነ: published ch. 51-52 gives "take refuge"; the form's lemma is right, the gloss of the stem unverifiable; left.
- Unit 24 "above the heights" (ዘልዑል) left without (?) in i: l shows "that-which-is-high" and the note explains the doubt.
- Unit 12 / 36 ዐውከኩ, አብዲ readings: already (?); left.
- Unit 5 ለብዉኬ, unit 6 አመነ: already (?) with honest notes; left.
- Unit 18 closing note sentence (interpretation): left, as in pass 1.
- Unit 29 length (56 words, no ፤): rule bars a cut; left.
