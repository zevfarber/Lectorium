# Review — popol-vuh-004

## Pass 1

Reviewer pass 1, 2026-11-24. I read conventions.md, runbook.md, ../run3/RUNBOOK.md §2, packet.md (the text and the establishment log),
popol-vuh-001/002/003.json, popol-vuh-glossary.json, the 003 review, wordre.py and the draft units.json. For meaning I used only
Brasseur 1861 (OCR lines 19275–19745, K'iche' and French). No modern translation was opened. One image crop
(i0020, lines 1–10) was looked at to check `vetal` against Brasseur's r'etal. I made every edit by script. No `t` was changed, and no unit was
added, removed or moved. Afterwards len(mt) == len(WORD_RE.findall(t)) holds for all 40 units, and the units' `t`, joined
in order with single spaces, give back the packet's 14 paragraphs exactly.

I compared mt with 001–003 by script. Every manuscript form here that also occurs in 001–003 has the same modern spelling, with
these exceptions:
- `chique` → chiqe ('to us', inside the speeches, against chike 'to them' in the frame). This is right, and it was one of the drafter's flags.
- `chi` → chi' 'mouth' (units 9, 10, 17). This is a different word from the preposition.
- `ha` → ja 'house' (unit 15). This is a different word from ja' 'water'.
- `oc` → ok 'enter' (unit 15). This is a different word from oq 'yet'.
- `cu` → ku (units 22, 33, 36). This is c- + v-, not the particle k'u (see below).

`ꜫaa` was the one real inconsistency (fixed below). I found every item of the establishment log (the doubtful readings, the letter choices,
the MS/Brasseur differences and the large capital A) mentioned in a note.

Counts: **major 0 · minor 13 · style 3** (16 rows).

### Changes

