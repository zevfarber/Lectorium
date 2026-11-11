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
