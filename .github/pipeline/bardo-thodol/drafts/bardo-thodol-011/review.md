# Review — bardo-thodol-011 (pp. 98–107)

## Pass 1

Checked against conventions.md, packet.md (the pinned print, its 11 `# fix:` lines and the establishment log), the pilot
(units.py, ../../../bardo-thodol-001.json), the units and reviews of 009 and 010, 003 (for thugs pa'i) and 006 (for the
gatekeepers), glossary.json, and the other recension in source/raw/bowiki-other-recension.txt. No modern translation was opened.

All 45 units and the about were read word by word: original → `l` → `i`. The grammatical labels in the notes were checked
against the forms and stems: sprad / sprod, khrid / 'khrid, 'ongs / 'ong, song / 'gro, bos / bod / 'bod, bkang / 'gengs,
bzung / 'dzin, dkrugs / dkrug, bkal / 'gel, bskor / skor, blta / lta, shar / 'char, log / ldog, phral / 'phral, and the
endings -r / -ru / -du, -s, -'i, -am, the sentence-ending -o, ma … na, gyi after a verb. All are right; two notes left a stem
unnamed (u. 16, 24).
The 13 `[?]` marks of the log are each called doubtful in their units: 11 (rtsal), 13 (rig pa), 14 (bla), 16 (bzang po),
19 (bkang's nga), 21 (be), 22 (gsma; nyams and chu), 23 (tsaN+Da; bkal), 34 (na), 37 (bkang). The obscure phrase at 102.5
(u. 22) is marked uncertain in sense, as the log asks. All 11 fixes are named in their units' notes. The misprint 106.1 is in
u. 40, whose note now opens with the required sentence. The "kept, note only" items (bod la, jams pa, rig pa, phra mo, seng
ha, ro kha khye, ka ka mu kha, thugs pa'i, kyai, dngangs) and the sense differences listed in the log are all in the notes.
Every other-recension claim in the notes was checked against source/raw/bowiki-other-recension.txt, and all hold.
Cross-references were checked: 010 for mgul nas, 'khyud cing, zhal sbyor alone, the commands and dus mnyam du; 003 for thugs
pa'i; 006 for the gatekeeper names; 009 for sngar 'dris kyi mi. One was wrong (u. 9, see below).

Division was checked by script against the `w` of 002–010: each run of 2–3 adjacent 011 words joined, looked up among the
earlier words, and each 011 word split, looked up among earlier adjacent pairs. Two runs are single words in the earlier parts
(དེ་ནས, 002–004; བཅས་ཏེ, 005, 007, 008) and were joined. No other division was changed.

units.json was edited in place by script (ensure_ascii=False, indent 1, no final newline, as written; the round trip was
checked to be identical first). Letter check (all `w` joined, ' / ' and spaces removed, against `hooks.letters()`): 45 units,
4805 letters, EQUAL.

### Changes

- about · minor · "heron" for the seventh Phra men's head: the print says dur bya, "charnel bird" (heron is only the Sanskrit
  kaṅka), and u. 32 says "charnel-ground bird" · now "charnel bird".
- about · minor · "Each time the dead person is told not to fear and to recognise …, the play of awareness". Not each time
  (the gatekeepers get only "recognise", the Gaurīs only "do not fear"), and the house `i` for rtsal here is "energy" · now
  "Again and again the dead person is told not to fear them and to recognise …, the energy of awareness."
- u. 17 · w · minor · དེ་ ནས་ was two words; 002, 003 and 004 write དེ་ནས་ as one word · joined (`l` "Then," already one).
- u. 40 · w · minor · བཅས་ ཏེ༔ was two words; 005, 007 and 008 write དང་ བཅས་ཏེ as དང + བཅས་ཏེ · joined.
- u. 9 · n · minor · fact. "closes the sentence with yin no … without 'so do not fear'" is wrong for the days before: day eight
  has yin pas ma 'jigs shig, days ten and eleven yin pas mos pa gyis shig · now says the days before had yin pas, running on
  to "so do not fear" (eighth) or "so have devotion" (tenth, eleventh), and that here mos pa dang gus pa gyis shig stands alone.
- u. 40 · n · minor · the required opening ended with a colon ("corrected here: there is …") · now "corrected here." and the
  reason follows as a new sentence.
- u. 37 · n · minor · "the gatekeeper Aṅkuśā, named for the hook she holds, as in 006" contradicts the rest of the note: here
  she holds a skull-cup, not a hook · now "as in 006, named for the hook she holds there; here she holds no hook".
- u. 37 · l · style · "Iron-Hook-Woman"; 006 u. 39 has "Iron-Hook-Lady" · now "Iron-Hook-Lady".
- u. 37 · i · style · 006 gives the gatekeeper goddesses their Sanskrit names in `i` (Aṅkuśā …) · now "the white tiger-faced
  Aṅkuśā, the Iron-Hook Lady". u. 38 is left without names, because the print names those three only by face and implement.
- u. 2, 23, 24 · i / l / n · minor · "Smaśānī" in `i`, `l` and the notes of u. 2 and 23, where u. 24's own note gives
  Sanskrit Śmaśānī (śmaśāna, charnel ground) · now "Śmaśānī" throughout.
- u. 12 · l · minor · the second gyi (… ཡིན་ གྱི་ ངོ་སྤྲད་པས) had no word in `l` · now "'thus it-is' gyi(?) face-introduced",
  matching the note, which leaves its force open.
- u. 25 · i · style · ཡང, "also", was in `l` but dropped from `i`; u. 35 has "too" for the same word · now "… of the sacred
  places, too, surrounding …".
- u. 42 · l · style · `l` gave Rākṣasī and Brahmāṇī, while u. 43–44 give the Tibetan words literally (Great-God, Youth,
  Hundred-Offerings) · now "Ogress" (srin mo) and "Brahmā-Lady" (tshangs ma); `i` keeps the Sanskrit.
- u. 16 · n · style · stem unnamed · now "log, the past stem of ldog, 'to turn back'".
- u. 24 · n · style · stem unnamed · now "phral, the past stem of 'phral, 'to separate, to tear apart'".
- u. 35 · n · style · "as one stack ('ongo)": འོངོ is two stacks written as one syllable · now "as one syllable".

Severity count: major 0 · minor 10 · style 6 (16 change lines).

### Refused

- u. 2 / u. 3 / u. 18 / u. 26: ཡང, "again", is not in `i` at the head of u. 2 and in u. 18 is "So point him out again". Kept:
  010 u. 16, 24, 32 render the same formulas the same way.
- u. 1 `i` "But even when pointed out …" for ཡང་: kept, it is 010 u. 31 word for word.
- u. 2 note on sme ma (perhaps the charnel goddesses or the gatekeepers). Considered adding that it may be a garbling of the
  other recension's phra men ma; refused, the note already says it is not explained and gives the other recension's reading.
- u. 5 note "with a ma added at the front": could be read as the feminine -ma. Kept, it is 010 u. 18's wording for the same
  spelling.
- u. 10 "As on the ninth and tenth days": the ninth (010 u. 22) has a ༔ after ngo shes nas that this one lacks; the words are
  the same, so the cross-reference holds.
- u. 12: the other recension has de ltar where the print has 'di ltar (first clause), and skye ste for skyes te; not noted. Not
  a sense difference, and the log does not list it.
- u. 20 `i` Pramohā(?): kept; it is the usual name of the western Gaurī, given with a query, and the note explains it.
- u. 27–34 / u. 37–38: stag gdong, seng gdong, phag gdong, sbrul gdong ma are one word each, but stag mgo ma, seng mgo ma,
  wa mgo can are divided. Kept: the gdong forms are the gatekeepers' names, the mgo forms are descriptions (X + head-having);
  no earlier part has either.
- u. 29 / 30 note glosses ("Jackal-Faced", "Dog-Faced") differ from the Tibetan heads (wa "fox", spyang "wolf"). Kept: the
  notes translate the Sanskrit names, and `i` follows the Tibetan head.
- u. 11 `i`: the doubtful rtsal is not queried in `i`. Kept: the same word is clear at 105.1 and the other recension has it,
  so only the letter, not the sense, is in doubt.
- No English in `i` was found that reads as remembered rather than built from the words; none was rebuilt.
- Not for this reviewer: `hooks.assemble` cannot run on this part yet, because tib.py has no reading for the Sanskrit stacks
  ཀརྨ (u. 4, 6), བྷནྡྷ (u. 5, 21, 22, 33), གསྨ (u. 22), ཙཎྜ (u. 23) and ཙིཏྟ (u. 23) ("onset karm", "onset b+han+d+h" …).
  They need OVERRIDE entries in tib.py, as earlier parts added for theirs. Left for the builder.

## Pass 2

Second pass. Each of the 153 entries in gloss.json and the 9 under __broaden__ was checked against the word and its use in
units.json (w / l / i / n), against the verb stems, against the master entries of related forms (bsnams pa, bhan dha, mthong shol,
the four Krodhīśvarī and Heruka names, rang rtsal, byung, gdams pa, ljang khu, lcags kyu ma) and against 010's pass 2. Stems
checked and right: song / 'gro, bkang / 'gengs ('gengs present), dkrugs / dkrug, bkal / 'gel, phral / 'phral, blta / lta,
bzung / 'dzin, 'ongs / 'ong. Sanskrit names were checked against units.json `i` and 009/010; all match. Each __broaden__ value
begins with the master entry verbatim + " · " (checked by script). The 218 known forms were read against their uses here; one
master entry (རིགས) does not cover its use (u. 12 mtshang rigs, for rig), and a broadening was added. ཤར, ཕྱིར, ཀྱི / གི for
kyis / gis, ལ "and", མ "mother", ཞིང "corpse" (broadened), ཉམས, ཆུ, གྱི "but" are covered.

Then all 45 units and the about were read again, original → `l` → `i`, with pass 1's changes. No `w` was changed. Letter check
(all `w` joined, spaces removed, against hooks.letters(p)): EQUAL. gloss.json and units.json were edited by script
(ensure_ascii=False, indent 1, no final newline; round trip byte-identical checked first).

Coverage: `r3.py packet` was run (it rewrote packet.md, byte-identical to before); novel-forms.json has 153 keys, every one in
gloss.json, none empty, none already in glossary.json, no extra keys. `r3.py build` was not run. (tib.py shows a one-line
uncommitted change not made by this pass; untouched.)

### Changes: gloss.json

- gloss __broaden__ བོད · sense · minor · "in bod la 'and say'": bod la is "call, and"; the saying is in 'di skad do · now "as
  printed in bod la, where bos la 'called, and' stands elsewhere in the same formula: perhaps 'bod without its prefix, or the
  future bod; read 'call' (uncertain)".
- gloss __broaden__ རིགས · added · minor · master "kind, class; family, lineage" does not cover mtshang rigs (u. 12, the print's
  rigs for rig 'see') · added "as printed in mtshang rigs, the print's spelling of rig 'to see, to know' …".
- gloss __broaden__ རིག་པ · uncertainty · minor · "probably a misprint for rags pa"; the log and u. 13 say "may be" · now "perhaps".
- gloss བྷནྡྷ · form · minor · "also bhan dha, bhan+dha": bhan+dha is no spelling (EWTS b+han+d+ha) · now "in Tibetan letters,
  written in one syllable with the letters stacked; also written bhan dha, in two syllables", matching the master བྷན་དྷ.
- gloss ཕྲ་མོ · sense · minor · gave only the doubtful name; phra mo is an ordinary word, "thin, fine, subtle" (master ཕྲ) ·
  now that first, then "as printed in phra mo dmar mo, uncertain: perhaps … Pramohā; or a slip for phra men …".
- gloss གཅིག་ཏུ · uncertainty · minor · the general form was marked "perhaps … the sense is not sure"; gcig tu "as one,
  together" is plain, only u. 37's phrase is unsure · now "as one, together, in one (gcig 'one' + -tu 'as'); in thogs pa gcig tu
  the sense is not sure".
- gloss རང་བྱུང · stem · minor · "byung 'arise, come forth'" named the past as the verb · now "byung, past of 'byung 'arise,
  come about'", as master བྱུང.
- gloss བེ་ཏ་ལི · uncertainty · minor · the doubtful be ([?], u. 21) was not marked, though gsma ri and tsaN+Da li are · now
  "be is doubtful on the image, the other recension has be ta lī".
- gloss བསྣོལ · stem · style · "bsnol, 'to cross'" unnamed stem · now "past stem of snol 'to cross, interlace'".
- gloss བསྣམས · stem · style · as 010 pass 2 for bsnams par · now "past stem of snom, the respectful verb 'to take, to hold'
  (snom / bsnams / bsnam / snoms)".
- gloss བཀང · wording · style · "the last letter is doubtful on the image" pinned a line's doubt on a common word (010 pass 2
  precedent, རབ: the doubt belongs in the note; u. 19 and 37 keep it) · removed.
- gloss ལྗང་ནག · wording · style · "the colour of the karma family" pinned to Karma Heruka (Ghasmarī is also ljang nag) · removed.
- gloss ཀརྨ་ཧེ་རུ་ཀ · wording · style · "heruka 'blood-drinking wrathful deity'… of the twelfth day" · now in the master pattern
  of the other four Herukas: "(Sanskrit karma 'action' + heruka, in Tibetan letters): the wrathful form of Amoghasiddhi".
- gloss ཀརྨ་ཀྲོ་ཏི་ཤྭ་རི་མ · wording · style · brought into the master pattern of the other four Krodhīśvarīs ("īśvarī 'sovereign
  lady', in Tibetan letters, with the Tibetan feminine -ma").
- gloss མཐོང་གཤོལ · wording · style · "with a ma added at the front" · now "a spelling of thong gshol (mthong written for thong)",
  as master མཐོང་ཤོལ.
- gloss ཙིཏྟ · wording · style · "said of the heart" · now "also used for the heart, the organ".
- gloss ལྷ་ཆེན / གཞོན་ནུ / བརྒྱ་བྱིན · wording · style · "with the goddess Mahādevī / his goddess Kaumārī / Indrāṇī" was unclear
  · now "also the name of his goddess, X, one of the Īśvarīs".
- gloss ཀ་ཀ་མུ་ཁ · wording · style · clause order ("…; easily confused with Kākamukhā: one of the eight Phra men") · reordered.
- gloss __broaden__ ལྕགས་ཀྱུ་མ · wording · style · "the print also gives her a skull-cup in place of the hook" was pinned to
  u. 37 (and "also" wrong) · now "Aṅkuśā (Sanskrit aṅkuśa 'hook'), the gatekeeper of the east".

### Changes: units.json

- unit 5, 21, 33 · n · minor · "bhanḍha" (4×) writes a retroflex ḍ; the letter is dental ད (EWTS b+han+d+ha) · now "bhandha".
- unit 27 · n · style · "bsnol, 'to cross, interlace'" unnamed stem · now "bsnol, the past stem of snol, 'to cross, interlace'".
- unit 39 · i · style · ཡང "also" was in `l` but dropped from `i` (pass 1 fixed the same in u. 25; u. 36 has "too") · now
  "These four gatekeepers, too, come out …".

Severity count: major 0 · minor 9 · style 13 (22 change lines; the three Īśvarī-name glosses counted as one).

### Refused

- gloss བཟང་པོ: not marked doubtful. The doubt is of the letters at 101.4, and bzang po is a common word; the note (u. 16) has it.
- gloss ཁ (ro kha khye) and ཁྱེ: line-bound and uncertain, but these are the readings' only senses here and are kept with their
  queries, as the note asks.
- gloss གསོབ, ཁུར, གཉེར་པ: considered adding noun senses (khur "load"); the given senses are right and general enough.
- gloss གསྨ་རི "kasma rī": checked against the other recension (ཀསྨ་རཱི); right.
- unit 5 n "with a ma added at the front": kept (pass 1 refused the same; 010 u. 18 wording). Only the gloss was changed.
- unit 38 `i` without the gatekeepers' Sanskrit names: kept, as pass 1 decided.
- unit 14 `i` "But as soon as …": the contrast is the sense of the passage after u. 13; kept.
- No English in `i` was found that reads as remembered rather than built from the words.
