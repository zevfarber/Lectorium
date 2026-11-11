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

## Pass 2

Reviewer pass 2 (2026-11-11). I checked every one of the 270 new gloss.json entries and all 23 `__broaden__` entries. Each was checked against the text, the unit notes as they stand after pass 1, the published mabinogi-glossary.json and the 002 gloss and review. The aids and rules were the same as in pass 1: Strachan, Morris-Jones, Silvan Evans and GPC from knowledge, the Red Book as third witness, and no translations. Edits were made by script (ensure_ascii=False, indent=1).

The "(obsolete)" tag the glosser put on about 20 words was a guess. It is not house style (002 left out the modern form when unsure), so I removed it everywhere. Where a modern form is certain I give it (marannedd, mwsgrell, cynhewi, darmerth, llopan, trosol, rhifedi, gomedd, weithian, didrahaus). Where it is not, I give the Middle Welsh lemma alone (tormynnawc, reudus, madws, didestyl, negessawl, keimat, goreugwr).

No unit note needed changing: every disagreement was the glossary's fault. All 102 `t` still equal cut.json.

Every novel-forms.json key (270) still has a non-empty entry. Every broadening still begins with the published entry, whole, followed by " · ".

Counts, by table row: **18 major, 47 minor, 1 style**.

### Changes — gloss.json

