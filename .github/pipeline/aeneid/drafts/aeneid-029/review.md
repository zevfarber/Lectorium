# aeneid-029 (IV.504–606): reviewer's record

Two passes. (1) Every grammatical label in every note checked against its form and its line, every citation checked against
`source/aeneid-greenough.json`. (2) Latin against `l` word by word (including misattached adjectives), `l` against `i`, `i` for
echoes of remembered English versions, speech marks, line division of `l` against `t`; then a full re-read of the edited
`units.json`. Scansion: I scanned every one of the 103 lines against the scanner's printout (`scan_latin.scan_line`), and checked the
vowel quantities of the scanner's reading syllable by syllable, because the scanner leaves open vowels free and fits the metre
(it can be right in shape and wrong in vowels, as at 504 and 526). `units.json` was edited by script
(`t`, `ln`, `p`, `v` asserted unchanged; every `l` keeps the line count of its `t`; “ and ” counts per unit unchanged in `l` and `i`).
`draft.py` was regenerated from the edited units and `make_units.py` reproduces `units.json` byte for byte (do not restore the old
`draft.py`). No modern translation was consulted; every rephrasing below was built from the Latin.

Counts: units/notes/about **major 6, medium 18, low 55**; scansion **major 6, medium 2, low 3**.
Overall **major 12, medium 20, low 58**.

## Speech marks (checked, no change)
“ opens unit 12 (534) and ” closes unit 22 (552, Dido); “ opens unit 27 (560) and ” closes unit 32 (570, Mercury); “ opens unit 35
(573) and ” closes unit 39 (579, Aeneas). Dido's second speech opens on unit 47 (590) and has no closing mark: it runs past the end of
this part (607 ff.), and the last unit (58) correctly carries none. `l` and `i` carry the same marks on the same units as `t`, with one
exception that is left on purpose: Greenough prints a second “ at the head of 591 (`“hic ait`), which `t` keeps and the note
explains; `l` and `i` carry only the opening “ at 590. The validator will therefore WARN on `l` and `i` (4 opening, 3 closing) and `t`
(5 opening, 3 closing); this is expected for a speech that crosses the part boundary.

## Units: major
- **5 (520–521) `n`.** "'amantes curae' … is a double dative": `amantes` is an accusative (object of `habet`); `curae` is the one
  dative (of purpose, predicative). Rewritten.
- **19 (547) `n`.** "It is the first time she speaks of her death in so many words": false; she says `moribundam` at 4.323. Now "She
  now says in so many words that she should die."
- **30 (566–568) `n`.** "The warning is fulfilled within a few lines: the dawn comes at 584": false; Dawn comes but the fleet is gone
  (the note on unit 44 says so). Now "The dawn comes at 584, but by then the fleet is gone."
- **38 (576–577) `n`.** "`deorum` as an old genitive plural": `deorum` is the ordinary full form (the old forms are `deum`, `divom`). Now
  "a partitive genitive plural".
- **43 (583) `n`.** "used word for word elsewhere in the poem (Books 3 and 5)": checked against the source: 3.208 is the same line;
  5.778 is `Certatim socii feriunt mare et aequora verrunt` (3.290 is the same line as 5.778), not a repeat. Now "repeated word for word at 3.208".
- **48 (592–593) `l`.** "Will they not arm": `arma` (object of `expedient`) turned into a verb and lost. Now "Will they not make arms ready".

## Units: medium
- **3 (515–516) `n`.** "The line is short, a little under a full hexameter": 516 is a half-line of eight syllables. Now says so and points to 4.44,
  4.361, 4.400, 4.503 (all half-lines in `scan-fixes.json`).
- **6 (522–524) `n`.** "modelled on … Apollonius of Rhodes (Argonautica 3)" and "the comparison with Medea runs through Dido's
  story": unchecked, and no copy of Apollonius is in the pipeline. Softened to "readers compare … the scene in Apollonius of Rhodes
  where Medea alone lies awake"; no book number, no claim about the rest of the story.
