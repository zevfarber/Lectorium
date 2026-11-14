# aeneid-070 (IX.621–716) — drafter's notes

43 units; `make_units.py` runs clean (no LINE COUNT / TOO LONG / NEWLINE / ENDING / NOTE LENGTH warnings). `t` comes only
from `A.cut`; no `sc`. Every note is under 140 words (longest 109: the 642–644, 668–671 and 710–713 units).
Paragraphs: 621, 672, 691 (all `p: true`; each note opens "A new paragraph in Greenough.").

## Speech marks

- Ascanius's prayer: “ 625 (`Iuppiter`) … ” 629 (`harenam.”`).
- Ascanius to dead Numanus: “ 634 (`“I, verbis`) … ” 635 (`remittunt.”`), cut as two units at `superbis!`.
- Apollo in his own form: “ 641 (`“Macte`) … closing mark misprinted at 644 (see below).
- Apollo as Butes: “ 653 (`“Sit satis`) … closing mark misprinted at 656 (see below).
4 “ / 4 ” in each of t, l, i. In t the two misplaced ” stand at the head of the 644 `”Simul` and 656 `”Sic` units; in l and i
the speech closes on the unit before (642–644 `capit.`, 654–656 `bello.`) and the following unit carries no mark. This is
the 042 handling (`parens. ”Sic`), not the 066/067/069 run-on handling, because running on would make both units six lines
(641–646, 653–658), over the five-line limit.

## Misprint calls (rule 5b; t as printed, l/i corrected, note opens "The print has X, a misprint for Y, corrected here.")

1. **9.635 `His`** for `Bis` (wrong letter). Ascanius is quoting Numanus's `bis capti Phryges` (9.599) back at him;
   `His capti`, "captured by these", gives no sense. Latin Library `bis`. Scansion is unaffected. Unit 635.
2. **9.644 `capit. ”Simul`** for `capit.” Simul` (closing mark joined to the next word, as 9.392, 9.561). Unit 642–644
   (note) and 644–646 (`t` starts with the mark; its note says so).
3. **9.654 `magnus, Apollo`** for `magnus Apollo` (stray comma). Apollo, disguised as Butes, names himself in the third
   person (`magnus Apollo concedit`); there is no vocative, and the comma cuts the adjective from its noun. If the reviewer
   thinks a stray comma is too slight for rule 5b, the note can be reworded as "Greenough's comma… read without it".
   Unit 654–656.
4. **9.656 `bello. ”Sic`** for `bello.” Sic` — same as 644. Same unit 654–656 (the note gives both calls, the comma first),
   and 656–658 starts with the mark.
5. **9.683 `inrumpunt`** with a small letter after the full stop at 682 (`nutant.`), for `Inrumpunt`. Unit 683–686.
   I did not treat the lack of any mark after `patentis` (683) as a misprint: with Greenough's punctuation the four named
   Rutulians are the subjects of `inrumpunt` and the `ut` clause is parenthetic, which reads cleanly.

## Kept as printed (doubtful readings / Latin Library variants)

- **676 `freti animis`** (LL `armis`): both give sense ("trusting in their courage / their arms") and both scan; noted in
  the 672–676 unit.
- **686 `at versi`** (LL `aut`): Greenough's `at… aut` vs LL `aut… aut`. Same meaning (they fled or fell); noted in the
  686–687 unit.
