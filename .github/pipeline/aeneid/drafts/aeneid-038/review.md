# aeneid-038 (V.680-778) review, two passes

Severity counts: **major 24, medium 22, low 27** (73 changes).
Build: `python3 build_aeneid.py aeneid-038` passes the tiling and scansion stages (17 hand scansions applied, nothing UNRESOLVED) and then stops only because `gloss.json` does not exist yet. Nothing was written to the manifest; the full build was NOT run to completion.
`units.json` was edited by script (`t` untouched, l line counts equal t, i single-line). `make_units.py` is now stale; `units.json` is authoritative.

## Scansion (17 entries added to scan-fixes.json; the scanner knows no vowel quantities, so cost 0.0 does not mean right)

Major (16): 5.684 heroum/infusaque (he, ro long; -a, -que short); 5.685 Aeneas + umeris (ŭ-mĕ-rīs); 5.690 Teucrum (Teu- one syllable); 5.700, 708, 741, 755, 770 Aeneas/Aenean (Ae-nē-ās); 5.703 fatorum (long fā, -rum elided) and Italas (short I, as published italos/italis); 5.712 coniunge (consonantal i); 5.713 trāde āmissis, superant; 5.745 plēnā, venerātur; 5.753 hypermetric (-que elides into exigui of 754; scanner UNRESOLVED); 5.759 vīcīna, Ĕrўcīno (scanner had vi/ci short, Ery- long); 5.761 (COSTLY 4.1) lātē, săcer, Anchiseo four syllables; 5.775 prōrā pă-tĕ-răm.
Medium (1): 5.735 colo / Huc left in hiatus across the full stop (see doubtful).

Checked by hand and left as the scanner has them: all other lines, including Iuppiter 687, Iovis 726/747, Iamque 738/762, Iliacis 725, Ilium 756, iuvenes 729, iubet/iura/iussa, Troianos/Troiam, aethere 695, proiicit 776 (pro-ji-cit: scanner's `pro–ii⏑cit⏑` is the same three syllables), euntes 777, deinde 741/773, huic 713, all hiatus candidates (only 735 needed one).

Doubtful quantities (unconfirmed against an edition): 5.735 hiatus colo/Huc (the elided fit needs -que and co lengthened; mine has all natural quantities but a hiatus); 5.689 da (imperative, long, only fit); 5.692 obrue, o lengthened before br; 5.724 mihi with long -i; 5.731 tibi long -i; 5.736 nigrarum, ni lengthened before gr; 5.703 oblitus, ob lengthened before bl; 5.761 Anchiseo sē long, four syllables; 5.759 Ĕryx short E against the 5.772 precedent (consistent) but vīcīna long-long (L&S); 5.753 rēmos.

## Notes / l / i / about

Major (8): n#681-684 said `est` is left out (it is in the line) and left `carinas` unlabelled; l#687 reversed the sense ("the flame to escape the fleet"); n#691-692 meaningless "dative-less form", object of the imperatives unlabelled; n#718 "Greek-style accusative" for Acestam; n#721 `subvecta` from a "deponent subvehor" (it is passive of subveho); n#724 "tmesis" around `miseratus… est` (none); n#740 said Greenough prints tenuis at 690 (he prints tenues); n#741-742 Odyssey-11 claim attached to the wrong scene (Aeneas here only speaks) -> cross-referenced to Creusa II.792-794 and Homer's ghost scenes, softened.

Medium (21): about (Penates -> Lar of Troy and Vesta); l 683 descendit; n 687 `quid`; l/i 695-696 (a rain; blackest on austris; "thick with water"); i 698-699 self-contradiction; l/i 704-707 (vel… vel as "whether"; "began"; "her many arts"); n 704 Nautes/Nautii/Pallas softened and sourced to ancient commentary; n 709 "double -que recurs" false; n 710 "unfinished clause", "four words"/"Stoic"; l 691-692 thou/thy and an invented object "me"; l 722 omitted visa; i 733-735 misplaced tristes umbrae; i 737 "There" for tum; n 750-751 l garbled; n 752 navigium not a diminutive; n 763 "contracted from stravi"; n 777 note's speculation replaced.

Low (27): umeris case; exosus label; cross-reference to previous part removed; Tritonia derivation hedged; Segesta hedged; 'Acestam'; l archaisms; 'incense-box' for acerra; 'forum indicere', 'novendiale', 'Ilium/Troia' claims attributed or softened; bello added to the note at 754; Averna label; unsupported "colo also means I tend" aside; "very words of 726-727"; vague "as the allies will"; l certatim, l 765 "There", l 759-761 Anchiseo, l 731-733 alta/"heights", l 721 subvecta, l 697 super.

Echoes of known English rephrased (low): i 687-690 ("to the last man", "ancient pity"), i 710 ("every fortune is to be overcome by bearing it"), i 743-745 ("hoary Vesta", "stirs the ashes", "censer").

## Facts verified or softened

- Nautes / Nautii / Pallas: kept as later tradition from the ancient commentators, not Virgil.
- Odyssey 11 at 742: refused as stated (the scene is not Odysseus's three tries); replaced by II.792-794 and a general Homeric reference.
- Tempestates at Rome (773): kept (cult of the Tempestates at Rome is well attested); no change.
- Acestes' Trojan mother and river-god father (note 711): confirmed (V.38). III.349-351 new names for old: confirmed. 615-617 the women who hated the sea: confirmed. 'spectare' historic infinitive in the last part: confirmed in aeneid-037.
- 5.777: Greenough prints it unbracketed; the Latin Library lacks it (variants file). Note rewritten without speculation.
- Speech marks: 687 opens / 692 closes; 709 opens / 718 closes; 724 opens / 739 closes; 741-742 two cries in one unit. All present and matched in l and i.
- 5.741-742: the print has `proripis? ”inquit,` (closing mark joined to the next word, a clear misprint); t as printed per the established practice, note says so. Per rule 5b this also belongs in QUESTIONS.md (not touched here).

## Refused / not changed

- Latin Library variants: all in-range variants are orthographic or morphological; the existing notes that mention them (flamma/viris 680, numen/nomen 768, additus 761, line absent at 777) stay because they affect sense or the unit's reading; the purely orthographic ones were left as drafted (harmless).
- No change to house renderings (none in range). No glossary work (gloss.json not yet made).
- 5.776 left as the scanner has it (cost 0.8, same syllables as pro-ji-cit).
