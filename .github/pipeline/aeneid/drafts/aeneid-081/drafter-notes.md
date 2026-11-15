# aeneid-081 — drafter notes (X.791–908)

- **Units:** 63. `make_units.py` runs clean (no LINE COUNT / TOO LONG / ENDING / NOTE LENGTH / MARK warnings); units joined reproduce the source (enforced by `aeneid_lib.cut`).
- **¶ units (p: true):** 791, 833 — the only two Greenough paragraphs in the stretch; both units start at the line start.
- **Title:** *Mors Lausi et Mezentii*; part "The Deaths of Lausus and Mezentius (X.791–908)".

## Misprints (rule 5b) — five, all the closing speech mark joined to the next word
| line | print | corrected reading | speech unit (l/i close with ”) | stray-mark unit (n opens "The print has…") |
|---|---|---|---|---|
| 812 | `tua. ”Nec` | `tua.” Nec` | ln 811 | ln 812 |
| 830 | `cadis. ”Increpat` | `cadis.” Increpat` | ln 829 | ln 830 |
| 856 | `linquam. ”Simul` | `linquam.” Simul` | ln 856 (`Sed linquam.`) | ln 856 (second unit on the line) |
| 882 | `prius. ”Dixit` | `prius.” Dixit` | ln 881 | ln 882 |
| 898 | `animi? ”Contra` | `animi?” Contra` | ln 896 | ln 898 |

`PAIRS = {811: 812, 829: 830, 856: 856, 881: 882, 896: 898}`. Note that the 856 pair has the same `ln` for both units (the speech ends and the narrative resumes on one line); the PAIRS mechanism keys on `ln`, so the exemption covers both, which is what we want, but a validator that keys PAIRS strictly by distinct `ln` may need to know this. t is untouched in all five.

No dropped punctuation found in the source for this stretch.

## Bracketed line
- 872 `[et furiis agitatus amor et conscia virtus.]` — Greenough's spurious bracket; in unit ln 870 (870–872), whose note says so. l and i keep the brackets. The Latin Library omits the line.

## Doubtful readings / points
- 850 `exitium infelix`: Greenough (and the Latin Library) print *exitium*; from memory many editors read *exilium* ("exile"), which fits 852. Noted in n as a variant reading of other editors; I could not check which editors print which.
- 857 `quamvis dolor … tardet` vs Latin Library `quamquam vis … tardat`: noted (slight sense change).
- 796 `prorupit`/`proripuit`, 801 `proturbant`/`perturbant`, 908 `arva`/`arma`: noted in n. Others are orthographic and ignored.
- 839 `multum … remittit`: *multum* for *multos* is odd; n gives both the "many messengers" and adverbial readings.
- 824 `patriae pietatis imago`: n takes it as Aeneas's love for Anchises, with the alternative (his love for his son) mentioned.
- 874 `enim` taken in the old asseverative sense ("indeed").
- 876 half-line; scanner flags it UNRESOLVED (expected for a half-line) — for the scan-fixes pass, not this one.

## Advisory
None added. Two deaths by the sword (Lausus 815–820, Mezentius 907–908) and a horse killed; described plainly, no lingering gore beyond the blood in the tunic and the "streaming gore" of the last line. Per conventions ("Book X–XII battle narrative: ordinary killing earns nothing") no trigger fires. Mezentius's death is a consented-to death by the enemy's sword, not a suicide in the Dido sense; I did not treat it as triggering anything, but the owner may want to look.

## Attributions from memory, unchecked
- IX.446–449 (apostrophe to Nisus and Euryalus)
- Iliad 16.856–857 and 22.362–363 (soul lamenting its fate as it goes to Hades)
- Lucretius 1.123 (*simulacra modis pallentia miris*)
- I.378 (*sum pius Aeneas*)
- X.495–500 (Turnus takes Pallas's belt); X.505–506 (Pallas carried back on his shield)
- XI.688–689 (Camilla: to fall by Camilla's weapon as consolation)
- Iliad 18.23–24 (Achilles pours dust on his head); Iliad 22.414 (Priam in the dung)
- VIII.481–495, VIII.494–495 (Mezentius expelled; people demand his punishment); VII.648 (*contemptor divum*)
- Iliad 17.426–440 (Achilles' horses weep); Iliad 19.400–403 (Achilles addresses Xanthus and Balius); Iliad 8.185–197 (Hector addresses his horses)
- XII.666–668 (same lines as 870–872, of Turnus)
- VIII.608–731 (the shield of Aeneas)
- Iliad 8.81–86 (Paris's arrow kills Nestor's trace-horse)
- Iliad 22.338–343 (Hector's plea for burial)
- 785–786 (Mezentius's wound, previous part) — from 080's notes; not re-checked.
