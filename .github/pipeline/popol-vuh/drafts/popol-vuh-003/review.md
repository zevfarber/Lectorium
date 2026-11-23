# Review — popol-vuh-003

## Pass 1

Reviewer pass 1, 2026-11-23. Read conventions.md, packet.md (text and establishment log), popol-vuh-001.json,
popol-vuh-002.json, popol-vuh-glossary.json, the 002 review, wordre.py, hooks.py (`assemble`) and the draft units.json.
The meaning checks used only Brasseur 1861 (OCR lines 18890–19400, K'iche' and French). No modern translation was opened.
All edits were made by script. No `t` was changed, and no unit was added, removed or moved. Afterwards
len(mt) == len(WORD_RE.findall(t)) holds for all 37 units.

mt was checked against 001/002 by script: every manuscript form in this part that also occurs in 001/002 has the
same modern spelling, with three exceptions. Each is a different word, so each is right: `ꜭoh` here is k'oj (unexplained, letters
respelled; 002's `ꜭoh` 'puma' is koj), `quech` here is kech 'of them' (002's is qech 'ours'), and `vi` in pa qui vi is wi'
'head' (the particle elsewhere is wi). Every item in the establishment log (doubtful readings, letter choices, MS/Brasseur
differences, the blank leaves, the paragraph mark) is mentioned in a note. The one exception is the standing g-shape → ꜭ rule,
which conventions.md already states and which 001/002 do not repeat in their notes.

Counts: **major 0 · minor 8 · style 3** (11 rows).

### Changes

| unit | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 0, 5, 8, 11, 13, 16, 19, 24, 26, 27, 30, 34, 35 | p | style | The drafter set `p: true`. hooks.py `assemble` ignores the unit's `p` and sets it from the packet's paragraph starts. (The drafter's 13 flags did match the 13 paragraphs.) The 002 draft carried no `p`. | Removed from all 13 units. The build sets them. |
| 4 | n | minor | chel was glossed 'let it come out' (optative), but l has "shall-it-come-out", read with chi banatahic 'shall it be done'. | Note now says 'shall it come out' (ch- + el), read with chi banatahic. |
| 11 | n, i | minor | The note analysed taquentah only as a verb 'be sent, be commanded'. Brasseur divides taqen-tah, and the end may be tah, the particle of wishing, as in caꜩihon tah (unit 9). The i "be at our bidding" added an 'our' that the K'iche' does not have. | Added the tah possibility to the note. i is now "be of use, be sent". |
| 12 | n | minor | The note read ma ca hizah as both a- 'you' and the root cah 'go down' without saying how both come out of the letters (c-a-hizah leaves only hiz-). | The parse is now spelled out: ma + c- + a- 'you (one)' + cahiza, with the c of cah not written or shared. The note says that the letters do not show this plainly and that the parse is uncertain. |
| 13 | n | style | The note said chi ꜭhauic, chi ꜩihon 'that they speak, that they talk', but l has "it" and the form has no plural marker. | 'that it speak, that it talk': singular, the effigy taken as one. |
| 18 | i | style | The couplet xe binic, xe chacanic was flattened into a main verb and a participle ("wandered …, going on all fours"). | "They only wandered to no purpose, they went on all fours." |
| 21 | l, n | minor | Que ꜭhau is c- (ongoing) + e 'they', as the note itself says, but l glossed it as completive "They-spoke". | l is now "They-speak". The note adds that the form is ongoing, not completive ('they would speak, they spoke' in a telling). |
| 23 | n | minor | (a) "ca marks the ongoing state, 'they are'": ca has no plural e (compare que in unit 21), so it is singular. (b) The i's "shrunken" for the unexplained coꜩ ꜭoh was not said to be a guess. | (a) The note now says c- has no plural e, each noun taken as one, '(they) are'. (b) Added "'shrunken' in i is a guess". |
| 23 | mt, n | minor | ieioh → ieioj kept the consonantal i as i, which is not a possible K'iche' spelling. The same part respells consonantal i as y (alai → alay, ꜭuxlaai → k'u'xla'y, as the pilot's alay), and Brasseur reads yeyoh. | mt yeyoj, letters only (nothing restored, since the word is unknown). The note says what the toggle shows. |
| 31 | l | minor | vbac was glossed "the-bone(?)", but it is v- 'its' + bac, and "of-their face" supplied an 'of' that is not there. | "its-bone(?) their face". |
| 35 | n | minor | (a) "Xoc vla 'they came in'": Xoc is x- + oc, singular (l "Entered"). (b) The note gave Brasseur's note on 'showed their faces' as if it were on xcut. His note (4) is on x-qutu qui vach (MS xcute), in the next sentence. | (a) The note now says singular, the animals taken together. (b) The note now says the gloss is from his note on x-qutu qui vach in the next sentence. |

### Considered and refused

- **achih → achi (unit 28).** The final h is dropped, not respelled. But the published parts set the precedent of dropping a final h in a certain word (vleuh → ulew), and achi 'man' is certain. Kept.
- **caa → kaa (unit 36).** Ximénez's double vowel often marks a glottal stop, and 'grindstone' is ka'. But the reading is uncertain, so it is respelled letter for letter, as 002's yaa → yaa. Kept.
- **taquentah → taqentaj, vzuculiquil → usukuliqil (units 11, 13).** Choosing q for qu is a k/q choice, which the per-word mt exists to make (002 pass 1 refused the same for que → qe). No ejective is restored. Kept.
- **ꜭoh k'oj (unit 23) against 002's koj.** This is a different, unexplained word, and the note says it is not the puma. By the letter rule ꜭ → k'. Kept.
- **"let it be found" for chu rico (unit 8).** chu rico is active ('let it find'). But published 002 unit 33 renders the same phrase "Let it be found", and i should stay consistent with it. Kept. A later pass may want to revise both.
- **xa … xa pu dropped in i (units 4, 8).** In these questions and wishes, "only" in English would mislead, and the l shows the particles. Kept.
- **xcotin, xcupin (unit 31) as agent-focus or antipassive -in forms.** This may be right (x-, no person prefix, the named creature as subject), but I cannot confirm the colonial ending from the permitted sources, and the l and n already mark the senses inferred. Not added.
- **"Come hither and blush" (unit 12).** 'come' is not a separate verb (vloc is 'hither'), but the directional implies motion toward the speaker, and 'blush' follows Brasseur's 'rougis', as the note says. Kept.
- **Ah Raxa Lac → Laq (unit 2) with a plain c.** This is consistent with the pilot's Laꜫ → Laq, and the same word as lac → laq in unit 36. Kept.
- **Not in the establishment log, flagged for the establisher.** Brasseur reads ch'uxic where the MS (as established) has chuxoc in unit 13 (Utz are ch'uxic ri y poy). The text is pinned, so the notes are left as they are.
- **Per-word mention of the g-shape → ꜭ rule.** It is a standing rule in conventions.md, and 001/002 do not repeat it in the notes. Not added.
