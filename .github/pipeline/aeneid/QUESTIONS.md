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
