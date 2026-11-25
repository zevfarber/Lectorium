# Review — popol-vuh-011

## Pass 1

Reviewer pass 1, 2026-11-25. I read conventions.md (all of it, with the house renderings table and "The modern-letters
toggle"), runbook.md ("ACTION draft" and the Reviewer paragraph), ../run3/RUNBOOK.md §2 (Reviewer), QUESTIONS.md,
packet.md (the 12 established paragraphs and the establishment log), known-forms.json / novel-forms.json, wordre.py,
popol-vuh-001…010.json, popol-vuh-glossary.json, the 010 review (as the model of this file) and the draft units.json
(31 units). For meaning I used only Brasseur 1861 (OCR lines 22480–22760: K'iche', French and notes; also his note on
cha / chah / chaah at 22402–22422, his introduction's list of the houses at 8700–8735 and on chay at 9820, and the
Pucbal-chah note at 9061) and the published parts and glossary. I opened no modern translation and recalled none. Every
edit was made by script (json load/dump, ensure_ascii=False, indent=1). No `t` and no `mt` was changed, and no unit was
added, removed or moved. Unit numbers are 0-based.

**mt against the published parts.** I compared every mt with 001–010 by script (MS form → modern form, lowercased).
Two forms differ from a published mt, both deliberate and explained in their notes: `Xcat` xq'at 'it was cut' (unit 17;
010's xcat is xk'at 'it burned', a different word; the cut verb is 006's xquicat xkiq'at and 009's catol q'atol, with
Brasseur's g in all three) and `vchac` uchaq' 'his younger brother' (unit 17; 006's vchac is uchak 'its work'). Forms
with more than one published mt each fit their sense here: ha is ja 'house' throughout (never ja' 'water'); vcab is
ukab' 'second', not uq'ab' 'hand'; cac is kak (the unknown cac of 004:0), not q'aq' 'fire'; chi is chik only where it
stands for chic (units 23, 28); oc is ok 'enter' after xe / ma and oq after apon / apan; ca is ka where unrendered
(unit 13) and qa 'we' (unit 30); que ke, qui ki, quib kib', cu k'u, vi wi, xe xe as in the bulk of 001–010. The 55
novel forms were checked letter by letter (ꜩ tz, ꜫ q', ꜭ k', ꜭh ch', v u/w, z s, h j, b b', c/qu k): no letter is left
unrespelled. Roots agree with the published letters: tuquel, queꜫum, buchuvic, quiz (k'is), maihah, humah, huzu, muc
(muq), coloquic / colocac, ꜭohe, chuxe, naipuch / naipu, coh (koj, so cohcha kojcha), biyh, opon, vꜩihoxic.

**The drafter's flagged decisions, ruled one by one:**
- `zima` → sima (×3). Kept. The image has the plain z (the establisher compared it at 2× with the looped ligature of
  Ꜩoꜩi on the same page). Reaching tz'ima' would replace a letter, not supply a mark, and the toggle rule allows only
  supplying. It matches 010's zimah simaj and ziban sib'an. Brasseur prints tzima, and his note names the calabash tzima.
  The note says all of this.
- `ꜩoꜩ` / `Ꜩoꜩi` → tzotz / Tzotzi, not sotz'. Kept. The MS has the tz ligature at both ends. sotz' would change the first
  letter (tz → s), which goes beyond supplying an ejective, and the drafter did not supply the final tz' either. This is
  consistent with 005's rule (Tz'iis only supplied the mark on a known word). Brasseur's zotz, with s first, is noted.
- Restored ejectives: `ꜩapim` / `ꜩapin` tz'apim / tz'apin, kept: the verb tz'apij 'shut' is certain, and Brasseur's
  'enfermés' fits. The precedent is 009's ketz'ab'al / Junb'atz' (tz' on the plain ligature in a known word). `capoh`
  q'apoj, kept: Brasseur has gapoh (g = ꜫ) and 'jeune fille', q'apoj is the certain modern word, and 006's xquicat
  xkiq'at sets the precedent (plain c, Brasseur g, certain word). `vchac` uchaq' 'younger brother', kept: Brasseur
  u chag 'son jeune frère', and the note separates it from 006's uchak 'its work'. `Xcat` xq'at, kept: as 006 / 009
  above, and the note separates it from 010's k'at 'burn'.
- Letter for letter: `Roo`, `chaꜫol` chaq'ol, `cac` kak, `catah` kataj, `quil` kil, `Aon`, `naipu` naypu, `cohcha`
  kojcha. All kept. Each word is uncertain (Roo, chaꜫol, cac, Aon) or its modern form is not certain from Brasseur's
  letters (catah: Brasseur catah; quil: Brasseur gil, but the word is uncertain). naypu and kojcha follow 010's naypuch
  and the published coh → koj.
- Proposed house renderings: Jaguar House (Balami Ha), Bat House (Ꜩoꜩi Ha), House of Blades (?) (Chaim Ha), zima 'the
  calabash', hun capoh 'a maiden'. All accepted for this part, but not added to the table meanwhile, in line with 008–010.
  They follow 010's Dark House (also a description, translated) and Brasseur ('maison des Tigres', 'maison des
  chauves-souris', 'calebasse', 'une jeune fille'). House of Blades now has Brasseur's introduction behind it ('la Maison
  des Lances d'Obsidienne'). The "(?)" stays because the -im of Chaim is not explained. Listed for QUESTIONS below.

**Establishment log.** Every doubtful reading, letter decision and division is mentioned in its unit's note. That
covers cac caracoh (1); chupan (2); quichouic and qui tit (3); ꜩiꜩotic / ꜩitilahic and ꜩapin / ꜩapim (5); Roo r / v,
chaꜫol and the blot, and the zac leloh re division (6); Que with the blot (7); the struck-through word and Brasseur's
a bi (8); xhe yaoc and Xquec (10); xca quizo (11); iꜫih (12); xqui zachic / xqui ca cup (13); xchi vevah (14); xe muc vi
and Pucbal Chah (16); Xcat and vchac (17); curi che (20); zima ×3 (21, 23, 28); qui caiih (24); the q-shaped ꜭux (25);
Ma co and its division (26); quil (27); ruc (28); capoh (29); Va cute and ca (30); and the names (Chaim Ha / Chayim-ha).
None was missing.

**Brasseur attributions.** I checked each one against the OCR. All hold except unit 6's composite note on cha / chay,
which has been corrected; units 1 and 10 were made exact.

Afterwards the JSON parses; len(mt) == len(WORD_RE.findall(t)) for all 31 units; no t or mt differs from the draft; and
the units' `t`, joined in order with a space, give back the packet's 12 paragraphs exactly.

Counts: **major 0 · minor 3 · style 9** (12 rows).

### Changes

| unit | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 6 | n | minor | "(Brasseur's note: cha or chay is the arrow, the knife or the lance of obsidian; his text Chayim-ha)". No such note exists. His note on cha (at the torch, 010) gives 'the word, the arrow and the arrow point, obsidian or flint', with no knife or lance. chay 'obsidian, or the lance' is in his introduction, which also names this house Chaim-ha, 'la Maison des Lances d'Obsidienne'. The note did not cite that, though it is the best support for 'House of Blades'. | Split into its true sources: the note on cha in the last part, the introduction on chay, and the introduction's 'la Maison des Lances d'Obsidienne'. His French here ('maison des combattants') is kept. |
| 20 | i | minor | "At once the tree bore fruit". 'At once' is Brasseur's 'aussitôt'. The K'iche' has only Ta … curi 'then … then' (l "Then it-bore-fruit then tree"). | "Then the tree bore fruit". The suddenness is still in unit 25 (huzu). |
| about | — | minor | "the tree, which had never borne fruit". The text says only that it had no fruit before the head was put in it (mahabi vvach maha choco …, unit 20). | "which had borne no fruit before". |
| 6 | i | style | "nothing but chaꜫol (?)". A colonial letter in `i`, where no published `i` has one; K'iche' words in the English are written as Q'ucumatz / Ahalq'ana are. | "nothing but chaq'ol (?)". |
| 6 | n | style | "Roo 'its fifth' …: r- 'its' + o(o) 'five', taken from its place in the list". 'five' is stated as fact, although it is inferred from the list. | "r- 'its' + o(o), taken as 'five' from its place in the list (inferred)". |
| 6 | n | style | "Brasseur reads chakol". The note did not say that his k is plain q, so his reading does not support the tresillo. It also did not tie 'victors' to the chac 'beat' of earlier parts. | Both added. |
| 3 | l | style | "thus they shut-in jaguars". This reads as active, but the note gives the participle 'so they (are) shut in'. | "thus they(-are) shut-in jaguars". |
| 5 | l | style | "they shut-in bats". The same problem. | "they(-are) shut-in bats". |
| 1 | n | style | "'the north wind, the shivering of the wind'". Brasseur's note reads 'la bise ou le frémissement du vent du nord'. | Quoted exactly, with the French. |
| 10 | n | style | "Brasseur reads x-be ya-oc 'that went to be given'". The gloss is ours, but it read as his French, which is 'qu'on vous a apportés la nuit dernière'. | Reworded so the gloss is ours, and his French added. |
| 16 | n | style | "chah would then be 'ash'" gave no source for 'ash'. Brasseur's note on cha (at the torch, 010) gives chaah, with two a, as 'la cendre'. | Added. |
| 28 | i | style | "the tree whose name became the calabash". The English is awkward. | "the tree, which came to be named the calabash". |

### Refused / left

- **The flagged mt decisions** (sima, tzotz / Tzotzi, tz'apim / tz'apin, q'apoj, uchaq', xq'at, Roo, chaq'ol, kak,
  kataj, kil, Aon, naypu, kojcha): all kept, for the reasons given above.
- **Unit 17 i "only the body of the elder was buried"** where the K'iche' has xa vnimal 'only his elder': kept. The note
  marks 'body' inferred (Brasseur's '(le corps de) l'aîné'). Without it, the English would say the head was buried.
- **Unit 10 i "they were asked"** for xvꜭhax 'were spoken to': kept. The words spoken are the lords' two questions.
- **Unit 21 i "which we still call today"**: 'still' is close to Brasseur's 'encore', but vacamic 'now, today' with the
  ongoing cohcha carries it. Kept.
- **Unit 10 note, xvꜭhax "ꜭha 'speak' + passive -x"** leaves the v unexplained. It follows 010's label for xe vꜭhaxic,
  and there is no source here to settle the v. Kept.
- **Unit 28 chi 'any more' (chik)** where Brasseur reads chiri 'there' (Ma u calah chiri): kept. The MS divides chi ri,
  as unit 23's ꜭo chi vi, and the note explains chi as chic.
- **The about: "shrieking bats"**: kept. It is the summary of unit 5, whose guesses are marked there.
- **Couplets**: Apa ꜭo vi … / Aon ꜭo vi … (10), the triplet Quix camic … (13), Ma co ma … / ma co naipu ma … (26) and xqui
  catah quib / xqui quil quib (27) are all kept as pairs or a triplet in `i`. No change.
- **Names in `l` in MS spelling** (Vvcub Hunahpu, Vvcub Came): kept, as in 009 and 010.

### For QUESTIONS.md (decided meanwhile as above; nothing blocked)

1. **Drafter's proposed renderings, not added to the house table meanwhile:** Balami Ha 'the Jaguar House', Ꜩoꜩi Ha
   'the Bat House', Chaim Ha 'the House of Blades (?)' (Brasseur's introduction: 'Maison des Lances d'Obsidienne'),
   Xuxulim Ha kept as a name, Pucbal Chah kept as a name (Brasseur 'le Cendrier'), zima 'the calabash', hun capoh
   'a maiden'.
2. **Written letter against the modern word, a new kind:** ꜩoꜩ (modern sotz') and zima (modern tz'ima') would need a
   letter replaced, not a mark supplied. Decided meanwhile: letter for letter (tzotz, sima), with 010's zimah and
   ziban. If the owner prefers the known word, all of these change together.
3. **uchaq' 'younger brother' against uchak 'its work'** (same letters vchac), and **xq'at 'cut' against xk'at
   'burned'** (same letters xcat): both splits rest on Brasseur's g and the sense. The same question as 006/009's q'at
   and 007's rixk'aq.
4. **For the glosser:** the known forms used in a new sense need a broadening. These are `xcat` (xq'at 'it was cut'),
   `vchac` (uchaq' 'his younger brother'), `quil` (kil, inferred 'hold back', in xqui quil quib), `humah` ('all alike',
   inferred), `cac` (the doubtful cac caracoh), `chah` (in the name Pucbal Chah, perhaps 'ash'), `ha` (in house names,
   ja) and `co` (k'o in ma co 'let there not be'). The novel `ꜩapim` / `ꜩapin` should note the m / n spellings, and
   `zima` the plain z.
5. **For the establisher:** Brasseur's OCR here reads `PuchakChah` (22605) and later `Pucbal-chah` (22706). The pinned
   text has Pucbal Chah, so nothing changes, but the log's "B. Pucbal-chah" holds only for the second.
