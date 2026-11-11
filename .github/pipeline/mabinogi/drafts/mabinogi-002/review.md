# mabinogi-002 — review

## Pass 1

Reviewer pass 1 (2026-11-11). All 72 units read against conventions.md, packet.md (established text and log) and the
published pilot mabinogi-001.json. Aids: Strachan, Morris-Jones, Silvan Evans, GPC (from knowledge), and the
project's third witness, Rhŷs & Evans 1905 (Red Book text), read on the page images (`source/raw/rhys-evans1905.pdf`,
PDF pp. 20–22 = printed pp. 8–10), as conventions.md allows for White Book defects. No English translation was
consulted. Edits made by script (Python load/modify/dump, ensure_ascii=False, indent=1); no `t` touched.

Counts: **6 major, 25 minor, 4 style** (35 items across 30 fields in 23 units).

### Changes

| unit | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 3 | n | major | Said dylyedauc is "soft-mutated after pa". Its radical is d- (dylyedawc ← dylyet 'right'), so nothing is mutated. | Says the radical is d-, so pa's softening has nothing to show. |
| 7 | n | major | "kyuuch … soft-mutated, after o" named the wrong base and the wrong cause. The word is gogyuuch (gogyfuwch 'level with'), softened after y 'to'. | Base is now gogyuuch (go- + kyuuch, the equative of uchel), soft after y 'to'. Cites the Red Book's yn ogyfuuch. |
| 11 | n | major | Called neut "neu + infixed 't". The -t is not an infixed pronoun: neut is the form the affirmative particle neu takes before a vowel. | Corrected, comparing yd beside y. |
| 36 | n | major | Called hynny "the object". tygyaw 'avail' is intransitive, so hynny is the subject. | Now "the subject hynny stands first". |
| 37 | n | major | wyaf was glossed "stands for uwyaf" and not called a slip. **Decision: it is a slip.** It is one letter short of uwyaf. The scribe writes uwyaf in the parallel sentence (unit 19, ffei uwyaf) and uwy at the end of this same sentence, and the Red Book has vwyhaf here. A lone w cannot carry both the v-sound and the w of wy (compare wwyta, where it takes two). | Note now says plainly: scribal slip, kept as Evans prints it, read uwyaf, with the evidence. **For the establishment log:** wyaf (col. 16) is not listed there and should be. |
| 37 | i | major | i ("no nearer to her than if it had been going at a walk") silently dropped yna … no chynt 'then … than before'. It followed the Red Book's no chyn bei reading, not the White Book's no chynt bei, and so no longer matched l. | Rebuilt from the White Book: "but he was no nearer to her then than before, as though it were going at a walk". |
| 3 | l | minor | "or else that he-would-see": the a of a welei is the verbal particle, not 'that'. | "or else he-would-see a-wonder". |
| 3 | n | minor | The a'y note said "the text prints the apostrophe". That implies the manuscript does; in fact the division and apostrophe are editorial. It also did not give the decisive witness. | **Judgement: the drafter's reading ae 'either' is right.** (1) a 'with' + 'y 'his' makes no sense after "one of the two things" and would give gymriw (and 'her' would give chymriw). (2) The unmutated kymriw and the following neu fit ae … neu. (3) The Red Book reads *ae kymriw ae archolleu* (image checked). The note now says the apostrophe is ours, gives the alternative and why it fails, cites the Red Book, and tells the reader to read ae. `t` untouched. |
| 3 | n | minor | Said nothing on neu ynteu, and had "a welei … 'that he would see'". | Glosses neu ynteu 'or else' and a welei with its verbal particle. Notes that the Red Book spells ryuedawt (rywedawt stays a spelling, not a meaning problem). |
| 6 | n | minor | "the imperfect of bot used for an ongoing state" passed over the fact that bydynt is the habitual imperfect. | "the habitual imperfect of bot (beside oedynt)". |
| 13 | l | minor | "the most that was his haste": uei 'would-be' was rendered "was". hitheu was not shown, against the pilot's practice (she-for-her-part). | "And the most would-be his haste, the farthest she-for-her-part would-be from-him." |
| 13 | n | minor | The mwyf slip was noted but without support. | Adds that the Red Book has vwyhaf. |
| 14 | n | minor | The idaw idaw note was honest but had no witness. | Adds "(the Red Book has it once)". |
| 15 | l | minor | l reordered the Welsh (subject before verb). | "avails-not the foot-speed in the world to-pursue her", in the Welsh order. |
| 19 | l | minor | lladei was rendered "he-struck" (the imperfect is 'would-strike'), and hitheu was not shown. | "the most he-would-strike the horse, the farthest she-for-her-part would-be from-him". |
| 20 | l | minor | hitheu was not shown. | "that she-for-her-part had-begun". |
| 23 | n | minor | Glossed y mae yno as "there is in it", which does not match the word or l ("there"). | "there is there: yno 'there', that is, in this business". |
| 30 | i | minor | Llyma 'here is' was given as "There"; the pilot keeps Llyma 'here' and Llyna 'there'. | "Here," said Pwyll, "is yesterday's horsewoman." |
| 30 | n | minor | The Bid note left the reader puzzled. | Adds that the Red Book has byd, the ordinary 2nd-person imperative. |
| 33 | i | minor | "What the page did then was mount…" keeps Sef's cleft. The house table drops Sef in i and avoids "This is what …". | "The page then mounted the horse; …" |
| 33 | n | minor | neir: the note was honest but had no witness. | Adds that the Red Book has neur ry adoed, and that the White Book's own reading stays uncertain. |
| 33 | n | minor | kynnwll was flagged as a guess, rightly, but with no witness. | Adds that the Red Book has the same word, so it is not this scribe's slip. 'gap, space' is still called a guess. |
| 34 | n | minor | Did not say why urys is softened. | Soft after amgen, as amgen uedwl in the pilot. |
| 37 | l | minor | As in units 13 and 19 ("he-struck", hitheu not shown). | "the most he-would-strike his horse, the farthest she-for-her-part would-be from-him". |
| 37 | n | minor | Base form "awwyn" is not a lemma. | "auwyn, modern afwyn 'rein'". |
| 37 | n | minor | Did not mention the awkward no chynt bei. | Says the White Book reading is awkward and the Red Book's no chyn bei gives 'than if it were at a walk'. |
| 39 | n | minor | The supplied words and the missing ef were already noted honestly. | Adds that the Red Book reads heb ef nyt oes allu. |
| 40 | n | minor | wrthpwythi: "'stubbornness' is the likeliest sense" overclaimed. | Now says the meaning is uncertain and the word perhaps unique. Reports the Red Book's wrthpwyll (gwrth- + pwyll), which points to 'contrariness, perversity'. Calls 'stubbornness' a guess on that basis. |
| 42 | n | minor | wwyta was called a slip outright ("wrote w twice"), yet the same notes treat the w-letter as the v-sound (wal, warch, gywerbyn, Sewyll). | Keeps it listed as a slip, as the log does. Adds that the first w may just be the v-letter, and that the Red Book has vwyta. |
| 50 | l | minor | hitheu was not shown. | "goes she-for-her-part past-him". |
| 66 | n | minor | Called a'm rodi "my giving … the infixed 'm" and dropped a 'and'. Gave hanwod without explaining its w. | "a 'and' + 'm 'my' … standing for the object of rodi"; anuod (modern anfodd), with w for the v-sound. |
| 28 | i | style | "with the horse along" was colloquial. | "and the horse with them". |
| 61 | i | style | "as far as I am concerned" was modern and flat. | "You have my welcome," he said. |
| 66 | i | style | "it is to learn your answer to that that I have come" was clumsy. The fronting is ordinary adverb-first order, not emphasis. | "And I have come to learn your answer to that." |
| 69 | i | style | "The sooner the better" is a ready-made English tag rather than a rendering of goreu … bo kyntaf. | "For my part," said Pwyll, "soonest is best; and make the appointment …" |

