# Virgil, *Aeneid* — conventions

*Pilot built 2026-10-12 (aeneid-001, I.1–101). Not yet approved by the owner; until he approves it, these
rules are proposed, and the work is **not** on `queue.txt`.*

The language-level Latin decisions are Ovid's (project doc `claude/latin-ovid-conventions.md`) and are not
reopened here: **reconstructed Classical (restored) Latin**; `langCode: null`; no transliteration, no
plain-letters toggle; no macrons in the text (lemmas in the glossary may carry them); verse as verse.
Everything below is what Virgil adds, or where the Aeneid differs from Ovid's set-up.

## Edition of record

**J. B. Greenough, ed., *The Bucolics, Aeneid, and Georgics of Virgil* (Boston: Ginn & Company, 1881)** —
the Latin text only. Public domain everywhere. Machine-readable copy: Perseus TEI
`PerseusDL/canonical-latinLit`, `data/phi0690/phi003/phi0690.phi003.perseus-lat2.xml` (sha256 recorded in
`source/aeneid-greenough.json`). The plan of 2026-10-11 proposed Hirtzel (Oxford 1900); no machine-readable
Hirtzel is reachable from the pipeline's network (archive.org and Gutenberg are blocked), so Greenough it is.
Both are pre-1930. If the owner wants Hirtzel later, it means re-archiving and re-issuing published parts.

**Witness B — The Latin Library** (`cltk/lat_text_latin_library`, `vergil/aen1–12.txt`) is a disagreement
detector only, exactly as for Ovid. It never contributes a character. Its disagreements are pre-computed in
`source/variants-latinlibrary.json` (u/v and i/j differences are ignored as orthography) and appear in each
part's packet. Note a variant in `n` only where it changes the sense; ignore orthography (`urguet`/`urget`,
`volnus`/`vulnus`) and morphology (`omnes`/`omnis`).

**Keep Greenough's spelling exactly**: `volnus`, `divom`, `Karthago`, `-is` accusative plurals (`montis`,
`omnis`, `duplicis`), `disiice`, `urguet`, `adparent`, `maxumus`. A note may give the familiar form once.

Mechanical normalisations made by `archive_aeneid.py`, and nothing else:
- Perseus encodes Greenough's printed speech marks as `<q>`; the archive prints them as “ ” (the opening
  mark where a speech opens, the closing mark after the last line of the speech, before any punctuation
  Greenough prints outside it). Magnus's Ovid carries “ ” the same way.
- Lines Greenough brackets as spurious (`<del>`: 61 lines, among them the Helen episode 2.567–588) are
  kept and printed inside `[ ]`. A part containing one says so in the note of the unit it falls in. None
  falls in Book I's first part.
- The Perseus note at 3.250 is dropped (Perseus's, not Greenough's).
- Book X: Greenough prints a half-line **62b** (`Tum regia Iuno`); it is kept as its own source line with
  `label: "62b"` (number 62). Greenough also prints **10.717–718 between 713 and 714**; the archive keeps his
  order. The parts containing these spots (`aeneid-072`, `aeneid-080`) say so in a note.

## Sectioning

The twelve books are the authentic division and are the manifest `group` (`"Book I"`). Inside a book, parts
end **only where Greenough begins a paragraph** (an indented line in the TEI — 447 in the poem), aiming at
~100 lines: 99 parts, 71–132 lines, median 99 (`parts.json`, `plan.md`). The pilot, I.1–101, is pinned.

- Ids `aeneid-NNN` in poem order; `seq` on every manifest entry.
- `part` = our English name for the stretch + citation, Roman book numeral and Arabic lines, as for Ovid:
  `Juno's Anger and the Storm (I.1–101)`. `titleEn` = `<English name> — Aeneid <cite>`. `title` = a short
  Latin title of our own (`Iunonis ira. Aeolus`). Never borrow a translation's headings.
- Library: language **Latin**, work **Aeneid**, workEn **Aeneid (Virgil)** — so the Latin optgroup shows
  *Metamorphoses (Ovid)* and *Aeneid (Virgil)* side by side.

## Verse and segmentation (Ovid's rules)

- `t` holds the verse lines joined by `\n`; `v: true`; `ln` = the line the unit starts on; `p: true` on the
  first unit of each of Greenough's paragraphs (when the unit starts at the beginning of that line).
- **Tap-unit = the punctuated sense-unit**: ends at `. ; : ? !` (or a dash where Greenough breaks off),
  may begin or end mid-line, at most five lines; split long periods at internal punctuation.
- `t` is cut from the source by script (`aeneid_lib.cut`), never retyped. The units joined in order must
  reproduce the source; the build and validator enforce it.
- `l` keeps the **same line division as `t`**; `i` is one line of real English.

