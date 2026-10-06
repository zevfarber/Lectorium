# odyssey-087 — review, pass 1 (17.508–606)

Reviewer worked from conventions.md (rules, the table by search for every word of the part, glossary and
notes sections), packet.md, units.json, new-renderings.md, the model drafts/odyssey-001/units.json, the
published parts in the repository root (searched line by line for every repeated word or phrase), the
last unit of odyssey-086.json, and source/odyssey-murray1919.json. `t` was not touched (checked: all 75
`t` values identical before and after; joined, they reproduce the source apart from the 17.512 stop
discussed below). Build and validator were not run.

Totals: 18 changes (0 high, 8 medium, 10 low); 1 source finding reported (17.512); 14 findings considered
and refused.

## Changes

Line · field · severity · what was wrong · what was done

1. 508 · l, n · medium · `l` rendered προσπτύξομαι "address", `i` "greet", the note "embrace, greet"; the
   shipped parts give "greet" in `l` (odyssey-009 line 22 "shall I greet him", odyssey-037 line 478 "I will greet him").
   · `l` now "so that I may greet him and ask him something"; note's gloss now ‘I may greet’.
2. 511 · n · low · note glossed πολυπλάγκτῳ as "a much-wandering man"; the table keeps "wandering" for
   ἀλάομαι and gives "much-straying" in `l` for πολύπλαγκτος. · note now ‘a much-straying man’.
3. 521 · n · medium · note said ἔθελγε is "as in θέλγοιτο two lines back"; θέλγοιτο stands at 514, seven
   lines back. · now "as in θέλγοιτο at 514".
4. 532 · n · medium · note said αὐτῶν is set against ἡμέτερον "a line later"; ἡμέτερον stands at 534, two
   lines after 532. · now "two lines later".
5. 532 · l · low · μέν left unrendered in `l` (unit 533 renders its μέν as "indeed"). · "For of their own
   indeed the possessions lie untouched in the house,".
6. 546 · l, n · medium · `l` had "By this, then," for τῷ κε καὶ, while the note says τῷ is ‘therefore’ and the
   shipped parts render τῷ (νῦν, μή) "Therefore"; καί was unrendered. · `l` line 1 now "Therefore too would
   death not be unfulfilled for the suitors,"; note adds "and καί is ‘too’". `i` unchanged.
7. 549, 556, 561 · i, n · medium · `i` rendered νημερτέα πάντ’ "everything without error" (three times, and
   the same phrase in two notes); the table lists "speak without error" among the avoided renderings of
   νημερτέα (row νημερτέα εἰπεῖν, 11.96) and keeps "unerring". · `i` now "everything unerringly" in all
   three; the two notes (549, 561) now say ‘everything unerringly’. `l` already had "unerringly". New row
   added to new-renderings.md.
8. 569 · l · medium · "So now Penelope in the halls bid" for τῷ νῦν; shipped `l` for τῷ νῦν is "Therefore now"
   (odyssey-007, odyssey-038); the `i` "So now" is the shipped `i` and stays. · `l` now "Therefore now …".
9. 571 · i · low · "her husband’s homecoming day" departs from the table's νόστιμον ἦμαρ `i` "the day of their
   homecoming". · "about the day of her husband’s homecoming".
10. 576 · l · low · "Not you, at least, are bringing him" reads as if someone else is bringing him; οὐ negates ἄγεις.
    · "You, at least, are not bringing him, Eumaeus;" (order given up for sense; coherence wins ties).
11. 576 · i · low · "What does the vagrant mean by this?" turned the aorist ἐνόησεν into a present, against its own
    `l` ("has … thought") and note ("did he have in mind"). · "What did the vagrant have in mind by this?"
12. 581 · l, n · medium · `l` "men overbearing" for ἀνδρῶν ὑπερηνορεόντων; the table's row for
    ὑπερηνορέοντες (6.5) fixes `l` "men over-bold" (shipped at 6.5, odyssey-027 line 5, for the identical phrase
    ἀνδρῶν ὑπερηνορεόντων) and `i` "overbearing". · `l` now "men over-bold"; note gloss follows; `i` unchanged.