### Considered and refused

- **Unit 2 i "first sitting at table"** (y bwyta kyntaf): this is a fair English rendering of 'the first eating' at a feast, so I kept it. I kept the same rendering in unit 26 for consistency.
- **Unit 12/15/21, pedestric rendered differently in l** ('on foot', 'foot-speed', 'speed'): the drafter did this on purpose. The notes explain that the use with a horse in unit 21 points to 'speed', and the word is flagged as disputed. Left alone.
- **Unit 20 n "gerdet ← kerdet, soft after it [vn]"**: un normally softens only a feminine noun, and kerdet is usually masculine. The note only describes what the text shows and does not explain it. I left it rather than add a claim I can't support.
- **Unit 22 i "the lady yonder" for unbennes**: the house table has no feminine of unben. "Lady chieftain" is not English. The l keeps "lady-chieftain" and the note gives the derivation. Kept.
- **Unit 33 n, kynnwll as a miswriting of kyuwng 'interval'**: I considered this and refused it, because the Red Book also has kynnwll.
- **Unit 35 yr araued**: the note already offers both readings (concessive 'for all the slowness' and 'at the gentle pace') and calls the phrase hard. The Red Book's arauet adds nothing. Kept.
- **Unit 37 i "gave his horse its head"**: this is an English idiom, but it is built from ellwg … wrth auwyneu 'loosing by the reins', and the note flags the uncertain force. Kept.
- **Unit 19/37 i "drove" for llad**: "struck the horse" reads as hitting it. l keeps 'strike', and the note explains that llad means both 'strike' and 'kill'. Kept.
- **Unit 39 l "said [he]"**: the bracket marks the ef the White Book lacks, which helps the reader. Kept.
- **Unit 41 i "as it pleased them"** (ual y bu llonyd ganthunt): acceptable. Kept.
- **Unit 42 i "whiled the day away"**: this fits diuyrru 'pass, divert (time)' exactly, so I don't take it as borrowed phrasing. Kept.
- **Unit 43 i "who were with us"**: this departs slightly from 'the company that we were'. It is natural English with the sense intact. Kept.
- **Unit 57 n, archut "imperfect subjunctive"**: in an unreal condition after pei, this matches pei ys guelwn (unit 4) and the pilot's practice. Kept.
- **Unit 65 l "said Pwyll" for Pwll**: the conventions say a readable slip is glossed under the intended word, and the note reports the slip. Kept.
- **Unit 67 i "here is my answer" for llyna**: the pilot itself varies (pilot 32 Llyna → "This is how"). Kept.
- **Unit 26 n makwyf vs pilot "makwy"**: both singulars exist, and makwyf is the form this part's own text has (unit 27). Kept.
- **Unit 29/48 yr un ford**: the note says honestly that the text has the article and that y'r is possible. Kept.
- **No `p` flags in units.json**: the runbook says the build sets `p`. Not a draft defect.
- **The other log items** (a wnath, mwyf, idaw idaw, warch, neir, a wnaet, wwyta, Pwll, supplied nyt oes, the tag lacking ef): all are noted in units 5, 13, 14, 22, 33, 38, 42, 65, 39 and 39 respectively. I strengthened some with Red Book support, as listed above.
- **Uncertain words**: pedestric, rywedawt, ystyr hut, kynnwll, rygyng, araued, auwyneu, wrthpwythi and diuwyn are all flagged without overclaiming. The one overclaim was wrthpwythi, now fixed.

