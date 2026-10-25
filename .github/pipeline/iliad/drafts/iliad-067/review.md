# iliad-067 (Iliad 11.328–433) — review, pass 1 (units.json only)

Scope: `units.json` read against `packet.md`, `new-renderings.md`, `conventions.md` (the whole Iliad file; its house-renderings table was read through in full, and the rows for every word of this part were read again against the units), the published parts (Iliad and Odyssey, by Greek-string search) and the source text. The last unit of iliad-066 (11.326–327, ending with a plain statement about the Achaeans) opens no speech, so no quotation mark runs over into this part. `gloss.json` was not touched or read. `t` was not touched: the script asserts that every `t` is byte-identical before and after, and the concatenated `t` equals the packet's 106 lines. The file is written back in the same format (indent 1, no trailing newline). Nothing was built, validated or committed.

Order followed: labels and positional claims in the notes, then cross-references, then notes against `l`/`i`, then Greek to `l`, `l` to `i`, remembered English, quotation marks. Scansion flags: none, so no line was scanned by hand and no sentence was added to any note.

Quotation marks checked: seven speeches, each with “ and `mark` on its first unit and ” on its last. 347–348 (units at 347, 348), 362–367 (362 to 367), 380–383 (380 to 382), 385–395 (385 to 394), 404–410 (404 to 409), 430–433 (430 to 433). All correct; none is missing, none is doubled. The six `mark` texts agree with the speakers. The `p` flags fall on the eight lines the packet marks with ¶ (328, 336, 349, 368, 384, 396, 401, 411).

Severity: high = a statement of fact that is wrong; moderate = a house-table or published-wording conflict, a wrong grammatical label, or a wrong force; minor = precision, cross-reference, omission, wording.

## Changes made (line · field · severity · what was wrong · what was done)

