# Review — bardo-thodol-010 (pp. 90–98)

## Pass 1

Checked against conventions.md, runbook.md ("ACTION draft", Reviewer) and ../run3/RUNBOOK.md section 2 (Reviewer), packet.md
(the pinned print, its 19 `# fix:` lines and the establishment log), establish-log.md and readings/ (BRIEF, the three reader
logs, witness_ga.txt), the published units of 001–009, the reviews of 008 and 009, glossary.json, and the other recension in
source/raw/bowiki-other-recension.txt. witness_ga.txt was checked to be the same text as the stored recension from
འདི་དང་བཏགས་གྲོལ་གཉིས onward, and every other-recension claim was checked against it. No modern translation was opened.

All 39 units and the about were read word by word: original → `l` → `i`. Every grammatical label in the notes was checked against
the form and the verb's stems: bsgrags / sgrog, btags / 'dogs, bstan / ston, bya / byed, bos / 'bod, shar / 'char, byung / 'byung,
skyes / skye, bros / 'bros, btegs / 'degs, bkang / 'gengs, sbyor / sbyar, bsgom / sgom, thon / 'thon, and the imperative
particles shig / cig. All are right; one note left a stem unnamed (u. 20).
The 16 `[?]` marks of the log are each said to be doubtful in the unit that has them (1, 2, 4 (×2), 6 (×2), 7, 8 (×3), 11 (×2),
18, 25, 34, 39). The uncertain senses are marked as not sure in the notes: zangs yag, bshugs, thug chom, rnge chung, and the
kro ti spelling. Each of the 19 fixes is named in its unit's note, and none of them is a misprint. The "kept, note only" items
and the sense differences in the log that fall in pp. 90–98.3 are all in the notes; 98.3–5 belongs to part 011.
Unit 9 keeps its `gap` field ("p. 92 l. 1: Buddha Heruka's last left-hand implement …"), and its note covers both the two
unreadable stacks after ཐ་མ་ and the uninked blank of about a word's width after བར་བ་ན་ on 92.1. Nothing is written for either.

Division was checked by script over the `w` of 001–009. Each 010 word, and each run of 2–4 adjacent 010 words, was looked up
among the earlier words. No run of 010 words is one word in 001–009, and no 010 word splits into two earlier words in a way the
earlier parts use. The joined forms ཞལ་དུ, ཡི་དམ་དུ, དུས་མཉམ་དུ and ཞལ་སྦྱོར follow the earlier practice (དུས་སུ, ཕན་ཆད་དུ,
ཞལ་སྦྱར), and ཡི་དམ་ གྱི་ ལྷ and ཞེས་ བྱ་བ are divided as before. No division was changed.
Renderings were compared with 001–009 by script. The house renderings are kept: between / bardo, face-introduce / point out,
blood-drinker, knowing / awareness, child of noble family.

units.json was edited in place by script (ensure_ascii=False, indent 1, no final newline, as written; the round trip was checked
to be identical first). Letter check (all `w` joined, ' / ' and spaces removed, against `hooks.letters()`): 39 units, 4348
letters, EQUAL. Then hooks.assemble and hooks.validate were run in memory with an empty part glossary. They gave no error other
than "no glossary entry" (168; the glosser has not run) and no WARN. `python3 ../run3/r3.py packet bardo-thodol
bardo-thodol-010` was rerun: 107 novel forms, 153 known.

### Changes

- about · minor · "each … dawns from his own quarter of the brain; each time the same words are spoken" is wrong twice.
  Buddha Heruka dawns from the east, which the note of u. 11 says is not his quarter, the centre. And day nine lacks the
  "recognise him as the form of your own awareness" sentence · now "dawns from a quarter of the dead person's brain; each time
  nearly the same words are spoken".
- u. 3 · i · style · ཡང་, "again", is in `l` but was dropped from `i` · now "Again call the dead person …".
- u. 4 · i · minor · "The peaceful bardo dawned before you" reads as "in front of you". གོང་དུ is "earlier" (l "before-at") ·
  now "Earlier the peaceful bardo dawned for you".
