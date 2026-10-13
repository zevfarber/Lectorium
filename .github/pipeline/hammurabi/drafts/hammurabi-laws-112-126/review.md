# Review, pass 1 — hammurabi-laws-112-126

Reviewer: adversarial, strongest model. Inputs: units.json, packet.md, linecheck.md, the plates (Plates 29–33,
Harper's List of Signs pp. 381–411 incl. the list of numerals, Plate 15 for comparison), the published parts
(laws-1-10 … laws-100-111, gap-a, gap-b) and Harper's glossary. units.json edited in place by script
(backup of the drafter's file kept outside the repository). Unit numbers are 0-based indexes into `sentences`
(law and stele line in brackets).

Method for the plates: every stele line of the part was set beside a rendering of the drafter's glyph string in
the project font and compared box by box (sign count, distinctive shapes); every linecheck line, every
Sumerogram, and every reading the drafter marked uncertain was then checked at high zoom against the monumental
forms in Harper's List of Signs.

## Changes

### High (a sign or a reading that does not match the plate, or a sense/force error)

1. unit 5 (§113, XIX 9) · glyphs/reading/note · high · the storehouse Sumerogram was entered as the single sign
   KISAL (reading KISLAḪ), "Harper's and not checked against the plate". On the plate the tail of the line, after
   i-na, is two shapes: KI (the same diamond as ki in XIX 8) and UD (the same shape as BABBAR in KÙ.BABBAR). KISAL
   is a different shape (a block of five horizontals with one upright, Harper's no. 103). · Replaced by two glyphs
   KI (log, val maškanum) + UD (log, val ""); reading KI.UD; morph g [0,1]; note rewritten (Harper's name for the
   ideogram is KISLAḪ; the plate has KI + UD; his list has no entry for the pair).
2. unit 24 (§121, XX 29) · glyphs/reading/lemma/note · high · ÍD entered as A + ENGUR (the river sign). The plate
   shows ONE sign, the same as the sign that spells it in it-tab-ši (XX 9) = A₂ (Á, "arm; hire"). · One glyph A2
   (log, tr Á, val idum); reading Á; morph idum g [0]; note rewritten (the case ending is not written; say idi kept
   but see Unresolved).
3. unit 22 (§120, XX 11) · glyph · high · the last syllable of na-aš-pa-kam was entered as GA with tr "kam". The plate
   draws it as a diamond with a hook inside (the same shape as -kam in il-kam, X 35, Plate 15), which is KAM; the GA
   sign is the shape of ga-ri-tim (XX 8) and ga-am-ri-im. · glyph sign GA → KAM (role phon, tr kam, reading
   unchanged); sentence added to the note. NB the published laws-26-41 (il-kam, a-la-kam) and gap-a (il-kam) enter the
   same syllable as GA: see "For the owner" below; this part now differs from them.
4. unit 18 (§118, XIX 71–73) · l/i/n · high (l ↔ i force) · l read "the-merchant has-passed-on; for silver he-may-give",
   i read "the merchant may pass him on and sell him", and the note called ušētiq a perfect. ušētiq is a Š PRETERITE
   (perfect would be uštētiq), so "may pass on" has no support in the form, and l and i disagreed. · l: "…for silver
   he-gives…"; i: "and the merchant has passed the slave on and sold the slave for silver, no claim shall be made on the
   slave."; note: preterite, read as a further condition with the ruling in ul ibbaqqar; uncertainty kept.

### Medium

5. unit 15 (§117) and unit 17 (§118) · morph lemma · medium · lemma kiššatum is the published prologue entry "totality,
   all (written with the KIŠ sign)"; the build would broaden it with an unrelated word. Harper lists the two as
   separate entries (KISSATU "service" 19,59/69; KISSATU "everything, the universe"). · lemma → kiššātum (new entry
   for the glosser); note says it is a different word.
6. unit 30 (§125, XX 67) and unit 33 (XXI 4) · morph lemma · medium · mi-im-ma-šu (mimmâšu) had lemma "mimma"; the
   published parts use lemma mimmûm for the same form (laws-1-10 etc., Harper's MIMMU). · lemma → mimmûm.
7. unit 16 (§117, XIX 61) · say/note · medium · MU 3{kam} said "šattam šalaštam" with the note "as in §30"; at §30 the
   published glossary has "the third year", while for a plain count ("for three years") laws-42-51 and 52-65 say
   šalāš šanātim. Here the sense is a duration (three years, then release in the fourth). · say → šalāš šanātim;
   note says so.
8. unit 3 (§112, XVIII 72) · say/morph/note · medium · innadnūšum (long ū, "the subjunctive -u sits on the plural,
   as the whole consignment is in view"): the published parts (laws-26-41 §37, 52-65) have innadnušum, subjunctive
   -u before the dative suffix, morph nadānum-N + -šu. The "plural" explanation is also wrong (the plural ending
   is not what the signs show; consignment is a collective). · say → innadnušum; morph [nadānum-N 0–3, -šu 4]; note
   corrected.
9. unit 5 (§113, XIX 13) · say/lemma/note · medium · u-ta-ar said utār with lemma târum (G); every published
   occurrence (100-111 §102, §104) is utâr, lemma târum-D "to give back". · say utâr, lemma târum-D; note.
10. unit 5 (XIX 10) · say/note · medium · li-qi₂-im said liqim; the published form for the same spelling is leqîm
    (100-111 §106). · say → leqîm; note.
11. units 8 and 14 (XIX 24, 49) · say/val · medium · MA.NA said "manê"; the published parts say mana (11-25 §24,
    52-65 §59). · say → mana; val of MA → mana.
12. unit 24 (§121) · note · medium · the note wrote Harper's measure sign as "ḲA". The owner's rule (2026-10-12): q
    everywhere reader-facing, including when citing Harper. · "ḲA" → "QA". (The only ḳ/Ḳ in the file; none in
    glyph/reading/say/l/i.)
13. unit 16 (§117, XIX 62) · say/note · medium · É said "bītim" (genitive) before the genitive šāyamānišunu u
    kāšišišunu; the construct state is bīt (Harper prints bît). · say → bīt; note says construct state.
14. unit 16 (XIX 64) · say · medium · ri-bu-tim said "ribūtim"; published rebûtim (42-51, glossary rebûm). · say →
    rebûtim; note.
15. unit 3 (§112) and about · i/about · medium · "up to five times" for a-du 5-šu; the published parts render the
    multiplier "five times" (11-25 §12), "three times as much" (100-111 §106), "six times" (§107); conventions:
    adi 3-šu / 6-šu "three / six times". · i: "five times"; about: "five times its value".
16. unit 0 (§112, XVIII 54) · say/note · medium · qa₂-ti-šu said qātišu; the published parts have qātīšu for this same
    spelling (gap-b; glossary of laws-100-111). · say → qātīšu; note "of his hands (so spelled in the earlier parts)".
17. unit 35 (§126, XXI 19) · say · medium · ubāršuma with a macron, while the same stem is ubârma in the published
    11-25 §23 and in unit 23 of this part (the circumflex marks the contraction). · say → ubâršuma; note and about
    follow.

### Low

18. units 10 and 11 (§115, §116) · i · low · "in the house of her distrainer": the -ša is the grammatical gender of
    nibūtum; the English "her" makes the hostage a woman. · i: "in the distrainer's house" (l keeps the literal
    "her-distrainer").
19. unit 1 and unit 2 (XVIII 60, 61, 67) · say/note · low · šu-bu-lu said šubulu / šubulūma: the Š-stem has the long
    ū (stative šūbul; ušābil in unit 0 is the same stem). · šūbulu, šūbulūma; note says so. (Harper's spelling carries
    no length; sense unchanged.)
20. unit 31 (§125, XX 75) · say/note · low · i-gu-ma said igūma; egûm is final-weak, so subjunctive + -ma is igûma
    (as ilqû for il-qu-u). · say and note → igûma.
21. unit 33 (§125, XXI 6) · say/note · low · šarrāqānīšu: a singular genitive before -šu has the short vowel (bītišu,
    ṣibtišu). · šarrāqānišu.
22. units 33 and 35 (XXI 4, 16) · morph lemma · low · ḫalqam / ḫalqu entered as new lemma ḫalqum; the published entry
    ḫalāqum already lists "ḫalqu, ḫalqam". · lemma → ḫalāqum (saves a duplicate entry).
23. unit 15 (§117, XIX 57) · note · low · the note called DUMU.SAL-zu "uncertain, my reading of the plate". Checked:
    the second row of XIX 57 reads ù, DUMU, SAL, zu. · note now states it (Harper's mâra-zu kept).
24. about · low · "a creditor who takes grain or silver from a debtor's store": §113 says grain (the claim is
    grain and silver, what he takes is grain); also the old KISLAḪ/ÍD and "up to five times". · about corrected
    (grain from a debtor's bin or storehouse, without the owner's say; Á for hire, KI.UD for the storehouse; "five
    times").

Severity counts: high 4, medium 13, low 7 (24 items).

## Checked and left (no change)

- All 208 stele lines: unit start lines, `nl` flags (incl. the glyph-level nl in na-ba-al-ka-at-tim across XX 71/72),
  and word division agree with Harper's lines. `p`/`ln` on the first unit of each law only (15 laws) — correct.
- Linecheck lines, each against the plate: XVIII 53 KÙ.BABBAR KÙ.GI NA₄ (NA₄ is the two-shape sign of Harper's no.
  97 abnu: ▷ + a hooked wedge — matches; the "single diamond" of the font is only the font's drawing), XIX 1/19/28
  ŠE ù KÙ.BABBAR, XIX 24/49 the fraction (see Unresolved), XIX 44 DAM.GÀR, XIX 57 SAL/DUMU/DUMU.SAL, XIX 61 MU + 3 +
  KAM (three shapes on the plate), XIX 72/78 KÙ.BABBAR, XIX 77 GEME₂ (SAL+KUR) and DUMU{meš} (DUMU, ME, EŠ: the
  three Winkelhaken), XX 1 DAM.GÀR, XX 10/19/XXI 3 É, XX 28 ŠE.GUR.E (ŠE, GUR, E) with 5 and SÌLA₃ (lozenge with a
  cross), XX 33/55 KÙ.GI, XXI 1 ŠA-GA (GAR + GA; the GA shape of the font matches the plate). All as drafted except
  items 1–3 above.
- XX 6 a-wi-lum (not -lim): the last sign matches LUM, as Harper prints. u₂-lu (U2 + LU) matches in XIX 4/9/XX 10.
  ušētiq XIX 71: u, ŠE (the barley sign), ti, iq — matches. babtum (ba-ab-ta-šu), utebbir, ubāršuma: syllabic,
  sign counts match; Harper's glossary has BABTU "loss, defects", ABARU II,2 "to file a claim for: u-te-ib-bi-ir",
  BARU II,1 "to declare, to itemize: u-ba-ar-šu".
- Glyph roles of ZU in SAL-zu etc. and TI in É-ti-šu left as phon (the published parts do the same).
- Reading reconstructs from the glyph `tr` for every word (the three differences — a-du 5-šu, MU 3{kam},
  DUMU{meš} — are the usual space / determinative conventions, as in the published parts). Every sign key exists in
  signs-cuneiform.json (KAM, A2, KI, UD were already there; no signs.py run needed). Every glyph covered by a morph.
- Cross-references checked in the published parts: ittakir §106, ikkiru §107, maḫar ilim §9 and §23, ītelli §35/§37,
  iriab §6/§105, makkūr (ŠA.GA) §6, iššakkan §105, uštašannâma §101, idukkūšuma §21, MU 3{kam} §30. All correct.
- Remembered English / copyright check: no phrase recognised as a fixed modern rendering (the only stock phrases
  are "natural death", "no claim", "make good", all built from the grammar here). q not ḳ: clean after item 12.
- Harper's apparatus points kept: XX 71/72 word split; XX 75 long line with two clauses; XXI 1 ŠA-GA printed with
  a hyphen (plate: two signs); XIX 7 šêʾim circumflex (irrelevant to the signs).

## Refused (suggestions not taken)

- Rewriting ittabši (unit 21) to the unmarked lemma bašûm used in 42-51: refused. gap-b already holds the entry
  bašûm-N ("N-stem of bašûm"), the form is an N perfect, and conventions use stem-labelled lemmas (bašûm-Š). Left.
- Changing the numeral reading of the fraction "šalšāt" (unit 8, 14): refused as a guess against a guess; left and listed
  under Unresolved.
- Changing nēbīša (unit 10, 11) to a short vowel like šarrāqānišu: refused; the noun's pattern (a participle-like form
  from nebûm, with -ša) is not secure enough to apply the rule.
- Changing "idi" to the construct "id" (unit 24): refused; the case ending of the Sumerogram is not written and
  Harper gives no form. Left, noted.
- Replacing GA by KAM in the published laws-26-41 / gap-a: out of scope (not this part's files); reported below.
- "ibbûm" (unit 21) "accident": Harper's gloss (IBBU, accident, XX 9 only); kept as drafted with the drafter's
  uncertainty note.
- Respelling šībī, našpakūtim, andurāršunu, kāšišišunu: no grounds against Harper's forms; left.

## Unresolved (for the second pass / the owner)

1. unit 35 (§126, XXI 15–19): l ("he-shall-prove-him-and") is active, i ("the one he accused shall be proved before
   the god") passive; the subject of ubâršuma is not secure and "babtum = the person he holds liable" is the
   drafter's reading against Harper's "loss, defects". The note carries the uncertainty; the voice mismatch between l
   and i remains. Severity low-medium. Second pass should decide whether l becomes "they-shall-prove-him" (impersonal)
   or i is reworded.
2. units 8, 14: the Akkadian word spoken for the ⅓ sign ("šalšāt", with a long ā) is a reconstruction; the plate
   shape (two uprights over a long horizontal) is the nearest Unicode ⅓ and Harper's own list of numerals draws "1–3"
   as a longer group. The glosser must mark it "(?)".
3. unit 24: say "idi" for Á našpakim (genitive ending vs construct "id").
4. unit 18: the whole reading of ušētiq … inaddin … ul ibbaqqar as condition + ruling (changed here) rests on form
   only; the owner's/merchant's act is uncertain.
5. unit 21: ibbûm "accident" (Harper's single attestation).
6. unit 5: the KI.UD identification is by shape; the Sumerogram name is Harper's KISLAḪ; his sign list does not
   contain it, so the pair is the plate's, not a list identification.

## For the owner / records (not part of units.json)

- Published laws-26-41 §27 (il-kam, a-la-kam, X 35–36 on Plate 15) and gap-a (il-kam) spell -kam with GA; on Plate 15
  (X 35) the sign is the KAM shape (diamond with a hook), as here. Suggest a QUESTIONS.md line and, if the owner
  agrees, a one-off correction of those words (not done: not this part's files). laws-1-10 (kunukkam) uses KA, which
  would also need checking.
- Glossary work for the glosser (new lemmas): šubultum, našpakum, maškanum, nibūtum, nebûm, 1/3, mâtum, uššušum,
  kāšišum, andurārum, etēqum-Š, baqārum-N, walādum, padārum, šapākum, šapākum-N, garītum, ibbûm, gamrum, 5, qûm, idum,
  kullumum, šalāmum-D, šeʾûm, šarrāqānum, babtum, ragāmum, kiššātum (new, distinct from kiššatum). Known lemmas to
  broaden at least: nakārum (the only entry is the gap-b "UNCERTAIN … only ik survives" one), šanûm-Š, bârum
  (ubâršuma, "prove him"), târum-D already covers utâr, ḫalāqum covers ḫalqam/ḫalqu, mimmûm covers mimmâšu.

---

# Review, pass 2 — hammurabi-laws-112-126

Reviewer: adversarial, strongest model. Inputs: units.json (as left by pass 1), gloss.json (Sonnet), conventions.md,
the five-plus published parts (all `hammurabi-*.json` glossaries, latest holder per lemma), the pass-1 notes.
units.json and gloss.json edited in place by script (backups outside the repository). Unit numbers are 0-based.
Method: every gloss.json entry read against the forms of the text and the notes; every `__broaden__` base compared
by script with the whole entry of its latest published holder (all 28 of the Sonnet draft start with the old entry exactly; all lemmas
used in the part and already published were also tested for forms the old entry does not cover); units.json re-read
for labels, l ↔ i, and tense.

## Changes — units.json

1. unit 35 (§126, XXI 15) · l/i/n · high · l "he-shall-prove-him" was active, i "the one he accused shall be proved"
   passive, and the note kept "who is the subject" open. The form is a singular active D present (ubâr) + -šu "him" + -ma,
   so a passive "shall be proved" had no support. · babtašu is read as the subject (the accused), -šu as the claimant:
   i "the one he accused shall prove it against him before the god, and"; l unchanged; note gives the other reading
   (babtašu object, claimant subject; Harper's gloss "to declare, to itemize") and stays UNCERTAIN.
2. unit 34 (§126, XXI 8) · note · medium · utebbir was called "D-stem perfect". Harper (per pass 1) lists it under
   ABARU II,2, his stem for the reflexive of the intensive (Dt), and u-te-ib-bi-ir has no perfect infix after the u;
   it is a Dt preterite. · note says so ("file a claim for" fits a reflexive).
3. unit 33 (§125, XXI 3) · lemma/note · medium · iš-te-ne-i-ma was called "a perfect with the repeated -ten-". The
   infix -ten- is the Gtn (iterative) stem and the tense is present (ištenēʾi). · lemma šeʾûm → šeʾûm-Gtn (new entry),
   note corrected, stem analysis marked UNCERTAIN (Harper gives only "to search for").
4. unit 19 (§119, XIX 74) · say/note · medium · ulidūšum: the verb is a w-initial verb, whose preterite is ūlid (long ū),
   and the subjunctive -u before the dative -šum stays short (the house pattern: innadnušum, iddinušum). · say
   ūlidušum; note says preterite ūlid, vowels UNCERTAIN (Harper's ul-du-šum is shortened).
5. unit 21 (§120, XX 4) · lemma/note · medium · našpakūtim was explained as a "plural-looking form of Harper's own";
   it is the abstract in -ūtum (as maṣṣarūtim in the same part). · lemma našpakūtum (new entry); note corrected.
6. unit 31 (§125, XX 70) · i/n · medium · nabalkattum rendered "pillage" (Harper) although the published gap-b entry,
   the part's only earlier use, reads it as "crossing-over" (nabalkutum) and marks it UNCERTAIN. · i: "through a breach
   or through a crossing-over (?)"; note gives both; `about` follows; nabalkattum broadened (see gloss, item 24).
   Also the note's "written bi-il-ši-im" vs reading pi₂-il-ši-im: now says Harper prints BI and it is read pi₂.
7. unit 1 (§112, XVIII 59) · n · medium · šūbulu called Harper's Š-stem "passive or infinitive-like"; itbal called a
   perfect (the perfect is ittabal; itbal is the preterite); the reason given for lā was wrong. · note: Š stative
   šūbul + -u, UNCERTAIN force; itbal preterite; lā = negative inside an "if" clause.
8. unit 18 (§118, XIX 71) · l/i · medium · l "he-gives" (present) against i "has … sold" (past): tense disagreed. ·
   i: "passes the slave on and sells the slave for silver" (English conditional present), note says why; l "not
   he-shall-be-claimed" (closer to ul ibbaqqar).
9. unit 2 (§112, XVIII 64) · n · low · "Uncertain: Harper's reading of ukannūšu(ma) as plural; a singular … is not what
   the signs spell" was an empty doubt (the plural -ū is spelled). · removed; note labels the form "D present, plural"
   and shows šūbulu + -ma = šūbulūma.
10. units 10, 11 (§115, §116) · say · low · É said bītim before the genitive-with-suffix nēbīša; construct state is
    bīt (as in item 13 of pass 1). · say bīt; unit 10 note explains; the noun nēbīša marked UNCERTAIN in shape.
11. unit 11 · n · low · note wrote "ma-ḫa-zi-im" but the reading and glyphs are ma-ḫa-ṣi-im (ZI read ṣi). · fixed.
12. unit 7 (§114, XIX 17) · n · low · Harper's b-spellings of the hostage words: later dictionaries write them with p
    (nepûm, nipûtum). · flagged in the note and in the nibūtum/nebûm entries (Harper kept as base).
13. unit 9 · l · low · l "he-has-distrained-and" for a preterite (ibbi). · l "he-distrained-and".
14. unit 14 · n · low · "the merchant pays the price of a slave": the law says a third of a mina; "price" is not in it.
    · removed.
15. unit 16 · n · low · "rebûtim šattim is 'the fourth year'" left out ina. · "ina rebûtim šattim … 'in the fourth year'".
16. unit 3 · n · low · "the first multiplied damages of the part" (meaningless); innadnušum not labelled. ·
    "a multiple of the loss"; "N-stem passive (preterite)".
17. unit 4 · n · low · "house wording" for "without the consent of" (the words say "without the owner"). · now says it is
    English idiom.
18. unit 8 · n · low · the reconstructed spoken ⅓ (šalšāt) was not said to be so in the note. · added; glossary has (?).
19. unit 12 · n · low · ukānma labelled only "singular". · "singular present".
20. unit 15 · n · low · iṣbassuma tense unlabelled (glossary said "perfect/preterite"). · preterite iṣbat + -šu + -ma.
21. unit 24 · n · low · "SILA₃" while the glyph and the glossary say SÌLA. · SÌLA.
22. unit 26 · lemma/n · low · lemma kullumum (the D infinitive) against the house habit of stem-labelled lemmas
    (kânum-D). · lemma kalāmum-D (new entry), note: D present of kalāmum.
23. unit 32 · n · low · ušallamma tense unlabelled. · "D present".
24. unit 34 · n · low · mimmēšu (oblique spelling for a subject) and Harper's brackets; babtum as "city quarter" in later
    dictionaries. · both said in the note (Harper kept as base).
25. `about` · low · "break-in or pillage" · "a breach or a crossing-over".

## Changes — gloss.json

26. kânum-D (broaden) · medium · the old entry lists uktīn and ukannūšuma without labels; the new reading gave only
    ukānma. · whole old entry + "uktīn (perfect, with the infixed -t-) … ukannūšuma (present, plural, -šu, -ma) …
    ukānma (present, singular)". NB uktīn has the infixed t after the first radical (uk-ti-in), so it is the D perfect,
    not a preterite (the preterite would be ukīn); the entry says perfect.
27. bârum (broaden) · medium · "he shall prove him (right)": "(right)" is invented. · "he shall prove him, and"; Harper's
    "to declare, to itemize" added; who proves whom UNCERTAIN.
28. abārum (broaden) · medium · utebbir "D perfect" (see item 2). · "Dt preterite, Harper's stem II,2, the reflexive of the
    D-stem", "he has made a claim against".
29. wabālum-Š (broaden) · medium · šūbulu/šūbulūma called a Š-stem with "passive" sense; ušābilšu tense not given. · Š
    stative šūbul + subjunctive -u, UNCERTAIN; ušābilšu preterite.
30. nadānum (broaden) · medium · listed an infinitive "ana maṣṣarūtim nadānum" that is not in the part (the text has
    inaddin/iddinma). · replaced with "ana maṣṣarūtim inaddin".
31. nakārum · medium · used 9 times in the part (ittakir, ittakiršu, ittakrūšu, ikkiru) but not broadened; the published
    entry is the gap-b one that begins "UNCERTAIN … only ik survives". · broadened (old entry whole + the forms, and a
    plain statement that here the verb is spelled out).
32. mimmûm · low · published entry only has mimmûšu; the part adds mimmâšu, mimmê, mimmēšu. · broadened.
33. nabalkattum · medium · see item 6; published entry is a guess for a broken word; here the word is whole. ·
    broadened, UNCERTAIN kept.
34. egûm (broaden) · low · "a preterite or stative form … UNCERTAIN" was vague for igûma. · "the preterite igi with the
    relative -u (as ilqû beside ilqe), then -ma".
35. ṣabātum, tabālum, wašābum (broaden) · low · iṣbassuma "perfect/preterite" → preterite; itbal "perfect" → preterite;
    wašib "stative/participle" → stative (wašib is not a participle).
36. šattum (broaden) · low · MU 3{kam}, šalāš šanātim added (the part's own use).
37. babtum · medium · see item 1; entry now says the party accused, with the later "city quarter" understanding.
38. walādum · medium · ūlidušum (item 4). nibūtum, nebûm · low · p-spellings flagged; nēbīša shape UNCERTAIN.
39. new entries kullumum → kalāmum-D, šeʾûm → šeʾûm-Gtn, + našpakūtum (items 3, 5, 22); našpakum loses the
    "plural-looking" remark.

Severity counts for pass 2: high 1, medium 14, low 24 (39 items).

## Checked and left (no change)

- Every `__broaden__` base: the whole old entry of the latest published holder, verbatim, then " · " + the new
  reading (28 entries; pass 2 added three, nakārum, mimmûm, nabalkattum, making 31). No base had drifted. All added readings use
  forms actually in the part (checked form by form; the stray infinitive in item 30 was the only invented one).
- New entries checked against the text: šubultum, maškanum (KI.UD, UNCERTAIN), 1/3 ((?), UNCERTAIN), mâtum (imtūt is
  the G perfect), uššušum, kiššātum (distinct from kiššatum), kāšišum, andurārum, etēqum-Š (ušētiq a Š preterite),
  baqārum-N (ibbaqqar N present), padārum, šapākum (išpuk preterite), šapākum-N (iššapku N preterite + -u), garītum,
  ibbûm (UNCERTAIN), gamrum, 5, qûm and idum (UNCERTAIN), šalāmum-D (ušallamma D present), šarrāqānum, ragāmum
  (irgumu preterite + -u). No invented root found; all q, no ḳ in either file or in the built story.
- Reading ↔ glyph `tr`, q, glyph keys, `nl`, `p`/`ln`: unchanged since pass 1 and re-checked by the gate (validate).
- Remembered English: none recognised. "natural death", "no claim", "make good" remain grammar-built.

## Refused (not changed, with reasons)

- Changing say šalšāt for ⅓ to another word: no evidence either way in the sources; stays (?) and UNCERTAIN.
- Changing "idi" to construct "id": still no spelled ending; UNCERTAIN in the entry. Left.
- Changing ittabši (bašûm-N lemma) or uštašannâma (šanûm-Š): follow the published entries; the stem is uncertain there too.
- Changing nēbīša to nēbîša / nēpîša: form of the noun not secure; marked UNCERTAIN instead.
- Making ittandin a different tense: the note's "perfect with an extra -n-" kept as spelled; it is the perfect.
- "bītim" in units where bēl governs it (bēl bītim): genitive after the construct bēl is right; only the É before a
  suffixed genitive (units 10, 11) was changed.

## Gate

`r3.py build` BUILT (37 units); `r3.py validate` PASS (one WARN: 21 stele lines differ from Harper's transliteration —
the linecheck list, each confirmed on the plate in pass 1); `signs.py check` in sync.