13. 586 · l, i, n · medium · the new row made ἄφρων "without sense" and ruled "senseless" out as "reserved for
    ἀφραδής". But ἄφρων is already shipped as "Senseless" in both layers (8.209, odyssey-035), the first
    ratified rendering wins, and the table itself gives ἀφραδής "senseless" too (two Greek words, one English,
    told apart by context, as ἀλήτης / ἀλήμων). · `l` "Not senseless the stranger;", `i` "The stranger is not
    senseless;", note gloss ‘senseless’; new-renderings.md row rewritten to say so.
14. 586 · i · low · "he judges things as they may well be" for ὀΐεται, ὥς περ ἂν εἴη: "judges" is out of line with
    `l` "supposes" and with the same verb's `i` "think"/"suppose" in the shipped parts; "well" added. · "he
    supposes things to be just as they may be;".
15. 590 · l, i, n · low · διεπέφραδε rendered "explained everything"; the same form is shipped as "made it plain"
    / "made all this plain" (odyssey-027 line 47). · both layers "when he had made everything plain"; note gloss
    ‘make plain, explain fully’.
16. 591 · n · low · note called the line "the same formula as at 543"; 543 has ἄρ’ (αἶψα δ’ ἄρ’), 591 has not. ·
    "(there with ἄρ’ after αἶψα δ’)" added.
17. 593 · l · low · "those other things" for κεῖνα: "other" is not in the Greek. · "those things".
18. 596 · i · low · `i` "for many of the Achaeans mean evil" turns δέ into a "for" (γάρ-force); `l` has "and". · "and
    many of the Achaeans mean evil".

## Source finding: 17.512 (not edited here)

Line 17.512, τὴν δ’ ἀπαμειβόμενος προσέφης, Εὔμαιε συβῶτα, ends without a stop in
source/odyssey-murray1919.json (`…συβῶτα`). This is a **missing-stop case under README rule 5**, not a
genuine absence:

- the identical half-line formula ends in ano teleia U+00B7 in all 12 other places the source has it (the
  source's other occurrence in this very part is 17.579, `…συβῶτα·`; the published parts 066, 067, 069, 070,
  077, 078, 081, 084, 085 all print `·`);
- the line is a speech introduction and the speech begins in 513, so the sentence must close here;
- nothing but a mark is missing (no letter, accent or word), one mark in one place.

Recommended action for the run: add U+00B7 after συβῶτα in book 17, line 512, of the source; update the
`sha256` of every part containing 17.512 (only odyssey-087 — odyssey-086 ends at 507); make the unit-2 `t`
`τὴν δ’ ἀπαμειβόμενος προσέφης, Εὔμαιε συβῶτα·`; record work/line/mark/part in LOG.md. Nothing else in the
unit changes: it already ends at the end of the line, the `l` and `i` already end with a colon, and the note
needs no change. The source and `t` were left as they are.

## Checks that found nothing to change

- Quotation marks: “ on the first unit and ” on the last unit of all eleven speeches (508–511, 513–527,
  529–540, 544–550, 553–559, 561–573, 576–578, 580–584, 586–588, 593–597, 599–601), in both `l` and `i`, none
  elsewhere; `mark` on exactly those first units (and no other unit); `p` on exactly the 15 units Murray's
  ¶ marks give. Last unit of odyssey-086 (507, `ἡ δ’ ἐπὶ οἷ καλέσασα προσηύδα δῖον ὑφορβόν·`) closes no
  speech and says the speech begins in this part, so there is no run-on speech into 087 and no “ is wanted
  there. Nothing runs on into 17.607 (the part ends on narration).
- Reused lines. Verified against the published JSON, line by line: 528 and 585 (odyssey-083), 534–536 (unit
  identical to odyssey-005 at 55), 538–539 (odyssey-005 at 58), 543 (077), 548 (055), 551 (085, adapted:
  she for he, one line only), 552 (014, fourth line), 560 (067), 565 (074, second line), 592→591 (002, second
  line; "to hers" correctly dropped), 598 (004), 604 (080, third line). In addition two whole published units
  that the packet does not list are repeated and are word-for-word identical to their published `l` and `i`:
  17.537 `τὰ δὲ πολλὰ κατάνεται.` (odyssey-005 at 58) and 17.599 `ἔσσεται οὕτως, ἄττα·` (odyssey-077 at 31).
  Only the note differs (see refusals). Gender-adapted copies ("she") are the only changes made to a reused
  wording.
