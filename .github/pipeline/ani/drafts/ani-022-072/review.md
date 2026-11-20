## Pass 1

Changes are listed as unit · field · severity · what was wrong · what was done. Units are numbered from 0, as in units.json. All edits were made by script (/tmp/claude-0/reviewer1/edit.py, edit2.py), and each script asserts the old value before it replaces it.

- U0, U2, U5, U12, U13, U15–U18, U20–U22 · glyphs Z9 (19 occurrences, every Z9 printed beside the horned viper I9) · major · The small cross was coded `det` and called "not read" or "a classifier". Spell 1 says otherwise: ani-001-a calls "the small cross at the viper's head" "its horns", and ani-001-b and every other published part code the horned viper as one sign, never with a separate determinative · Each such Z9 now takes the viper's own role with empty tr: `suff` in the 17 ·f, `phon` in tp(·f) U5 and iwf U17. Every one was already in the viper's morph. The notes now say that the cross is the viper's horns as Budge's type prints them: U0 n·f, U2 im·f, U5 tp·f, U13 wnwt·f, U15 iw·f, and U17 iwf, where the draft had made it a classifier of meat.
- U15, U18, U22 · n · major · iw·f pr·f, iw·f ꜥq·f and iw·f ir·f were labelled "the construction of the future". The future with iw is iw·f r sḏm. iw·f + sḏm·f states what happens as a rule · U15 now reads "iw·f sḏm·f states what happens as a rule, and in a rubric's promise it is put in English as 'he will …'". U18 and U22 point back to it. The English renderings are kept.
- U22 · n · minor · mrt·f was described as "the man with hand to mouth and a stroke, and ·f", but no stroke is printed. The sign taken for a stroke is the viper's cross · "a stroke" deleted.
- U22 · glyphs R8[0] tr · minor · The nine flags were read psḏt, but the first flag carried tr "nṯr" · tr → "psḏt", so the nine flags write the word as a group.
- U22 · l / i · minor · l "these · Nine-gods" and i "like that Ennead of gods": nn is "this, these", and "of gods" is not written · l "like · this · Ennead · which-is · in · the-Duat"; i "like this Ennead which is in the Duat,". In the note, nn is "'this, these'", and "as in Spell 22" is now "as in line 3 of Spell 22".
- U14 · words[šꜥt] glyphs Y1, V6 · n · minor · Y1 was coded det and the cord V6 phon "š". This is not how the published Spell 125 rubric codes the same word (Y1 log šꜥ, the tied band det), and the note left the missing ꜥ unexplained · Y1 → log "šꜥ"; V6 → det. The note now says the word is written as in the rubric of Spell 125, without š or ꜥ, that the reading follows Budge, and that mḏꜣt 'book' fits the signs as well. The note was trimmed from 1751 to 1625 characters.
- U0 · n · style · 1967 characters, with a sign-by-sign repeat of things given in Spell 1 · trimmed to 1813. No reading or claim was changed.
- U0, U5, U24 · words[ꜣny] glyphs M17 ×2 tr · style · "y", "y"; every published part codes Ani's reeds "i", "i" · → "i".
- U15, U18, U22 · words[iw·f] say · style · "iuf". The published iw·f is "iuef" (125 introduction), and the 001-b review set "-uef" for ·f after w · → "iuef". (iwf 'meat' stays "iuf", as in the 125 rubric.)
- U15 · words[mr·f] glyph N36 role · minor · coded log. The note itself says the canal sign writes the verb mri "with a sign of the same sound", which is a phonogram. The hymn to Ra codes N36 phon mr · role → phon.
- U5 · p / l / n · style · p:true on a unit that continues the speech, where the note says "the speech goes on", and l "that-one" for nn · p removed (001-b review: p only on a chapter, a rubric or a new speech); l "this-one"; note "nn 'this, these' … here standing alone as a noun, 'this one'".
- U12 · i · minor · "Give me my mouth" turns into an imperative what l and the note give as a sḏm·f wish ("may-give-you") · i "May you give me my mouth, that I may speak with it."
- U23 · l / i / n · minor · l "in · properly · truly" and i "truly and properly, a million times over". The published Spell 125 rubric renders the same formula šs mꜣꜥ ḥḥ n sp as "truly · right" / "Truly right, a million times", and "over" adds a word · l "in · truly · right · a-million · of · times"; i "truly right, a million times."; the note now points to Spell 125.
- about · minor · "comes through the Pool of Flame to the god who rules the darkness": he comes *from* the Pool and has quenched it (U6), and the god hailed is the lord of light, whose title as chief of the darkness is doubtful (U7) · now "says he has come from the Pool of Flame and quenched it, and hails the lord of light, foremost of the Mansion."

