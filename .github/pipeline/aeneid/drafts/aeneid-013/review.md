# aeneid-013 review (Aeneid II.386-485), two passes

Findings: **major 3, medium 20, low 9**. Changes made by script to `units.json` (16 fields in 14 units plus `about`; `t`, `ln`, `p`, `v` and the `l`/`i` line counts untouched, checked against the original) and 15 entries added to `scan-fixes.json`. Speech marks checked: the opening mark is at 387, the closing mark follows "ipsi." at 391 (the speech does end there; the rest is Aeneas's narration, Greenough prints no other marks); `l` and `i` of u0 open it, `l` and `i` of u1 close it, u2 carries it only in `t`. Balanced.

## Changes to units.json
Major
1. u44 (471-475) n: "A simile with no main verb" is false; the snake has its own verbs, `convolvit` and `micat`. Reworded.
2. u7 (400-401) n: "'ingentem' stands at the end of the line before its noun" is false (it is mid-line 400); now "held apart from 'equum' (next line) by 'formidine turpi'".
3. u46 (479) n: "A new paragraph begins at 479" is unsupported. The packet marks paragraphs at 386, 402, 410, 438, 453, 469 only, and `source/aeneid-greenough.json` has `p` at 469 and 486 and not at 479; the unit has no `p` flag. Claim removed (replaced by "'ipse' is Pyrrhus").

Medium
4. u11 (407) n: "Coroebus was warned by Cassandra and ignored her" is not in the Latin and cannot be verified here. Removed.
5. u15 (417-418) l: third line "horses Eurus;" reversed the Latin order (Eurus equis). Now "Eurus with horses;".
6. u18 (422) n: 'primi' called "used as an adverb"; it is a nominative plural agreeing with the subject, rendered as an adverb. Fixed.
7. u24 (429-430) n: 'tua plurima... pietas' said to have 'te... labentem' "framed between"; the words interleave (te | tua plurima | Panthu | labentem | pietas). Fixed.
8. u33 (448) n: "'-que' links the 'auratas trabes' to the object of 'convellunt'" was muddled; 'trabes' is the object of 'devolvunt'. Fixed.
9. About: "for against an enemy who asks whether it is cunning or courage?" was garbled; now "for who, against an enemy, asks whether it is cunning or courage?".
10-23. Fourteen scan-fixes entries where the scanner's fit is a valid hexameter with wrong quantities or syllable counts (listed below): 389, 394, 398, 408, 419, 421, 426, 427, 433, 439, 462, 466, 468, 477.

Low
24. u0 n: 'prima' "predicative" softened to "agrees with 'fortuna', best rendered as an adverb".
25. u1 i: "The enemy himself" (number clashed with plural 'ipsi') to "The Greeks themselves will furnish the arms." n: unverifiable "the arms are what the dead Greeks leave behind" removed.
26. u7 n: tail clause about the horse being mentioned "because the Greeks go back where they began" cut (interpretation, no support).
27. u9 l: 'passis' had slipped from line 1 to line 2; now "with loosened, Priam's maiden, / locks, from the temple," (Latin line division kept).
28. u22 i: "The gods thought otherwise" is a stock rendering; now "The gods saw it another way".
29. u32 l: "with these, themselves," punctuation (his se).
30. u42 n: "one of the incomplete lines Virgil left in the poem" now says it is a half-line that Greenough prints short. Checked: 2.468 is one of Virgil's recognised hemistichs; "The paragraph ends here" is true (next paragraph 469).
31. u44 n: 'pastus' called a participle of "the deponent 'pascor'"; it is the passive of 'pasco' with middle sense. Fixed.
32. scan-fixes 2.444 (syllabification only; see below).

## Checked and left
- Homer / scholia / other cites: none present (the one outside claim, Cassandra's warning, removed as above). Antecedent claims about Androgeos (2.371) and Panthus the priest of Apollo (2.319) are true to the poem.
- Notes on spelling variants: 'apparent' 422 (both texts), 'Adparet' 483, 'adparent' 484, 'Achaia'/'Achaica' 462: accurate.
- 'i' lines checked for echoes of known English versions; only u22 was rephrased. The `l` word order, `l`/`i` agreement and line counts hold for every unit.
- Every grammatical label in every note read against the form in the line; those not listed above are true.

## Scansion
Hand-scanned all 100 lines (quantities of every syllable, not only the flagged ones). Scanner right, no entry: 2.417 (Zephyrusque Notusque et laetus Eois: con-fli | gunt Ze-phy | rus-que No | tus-que et | lae-tus E | o-is; E- must be short here, the only fit, though 1.489 Eoas has long E-), 2.418 Eurus (Eu is one syllable), 2.459 Teucri, 2.402 Heu nihil (no hiatus; Heu one syllable, nihil short-short), 2.403 Priameia, 2.428 Hypanisque Dymasque (no hiatus), 2.414 Aiax (a- long in acerrimus, A-iax).
Entries added (all validated against the validator's rules: letters of `sc` = words of the line, six feet / one x, foot patterns, half-line branch for 468):
- 2.389, 398, 433, 462, 466: Danaum is Da-na-um (3 syllables); scanner took Da-naum with a long Da- (the known blind spot).
- 2.394, 426: Greek -eus in Rhipeus, one syllable (Rhi-peus), as the existing 2.339; 2.427 Teucris likewise; 2.419 Nereus likewise (Ne-reus).
- 2.408: iniecit, consonantal i (in-jē-cit).
- 2.421: tota (abl., both long) and agitavimus (a-gi short) had wrong quantities. 2.439: tota long-long and morerentur mo-re short, short. 2.477: Automedon is Au-to-me-don (to, me short, don long) and una has long u.
- 2.444 obiciunt: quantities right, syllable division only (cf. 2.200).
- 2.468 (Half-line): tē-lō(rum) | in-te-re | ā ces | sat ge-nus. Only parse; needs the final -a of interea long and sat lengthened in arsis.

## Refused / left, with doubt
- 2.447 (extrema iam in morte): scanner's parse (ma long, iam elided into in) is the only fit I found by brute force, but I cannot confirm the treatment of 'iam' (consonantal j vs vowel). Left.
- 2.449 (imas): the fit needs the i of 'imas' long (and mucronibus mu- long); same demand at 1.84 sedibus imis. Left.
- 2.433, 2.419: both fits need one lengthened syllable (si before fata; i of imo). Entries keep the scanner's choice there; flag for the owner.
- 2.339/2.394/2.426 rest on Rhi- being long (the 2.339 caveat stands).
- 2.442 (parietibus, scanner cost 1.5), 2.455, 2.456, 2.429: quantities checked, scanner right.
- Syllable divisions like 'su-bla-to' (474), 'o-bi-ci-unt' elsewhere, 'e-xer-ci-tus' (415) differ from the orthographic divisions but the quantities are right; not changed (only 2.444 added, for consistency with 2.200).
- Glossary: not touched.

## Counts
major 3, medium 20 (items 4-9 are 6; 14 scan entries), low 9.