- u. 4 · n · style · the note did not say that the print itself has the same formula earlier (003 u. 19
  འདིར་འཁྱམས་དགོས་བྱུང་བ་ཡིན་ནོ). That supports the doubtful དགོས་བྱུང · now says so.
- u. 11 · l · minor · ཉི[?] had no word in `l`, so the literal line dropped a word · now "own's manifest itself(?) just-that like
  dawns"; the note now says that the idiomatic line leaves it out and the literal line gives it as "itself(?)".
- u. 15, 23 · l · style · བསུ་བ་ལ་འོང was "welcoming-for comes". In 004–008 the formula is "meeting for come" every time (004
  u. 11, 35; 005 u. 16, 44, 45; 007 u. 36, 37, 40; 008 u. 8) · now "meeting for come-because".
- u. 32 · l · style · the same for བསུ་བར་འོང · now "meeting-to come-because".
- u. 15, 16 · i · style · u. 15's `i` ended with a dangling "So", and u. 16 began a new sentence, "Point him out again." · the
  "So" is moved: u. 15 ends "… come to meet him.", and u. 16 is "So point him out again. …".
- u. 23, 24 · i · style · the same dangling "So" · moved the same way.
- u. 20 · n · minor · stem. "thon, 'to emerge'" did not name the form · now "thon, the past stem of 'thon, 'to emerge'".
- u. 22 · n · style · "it has a ༔ after ngo shes nas" left unclear whether "it" is the print or the other recension. Both have
  the ༔ (other recension ཡི་དམ་དུ་ངོ་ཤེས་ནས༔) · now "like the other recension, the print has a ༔ after ngo shes nas".
- u. 25 · i · style · རབ[?] is doubtful, and `l` marks it "intensely(?)", but `i` gave "blazing fiercely" with no mark. u. 7 and
  u. 34 mark their doubts in `i` · now "fiercely(?)".
- u. 37 · n · minor · fact. "where the other days have khyod rang gi" is wrong for day nine, which has no such sentence (the
  note of u. 21 says so) · now "where the eighth and tenth days have khyod rang gi … (the ninth has no such sentence)".

Severity count: major 0 · minor 5 · style 8 (13 change lines, covering 17 field edits: some lines cover two units).

### Refused

- ma skrag cig "Not be-afraid!" in place of 003's "Not be-frightened!". Refused: 008 u. 14 already has "Not be-afraid!", so the
  draft follows the latest published usage, and the sense is the same.
- "dngangs is the print's spelling" (u. 12). It could be read as saying that dngangs is non-standard, when the other recension's
  sngangs is the variant. Refused: the phrase is the editor's wording from the establish log, and it is used the same way in
  the parts before.
- u. 8: "kyi … where kyis is meant". It was checked: kyi for the instrumental is a common print habit, and the other recension
  has gyis. The note is right as it stands, so nothing was changed.
- u. 23 / u. 31: `i` turns the `ma … na` "if" clauses into statements ("those … do not recognise. For them …"). Refused: `l` keeps
  the conditional, and the sense is the same.
- u. 11: rdo rje 'bar ba'i spu seb, read in `i` as "hairs, which blaze like vajras". Kept: the note gives the other reading.
- The gaps.json entry that the establish log asks for, for u. 9. Not done: it is a repository-level file outside units.json, and
  editing it is not this reviewer's job. The `gap` field on u. 9 is present and correct; the entry is left for the builder or
  editor.
- No division was changed and no `w` letter was touched.

## Pass 2