Re-check after editing: units.json parses. The 562 sign codes, in order across all units, equal the packet's w0..w178. Every morph covers each glyph index of its word exactly once. Rubric and restored flags match the packet word for word (w8 R8; w77 G43 A1; w100 the four signs of ir·tw·s). The ln values follow Budge's numerals, which restart at 1 for Spell 22 and again at the Rubric. The validator will WARN twice for `phon` with empty tr: the horns Z9 in U5 tp(·f) and U17 iwf. This is deliberate, because the cross belongs to a phonetic viper; `det` would be the error corrected above.

### Refused findings
- U16 šnꜥ·tw·f, E23 coded phon "rw" while the note says the lion "is not read": this is exactly how the published 001-b codes and describes the same word. Kept for consistency.
- U7 ḥry-tp, with X1 phon "t" left out of the reading: the t is printed, and the note says why it is not read. Budge reads the group ḥert 'Great', so ḥwt ḥrt 'the upper/great Mansion', with tp + god after it, is a possible alternative that pass 2 should weigh. The reading is marked doubtful either way. Kept.
- U7 sšp from O42 (šsp): the note already says the s is not written and calls the reading doubtful. O42 may well write sšp 'light' on its own, but no lexicon may be opened to settle it. Kept, with the doubt.
- U6, U12 p:true on red lines inside the speech: these are the red section openings of the spell ("I have come …", "Give me my mouth"), like the red addresses in 001-b that carry p. Kept. U7 (the new address "Hail to you") kept likewise.
- U1 ḏd from the cobra alone; U6 nsrt; U11 dni·k tpyw-ꜥ·k; U13 šms·i and nbdt; U19 imyt ḏdw; U22 the stray n; U24 iw with no predicate: every doubt is marked in the note and in l / i. Each reading fits the signs better than any alternative. Kept.
- U2 rdi·w as the passive sḏm·w with iw ("is given"; Budge's wish noted): the grammar is sound, and the lemma sḏm·w is known. Kept.
- U3 / U16 n + passive taken as future: the note gives the past as possible, as 001-b and the 125 rubric do. Kept.
- U13 ib·i: the reading already supplies the unwritten ·i, and the note opens with "The papyrus writes ib …; read ib·i", as the published mꜣꜣ·n·i and ii·n·i precedents do. No change needed.
- U17 wr n iwf 'a great portion of meat' against Budge's "meat" for ur: the swallow writes wr, and the 125 rubric reads the same phrase the same way. Kept.
- Joins and splits (U0 ḥtp-nṯr, mꜣꜥ-ḫrw / n·f; U1 wbn·kwi; U2 rdi·w / n·i; U7 ind-ḥr·k kept whole because the cobra stands after the face; U9 ꜣḫ·kwi): each is stated in its note, and q is correctly re-indexed. Kept.
- Budge-isms: no "triumphant", "homage", "saith", "thee", "bond of regularity" or "victorious" remain in l / i. Budge's words appear only in the notes, quoted as his.

## Pass 2

Changes are listed as U<n>/gloss · field · severity · what was wrong · what was done. Units are numbered from 0. All edits were made by script (/tmp/claude-0/reviewer2/edit.py), and the script asserts each old value before it replaces it.

- gloss smꜣw · major · "perhaps 'joined, unbroken' … from smꜣ 'to unite, join'" invents a sense and a derivation, and it carried the occurrence phrase into the lemma · now "a word qualifying darkness, kkw smꜣw, perhaps 'deep, utter darkness' (?) (written with the sign smꜣ 'unite'; form and meaning uncertain; Budge: samau, 'darkness')".
- gloss ḥꜣ · minor · "from the noun ḥꜣ 'back'" is an etymology that cannot be checked, and "ḥꜣ·k 'behind you'" pinned the entry to this occurrence · now "ḥꜣ — behind, around, about (preposition; Budge: ḥa)".
- gloss qrsw · minor · "from qrs 'to bury'" stated a derivation as fact · now "(noun m.; the w often not written; cf. qrs 'to bury'; Budge: qeres)".
- gloss tpy-ꜥ · minor · "literally 'those who were before'; the blessed dead who went before" is an invented literal sense plus this occurrence's lore · now "forebear, predecessor (noun; written with tp 'head' and the arm ꜥ; plural tpyw-ꜥ 'ancestors'; Budge: ṭepu-ā)".
- gloss sšp · minor · "reading doubtful, the signs give šsp" belongs to the U7 note (where it already stands), not to the lemma. The gender "m." was also unverified · now "sšp — light, brightness (noun; Budge: seśep, 'radiance')".
- gloss nsrt, šms, ḥwt, nbdt · style · each was pinned to this occurrence ("š nsrt 'the Pool of Flame'…; reading not sure"; "sign identification not sure here"; "used of the great house of a god"; "read from its fire classifier only") · these phrases were dropped or made general. šms keeps the idiom šms ib "follow one's heart, do as one wishes", which is a sense of the lemma.
- gloss kkw, swḥt · style · Budge's spelling was missing (conventions) · added (keku, suḥt).
- gloss __broaden__ dni · minor · The noun "share, portion" was attached to the verb with "also", and it carried "dni·k 'your share'" · now "a second word of the same spelling: share, portion (?) (noun; Budge: ṭenà, 'portion')".
- gloss __broaden__ ḫt · minor · "tp ḫt 'on top of the stairs'" pinned the entry to this occurrence, and the sense was given without Budge · now "a third word: stairway, terrace (?) (noun; written with the stairway sign; Budge: χet, 'steps')".
- gloss __broaden__ wḏ · style · "the masculine noun wḏ … (from the verb)" · now "also wḏ 'command, decree' (noun m.)". The tp entry is accepted as it stands. All four __broaden__ values begin with the known entry copied whole, followed by " · " (checked by script).
- U16 · words[st] glyph X1 role · minor · coded phon. Q1 already carries st, so t is its complement, as the published 125 introduction codes it · role → comp.
- U7 · n · minor · The ḥry-tp sentence explained the unread t by agreement with ḥwt, which a noun title cannot show. Budge's alternative was not given, and "deep, unbroken darkness" repeated the invented gloss · the t is now "perhaps a feminine ending written by attraction to ḥwt". Budge's grouping is added: ḥwt ḥrt 'the Upper Mansion' would leave the head and the god sign with no place. "unbroken" was dropped.
- U14 · words[ir·tw·s] say · style · "irtus"; the house pattern is ·tw·f → -tuef, so ·tw·s → -tues · "irtues".

Items left from pass 1, now settled:
- ḥry-tp / ḥwt ḥrt (U7): ḥry-tp is kept. It accounts for every sign except the t, and the god classifier suits a title of a divine person. ḥwt ḥrt accounts for the t but leaves D1, Z1 and A40 unexplained. The reading stays marked doubtful, and the note now gives both.
- sšp (U7): kept as it is: O42 tr "šsp", reading sšp, with the doubt in the note. Whether O42 alone can write sšp cannot be checked without a lexicon.
- E23 in šnꜥ·tw·f (U16): kept as phon "rw" with the note "not read". This follows house practice (published 001-b codes and describes the same word in the same way, and the 001-b pass 1 rule lets a surplus sign keep phon tr with a "not read" note).

Fresh re-read of units.json: I checked l against the Egyptian, i against l, the grammatical labels, names, say forms, rubric and restored flags, and the ln and p values. I found nothing further.

Re-check: units.json and gloss.json parse. The sign sequence still equals the packet's w0..w178 (562 signs). Morph coverage is exact. Every morph lemma has an entry in known-lemmas.json or in gloss.json. Every gloss key is used.
