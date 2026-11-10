# aeneid-039 (V.779-871) review, two passes

Severity counts: **major 38, medium 14, low 15** (67 changes: 49 to units.json, 18 to scan-fixes.json).
Text (l / i / n / about / cut points): major 21, medium 13, low 15. Scansion: major 17, medium 1.

Build: `python3 build_aeneid.py aeneid-039` passes the tiling and scansion stages (18 hand scansions applied, nothing UNRESOLVED, every line checked against the validator's foot rules by a separate script) and then stops only because `gloss.json` does not exist yet. Nothing was written to the manifest; the full build was NOT run to completion.
`units.json` was edited by script (`t` untouched; the units joined still reproduce the edition character for character; l line count equals t; i single-line; speech marks matched in t, l and i). One structural change: units 5.850 and 5.869 were merged with their neighbours (see below), so there are now **60 units**, not 62. `make_units.py` was regenerated from the final `units.json` and reproduces it exactly (checked), so it is not stale this time.

## Scansion (18 entries added to scan-fixes.json; the scanner knows no vowel quantities, so cost 0.0 does not mean right)

I checked every line's syllable quantities against the natural quantities, not only the lines packet.md flags. Where a line has no fit with all natural quantities, the entry says which one licence it takes.

Major (17):
- 5.792 and 5.815: Virgil's hemistichs (scanner UNRESOLVED); entered as half-lines (792: in reg | nis hoc | au-sa tu | is; 815: u-num | pro mul | tis da-bi | tur ca-put).
- 5.804, 5.809, 5.827, 5.850: Aeneae / Aenean split as A-e by the scanner (the recurring Ae- blind spot); now Ae one syllable, -nē- long (as in the published parts).
- 5.811 periurae: i consonantal after the prefix (per-iu-rae, per long by position); scanner read pe-ri-u-rae.
- 5.800 (flagged COSTLY 2.1): Cytherea with its usual ŭ ŭ - ŭ, meis two syllables; the only one-licence fit lengthens te (see doubtful).
- 5.826 (COSTLY 1.2): Nisaee / Spio / Thalia / Cymodoce had short Spi-o, Tha-li and long -que, -a; natural quantities (Nēsaeē, Spīō, Thălīa, Cȳmodŏcē) fit.
- 5.831: solvēre, sinūs, ūna: scanner had re, si, u long and nus short.
- 5.843: Palinure keeps short Pa-li- as everywhere else; scanner lengthened both (Iaside then all long; see doubtful).
- 5.849: huic one long syllable and Mē long (Mene + elided -ne); scanner read Me short and huic as two syllables.
- 5.853: amittēbat / tenēbat long -ē-, oculos ŏ-cŭ-lōs; scanner had te short and o, cu long (needs bat lengthened at the caesura; see doubtful).
- 5.857: quies two syllables (qui-es, as in quiete in this part); scanner read it as one and lengthened -na.
- 5.864: adeo ă-dĕ-ō; scanner had a long, de short.
- 5.869: cāsū, ănimum; scanner had ca, su short and a, ni long.
- 5.871: ignotā ablative (long -ta), Palinure short Pa-li-; scanner had the reverse.
Medium (1): 5.787 reliquias four syllables (re-li-qui-as, as 1.30); scanner's three-syllable synizesis fitted but misses the word.

Checked by hand and left as the scanner has them: 5.779-786, 788, 790 (excierit with short -ci-, the only fit), 791 (Aeoliis, ne- long in nequiquam as in published parts), 793-799, 801-803 (Simoëntaque: o and ë separate, Si-mŏ-ĕn-ta-que), 805-808, 810, 812-814, 816-825 (825 Thetis / Melite / Panopeaque: the scanner's reading is the natural one despite COSTLY 2.6), 828-830, 832-842, 844-848, 851-852, 854-856, 858-863, 865-868, 870. Lines with Greek eu: none. Hiatus: none needed (all elisions across -m / vowel: omne est, Neptunum exercita, tantum amissum, vasto aethere, etc.); exanimata (805) is ex-a-ni-ma-ta as the scanner has it; aëra (839) a-ĕ-ra as published precedent; huic fixed above; Inousque, Iaside, Cymodoceque, Nisaee see above and doubtful.
Also confirmed: -que after a final consonant makes position (marisque 802, manibusque 818, pariterque 830, multorumque 865), so ris, bus, ter, rum long there are right.

Doubtful quantities (unconfirmed against an edition; the line fits only with these):
- 5.789 nuper with long nu- and long final -hi in mihi (the scanner's only fit; L&S has nŭper).
- 5.800 te long in the fourth foot (is te | fi-de-re); every other fit costs more.
- 5.801 ducis with -cis lengthened at the penthemimeral caesura.
- 5.823 chorus / Inous: fit needs chorus-rus long and I-no short, us long.
- 5.835 fere with long -re (adverb ferē).
- 5.843 Iaside all long (Ia-, -si-, -dē), the one way to keep Pa-li- short.
- 5.853 bat of amittebat lengthened at the caesura.
- 5.797 tibi with long -bi (as in the published parts).

## Notes / l / i / about (changes by unit, line cited)

Major (21):
- 781-782: n said exsaturabile means "that cannot be sated" (it is "that can be sated"; nec negates it); l/i now show "not to be sated"; i "savage" -> "grievous".
- 783-784 (flagged quam/infracta): n asserted Juno as antecedent and subject of quiescit; the Latin gives either Juno or her ira; restated; l "nor any softens" mis-attached ulla.
- 785-786: n read "poenam traxe per omnem" as "drawn out the punishment" (it is per omnem poenam, with an unexpressed object "them"); l moved "Not enough it is" onto the wrong line.
- 790-792: l lines misaligned ("in your" on the wrong line, "she" stranded); n "deponent audeo" (it is semi-deponent).
- 793-795 (flagged socios linquere ignotae terrae): n made socios the object of subegit while i read it as the men left behind, with "some of" invented; now subegit has an unexpressed object (Aeneas), socios is the object of linquere, ignotae terrae a dative; l shows "(him)".
- 796-797 (flagged dare vela tibi): i made tibi into "your waves"; tibi is Neptune, to whose care the sails are entrusted (vela dare also noted as the idiom for setting sail); l's line division realigned.
- 803-804: n called "Aeneae tui" a possessive genitive (objective genitive after cura); Greek accusatives Xanthum / Simoënta noted; l "of your son" supplied "son".
- 806-808: n glossed daret "would give" (imperfect subjunctive after cum = "was giving") and called the plural amnes "the river"; l reordered.
- 808-810: l "to the Peleian's strong one" for Pelidae forti ("to the strong son of Peleus"); n Iliad claim "Aeneas has no gods" softened (Apollo had urged him).
- 813: l/i "as you wish/desire" made quos optas adverbial; it is the relative clause on portus; subject (Aeneas) named.
- 816-818: l "when she had soothed" (Neptune is the subject); l "spuming".
- 819: n "summa a neuter plural adjective used as a noun" (it agrees with aequora); l restructured.
- 848-849: n labelled "Mene... ignorare iubes?" an accusative and infinitive of indignation; it is ordinary iubeo + acc. + inf. in a question; the indignant infinitive is the next question (849), now labelled there; 849's note had a duplicated sentence and the unsupported "the real monster is the god".
- 850-851 (print misprint, see below): n garbled ("the sea as the thing entrusted", "credam understood" when credam is expressed); Latin Library "caeli" guess removed.
- 852-853: n called clavum an accusative after affixus (it is the object of amittebat; affixus et haerens are nominatives); l "his eyes... was holding".
- 854: n "Stygia for the Styx" (the adjective agreeing with vi).
- 830 (flagged fecere pedem): n gave "to haul the sheet taut" as fact; the sense of pedem facere is not settled; now said so, with sinistros... dextros... sinus explained; i hedged.
- 831: n "a double -que" for torquent detorquentque (one -que); i "round and round" wrong for torquent / detorquent.
- 871: n "the last word of the book's action" (harena is last); "nudus... unclothed/unburied" hedged; i rephrased (see echoes).
- 850-851 / 869-870 merges are listed under low.

Medium (13): 779-780 n (Latin Library line is the same line Greenough prints at 777, set before "At Venus"; "spurious repeat" unsupported); 787-788 n/l/i (peremptae agrees with Troiae, cineres atque ossa in apposition; i "already... still" unsupported); 788 n ("The line stands in the middle of its line" nonsense) and i ("let her tell" invented); 802 n (caelique marisque is a double -que, not "one word each side"; l "furies"); 820 n/l/i (aquis "ablative of agent or cause" stated as certain; debated; l "is spread flat sea" garbled); 825 n (Thetis is not in Homer's Nereid catalogue, Il. 18.39ff; restated); 827 l ("mind" twice for one mentem) and n trailing space; 835 l (turning-post on the wrong line) and n (V.738 cross-reference made specific: "Nox humida torquet medios cursus"); 836 n (pointer to a note "in the last part" removed; the iamque... cum pattern explained in place); 841 n (flagged Phorbas: "not otherwise heard of" unverifiable, now "the poem tells nothing more of him here"; "in high" dangling in l); 857 l/i (primos agrees with artus, not quies); 815 n/i (the "old idea that a god's favour must be paid for with a victim" removed as unsupported; i "one life will be given for many" rephrased as a close echo); 870 l (sereno agrees with caelo et pelago; it is not what is trusted).

Low (15): about ("ready to leave Sicily" contradicts 777-778); 789 i tense; 804 n Iliad "from the field"; 814 n ("you" = Venus); 821 n (aethere separation or place); 822 n (verbless list; senior "aged"); 832 n (sua refers back to the fleet); 834 n (ad hunc... contendere); 840-842 l ("bear themselves" read as a reflexive); 858-860 n (object of proiecit, agreement of praecipitem); 867 n (cross-reference "see 837" -> 838; fluitantem errare simplified); 869 l ("of his friend" dangling); 862 n (iter tutum an internal accusative, not "of extent"); two merges: **850-851** (the print has no mark after "credam", so the unit would not end at punctuation, and the build refuses; the unit is merged with the second half of the question) and **869-870** (no mark after "amici"; merged with the speech's first line, which ends in a comma).

Echoes of known English rephrased (low, counted above): 815 "one life will be given for many"; 871 "naked on an unknown shore" (now "bare on sand you do not know"); 870 "trusted too much in a calm sky and sea" (now "put too much faith in a serene sky and sea").

## Facts verified or softened

- Homeric parallels: Il. 21 (Xanthus choked, rising against Achilles), Il. 20 (Poseidon saves Aeneas in a mist), Il. 21.441ff (Laomedon cheats Poseidon), Il. 13.23ff (Poseidon's drive), Il. 14.231ff and 286ff (Hypnos and Hera; Hypnos as a bird), Il. 18.39ff (Nereid catalogue), Od. 12 (Sirens): kept; the Il. 20 wording "Aeneas has no gods" softened and Thetis removed from the Nereid list. Nothing was cited that I could not stand behind.
- Cross-references checked: V.604ff (Iris and the women), V.746ff (men left in Sicily), I.124ff (Neptune calms the storm), I.142ff, V.738 (Anchises: "Nox humida torquet medios cursus"), VI.337ff (Palinurus's shade) — all confirmed. Palinurus appears in Book III. Book V ends at 871.
- Speech marks, all present and matched in t, l and i: 781 opens / 798 closes (unit 10); 800 opens / 815 closes; 843 opens / 846 closes; 848 opens / 851 closes (now at the end of the merged 850-851 unit); 870 opens (now mid-unit in the merged 869-870 unit, after the line break) / 871 closes.
- 5.850 and 5.869 (README rule 5b): t kept as printed (the print has no mark after "credam" and none after "amici"); each note opens with the print's reading ("The print has 'credam quid enim' with no marks, where the sense needs '(quid enim?)'"; "The print has 'amici' with no mark after it, where a colon belongs"). Per rule 5b these two spots also belong in QUESTIONS.md with the correction and the place; **not touched here, to be added by the run's owner**.
- Hemistichs 792 and 815: both are Virgil's unfinished lines; Greenough prints them short; both noted in the units and entered in scan-fixes as half-lines.
- Latin Library: the 779 variant is the same line as Greenough's 777 in a different place (noted); the others in range are orthographic or morphological (omnes/omnis, puppes/puppis, tenent/tenet, brachia/bracchia, humida/umida, voltum/uultum, affixus/adfixus, revolsa/reuulsa, tenues/tenuis, secius/setius, difficiles/difficilis), and the existing notes that mention them are left, except 851 where caelo/caeli does touch the sense and is stated as a plain difference.

## Refused / not changed

- Adding the missing "?" / ":" to the source (rule 5): the instruction for this run is t as printed; merged units instead.
- 804 Troia: scanner's Tro-i-a (a elided before Achilles) is the only fit; kept.
- 791, 797, 799 (Sā-), 802, 823, 835: scanner's fits kept as the only fits (see doubtful), no scan-fixes entry needed.
- 844 "dative of purpose" for quieti: kept (dative of the thing for which; either label is defensible).
- 819 / 835 "caeruleo... curru" framing, "meta" picture of the games: kept.
- 799 Saturnius, 812, 813 (accedet + accusative), 838-839 (inverted cum, Hypnos), 855-856, 861, 862 (promissis), 864-866 (Sirens off the Campanian coast), 870: labels checked true of this form in this line; no change beyond what is listed.
- No house renderings in range; no glossary work (gloss.json not yet made); `new-renderings.md` left as drafted.
