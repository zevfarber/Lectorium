# Aeneid — questions for the owner

Open:

1. **Approve the pilot?** aeneid-001 (I.1–101) is live. If approved, add `aeneid` to `.github/pipeline/queue.txt`
   (after `beowulf`, or wherever you want it) and the shared routine continues the poem from aeneid-002.
2. **Edition: Greenough (1881), not Hirtzel (1900).** Hirtzel could not be fetched (no reachable machine-readable
   copy). Greenough is the Perseus text and public domain. Meanwhile: proceeding on Greenough. Switching later means
   re-archiving and re-issuing published parts.
3. **Audio for the pilot.** Pushing a new Latin part does not build its audio; the daily sweep reaches the Aeneid only
   after the Odyssey, Igor, Aesop and all of Ovid (none of Ovid has audio yet either). A single *Build audio* dispatch
   with id `aeneid-001` would make it now (≈35k characters of SSML plus word clips; inside the $10/month budget).
   Meanwhile: left to the sweep.
4. **Library sub-grouping.** Aeneid entries carry `group: "Book I"` etc. (as the Odyssey does), so once there are
   several parts the text picker shows them under book headings. Ovid's entries have none. Meanwhile: kept.
5. **Dido's suicide (Book IV)** is not covered by any content-advisory trigger (the same gap noted for Ovid).
   Meanwhile: no advisory unless a trigger fires; to be decided before aeneid-030 (IV.607–705), where her death falls.

6. **I.203 set piece decided by the run.** The conventions asked for a dedicated pass before the batch reaching I.203; the unattended run built it from the Latin, rephrased away from known versions, and recorded it in the house-renderings table. Meanwhile: published as is; change it if you prefer another.
7. **Glossary `genitor`.** The broadened entry keeps the old "here Neptune" reading whole, per the broadening rule; the new reading (Jupiter, voc.) is appended.

8. **I.462 set piece decided by the run (aeneid-005).** As with I.203 (item 6): built from the Latin alone, rephrased away from known versions, added to the house-renderings table. The reviewer could only check against remembered versions. Meanwhile: published as is; change it if you prefer another.

9. **Half-lines.** Greenough prints ~58 half-lines (first: 1.534, 1.560). Meanwhile: each is hand-scanned in scan-fixes.json with a reason starting "Half-line", and validate_aeneid.py accepts such lines (fewer than six numbered feet, one × mark). Tell me if you want them treated differently.

10. **Doubtful quantities (aeneid-008).** 1.663 hand scansion needs Ergo not elided before his; 1.682 needs -us long before elided -ve; 1.703 intus, 1.733 huius, 1.693 amaracus each need a long syllable the references did not confirm. Meanwhile: kept the only parse that fits; revisit if you know otherwise.

11. **II.49 set piece decided by the run (aeneid-009).** Built from the Latin alone, rephrased away from known versions, added to the house-renderings table. Meanwhile: published as is; change it if you prefer another.

12. **Scansion not confirmed (aeneid-012).** 2.288 gemitus (scanner marks ge/mi long) and 2.325 Dardaniae/Troes (scanner splits ae and reads Troes as one syllable) are published on the scanner's fit; the reviewer could not settle them from public-domain sources. Audio quantities may be off there. Meanwhile: kept; revisit if you know otherwise. 2.339 Rhipeus rests on a long Rhi, also unconfirmed.

13. **Doubtful quantities (aeneid-013).** 2.433 long *si*, 2.419 long *i* in *imo*, 2.447 *iam*, 2.449 *imas*, 2.468 (half-line) long final -a of *interea* and lengthened *sat*, 2.417 short E- in *Eois* (cf. 1.489 long), and *Rhi-* long (as at 2.339) rest on the only fit found, unconfirmed. Meanwhile: kept; revisit if you know otherwise.

14. **Check merentis (aeneid-014, 2.585–586).** Read as acc. pl. of the participle merens agreeing with *poenas* ("deserved punishments"); the genitive-singular alternative is named in the note. Meanwhile: published as is.

15. **2.563 Iuli (aeneid-014).** The aeneid-015 review found Iulus/Iulum scan as three syllables (Ĭ-ū-lus) with a dactylic fifth foot (cf. 1.556, 1.690); aeneid-014 published 2.563 with a spondaic fifth foot and consonantal I. Meanwhile: left; a scan-fixes entry would apply on a rebuild of 014.

16. **Scansion not confirmed (aeneid-016).** 2.745 scans only with *deo* as one short syllable (synizesis); 2.787 is treated as a half-line (11 syllables; on the traditional list of Book II hemistichs, not sourced in the pipeline); long -bi of *tibi*/*ibi* (704, 784, 792), *Lydius* (781), *asylo* (761), *donec* (719), *e tanto* (718), *iuxta* (714), *gaza* (763) rest on the only fit found. Meanwhile: kept; revisit if you know otherwise.

17. **Scansion not confirmed (aeneid-017).** 3.74 (`Neptuno Aegaeo` unelided, long i of Nereidum) and 3.97 (`domus Aeneae` unelided, after 1.617) are hiatus fits, the only parse found; 3.41 `Quid miserum, Aenea, laceras?` has no hexameter under natural quantities (published on the scanner's fit); long -a of `iuxta` (22), `radicibus` (27), long -o of `meo` (18), short -es of `Thraces` (14) rest on the only fit found. Meanwhile: kept; revisit if you know otherwise.

18. **Scansion not confirmed (aeneid-018).** 3.108 `Rhoeteas` is hand-scanned Rhoe-tē-as (long te, Greek ει); 3.163 `Grai` (two long syllables) and 3.168 `Iasius` (long Ia- and si; Ī-ă-sĭ-us also fits) are on the scanner's COSTLY fits. Meanwhile: kept; revisit if you know otherwise.

19. **Scansion not confirmed; misprint (aeneid-019).** 3.209 final -dum of `Strophadum`, 3.211 `insulae Ionio` (scanner fit kept), 3.213 `liquere` long li-, 3.272 `Laërtia` with diaeresis, 3.277 `prora` before consonantal i, 3.295 long `Pri-` rest on the only fit found. 3.286 prints `clipeum.` where a comma is meant (rule 5b): the reading text has the comma, the note says so, `t` stays as printed because the checks require it. Meanwhile: published as is.

20. **Punctuation and speech marks (aeneid-020).** 3.315: Greenough prints a closing ” at 319 but no opening “ before Aeneas's reply; the reading text supplies it, `t` stays as printed (rule 5 would instead add the mark to the source and re-pin — tell me if you prefer that). 3.391 prints `iacebit.` where a comma is meant (rule 5b): reading text has the comma, `t` as printed. Meanwhile: published as is.

21. **Scansion not confirmed (aeneid-020).** 3.308 `deriguit` long -it in arsis; 3.311 `si` before `lux`; 3.316 initial `ne` long; 3.317 `te` long; 3.335 `Cha-` long and elided n'ā long; 3.354 `aulaï` final long; 3.365 `Harpyia` with long py- (consonantal i; 019 has four syllables Har-pў-ĭ-ae); 3.393 `requies`; 3.396 `Italique` short I vs long I at 3.364. 3.340 is a half-line deliberately not completed. Seven notes exceed 140 words (WARN). Meanwhile: kept; revisit if you know otherwise.
