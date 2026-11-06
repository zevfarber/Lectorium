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
