# Marcus Aurelius, *Meditations* (Τὰ εἰς ἑαυτόν) — conventions (set up 2026-11-21)

Added to the text pipeline at the owner's request ("I want to add Marcus Aurelius to the list"). Greek prose; the
build is Hesiod's adapted for prose (no scansion). The shape of a unit is the Aesop fables' (`aesop-001.json`):
prose sense-units, a note on each, two English layers.

## Edition of record
J. H. Leopold, *M. Antoninus Imperator Ad se ipsum* (1908), the Greek text. Public domain everywhere. Perseus TEI
`tlg0562.tlg001.perseus-grc2`, kept in `source/`; the archive is `source/meditations-leopold1908.json`
(`archive_meditations.py`). Older English versions (Casaubon 1634, Long 1862, Haines's Loeb 1916) are in copyright
nowhere but are published translations: the copyright policy treats them like the KJV — a silent meaning check
on a hard passage, never for wording, never quoted, never named.

What the edition does that the text keeps:
- `⟨ ⟩` — words Leopold supplies (41). The note says the word is the editor's and what the manuscripts have
  (nothing) where it matters to the sense.
- `[ ]` — words Leopold deletes (18), kept as printed. Translate them inside [ ] in `l` and leave them out of `i`;
  the note says why an editor would cut them if the reason can be seen from the Greek.
- `†` — two places (3.4, 4.18) where Leopold judges the text corrupt. The note says plainly
  that the text is damaged here and the English is a guess at the sense.
- Verse quotations (Homer, Hesiod, Euripides, Empedocles…) set as verse: their units are `v: true` (the build sets
  it) and `l` keeps the line breaks. The note names the poet where Marcus does or where it is certain, and says
  the line is quoted, not Marcus's own.
- The two book subscriptions Leopold prints (end of Book 1: Τὰ ἐν Κουάδοις πρὸς τῷ Γρανούᾳ; end of Book 2: Τὰ ἐν
  Καρνούντῳ) are one unit each. The note: these are headings in the manuscripts naming where the notes were
  written (among the Quadi on the river Gran/Hron; at Carnuntum on the Danube), and whether they belong to the
  book before or after is disputed.

## Sectioning, library, numbering
Parts end only at a chapter's end and never cross a book, ~800 Greek words (651–1014): 38 parts (`parts.json`,
`plan.md`). Library: language Ancient Greek; work **Τὰ εἰς ἑαυτόν — Meditations (Marcus Aurelius)**; group
`Book N`. `cite` is `4.11–24`; `part` = `<English name> (<cite>)`, `titleEn` = `<English name> — <cite>`.
The English name is ours, from the content of the stretch ("Debts to Family and Teachers", "Morning Thoughts").
Numbering: the build puts the standard book.chapter number (`ln`, e.g. "4.3") on each chapter's first unit and
starts a paragraph there; the reader shows it in the margin. The drafter writes none of `ln`, `p`, `v`, `tr`.

## Segmentation
The unit is the punctuated sense-unit: a sentence, or a colon ending at `·` where Marcus strings maxims together.
Book 1 is lists ("From X: …; …; …") — a unit may be one item or a few short ones, ending at `·` or `;`. No unit over
70 Greek words (the build refuses); cut long periods at a `·`, `;`, or a comma that closes a clause. A unit never
crosses from one chapter, or from prose into a verse quotation, to the next.

## The two English layers
- `l` follows the Greek order as far as English can bear. Coherence wins ties. Marcus's articular infinitives and
  neuter adjectives used as nouns (τὸ καλόηθες, τὸ μὴ φοιτῆσαι) are kept visible in `l` ("the good-charactered",
  "the not going") and made into natural English in `i`.
- `i` is real English prose: plain, compressed, serious — Marcus writing to himself, not a sermon. Not archaic,
  not modern self-help idiom. No `\n`.
- Second person: Marcus addresses himself as "you" (σύ, imperatives). Keep "you"; never turn it into "one" or "we".
- **The same Greek gets the same English.** Marcus repeats his maxims across books; the packet shows where a
  sentence already stands in a published part, and the validator enforces identical English for an identical unit.
- Proper names in their familiar English forms (Verus, Rusticus, Epictetus, Apollonius, Sextus, Fronto,
  Alexander the Platonist, Severus, Maximus, Antoninus [Pius], Hadrian, Augustus, Heraclitus, Democritus,
  Socrates, Chrysippus, Epicurus, the Quadi, Carnuntum). `tr` carries the Greek form.
- Never bowdlerize; never soften his bleak passages on death, decay and the body.