- Scansion: the packet flags no line, so there is nothing to hand-scan and no note gets a metre sentence.
- Remembered English: none found in `i`; the unusual phrasings ("fail of its fulfilment", "rolling on and on",
  "gave me over to pains") are built from the case relations and sit in the table's registers.
- Cross-references checked against the line: 508 (ἄνωχθι, also 569), 512 (= 579), 514 (θέλγοιτο), 522 (Ὀδυσσῆος,
  525 Ὀδυσῆος), 528 (= 585 = 560 formula), 529 (κάλεσσον, 544), 543 (= 591), 551 (= 574), 570 (= 582), 594
  (μελόντων, 601), 599 (δειελιήσας, 606), 602–603; and the spellings Ὀδυσσεύς 538 / Ὀδυσεύς 539.

## Findings considered and refused

1. **αἰδοῖος "shamefaced" against the table's "revered" (578).** Kept. The word is the active sense ("bashful,
   shamefaced") that LSJ gives for this very line, and the shipped "revered" (odyssey-026 line 447, -033 line 22, -068 line 234, the
   table's αἰδοίοισιν row) is the passive sense; the new row says so, keeps "revered" out, and the note
   explains the word (built on αἰδώς, "often ‘revered’, but here …"). A rendering "revered vagrant" would be
   wrong, and no other house word covers the sense. The same line's αἰδεῖται "is shy" is a different
   Greek word and stays.
2. **"father" in lower case (553 ξεῖνε πάτερ, 599 ἄττα).** Justified. 553 is "stranger, father" exactly as the
   table's ξεῖνε πάτερ row (7.28); 599 stands after a comma inside the sentence and the table's 16.31 row for
   ἄττα is lower-case "father" (the capital "Father" of the 17.6 row is only the sentence-initial form, and
   published 077 prints "father;" for this very line).
3. **"fine clothes" absent at 557.** Not a drop. 557 ἕσσει σε χλαῖνάν τε χιτῶνά τε, τῶν σὺ μάλιστα has no
   εἵματα καλά (550 has them and renders them "fine clothes", as the table and the published 077 line do); the
   note at 556 says so. Adding "fine clothes" would put English in that the Greek does not have.
4. **Unit 533 cut at a comma.** Justified: with 533b–537a the sentence would span five lines (533, 534, 535,
   536, 537), over the four-line limit, and the cut gives 534–537a, which is exactly the published odyssey-005
   unit, so its `l`/`i` are reused word for word.
5. **κατάνεται note (537).** The odyssey-005 note gives a parse (present passive of κατάνω); ours says the
   formation is not certain. Kept: ours is the safer claim, the `l` and `i` are the published ones, and
   nothing in either note contradicts the English.
6. **ἀγχοῦ "near" (525) beside "close by" in the 552 note.** Different uses: bare ἀγχοῦ is "near" (odyssey-027
   line 5), ἀγχοῦ ἱστάμενος is the table's "standing close by". Kept.
7. **ἄλλως "otherwise" (577)** against the table's ἄλλως "idly" (14.124). Different sense (ἦε καὶ ἄλλως =
   "or even otherwise", not "in vain"); the table row names the 14.124 context. Kept.
8. **κῆρας "death-fates" / "spirits of death" (546)** against row 1744 ("escaped death"): the table's
   κῆρα μέλαιναν and κῆρα (16.169) rows use "death-fate" in `l` and "spirit of death" in `i`, which is what
   unit 28 has. Kept.
9. **ἐν μεγάροισι "halls" in `l`, "hall"/"halls" in `i`.** Matches the shipped usage ("halls" in `l`, `i`
   varies); no table row. Kept.
10. **τί … τοῦτ’ "accusative of respect" (576 note).** Reading is uncertain (object τί with τοῦτ’ adverbial, or
    the reverse); the note's gloss "what in this?" is what `l` says, and no label in it is false. Kept.