## The two English layers and the notes

- `l`: structurally transparent where English can bear Virgil's order; coherence wins ties. Show the
  hyperbaton when it teaches something (`cavum… montem` framing the line), then fall back to sense.
- `i`: real, slightly elevated English. Never childish, never modern-casual.
- `n` on every unit: what the reader needs to read these words — constructions, Greenough's archaic forms,
  epic conventions, the Homeric model where Virgil is rewriting a scene, mythological background. Flag a
  recurring pattern the first few times ("you'll see this constantly"), then nudge.
- Recurring patterns already flagged in the pilot: old genitive plural `-um`/`-om` (`superum`, `divom`,
  `virum`, `Danaum`); `-ere` = `-erunt`; elision; double `-que… -que`; ellipsis of the verb of speaking
  (`haec secum`, `Aeolus haec contra`); connecting relative; accusative and infinitive of indignation
  (`Mene… desistere`, `Mene… non potuisse`); dative of possession (`sunt mihi`).
- Sole source: the Latin plus public-domain reference works (Lewis & Short, Allen & Greenough's grammar,
  Greenough's own school notes, Conington's commentary). No modern translation is opened while drafting.
  The old Dryden is public domain and may be consulted silently as a meaning check on a hard passage, never
  for wording.

## House renderings (decided in the pilot; use these, do not re-decide them in a batch)

| line | Latin | `l` | `i` |
|---|---|---|---|
| I.1 | *Arma virumque cano* | "Arms and a man I sing" | "War is my song, and a man" |
| I.11 | *Tantaene animis caelestibus irae?* | "Are there such great angers to heavenly spirits?" | "Can the spirits of heaven harbour such anger?" |
| I.33 | *Tantae molis erat Romanam condere gentem!* | "Of so great a mass it was to found the Roman nation!" | "Such a weight of toil it took to found the Roman nation!" |
| I.94 | *O terque quaterque beati* | "O both three-times and four-times blessed" | "How fortunate, three times and four times over" |

Set pieces still ahead, to be decided in a dedicated pass before the batch that reaches them (Ovid's
ruling of 2026-08-27): I.203 *forsan et haec olim meminisse iuvabit*; I.462 *sunt lacrimae rerum*;
II.49 *timeo Danaos et dona ferentis*; IV.23 *agnosco veteris vestigia flammae*; VI.126–129 *facilis
descensus Averno*; VI.851–853 *tu regere imperio populos, Romane, memento*; XII.952 *vitaque cum gemitu
fugit indignata sub umbras*. For each: build from the Latin, check the result against memory of the
best-known modern versions for verbatim echo, and rephrase any distinctive echo.

## Glossary

One work-level **`aeneid-glossary.json`** (the `metamorphoses-glossary.json` wrapper), keyed by the
lowercased form exactly as the reader's `WORD_RE` cuts it — enclitics stay on the word (`virumque`,
`mene`, `quidve`). Entry: `lemma — meaning (parse)`, general to the form, never pinned to a line, under 230
characters. Additions only; an existing entry may be broadened (`__broaden__`, the old entry kept whole).
Not shared with Ovid's glossary: Ovid's entries carry Ovid-specific readings.

## Scansion

`sc` is made by the build with the shared scanner `.github/scripts/scan_latin.py` (Ovid's), then
overridden line by line by **`scan-fixes.json`** — hand scansions, each with its reason. The scanner's
recurring Virgilian blind spots: Greek `eu` (Eurus, Teucri) and initial `Ae-` split in two; consonantal `i`
after a prefix (`coniunx`, `iniuria`, `disiecit`) read as a vowel; synizesis preferred to the ordinary
reading (`Danaum`, `reliquias`); hiatus (`Samo hic`, I.16). **Do not run the "Scan Latin verse" workflow on
`aeneid-*.json`**: it would overwrite the hand fixes. The validator checks every line is six feet of
dactyls/spondees.

## Audio

Same route and voice as Ovid: `build_pinned.py` → `latin_verse.py` (normal word stress, long vowels from
`sc`, elision as in verse), de-DE-Wavenet-B at 0.85. No configuration is needed — `language: "Latin"`,
`langCode: null` is what routes it. A new Latin part is left to the daily "missing" sweep (pick_targets.py),
which takes Odyssey → Igor → Aesop → Ovid first; the owner may dispatch *Build audio* with a part id to
build one sooner.

## Advisories

`claude/content-advisory.md` applies unchanged (sexual violence always; graphic detail rarely; never
bowdlerize). Ahead: Book II (Priam's death, Laocoön), Book IV (Dido's suicide — not covered by any trigger
yet; see QUESTIONS.md), Book X–XII battle narrative (ordinary killing earns nothing).