- **7 (524–525) `n`.** "puts the singular verb with the nearest subject": `tacet` has `omnis ager` as subject; the animals are a
  loose list, among the subjects of `lenibant`. Rewritten.
- **8 (526–528) `n`.** "`quae` stands for neuter plural": `quae` is feminine (it agrees with `positae`). "Without it the sentence has no
  main verb" overstated (the clauses have finite verbs; it is `positae` that hangs). Both rewritten.
- **16 (540–541) `n`.** "`sinet` has the same understood `me`; `invisam` agrees with the understood `me`": `me` is expressed (`Quis me
  autem … sinet`). Now `me` is the object of `sinet` and `accipiet`; `invisam` agrees with `me`.
- **18 (543–546) `n`.** "`revelli` … is, like `agam` and `iubebo`, in a series of questions in the future": `revelli` is a perfect inside the
  relative clause. Rewritten.
- **28 (563–564) `l`.** "She schemes and dread outrage … turns over" made `dolos` read as a verb. Now "She treacheries and dread outrage
  in her breast turns over" (matches the note's "treacheries").
- **28 (563–564) `n`.** The parenthesis "(from her pyre we know it is her death, though Mercury makes it sound like a plot against the
  Trojans)" is interpretation stated as fact (and `certa mori` says it outright): removed. The Latin Library variant
  `concitat aestus` "does not change the sense" overstated: now stated as "much the same picture".