### Note for the glosser

Unit 3 a'y should be glossed as ae 'either' (conjunction), not a 'with' + y 'his', or the gloss entry for this occurrence should say so.

### Verification

units.json loads as valid JSON with 72 sentences. Every `t` is identical to `cut.json` (script check). Only `l`, `i` and `n` were changed, in 30 fields.

## Pass 2

Reviewer pass 2 (2026-11-11). Every one of the 230 gloss.json entries and all 27 `__broaden__` entries were checked against the
text, the unit notes after pass 1, known-forms.json and the published glossary's format (mabinogi-glossary.json). Aids as in
pass 1: Strachan, Morris-Jones, Silvan Evans, GPC (from knowledge), the Red Book as third witness. No translation was consulted
and nothing was looked up on the web. Edits were made by script (Python load/modify/dump, ensure_ascii=False, indent=1), and no
`t` was touched. 221 of the 230 new entries were rewritten in whole or in part (only `llaw` and 8 others are unchanged), and
10 known forms were broadened that the glosser had missed. The house shape `lemma (modern) — meaning; grammar; mutation and
cause` uses the Middle Welsh lemma and gives the modern form in brackets, as the published entries do (gwreic (gwraig),
gwelet (gweld)). Where I was not sure a modern form exists, I left it out rather than guess.