## Sole-source rule
Draft from Leopold's Greek plus, from your own knowledge, the public-domain aids: **LSJ 8th ed. (1897)**,
**Smyth (1920)**, **Goodwin's *Greek Grammar***. Modern translations of the *Meditations* are in copyright and
distinctive — Hays, Hammond, Hard, Waterfield, Staniforth, Farquharson, Hicks & Hicks, and others. Never consult
them, never name them. Marcus is among the most-translated and most-quoted ancient authors: an English sentence
that arrives fully formed and sounds familiar is very likely someone's translation — rebuild it from the grammar.
Check every famous passage (2.1, 4.3, 4.49, 5.1, 6.6, 7.69, and any other chapter that turns up in anthologies) for
verbatim overlap with the well-known modern versions before delivering, and rephrase any distinctive echo.

## House renderings (use as written; a note on first occurrence in a part, then a nudge)

| Greek | `l` | `i` |
|---|---|---|
| Παρὰ τοῦ X (Book 1, opening each debt) | "From X:" | "From X:" followed by the qualities as nouns or "-ing" phrases ("From my grandfather Verus: good character and an even temper.") |
| τὸ ἡγεμονικόν | "the ruling-part" | "the ruling part (of the mind)" — note: the Stoic term for the mind's command centre, where judgment happens |
| λόγος (cosmic or human reason) | "reason" | "reason" — note says logos when it is the reason running through the whole; never "the Word", never left as "logos" in `i` |
| φύσις / ἡ τῶν ὅλων φύσις | "nature" / "the nature of the wholes" | "nature" / "the nature of the universe" |
| τὸ ὅλον / τὰ ὅλα | "the whole" / "the wholes" | "the whole" / "the universe" |
| ὁ κόσμος | "the world-order" | "the world" — note on first use: an ordered whole, not just "the world" |
| ὑπόληψις | "supposition" | "judgment" (or "opinion" where it means what someone else thinks) |
| φαντασία | "impression" | "impression" (what presents itself to the mind; never "fantasy", "imagination" only where the context forces it) |
| δόγμα, -ατα | "doctrine(s)" | "principle(s)" |
| ὁρμή / ἀφορμή | "impulse" / "repulsion" | "impulse" / "aversion" |
| ὄρεξις / ἔκκλισις | "desire" / "avoidance" | "desire" / "avoidance" |
| πάθος | "passion" | "passion" (a disordered emotion, in the Stoic sense — note on first use) |
| ἀπάθεια | "passionlessness" | "freedom from passion" |
| ἀταραξία / ἀτάραχος | "undisturbedness" / "undisturbed" | "calm" / "calm" |
| ὁ δαίμων (the one within) | "the daimon" | "the guardian spirit within you" — note: the divine element in each person; never "demon" |
| κοινωνικός / τὸ κοινωνικόν | "community-minded" | "made for community" / "the social good" by context |
| τὰ ἀδιάφορα | "the indifferent things" | "things that make no difference (to the good life)" — note: the Stoic technical term |
| τὸ κατὰ φύσιν / παρὰ φύσιν | "the according-to-nature" / "against nature" | "what accords with nature" / "against nature" |
| προαίρεσις | "choice" | "will" or "choice" by context |
| εἱμαρμένη | "fate" | "fate" |
| πρόνοια | "providence" | "providence" |
| ἄτομοι | "atoms" | "atoms" — Marcus's "providence or atoms" dilemma: note on first occurrence |
| σύ (self-address) | "you" | "you" |

New recurring terms: choose a rendering with the same care, list it in `drafts/meditations-NNN/new-renderings.md`,
and the run copies it into this table at publish.

## Notes (`n`)
What a tutor would point at, for a reader who may have little Greek: the construction (articular infinitive,
genitive absolute, the verbal adjective in -τέον, optative of wish, the neuter adjective as an abstract noun), the
Stoic term and what it means in the system, the person named and who they were (only what is securely known), the
editorial sign and what it means. Second-century forms that differ from classical Attic (γίνομαι for γίγνομαι,
-σσ- for -ττ-) get a one-line flag the first few times. Quote Greek bare (no backticks), English glosses in single
quotes. A note makes no claim about the rest of the work that the part cannot show. Most units carry a note of
25–90 words; a unit whose words have all been explained in the part may have a short one.

## Glossary entries
One shared file, `meditations-glossary.json` (repository root). Keys are lowercased word forms exactly as printed
(an elided form without its apostrophe: `δ`, `ἀλλ`, `ἐφ`). One entry per form, general to the form, never pinned
to a line: `<dictionary form as LSJ lemmatises it> — <terse meaning>; <parse>`, e.g.
`"ἡγεμονικὸν": "ἡγεμονικός, -ή, -όν — able to command; as noun τὸ ἡγεμονικόν, the ruling part of the soul (Stoic); neut. nom./acc. sg."`.
Typographic ’ only, under 230 characters. A genuine homograph gets both readings joined by " · ".
**Seeded entries:** at setup the Aesop glossary's entries were copied in for the 1,667 forms the two texts share.
Before a seeded entry is relied on, check it covers Marcus's use (Aesop's meanings are the everyday ones; Marcus
uses many of the same words as Stoic terms) and broaden it under `__broaden__` where it does not. Additions
only: an entry may be broadened (old entry whole, then " · " and the new reading), never replaced.
