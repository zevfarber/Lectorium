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
