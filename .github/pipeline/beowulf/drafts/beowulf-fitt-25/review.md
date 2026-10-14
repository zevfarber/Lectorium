# beowulf-fitt-25 — reviewer, pass 1

Only `l`, `i` and `n` were edited, in `units.json`, by script (json load, modify, dump with `ensure_ascii=False`, `indent=1`). `t`, `ln`, `v` and `p` are unchanged (checked by script, unit by unit, before the write). The file's one-space indent and key order are preserved. Read: conventions, packet, units, the source lines cited in the notes, the apparatus, `known-forms.json`, fitt 02 and fitt 24 (register and renderings), and a grep of every published part for the recurring renderings (Waldend, Metod, gāst, Scylding, duguð, cempa, cuma, hund missēra, lēan, Hrunting).

Counts: high 0 · medium 9 · low 17 · total 26 changes.

## Pass 1

Lines are the unit's starting line.

| Line | Field | Sev. | What was wrong | What was done |
|---|---|---|---|---|
| 1745 | l | medium | `l` “crooked wonder-commands”, but the note reads ‘wōm’ as “wicked” (stain, sin) and says so; `i` has “wicked”. `l` contradicted its own note. | `l` now “the wicked wonder-commands”. |
| 1748 | l | medium | “what he has long held” renders `hēold` (preterite) as a perfect. | “what he long held”. |
| 1758 | i | medium | “choose the better part, the lasting benefits” is a remembered phrase (a well-known rendering of this passage, and “the better part” is a stock English idiom) rather than built from `þæt sēlre gecēos, ēce rǣdas`. | “choose what is better, the lasting gains” (`rǣd` “advantage, benefit”, as the note says). |
| 1774 | i | medium | “For all that, a reversal came upon me” — in English “for all that” means “despite that”, the opposite of `mē þæs … cwōm` (“to me for that came”). | “Because of that, a reversal came upon me”. |
| 1783 | n | medium | The note said Kock's ‘gemǣne’ “would leave the treasures ‘shared’ without the genitive”. The apparatus gives only “Kock gemǣne”; the consequence was invented and is not even clear grammar. | Now “the apparatus records Kock's ‘gemǣne’ in place of ‘gemǣnra’.” |
| 1789 | n | medium | Quoted ‘heofones helm’ “helm of the heavens”. The poem has `heofena Helm` (182), which fitt 02 renders “the heavens' Helm”; the quoted form does not occur. | Now cites ‘heofena Helm’ at 182 and the night-covering ‘scaduhelma’ (650). |
| 1792 | n | medium | “Ettmüller ‘ungimetes’”. The apparatus gives “E.”; in this edition `E.Sc.` is Ettmüller and `E.` (cf. “Earle 117”, 253a) is Earle. | “Earle (the apparatus ‘E.’)”. |
| 1809 | n | medium | Called ‘tealde’ a “past subjunctive”. The weak past singular has one form for indicative and subjunctive; the form cannot show mood. | Now says the form has one shape for both and the mood cannot be told from it. |
| 1812 | n | medium | “Beowulf … is the nearest man”. The man named just before is Unferth (`gūðwine`), so “nearest” is false. | “The poet does not say whom he means. I take Beowulf … though Unferth, named just before, is also possible.” |
| 1740 | l | low | “a portion of over-thoughts”; the same word `dǣl` is “share” at 1752 and in the note. | “a share of over-thoughts”. |
| 1745 | n | low | “armour does not stop the arrow”: assert-by-negation, and it goes beyond the text (`under helm`). | “the arrow goes in beneath the helmet”. |
| 1745 | n | low | The dot-under-vowel was explained in three sentences. | One sentence: the sign, that the vowel does not count in the metre, and where it recurs (1782, 1797). |
| 1748 | n | low | “read from Thorkelin's transcripts A and B”. The apparatus says only “Fol. 168b waldend AB” (a leaf marker with sigla); “read from” claims more than it shows. | “The apparatus marks the start of a new manuscript leaf (fol. 168b) at ‘waldend’, citing the Thorkelin transcripts A and B.” |
| 1755 | i | low | “the dead earl's old hoard” adds “dead”, which is not in `eorles`. | “the earl's old hoard”. |
| 1774 | l | low | “in my homeland” for `on ēþle`; the note has “in the homeland”. | “in the homeland”. |
| 1778 | n | low | `sig` called a form of ‘bēon’. The subjunctive `sīe/sig` belongs to ‘wesan’ (`known-forms`: `is` is ‘wesan’; ‘bēon’ is used for `bið`). | “subjunctive of ‘wesan’, ‘be’”. |
| 1790 | n | low | “The text does not name him … no one else is in question”: negation where the identification can be stated. | “He is Hrothgar, who spoke the last lines and was called ‘se snottra’ at 1786.” |
| 1794 | l | low | “sea-warriors” for `heaþolīðende`; the note analyses it as `heaþo` + `līðende` (“battle-farers”), so `l` dropped ‘battle’. | `l` “battle-sailers”. |
| 1794 | n | low | “battle-farers” (not matching the `līðende` gloss “sailing”). | Note matched to `l`: “battle-sailers”. |
| 1799 (`reced`) | i | low | “towered above him” — “above him” is not in the Old English. | “the hall towered, broad and bright with gold”. |
| 1799 (`reced`) | n | low | Closer “The line gives the building that surrounds the sleeping Geat.” is filler. | Removed. |
| 1802 | n | low | “‘cōmon … gongan’ at 1642”. `cōmon` is in 1640 and `gongan` in 1642. | “at 1640–1642”. |
| 1802 | n | low | “read from B” (same overstatement as 1748; the apparatus has “Fol. 169b ða com B.”). | “The apparatus marks the start of a new manuscript leaf (fol. 169b) at ‘ða com’, citing the Thorkelin transcript B.” |
| 1807 | n | low | “Unferth, as at 499”. Line 499 has `Ecglāfes bearn`, not `sunu`. | “(‘Ecglāfes bearn’ at 499)”. |
| 1809 | n | low | “‘lēan’ … the word of 1692”. 1692 has the compound `endelēan`; the simple word is at 1584. | “the word of 1584 (and of ‘endelēan’ at 1692)”. |
| 1814 | n | low | ‘hæle’ called “a form of ‘hæleð’” with no case. The argument that Beowulf is the greeter needs it to be nominative (`known-forms`: nominative singular). | “a nominative singular variant of ‘hæleð’”. |