11. **Ἀχαιοί = the suitors (513, 596 notes).** The claim is borne out inside this part (596 "many
    of the Achaeans … think evil", 513 beside 530–540) and is not asserted of the rest of the poem. Kept.
12. **οὐκ ἀτελής rendered "not unfulfilled" / "would not fail of its fulfilment" (546).** Matches its new
    row, the published ἀτέλεστος "unaccomplished" family and the litotes explained in the note. Kept.
13. **ἔσσεται note "is ἔσεται … (Attic ἔσται)" (599) against the published note.** Same fact, worded
    differently; the English is identical to the published unit. Kept.
14. **ἡ μὲν ἄρ’ ὣς ἀγόρευεν row against the table's ἡ μὲν ἄρ’ ὣς εἰποῦσ’ (15.43, "She, indeed, then so having
    spoken").** The new row has δέ answering μέν ("she … and he"), so no "indeed" is wanted; the two rows are
    kept apart on purpose by their verbs. Kept.

---

# odyssey-087 — review, pass 2 (17.508–606)

Second reviewer, working fresh from conventions.md (house table searched by stem for every word of the part,
glossary and notes sections), packet.md, units.json, new-renderings.md, gloss.json, novel-forms.json,
known-forms.json, odyssey-glossary.json (old entries for every `__broaden__` key) and the published parts
odyssey-001 to -086 in the repository root (every line of the part compared mechanically with every published line
by word windows, then read). `t` was not touched (checked by script: all 75 `t` identical before and after; the
17.512 `t`, which ends without the ano teleia, is left as it is). Edits made to units.json and gloss.json in place by
script (diff: 10 changed lines in each file, nothing else). Build and validator were not run.

Totals: 17 changes (0 high, 3 medium, 14 low); 14 findings considered and refused; 1 observation for the run
owner (534 `t`, below).

## Changes

Line · field · severity · what was wrong · what was done

1. 583 · l, n · medium · `l` "And indeed for you yourself thus it is much finer" for καὶ δὲ σοὶ ὧδ’ αὐτῇ πολὺ
   κάλλιον; the same half-line is shipped twice as "And also for you yourself …" (odyssey-027 lines 39 and 60,
   both with the note ‘and also, moreover’). A repeated line gets the same English. · `l` now "And also for you
   yourself thus it is much finer, O queen,"; note now ‘and also, moreover’.
2. ἔρχεό · gloss · medium · "accent thrown back by a following enclitic" is the wrong direction: ἔρχεο (a
   proparoxytone) takes an extra acute on its last syllable before the enclitic μοι; nothing is thrown back. ·
   now "extra acute on the last syllable from the following enclitic".
3. θέλγοιτό · gloss · medium · same false claim ("accent thrown back by the enclitic"); the printed acute on the
   ultima is the one the enclitic κε brings. · now "extra acute on the last syllable from the enclitic κε".
4. 589 · l, n (+ new-renderings.md) · low · `l` "so was speaking" for ἡ μὲν ἄρ’ ὣς ἀγόρευεν; the same hemistich
   (ἀγόρευε) is shipped as "She, then, so spoke" (odyssey-086 line 505), first ratified rendering wins; pass 1's
   new row had fixed the divergent "was speaking". · `l` "She, then, so spoke, and he went off, …"; note gloss
   ‘spoke’ (imperfect named); the new-renderings.md row rewritten to say "was speaking" is withdrawn and why.
   `i` unchanged.
5. 524 · l, i · low · the repeated half-line ἔνθεν δὴ νῦν δεῦρο τόδ’ is shipped (odyssey-086 line 444) as "From
   there indeed now here to this place …" / "From there I have now come to this place"; ours had "now to here, to
   this place" and "come here, to this place". · `l` "From there indeed now here to this place he came, suffering
   woes,"; `i` "From there he has now come to this place, suffering woes, rolling on and on;".
6. 511 · i · low · "a man who has roamed far" for πολυπλάγκτῳ; the table row πολύπλαγκτος (17.425) fixes `i`
   "far-roaming". · "for he looks like a far-roaming man.”"
7. 539 · i · low · "his own fatherland" for πατρίδα γαῖαν, which carries no possessive in the line (the table row
   gives "his own" only where the line has ἥν/ἑήν; ᾧ παιδί two words later is the line's "own"). · "his
   fatherland" (`l` already so).
8. 541 · n · low · note called ἔπταρεν the aorist of πταίρω while the gloss lemma is πτάρνυμαι. · note now "πταίρω
   (also πτάρνυμαι)".
9. 545 · n · low · same for ἐπέπταρε: note ἐπιπταίρω, gloss ἐπιπτάρνυμαι. · note now "ἐπιπταίρω (also
   ἐπιπτάρνυμαι)".
10. ἑψιαάσθων · gloss · low · "(= Attic ἑψιάσθωσαν)"; the contracted equivalent of the form is ἑψιάσθων (-σθων is the
    Attic 3 pl. imperative ending too). · "(= Attic ἑψιάσθων)".
11. ἐπέπταρε · gloss · low · "unmarked ending -ε" says nothing (the point is the absent movable ν beside ἔπταρεν). ·
    "without the movable ν (cf. ἔπταρεν)".
12. δειελιήσας · gloss · low · "sup … ’having supped’" fixed a sense the note and new row call uncertain, and "having
    supped" is the avoided rendering. · "take the evening meal (sense inferred from δείελος ’evening’; ’spend the
    evening’ also given) … ’having taken the evening meal’".
13. πολυπλάγκτῳ · gloss · low · "masc. dat. sg." though the form is masc./neut. · "masc./neut. dat. sg.".
14. ἀκήρατα · gloss · low · "neut. nom. pl." though the form is also acc. pl. (the glossary writes nom./acc. for
    such forms, e.g. ἄλλο, καλά). · "neut. nom./acc. pl.".
15. ἀτελὴς · gloss · low · "masc. nom. sg." though the form is masc./fem. · "masc./fem. nom. sg.".
16. ἐΰφρων · gloss · low · same. · "masc./fem. nom. sg.".
17. αἰδοῖος · __broaden__ · low · the new reading's example translated αἰδοῖος ἀλήτης "a bashful vagrant", while the
    house rendering (new row, `l` and `i`) is "shamefaced". · example now ’a shamefaced vagrant’. Old entry kept
    whole.

## Checked and found correct

- Every note's grammatical labels and positional claims against the line (cases, numbers, tenses, moods,
  "next line", "two lines later", "next unit", "line 529 / 508 / 514 / 522 / 543 / 551 / 570 / 594 / 599 / 602–603"
  cross-references): no error beyond items 8–9. Possessive ᾧ (539) and the relatives ἣν (517), τῶν (557, 565), τοὺς
  (596), ὅς (559) are labelled correctly and the article-forms are called pronouns or "article-like" in the
  notes.
