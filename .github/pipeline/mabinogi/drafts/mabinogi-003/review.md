# mabinogi-003 — review

## Pass 1

Reviewer pass 1 (2026-11-11). All 102 units were read against conventions.md, packet.md (the established text and the establishment log) and the published mabinogi-001.json and mabinogi-002.json. Aids: Strachan, Morris-Jones, Silvan Evans and GPC, from knowledge. The third witness, Rhŷs & Evans 1905 (Red Book text, `source/raw/rhys-evans1905_djvu.txt`, printed pp. 12–17), was read for the whole passage. No English translation was consulted. Edits were made by script (Python load/modify/dump, ensure_ascii=False, indent=1). No `t` was touched.

Unit numbers below count from 1 in units.json. The drafter's request list is one lower in places: its "unit 1" trossei is unit 2 here, its "21" derw is 22, its "29" dottit/bydei is 30, its "53" is 54, its "85" rule is 86, its "38" is 39, its "57" is 58 and its "60" is 61.

Counts: **1 major, 31 minor, 1 style** (33 items).

### Changes

| unit | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 61 | n | major | The note on yn y carchar e hun said whose prison it was is "most naturally Pwyll's". That is an unsupported steer, and the note did not say that 'his' should soften carchar. The Red Book has y garchar. | The note now says the reading is uncertain. It says 'his' would give y garchar (as in the Red Book), so the White Book either leaves the mutation unwritten or has the article ('in the prison by himself'). It gives both referents: each man in a prison of his own, or the court's prison. l and i keep "his own" and do not choose. |
| names in l (units 4, 6, 15, 20, 22, 37, 39, 42–45, 56, 58, 60, 61, 70, 72, 75, 79, 81, 83–85, 87, 89, 93, 94, 98, 99, 101, wherever a manuscript form stood) | l | minor | l printed the manuscript forms of the names: Riannon, Heueyd/Eueyd/Euey Hen, Guawl/Gwaul, Clut, Dyuet. The published l layers use the modern forms (001: Dyfed, Annwfn, Hafgan; 002: "Rhiannon daughter of-Hefeydd the-Old"), as conventions.md requires for names in English. | By script, in every l: Rhiannon, Hefeydd (the-Old), Gwawl, Clud, Dyfed. The slip Euey Hen (unit 70) is shown under the intended name, as 002 did for Pwll; its note gives the slip. Notes still quote the Welsh as written. |
| 1 | l | minor | "making he-did": chyrchu is 'make for' (the note says so). | "making-for he-did". |
| 1 | n | minor | Did not say that teulu after 'e 'his' should be softened (deulu). | Says the mutation is not written, and that the Red Book has the same. |
| 2 | l | minor | "would-turn-it" added an object that the Welsh does not have. | "would-turn". |
| 2 | n | minor | Called trossi "a by-form of troi". It is its own verb (modern trosi), beside troi. | Now "third-person imperfect of trossi (modern trosi) 'turn', a verb beside troi". Adds the Red Book's y trossei. **The imperfect label is right.** |
| 4 | i | minor | "a great gathering": mawr qualifies only arlwy. | "a gathering and rejoicing and a great banquet". |
| 6 | i | minor | "This was how they sat:" keeps the Sef cleft. The house drops Sef in i. | "They sat with Hefeydd the Old on one side of Pwyll and Rhiannon on his other side; …" |
| 13 | n | minor | dodwyf was called an "old first-person form". **The check confirms it means 'I have come'.** | Now an old first-person perfect of dyuot, beside the preterite deuthum. Adds that the Red Book has dodwyf too. |
| 22 | n | minor | "derw is a form of daruot" was right but vague. | "derw is deryw, the old third-person perfect of daruot, 'it has happened'". Adds that the Red Book also writes derw. |
| 23 | l | minor | l dropped ui ("I-cannot on-me"). | "I-cannot, I, on-me". |
| 27 | n | minor | "byd softened after the subject" gave the wrong cause. | Now "softened as after the relative a, which is often left unwritten before forms of bot". |
| 30 | n | minor | dottit: **the label (impersonal imperfect subjunctive) is right**, but the tt was not explained. | Ending -hit, with d + h giving tt. The Red Book's pei dottit confirms bei = pei 'if'. |
| 30 | n | minor | "seith cantref: Dyfed's seven cantrefs" overclaims. hynn 'these' points to where they are standing, which is Hefeydd's court. | Corrected, with a remark that Dyfed is also reckoned seven cantrefs. |
| 30 | n | minor | bydei was called "the imperfect of bot". | "the habitual imperfect of bot (modern byddai), … in the result of an unreal condition". Notes that the Red Book has na bo. |
| 36 | n | minor | The am pen note was plain, as the log requires, but gave no witness. | Adds that the Red Book has am benn. |
| 39 | n | minor | nit eidawaf: the note had "appears to be a verb … rare form" but did not say plainly that the reading is uncertain or what the other witness has. | Says it is uncertain and not otherwise known. Gives the Red Book's nyt adawaf i y rodi y neb (adaw 'allow'), and says that l and i follow a guessed White Book sense. |
| 45 | n | minor | Penn Annwn: no witness given. | Adds that the Red Book has Annwuyn here and that it is the same name. |
| 46 | n | minor | ymdanw: no witness given. | Adds the Red Book's ymdanaw. |
| 54 | n | minor | gyuodassant: "the plural verb follows a plural sense" did not state the rule it departs from, which unit 86 states. | Now says a fronted noun subject usually takes a singular verb (cross-reference to Y meicheu a aeth), and that here the plural follows the sense of Riuedi mawr. **The plural is a genuine sense-agreement, not an error.** |
| 58 | l | minor | l dropped the vocative particle A. | "O champion(?)", as 002 has "O men" for A wyr. |
| 58 | n | minor | geimat was not given a base form or a cause for its mutation. | Vocative A 'O' softens keimat to geimat. The note still calls the word's meaning disputed and 'champion' a guess. |
| 60 | n | minor | yny uyd: the softening was not mentioned. | "byd, softened after yny". |
| 61 | n | minor | Ac ar yny: the slip was plainly noted but no witness was given. | Adds that the Red Book has ar hynny. |
| 65 | i | minor | "This was the game they played:" keeps the Sef cleft. | "They played a game of this kind: each one would strike …" |
| 70 | i | minor | "no death for him" did not match unit 69's "no fit death" for the same word dihenyd, and the l has a-fit-death. | "that is no fit death for him". |
| 70 | n | minor | Euey Hen: no witness given. | Adds that the Red Book has eveyd hen. |
| 70 | n | minor | hyny: not said to be kept as written, and no witness given. | "(the Red Book has hynny); kept as written". |
| 79 | l | minor | "until it-be free for his men" turned y 'his' into 'for' and added "it". The note correctly treats y wyr as subject. | "until may-be free his men to go for-him". |
| 86 | n | minor | The rule was right, but it did not mention the exceptions that occur in this part. | Adds that a pronoun subject takes a plural verb (wynt a welynt) and that a noun of plural sense sometimes does (Riuedi mawr … a gyuodassant). **The rule as stated is correct.** |
| 91 | n | minor | The note on honno not being supplied gave no witness. | Adds that the Red Book has y nos honno. |
| 99 | n | minor | rwydhao was given as if it were the radical. | "rhwydhao, softened after a, … of rhwydhau". |
| 13 | i | style | "ask a request of you" is redundant. | "make a request of you". |