## Considered and refused

- 1792–93 subject. `Gēat` (nominative, half-line standing alone) and `rōfne randwigan` (accusative with impersonal `lyste`) are the same man; the note says so and states that it is a reading. `l`/`i` agree with it. Kept.
- 1794–98 subjects. `seleþegn` is subject of `wīsade`; `sē` is the same man; `heaþolīðende` is the subject of `habban scoldon`; `him … wērgum … feorrancundum` are the datives. Checked, correct.
- 1807–08 subjects. `se hearda` is Beowulf (cf. 401, `swā him se hearda bebēad`); `sunu Ecglāfes` is Unferth, read as the one to whom Hrunting goes; `his sweord` is Unferth's. The note says the construction is loose and the reading is its own. `sunu` as dative in sense is in `known-forms`. Kept.
- 1816 subject. Beowulf as greeter, with `hæle hildedēor` nominative and `Hrōðgār` object, is the reading in the note, supported by 1644–46. Hrothgar as subject is possible grammatically; the note states the choice. Kept.
- 1745–47 construction. `Þonne bið … drepen … biteran strǣle … wōm wundọrbebodum wergan gāstes` — passive with an unstated subject (the man), instrumental dative of the arrow, and the commands of the spirit: matches `l`. `him … ne con` is a parenthesis (reflexive dative with `bebeorgan`). Kept.
- 1748–52 subjects. `þinceð` takes the `þæt` clause as subject; `gȳtsað`, `seleð`, `forgyteð`, `forgȳmeð` all have `hē`. The two readings of `þæs þe` are both set out in the note; `l` and `i` follow the causal one the note says it follows. Kept.
- 1760 `oferhȳda`: genitive plural with `gȳman`, as the note says (cf. 1757). Kept.
- 1762–68 list. One singular verb with a string of `oððe` subjects; `þec`/`ðec` are the accusative, `eafoþes` the genitive after `getwǣfeð`. `l` “will part”/“will overpower” render present forms in a future context after `bið` “will be”; the note says `bið` is a present used for the future. Kept.
- 1759 `secg[a]` “best of men”: the genitive plural is a conjectural emendation and the note gives the apparatus. Kept.
- 1803 `scaþan` “warriors” in `l`: not word by word (the lexica give “foe, ravager”), but the note says plainly it is a guess from context. Kept; the owner may prefer a transparent `l`.
- 1805 `collenferhð` “swollen-minded”: the note says the root is uncertain, so the literal part is also a guess. Kept.
- 1809 `i` “thanked him for the kindness” for `þæs lēanes`: an interpretive rendering of “reward, requital” of a lent sword; the note gives the range, including Müllenhoff's `lǣnes`. Kept.
- 1794 `ealle … þearfe`, `andrysnum` “courtesies”: lexical, no better reading found. Kept.
- 1774 `Hwæt` “What!”/“Listen!” and `Metode` “Measurer”/“God”, `Waldend` “Wielder”/“Ruler”, `hund missēra` “half-years”/“seasons”, `cempa` “champion”, `cuma`, `Hrunting`, `Scylding`: all agree with the published parts (checked by grep).
- 1745 `gāst` “ghast” in `l` and “spirit” in `i`: the same pair as fitt 02 (129), 12 (805) and 23 (1620). Kept.
- 1752/1777/1802 leaf notes: apart from the softening above, the abbreviation `AB` cannot be checked against anything but the packet; the notes match it.
- 1748 `fǣtte` and the manuscript's `fædde`: the note follows the apparatus and flags the sense as partly a guess. Kept.
- 1769 “a hundred half-years”, fifty or a hundred: the note states the uncertainty. Kept.
- Remembered English in `i`: apart from 1758, nothing found that is a known phrase from a translation. “Take no heed of pride”, “a reversal came upon me” (a gloss of `edwenden` in the lexica), “thanks be to God”, “the helm of night grew dark”, “went to the high seat”, “a man of spirit” are built from the glosses.
- Plain notes: “the text does not say” at 1755 and “is a guess” at several lines state uncertainty about a reading; they are not assert-by-negation and were kept.