- Quotation marks, by script: “ on the first unit and ” on the last unit of all eleven speeches in both `l` and
  `i`, no others; `mark` exactly on those eleven first units, all with the right speaks/answers; `p` on the 15 ¶
  units; no ASCII quote, backtick or double quote anywhere in `l`, `i`, `n`; `l` line count equals `t` line
  count in every unit; no `\n` in any `i`.
- Whole-unit reuse, by script against all published parts: 528, 537 (`τὰ δὲ πολλὰ κατάνεται.`), 548, 560, 585,
  598 and 599 (`ἔσσεται οὕτως, ἄττα·`) have `l` and `i` identical to every published occurrence (17.537 and
  17.599 included). Line-level reuse (534–537, 542, 551/574, 552, 564, 591, 602–604) matches the published
  English line for line, apart from the gender or tense adaptations (she for he) pass 1 recorded and items 1, 4, 5.
- gloss.json: all 66 forms are in novel-forms.json and none is already in odyssey-glossary.json; all entries
  are under 230 characters, ’ only, no digits as line numbers, no "here"; the one homograph (ἄπειμι) has both
  readings joined by " · ". Each `__broaden__` value begins with the old entry whole (checked against
  odyssey-glossary.json, character for character) followed by " · "; the new reading is true of the line it
  cites in every one of the eleven (αἰδοῖος, αὐτῶν, γενέσθαι, κ, κε, κήδεά, κεῖνα, κρήτῃ, νημερτέα, πλεῖον,
  ὑπερηνορεόντων). The old κρήτῃ entry has U+2018 ‘ in it; it is the existing entry and must stay whole.
