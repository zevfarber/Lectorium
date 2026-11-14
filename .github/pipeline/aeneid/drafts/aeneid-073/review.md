# Review — aeneid-073 (Aeneid X.96–184), adversarial reviewer

**Severity counts: major 12, medium 5, low 29 (27 in pass 1, 2 in pass 2). Refused or upheld-without-change findings: 20. Scan-fixes entries added: 12 (all wrong full lines; no half-lines, no carriers).**

I reviewed this part in two passes.

**Pass 1** covered all 43 units word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every elision list, every "framing" claim, every cross-reference and every attribution made from memory. I also checked:
- the drafter's misprint call at 10.113 (`invenient. ”Stygii`), its handling against the 071 precedent (9.781), and looked for other misprints
- the Latin Library variants
- the speech marks
- the drafter's doubtful points (10.129 *Menestheo*, 10.109–110, 154 *libera fati*, 167, 184)
- the no-advisory decision
- `about`, the title and the part names

I read every `i` for echoes of the well-known English versions.

I worked from the Latin, the pinned source and memory of the public-domain reference works (Lewis & Short, Allen & Greenough, Greenough's notes, Conington). No translation was opened and nothing was searched.

I checked the in-poem cross-references against the pinned source, and all are right:
- 1.121 (*et qua vectus Abas*), 1.183 (*aut Capyn*)
- 3.250 (*Accipite ergo animis atque haec mea figite dicta*, identical to 10.104: added to the note, L4)
- 7.1 (*Aeneia nutrix*, used for the scansion of *Aeneia* at 156)
- 7.641 (*Pandite nunc Helicona, deae, cantusque movete*, identical to 10.163)
- 8.479–480 (Agylla/Caere, the Lydian settlers), 8.502–503 (the oracle: *externos optate duces*; *tum Etrusca* with long *Ē-*, used at 180)
- 9.104–106 (= 10.113b–115, Jupiter's oath to the Mother of the Gods)
- 9.779–781 (Mnestheus at the rally; the 9.781 misprint precedent)
- 5.100 (*quae cuique est copia*, disyllabic *cuique*, used at 107)
- the in-part references to 111, 133 and 148

**Pass 2** re-read every edited field in full, re-checked speech marks, line counts and note lengths, and made two more changes (P2-1, P2-2).

**Scansion.** I hand-scanned all 89 lines. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story` (with each unit's `ln`), and compared its output with mine syllable by syllable. The helper is `drafts/aeneid-073/scan_check.py` (072's, with the part id changed).
- **The packet's flag.** 136 (COSTLY 2.0) is wrong: *buxo aut* is a hiatus at the caesura, not an elision (M5).
- **Eleven more lines are wrong without a packet flag:** 105, 107, 109, 123, 141, 147, 156, 157, 159, 165, 179.
  - Initial *Ae-*: *Aeneas* 147, 159; *Aenean* 165 (quantities); *Aeneia* 156 (with a hiatus).
  - Consonantal *i* after a prefix: *coniungi* 105, *subiuncta* 157.
  - Hiatus: 136 *buxo aut*, 141 *domo, ubi*, 156 *duci. Aeneia*.
  - *cuique* made three syllables: 107.
  - Wrong quantities with no special feature: 109 (*fātīs*, *Ĭtălum*), 123 (*Hĭcĕtāŏnius*).
  - Synizesis plus hiatus where the line has an ordinary elision: 179 (*Alphe(ae) ab*).
- **No carriers are needed:** every unresolved or wrong line is entered, and no unit was left without `sc`.

Every new `scan-fixes.json` entry was checked by script (`drafts/aeneid-073/add_scan_fixes.py`):
- against the build's word-match rule (`strip(sc) == WORD_RE.findall(line)` for the line as printed)
- against the validator's metre rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet, then –×/⏑×
- against its own `why`: each `why` gives a syllable count, and the script checked it.

I then ran a replica of the build's scansion step, reading the fixes from `scan-fixes.json` itself:
- all 12 entries apply (keys `10.n`)
- **all 43 units get `sc`**
- every unit's `sc` lines up with its words
- all 89 lines pass the validator's metre check
- the scanner report is empty (no UNRESOLVED, MISMATCH or COSTLY left)

**What was edited, and how.**
- **Scripts.** `units.json` was edited only by Python scripts: `review_edits.py` for pass 1 (32 edits) and `review_edits_pass2.py` for pass 2 (2 edits). Each old string was asserted to occur exactly once in its field. The file is written with `aeneid_lib.jdump`; a round-trip of the drafter's file through `jdump` was byte-identical before any edit.
- **Untouched fields.** `t`, `ln`, `p` and `v` are as the drafter left them in all 43 units (checked by script against a copy taken before any edit). `title`, `titleEn`, `part` and `about` are unchanged. No unit boundary was changed.
- **21 units changed:** 2, 3, 5, 6, 7, 10, 11, 12, 13, 15, 19, 20, 21, 22, 27, 29, 31, 34, 38, 39, 40.
- **Layout checks.** `l` has the same number of lines as `t` in every unit, and no `i` has a line break.
- **Speech marks.** `t`, `l` and `i` each have 1 “ and 1 ”, on the same units: Jupiter 3 (104) / 10 (113).
- **Note lengths.** The notes run 43–113 words, under the validator's 140.
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- **`scan-fixes.json`.** The diff only appends: 130 insertions, 0 deletions, trailing newline kept, formatting unchanged (`json.dumps(indent=1, ensure_ascii=False)`; a round-trip of the old file was byte-identical before appending). The new keys follow 10.90, in line order.
- **Build and validator not run.** `build_aeneid.py` has no dry-run mode, so its scansion step and the validator's metre and `sc`-alignment checks were replicated instead.

## Changes — pass 1

### Major (scanner wrong; each now has a scan-fixes entry)
- **M1. 10.105, *coniungi* (COSTLY 1.5, unflagged).** The scanner read *co-ni-un-gi*, with short *co-*. Right: Quan-dŏ-quĭ | d(em) Au-sŏ-nĭ | ōs con | iun-gī | foe-dĕ-rĕ | Teu-cris (15).
- **M2. 10.107, *cuique* (COSTLY 0.6).** The scanner made *cuique* three syllables (15). It is two, as at 111 and 5.100 (*quae cuique est copia*): quae cui | qu(e) est for | tū-n(a) hŏ-dĭ | ē quam | quis-quĕ sĕ | cat spem (14).
- **M3. 10.109 (unflagged).** The count is right but the quantities are not: the scanner made *fātīs* short-short and *Ĭtă-* long-long. Right: Seu fā | tīs Ĭ-tă | lum cas | tr(a) ob-sĭ-dĭ | ō-nĕ tĕ | nen-tur (15). Short *Ĭtălum* as at 10.41.
- **M4. 10.123, *Hicetaonius* (COSTLY 1.5).** The scanner lengthened *Hi-ce-* and ran *-nius* together (16). Right (Greek Ἱκετάων): Ā-sĭ-ŭs | Im-bră-sĭ | dēs Hĭ-cĕ | tā-ŏ-nĭ | us-quĕ Thy̆ | moe-tes (17), five dactyls.
- **M5. 10.136 (flagged COSTLY 2.0).** The scanner elided *buxo*, lengthened *-ri-* of *Oricia* and *te-re-* (13). Right, with hiatus at the main caesura: in-clū | sum bux | ō aut | Ō-rĭ-cĭ | ā tĕ-rĕ | bin-tho (14).
- **M6. 10.141, *domo, ubi* (COSTLY 1.0).** The scanner elided *domo* and lengthened *ge-ne-* and *do-*. With the elision no fit exists under natural quantities. Right, with hiatus: Mae-ŏ-nĭ | ā gĕ-nĕ | rō-sĕ dŏ | mō ŭ-bĭ | pin-guĭ-ă | cul-ta (17).
- **M7. 10.147, *Aeneas* (COSTLY 1.2).** The scanner split *Ae-* (17). Right: con-tŭ-lĕ | rant mĕ-dĭ | (a) Ae-nē | ās frĕ-tă | noc-tĕ sĕ | cā-bat (16).
- **M8. 10.156, *duci. Aeneia* (COSTLY 1.0).** The scanner elided *duci* and lengthened *commissă* and *dŭ-*. Right, with hiatus across the full stop (as *colo. Huc*, 5.735) and *Aenēĭa* as at 7.1: ex-ter | nō com | mis-să dŭ | cī Ae | nē-ĭ-ă | pup-pis (14).
- **M9. 10.157, *subiuncta* (unflagged).** The scanner read *su-bi-unc-ta* (16). Right: prī-mă tĕ | net rōs | trō Phry̆-gĭ | ōs sub | iunc-tă lĕ | ō-nes (15).
- **M10. 10.159, *Aeneas* (COSTLY 1.2).** The scanner split *Ae-* (15). Right: Hic mag | nus sĕ-dĕt | Ae-nē | ās sē | cum-quĕ vŏ | lū-tat (14).
- **M11. 10.165, *Aenean* (COSTLY 0.6).** The count is right but the quantities are wrong: the scanner made *-ne-an* short and *-que ra-* long. Right, as 10.65: Ae-nē | ān ar | met-quĕ ră | tēs pĕ-lă | gō-quĕ vĕ | hā-tur (15).
- **M12. 10.179, *Alpheae ab* (COSTLY 1.5).** The scanner got the same feet by synizesis of *-eae* with *ab* left in hiatus. The entry gives the ordinary elision the note states: Hōs pā | rē-rĕ iŭ | bent Al | phē(ae) ăb ŏ | rī-gĭ-nĕ | Pī-sae (15).

### Medium
1. **Note 135b–137a, boxwood.** The note called boxwood and terebinth "both dark" woods. Boxwood is pale yellow. The note now reads "both close-grained woods, boxwood pale yellow and terebinth dark, against which the white ivory shows bright".
2. **Note 135b–137a, hiatus.** The note listed "Elision 'bux(o) aut'". It is a hiatus (M5). The note now says so and reads "No elisions".
3. **Note 137b–138, *subnectens circulus*.** The note made the circlet a second subject of *accipit* and then glossed it as "the neck takes both the hair and the band", which makes the band the object. The note now reads "the neck and the circlet both receive the hair, the circlet binding it up".
4. **Note 139–142, *domo, ubi*.** It was listed as an elision. It is a hiatus (M6), and the note now says so.
5. **Note 156b–158, *duci. Aeneia*.** It was listed as "Elision across the start of the unit". It is a hiatus across the full stop (M8), and the note now says so.

### Low
- **L1. `l` 101b–103.** "trembling" for the passive *tremefacta* is now "made to tremble from its base".
- **L2. Note 101b–103.** "supply 'est'" now adds "or take 'tellus' as a second subject of 'silescit'". Both construals are current.
- **L3. Note 101b–103.** "hushed before the king of the gods speaks" did not match *eo dicente*. It is now "as".
- **L4. Note 104.** Added: "The whole line repeats III.250, where the Harpy Celaeno begins her prophecy" (checked in the edition).
- **L5. Note 107–108.** Added "'cuique' is two syllables, 'cui-' one, as at 111", to match M2.
- **L6. `i` 109–110.** "warnings misread" committed to one reading that `l` and `n` leave open. It is now "ill-starred warnings".
- **L7. Note 111a.** "will get no special favour from the consequences of their acts" was muddled. It is now "are not released from the consequences of their acts".
- **L8. `l` 113–115.** "By the Stygian streams of his brother" attached *Stygii* to the streams. It agrees with *fratris*, so the line is now "By the streams of his Stygian brother".
- **L9. Note 113–115, misprint.** The 5b sentence now has 071's form: "corrected here: the closing mark is joined to the next word (as at IX.781); t keeps the print." The single quotes follow 054/071.
- **L10. Note 116a.** *Hic finis fandi* is not a half-line, because line 116 is complete. It is now "A brief formula closing the speech, filling the first half of the line".
- **L11. `l` 116b–117.** "From his throne then Jupiter golden" made Jupiter golden. It is now "From his golden throne then Jupiter".
- **L12. Note 116b–117.** *Solio… aureo* does not frame the line. It now reads "enclosing 'tum Iuppiter'".
- **L13. `l` 118–119.** "at the gates around, all of them" could be read of the Rutulians. It is now "at all of them".
- **L14. Note 121b–125a.** "two men named after Assaracus" is an inference. It is now "two men who bear the name of Assaracus".
- **L15. Note 121b–125a.** Added "'Hicetaonius' is Hi-ce-ta-o-ni-us, six syllables", to match M4.
- **L16. `l` 132–135a.** "his head uncovered, his handsome head" gave *caput* twice. It is now "his handsome head uncovered".
- **L17. Note 135b–137a.** "a port in Epirus, known for the terebinth" was softened to "a port on the coast of Epirus". Virgil's own epithet is the only evidence I can vouch for.
- **L18. `l` 137b–138.** *cui* was not rendered. The line is now "whose flowing locks the milk-white neck / receives, and, binding them beneath, a circlet of pliant gold."
- **L19. Note 137b–138.** *fusos… crinis* does not frame "the rest of the line". It now reads "enclosing 'cervix cui lactea'".
- **L20. Note 139–142.** *magnanimae… gentes* does not frame the line. It is now "enclosing 'viderunt, Ismare'". "both armies saw him" was softened to "the peoples who watched him fight".
- **L21. `l` 148–150a.** *quidve… quidve* was "and what… and what", although the note glosses *-ve* as "or". It is now "or what… or what".
- **L22. `i` 153b–154a.** "there was no delay; Tarchon joins" mixed tenses. It is now "there is no delay".
- **L23. Note 156b–158.** Added "'subiuncta' is sub-iuncta, the i a consonant", to match M9.
- **L24. Note 166.** *aerata… tigri* does not frame the line, because *Massicus* comes first. It now reads "enclose 'princeps secat aequora'".
- **L25. Note 172–174.** "'mines like the Chalybes''" was garbled. It is now "'with the Chalybes' metals', iron mines like theirs".
- **L26. Note 175–178.** The elision list left out *atqu(e) horrentibus*. Added.
- **L27. Note 179–180a.** Added "'Etrusca' has a long first syllable here, as at VIII.503 (short at 148)". This is the metre's only fit, and the scanner already has it.

## Changes — pass 2
- **P2-1. Note 135b–137a.** "ivory set into dark wood" contradicted the Medium 1 correction. It is now "ivory set into wood".
- **P2-2. Note 135b–137a.** "stays long at the pause in mid-line" now reads "stays long at the main caesura", matching the 10.136 entry.

## Scan-fixes entries added (12)
| key | reason | syllables |
|---|---|---|
| 10.105 | *coniungi*, consonantal i after a prefix | 15 |
| 10.107 | *cuique* two syllables | 14 |
| 10.109 | *fātīs*, *Ĭtălum* (quantities) | 15 |
| 10.123 | *Hĭcĕtāŏnius* (quantities, no synizesis) | 17 |
| 10.136 | hiatus *buxo aut* (packet flag) | 14 |
| 10.141 | hiatus *domo, ubi* | 17 |
| 10.147 | *Aeneas*, initial Ae- | 16 |
| 10.156 | hiatus *duci. Aeneia*; initial Ae- | 14 |
| 10.157 | *subiuncta*, consonantal i after a prefix | 15 |
| 10.159 | *Aeneas*, initial Ae- | 14 |
| 10.165 | *Aenēān* (quantities) | 15 |
| 10.179 | *Alphe(ae) ab*, elision, not synizesis + hiatus | 15 |

## Hand-scan notes on the special lines (scanner right, no entry)
- **120 *Aeneadum***: At lĕ-gĭ | (o) Ae-nĕ-ă | dum val | lis ob | ses-să tĕ | nē-tur. *Ae-* is one syllable and *-nĕ-* is short (*Aenĕadae*). Right.
- **129 *fratre Menestheo***: nec Cly-tĭ | ō gĕ-nĭ | tō-rĕ mĭ | nor nec | frā-trĕ Mĕ | nes-theo (16), with *-theo* in synizesis. This is right for Greenough's reading, and it agrees with the drafter's note. The reading *Mnestheo* would need *frātrē Mnēstheō*, a spondaic fifth foot with *-e* lengthened before *mn*. That is a further reason the print may be sound; see the questions below.
- **143 *Mnestheus*** (COSTLY 1.5): Ad-fŭ-ĭt | et Mnes | theus quem | pul-sī | prīs-tĭ-nă | Tur-ni. Right. The scanner prints no ‖, but the validator does not require one.
- **148 *Euandro*** (COSTLY 1.5): *Eu-* is one syllable. Right. **158 *Teucris***: right.
- **127 *conixus***: *cō-nī-xus*. The *i* is a vowel (from *nitor*), not a consonantal *i*. Right.
- **182 *adiciunt***: *ā-dĭ-cĭ-unt*, with the first syllable long (as *adiiciunt*). Right, and it agrees with the note.
- **130 *Hi iaculis***: the *i* of *iaculis* is consonantal, so there is no hiatus. Right.
- **116 *aureo*** (two syllables) and **101 *eo*** (two syllables): right. **180 *urbs Etrusca***: *Ē-* must be long (no other fit; cf. 8.503). The scanner has it.
- **169 *gorytique***: *gō-rȳ-tī-*, the only fit. Right.

## Refused or upheld findings
1. **10.113 misprint `invenient. ”Stygii` (upheld).** It is handled as at 9.781 (071): `t` keeps the print; `l` and `i` close the speech after "find."; the note opens with the 5b sentence (now in 071's exact form, L9). There is only one way to read it, so it is a clear misprint, not a doubtful reading.
2. **No other misprints.** I checked the capitals after stops, the closing mark at 113, and Greenough's spellings (*adsensu*, *adnuit*, *adfuit*, *adfixus*, *volnera*, *moerorum*, *inrigat*, *divom*, *Tercentum*, the *-is* accusatives *torrentis* and *crinis*). Upheld.
3. **10.129 *Menestheo* (upheld as printed).** The Latin Library agrees with Greenough. It scans with synizesis. The note neither identifies this brother with the Mnestheus of 143 nor denies it. I did not add the alternative reading *Mnestheo* to the note, because I cannot check which editors print it. It goes to the owner.
4. **Latin Library variants.** All are orthographic (*volnera/uulnera*, *dirigere/derigere*, *moerorum/murorum*, *divom/diuum*, *Tercentum/ter centum*) except the name *Astur/Astyr*. The name is noted as the same man, which is correct and harmless. Upheld.
5. **10.109–110, "It is all one whether…"** The supplied main thought is the usual way of taking the *seu… sive* clause. Upheld (only the `i` wording of *monitis sinistris* changed, L6).
6. **10.154 *libera fati*** as "freed from the bar of fate" (the oracle of 8.502–503). Upheld; the edition confirms the oracle.
7. **10.184 *intempestae*** as "unwholesome / fever-ridden", following the old explanation. Upheld, and the note says "explained of old".
8. **10.167 *mille manus iuvenum*** as "a band of a thousand young men". Upheld.
9. **10.107 *secat spem*** as "follows a hope's path". Upheld.
10. **10.104 *animis*** as a local ablative. A dative ("into your minds") is also possible, but the label is defensible. Upheld.
11. **10.143 *pristina*** as "former, recent but already past". Upheld. (L&S also gives "of the day before", which would sharpen it, but the note is not wrong.)
12. **Note 96–99, Georgics 1.356–359** as the weather-sign parallel (*nemorum increbrescere murmur*). Upheld.
13. **Note 113–115, Iliad 1.528–530** (Zeus's nod shakes Olympus). Upheld.
14. **Note 127–129, Iliad 5.302–304** (Diomedes' stone that two men of today could not carry). Upheld.
15. **Note 163–165, Iliad 2.484–493** (the invocation before the Catalogue of Ships). Upheld.
16. **Hicetaon as Priam's brother** (Iliad 20.238, among the elders at 3.147); **Sarpedon killed by Patroclus** (Iliad 16). Upheld.
17. **Geography and myth:**
    - Capua from Capys
    - Etruscan Pisa from Pisa in Elis
    - the Pactolus' gold
    - the Chalybes as iron-workers
    - Elba's iron
    - Populonia facing Elba
    - Caere as Mezentius's city
    - Pyrgi as Caere's port
    - the Minio as a river of southern Etruria
    - the Etruscans as Lydians

    Upheld as standard. The one claim I could not vouch for (Oricum "known for the terebinth") was softened (L17).
18. **Echo check.** *Fata viam invenient* → "The fates will find a way" is the stock rendering of a proverbial tag. Like "father of the gods and king of men" in 072, it is not a distinctive echo. No other `i` line echoes a known English version. Upheld.
19. **Speech marks** (“ 104 / ” 113, one speech). They agree in `t`, `l` and `i`. Upheld.
20. **Advisory: none (upheld).** There is siege fighting, but no killing on stage in this stretch.

## For the owner (QUESTIONS.md)
- **10.129 *fratre Menestheo* (doubtful reading, kept as printed).** Many texts are said to read *Mnestheo*. Is the brother the Mnestheus of 143? I have not verified which editors print what. The print scans (*Me-nes-theo*, synizesis). *Mnestheo* would need a spondaic fifth foot. Left as printed, with no identification in the note.
- **Misprint (rule 5b):** 10.113 *invenient. ”Stygii* for *invenient.” Stygii*. `t` keeps the print.
- **Hiatus lines entered as hand scansions:** 136 (*buxo aut*, at the caesura), 141 (*domo, ubi*), 156 (*duci. Aeneia*, across the stop). Each is the only fit under natural quantities. I recall 136 and 141 being cited as Virgilian hiatus, but have not checked a commentary.
- **10.179** was entered although the scanner's feet were right, because its analysis (synizesis of *-eae* with *ab* in hiatus) contradicts the elision the note states, and the audio reads elision from `sc`.
- **Unchecked attributions from memory:** Georgics 1.356–359; Iliad 1.528–530, 2.484–493, 5.302–304, 16 (Sarpedon), 20.238 / 3.147 (Hicetaon); the Capys–Capua, Pisa–Elis, Populonia and Minio facts.
- **Advisory:** none taken.