Counts: high 0 · medium 9 · low 17 · total 26.

# beowulf-fitt-25 — reviewer, pass 2

`units.json` edited by script only (`l`, `i`, `n`; `t`, `ln`, `v`, `p` checked unchanged unit by unit). `gloss.json` fixed in place by script. After the fixes: novel keys equal `novel-forms.json` exactly; every `__broaden__` entry begins with the shared glossary's old text verbatim followed by ` · `. Citations in the notes (lines 75, 81, 82, 116, 133, 147, 182, 183, 280, 308, 401, 499, 650, 751, 1216, 1455, 1475, 1498, 1584, 1640–42, 1646, 1658, 1659, 1674, 1692, 1703, 1707, 1719, 1720, 1786) were checked against `source/beowulf-klaeber1922.json`; all are right.

## Text changes

| Line / form | Field | Sev. | What was wrong | What was done |
|---|---|---|---|---|
| 1792 `unigmetes` | n | medium | Pass 1 asserted “Earle (the apparatus ‘E.’)”. The packet's apparatus gives only “E. ungimetes” and does not name the scholar; the identification rests on the whole-poem apparatus, which the packet does not carry. | Now says the reading is given under the siglum ‘E.’ and “I take that to be Earle, but the packet does not spell it out”. The identification is plausible (the full source apparatus uses ‘E.’ beside “Cf. Earle 117”) but unproven. |
| 1748 `waldend` | n | low | Pass 1's “citing the Thorkelin transcripts A and B” states what ‘AB’ stand for; the packet does not. | “citing the sigla ‘AB’ (I take these to be the two Thorkelin transcripts)”. |
| 1802 `ða com` | n | low | Same, for ‘B’. | “citing the siglum ‘B’ (I take this to be a Thorkelin transcript)”. |
| 1796 `beweotede` | n | low | “Grundtvig's translation”: the packet has only “Gru. tr.”, so “translation” is a guess at the abbreviation. | “credits ‘beweotede’ to Kemble and to Grundtvig (‘Gru. tr.’)”. |
| 1760 `gȳm` | n | low | “taking the genitive as at 1757”: `egesan` at 1757 is a weak form that may be genitive or accusative singular, so “as at” was not true; it also clashed with the 1755 note (“genitive or accusative”). | “here with a genitive (at 1757 ‘egesan’ may be a genitive or an accusative)”. |
| 1807 `Hrunting beran` | i | low | “the stern hero” adds “hero” (OE `se hearda`); “take back his sword” adds “back” (OE `niman`, and `l` has “take his sword”). | “the stern man”; “take his sword”. |
| 1741 `weard` | n | low | “The text gives the guardian no other name.” Negation filler. | Sentence removed. |
| 1742 `bona` | n | low | “The slayer is not named here; … shows that I should take him”: negation, and “shows” overstates an inference. | “‘wergan gāstes’ in 1747 suggests that the slayer is the accursed spirit, the devil; that reading is mine.” |
| 1769 `middangeard` | n | low | “as at 75 and 751”: at 751 the form is the genitive `middangeardes`. | “as at 75 and, in the genitive, 751”. |
| 1785 `snottra` | n | low | “Hrothgar's last words were ‘Gā nū tō setle’”: that phrase opens his closing command (1782), it is not his last words. | “Hrothgar's command at 1782 was …”. |