- Known forms whose existing entry I checked against their use here and found already covering it: τῶν and τοὺς
  as relatives, τοι (dative and particle), ὅ (= ὅτι), ὁ/οἱ/ἡ, ᾧ and ὅνδε (possessive), ἑ, κέ/κε/κ’ in all their uses
  except those broadened, ἦ, τί/τι, ἠέ/ἢ, αὐτῇ (with σοί), ἔπ’, πόσιος.

## Findings considered and refused

1. **κῆρας "death-fates" / "spirits of death" (546) against the shipped "death and the fates" (odyssey-008 line
   349, odyssey-025 line 385).** Kept. The later table rows κῆρα μέλαιναν, θάνατον καὶ κῆρα (16.169) and ἔκφυγε
   κῆρα fix "death-fate" in `l` and "spirit of death" in `i` for κήρ; the shipped parts predate them. Conflict
   between the two is for the run owner, not for this part.
2. **γνώῃ gloss ’she may recognise’ pins the sex of the subject.** Kept: the quoted English in an entry is an
   illustration of the parse (cf. εἰρέσθω ’let her ask’), not a line reference; it names no line.
3. **χαλεπῶν "masc. gen. pl."** Kept: it is the agreement actually seen with μνηστήρων; the glossary
   gives the gender of the noun an adjective agrees with (cf. ἀθανάτοισι "masc. dat. pl."), and only items 13–16 (ambiguity of case or
   gender within the form) were treated as errors.
4. **κέ has no "+ subj. in the protasis after εἰ" reading (556, εἰ δέ κέ σε γνώῃ).** Kept: the entry has "after εἴ"
   and "after αἴ" for the same construction; the unaccented εἰ changes nothing about κέ.
5. **τὰ δὲ πολλά (537) has no "article-like with an adjective" reading in τὰ.** Kept: covered by "’these things’";
   the unit is a published one whose glossing already stands.
6. **μοι (545 ὅ μοι υἱὸς) has no possessive reading.** Kept: "dat. of the person affected, ’from my …’" is the same
   construction.
7. **ἀνεδέγμεθ "aor. 1 pl."** Kept: the glossary writes "aor. 1 sg." for first person throughout (ἱκέτευσα,
   ἔρυξα); the entry itself says athematic.
8. **ἐξολέσειε "(-σειε = -σαι)".** Kept: the ending -σειε is Attic too, but the entry only says the two endings are
   one optative; no false claim.
9. **ἐρέωμαι without a tense.** Kept: pres./aor. is not decided for the epic subjunctive of ἔρομαι (εἴρομαι) and
   the known entry for the same verb says nothing either.
10. **ἔρυξα not marked "unaugmented".** Kept: for ἐρύκω the augment cannot be told from the stem (ἔρυξα may be
    ἔ-ρυξα or unaugmented), and the unit note does not claim either.
11. **νημερτέα broaden: "neut. acc. pl. as adv./predicative" against the old "used as a noun".** Kept: with πάντ’
    as object of ἐνέποντα the word is not a noun; pass 1's reading stands and the old entry is whole inside.
12. **Notes call τὰ in 537 "the article with a neuter plural".** Kept: it describes the article-like use of the
    pronoun-form with πολλά, which is how the glossary words it.
13. **αὐτῶν broaden "their own with no possessive expressed" overlapping the old "our own … no other possessive".**
    Kept: different person and a different line; the old entry is whole and the new reading is its own.
14. **μηχανόωνται "devise" (587) against the shipped "contrive" (odyssey-010, -011, -021).** Kept: the
    table's μηχανάομαι "devise" (rows 14.340, 16.169) and the recent shipped parts (077, 078, 086) all say "devise".

## Observation for the run owner (not an edit)

- 17.534: the packet prints the published unit's `t` with ὄις (odyssey-005 line 55) while the archive text of this
  part prints ὄϊς (with the diaeresis, 17.535). Because of that one character the unit is not a whole-unit
  repeat for the validator's identity check; its `l` and `i` are nevertheless word for word the published ones,
  as checked. `t` was not touched.