| form | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| uaranned | entry | major | Gave the lemma "baraned (obsolete)" and the mutation b > u. The radical is m- (the unit 4 note has maranned). | maranned (marannedd) 'wealth, stores', with m > u after holl. |
| eistedyssont, eistedyssant, gyuodassant | entry | major | Called them 3 pl. pluperfects ('had sat', 'had risen'). -yssont/-assant is the 3 pl. preterite (the pluperfect is -assei/-assynt), as the unit 6 and 54 notes say. | Called 3 pl. preterite. gyuodassant now also notes the plural by sense (unit 54). |
| gynted | entry | major | Gave 'porch, entrance' and said this "fits the context". The unit 9 note and i have 'upper end of the hall', the MW sense. | 'the upper end of a hall, where the lord sat'. The modern 'porch' is marked as later. |
| uelly | entry | major | Gave the lemma "melly" and said "soft-mutated (m>u)". uelly is felly spelt with u for v, so there is no mutation. | uelly (felly), u = v, no mutation. |
| neus | entry | major | Example glossed "you have indeed given it". rodes is 3 sg. (unit 16 note: 'he has given it'). | 'he has given it so'. |
| uuscrellach | entry | major | Gave the lemma "buscrell (obsolete)", the mutation b > u and the meaning 'foolish'. The radical is m- (unit 20: muscrell 'feeble, inept'). | muscrell (mwsgrell) 'feeble, inept, slow', m > u as complement after ny bu. |
| tormynnawc | entry | major | Gave 'turbulent, domineering' from an invented "tormyn 'tumult'". The unit 22 note gives the usual 'with a great host' and calls it uncertain. | Aligned with the note: disputed, usually 'with a great host, mighty'. |
| derw, chan, yt | entry | major | Took derw as an adjective "true, certain" (and chan's example as "since it is true"). yt said "the construction is uncertain". The unit 22 note (pass 1) has derw = deryw, perfect of daruot. | derw: daruot, = deryw 'it has happened', with the Red Book's derw. chan and yt now use 'it has befallen you'. yt's lemma is now y 'to', conjugated. |
| rot | entry | major | Gave "rhawd (obsolete here), probably 'company, host'", reading y rot a'th uarchogyon as 'the company and your horsemen'. It is y rwng conjugated, 2 sg. 'between you' (unit 36 note, l and i). | y rwng (rhwng), 2 sg. y rot 'between you', compared with y rof. |
| eidawaf | entry | major | Gave "probably 'I allow, I grant'", an invented sense for eidaw. It did not mention the Red Book. | Aligned with the unit 39 note: uncertain, apparently 'I own (it)' from eidaw. The Red Book reads nyt adawaf (adaw 'allow'). |
| chyuyt | entry | major | Called it present subjunctive. kyuyt is the 3 sg. present indicative (the subjunctive would be kyuotto). The unit 32 note agrees. | 3 sg. present, spirant after ony. |
| geimat | entry | major | Gave the lemma as geimat itself (obsolete), with 'one who steps'. It did not give the radical, and the cause appeared only in passing. | keimat, softened after vocative A 'O'. Usually 'champion, warrior', disputed (unit 58). |
| delei | entry | major | Called it 3 sg. imperfect. delei is the imperfect subjunctive (the indicative is deuei), as the unit 63 note says. | 3 sg. imperfect subjunctive. |
| ueithon | entry | major | Gave "meaning uncertain … perhaps a form of mach 'surety', or a corrupt word". It is weithon 'now' (unit 81 note: 'now, at this point'). | weithon (weithian) 'now', gweith + hon, with u for w. |
| weicheu | entry | major | Gave the cause of the mutation as "not clear, perhaps carried over from y Wawl", and the change as "m>f". | Soft (m > w for the v-sound) as the object of gouyn, separated from it (unit 81). Compare ueicheu. |
| adawaf | entry | major | Gave the lemma gadu with "g lost by soft mutation after a". It is adaw 'leave' (unit 87 note), and a- is its radical. | adaw (gadael) 'leave; promise', with no mutation. |
| ommed, ommedwyt | entry | major | Gave the lemma "ommed (obsolete)", with na ommed taken as an impersonal "let … be refused". It is gommed (gomedd); na ommed is the 2 sg. negative imperative 'do not refuse' (unit 94), and ommedwyt is impersonal preterite after ny (unit 97). | gommed (gomedd). The g is lost after na and after ny. |
| y (broaden) | entry | major | The new reading gave y am hynny as 'concerning that' (units 6 and 90: 'around that, besides'). It also missed y 'their' (for eu, unmutated), which this part uses in y bot (unit 47) and y kymryt (unit 82). | Old entry kept whole. (9) is corrected and (10) 'their' is added. |
| trossei | entry | minor | Gave the lemma "trosi (trosi)". | trossi (trosi), a verb beside troi, aligned with unit 2. |
| odyna | entry | minor | "o + dyna". | od 'from' + yna; modern oddi yna, oddyna. |
| gwineu | entry | minor | Gave 'dark brown, dark-haired', against the note and i ('auburn'). | 'auburn, chestnut-brown (of hair)'. |
| dodwyf | entry | minor | Gave "built on the stem dod- with wyf", with no tense. | Old 1 sg. perfect 'I have come', beside deuthum; the Red Book agrees. |
| darmerth, kynhewi | entry | minor | Tagged obsolete, with the meaning "not certain". Both are known words. | darmerth (darmerth) 'preparation, provision'; kynhewi (cynhewi) 'fall silent'. |
| got | entry | minor | The cause in got uechan was garbled ("as a feminine noun after the verb … as its object"). | Soft as the object separated from its verb (i'th law intervenes). |
| uechan | entry | minor | Did not give the feminine form bechan. | Feminine bechan, softened after a feminine noun. |
| perllan | entry | minor | Said "base form" and nothing more. | Says the expected y berllan is not written here. |
| reudus, didestyl, madws, negessawl, didraha, riuedi, oreugwyr | entry | minor | Tagged "(obsolete)". madws also had 'preferable', and didraha had 'easy to grant', against the notes. | Tag removed. Meanings aligned with the notes (madws 'it is time, it is fitting'; didraha 'without arrogance, modest'; riuedi (rhifedi) 'number'). Uncertain words are still called uncertain. |
| lloneit | entry | minor | Gave the modern form as llond only. | llonaid, llond. |
| dottit | entry | minor | "tt for t" misdescribed the form. | Ending -hit, d + h > tt (unit 30). |
| bydei | entry | minor | Gave "imperfect/conditional". | Habitual imperfect (modern byddai), as unit 30. |
| sseghi | entry | minor | Called it "a slip … with the n dropped". It is not in the log; the unit 33 note has g for the ng sound. | Spelling with ss and g for ng, not a slip. |
| glwm | entry | minor | Gave "object of the verbal noun llad". The unit 35 note has llad as the imperative. | Object directly after the imperative. |
| rwymedic | entry | minor | Gave the verb as "rwymo". The MW form is rwymaw. It did not mention yn. | rwymaw (rhwymo); rh- unsoftened after predicative yn. |
| annwn | entry | minor | Gave "the otherworld", a rendering the house rules avoid. | 'Annwfn, the realm of Arawn'; Penn Annwn 'Head of Annwfn'. Gives the spelling contrast and the Red Book's Annwuyn. |
| ymdanw | entry | minor | Gave no witness. | Kept as written; the Red Book has ymdanaw. |
| lloppaneu, loppaneu | entry | minor | Gave "lloppan (obsolete)", 'clout', meaning uncertain. | lloppan (llopan) 'rough boot, shapeless footwear', as unit 46. |
| draet | entry | minor | Mixed MW and modern ("plural traed"). | Plural traet (traed). |
| ro | entry | minor | Said "soft after the optative a". r- shows no mutation. | Says no mutation shows. |
| archaf | entry | minor | Said "spelt with a (a-affection)". The a is the stem vowel, and erchi has the affected e. | Corrected. |
| sswydwyr | entry | minor | Gave a modern lemma with the modern equivalent "swyddog". | swydwr (swyddwr), plural swydwyr, ss for s. |
| carchar | entry | minor | Gave 'in his own prison' with no doubt. | Says y garchar would be expected (as in the Red Book) and the reading is uncertain (unit 61). |
| yspeil | entry | minor | Gave only 'spoil, booty'. The note and i have 'gear'. | Adds 'gear, garments'. |
| throssawl | entry | minor | Gave "trosawl (obsolete)", meaning guessed. | trossawl (trosol) 'bar, stave, cudgel'. |
| dihenyd, dihenyt | entry | minor | Gave 'death penalty', and examples that did not match l and i. dihenyt said "oed 'was' understood"; the sentence has no verb and is present. | 'end, death, the death a man deserves'. Examples now match units 69–70. |
| euey, hyny | entry | minor | Gave no witness, and hyny was not said to be kept as written. | Adds the Red Book's eveyd hen and hynny. Both are kept as written. |
| perthyn | entry | minor | Called it "impersonal". | 3 sg. present, in perthyn ar 'be the duty of'. |
| uydwn | entry | minor | Gave "1 pl. future/imperfect". | 1 pl. future. |
| dylyer | entry | minor | Gave "impersonal present … modern dylid". | Impersonal present subjunctive, as unit 82. |
| ennein | entry | minor | Gave 'ointment, salve' only. l and i have 'bath'. | 'bath; also ointment'. |
| ouynno | entry | minor | Gave the cause as "after relative a". The softening is after the infixed 'th. | After the infixed 'th. |
| paub | entry | minor | Said "b for w". | u for w. |
| digriuwch | entry | minor | Gave the modern form "difyrrwch". | digrifwch; meaning 'amusement, pleasure', as the house table has it. |
| lonydu, llonydu | entry | minor | Said "no clear softening word", and used the modern lemma. | Soft as the object of dechreu (unit 94). MW lemma llonydu (llonyddu). |
| llonydit | entry | minor | Called it impersonal imperfect subjunctive. | Impersonal imperfect, as unit 96. |
| rwydhao | entry | minor | Gave rwydhau as the radical. | rhwydhau, softened (rh > r) after a. |
| ui (broaden, tentative) | entry | minor | "probably emphatic 'I' … 'I cannot (act) against what you ever say'; uncertain". This contradicts the unit 23 idiom, and the entry missed mi ui (unit 27). | Old entry kept. New reading: softened 'I' after a verb, 'I cannot bring myself to do what you say'; and the emphatic mi ui 'I myself'. |
| yny (broaden) | entry | minor | Gave "behold the household", a rendering the house rules avoid, and no witness. | 'warband'. Kept as written; the Red Book has ar hynny. |
| uuwyt, treulwyt, wnaethpwyt, wnaethpwyd, gollyngwyt, rydhawyt, guarywyt, dreulwyt | entry | style | Labelled "3 sg. impersonal" (the impersonal has no person), and uuwyt as 'there was'. | "impersonal preterite"; uuwyt 'it was (been)'. |

### Broadenings checked
All 23 are needed: each covers a sense or use this part has that the published entry lacks. All 23 keep the published entry whole, followed by " · ".

The tentative ones:
- **ymgueiraw** ('make oneself ready' with ar, sense uncertain): kept. It is honest and fits unit 3.
- **y am**: corrected to 'around that, besides' (see the y row above).
- **ui**: rewritten (see the ui row above).

### Considered and refused
- **Published-glossary entries carrying "3 sg. impersonal"** (gelwit, gyweirwyt): not mine to change in this pass. They are recorded here for the owner.
- **Example phrases in parentheses**: they are the published house practice (002 and the work glossary). Each entry's meaning and grammar are stated generally, and the example only illustrates. Kept.
- **diskynnent lemma "disgyn"**: the MW verbal noun is diskynnu or discyn, and the modern disgyn is a fair lemma. Kept.
- **ammouyn lemma ymouyn (ymofyn)**: amouyn and ymouyn are by-forms. Kept.
- **llef "noun f."** and **enryded "noun f."**: gender varies in the sources. Not worth a claim either way. Kept.
- **wedy "no clear softening word"**: gwedy is often written wedy with no mutating word before it. The entry is honest. Kept.
- **derw as an adjective 'true'**: I considered whether a separate adjective lies behind derw. The construction with yt and a verbal noun fits deryw 'it has befallen', and the Red Book writes the same. I kept the pass-1 reading and did not add the adjective as an alternative I cannot support.