Counts, text: high 0 · medium 1 · low 9 · total 10.

## Gloss changes

| Key | Field | Sev. | What was wrong | What was done |
|---|---|---|---|---|
| `lōg` | entry | high | Lemma `lēogan` “lied, belied” (strong II). The preterite of `lēogan` is `lēag`; `lōg` is the preterite of `lēan` “blame” (strong VI), as the unit's note says, and `l`/`i` have “found fault”. Lemma, meaning and class all wrong. | `lēan — blamed, found fault with (3rd singular preterite, strong verb VI; takes the dative; wordum lōg …)`. |
| `wōm` | entry | medium | A novel key carried two readings joined by ` · ` (that form is for `__broaden__` only), one of them “crooked” (that is `wōh`, not `wōm`), plus a line-bound remark (“in apposition to the arrow and its source”). | One entry: noun “stain, sin, wickedness”, also taken as a qualifier “wicked, foul”, form and sense uncertain. |
| `egesan` | entry | medium | “accusative plural”; the word is a singular (terror) in its line and the unit note reads it so. | “accusative singular, or genitive singular; gȳman takes either case”. |
| `þearfe` (broaden) | new reading | low | “accusative plural … ‘a thane's needs’”: number cannot be fixed (`ealle … þearfe`; the unit renders a singular). | “accusative, singular or plural”; gloss “a thane's need”. Old text untouched. |
| `forsiteð` | entry | low | “takes the accusative” (no object in its clause) and “dims” (sense of the sister verb, not of `forsittan`). | “obstructs, hinders”; dropped the case remark. |
| `scaþan` | entry | low | Gave only “warrior, marauder”, dropping the lexical sense “foe, ravager” and presenting the guess as the meaning. | “foe, marauder, ravager; of armed men, warrior … the sense warrior is a guess from context”. |
| `andrysnum` | entry | low | Lemma `andrysnu` and parse “neuter plural, dative plural” (redundant, and the lemma is the plural). | Lemma `andrysne`; “neuter, dative plural”. |
| `gæst` | entry | low | “a variant spelling of gæst/gīest” cites the form as its own variant. | “a variant spelling of gest, gīest”. |
| `gȳtsað` | entry | low | “cf. ‘yet’ in the sense of craving”: false etymology (`gīet` “yet” is another word). | “from gīetsung ‘greed’”. |
| `lēanes` | entry | low | “cf. ‘lean’ in ‘guerdon’”: `guerdon` is French, not a relative. | Cognate remark removed; “reward, requital”. |
| `strǣle` | entry | low | “cf. ‘strāl’”: a bare foreign form with no gloss. | Removed. |

Counts, gloss: high 1 · medium 2 · low 8 · total 11.

## Considered and refused

- Pass 1 edits (the 26 listed above): re-read each; none introduced an error apart from the over-statements fixed above. The `sig` correction (‘wesan’) is kept; `sīe/sig` is accepted under either ‘wesan’ or ‘bēon’ in the lexica, so the gloss `sig → wesan` and the note agree.
- `beweotede` gloss lemma `bewitian` against the note's ‘beweotian’: spelling variants of one verb; left.
- `biteran` (weak dative feminine) and `nīowan` (weak dative feminine) without a determiner: unusual in strict grammar but the forms are what is printed; left.
- `collenferhð`, `rūmheort` glosses differing in wording from `l`: the units' notes call these guesses; the glosses give the lexical range. Left.
- `ingenga` / `ealdgewinna` “in apposition to Grendel/a name”: they are predicate nominatives after `wearð`; close enough for a glossary remark. Left.
- `lǣne` nominative singular masculine vs possible weak form: no difference in this ending. Left.
- 1809 note “Beowulf blames neither the man nor the blade”: a statement of what the sentence says, with the cause given; not assert-by-negation. Left.
- 1803 `scaþan` “here it must be said of the Geats”: the note already calls the sense a guess. Left.
- Remembered phrasing in `i`: none found beyond what pass 1 changed.
