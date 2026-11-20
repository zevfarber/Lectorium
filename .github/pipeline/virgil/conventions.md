# Virgil, *Eclogues* and *Georgics* — conventions (set up 2026-11-20)

Everything in `../aeneid/conventions.md` applies (the Latin decisions, edition, segmentation, the two English layers,
notes, glossary shape, scansion, audio, advisories) except what is said here. These are the owner's first "easy win"
reserve texts on the text pipeline: same edition and machinery as the Aeneid.

## Edition
Greenough, *The Bucolics, Aeneid, and Georgics of Virgil* (Boston: Ginn & Company, 1881) — the Aeneid's edition.
Perseus TEI `phi0690.phi001` (Eclogues) and `phi0690.phi002` (Georgics), kept in `source/`; the archive is
`source/virgil-greenough.json` (made by `archive_virgil.py`). No second witness was archived.
These TEI files carry **no paragraph marks and no speech marks** (the Aeneid's do):
- **Eclogues**: Greenough prints the speaker's name over each turn (TEI `<speaker>`); the archive records it as
  `speaker` on the turn's first line, and each turn begins a paragraph. A unit never runs across a change of
  speaker. The first unit of each turn begins its `i` with the speaker's name and a colon (`Meliboeus: …`); the
  build refuses otherwise. A turn may end without punctuation in Greenough (Ecl. 1.10); the unit ends there anyway.
  Ecl. 5.43–44, Daphnis's epitaph, is printed in capitals with V for U, as Greenough prints it.
- **Georgics**: paragraphs are Perseus's sense sections (`card` milestones). Five lines Greenough brackets are kept
  in `[ ]`, as in the Aeneid.
- No “ ” in the text: these TEI files do not mark speeches. Speeches inside a Georgics passage are shown in `i`
  with English quotation marks; `t` stays as printed.

## Sectioning and library
Each Eclogue is one part (63–111 lines); the Georgics are cut at the sense sections, ~100 lines (84–120).
`parts.json` gives each part its `work` (Eclogues | Georgics), `cite` (`Ecl. I`, `G. I.1–117`) and `group`
(`Eclogue I`; `Book I`). Library: language Latin, works **Eclogues (Virgil)** and **Georgics (Virgil)**.
`part` = English name + citation, `titleEn` = `<English name> — <cite>`; `title` a short Latin title of our own.

## Glossary
`virgil-glossary.json` (repository root), seeded on 2026-11-20 with the Aeneid glossary's entries for the
4,379 forms the two works share with it; the other 3,910 forms are new. Same shape and rules as the Aeneid's.

## Scansion
`scan-fixes.json` here is keyed `<book>.<line>` with book `E1`…`E10`, `G1`…`G4`. The Aeneid's file shows the
pattern and the scanner's Virgilian blind spots. The inscription lines (Ecl. 5.43–44, capitals, V for U) will need
hand scansion.

## House renderings (use as written)

| line | Latin | `l` | `i` |
|---|---|---|---|
| Ecl. 1.1–2 | *Tityre, tu patulae recubans sub tegmine fagi / silvestrem tenui Musam meditaris avena* | "Tityrus, you, of a spreading lying-back under the cover of beech, / a woodland Muse on a slender reed are practising" | "Meliboeus: Tityrus, you lie back in the shade of a broad beech and work out a country song on a thin reed pipe" |
| Ecl. 4.5 | *magnus ab integro saeclorum nascitur ordo* | "a great from-the-fresh-start of ages is born order" | "the great procession of the ages is beginning over again" |
| Ecl. 10.69 | *omnia vincit Amor: et nos cedamus Amori* | "all things conquers Love: let us too yield to Love" | "Love overcomes everything; so let us give way to Love as well." |
| G. 1.145–146 | *labor omnia vicit / improbus* | "toil all things has conquered, / relentless" | "relentless work has won through everything" |
| G. 2.490 | *felix qui potuit rerum cognoscere causas* | "fortunate who has been able of things to come to know the causes" | "Happy the one who has managed to learn why things are as they are" |
| G. 3.284 | *sed fugit interea, fugit irreparabile tempus* | "but flees meanwhile, flees unrecoverable time" | "But meanwhile time is running away, running away past all recovering" |

Check each against memory of the well-known modern versions for verbatim echo when it is reached, as the Aeneid's
rule says; rephrase any distinctive echo and update this table.
