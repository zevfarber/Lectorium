# Review, pass 1 — secret-history-271-274 (§§271–274)

Scope: every unit (U0–U50, 468 words) checked against the packet, conventions.md, the glossary and the published parts. Fixes were made in place in `units.json` (JSON still valid; every `t` equals the packet exactly, 468 words, 51 units; `ln` and `p` correct: `p` on U0, U7, U37, U41; every word still carries its packet Ming gloss in square brackets). Where a lemma changed, the matching entries in `gloss.json` were synced (listed at the end). `build`/`validate` were not run (`validate` refuses before `build`).

Totals: 0 critical, 5 major, 11 moderate, 37 minor (53 changes); 13 findings refused or left as they were (plus the open doubts below).

## Changes

### Major
1. U14 · word 120 (`altan` in "altan müṅgün") · major · lemma was `Altan`, glossed "the Jin emperor's title", but the word is plain "gold" (Ming 金, between "gold" and "silver"). Now `altan` "gold (noun)".
2. U38 · word 343 (`altan müṅgün`) · major · same error; same fix.
3. U44 · word 392 (`šira altan`, "yellow gold") · major · same error; same fix. (Words 26 and 337, `Altan Qān-(n)i`, really are the Jin ruler; left as `Altan`, as in 246–254.)
4. U20 · word 189 (`bi"` in "ken bi") · major · morph said "I (first-person pronoun)", but the Ming is 有 and the sense is "who is?" (the unit's `l` and `i` already read it so). Now `bi` "is, exists (verb, perhaps a short form of bü-; Ming 有)", as the glossary's second sense of `bi`.
5. U12 · `i` · major · "the shamans were set to divine through the diviners" mistook the grammar: tölgečin-e is the dative causee of the causative tölgeleġülüġešü (Ming 卜人行 敎卜呵), so the diviners are the ones made to divine; "through" had no basis. Now "the shamans had the diviners divine, and (they found) that". Note rewritten ("were made to divine" was also a passive misreading); it now says who gives the order is not stated and that the doubled böġes is uncertain.

### Moderate
6. U12 · words 102–103 · moderate · labels contradicted themselves ("tölge- … noun-forming stem", then "tölge- verb + -le- verb-forming"). Now `tölgečin` "diviner (tölge 'divination' + agent -či + -n, as qoničin, temeġečin in the house)" + `-e` dative; and `tölge` "divination (noun)" + `-le-` + `-ġül-` + `-ġešü`.
7. U31 · `i` · moderate · an inner single quote opened at "Shamans, chant your spell!" and was never needed: Shiratori's closing mark after žügerüdkün closes Tolui's one speech, whose opening is in U21. The command is part of that speech, not a quotation within it. Inner mark removed; the note's "single outer quote" is now true.
8. U14 · `i` · moderate · tense clashed with the units round it (U13 "make trouble", U17 "grows", U18 "slackens"; adalamui, talbiramui are present): "the spirits would not let go, and made trouble". Now present, and the note says so.
9. U14 · word 129 (`talbiran`) · moderate · analysed as talbi- + "-ran, ending uncertain", while talbiramui (U18, same Ming 放) is read as stem talbira-. Made consistent: `talbira-` + `-n` converb (both tentative); note says so.
10. U44 · `i` · moderate · dropped "yellow" (širamal, Ming 黃, which `l` has) and added "cloths" and "plain" with no support in the Ming (渾金 "whole gold", 織金 "woven gold", 繡金 "embroidered gold"). Now "yellow gold, yellow gold-bearing things, whole-gold things, gold-woven things, gold-embroidered brocades". The note had also said the stems "are not known elsewhere"; darda is already in the glossary (as a brocade, Ming 渾金段子) and the note now says so.
11. U44 · word 397 (`dardas`) · moderate · morph gloss now follows the glossary ("brocade"; there 渾金段子, here 繡金).
12. U45 · word 411 (`kürgeġülžü`) · moderate · split kür- + -ge- + -ġül-, against the glossary lemma `kürge-` used in 93–99, 109–114, 140–143, 214–217, 227–229, 246–248, 254. Now `kürge-` + `-ġül-` + `-žü`.
13. U49 · note and word 457 (`Žalairtai`) · moderate · note and morph said the Ming glosses it 種(名) "people name"; the packet's Ming here is 人名. Corrected to say the Ming has 人名 here (the glossary's earlier entry has 種(名)).
14. U7 · note · moderate · said "the Ming writes the year 免, evidently a slip for 兔". This packet writes 兎兒; the 免 belongs to the glossary's earlier entry. Corrected.
15. U0 · `l` · moderate · "Čiṅgis Qaγan to-his-own-father" — the form is ečige-jüġen, reflexive only, no dative (the morph says so). Now "his-own-father".
16. `about` · moderate · claimed the princes "go west as far as the Rus" (the Ming says only 種名, and `i` keeps Orusud untranslated) and "a second force is sent to the Jurchen and Korea" (the text says "formerly", of an earlier campaign). Reworded to what the units say.