Counts, by table row (one row may cover several forms): **31 major** (24 new-form rows and 7 broaden rows), **38 minor** (32 new-form rows, 4 broaden rows and 2 unit notes) and **1 style** row (lemma normalisation across about 60 forms).

### Changes — gloss.json (new forms)

| form | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| dylyedauc | entry | major | Said "d is probably soft-mutated after pa". Pass 1 decided otherwise: the radical is d-, so the softening shows nothing. | Corrected: dylyedawc (dyledog), d- is the radical. |
| ogyuuch | entry | major | Gave the base as "o + soft-mutated kyuuch, etymology uncertain", which contradicts unit 7. | gogyuuch (gogyfuwch): go- + kyuuch, the equative of uchel; g lost after y 'to'; the Red Book has yn ogyfuuch. |
| warch | entry | major | Called it a "scribal slip, w printed for u by mistake". The log and unit 22 say it is uarch with the w-letter for the v-sound, not a slip. | Now: soft-mutated object, w-letter for v. |
| diuwyn | entry | major | Gave di- + gwyn 'white' and the meaning 'dull'. The spelling uw = fw requires mwyn, as the unit 62 note says. | di- + mwyn, 'worthless, unpleasing', with the debate noted. |
| ffryt | entry | major | Said "meaning uncertain, perhaps 'beauty… course'". It is pryt 'form' after y 'her' (unit 62). | pryt (pryd), spirant after y 'her', written ffr. |
| dabre | entry | major | Said "meaning uncertain, perhaps 'lead out'". It is the old imperative 'come!' of dyuot (unit 45). | dyuot (dod), 2 sg. imperative 'come!'. |
| hayach | entry | major | Gave 'any longer' and an invented etymology from hwy. | hayach (haeach) 'almost; with a negative hardly', as in unit 48. |
| gwrthyt | entry | major | Called it 2 sg. present. -yt is the 3 sg. present, the form a relative verb takes whatever the person of its antecedent. | Lemma gwrthot (gwrthod), 3 sg. present, relative after ti. |
| bydynt | entry | major | Called it "3 sg./3 pl.". -ynt is 3 pl. only. | 3 pl. habitual imperfect, beside oedynt. |
| cany | entry | major | Lemma "cany (canys) — since, for … possibly can + ny; uncertain". The unit 38 note says plainly can + ny 'since … not'. | Now can + ny, which softens the verb. The invented modern equivalent is dropped. |
| tygyaw | entry | major | Said "the negative is implied rather than written". The negative is written: it is the ny of cany. | The claim is removed. |
| wyaf | entry | major | Said "probably a slip … not noted in the establishment log". Pass 1 decided it is a slip and added it to the log. | Now a scribal slip for uwyaf, one letter short, with the Red Book's vwyhaf. |
| orymdeith | entry | major | Said "soft mutation after y 'his'". Unit 2 says y 'to', and l is "to walk-about". | Soft after y 'to'; used like a verbal noun. MW lemma gorymdeith (gorymdaith). |
| rywedawt, ryuedawt | entry | major | Both claimed "r written for soft-mutated rh" (an object, a fronted word). There is no mutation: the manuscript writes r for rh. rywedawt is only the w-for-u spelling. | ryuedawt (rhyfeddod), unmutated. The spelling of rywedawt is explained. |
| araued | entry | major | Called it "equative 'as slow as, however slow'", against the note's noun 'slowness'. | Glossary and note reconciled: araued has the -ed of the equative but is used as a noun 'slowness'. The unit 35 note was edited to match (below). The araf entry points to it. |
| bei | entry | major | Said bei is "also the soft-mutated form of the conjunction pei 'if'". It is not. It also gave the meaning "though he were at his stride". | bot, imperfect subjunctive, 'if it were at its step' = at a walk (unit 37). |
| pei | entry | major | Said "also appears mutated (bei, phei)". | Now: after a written phei, ffei, fei. In pei … pellaf it is like modern po (units 13, 19). |
| rygyng | entry | major | Gave 'run, impetus, rapid pace' and "take a run". The note says it is an easy gait, an amble. | 'amble, an easy gait; which gait exactly is uncertain'. |
| wrthpwythi | entry | major | Gave an invented lemma "gwrthbwyth?" with the meaning 'reply, retort', and claimed it was "soft-mutated after gattei". | Now as unit 40 has it: hard, perhaps unique, meaning uncertain. The Red Book's wrthpwyll points to 'contrariness'. 'stubbornness' is a guess. |
| ymgueiraw | entry | major | Gave the base "cweiriaw". The word is ym- + kyweiraw. | ymgyweiraw, ym- + kyweiraw 'prepare'. No modern form is given, because I was not sure of one. |
| choffa | entry | major | Lemma "cofio (cofio)". koffa is the imperative of koffau (coffáu), not of cofio. | koffau (coffáu), 2 sg. imperative. |
| gynt | entry | major | Covered only the comparative 'swifter', with the cause of its mutation "not certain". It missed no'r dyd gynt 'the day before' (unit 34). | Two senses: 'swifter', and the adverb 'before, formerly' (modern gynt). |
| gerdet | entry | major | Did not cover y gerdet 'to go' (unit 51), where it is soft after y 'to'. | Now general: soft after y 'to'; after vn (cause unclear, since kerdet is usually masculine); and in amgen urys gerdet. |
| pedestric, bedestric | entry | major | Gave 'a footman' and 'his foot-travel'. The notes call the meaning disputed ('going on foot' or 'speed'), and in this text the word is used of a horse. | Both now say the meaning is disputed, with the two readings. bedestric is soft after y 'his, its'. |
| ry | entry | minor | Its modern form "(rhy)" is the adverb 'too', a different word. This is an invented equivalent. | Modern form deleted. |
| athoed | entry | minor | Said "spelling uncertain". athoed is a regular MW pluperfect of mynet. | Says athoed beside aethoed. |
| adoed | entry | minor | Said "apparently aethoed spelled adoed". | Now "a by-form or spelling of athoed". |
| neir | entry | minor | Matched the note, but did not give the Red Book reading. | Adds that the Red Book has neur, and that the White Book's own reading is uncertain. |
| chynnwll | entry | minor | Did not say the Red Book has the word too. | Added, as in unit 33. |
| wwyta | entry | minor | Called it a slip outright. | Aligned with unit 42: listed as a slip, though the first w may be the v-letter; the Red Book has vwyta. |
| mwyf | entry | minor | Did not cite the Red Book's vwyhaf. | Added. |
| lladei | entry | minor | Gave "'he struck'". Pass 1 decided the imperfect is 'would strike'. | Now 'would strike, used to strike'. Lemma llad (lladd). |
| cael, gauas, caffwn | entry | minor | The lemma was reversed: "cael (caffael)". | caffael (cael). |
| ellwg | entry | minor | Gave the modern form as "(ellwng)". | ellwng (gollwng). |
| tric | entry | minor | Lemma "trigaw". The note has trigyaw. | trigyaw (trigo). |
| gymhellaud | entry | minor | Lemma "kymell". The MW form is kymhell (unit 54). | kymhell (cymell). |
| gerdeu | entry | minor | Gave "cerdd … plural cerdeu", which mixes modern and MW spelling. | kerd (cerdd), plural kerdeu. |
| hanwod | entry | minor | Said "cause of the h uncertain". The h- after 'm before a vowel is regular. | The hedge is removed, and the w for the v-sound is explained. |
| allu | entry | minor | Said "cause of the mutation uncertain". The unit 39 note says it is softened after oes. | Aligned with the note. |
| gywiraw | entry | minor | Said "cause uncertain". | Soft as the object of an imperative (compare arho ui, unit 56). |
| uydei | entry | minor | Gave "imperfect habitual/subjunctive … soft after fronted pellaf". | Habitual imperfect, soft after a fronted word, with the relative a understood. |
| odyno, diuyrru, enkyt, meityn, racco | entry | minor | Each said "modern form/GPC headword uncertain", or gave none, or gave an inexact form ("perhaps a variant of ennyd"). | Gives the real modern forms: oddi yno, difyrru, encyd, meitin, acw. enkyt is no longer called a variant of ennyd. meityn's meaning is aligned with unit 57. |
| threigylgueith | entry | minor | Gave the modern form "(treigylgweith)", which differs from the published entry. | Aligned with the published threigylgweith: treigylgweith (treiglwaith), with the gu spelling noted. |
| yniuer | entry | minor | Said "company/place … construction uncertain". | 'the company that we were yesterday', matching units 26 and 43. |
| unbennes | entry | minor | Gave 'queen, sovereign lady'. The house rendering is unben = chieftain. | 'lady-chieftain, lady'. |
| ohonawch | entry | minor | Said "the i … is not explained here". The i token was being glossed as 'I/me'. | Explained, with a hedge, as the 2 pl. echoing pronoun chwi with its ch run into the ending. See the i broaden and unit 8. |
| ymordiwedei | entry | minor | Said "the particle yr before it is uncertain". The note says yr is the verbal particle. | Aligned with the note. The modern form is given as cf. goddiwes. |
| gorssed, maes, bid | entry | minor | Pinned to one line ("here part of the place-name", "here 'company'", "addressed here to the youth"). | Made general: each sense or use is stated, with examples. |
| gan | entry | minor | Gave "y gan y uarch 'from the horse'". | 'from his horse'. Possession by things is covered too. |
| ford | entry | minor | Its example "yn y ford" is not in the text. | Replaced with y'r ford and yr un ford. The f-for-ff spelling is stated. |
| uwyaf, fei, ffei, phei | entry | minor | Said "construction not certain". The notes explain the construction (like po). | Aligned with units 13, 19 and 37. |
| llonyd | entry | minor | Gave only the noun 'peace'. In ual y bu llonyd ganthunt it is the adjective 'content'. | Adjective 'content, at ease', with the noun as well. |
| llamsachus | entry | minor | Gave the source "llamsach 'a leap'", which I cannot confirm. | from llam 'leap', as the note has it. |
| hebdaw | entry | minor | Said "sense 'past' not certain". The note gives 'past him'. | 'past him, without him'. |
| riannon | entry | minor | Gave a conjectural etymology (*rigantona). That is not a reader's gloss. | Removed. |
| dangosses, gwedy, eiste, kerdet, uarchoges, neu, nat, llessach, sewyll, ass, wypych, uakwyueit, makwyf | entry | minor | Small inaccuracies: "3 sg. impersonal" for elwit; neu's affirmative sense lacked neut; "page" was missing; sewyll lacked the w-spelling; and so on. | Corrected in place. The grammar matches the notes. |
| ≈60 forms (gwled, darparedic, uch, kynnedyf, kymriw, eureit, prifford, parawt, barawt, gwaret, echtoe, ysparduneu, yskynnu, yskynn, crassaw, rann, neit, trydyd, rei, hut, ryw, kyuoyth, gwrthyt, karyat …) | lemma | style | The lemma was given as "modern (modern)" (e.g. "gwledd (gwledd)"), against the published practice of MW lemma (modern). | Changed to MW lemma (modern) throughout. The examples were kept or tightened. |

