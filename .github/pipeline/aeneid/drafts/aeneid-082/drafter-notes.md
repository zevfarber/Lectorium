# aeneid-082 — drafter notes (XI.1–99)

- **Units:** 46. `make_units.py` runs clean (no LINE COUNT / TOO LONG / ENDING / NOTE LENGTH / MARK / COVERAGE warnings); the cut covers all 99 lines, and the units joined reproduce the source (enforced by `aeneid_lib.cut`).
- **¶ units (p: true):** 1, 29, 59 — Greenough's three paragraphs in the stretch; each unit starts at the line start.
- **Title:** *Tropaeum Mezentii. Funus Pallantis*; part "Mezentius's Trophy and Pallas Sent Home (XI.1–99)".

## Speeches
| speech | lines | first unit (“) | last unit (”) |
|---|---|---|---|
| Aeneas to his captains | 14–28 (one speech; *ait* at 24) | ln 14 | ln 26 (26–28) |
| Aeneas over Pallas | 42–58 | ln 42 | ln 57 (57–58) |
| Aeneas's farewell | 96–98 | ln 96 | ln 97 (97–98, `vale.`) |

## Misprints (rule 5b; t as printed, l/i corrected, note opens "The print has…")
| line | print | corrected reading | note in unit |
|---|---|---|---|
| 24 | `“Ite, ait, egregias` | `Ite,” ait, “egregias` | ln 24 — the pattern of 6.46, 6.52, 7.121 (QUESTIONS item 44): an opening mark at the head of a line where *ait* interrupts a speech already open since 14. Alternative reading: Greenough closed the speech at 23 and the ” is missing there (a new speech beginning *Ite*); the English would be the same. |
| 87 | `terrae.~.~.` | `terrae.` | ln 86 (86–87). Unique in the source (no other `~` anywhere in the poem). The line is complete; the marks may be the encoder's or the printer's sign for something (a suspected gap?) that I cannot check. Flag for the owner: if they mean something, only the note changes. |
| 98 | `vale. ”Nec` | `vale.” Nec` | ln 98 (`”Nec plura… ferebat.`); the speech unit ln 97 closes ” in l/i and says "see the next unit", as 081 did at 812/856. |

Mark-check exemptions in the script: `PAIRS = {97: 98}` (the 98 stray-mark pair) and `OTHER = {24, 42}` — 24 for the misprinted “; 42 because Greenough prints `“Tene, inquit,` with no marks round *inquit* (his habit) and l/i add them (as 054, 061). The validator will count t's marks as printed: t has “ at 14, 24, 42, 96 and ” at 28, 58, 98 (4/3); l and i are balanced.

## Variants (Latin Library)
- 82 `sparsuros` / LL `sparsurus` — noted (sparsurus would make Aeneas the one who sprinkles). The rest (nequa, expectatique, adspicies, crates, necdum, viresque, vestes) are orthography/morphology and ignored; Greenough's spellings explained in the notes where useful.

## Doubtful constructions / points
- 16 *manibusque meis Mezentius hic est*: taken as "this, by my hands, is Mezentius" (the trophy is what is left of him), *manibus* ablative of means.
- 22 *socios inhumataque corpora*: taken as hendiadys.
- 37 *foribus*: ablative of way ("through the doors"), dative given as the alternative.
- 47 *in magnum imperium*: the Etruscan command and, beyond it, empire.
- 56–57 *nec sospite dirum optabis nato funus pater*: Evander will not have to wish for his own death because his son survived through cowardice.
- 58 *Ausonia* vocative, *perdis* serving both vocatives.
- 77 *amictu*: "probably the second of the pair" of robes.
- 31 *Parrhasio Evandro*: noted as hiatus only; the scansion (scanner flag) is for the scan-fixes pass. Scanner flags 4, 31, 58 not touched here (no `sc` written).

## Advisory
None. The funeral of Pallas and the captives bound for sacrifice (81–82) are treated as in 078/081: stated, not described. The killing of the captives is not narrated in this part; the note states the purpose in one sentence ("Virgil states it and does not describe it"). Acoetes's self-disfigurement in mourning (86) is a conventional gesture, two words. No trigger in conventions or the house advisory practice fires.

## Attributions from memory, unchecked
- VI.325–330 (the unburied wait a hundred years); VI.429 (line 28 repeated of the infants)
- VIII (Evander's parting, the Etruscan command); X.479–489 (Turnus's spear through Pallas's shield, corslet and chest); X.495–500 (Turnus takes the belt); XII.940–952 (the belt at the end)
- X.517–520 (Aeneas takes eight young men alive for sacrifice)
- IV.264 (line 75 repeated word for word)
- IX.435–437 (Euryalus as a cut flower); Iliad 8.306–308 (the poppy simile)
- Iliad 8.185 (Aethon one of Hector's horses); Iliad 17.426–440 (Achilles' horses weep); Iliad 23.175–176 (twelve Trojans at Patroclus's pyre)
- Catullus 101.10 (*ave atque vale*)
