# Hesiod, *Theogony* and *Works and Days* — conventions (set up 2026-11-20)

An "easy win" reserve on the text pipeline, at the owner's request: Greek hexameter on the Iliad's machinery.
Everything in `../iliad/conventions.md` (and through it `../odyssey/conventions.md`) applies — the two English
layers, notes, romanization, scansion, the glossary-entry format, the house-renderings tables, sharing English
with Homer, advisories — except what is said here.

## Edition of record
H. G. Evelyn-White, *Hesiod, the Homeric Hymns and Homerica* (Loeb Classical Library; London: Heinemann, 1914), the
Greek text only. Public domain everywhere. Perseus TEI `tlg0020.tlg001` (Theogony) and `tlg0020.tlg002` (Works and
Days), `perseus-grc2`, kept in `source/`; the archive is `source/hesiod-evelyn-white1914.json` (`archive_hesiod.py`).
Evelyn-White's own English translation is in copyright nowhere (1914) but is a published translation: the
copyright policy treats it like the KJV — a silent meaning check on a hard passage, never for wording, never
quoted.

What the edition does that the text keeps:
- Lines he brackets as spurious are kept in `[ ]` (12 in the Theogony, 14 in the Works and Days). A unit containing
  one says so in its note.
- Theogony 929a–t: after line 929 he prints, from Chrysippus as quoted by Galen, a different version of the births
  of Hephaestus and Athena. The archive keeps it in `⟨ ⟩`, labelled 929a–t (all `ln` 929), with the ellipsis the
  edition marks inside it recorded, not printed. The first unit of the passage says plainly in its note what it is.
- Transposed lines (Th. 212–214, 425–434; WD 168–173, 360–363, 767–769) and the omitted WD 310 follow the edition;
  the unit says so in its note.

## Sectioning and library
Parts end only where Evelyn-White begins a paragraph, ~100 lines (91–113): 10 Theogony parts, then 8 Works and Days
parts (`parts.json`, `plan.md`). Library: language Ancient Greek; works **Θεογονία — Theogony (Hesiod)** and
**Ἔργα καὶ Ἡμέραι — Works and Days (Hesiod)**; `group` Theogony / Works and Days. `cite` is `Th. 1–103`,
`WD 1–105`; `part` = `<English name> (<cite>)`, `titleEn` = `<English name> — <cite>`.

## Dialect and glossary
Hesiod's language is the epic Kunstsprache with Boeotian/Aeolic touches; a note says where a form is not Homeric.
`hesiod-glossary.json` (repository root) was seeded at setup with the Iliad's, then the Odyssey's, entries for the
3,291 forms Hesiod shares with Homer (of 5,519); check a seeded entry against the use here and broaden it where
Hesiod uses the form differently.

## House renderings (use as written)

| Greek | `l` | `i` |
|---|---|---|
| Th. 1 Μουσάων Ἑλικωνιάδων ἀρχώμεθ’ ἀείδειν | "With the Muses of-Helicon let us begin to sing" | "Let us begin our song with the Muses of Helicon" |
| Th. 116 ἤτοι μὲν πρώτιστα Χάος γένετ’ | "Truly first of all Chaos came into being" | "First of all, Chaos came to be" (Chaos untranslated; the note: a yawning gap, not disorder) |
| Th. 27–28 ἴδμεν ψεύδεα πολλὰ λέγειν ἐτύμοισιν ὁμοῖα, / ἴδμεν δ’, εὖτ’ ἐθέλωμεν, ἀληθέα γηρύσασθαι | "we know how to say many false things like to true ones, / and we know, whenever we wish, how true things to proclaim" | "We know how to tell many lies that sound like the truth, and we know how to speak the truth when we choose." |
| WD 1 Μοῦσαι Πιερίηθεν | "Muses from-Pieria" | "Muses of Pieria" |
| WD 289 τῆς δ’ ἀρετῆς ἱδρῶτα θεοὶ προπάροιθεν ἔθηκαν | "but before excellence sweat the gods have set" | "But in front of excellence the gods have put sweat" |
| ἀρετή (WD) | "excellence" | "excellence" / "success" by context (+ note) |
| ἔρις | "Strife" (the goddess) / "strife" | the same |

Check each against memory of the well-known modern versions for verbatim echo, as the Iliad's rule says.
