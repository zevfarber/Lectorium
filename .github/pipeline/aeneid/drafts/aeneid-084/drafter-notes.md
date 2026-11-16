# aeneid-084 — drafter notes (XI.225–335)

- **Units:** 56. `make_units.py` runs clean (no LINE COUNT / TOO LONG / ENDING / NOTE LENGTH / MARK / COVERAGE / JOIN / SHA warnings); all 111 lines covered. Notes 36–116 words.
- **¶ units (p: true):** ln 225, 243, 296 — Greenough's three paragraphs; each unit starts at the line start.
- **Split at a colon:** 225–230 is one period of six lines; cut at `ferunt:` (227).
- **Speech open at XI.225?** No — 083 ends with narrative (222–224).
- **Title:** *Responsa Diomedis. Concilium Latini*; part "Diomedes' Refusal and Latinus's Council (XI.225–335)".
- **Advisory:** none (no trigger; Agamemnon's murder is one line, no detail).

## Speeches
| speech | lines | first unit (“) | last unit (”) |
|---|---|---|---|
| Venulus's report | 243–295 | ln 243 | ln 294 (294–295) |
| Diomedes, quoted inside it | 252–293 | ln 252 (second “ in the print) | no mark of its own: the print's single ” at 295 closes both |
| Latinus | 302–335 | ln 302 | ln 335 |

l and i follow the print's marks exactly (two “, one ”), so counts match t and no exemption is needed; the
validator may WARN 3 opening / 2 closing marks for the part. Diomedes' words in fact end at 293 (*cavete.*):
294–295 (*rex optime, regis… audisti*) are Venulus to Latinus. Not treated as a misprint (Greenough's way of
printing a quotation that ends a speech's penultimate stretch is not certain); the notes at 293 and 294 say
where Diomedes stops. If the owner wants a ” after *cavete.* in l/i, only those two units change.

## Misprints (rule 5b; t as printed, l/i corrected, note opens "The print has…")
| line | print | corrected | note in unit |
|---|---|---|---|
| 236 | `olli` (small letter after the full stop ending 235) | `Olli` | ln 236 (236–237). Lowercase-after-stop ruling (QUESTIONS item 43) still open; handled as 083 (220 `ingravat`). |

## Possibly dropped punctuation (rule 5 candidates — NOT fixed: I may not touch the source; orchestrator to decide)
- **11.291** `praestantibus armis` with no stop before `hic pietate prior.` (292). Most editions print `armis;`.
  t as printed; l puts a semicolon, i a stop-like break; the note at ln 291 says the print has no stop. If the
  printed Greenough has the semicolon, rule 5 applies (add `;` to the source, re-pin aeneid-084).
- **11.326** `navis` with no mark before `seu pluris…`, and **11.328** `materies,` where editions have `;`.
  Could be Greenough's light pointing; t as printed, l/i punctuate by sense, the note at ln 326 says so.
  I cannot check the printed page (Perseus TEI is the only copy here).

## Doubtful readings (kept, said so)
- **268 `subsedit`** — kept; note gives the variant `possedit` (sense changes). The Latin Library agrees with Greenough here (no variant in the packet); `possedit` is from memory of the apparatus, unchecked.
- Latin Library variants in the packet are all orthography/morphology (260 Caphereus, 264 penatis, 266 Achiuum, 277 appetii/uulnere, 308 si quam ascitis, 319 collis) — none noted for sense; 277 `adpetii` and 308 `adscitis` spellings are glossed in the notes.

## Scansion (for scan-fixes.json; not written — outside drafts/aeneid-084/)
- **11.260** `sīdŭs ĕt | Eūbŏĭ|cāe cāu|tēs ūl|tōrquĕ Că|phāreūs` — `-eus` one syllable by synizesis; `Euboicae` with Eu- long, -bo-i- short (Εὐβοϊκός).
- **11.309** `pōnĭtĕ | spēs sĭbĭ | quīsquĕ sĕd | hāec quām_ān|gūstă vĭ|dētīs` — scanner fails on the elided monosyllable `quam`.
- Also check: 262 `Prōtei` (-ei one syllable), 265 `Īdŏmĕnei` (-ei one syllable), 292 `Coeant` (coe- one syllable), 232/282 `Aenean`, 233 `deum`, 243 `Diomedem`, 276 `caelestia`, 247 `Iapygis` (I- vocalic).

## Unchecked attributions from memory
Iliad 5 (Diomedes vs Aeneas with the stone; Aphrodite wounded in the hand); Iliad 6 (Hector and Aeneas named as Troy's best, Helenus's words); Odyssey 4 (Menelaus and Proteus on Pharos), 9 (Cyclops), 11 (Agamemnon's murder); Aeschylus, Agamemnon; Ovid Met. 14 (Diomedes' companions turned to birds); Aeneid I.39–45, I.100–101, III.121–122, III.325–336, III.588–681, VII.591–600, VIII.9, VIII.319–325; Nauplius's false beacons at Caphareus for Palamedes; Idomeneus's vow; the Locrians in Libya (Servius); Aegiale's infidelity; Argyripa = Argos Hippion, later Arpi; the Sicani as early inhabitants of Latium; *pacem petendum* as a Lucretian construction; *possedit* as a variant at 268.

## For QUESTIONS.md
- 236 lowercase `olli` (item 43 still open).
- 291 / 326 / 328 possibly dropped punctuation (rule 5) — needs a look at the printed Greenough.
- 252/295 nested speech with a single closing mark: confirm l/i should follow the print rather than close Diomedes at 293.
