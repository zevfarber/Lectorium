# Review — bardo-thodol-012 (pp. 107–115)

**units.json is now the master.** It was edited in place by script; `scratch/build_units.py` is stale and must not be
re-run (it would overwrite these edits).

## Pass 1

Checked against conventions.md, ../run3/RUNBOOK.md §2, runbook.md, packet.md (the pinned print, its 11 `# fix:` lines and
the establishment log), the pilot (units.py, ../../../bardo-thodol-001.json), the units and reviews of the earlier parts
(011 above all, 010 for the formulas, 006 for the gatekeeper goddesses and chos kyi rgyal po, 008 for bzung cig, 006/007 for
bos), glossary.json, and the other recension (readings/witness_ga.txt = source/raw). No modern translation was opened.

All 49 units and the about were read word by word: original → `l` → `i`. The grammatical labels in the notes were checked
against the forms and stems: shar / 'char, song / 'gro, byung / 'byung, byas / byed, shi / 'chi, mnan / gnon, bcings / 'ching,
rgyob (imperative of rgyag, past brgyab), sod (imperative of gsod), bsad / gsod, btubs / gtub, bsnams / snom, bos / 'bod,
bzung / 'dzin, mdzod (respectful command); the endings -r / -ru / -du / -su, -s (ya sos, thugs rjes), -'i, la, nas, the
sentence-ending -o (repeating the last letter: 'jigs so, skrag go, brgyal lo), ma … na, mi vs ma, and the command particles
cig / zhig / shig after their finals (rgyug cig, thob cig, byed cig, skrag cig; bzung zhig; bos cig "where shig is usual").
All are right except bos (u. 48, named only as the past stem in a command) — fixed below.

The 11 `[?]` marks of the log are each called doubtful in their units: 0 (pha), 12 (ri), 20 (bred), 29 (sang), 35 (mkha',
yong), 37 ('thung), 38 (par), 40 (gzugs), 41 (dngos), 48 (thon). The two misprints (u. 18 cha la las, u. 41 dngos pa can)
open their notes with the rule-5b sentence. The contraction 'grog (u. 20) is named. Of the eight missing tshegs only two
(u. 6, u. 9) were named; 011 named every one, and the other six are now named (below). Every "Kept, note only" item is in its
note: pha wad "perhaps for pha wang 'bat'" and dga' ba / rdo rje (u. 0), Vajra Sow (u. 13), chos sku for longs sku, with the
text and both translations as printed (u. 18), snon mar marked uncertain with the other recension's gyis non par (u. 20), no
lus (u. 23), the missing negative at 113.3 (u. 34: `l` as printed, `i` "[do not]", the note explicit and naming the ×7
image check), u. 45 na ni, the two snake heads (u. 8), zhed mi dgos and ra mda' la rgyug cig (u. 40, 48), kyai and dngangs
(u. 0, 21). The 112.3 gap unit (u. 26) has a `gap` field in 010's format and "[ … ]" in `l` and `i`; its note describes the
traces as the log does. The sense differences listed in the log are all in the notes; every other-recension claim was checked
against the witness, and all hold.

Cross-references checked and right: chu srin, srin mo, zhing, sgo ma, dbang phyug ma, he ru ka drag po'i lha, mda' gzhu
'gengs, mgo lus phral, don la, rang rtsal, mgo brnyan, gnyis su med par thim nas … 'gyur ro (011); khyung, gshin rjer (010);
rang snang du (003); the four implements of the gatekeeper goddesses (006 u. 38); ming nas bos and gsol ba thob cig "as a
guess" (003–006); 011's withdrawn spra'i[?] (u. 2). House renderings checked: bar do "the between" / "bardo", 'od gsal "clear
light", chos sku "body of truth", chos nyid "reality", rig pa "knowing" / "awareness", khrag 'thung "blood-drinker", rigs kyi
bu "child of noble family", ngo shes "face-knowing" / "recognise", chos kyi rgyal po "King of the Teaching" (as 006 u. 39).

Division was checked by script against the `w` of 002–011 and the glossary keys: each run of 2–3 adjacent 012 words joined
and looked up, each 012 word split and looked up among earlier adjacent pairs. No join is a single earlier word; the one split
hit (འཇིགས་སྐྲག, which 003 also has as one word, glossary key) is right as one word. No `w` was changed.

units.json was edited in place by script (ensure_ascii=False, indent 1, no final newline; the round trip was checked to be
identical first). Letter check (all `w` joined, spaces removed, against `hooks.letters()`): 49 units, 4618 letters, EQUAL.

### Changes

- u. 48 · n · minor · stem. "bos, the past stem of 'bod, 'to call', here in a command": bos is the past and the imperative
  stem; 006 and 007 say so · now "bos, the past and imperative stem of 'bod, 'to call' ('bod / bos / bod / bos), as in 006".
- u. 48 · n · style · stem. bzung named as past stem in a command without the imperative; 008 u. 23 gives it · now "…, where
  the imperative is zung; …; the other recension has zungs shig, as in 008".
- u. 34 · n · minor · the note said "the idiomatic line adds [not] in brackets"; `i` has "[do not]" · now "[do not]".
- u. 27 · i / n · minor · "the clear light's own natural radiance" read 'od gsal as the owner of rang mdangs, but it has no
  -'i, and rang gi is everywhere in this passage "your own" (rang gi rig pa'i rang mdangs, u. 19, 25, 41) · `i` now "Recognise
  them as the clear light, your own natural radiance."; the note says why. `l` ("Clear-light own's own-radiance-as") kept.
- u. 19 · i · minor · force. "know that whatever dawns is …; and at that very moment you become a buddha" made shes nas, a
  clause chain ("having known …, at once …"), into a command · now "…, knowing that whatever dawns is the natural radiance of
  your own awareness, dawned of itself, you become a buddha at that very moment, …".
- u. 19, 23, 29, 32, 33, 34 · n · minor · six of the eight missing-tsheg fixes (111.1/2 'thung|gi, 111.4/5 kyai|rigs, 112.4/5
  yid|la, 113.1/2 kyai|rigs, 113.2/3 shes|na, 113.3/4 po'i|sku) were not named, where u. 6 and 9 and all of 011 name theirs ·
  added "The print runs X and Y together across the line join, here divided." (u. 29: "At the line join the print sets the
  tsheg after yid at the start of the next line; here it is written after yid.", as the log describes it).
- u. 41 · n · style · the rule-5b opening ended with a colon ("corrected here: the o-sign …"); 011 pass 1 fixed the same ·
  now "corrected here. The o-sign …".

Severity count: major 0 · minor 5 · style 2 (7 change lines; the six tsheg notes counted as one).

### Refused

- u. 0–14 `i`: the Īśvarīs' names are translated (Delight, Peaceful One, Nectar, Moon, Club, Eater …) where 011 u. 41–43 gave
  Sanskrit names (Brahmāṇī, Mahādevī, Kaumārī, Indrāṇī). Kept: those were the consorts of named gods, whose Sanskrit is in
  their Tibetan names; here the names are ordinary words, the note of u. 0 says they are translated, and 011 u. 42 also gave
  gtogs 'dod in Tibetan. srin mo "Rākṣasī" and phag mo "Vārāhī" follow 011 and the established Sanskrit.
- u. 3 / u. 15 `i` "yoginīs" where the print has rnal 'byor without -ma and `l` has "yogins": kept; the note explains, and the
  goddesses are female.
- u. 23 `i` "eighteen of you stacked": the print lacks lus; kept, the note says the sense holds, as the log asks.
- u. 30 `i` "if you do not recognise them now and are frightened" for nas … nas: kept; the note says the sense and the other
  recension (skrag na) want a condition and the idiomatic line reads it so.
- u. 37 `i` "he comes" for de lta bu'i … yong ngo (who comes is not stated): kept; the sentence continues the description of
  Yama's body (u. 35–36).
- u. 45 `i` "this is your yidam deity": "they are" was considered; kept, the subject is unexpressed and the sentence also
  points forward to the call on the yidam.
- u. 42 note: the log calls the other recension's order "agent and object reversed"; the note says the sense is the same. Kept:
  in both, emptiness is agent (kyis) and emptiness object (la); only the order differs.
- about: long (1776 characters, 011 has 1601) but accurate to this part and plain; kept. It keeps "the body of truth" for both
  aspects, as printed.
- No English in `i` was found that reads as remembered rather than built from the words; none was rebuilt.
- Not for this reviewer: gaps.json and QUESTIONS.md entries for the 112.3 gap (the log asks for them); left for the builder.

## Pass 2

Second pass. Each of the 114 entries in gloss.json and the 10 under __broaden__ was checked against the word and its use in
units.json (w / l / i / n), against the verb stems and against the master entries of related forms (ཕྲལ, དབྱུག་ཏོ, བརྩེགས་པ in
རབ་བརྩེགས་པའི, ཁྲག་འཐུང, ཞིང, བོས, རང་རྩལ). Stems checked and right: mnan / gnon, bcings / 'ching, bsad / gsod, btubs / gtub,
rgyob (imperative of rgyag), sod (imperative of gsod), bos / 'bod, bzung / 'dzin, shar / 'char, byung / 'byung. Coverage by
script: novel-forms.json has 114 keys, every one in gloss.json, none empty, no extra keys; every word of units.json (punctuation
stripped) is in glossary.json or novel-forms.json. Each remaining __broaden__ value begins with the master entry verbatim
+ " · " (checked by script). The 211 known forms were read against their uses here; none was found whose master entry fails
this part's use (ན 'in', གི for gis, ཀྱི, ཤར 'east', ཐོན, ཁ, ཡོད་པ, དེ closing a phrase, བྱ་བ without zhes are all covered).

Then all 49 units and the about were read again, original → `l` → `i`, with pass 1's changes, and every note was set against
the gloss of the same word; no disagreement remains. No `w` was changed. Letter check (all `w` joined, spaces removed, against
hooks.letters() for the part): 49 units, 4618 letters, EQUAL. gloss.json and units.json were edited by script
(ensure_ascii=False, indent 1, no final newline; round trip byte-identical checked first).

### Changes: gloss.json

- gloss འཐུང་བ · stem · minor · "past 'thungs": the past of 'thung is btungs ('thung / btungs / btung / 'thungs; 'thungs is the
  imperative) · now "past btungs".
- gloss རྒྱའོ · sense · minor · "to expand, to become": rgya does not mean 'become' · now "expand, open out (rgya, the second
  syllable of the verb sangs rgya 'to awaken', + -'o): sangs mi rgya'o 'will not awaken'".
- gloss ཕྲལ་བ · stem · minor · "phral, the verb 'to tear off'" named the past as the verb · now "phral, past stem of 'phral 'to
  separate, tear apart'", as master ཕྲལ.
- gloss བྲེད་པས · wording · minor · "because (they) are scared" (the one who dreads is "you") and "bred is doubtful on the image"
  pinned to the line · now "because of dreading, because (one) is scared (bred 'to be scared, to dread' + -pas 'because')";
  the doubt stays in the note (u. 20).
- gloss རི · wording · minor · the entry led with the line's doubt ("as printed after sgo ma, doubtful on the image …") and put
  the meaning second · now "mountain, hill (ri); where it gives no sense, perhaps a syllable set twice by mistake (uncertain)";
  the image doubt stays in the note (u. 12).
- gloss __broaden__ ལྷའི · dropped · minor · "where the other quarters have their own name … perhaps in error for lho'i" is a
  doubt about one line, not a new sense; the master "of the gods" covers the reading in `l` / `i` ("Gods'(?)", "divine(?)"),
  and the note (u. 3) carries the doubt.
- gloss __broaden__ ཐོན · dropped · minor · master "come out, emerge" already covers gang thon "whatever comes out"; the rest was
  the line's image doubt, which the note (u. 48) has.
- gloss __broaden__ གང · dropped · style · "gang shar 'whatever dawned'" adds nothing to the master "what, whatever".
- gloss __broaden__ ཆེ་བ · dropped · style · "the large ones: che ba ni" is the master "great, big" used as a noun; not a new sense.
- gloss __broaden__ དགའ་བ, ཞི་བ · wording · style · "(the first goddess of the south; also the second of the west)", "(a goddess
  of the south)" pinned the name to this passage · removed.
- gloss ཡོང་ངོ, རང་གཟུགས, སང་རེས · wording · style · "yong / gzugs / sang is doubtful on the image" pinned a line's doubt to the
  form (yong ngo is clear at 114.2) · removed; the notes (u. 35, 40, 29) keep it. ཡོང་ངོ also "will come" → "comes, will come".
- gloss སངས · wording · style · "the negative mi stands between it and rgya" read as of one line · now "in the negative, mi
  stands between it and rgya (sangs mi rgya)".
- gloss འགྲོ་གོ · wording · style · "the print writes it as one syllable" · now "also written as one syllable, 'grog".
- gloss དབྱུག་ཐོ · wording · style · "the print's spelling of dbyug to" · now "a spelling of dbyug to", and "staff, stick" as master.
- gloss གཅོད་པ · stem · style · "gcod, the present stem of gcod 'to cut'" (circular) · now "the present stem of 'to cut' (past bcad)".
- gloss བརྩེགས་པ · stem · style · "brtsegs 'to pile up'" unnamed stem · now "brtsegs 'piled up', past of rtseg", as master.
- gloss གསལ་ཤིང, མཆེ་ཞགས · wording · style · "as printed, uncertain" suggested a misprint where only the sense is unsure · now
  "uncertain: …".

### Changes: units.json

- unit 25 · i · style · force. "When you recognise …" for ngo shes pas, the causal -pas ("because (you) recognise", as the note
  says) · now "By recognising all these appearances …".

Severity count: major 0 · minor 7 · style 12 (19 change lines; grouped entries counted as one line each).

### Refused

- gloss ཕ་ཝད, སྣོན་མར: kept with "as printed" and the doubt: the word exists only as this doubtful reading, and the doubt is its
  only sense (as 011 pass 2 kept ཁྱེ).
- gloss __broaden__ ཡང "de yang … opening a description": kept; "that is" at the head of a description is not in the master.
- gloss __broaden__ ཆ, ཟ་བ, རྡོ་རྗེ: kept; aspect / goddess names are new senses.
- gloss ཞིང་ཆུང "small corpse" without a query: kept; the master ཞིང already carries the reservation, and the note points to 011.
- unit 3 note "one would expect lho'i": kept in the note (that is where the doubt belongs) after the broadening was dropped.
- No English in `i` was found that reads as remembered rather than built from the words.
- Not for this reviewer: the master glossary entry ཁྲག་འཐུང gives "past 'thungs" for 'thung; the past is btungs. glossary.json
  was not edited (out of scope); the builder should correct it when merging.