### Minor
17. U14 · `i` · double outer quotes (the quotation is not inside another one): now “Let us give …”.
18. U15 · `i` · double outer quotes for both quotations; "a man of his own line" → "a man of the line" (uruγ has no reflexive; matches U18 and `l`). `l`: the invented single quotes ‘what has-become?’ removed (not in Shiratori).
19. U42 · `i` · double outer quotes: “That land is good, and its goods are good,”.
20. U17 · `i` · "Shall we give …?" imposed a question on a hortative (-üje, `l` "let-us-give"); now "Let us give … ," (still single, inside the shamans' speech).
21. U44 · word 393 (`širamal`) · the single morph claimed "nominal -mal"; now šira + -mal (ending of uncertain force).
22. U44 · word 404 (`tobičaγ̇ud`) · lemma lost the dot: `tobičaγ̇` (as printed and as Kibčaγ̇).
23. U44 · note · added that the plural endings (-d, -ud, -dud, -sud) are parsed loosely.
24. U47 · word 428 (`Kibčaγ̇ud-i`) · lemma `Kibčaγ` → `Kibčaγ̇`, the glossary's headword.
25. U47 · word 436 (`Orusud-i`) · Orus + -ud → `Orusud` + -i, the glossary's headword (260–270).
26. U49 · `i` · "Jürched" → "Jurchen" (246–248, 253).
27. U8 · note · "Qunžiγ̇u is not found elsewhere" was wrong (in the glossary already, Ming 爛木, uncertain). Also added that the subject of U8–U9 (Jebe or Ögödei) is not named; `i` "he" leaves it open.
28. U11 · note · "Ming 到着" → 被到着 (the packet's reading; the passive the glossary already allows).
29. U13 · note · "the dead emperors … by the sense" overclaimed; now "which I take to be the spirits of the dead Kitad emperors (the Ming says only 帝(每))". Added that türgün-w has an unexplained -w.
30. U0 · `l` · Čiṅgis → Chinggis (the rest of the `l` and the published parts use Chinggis).
31–32. U2, U4 · `l` · Čaγ̇adai → Cha’adai (as 260–264; the draft mixed the two).
33. U0 · note · it said the speech "simply begins"; the English supplies "said"; now stated.
34. U5 · note · "the iležüġüi is" (nit).
35. U24 · `l` · "if-I-lose, I whose" doubled "I"; now "if-lost, I whose".
36. U34 · word 312 (`deġü-ner(i)-jen`) · split -(i) "accusative" + -jen; no accusative is meant. Now `-(i)jen`, as conventions (227–229) and as qotod(i)-jan, usun(i)-jan in this part. (Earlier parts 64–245 mostly split it; the conventions rule and internal consistency won.)
37. U34 · note · added the two doubts the draft hid: belbisün and beri-jen Berüde may be two persons, or Berüde may be a plural of beri (the Ming says 婦人名, followed); and the Ming 弟姪每 means "younger brothers and nephews", of which `i` gives the first.
38. U36 · note · "could also be Tolui's own words" contradicted Shiratori's quote mark (closed at soγtaba"); replaced by the real doubts: "so it was" for teimü is loose, žöb ese boluγsan uncertain.
39. U38 · `i` · "gold-brocaded patterned silks" → "gold-bearing, patterned silks" (Ming 金有的 紋有的; "brocaded" is not in the Ming).
40. U46 · `l` · teriġüten is printed twice; `l` now "and-so-on and-so-on".
41. U21 · word 196 (`sutu`) · the gloss asserted a formation su + -tu in a single morph; now "perhaps … uncertain".
42–53. `l` quotation marks (twelve units) · `l` must carry Shiratori's marks, straight, at the printed places (published 267–270). Added at U16, U19, U20 (replacing single marks), U21, U31, U33, U35; straight for the curly ones at U5, U43, U45, U50; removed the invented ones at U15.

## Findings refused or left open (reason)
- türgün-w (words 116, 131, 162) vs türgen-e (172): both Ming 緊行, Han 古捏/格捏 differ. Not unified: no secure basis to call -w an error; the note now states it.
- kiči-d(ud), qači-d(ud), lausa-s-ud, načidu-d: stems and plural endings are conjectures from the Ming 每; both -d and -d-ud fit the Han. Left, with a note.
- tulbalba as tulba- + -l-: uncertain, labelled so. Left.
- önečirekün, kibqaqun as "would be": matches the house reading of -qun in 265–266 (ülü odqun "will not go"); the doubt is already in the U26 note.
- ebedčin as a single lemma: the glossary has no entry and the formation (ebed- + -čin) is not certain. Left.
- alžaγdarun from alža-: kept; consistent with U4 alžaqu and the Ming 艱難.
- aldaγ̇asu "if I lose you": kept (Ming 失了呵, accusative čima-ji); the glossary's "be at fault" is a possible reading and is stated in the note.
- Asud, Sesüd, Bolarman, Kerman-Kiwa as towns: kept; follows the Ming 城名 (the note states the conflict with 267–270).
- Orusud not rendered "Rus"; Altan on words 26 and 337 not changed (precedent 246–254).
- U29 "what lay in front / outside": a gloss on -ji; honest in the note. Left.
- U1 `l` "?" (not in Shiratori): harmless; left.
- Bianliang for 汴梁 (U40 note) is outside knowledge but only reported as the Ming's gloss. Left.
- No remembered English in `i` was identified; no modern translation was consulted. I could not rule out a close echo in U27 "in the stead of", U30 "Fair of face, long of spine", U28 (the two fish).

## Open doubts (unresolved, stated in the notes)
- U0: who "sat" (Ögödei, reading by reflexive; or Chinggis); U5/U6 who sends and who appoints.
- U8–U9: the subject of the Kitad campaign (Jebe or Ögödei).
- U12: who orders the divining; the doubled böġes.
- U19: medemü-že "he knows indeed" (the sense is the Ming's).
- U26: žöb ese boluγsan (the reading of Tolui's condition) and the force of -kün/-qun.
- U28, U30: the fish names and Tolui's boast.
- U34: Berüde (a name, or a plural), the "until they are grown" guess for oin-a kürtele.
- U36: teimü "so it was", žöb ese boluγsan josun.
- U37: what "giving the boys names" means.
- U44: the kinds of horse, camel, mule; U47: Ejil/Itil.

## gloss.json entries changed to match the morphs
tölgečin-e, tölgeleġülüġešü, kürgeġülžü, orusud-i, talbiran, širamal, sutu, tobičaγ̇ud. The glosser should check that `deġü-ner(i)-jen` (now -(i)jen) and `kibčaγ̇ud-i` (lemma Kibčaγ̇) agree with the glossary on build.