### Changes — `__broaden__`

All 27 of the glosser's values began with the old entry followed by " · " (script check). I left that prefix alone and corrected the new readings.

| form | severity | what was wrong | what was done |
|---|---|---|---|
| a | major | (7) gave a'y kymriw as "perhaps 'either, or' (ai), reading uncertain". Pass 1 decided the reading. The interrogative particle (a oes? a dywedy di?) was missing from the entry altogether. | (7) interrogative particle. (8) the editorial a'y stands for ae 'either' (ae … neu), as the Red Book's ae kymriw shows: read the two halves together as ae. |
| y | minor | Said nothing on a'y kymriw. | Adds (8): 'y in a'y kymriw is the second letter of ae (see a). |
| yr | major | Did not cover yr as the verbal particle before a vowel (yr ymordiwedei, unit 35). | (3) is aligned with the note ('for all … that'). (5) verbal particle added. |
| m | major | Glossed a'm rodi as "and gave me" and called the h "cause uncertain". | a'm rodi 'and my giving' = giving me (unit 66). h- is regular before a vowel. |
| gam | major | Gave "even at his stride, reading uncertain". | cam 'step', soft after y 'his, its'. bei ar y gam = at a walk (unit 37). |
| e | minor | Added only 'from' (e wrthaw). It missed 'her' (e hymlit), the verbal particle (e deuthum), e uynyd and e ymdeith. | All of these are added. |
| uryt, welei, o, heb | minor | Small slips in wording ("idiom uncertain" for heb law, the wrong spelling ryuedawt for the text's rywedawt). | Tightened. |
| neut | major (added) | The glosser had left it unbroadened. Pass 1 decided neut is affirmative neu before a vowel, not neu + an infixed pronoun. | Broadened to say so. |
| oed | major (added) | The known entry gave only 'was'. In gwna oed a mi (unit 68) oed means 'appointment', and the note says so. | Broadened with 'appointed time, tryst', = oet. |
| i | major (added) | In ohonawch i, the known entry wrongly offered 'I/me'. | Adds (4): the probable 2 pl. echoing pronoun. |
| ac, wyr, wr, lys, wreic, uot, nys | minor (added) | The known entries named a cause of mutation, or a use, that does not fit this part: wyr only after yn; lys only after y 'his'; wreic only after a possessive; ac only before a vowel (but Ac wal, ac racdaw); nys only 'it'. | Broadened with the uses this part shows. |

### Changes — units.json

| unit | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 8 | n | minor | ohonawch i: the spaced i was left unexplained. | Adds that the i is probably the echoing pronoun chwi with its ch run into the ending. This now agrees with the glossary. |
| 35 | n | minor | araued "(araf + -ed) 'slowness'" did not say what the -ed is, so it seemed to contradict the glossary's equative. | "araf 'slow' with the -ed of the equative, 'as slow', used as a noun". Note and glossary now agree. |

I re-read the rest of the units for contradictions between notes and glossary. None remain. l and i were checked again and need no change.

### Considered and refused

- **gwedy (gwedi)**: GPC's modern headword is wedi. I kept gwedi to match the published guedy (gwedi). Literary Welsh has both.
- **allu "softened after oes" (unit 39)**: I left the note and aligned the glossary with it. Softening of the subject after oes is attested in MW, though not always.
- **Known entries a little narrow for this part** (uu "soft after a" in Pennaf neges uu; adnappo "in the negative relative"; uei "after a" in fei … uei): their main sense is still right and general, so I did not broaden them.
- **drythyll, the cause of the softening**: left "uncertain", as the note has it. I would not invent a rule.
- **Modern forms for canwelw, unbennes, pedestric, kynnwll, diuwyn, ymgyweiraw, cany, llamsachus**: left without a modern form, because I am not sure one exists. Per the brief, I did not guess.
- **kymriw (cymriw)**: kept. I believe GPC has cymriw, and the glosser and drafter agree.
- **Heueyd, uerch, hen and the other proper names**: fine as glossed.

### Verification

- gloss.json loads as valid JSON. Its keys are exactly the 230 keys of novel-forms.json plus `__broaden__`, and no value is empty.
- `__broaden__` has 37 entries. Each one is the known-forms.json entry whole, then " · ", then the new reading (script check).
- With the reader's tokenizer (r3lib.tokens), every token of every `t` has an entry in the glossary or gloss.json. No new key is unused, and none is already in the glossary.
- units.json has 72 units, and every `t` is identical to cut.json.
