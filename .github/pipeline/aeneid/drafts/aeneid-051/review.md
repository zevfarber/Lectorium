# Review — aeneid-051 (Aeneid VII.195–285), adversarial reviewer

I reviewed this part in two passes.

**Pass 1** covered all 39 units, word by word. I checked `l`, `i` and `n` against the Latin, every grammatical label, every cross-reference and every historical or mythological claim. I also checked the speech marks, the rule-5b misprint decisions (7.197, 7.254, 7.259, 7.267, 7.274), the doubtful comma at 7.216, the two Latin Library variants that matter (7.207 *penetravit*/*penetrarit*, 7.266 *illi*/*pars mihi*), and every `i` for remembered English. I worked from the Latin, the pinned source and memory of the public-domain reference works. No translation was opened. Every in-poem cross-reference was checked against the pinned source:
- 1.521–558 (Ilioneus before Dido), 1.544–545 (*nec pietate… nec bello maior et armis*), 1.565 (*quis Troiae nesciat urbem*), 1.572–574 (Dido's offer), 1.647–655 (gifts from Troy)
- 3.96 (*antiquam exquirite matrem*), 3.167 (*hinc Dardanus ortus*, the Penates), 3.170 (*Corythum*), 3.707–711 (Anchises dies at Drepanum)
- 7.47–48 (Faunus father of Latinus), 7.64–80 (bees, Lavinia's hair), 7.81–101 (Faunus's oracle at Albunea; 98–99 *qui sanguine nostrum / nomen in astra ferant*, word for word), 7.128, 7.150 (Numicus), 7.153–154 (hundred envoys, olive boughs), 7.286–289 (Juno from Argos)
- 8.319–325 (Saturn in Latium; 8.322 *legesque dedit*, see item 21)

**Pass 2** re-read every edited field in full and made one more change (P2-1).

**Scansion.** I hand-scanned all 91 lines by quantity. I then ran the scanner in-process, the way `build_aeneid.py` calls `SL.scan_story`, and compared it with my scansion syllable by syllable. Every new `scan-fixes.json` entry was checked against a replica of the build's word-match rule (`strip(sc) == WORD_RE.findall(line)`) and the validator's rule: six feet, 12–17 syllables, one ×, five –⏑⏑/–– feet and a sixth –×/⏑×. The half-line 248 (its `why` begins "Half-line") was checked against the validator's hemistich rule instead (feet 1..k, k < 6, one ×), in the format of 7.129. Each `why` gives a syllable count, and a script checked that count against its entry. A replica of the build's scansion step with all fixes applied gives an empty scanner report (both COSTLY flags and both UNRESOLVED lines cleared), and every line passes the validator's check.

**What was edited, and how.**
- `units.json` was edited by Python script. Each old string was asserted to occur exactly once in the named field.
- `t`, `ln`, `p` and `v` were checked unchanged in all 39 units, by script against a copy taken before any edit. `title`, `titleEn`, `part` and `about` are unchanged.
- `l` still has the same number of lines as `t` in every unit, and no `i` has a line break.
- No note is over 140 words (longest: units 8 and 11, 134 each).
- **`make_units.py` was not touched.** It still holds the drafter's strings, so re-running it would undo this review. Build from `units.json` as it stands.
- The diff to `scan-fixes.json` only appends: 202 insertions, 0 deletions, trailing newline kept.

**Speech marks.** Latinus, 195–211: “ on the first unit (*Dicite*), ” on the last (after *auget.*). Ilioneus, 213–248: “ on *Rex*, ” after *vestes.* Latinus, 259–273: “ before *Di*, inside the unit that opens with the narrative *tandem laetus ait:*, and ” after *opto.* All three layers have 3 “ and 3 ”. Nothing was changed.

**Severity counts: major 11, medium 9, low 20 (19 in pass 1, 1 in pass 2). Refused findings: 20. Scan-fixes entries added: 18.**

## Changes — pass 1

### Major
1–11. **Scansions the scanner got wrong with no flag.** Each line fit six feet, so nothing warned, but the quantities were wrong. Each line now has a hand entry.
   - **7.196 *auditique advertitis***: the scanner made *audĭtĭ* short and *advertītīs* long. Hand scansion: ēt gĕ-nŭs | au-dī | tī-qu(e) ad | ver-tĭ-tĭs | ae-quŏ-rĕ | cur-sum.
   - **7.223 *ierit***: the scanner read the i as a consonant (two syllables). Hand scansion: tem-pes | tās ĭ-ĕ | rit cam | pōs quĭ-bŭs | ac-tŭs ŭ | ter-que.
   - **7.226 *summovet oceano et***: the scanner made *-mo-* and *-vet* long and *O-* short, and elided *oceano*. With natural quantities (*summŏvet*, *Ōcĕănō* as at 1.287, *sī*) there is no fit unless *oceano* stands in hiatus at the caesura. Hand scansion: sum-mŏ-vĕt | Ō-cĕ-ă | nō et | sī qu(em) ex | ten-tă plă | gā-rum. This is the only fit (see the doubtful list).
   - **7.234 *Aeneae***: the scanner split Ae-. Hand scansion: Fā-tă pĕr | Aē-nē | ae iū | rō dex | tram-quĕ pŏ | ten-tem.
   - **7.238 *adiungere***: the scanner read the i as a vowel (a-di-un-ge-re) and made *ad-* short. Hand scansion: ēt pĕ-tĭ | ē-rĕ sĭ | b(i) ēt vŏ-lŭ | ē-r(e) ad | iun-gĕ-rĕ | gen-tes.
   - **7.244 *reliquias***: the scanner used synizesis (re-liqu-ias). Hand scansion: mū-nĕ-ră | rē-lĭ-quĭ | ās Trō | (ia) ex ar | den-tĕ rĕ | cep-tas.
   - **7.254 *voluit***: the scanner scanned the misprint (vŏ-lŭ-ĭt). The reading is *volvit*, as the note says, so the line is scanned that way on the printed word (`vol–4uit–`, as the 5.181 *Illum* and 5.514 *vota* entries do): ēt vĕ-tĕ | rīs Fau | nī vol | vīt sub | pec-tŏ-rĕ | sor-tem.
   - **7.263 *Aeneas***: the scanner split Ae-. Hand scansion: Ip-sĕ mŏ | d(o) Aē-nē | ās nos | trī sī | tan-tă cŭ | pī-d(o) est.
   - **7.276 *Teucris***: the scanner split Teu-. Hand scansion: om-nĭ-bŭs | ex-tem | plō Teu | crīs iŭ-bĕt | or-dĭ-nĕ | dū-ci.
   - **7.280 *Aeneae***: the scanner split Ae-. Hand scansion: ab-sen | t(i) Aē-nē | ae cur | rum gĕ-mĭ | nōs-quĕ iŭ | gā-lis.
   - **7.283 *supposita de***: the scanner made *-pō-sī-* long and *-tă* and *dĕ* short. Hand scansion: sup-pŏ-sĭ | tā dē | mā-trĕ nŏ | thōs fū | rā-tă crĕ | ā-vit (*supposita* is ablative with *matre*).

### Medium
12–15. **Scansion: the packet's flags.**
   - **7.208** (COSTLY 2.0): I confirmed the scanner's parse by hand and entered it to clear the flag: Thrē-ĭ-cĭ | am-quĕ Să | mum quae | nunc Să-mŏ | thrā-cĭ-ă | fer-tur. *Threiciam* has four syllables, as *Threïcius* at 6.645.
   - **7.221** (COSTLY 2.0): the scanner read *Tro-ius* and split Ae-. Hand scansion: Trō-ĭ-ŭs | Aē-nē | ās tŭ-ă | nōs ad | lī-mĭ-nă | mī-sit (as at 1.596).
   - **7.241** (UNRESOLVED): *urguet* is two syllables, with the u after g a consonant. Hand scansion: hūc rĕ-pĕ | tīt ius | sīs-qu(e) in | gen-tĭ-bŭs | ur-guĕt Ă | pol-lo. **7.242** is entered as a carrier line (the scanner's own fit, cost 0.0), because it shares the unit and the build gives no `sc` to a unit with an unresolved line.
   - **7.248** (UNRESOLVED): a half-line, Ī-lĭ-ă | dum-quĕ lă | bōr ves | tēs, entered as a hemistich like 7.129. **7.246** and **7.247** are entered as carrier lines (the scanner's own fits, cost 0.0) for the same reason as 242.
16. **Note 219–221, a wrong label**: "Jupiter's name in three cases ('Iove… Iove… Iovis')". *Ab Iove* and *Iove… avo* are both ablative, so there are two cases. It now reads "said three times in two cases (… ablative, ablative, genitive)".
17. **Note 225–227, a wrong label**: "its subject is the 'quis' in 'siquem'". *Quem* is accusative, the object of *summovet*, and cannot be the subject of *audiit*. It now reads "its subject is understood from 'siquem' ('quem' is the object of 'summovet'): '(is) audiit, siquem…'" (see P2-1).
18. **Note and `l` 213–215, a doubtful label**: "'regione viae', 'from the line of our way', is an ablative of separation with 'fefellit'". *Fallo* does not take an ablative of separation. *Regione viae* is "in the line of our course". The note now reads "'in the line of our way', is ablative with 'fefellit'…: nothing misled us on our course" (no sub-label). `l` now reads "nor has a star, in the line of our way, or a shore deceived us:".
19. **Note 280–283, wrong etymology**: "'Daedala'… is from the name of the craftsman Daedalus". It is the other way round: the craftsman is named from the Greek adjective δαίδαλος. Corrected.
20. **Note 280–283, imprecise citation**: "who secretly bred his mares to the divine horses of Laomedon (Iliad 5)". In Iliad 5.265–272 (Diomedes to Sthenelus), the breed is the one Zeus gave Tros for Ganymede. Anchises stole it by putting his mares to those horses without Laomedon's knowledge (λάθρῃ Λαομέδοντος). It now reads "who put his mares to the horses of the breed Zeus gave Tros, without Laomedon's knowledge (Iliad 5.265–272)".

### Low
21. **Note 202–204**: "Evander tells the story in Book VIII (8.319–325)" was attached to "men were just without compulsion". Evander's Saturn *legesque dedit* (8.322). The note adds "though in his version Saturn also gives the Latins laws."
22. **`i` 202–204**: "we are Saturn's people, just not because chains or laws compel us, but…" can be misread as "just not". It now reads "righteous not because chains or laws compel us but of our own free will". This also moves it away from the common English turn "just without laws".
23. **Note 205–208**: "'His ortus… agris'… frames the clause" (it wraps *ut*, not the clause) now reads "goes round 'ut', which stands late in its clause."
24. **Note 209–211**: "'Aurea… regia'… frames the line" (*caeli* ends the line) now reads "spans the line".
25. **Note 209–211**: "he increases" is right for the sense, but the grammatical subject of *accipit et… auget* is *regia*. The note adds "(the subject slides from the palace to Dardanus)".
26. **Note 216–218**: "'Hanc… urbem'… frames the line" (*consilio* stands first) now reads "spans the line".
27. **Note 216–218**: "'Extremo… Olympo' frames 'veniens Sol'" (it frames *veniens Sol aspiciebat*, the whole line) now reads "frames the line".
28. **Note 245**: "'Hoc… auro'… frames the line" (*libabat ad aras* follows) now reads "goes round 'pater Anchises'".
29. **Note 255–258**: "'Totum… orbem' frames the line" (*egregiam et* stand first) now reads "goes round 'quae viribus occupet'".
30. **Note 260–261**: "'Dabitur'… is impersonal, its subject the clause" contradicted itself. It now reads "has for its subject the clause 'quod optas'".
31. **Note 266, an unverifiable alternative cut**: "some take 'illi' as an old genitive with 'tyranni', 'of that prince'" could not be verified. It also leaves *pacis erit* without a person. The note now reads "'Illi' is dative, 'for him', Aeneas, and 'tyranni'… is Latinus himself." The variant sentence (*pars mihi*) is kept.
32. **Note 243–244**: *reliquias* "has four syllables and a long first", to go with the 7.244 fix.
33–39. **Scansion pointers added to notes**, to go with the fixes:
   - *ierit* three syllables (222–224)
   - hiatus after *Oceano* (225–227)
   - *Aeneae* three syllables (234–235)
   - *adiungere* with a consonantal i, and *precantia* three syllables (236–238)
   - *urguet* two syllables (241–242)
   - the line scanned with *volvit* (251–254)
   - *Aeneas* three syllables (263–265)
40. **Note 276–277**: added "'Teucris' is two syllables, 'Teu-cris'."

## Changes — pass 2
- **P2-1 (low)**: in note 225–227, the pass-1 gloss "'he has heard, anyone whom…'" was not English. It now reads "'he has heard (it), whoever there is whom…'".

## Scan-fixes entries added (18)
Appended at the end of `scan-fixes.json`, each with its reason:
- 7.208, 7.221 (packet COSTLY flags)
- 7.241 (UNRESOLVED) with carrier 7.242
- 7.248 (half-line, UNRESOLVED) with carriers 7.246 and 7.247
- 7.196, 7.223, 7.226, 7.234, 7.238, 7.244, 7.254, 7.263, 7.276, 7.280, 7.283 (no flag, wrong quantities)

Each matches its line's words under `WORD_RE`. Each full line has six feet, five –⏑⏑/–– feet then –×, 14–16 syllables and one ×. 7.248 has feet 1–4 and one ×, and its `why` begins "Half-line". In the replicated build all 18 apply, the scanner report is empty, and all 91 lines pass.

## Hand-scan notes on the special lines (scanner right, no entry)
- **Initial Ae-**: *Aeneadae* (284) and *aetherio* (281) are right. *Aeneas*/*Aeneae* at 221, 234, 263 and 280 are fixed.
- **Greek eu**: *Ilioneus* (212) is right, with *-neus* one syllable; so is *Ilionei* (249), with *-nei* one syllable. *Europae* (224) is right. *Teucris* (276) is fixed.
- **Consonantal i**: *adiungere* (238) is fixed. Also right: *Iove*/*Iovis* (219–220; *Ab* long before consonantal I), *Troiam* (233), *Troiane* (260), *Troiaeve* (262), *iungi* (264), *iungere* (268), *iubet* (276), *iugalis* (280), *cuius* (197), *huic* (257).
- **Synizesis**: *deerit* (262) is two syllables, right, and the note says so. *precantia* (237) ends the line as three syllables (*-tia* one), the scanner's fit and the only one (see the doubtful list). *ierit* (223) and *reliquias* (244) are fixed (no synizesis).
- **Hiatus**: only 7.226 (fixed). Every other vowel meeting is an ordinary elision. *fama est* (205), *bello est* (235) and *cupido est* (263) are prodelision.
- **Others checked and right**: *Ăsiae* (224, the continent, short A, as 1.385), *indĕcŏres* (231, from *indecor*), *excēpisse* (233), *ēgēre* (240), *Ī-dae-ās* (207, 222), *Sāturni* (203), *Cŏrythi* (209), *altāribus* (211), *tĭāras* (247), *ālĭpĕdes* (277), *tăpētis* (277), *mŏnīlia* (278), *nŏthōs* (283), *Thybrim et* elided (242). *sublimes* (285) is divided su-bli by the scanner with *su-* long: the quantity is right and the division cosmetic.

## Doubtful quantities and readings entered on the only fit
- **7.226 hiatus *oceano | et*** at the caesura: the only fit with natural quantities. UNCONFIRMED against an edition.
- **7.237 *precantia*** as three syllables (*-tia* by synizesis, or a consonantal i): the scanner's fit, the only one. No entry.
- **7.253 *conubio***: the scanner reads *cōnŭbĭō* (short u). A three-syllable *cōnūbyō* also fits. Handbooks differ on Virgil's *conubium*. The scanner's fit is kept, with no entry.
- **7.254**: the scansion follows the corrected *volvit* on the printed *voluit* (`vol–uit`). If the owner prefers `sc` to scan the print, drop the entry.
- **Long by position before stop and liquid, on the only fit**: *ā-* of *atra* (214, long by nature anyway), *sā-* of *sacra* (242), *ă-* of *agris* in the sixth foot (206).

## Refused findings
- **R1 — misprint 7.197 `petitis ?`**: kept as a rule-5b note, following *Heus !* at 7.116 (aeneid-050). Only the spacing is affected.
- **R2 — misprints 7.259 `tandem`, 7.267 `vos`, 7.274 `haec`**: kept. Each is lowercase after a full stop, the sense allows only a new sentence, and each note opens with the print's reading. (Three in one part: see the owner's list.)
- **R3 — misprint 7.254 `voluit`**: kept, as a misprint for *volvit*. *Voluit* (from *volo*) makes no sense with *sortem*. *Volvens* (251) and *veteris… volvit sub pectore sortem* are the only possible sense. Greenough's own reading must be *volvit*: the Perseus *u*/*v* encoding is the likely source. The meter allows either, so only the sense decides.
- **R4 — 7.216 `urbem,`**: kept as doubtful and not corrected, as the note says. A comma setting off a long fronted phrase is possible in 1881 punctuation.
- **R5 — 7.207 *penetravit***: the note's handling is kept (indicative in a loose indirect question; the Latin Library has *penetrarit*; the sense is the same). Not a sense-changing variant, so no more is needed.
- **R6 — 7.266 *illi* / *pars mihi***: the note's handling is kept: Greenough's reading is translated, and the common reading is given with its sense. Only the unverifiable alternative was cut (item 31).
- **R7 — Ovid, *Met.* 1.90 *sponte sua, sine lege*** (unit 202–204): kept. From memory, 1.89–90 *Aurea prima sata est aetas, quae vindice nullo, / sponte sua, sine lege fidem rectumque colebat*.
- **R8 — Georgics 1.233** (five zones, unit 225–227): kept. From memory, *Quinque tenent caelum zonae* begins at 1.233, and the note says "1.233 and after".
- **R9 — Homer's "backward-flowing" Ocean** (ἀψόρροος): kept.
- **R10 — Circe as the Sun's daughter, Odyssey 10**: kept (Od. 10.138).
- **R11 — "Corythus… usually taken to be Cortona, named in some accounts after its founder, Dardanus's mortal father"**: kept. It is hedged, and it is the Servian tradition.
- **R12 — Dardanus "usually said to have come from Arcadia or Samothrace"**: kept; these are the Greek traditions.
- **R13 — Ilioneus "the eldest of the envoys"**: kept; *maxumus Ilioneus* (1.521).
- **R14 — 7.154 cited for suppliants' fillets**: kept. 154 has the olive boughs (*ramis velatos Palladis*), and the note cites it for the boughs only.
- **R15 — `i` 202–211, 213–248, 259–285 for echoes**: no other distinctive echo found. "Tell me, sons of Dardanus", "he stands rooted to the ground", "champ tawny gold" and "a shore where we shall do no harm" are plain renderings of the Latin.
- **R16 — `l` 222–224 "a storm went plains"**: kept. It shows the interlocking order the note explains, which is house practice for `l`.
- **R17 — "ablative of place" for *solio* (210)**: kept.
- **R18 — *pectoribus* "ablative of place or dative"** (278): kept; both are possible.
- **R19 — `title`, `titleEn`, `part`, `about`**: our own, and the summary is accurate. Unchanged.
- **R20 — *sublimes* syllable division** (285): cosmetic, no entry (as *subiciunt* in aeneid-050).

## For the owner (QUESTIONS.md)
- **Misprints to record (no emend list for the Aeneid)**: 7.197 `petitis ?` → `petitis?`; 7.254 `voluit` → `volvit`; 7.259 `tandem` → `Tandem`; 7.267 `vos` → `Vos`; 7.274 `haec` → `Haec`. In each case `t` is as printed and `l`/`i` give the reading. Three lowercase starts after a full stop in one part may mean the encoding sometimes has a stop where Greenough printed lighter punctuation. Either way the reading text starts a new sentence.
- **Doubtful, kept as printed**: 7.216 the comma after `urbem`.
- **Scansion on the corrected reading**: the 7.254 entry scans *volvit* on the printed word, following 5.181 and 5.514.
- **Doubtful quantities on the only fit**: 7.226 hiatus *oceano | et*; 7.237 *precantia* trisyllabic; 7.253 *cōnŭbio* (scanner's choice between two fits). None was checked against an edition.
- **`make_units.py` is stale**: `drafts/aeneid-051/make_units.py` still holds the drafter's strings; re-running it would discard this review.
- **From memory, worded as attributions**: Ovid *Met.* 1.90; Georgics 1.233; Iliad 5.265–272 (Anchises and the breed of Tros's horses); Odyssey 10 (Circe the Sun's daughter); the Servian Corythus. None was checked against a text in this run.