Second pass. Each of the 107 entries in gloss.json and its one broadening (རབ) was checked against the word and its use in
units.json (w / l / i / n), against the stems of the verb, against the master entries of related forms (bsnams pa, sbyor, sbyar,
zhal sbyar, stug po bkod pa'i, ngo sprad, bsgrags pa'o) and against glossary.json style. The specific items were each checked:
- bsgrags / sgrog: right (sgrog / bsgrags / bsgrag / sgrogs).
- btegs / 'degs: right.
- bkod / 'god: wrong (see below).
- sbyor / sbyar: wrong (see below).
- bsnams: no stem was given (see below).
- thong gshol / mthong shol "plough": thong gshol is the plough, and the sense is right. mthong shol is now given its parts.
- The four Krodhīśvarī names: the sense is right, but the parts are now given as krodhī + īśvarī.
- bsgrad pa / bgrad pa: right. bsgrad pa is marked uncertain and pointed to bgrad pa, and neither entry claims a stem.

The master entries of the 153 known forms used in this part were read by script against the units where each occurs. One master
entry does not cover its use here (ཕྲ, "inlay"), and a broadening was added for it. ཤར "east", ཕྱིར "back", ཀྱི for kyis, གིས
"by", ལ "on" and ཡང "again" are already covered. Every other-recension claim in the notes was checked again against
source/raw/bowiki-other-recension.txt, and all of them hold. Among them, u. 1's 'phra is right: the establishment log's "ཕྲ too" is
the slip, not the note. The cross-references to the published parts were checked: 003 for ma dngangs shig, 004 for zhal sbyar,
009 for yi dam gyi lha yin par, and 004 / 005 for the days of Vajrasattva, Ratnasambhava and Amitābha. All are right.

Then all 39 units were read again from the original through `l` to `i`, with pass 1's changes. The grammar labels in the notes
were checked against the form, and the notes against the glosses. None of these contradicts the other. No `w` division was
changed. Unit 9 keeps its `gap` field.

gloss.json was edited by script (ensure_ascii=False, indent 1, no final newline). A round trip was checked to be byte-identical
first. units.json was not edited. Key check: the gloss.json keys equal novel-forms.json (107). None is in the master glossary and
none is empty. Each broadening begins with the master entry whole + " · ". The source sha256 matches. R.common_checks,
hooks.assemble and hooks.validate were run in memory, with gloss.json merged as `r3.py build` merges it and nothing written. The
result: 39 units, 0 errors, no "no glossary entry". There is 1 WARN: u. 11's note is 1912 characters, see Refused. `r3.py build`
was not run.

### Changes: gloss.json

- gloss བཀོད་པ · stem · minor · "bkod, past and future stem of 'god". The future is dgod ('god / bkod / dgod / khod) · now "past
  stem", with the four stems. "inlaid" is dropped, because it was this line's sense; the entry is now "set, arranged, set out".
- gloss ངོ་སྤྲད་པར · stem · minor · "ngo sprad, past stem of ngo sprod". sprad is the past and future stem (sprod / sprad / sprad /
  sprod), and with bya, the future of byed, it is the future here · now "the past and future stem of sprod", with the four stems.
- gloss ཞལ་སྦྱོར · stem · minor · "sbyor, present stem of sbyar". That makes sbyar the verb. The verb is sbyor, whose past and future
  are sbyar, as in the master entry སྦྱོར · now "sbyor, the present stem of sbyor 'to join' (sbyor / sbyar / sbyar / sbyor)". zhal
  is marked as respectful, and the entry points to zhal sbyar, which uses the past stem.
- gloss དབུ་སྐྲ · parts · minor · "(the respectful words)". skra is the plain word for hair; the compound is respectful through dbu ·
  now "the respectful word (dbu 'head', respectful, + skra 'hair')".
- gloss བསྣམས་པར · stem · style · bsnams was given only as "the respectful word for 'hold'" · now "past stem of snom, the respectful
  verb 'to take, to hold' (snom / bsnams / bsnam / snoms)".
- gloss ཁཊྭཾ་ག, ཁ་ཊྭཾ་ག · wording · style · "here spelled in two / three syllables" was pinned to a line · now "written in two
  syllables, khaTwaM ga; also written kha TwaM ga", and the converse.
- gloss ཞེས་པ · wording · style · "the (sound) called" was pinned to u. 8 · now "so called, what is called (zhes 'thus, so', closing a
  name or a quotation, + -pa)".