- **645 `misit`** (LL `mittit`): tense only, no change of sense; not noted.
- Orthographic, ignored: 677 `adstant`, 679 `aëriae`, 699 `aëra`, 700 `volneris` (Greenough's forms mentioned as his).
- Interpretive choices flagged in notes: 657 `mortalis aspectus` taken as "mortal sight" (alternative: his mortal
  appearance); 668 `ab occasu` as "from the west" (alternative: the setting of the Kids); 709 subject of `intonat` taken as
  Bitias (`ingens`), alternative the earth; 697 `Thebana` as probably Thebe in the Troad.

## Set pieces

None (checked against the conventions list). `sic itur ad astra` (641) is famous but not on the list; I rendered it
"so one goes to the stars" (l) / "This is the road to the stars" (i), built from the Latin.

## Advisory: none

Ordinary battle killing (Numanus shot through the head; Antiphates' lung wound; Bitias felled). No sexual violence.
Consistent with 067–069.

## Scansion worries (for the reviewer)

- **640, 652 `adfatur Iulum`** (flagged): `Iulum` is three syllables, `Ĭūlum` (cf. 1.267 `cognomen Iulo`), giving fifth
  foot `fā tŭ rĬ | ū lūm`. 640: `nū bĕ sĕ | dēns āt | qu(e) hīs vīc | tō r(em) ād | fā tŭ rĭ | ū lūm`.
  652: `āt qu(e) hīs | ār dēn | tēm dīc | tīs ād | fā tŭ rĭ | ū lūm`. The scanner seems to treat the I as consonantal and/or
  not to elide `atque his`.
- **647** (flagged): hiatus `Dardanio | Anchisae` and spondaic fifth foot:
  `ān tī | qu(um) īn Bū | tēn hīc | Dār dă nĭ | ō Ān | chī sae` (13 syllables, one dactyl).
- **650** (UNRESOLVED): hypermetric line; `coloremque`'s `-que` elides into `et` at the start of 651:
  `ōm nĭ ă | lōn gae | vō sĭ mĭ | līs vō | cēm quĕ cŏ | lō rēm(que)`. Needs a hand fix; I do not know how the validator
  treats a hypermetric syllable.
- **673** (flagged): `Iovis` consonantal I; `Iaera` taken as three syllables `Ĭ-ae-ra`:
  `quōs Yŏ vĭs | ē dū | xīt lū | cō sīl | vēs trĭ sĬ | ae ră`. I am not certain of Iaera's quantities.
- **674 `abietibus`**: consonantal i, `āb yĕ tĭ | būs yŭ vĕ | nēs pă trĭ | īs ēt | mōn tĭ bŭs | aē quōs`.
- **634 `traicit`**: consonantal i after prefix (`trā yĭ cĭt`), and `I` (imperative) one long syllable.
- **698 `coniecto`**, **711 `iaciunt`**, **698/704 `iaculo`**: consonantal i.
- **716 `Typhoeo`**: synizesis of `-eo`; `Iovis` consonantal: `Ī nă rĭ | mē Yŏ vĭs | īm pĕ rĭ | īs īm | pōs tă Tў | phōe(ō)`
  — check.
- **Ae- / eu**: 636 `Teucri`, 710 `Euboico` (eu one syllable); 638 `Aetheria`, 645 `aethere`, 653 `Aenide` (Ae- one
  syllable); 679 `aëriae` and 699 `aëra` have a diaeresis (a-e two syllables).
- 690 `eodem` read as three syllables (`rān tŭr ĕ | ō dēm`).
- 676 `fret(i) animis` elision; 715 `Prochyt(a) alta`.

## Attributions made from memory or inference (please check)

- Checked in source: 2.693 `intonuit laevum` (Anchises's omen); 9.599 `bis capti Phryges`; 9.593 `cui Remulo cognomen`;
  9.40–43 Aeneas's order to stay inside the walls; 1.267–268 Iulus's name; Butes at 5.372 and 11.690–691 (different men).
- Unchecked: Georgics 1.40 (`audacibus adnue coeptis`); Eclogue 3.87 (`iam cornu petat et pedibus qui spargat harenam`,
  said to be repeated word for word); Iliad 1.528 (Zeus's nod to Thetis); Iliad 17.322–325 (Apollo as the herald Periphas
  rousing Aeneas); Iliad 1.46 (Apollo's arrows rattling as he comes down); Iliad 12.156–158 (stones like snow from the
  Greek wall); Iliad 12.131–134 (the two Lapiths before the gate like oaks); Iliad 4.504 (`and his armour rang upon him`,
  a formula); Iliad 2.783 (`ein Arimois`, Typhoeus); Sarpedon killed by Patroclus (Iliad 16).
- Background from memory: Assaracus as Anchises's grandfather; Roman augury favouring the left; gilded horns of victims;
  white victims for the gods above; amentum (javelin thong); the Haedi as stormy stars; phalarica as a siege-spear often
  wrapped in burning tow; Cumae founded from Chalcis in Euboea; Roman piers of sunk masonry at Baiae; Inarime = Ischia with
  Typhoeus beneath; Thebe in the Troad (given as "probably").
