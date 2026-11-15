# aeneid-080 drafter notes (X.689–790)

38 units. Title `Mezentii pugna. Mors Orodis`; part "Mezentius in Battle (X.689–790)"; titleEn "Mezentius in
Battle — Aeneid X.689–790". ¶ units: 689, 747, 755, 769 (all four of Greenough's paragraph starts begin a unit).
make_units.py prints no warnings. `sc` not written. PAIRS = {742: 744, 772: 776} (the two split speech marks).

## Greenough's order 717–718
- Greenough prints 717–718 (`ille autem… hastas`) between 713 and 714. Kept. They fall in the unit ln 712
  (t = lines 712, 713, 717, 718); its n says Greenough prints them here and most editions put them after 716.
  (`prev_end_line` in the script is computed by arithmetic and is wrong across the reordered lines, but no
  paragraph starts nearby, so the p flags are unaffected.)

## Misprints (rule 5b)
- 744 `viderit. ”Hoc`: speech unit 742–744 ends at `viderit.` (t has no closing mark; l and i close with ”); the
  stray ” begins t of unit 744. The n of unit 744 opens "The print has 'viderit. ”Hoc'… corrected here"; the n of
  742 ends "On the closing speech mark, see the next unit."
- 776 `Aeneae. ”Dixit`: same treatment; speech unit 772–776, stray mark in unit 776 (n opens with the print's
  reading).
- 718 `hastas.` followed by lower-case `haud` (714): my own finding. The sentence plainly runs on (simile into
  `haud aliter`), so I treated the full stop as a misprint for a lighter stop: t unchanged, l ends with `;`, the
  next unit's l and i start in lower case, and the n of unit 712 opens with the print's reading. I could not see
  what mark Greenough actually printed, so the n says only "a misprint for a lighter stop". Reviewer to confirm
  this counts under 5b (it may instead be a Perseus artefact of moving the lines).
- 783 `tum` in lower case after 782 `Argos.`: a knock-on of the run's added full stop (rule 5). Per instructions,
  nothing noted in n; l and i begin "Then". Reviewer may prefer to restore a comma/semicolon at 782 instead, or to
  treat `tum` as a 5b misprint for `Tum`.
- No other misprints found (checked capitals after stops, speech marks, odd letters).

## Variants (Latin Library) and how handled
- 705 `Parin creat` / `Parim; Paris`: noted in n of 705–706 (subject of `occubat` named vs. understood).
- 710 `pastus` / `pascit`: noted in n of 707–711 (different construction, same picture).
- 727 `accumbens` / `incumbens`: one clause in n of 726–729 ("much the same").
- 742 `quae` / `quem`: one clause in n of 742–744 ("at which (words)" vs "to whom").
- 785 `transit` / `transiit`: mentioned as an aid to the form (contracted perfect), not as a variant.
- Not noted: 704 `genitori`/`genitore` (dative vs ablative of origin, same sense), 709 `multosve`/`multosque`,
  712 `propiusque`/`propiusve`, 749 `Croniumque`/`Cloniumque` (a name only), and the orthographic ones
  (`praegnans`, `inproba`, `expirans`, `volnus`, `divom`, `volnere`).

## Segmentation
- Two units end at a comma (house practice per 079): 693–697 `fugacem,` (nine-line sentence split) and 707–711
  `armos,` (boar simile). The lion simile 723–729 is split 723–725 `cervum,` (comma) / 726–729, so the half-line
  728 and the anacoluthon `sic ruit` stay in one unit; the n of 726 says 728 is unfinished and that `sic ruit`
  picks up `Hunc ubi… vidit` (722).
- 772–776 is one five-line unit containing Mezentius's whole speech (with `adsint!` inside), so that each split
  speech mark has exactly one partner unit in PAIRS.
- 736–737 (`hasta:` + one-line speech) joined; 762–763 `campo.` and 768 kept short.

## Readings I am less than sure of
- 706 `ignarum`: "a stranger to (the land)".
- 716 `iustae quibus est Mezentius irae`: double dative.
- 754 `insidiis, iaculo et longe fallente sagitta`: n gives the split (javelin = Salius, arrow = Nealces) as
  "perhaps".
- 776 `tropaeum Aeneae`: genitive "of (victory over) Aeneas".
- 782 `dulcis… Argos` taken as accusative plural of `Argi` (cf. `ab Argis` 779).
- 785 `transit`: contracted perfect or present ("perhaps").
- 781: n calls it hypermetric (`caelumque` elided into `aspicit`); I scanned this myself, consistent with the
  scanner's UNRESOLVED flag.

## Attributions written from memory, not checked against a text
- Rock simile Iliad 15.618–621; Latinus as rock Aen. VII.586–590.
- Boar at bay, Odysseus, Iliad 11.414–420 ("perhaps").
- Lion sighting a stag or goat, Menelaus seeing Paris, Iliad 3.23–28.
- Iphidamas the bridegroom, Iliad 11.221–247 ("perhaps"); "bronze sleep" Iliad 11.241 ("perhaps").
- Dying prophecies: Patroclus to Hector 16.851–854; Hector to Achilles 22.358–360; Achilles' reply 22.365–366.
- Patroclus's foot on Sarpedon to draw the spear, Iliad 16.503 ("perhaps"); paean after Hector's death 22.391–394
  ("perhaps"); spear through shield-layers 7.245–248 ("perhaps").
- Orion in the underworld, Odyssey 11.572–575 ("perhaps"); Orion's power to walk the sea a gift from Neptune.
- Strife, head in heaven, Iliad 4.443; Aen. IV.177 the identical line of Rumour.
- Hecuba daughter of Dymas in Homer, Iliad 16.718 ("perhaps"); daughter of Cisseus in Euripides; her firebrand
  dream. Theano wife of Amycus perhaps not Antenor's wife.
- Aen. refs: VIII.481–495 (Mezentius expelled), VII.648 (`contemptor divum`), VII.649–654 (Lausus),
  III.170 (Corythus), IV.41 (`Numidae infreni`), VIII.185–275 (Hercules and Cacus), XII.309–310 (745–746 repeated).
- Vesulus = Monte Viso, source of the Po; Corythus = Cortona (traditional); Valerus and the Valerii.

## Advisory
- None recommended: ordinary battle killing (Latagus's face crushed, Palmus hamstrung, Acron's death-throes, the
  lion simile's gore are brief and conventional).

## New renderings
- None (new-renderings.md says "None.").