- gloss བར་མ · sense · style · "the print's other spelling of bar pa". bar ma is a regular form, "the middle one", and not a
  misspelling · now "(bar 'between, middle' + -ma), the same as bar pa". བར་བ is kept as it stands: it is the print's ba for pa.
- gloss མཐོང་ཤོལ · parts · style · no parts were given · now "a spelling of thong gshol (mthong written for thong, shol for gshol);
  the reading is doubtful".
- gloss བུདྡྷ- / བཛྲ- / རཏྣ- / པདྨ་ཀྲོ་ཏི་ཤྭ་རི་མ · parts · style · "krodha 'wrath' + īśvarī 'lady'" does not give krodhīśvarī.
  krodha + īśvarī would be krodheśvarī · now "krodhī 'wrathful', written kro ti, + īśvarī 'sovereign lady'" in all four.
- __broaden__ རབ · wording · style · "the reading there is doubtful" was pinned to u. 25 (the doubt belongs in the note) · now
  "best, highest · very, intensely, before a verb or adjective (rab 'bar ba 'blazing intensely')".
- __broaden__ ཕྲ · added · minor · the master entry "subtle, fine, thin" does not cover g.yu'i phra, "turquoise inlay" (u. 1, as its
  note has it) · now "subtle, fine, thin (phra) · inlay, fine inset work (phra): g.yu'i phra 'turquoise inlay'".

### Changes: units.json

None.

Severity count, pass 2: major 0 · minor 5 · style 7 (12 change lines; 17 entries touched: 15 edited, 1 broadening rewritten, 1
broadening added).

### Checked and confirmed (no change)

- Stems and respect labels in the gloss:
  - bsgrags (pas, par): past of sgrog.
  - sgrog pa: present.
  - btags: past of 'dogs.
  - bstan: past and future of ston.
  - btegs: past of 'degs.
  - bkang: past of 'gengs.
  - bsgom shig: bsgom, future of sgom, with the command.
  - Respectful words: dbu, zhabs, spyan, gzigs, mgul, zhal, bzhugs.
- Uncertain readings and guessed senses marked as such: bsgrad pa, zangs yag tu, ha ha'i, sha'u, bshugs, stob pa, thug chom, spu
  seb, nyi, rnge, mthong shol.
- ཐོང་གཤོལ "plough": right, and general to the form.
- The notes' labels are the same as the glosses': sbyor in u. 36, bsgom in u. 36, btegs in u. 11, bkang in u. 34, bsgrags in u. 1
  and u. 14, thon in u. 20.

### Findings considered and refused

- u. 18 `l` "plough(?)" against `i` "a plough", which has no mark: the mark in `l` is for the doubtful letters, and the note says the
  sense is clear. In u. 25 the doubt was over a word that changes the sense. Kept.
- u. 6 `l` "spread-wide(?)" against `i` with no mark: the same reason. The note says the sense is the same either way. Kept.
- u. 10 note "(krodha, 'wrath'; īśvarī, 'lady'); kro ti is the print's spelling of krodhī": it is loose, but it names krodhī and is
  not wrong. Kept. The gloss entries now give the parts exactly.
- gad rgyang, perhaps usually written gad rgyangs: not sure enough to add. Left as the glosser has it.
- A stem for bgrad / bsgrad, and for brkyang / bskum in brkyang bskum du: the stems were not certain enough to state. The entries
  give the sense and the parts only, which is safe.
- WARN: u. 11's note is 1912 characters. It carries six doubtful or variant points (thug chom, tsam pa, spu seb, gis, east / inside,
  nyi) that the establishment log requires. Cutting it is left to the editor.
- The gaps.json entry for u. 9: as pass 1 said, this is outside the reviewer's files, and it is left for the editor.