(The script replaced every occurrence of a manuscript name form in l, and a check found none left.)

### Drafter's requested checks: verdicts
- **dodwyf** (13): this is correct as 'I have come', an old 1 sg. perfect of dyuot. The Red Book has the same.
- **trossei** (2): this is correct as a 3 sg. imperfect, used of a habit. Only the "by-form of troi" wording was changed.
- **derw** (22): this is correct. It is the perfect deryw of daruot, now named as such.
- **dottit** (30): this is correct as an impersonal imperfect subjunctive. The tt is now explained.
- **bydei** (30, 55): the habitual imperfect, so the label is made precise.
- **gyuodassant / rule in 86**: both are correct, and they are now cross-referenced.
- **nit eidawaf** (39): the reading is uncertain, and the note now says so. The Red Book's reading differs.
- **geimat** (58): disputed and flagged. The missing explanation of the vocative mutation has been added.
- **yn y carchar e hun** (61): uncertain. This was the one major item, and it is fixed.

### Considered and refused
- **Llyna in i (units 22 "That is the man", 72 "Here is the counsel for you")**: l has There-is every time. The published i layers render llyna freely (001: "This is how", "this was the court", "here is the story"; 002: "That … is the errand", "here is my answer"), and pass 1 of 002 refused the same change. At unit 72 the Red Book actually reads llyma. Kept.
- **Llyma in unit 61**: l "behold" and i "there was the warband" follow the pilot's narrative llyma (001 units 9 and 48: l "behold", i free). Kept.
- **Unit 4 l "a great banquet"** (Welsh order arlwy mawr): this is a minor departure from Welsh order that English bears easily. Kept.
- **Unit 10/81 "y … the article" after heb**: this is the pilot's own explanation (001 unit 36, 002 unit 8). Kept for consistency.
- **Unit 29 reudus, 62 didestyl and yspeil, 22 tormynnawc, 37 madws**: each is flagged as uncertain or rare. The Red Book has the same words, so it adds nothing to their meaning. Kept.
- **Unit 34 "tros softened" (dros)**: dros is the usual form and the claim does no harm. Not worth a change.
- **Unit 35 llad as imperative**: it could equally be the verbal noun carrying the instructions, but the imperative is the same form and the note says so. Kept.
- **Unit 40 i titheu (no softening after i 'for')**: I am not sure enough about mutation after a preposition before a conjunctive pronoun to add a claim. The Red Book has y titheu as well. Left alone.
- **Unit 66 i drops uelly ("What game is this you are playing?")**: the "this" carries the force of uelly. Kept.
- **Unit 67 "g for the mutated ngh" in yg got**: this is a fair account of the spelling. The Red Book's ygcot supports a nasal there. Kept.
- **Unit 68, the remark that the game is not known from other sources**: it is hedged and harmless. Kept.
- **Unit 99 oet a chyfnot: l "a-time" against unit 28 "a-tryst"**: the context differs (an appointed day for travel, not a tryst). Kept.
- **The other log items**: am pen (36), Ac ar yny (61), Euey Hen (70), hyny (70), ymdanw (46) and Penn Annwn (45) are all stated plainly in their notes. Red Book support was added to each, as listed above. Nothing was supplied, so there were no supplied-word notes to check.

### Verification
After the edits, a script confirmed that units.json has 102 units and that every `t` equals the corresponding `t` in cut.json, character for character.
