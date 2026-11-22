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