- **32 (569–570) `n`.** "`semper` is Greenough's word order" (it is Virgil's) and "some readers have found it ironic" (unverifiable):
  now "Latin puts `semper` before `femina`" and the reader "may set it beside his `certa mori` (564)".
- **41 (581) `n`.** "puts the three words that mean 'all together' side by side": `idem` does not mean 'all together' (it is 'the same', with
  `ardor`). Rewritten.
- **46 (589–590) `i`.** "and had beaten her fair breast … and torn her golden hair" made the perfect participles `percussa … abscissa`
  coordinate with the previous finite verbs. Now "having struck her fair breast … and torn her golden hair".
- **47 (590–591) `n`.** "'hic ait' is the poet's 'she says' … with 'hic' as 'this man'": `hic` goes with `ibit` and `ait` is the parenthesis.
  Rewritten; also says the speech runs beyond this part.
- **54 (600–601) `n`.** "Dido, who has been compared with Medea since the night-piece at 522, speaks as her": unchecked. Now only
  "The picture recalls Medea …" (the myth of Absyrtus is certain).
- **55 (601–602) `n`.** "`epulandum` … agrees with the understood `eum`": it agrees with `Ascanium`. Corrected.
- **58 (604–606) `n`.** "which is the first plain statement of the plan": false (547 `morere`). Now "which says outright what she now wishes
  she had done." Contraction explained as dropping "-vi-" and "-is-" (`extinxissem`), not "-si-".
- **38 (576–577) `i`.** "holiest of the gods" for `sancte deorum` (a vocative with a partitive genitive, 'holy one among the gods', as the
  note says): now "holy one among the gods".
- **About (part summary).** "A woman, the god says, is always a fickle and changeable thing" is a distinctive, well-known English formulation: now "The god
  ends by saying that woman is always inconstant."

## Units: low
- 0 `i`: past tense for the Latin historic present (and "had a vast pyre raised") out of step with the next unit; now present.
- 1 `i`: "thunders out the names of three hundred gods" added "names"; now "calls in a voice of thunder on three hundred gods".
- 2 `n`: "set back to tell what was done before the rites began" (no basis) and "(by servants)" (not in the Latin): removed.
- 3 `l`: `amor` rendered "the love-charm" in the word-for-word layer; now "love" (note explains). 3 `i`: "sought too is the love-charm"
  reordered. 3 `n`: "Whoever got it first had a potion…" → "It was used in love-potions."
- 4 `i`: "sandal-strap" (the Latin says `vinclis`) and "altar" (`altaria`, plural): now "bindings", "altars". 4 `n`: "unshod … nothing may bind the
  worshipper" hedged ("usually taken as the dress of magic ritual").
- 5 `n`: "(he is leaving)", "not forgetting oaths", "the first of her prayers": removed (not in the Latin).
- 6 `n`: "split by the verb and the object" (only `soporem` stands between them). 6 `i`: "weary bodies … peaceful sleep" too near a
  remembered version; rebuilt ("tired creatures … the gentle quiet of sleep").
- 7 `n`: `lapsu` "ablative of manner or place" → "of attendant circumstance".
- 9 `i`: "Phoenician queen" for `Phoenissa` → "woman" (as `l`). 9 `n`: `animi` "genitive of respect" → "genitive (or old locative)".
- 10 `l`: "her cares" (no pronoun in Latin) → "cares". 10 `n`: `resurgens` "with `amor` as its subject" → "agreeing with `amor`".
- 13 `n`: `inrisa` "agrees with `ego` in `experiar`" → "with the 'I' of `experiar`".
- 14 `i`: "every last command" added "every" → "last commands"; "ships" → "fleet" (`classes`, as the note says).
- 15 `l`: "Is it that" for `Quiane` → "Is it because". 15 `n`: "some read `iuvat` as…" (unverifiable) → "could also be taken as".
- 17 `n`: "became a proverb" → "came to be a byword".
- 21 `n`: "which does not marry" → "which lives without marriage".
- 22 `n`: "This is her real grief" → "may be".
- 23 `n`: "`Tantos… suo` frames the line" → "`Tantos… questus`".
- 25 `n`: "`visa est monere` (Greenough prints `monere est` …)" misquoted the order; now "`visa… est` … is split by `monere`".
- 26 `i`: "like Mercury in everything — in voice and colouring, in golden hair" too close to a familiar version; rebuilt. 26 `n`: added that
  558 is hypermetric (its `-que` elides into `et`, 559).
- 27 `n`: "a regular address for Aeneas" → "how Mercury addresses Aeneas"; "as English cannot" (false: `i` does it) removed.
- 30 `i`: "Dawn finds you still lingering on this land" (common phrasing; `attigerit` is 'touches') → "Dawn's first light touches you still
  delaying in these lands".
- 31 `n`: "third and sharpest command" → "last and most urgent".
- 34 `n`: "of rousing a team" → "'harries, rouses'".
- 37 `i`: "A god sent down from high heaven … spurs us" too near a familiar version; rebuilt, keeping `missus` ("sent"). 37 `n`: "does not
  know it was him" → "who it was (`quisquis es`, 577)".
- 39 `i`: "across the sky" (`caelo` is 'in the sky') → "in the sky". 39 `n`: "the right hand side is lucky for Romans" (Roman
  augury favoured the left) → "'right-hand', hence 'favourable'".
- 40 `i`: "naked steel" (stock phrase) → "the drawn blade". 40 `n`: `stricto ferro` "ablative absolute or of means" → "of means".
- 41 `n`: "heavy with short syllables" → "full of short syllables".
- 44 `i`: "early Dawn, leaving the saffron bed of Tithonus, was scattering new light over the earth" followed a familiar version too closely;
  rebuilt.
- 45 `n`: `primam` "a variant of no importance" → "gives much the same picture ('the first light')".
- 47 `l`: "at our realm" → "realms" (`regnis`).
- 49 `n`: `tela` "at the end" (it stands mid-line).
- 50 `i`: "What madness is this that turns my mind?" near a remembered version → "What madness is altering my mind?"
- 52 `n`: "laying out the walls of Carthage (4.260 and following)": 4.260–261 is `fundantem arces ac tecta novantem`; now "founding
  its citadels and building new houses (4.260)".
- 53 `n`: `aiunt` "she does not believe the legend" → "may be bitter: she doubts".
- 54 `i`: "seized him, torn his body limb from limb" (stock phrase) → "carried him off, torn the body apart".
- 55 `n`: the banquets of Atreus and Tereus "is of" → "recalls".
- About: "her sister's pyre built" (Anna builds it for Dido) → "a pyre raised"; "watch-tower" → "watch-towers" (`speculis`).

## Refused findings (checked, left as they were)
- 569–570 house rendering `i` "Always a wavering, shifting creature is woman." against remembered versions (the stock "fickle and
  changeable thing" and the Dryden-style "various and changeful"): no phrase of any known version recurs; `l` "Changeable and fickle
  always a woman" is word for word. Kept; `new-renderings.md` unchanged and accurate.
- Citations verified against the source and kept: 4.24–29 (Sychaeus oath), 4.31 (Anna begins), 4.196 (Iarbas, `Iarban`; 4.36 `despectus
  Iarbas`), 4.222 and 4.265–276 (Mercury's first visit, speech 265–276), 4.260, 4.415 and 4.519 (`moritura`), 4.424 (`superbum`), 4.483–498
  (priestess), 4.494–497 (the pyre), 4.564 against 4.532 (`irarum fluctuat aestu`), I.94 (`terque quaterque`), 9.459–460 (same two lines
  as 584–585), 3.208 (same line as 583).
- Bracketed 528: printed inside `[ ]` in `t`, `l` and `i`; the note says it is Greenough's spurious line and what it supplies. Kept.
- 12 `n` (`quid ago` is indicative, the rest deliberative subjunctive): both true as stated. 13 `n` Greek-style accusative at 509/518/589:
  true. 1 `n` Hecate "three faces" and 17 `n` Laomedon's cheating of Apollo and Neptune: myth, certain.
- 0 `n` "ablative absolute" with `secta` agreeing with `ilice`; 21 `n` `expertem` with `vitam`; 27 `n` `quae … stent` indirect question; 30 `n`
  `attigerit` future perfect; 45 `n` `aequatis velis`: left (correct or properly hedged).
- 28 `i` "She is turning over schemes and a dreadful crime", 24, 29, 33, 35, 36, 42, 51, 56, 57, 58 `i`: close to the Latin, no distinctive
  echo that I could tie to a remembered version.
- Tense in `i`: kept as English past or present variously where the Latin has historic presents (40, 34), as in the earlier parts.

## Scansion
I read all 103 lines against the scanner's printout and checked every syllable's quantity against the word, not only the flagged
lines. Added to `scan-fixes.json` (appended after 4.503, ascending; no other entry touched):

- **4.504 (medium).** The scanner fitted `At rĕ-gĭ | nā pў-ră | …`: right shape, wrong vowels. It is `At rē | gī-nă pў | rā pĕ-nĕ | trā(li) in
  | sē-dĕ sŭb | au-ras` (`rēgīna`; `pyrā` ablative, the only reading that fits).
- **4.515 (low) and 4.559 (low).** Scanner correct; entered because each shares a unit with a line the scanner cannot fit (516, 558),
  and a unit with an unresolved line receives no `sc` (the 1.333 case).
- **4.516 (major, half-line).** UNRESOLVED. `et mā | trī prae | rēp-tŭs ă | mor×`, eight syllables, entered as a half-line (why starts
  "Half-line"; feet 1–4, one ×), like 4.44, 4.361, 4.400, 4.503.
- **4.526 (medium).** `quae-que lă | cūs lā | tē lĭ-quĭ | dōs quae | (que) ăs-pĕ-ră | dū-mis`: the scanner had `cus la te` long-short-short
  and `li qui` long-long, wrong for `lacūs`, `lātē` (as 1.21) and `liquidos`.
- **4.538 (major).** `Quiane`: the scanner read the `i` after `qu` as consonantal (the 4.433 `requiem` mistake), so `Quia` was one syllable
  and the line sixteen. It is `iūs-să sĕ | quar quĭ-ă | (ne) au-xĭ-lĭ | ō iŭ-văt | an-tĕ lĕ | vā-tos`.
- **4.542 (major).** Flagged COSTLY 3.5. `Lā-ŏ-mĕ | dōn-tē | ae sen | tīs per | iū-rĭ-ă | gen-tis`: `Laomedonteae` six syllables, `sentīs`
  long, `periuria` with the consonantal i after the prefix (`per-iū-ri-a`). The scanner ran `-teae` together and read `pe-ri-u-ri-a`.
- **4.549 (low).** Same quantities, different syllable division: `ob-ĭ-cĭs` (`ob` long by position before consonantal i), not an open long
  `o-`, which the audio would sing as ō.
- **4.554 (major).** `Aeneas` split A-e-ne-as by the scanner; it is Ae-nē-ās (as 4.466): `Ae-nē | ās cel | (sa) in pup | pi iam | cer-tŭs ĕ | ūn-di`.
- **4.558 (major).** UNRESOLVED: a hypermetric line (like 1.332, 1.448): `-que` of `coloremque` elides into `et` of 559; sixteen syllables
  count: `om-ni-ă | Mēr-cŭ-rĭ | ō sĭ-mĭ | līs vō | cēm-quĕ cŏ | lō-rĕm(que)`.
- **4.571 (major).** `Aeneas` again (cost 1.2): `Tum vē | Ae-nē | ās sŭ-bĭ | tis ex | ter-rĭ-tŭs | um-bris`, `vero` elided into `Ae-`.

Hand-scanned and found correct (scanner left): 4.505 `ilice`, 4.510 `Chaos` (Chă-ŏs), 4.511 `Hecaten`, `Dianae`, 4.513 `aënis` (ă-ē-nis),
4.518 `exūta` (`unum` elides), 4.524 `aequora`, 4.529 `Phoenissa`, 4.537 `Teucrum` (`Teu` one syllable, cost 1.5 only from the
synizesis options), 4.541 `nescīs heu`, 4.545 `Sidonia`, 4.547, 4.552 `Sychaeo`, 4.556 `redeuntis`/`eodem`, 4.562 `Zephyros`, 4.569
`Heia age` (Hē-j(a) ăge), 4.570, 4.585 `Tithoni`, 4.590 `Iuppiter`, 4.598 `aiunt` (ā-iunt), 4.599 `subiisse`, 4.604 `metui`. All lines with `eu`
(537 `Teucrum`, 554 `eundi`, 556 `redeuntis`; none is Greek `eu` except `Teucrum`), initial `Ae-` (520, 524, 532, 564, 574, 587, 599 correct;
554, 571 fixed) and consonantal `i` after a prefix or hiatus (538 `Quiane`, 542 `periuria`, 549 `obicis` fixed; 556, 569, 598, 599 correct) are covered.

Doubtful quantities, not changed:
- 4.520 `si quod` and 4.568 `si te his`: `si` must be long in the arsis (it is short by nature); no other fit.
- 4.526 `liquidos` as lĭquĭdus: inferred from the only fit that keeps `lātē` long.
- 4.558 `similis` with final -is lengthened at the pause (the only fit; hypermetric line).
- 4.556 `dei` as dĕ-ī and `redeuntis` as four syllables (rĕ-dĕ-ūn-tĭs); synizesis is possible but the scanner's reading fits at cost 0.6.
- 4.505 `ilice` with first i long and 4.504 `pyra` with short y: both forced by the metre; I could not confirm them from the Latin alone.
- 4.585 `Tithoni` with long Ti-, 4.511 `Dianae` with short Di-, 4.544 `Tyriis` with short Ty-, 4.552 `Sychaeo` with short Sy-: scanner readings, forced by the fit.

`draft.py` regenerated from `units.json`; `gloss.json`, `known-forms.json` and `novel-forms.json` untouched (no Latin and no form in `t`
changed). `new-renderings.md` untouched.