| unit | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| about | about | minor | It said "his teeth shine with jewels". In the text the jewels go with the bone of his face (his eyes, unit 28), and the teeth shine blue-green with stone. | It now says "the bone of his face is silver and glitters with jewels, that his teeth shine blue-green". |
| 0 | n | minor | tio was given only as 'bite'. In 003 the same verb (xtio qui tiohil) is 'ate', and if cac is Brasseur's 'fowl' then 'you ate us' belongs to the fowls. The note also left out that Brasseur read fowls in the last part's list too (qui aq, where the MS has qui caa). | Added that ti is 'eat flesh' as well as 'bite', and the fowl alternative. Added Brasseur's qui aq in 003. l and i are unchanged. |
| 1, 3 | mt, n | minor | `ꜫaa` was given as q'aa by the letter rule. That is not a K'iche' word, and it differs from 003's `caa` → kaa for the same word. The word is certain: the grindstones speak, Brasseur prints caa both times, and his note says "caa en quiché". | Changed mt to kaa in both units, as in 003. Note 1 now says why. Note 3 says the toggle shows kaa. (The full modern ka' is not supplied, so that 003 stays consistent. See refused.) |
| 3 | n | minor | "a clear double e in queech, where Brasseur prints queeh" made the double e the difference. Both have it. The difference is the c of the final ch. | "a clear double e and a final ch in queech; Brasseur prints queeh." |
| 7 | i | minor | "Were we not dying because of you?" is progressive. xoh camic is completive, and both the l and the note read 'did we not … die'. | "Did we not die because of you?" |
| 9 | i | minor | "It was we who were brought to nothing" is a cleft taken over from Brasseur's "c'est nous qui …". The K'iche' xoh zach vi has no such focus. | "We were brought to nothing;" |
| 12 | n | style | xcha was called "a second verb of saying beside xꜭha". The pilot calls xecha "the usual verb introducing speech", and Brasseur writes x-cha for both. | "the verb of xecha in the first part, written here beside xꜭha". |
| 15 | n | minor | que rah was labelled c- + e 'they' + r- + ah 'want' without saying that r- is the singular 'his, its' after a plural subject. | The note now says rah is the form of xrah in 002, and that it seems to stand as a fixed word 'want to' after a plural subject. That last point is hedged. |
| 18, 19, 20 | mt, n | minor | vetal → uetal is not a possible K'iche' spelling, because the language has no word-initial ue. By the letter rule, v before a vowel is w (waral, wa'e, winaq), and the same part gives ve → we. Brasseur prints r'etal all three times. A crop of i0020 shows a clear v. | mt is now wetal ×3. Note 18 adds Brasseur's r'etal, says that the manuscript clearly has v, and says what the toggle shows. |
| 19 | i | minor | "only wood was put into their flesh" says that wood was inserted into flesh. The K'iche' (xa che qui tiohil), and the note, say that their flesh was only wood. | "because their flesh was only wood, set there by the Builder and the Shaper." |
| 21 | mt, n | minor | hubic → jub'ik gave the wrong final consonant for a certain word (modern jub'iq' 'a little'). The note's etymology "hun 'one' + -bic" was invented. | mt is now jub'iq'. The ejective is supplied because the word is certain. The note now gives the modern word only. |
| 25 | n | minor | quiꜭohe was labelled c- + in 'I' + ꜭohe without saying that the n of in is not written. As written, qui- is the shape of 'they'. In the same speech quinel keeps the n. | The note says the n is not written, gives qui poco (002, x of ix dropped) and quinel as the comparisons, says that the In before it decides the person, and gives Brasseur's future 'I shall be great once more'. |
| 27 | n | minor | It misquoted 002 as "on four feet you shall walk, on four feet you shall stand". 002 has cahcah ibinibal, ychacabal 'on all fours your walking, your standing'. | The note now quotes 002's words and its l. |
| 28 | n | style | ve 'teeth' did not show Brasseur's division v'e, which is the evidence for a prefix. | Added "who writes v'e, that is v- 'its' + e". |
| 37 | n, l | minor | xuraih was analysed as x- + v- + raih "a form of ah 'want' (as in xrah)". That leaves an r- after the v- 'he'. Brasseur's French has 'désirait'. | The note now takes raih as its own verb 'desire, long for', says the analysis is inferred, and explains why it is not ah. l "he-wanted" → "he-desired". |
| 39 | n | style | "as vbanatahic in the preamble". That word is in the last line of 001 (…rutzinic vbanatahic cumal), not in the preamble. | "in the last line of the first part". |

### Checked and kept (drafter's flags and other findings refused)

- **cu → ku before nimarizah and cobizah (units 22, 33, 36).** Kept. A bare nimarizah after the particle k'u would be a stem with no aspect or person. c- (ongoing) + v- 'he' gives the regular ku-, and Brasseur himself writes c'u nimarizah, xere-c'a nimarizah and c'u cobizah, marking the c- off from u. The notes and l say so.
- **quiꜩih → qitzij (unit 33).** Kept. qitzij 'true, truly' is a certain word. The qu is the uvular here, and Brasseur's quitzih agrees.
- **Restored ejectives.** All kept, because each word is certain in context:
  - q'aq' 'fire' (units 11, 13; Brasseur gag).
  - xk'ub' 'hearthstone' (Brasseur qixcub, his q = k').
  - aq'anik / aq'an 'climb'.
  - ch'umil 'star'.
  - ik' 'moon'. This includes rik'il and ik'il, where the parallels with vꜫih, vzac and chi ꜫihil decide the reading.
  - k'ax 'pain'.
  - chuq'ab' (as 002).
  - k'utun and q'alajob' (as 001).
- **chique as chiqe and chike.** Kept. 'to us' inside the dogs', grindstones' and pots' speeches, 'to them' in the frame. Each is right where it stands.
- **cac: kak (unit 0) against q'aq' (unit 11).** Kept. These are two different readings. In unit 0 the word is uncertain (the 'fowl' of Brasseur, or something else), so the letters are respelled and nothing is restored. In unit 11, chuvi cac 'on top of the fire' next to pa ꜫaꜫ in unit 13 makes 'fire' certain.
- **ꜫaa as full modern ka'.** Not done. 003 printed kaa for caa, and 003's review refused ka' while the reading was uncertain. Changing only this part would split the word between two parts. If ka' is wanted, change both together in a later pass.
- **calibal, tocol, vcayohic, cuval, coconic with k where Brasseur has g or q.** Kept. The meanings are inferred, so the letters are respelled (c → k), as 003 did with cahizabal.
- **"you bit us" in unit 0's i.** Kept, because it is Brasseur's 'vous nous mordiez' and the dogs are named. The note now gives the other reading.
- **"your stick … for us" in unit 5's i against l "our stick".** Kept. ca cheel is 'the stick for us', and i gives the sense. l shows the possessive.
- **"Great is my light" (unit 27) against the house "the clear light" for zaquil.** Kept. The house phrase belongs to the creation's zaquil. Here it is the macaw's boast of his own brightness, and unit 31 does use "the clear light".
- **Unit 13's i follows one of the two readings the note gives.** Kept. The note says both are uncertain, and i cannot hedge.
- **Unit 2's "when you were people still".** Kept. The note gives Brasseur's opposite reading and says the line is uncertain.
- **Remembered English.** I found no phrase that I could not rebuild from the K'iche' words and Brasseur. "gleams white from afar, like the moon" comes straight from zac-, chi nah and queheri ic.

### For later steps

- **House table.** Vucub Caquix is a new name. Its rendering (l Seven Macaw, i Vucub Caquix, the name kept, the MS spellings Vvcub / Vucub both printed) should go into conventions.md's table at build.
- **Glosser.** These known forms are used in new senses and need `__broaden__`:
  - `chique` (also chiqe 'to us').
  - `cu` (also ku-, c- ongoing + v- 'he').
  - `ha` (also ja 'house').
  - `chi` (also chi' 'mouth').
  - `caa`. Its "(uncertain)" can now cite the grindstones' speeches. The tresillo spelling `ꜫaa` gets mt kaa.
  - New keys must match the mt as now set: wetal, jub'iq', kaa.

## Pass 2

Reviewer pass 2, 2026-11-24 (a different reviewer from pass 1). I read conventions.md, runbook.md, ../run3/RUNBOOK.md §2,
packet.md, units.json and gloss.json as left by pass 1, pass 1's review, popol-vuh-001/002/003.json, popol-vuh-glossary.json,
novel-forms.json, known-forms.json, the 003 review and wordre.py. For meaning I used only Brasseur 1861 (OCR lines 19275–19745,
K'iche' and French); no modern translation was opened or recalled. I made every edit by script; no `t` was changed and no unit
was added, removed or moved.

I went through all 40 units again: every grammar label against its form, K'iche' → l word by word, l ↔ i, the house table,
every mt against its MS word (by script against 001–003 and against the glossary heads), and every cross-reference in the
notes against the published parts (xtio, xcut qui vach, ronohel xcute qui vach, qui mayxic/qui cutuxic, vbac qui vach and
qui caa in 003; cacha, qui poco vi ivib, mixix, tihtobeh, xrah, chuꜫab, cahcah ibinibal, ychacabal, Hupacha, ca byih and
xe chacatah in 002; vcutunizaxic/vcalahobizaxic, xecha, ta chuxoc and vbanatahic in 001). One cross-reference was wrong.
The units needed little after pass 1. The gloss needed more: it was written before pass 1's edits, and three of its modern
forms were stale.

Then I checked every gloss.json entry against the text and the final mt. After the edits, the modern form at the head of
every entry (and of every reading in each `__broaden__` value) matches the mt of that word in units.json, script-checked.

Counts: **major 3 · minor 21 · style 5** (29 rows; units 3, gloss 26).

### Changes — units.json

| unit | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 13 | i | style | "came rushing out of the fire straight at their heads": nothing in the K'iche' gives "straight", and the line is already a guess. | "came rushing out of the fire at their heads". |
| 20 | l, n | minor | l "in its-showing-a-face" and n "'in its appearing'". chi vachinic has no possessive prefix, so "its-" was not in the form. | l "in showing-a-face". n "chi vachinic 'in appearing, in looks' (no possessive prefix)". |
| 24 | n | minor | "vꜭoheic 'its being', as qui ꜭoheic in the second part". qui ꜭoheic is in the first part (001, `E nimac etamanel, e nimac ahnaoh chi qui ꜭoheic`), and it is not in 002. | "in the first part". |

### Changes — gloss.json

| key | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| ꜫaa | value | major | Head q'aa: stale (pass 1 set mt kaa), and q'aa is not a K'iche' word. | "kaa — grindstone, the metate on which maize is ground (fully modern ka'); noun, caa written with the tresillo". |
| vetal | value | major | Head uetal: stale (mt wetal), and impossible as a spelling. | "wetal — its sign, its trace; v- 'its' before a vowel + etal 'sign, mark' (modern retal; Brasseur r'etal); etal also 'descendants'". |
| hubic | value | major | Head jub'ik: stale (mt jub'iq'). The etymology "jun 'one' + -b'ik" was invented, and pass 1 had already removed it from the note. | "jub'iq' — a little; adverb". |
| xuraih | value | minor | "he wanted … raij, a form of aj 'want' (as in xrah)": the analysis pass 1 rejected, because it leaves the r- after u- unexplained. | "he desired, longed for; x- + u- 'he' + raij 'desire' (inferred; Brasseur 'désirait'), not a form of aj 'want'". |
| cac | value | minor | The first reading described the draft ("a word the draft leaves out of the idiomatic line"), not the form. | "kak — (uncertain) meaning not known; the letters respelled. Brasseur takes it as ac 'fowl, turkey'". The fire reading is unchanged. |
| hule | value | minor | It ended "left out of the idiomatic line", which is about the draft. | That clause is removed. Brasseur's reading of vetal hule vinac is kept. |
| icouen | value | minor | "(guess) to surpass … 'to rise above all' is a guess", which quoted the draft's i. | "(uncertain) not otherwise known; Brasseur nimaliqouen 'to surpass', perhaps from a verb of passing". |
| __broaden__ vxic | value | minor | The new reading ended "'finery' in the idiomatic line is a guess", which is about the draft. | "(uncertain) finery, precious stones (Brasseur 'pierreries'), or perhaps xik' 'wing'; paired with vpuvac 'his silver'". The old entry is kept whole in front. |
| __broaden__ ꜫih | — | minor | The "new" reading "q'ij — sun" is already in the glossary entry ("day, sun"), so this was not a broadening. | Removed. |
| xcha | value | minor | "second verb of saying beside xch'a": pass 1 corrected this in the note. The glossary's xecha is "x- + e- + cha 'say'". | "x- completive + cha 'say', the singular of xecha". |
| rah | value | minor | "r- + aj 'want'" did not say that r- is the singular after a plural subject. | Now matches note 15: r- 'his, its' + aj, the form of xrah, apparently fixed after a plural subject, with the wanted act following. |
| chucab | value | minor | "our strength": the 'our' is ca, a separate token. It also cited the toggle, which is about the reader, not the form. | "chuq'ab' — strength, force; noun, written with plain c (ca chucab 'our strength'); compare chuꜫab 'on the arm of'" (the glossary's 002 entry). |
| naquipa | value | minor | "what for, why": the 'why' comes from naquipa rumal, not from naquipa alone (note 4). | "naqipa — what; naqi 'what' + pa, in naquipa rumal 'why, for what reason'". |
| cati | value | minor | "we shall bite": the 'shall' is in xquix, not in cati. | "qati — we bite (you); qa- 'we' + ti' 'bite, eat flesh'", with the doubtful reading stated as the log gives it. |
| catio | value | minor | "we shall eat": same problem as cati. | "qati'o — we eat, bite (you); qa- + ti' + transitive -o (xquix catio 'we shall eat you')". |
| xquix | value | minor | "(doubtful reading, as in xquix cati chic, xquix catio)" called both occurrences doubtful. Only cati is doubtful, and xquix catio is clear. | xk- 'shall' (xchi- before a vowel) + ix 'you (pl.)', the object, before a verb with its own subject prefix. The doubt is moved to cati. |
| itio | value | minor | "bite" only. Pass 1 added 'eat flesh' to note 0, and 003's xtio (glossary xti'o 'ate, bit into') is the same verb. | "iti'o — you (pl.) bit, ate (us); i- + ti' 'bite, eat flesh' + transitive -o, as xti'o". |
| xbutic | value | minor | "x- completive + b'utik 'flood'" put the -ik inside the root. | "x- completive + b'ut 'flood' + -ik". |
| vꜭoheic | value | minor | "as qui ꜭoheic in the second part": the same wrong reference as unit 24. | "in the first part". The head uk'oje'ik is kept, as in the glossary's ꜭoheic. |
| quiꜭohe | value | minor | It did not say that the n of in is not written, which is the point of note 25. | Added that the n is not written and that, as written, qui- is also the shape of 'they'. |
| quiloc | value | minor | "their being seen": 'their' is the separate token qui. | "seeing, being seen (uncertain; form not clear); qui quiloc 'their seeing'". |
| xbanatahic | value | minor | "as ub'anatajik in the preamble": that word is in the last line of 001, and pass 1 corrected this in note 39. | "as vbanatahic in the first part", and the root is given as b'anataj 'be done'. |
| xoh | value | style | "(did it to us)" was a draft paraphrase. | "we, us (completed action); x- + oj, the absolutive, before the verb (xoh camic 'we died')". |
| hutaꜫih | value | style | "(doubled in the text)" pinned the entry to a line. | Removed. |
| vaic | value | style | "eating, ate": -ik makes a verbal noun, and the 'ate' came from the line. | "eating". |
| nimarizah | value | style | "-ariza 'make'" did not match the head nimarisaj. | "causative -arisaj", with the reflexive use given generally. |

### Checked and kept / refused

- **`caa` in `__broaden__`.** Not added. caa is a known form, but it does not occur in this part, which writes only ꜫaa, so there is no use here for a broadening to cover. A broadening can only add to an entry. It cannot take out the old entry's "(uncertain)". The new entry for ꜫaa gives the word as certain, without the hedge. If the caa entry should lose its "(uncertain)", that is an edit to the work glossary at build. It is not a `__broaden__`.
- **Pass 1's requested broadenings.** All present and exact (old entry whole + " · " + new reading, script-checked): chique (chiqe 'to us'), cu (ku-), ha (ja 'house'), chi (chi' 'mouth'). Also va (wa 'food'), coh (koj ongoing), oc (ok 'enter'), ve (teeth, uncertain), vxic and ꜫihil, each a sense the old entry lacks.
- **Coverage.** Every key of novel-forms.json has an entry, and gloss.json has no key outside it. Every token of the text is in the work glossary, known-forms or novel-forms.
- **"the people built, the people shaped" (units 16, 20, 25) against the house i "a person built, a person shaped".** Kept. In these units the phrase names the wooden people already made and now ruined, so the plural is the sense. 002 uses the singular because it speaks of the person still to be made.
- **qui quiloc → kiloq (q, not k).** Kept. Brasseur's qu'iloc does not decide between k and q. Ximénez's verbal -oc is -oq elsewhere (chuxoc, zaquiroc), and the note says the form is not clear.
- **Unit 28 i "my teeth" against note "v- 'its' + e".** Kept. The speaker is the macaw, and Brasseur reads "mes dents". The note already says that the reading of ve is uncertain.
- **Unit 25 i "I stand now above".** Kept. ꜭohe 'be, be there' with chuvi 'on top of' is a position. 'stand' adds no claim that the l "I-am … on-top-of" lacks.
- **Unit 34 l "Only" for xere (elsewhere "Thus").** Kept. xere covers both 'just so' and 'only this' (note 6, glossary), and here it introduces a limitation.
- **Examples inside gloss entries** (e.g. ca chucab, que rah, chi qui holom). Kept. They illustrate the form in MS spelling, as the published glossary's entries do. They do not stand in for the meaning.
- **ꜫaa as full modern ka'.** Not changed, for pass 1's reason (consistency with 003's caa → kaa). The gloss mentions ka' as the fully modern form.

### Verification (script)

units.json and gloss.json parse. len(mt) == len(WORD_RE.findall(t)) for all 40 units. The units' `t`, joined in order, give back
the packet's 14 paragraphs exactly, paragraph by paragraph. All 128 novel forms are keyed in gloss.json. Every `__broaden__` value
begins with the existing glossary entry whole + " · ". The head modern form of every gloss entry agrees with the mt of that word.