1. 354 (unit "Ἕκτωρ δ’ ὦκ’ ἀπέλεθρον…") · `l` · moderate · "ran back a measureless way": the Iliad table gives ἀπέλεθρον as "immeasurable" (ἶνα ἀπέλεθρον, 5.245, 7.269) and expressly turns "measureless" down. · Changed to "ran back an immeasurable way"; the note's gloss "a measureless (distance)" changed to "an immeasurable (distance)". `i` ("a very great distance") left.
2. 354 · `l` · moderate · "leaned with a stout hand": the published unit for the same words (iliad-029, 5.309) has "propped himself with stout hand", and this unit's own note says "propped himself with a stout hand", so `l` and the note disagreed. · `l` now "and propped himself with a stout hand".
3. 360 (unit "καὶ ἀλεύατο κῆρα μέλαιναν") · `n` · high · "3.360, where Menelaus ‘avoided the black death-fate’": at 3.360 it is Alexander (Paris) who leans aside and avoids the black death-fate (the published iliad-019 unit shows "he leaned away" for ὃ δ’ ἐκλίνθη, and Menelaus is the thrower). · "Menelaus" changed to "Alexander".
4. 344 (unit "ἅμα δὲ Τρώων εἵποντο φάλαγγες") · `n` · moderate · "εἵποντο is the epic spelling of ἕποντο": the form is the ordinary augmented imperfect of ἕπομαι (εἱπόμην), not a spelling of an unaugmented ἕποντο; the published unit for this half-line (iliad-032, 5.591) says "the imperfect of ἕπομαι". · Now "εἵποντο is the imperfect of ἕπομαι ‘follow’".
5. 368 (unit "ἦ, καὶ Παιονίδην…") · `i` and `n` · moderate · Agastrophus's death is already told at 342 ("until he lost his dear life"), so ἐξενάριζεν here is the stripping of a man already dead. The table (6.417) gives "strip of his armour" when the killing has been told, and keeps "killed and stripped" for where it has not (335, 422). `i` said "was killing and stripping", and the note said "kill and strip … the act under way". · `i` now "So he said, and was stripping the son of Paion, famous with the spear, of his armour."; the note now says that Agastrophus has already lost his life (342) and only the stripping is left. `l` ("he was despoiling") unchanged.
6. 368 · `n` · minor · "Agastrophus, wounded in the hip at 338–339": the wound is in 338 only (339 begins "but not for him were the horses"). · "338–339" changed to "338".
7. 389 (unit "οὐκ ἀλέγω…") · `i` · moderate · βάλοι is an aorist optative in a general comparison, rendered "were to hit" in `l`; `i` had "than if a woman had hit me", which is a past (pluperfect) force the Greek does not have, and the wording is also the usual one for this line in older English. · `i` now "than if a woman were to hit me, or a senseless child;".
8. 375 (unit "ὃ δὲ τόξου πῆχυν ἄνελκε") · `l` · minor · μιν is not translated in the literal layer, although the note reads the line as "nor did the shaft, then, escape him from his hand in vain". · `l` now "and then the shaft did not escape him from his hand in vain,". `i` unchanged (it follows the table's 5.18 row, "did not leave his hand in vain").
9. 365 (unit "ἦ θήν σ’ ἐξανύω…") · `l` and `i` · minor · πού (named in the note as "somewhere, perhaps") is dropped from both layers; the published `l` for εἴ που is always "if somewhere / anywhere", and the Odyssey's `i` has "if you perhaps saw it". · Both now read "if perhaps some one of the gods is a helper to me too."
10. 397 (unit "ὃ δ’ ὄπισθε καθεζόμενος…") · `i` · minor · ἕλκε is an imperfect ("was drawing", as the note and `l` say) but `i` had the simple past "drew". · `i` now "was drawing the swift shaft out of his foot".
11. 380 (unit "βέβληαι οὐδ’ ἅλιον…") · `i` · minor · "my shaft did not fly in vain" is the stock English for this clause in older versions, and "fly" is not in ἔκφυγεν; rebuilt from ἐκ- + φεύγω and matched to the "leave his hand in vain" of 376. · `i` now "my shaft did not go forth in vain".
12. 333 (unit "τοὺς μὲν Τυδεΐδης…") · `n` · minor · "as in the Odyssey’s same words (21.153)": the Odyssey has the same pair of genitives but a different verb form (κεκαδήσει, future). · Now "as in the Odyssey’s θυμοῦ καὶ ψυχῆς κεκαδήσει (21.153)".
13. 336 (unit "ἔνθά σφιν κατὰ ἶσα…") · `n` · minor · "ἐξ Ἴδης καθορῶν … as at 11.183": 11.183 has Zeus sitting down on Ida, not these words. · Now "(Zeus took his seat on the peaks of Ida at 11.183)".
14. 373 (unit "ἤτοι ὃ μὲν θώρηκα…") · `n` · minor · "against ὃ δέ in the next line": the ὃ δέ is in 375, two lines on. · Now "in 375".
15. 403 (unit "ὀχθήσας δ’ ἄρα εἶπε…") · `n` · minor · "The same line stands at Odyssey 5.298, 5.355 and 5.464": it also stands at 5.407 (odyssey-026, unit at 406). · 5.407 added.
16. 407 (unit "ἀλλὰ τί ἤ μοι…") · `n` · minor · the note glosses τί ἤ as "but why, then?" while `l` has "indeed". · Now "but why, indeed?".
17. 426 (unit "τοὺς μὲν ἔασ’…") · `n` · minor · "αὐτοκασίγνητον … as at 2.704": the word stands at 2.706 (2.704 is the line with Podarces). · "2.704" changed to "2.706".
18. 357 (unit "ὄφρα δὲ Τυδεΐδης…") · `n` · minor · "I take καταείσατο …" is the only first-person statement in the published notes' manner; the other notes are impersonal. · Now "καταείσατο is taken as …".
19. 393 (unit "τοῦ δὲ γυναικὸς…") · `n` · minor · "ἀμφίδρυφοι … is the adjective of 2.700": 2.700 has the form ἀμφιδρυφής; 11.393 has a different form of the same adjective. · Now "is a form of the adjective ἀμφιδρυφής of 2.700".
20. 419 (unit "ὥς ῥα τότ’ ἀμφ’ Ὀδυσῆα…") · `n` · minor · "with the epic doubled σ, as in the simile’s σεύωνται" suggests the simile's form has the doubled σ too. · Now "with the epic doubled σ; it is the verb of the simile’s σεύωνται".

Count: 1 high, 5 moderate (items 1, 2, 4, 5, 7), 14 minor; 20 entries (item 6 is a second correction in the same unit as item 5).

## Findings considered and refused

- 402 `l`/`i` "terror" for φόβος ἔλλαβε πάντας. The table's lower-case φόβος in battle is "flight" (5.252 and 5.272 at iliad-029, 6.96 and 6.277 at iliad-036 and -038, 8.139 and 8.105 at iliad-047, and the unit at iliad-064 ln 70), and `new-renderings.md` lists "flight" among the avoided words without citing those rows. Refused: "flight seized all" is not English, the published iliad-014 gives "terror" to φόβος where it seizes or is carried, and the note says what the word means. Recorded here so that the human reading `new-renderings.md` can add the reference to the 5.252 row (the entry there says only "the table’s Φόβος ‘Terror’ in lower case").
- 347 `i` "rolling down on the two of us": "down" is not in κυλίνδεται, but the Odyssey's published `i` for the same verb with the same subject-type (odyssey-006, "a great disaster is rolling down upon them") has it; kept for agreement.
- 337 `i` "went on killing and stripping one another" against the table's "strip": no death has been told for these fighters, and ἀλλήλους makes both acts part of the verb; the note says so. Kept.
- 387 `i` "your many arrows" for ταρφέες ἰοί ("thick" in `l`): English "thick arrows" would mislead; "many" is the force of "close-set". Kept.
- 410 `i` "must stand his ground strongly" and 348 "by holding our ground": English idiom for ἑστάμεναι and μένοντες, built from the grammar; the table keeps "stand fast" for μένω and "firmly" for ἔμπεδον, and neither is used. Kept; I cannot rule out that older translations use "stand his ground", but the phrase is not a fixed rendering of anything.
- 364 `i` "to whom you must pray when you go into the crash of javelins": the form is forced by μέλλω ("sure to", table 1.564 "must") and ἰών; "crash" is the house word for δοῦπος. Kept.
- 425 `i` "clutched the earth" for ἕλε γαῖαν: the note says the picture is of a dying man clutching the ground. Kept.
- 398 `i` "through his body" for διὰ χροός ("skin" in `l`): the note says χρώς is "body" in the English. Kept.
- 395 `i` "gather round him" for περὶ … πλέες: a verb of motion is added to carry the comparison; the sense is the same. Kept.
- 352 `i` "glanced off the bronze" for πλάγχθη: a plain English verb for a point driven off course. Kept.
- 391 `i` "lifeless" for ἀκήριον: the note says the sense is inferred from the formation, as the table does for 5.812. Kept.
- 343 `i` "along the ranks" against `l` "through the ranks": identical to the published iliad-032 pair for κατὰ στίχας. Kept.
- 376 / 380 `l`: "did not escape … in vain" is the same clause in both places. Kept (only the `i` of 380 changed, see 11).
- 404 Greek without a comma after ἐγώ against the Odyssey's printing: `l` and `i` are identical to odyssey-026. Kept.
- Cross-references checked and found right: 2.835 (Percote), 2.831–834 (word for word, including 11.331b–332), 2.700, 3.135, 3.149, 3.329, 4.138, 4.139, 4.282, 5.18, 5.106, 5.182, 5.284, 5.309–310, 5.590, 5.680, 5.808, 5.873, 6.432, 6.469, 8.91, 10.369, 10.507, 1.72, 1.193, 1.26, 1.409, 1.410, 2.270, 2.645, 3.360, 5.72, 6.208, 9.673, 11.166, 11.273–274, 11.186–194; Odyssey 1.161, 5.465, 8.380, 19.445, 21.153, 22.163.

## Notes for the caller

- `new-renderings.md` (not edited) has no row for ἀπέλεθρον; the change at 354 follows the table's existing "immeasurable".
- The glosser's file was not read; the second pass will need to check the parse of ἐνάριζον, καταείσατο, κεκαδών, ἐπαυρίσκω and the two ἀμφίδρυφος/ἀμφιδρυφής forms against the notes as they now stand.

# Pass 2 (gloss)

Scope: `gloss.json` read against `units.json` (the line each form stands in, and the notes as they now stand after pass 1), `novel-forms.json`, `known-forms.json`, the root `iliad-glossary.json` and `odyssey-glossary.json`, `new-renderings.md`. `units.json` and `t` were not touched. Mechanical checks, by script: all 125 novel forms have an entry and no entry lacks a novel form; no entry reaches 230 characters; no ASCII apostrophe, backtick, line number or "here" in any entry; all 26 `__broaden__` keys (before items 1 and 2 removed two) exist in `iliad-glossary.json` and each new entry begins with the old entry whole followed by " · " (so `build_iliad.py`'s keep-whole check passes). Every novel parse (case, number, tense, mood, person, voice, lemma, meaning) was then read against its line; every known form in the part was read against its existing entry for coverage. Nothing was built, validated or committed. `gloss.json` is written back in the same format (indent 1, no trailing newline).

## Changes made (form · severity · what was wrong · fix)

1. `__broaden__` εὔχεσθαι · high · the added reading "’boast, claim’ (ᾧ μέλλεις εὔχεσθαι ’in which you are sure to boast’)" is wrong: ᾧ is the relative dative of Apollo, and the unit (`l`, `i`, note) has "to whom you are sure to pray". The old entry ("pray, vow") already covers the use, so no broadening is warranted. · Entry removed.
2. `__broaden__` θυμοῦ · moderate · the added reading "the life that leaves the body: ’of life’ … ’having robbed of life and breath’" contradicts the part (`l` "of heart and of life", `i` "heart and life", the new-renderings row keeping θυμός "heart" and ψυχή "life" after the Odyssey) and the old entry ("heart, spirit, soul") already covers it. · Entry removed.
3. `__broaden__` ἀπέλεθρον · moderate · the added reading gave "’a measureless distance’ … ’ran back a great way’"; the Iliad table turns "measureless" down (5.245, 7.269) and pass 1 changed `l` and the note at 354 to "immeasurable". · Now "’an immeasurable distance’ (ἀπέλεθρον ἀνέδραμε ’ran back an immeasurable way’)".
4. `__broaden__` ἐφόβησε · moderate · the added reading gave "’scared’", which the table avoids for φοβέω (new-renderings: "scared" refused; φοβέω "put to flight"). · Now "plain narrative: ’put to flight’ (Δαναοὺς ἐφόβησε ’put the Danaans to flight’)".
5. `__broaden__` φόβος · minor · the sense list had "panic", which the table reserves for φύζα. · "flight, fear, panic" now "flight, fear".
6. `__broaden__` ἀκήριον · minor · the added reading glossed only "’lifeless’", where `l` and the note have "spiritless" ("lifeless" being the effect). · Now "’spiritless’ (ἀκήριον … τίθησι ’makes spiritless, lifeless’)".
7. ἐπαύρῃ · moderate · the parse was left open ("aor. subj. 2/3 sg. (mid. ἐπαύρηται)"); the line has the shaft as subject, so the form is 3 sg. act. (and the Odyssey's entry for the same spelling is a different parse, 2 sg. mid., so a hedged entry would be misread). · "aor. subj. 3 sg. act., after εἴ κε: ’if it touches’".
8. βάλοι · moderate · "’would hit, might strike’" gives an apodosis force; the form is an optative in a supposition after ὡς εἴ (`l` "were to hit", note "an optative"). · "’were to hit’".
9. κεκαδών · minor · "’having robbed of’" against the house "deprived" (new-renderings row, `l`, note). · "’having deprived of’".
10. καταείσατο · minor · the lemma "καταΐεμαι (ἵεμαι)" is not a dictionary form; the note takes the verb as the aorist middle of ἵεμαι with κατά, as at 4.138. · Lemma now in the form the existing entries for εἴσατο and ἐείσατο use: "ἵημι (mid. ἵεμαι), with κατά".
11. ἀμφίδρυφοί · minor · the sense is the traditional one for this word but the entry did not say so, and the note ties the word to ἀμφιδρυφής (2.700, already in the glossary) while the lemma stood alone. · "ἀμφίδρυφος (cf. ἀμφιδρυφής) — torn all round, i.e. cheeks scratched in mourning (traditional sense)".
12. χραίσμῃσι · minor · "(= Attic opt.)" read as if the form itself were the Attic optative. · "epic -ῃσι (= Attic -ῃ), with ἄν where Attic has the optative".
13. πλάγχθη, τιταίνετο, ἐτάνυσσε · minor · Homeric forms without their Attic equivalent (runbook: Homeric forms name it). · Added (= ἐπλάγχθη), (= ἐτιταίνετο), (= Attic ἐτάνυσε).

Count: 1 high, 5 moderate (items 2, 3, 4, 7, 8), 7 minor (items 5, 6, 9, 10, 11, 12, 13); 13 entries (item 13 covers three forms).

## Changes to `new-renderings.md` (asked for by pass 1)

- A row for ἀπέλεθρον ἀνέδραμε (11.354) added before the ἐρωὴν δούρατος row: `l` "quickly ran back an immeasurable way", `i` "ran quickly back a very great distance"; "measureless" turned down (5.245, 7.269), following the table's ἶνα ἀπέλεθρον "immeasurable".
- The φόβος ἔλλαβε πάντας row now cites the table: "flight" is the table's rendering of φόβος in battle (5.252 and 5.272), and the row records the departure and why ("flight seized all" is not English; the action is a seizing; the table already has φόβος "terror" at 2.767).

## Findings considered and refused

- The other 24 `__broaden__` entries: each old entry was found in `iliad-glossary.json` and kept whole; each added reading was checked against its line (γυναικὸς 393, δεινόν 417, κακόν 362 and 404, κακότητος 382, κατὰ ἶσα 336, λευκὸν 415, μάχην 336, ποδὸς 388 and 397, πόνοιο 430, πῆμα 413, σεύωνται 414, τ’ 409, τεύχε’ 333 and 430, ἄνδρε 430, ἔπι 369, δόλων 430, ἱππόδαμον and ὑπείροχον 335, ὀλέσσῃς 433, υἷε 328). All are warranted (the old entry did not cover that case/number/construction) and correct.
- Known forms read against the part for a missing broadening (all 418 in `known-forms.json`): none needed one. Closest calls, kept: κατ’ (338, "in the hip") is covered by the existing "upon, against" sense (κατ’ ἀσπίδα); ἐπὶ (411, adverbial "on, up") by the existing adverb senses; πῆμα nominative at 347 by the existing "neut. nom. sg., subject" sense; Δαρδανίδαο (371) and δοιοῖσιν (431) differ from the example the old entry gives but the parse and meaning hold.
- ἐπιείσομαι, ἆτ': the "from the εἶμι stem" parse and the "unusual -α vocative" are as in the entries already in the Odyssey's glossary and agree with the notes at 367 and 430; I cannot settle them from the allowed sources. Kept.
- ἔμπνυτο, αἴνυτ: "unaugmented" with no Attic equivalent named; Attic has no corresponding form in use for either. Kept.
- καταείσατο meaning "speed down, dart down": kept; it is the note's reading (the spear came down into the ground).
- ἰὸς / ἰοί given only the arrow reading: the poison reading does not occur in the part, so no " · " pair is called for. βιὸς is already kept apart from βίος.
- ἀγοστῷ "crook of the arm, hollow of the hand": the sense is traditional rather than certain, but the entry states the two usual glosses without claiming more. Kept.
- Entries not listed above (all the other novel forms) were checked for case, number, tense, mood, person, voice, lemma and meaning against their lines, and are correct as written.
