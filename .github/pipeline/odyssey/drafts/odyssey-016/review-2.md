# Review 2 — Glossary pass, odyssey-016 (Odyssey 4.219–331)

This pass was split across two agent instances (the first interrupted by an infrastructure
restart before it could write up its findings). This report covers the complete picture:
what the first instance had already fixed, what this instance verified, and what this
instance additionally found and fixed.

## Method

- Read `conventions.md` (glossary section), `units.json` (60 units), `gloss.json` (183 novel
  entries + `__broaden__`), `novel-forms.json`, `known-forms.json`, and the master
  `odyssey-glossary.json`.
- Wrote a small script replicating `odyssey_lib.forms()` (the exact tokenization the build
  script uses: `WORD` regex over `t` fields, lower-cased) to check coverage.
- Built a form→context map for all 386 known forms and all 183 novel forms against every
  line they appear on in this part's `units.json`, and checked each master/gloss entry's
  stated case/number/gender/tense/mood/voice against that context.
- Grepped every unit note (`n`) that mentions "augment" (29 units did) and checked each
  claim against the actual verb's root, principal parts, and the augment rules stated in
  `conventions.md`.

## Coverage check: PASS, clean

- 569 unique word-forms appear in this part's `t` fields (800 tokens total).
- Every one has an entry, either in `gloss.json` (183 novel forms) or the master glossary
  (386 known forms). Zero forms are missing coverage.
- `novel-forms.json` and `known-forms.json` exactly partition the 569 forms: no form is in
  both lists, no form in either list is absent from `units.json`, and no form in
  `units.json` is absent from both lists.
- This confirms the build script will not refuse on missing glossary coverage.

## Work already done by the interrupted first pass (verified, not redone)

1. **Apostrophe style fix**: every English gloss and quoted-Greek gloss in `gloss.json` now
   uses the single typographic `’` (U+2019) exclusively. I scanned the whole file
   programmatically for left curly quotes (`‘`), ASCII apostrophes (`'`), and backticks —
   zero found anywhere, including inside the five `__broaden__` entries. This was a
   systematic, complete fix; nothing was left half-converted.
2. **Five `__broaden__` entries** (οἵ, ἐπὴν, ἐοικότα, δυσμενέων, ἐδήσατο, τοί) — I re-derived
   each from scratch against the actual line(s) where the form is used in this part, and
   independently confirmed all five are correct and genuinely needed:
   - **οἵ** (used twice, ll. 291 and 318): l.291 is the enclitic dative singular pronoun
     "to/for him" (accented because followed by the enclitic τι — confirmed against the
     unit's own note, which correctly reads it as dative); l.318 is the plain relative
     "who" matching the master's existing entry. Both readings needed; broaden is correct.
   - **ἐπὴν** (l.222): master had only "conj. + subj."; here it governs a bare optative
     (μιγείη) in a generalizing conditional with no ἄν/κε — a genuine second reading.
     Correct.
   - **ἐοικότα** (l.239): master had only the masc. acc. sg. participial reading
     ("fitting", ἐοικότα μυθήσασθαι); here it is neuter nom./acc. plural, substantival,
     "fitting things" (ἐοικότα γὰρ καταλέξω). Correct, distinct reading.
   - **δυσμενέων** (used twice, ll. 244 and 318): l.244 is the participle reading already in
     master (masc. nom. sg., "being hostile"); l.318 is the adjective δυσμενής, gen. pl.,
     agreeing with ἀνδρῶν ("of hostile men") — genitive plural of a 3rd-declension -ής
     adjective cannot be confused with the participle's paradigm (which would give
     δυσμενεόντων in the genitive plural), so this really is a distinct homograph. Correct.
   - **ἐδήσατο** (l.309): master had only "bound on (for herself)"; here the subject is
     Menelaus binding on his own sandals — same verb form, needs the masculine reading
     added. Correct.
   - **τοί** (l.328): master had only the nom. pl. pronoun/relative reading; here it is the
     enclitic dative singular "to you" (σοι), written with an accent because it precedes
     another enclitic (τι) — the standard rule that the first of two successive enclitics
     is accented. Correct reading, though see the one polish item below.
   - All six broaden values were checked to contain the old master-glossary text **whole**,
     followed by ` · ` and the new reading, and all are under 230 characters (the longest,
     ἐοικότα, is 223).
3. **Two note (`n`) fixes in `units.json`** made by the first pass are present at ll. 219
   (ἐνόησ’ correctly explained as augmented, with the elision it's easy to mistake for
   correctly separated from the augment question) and one other small correction; I did not
   find any regression from these, and they read correctly in context.

## New findings and fixes made in this pass

### 1. Augment mislabeling — `ἐνέηκε` (l.233 note, and its `gloss.json` entry) — FIXED

This is exactly the documented weak spot ("augment mislabeling in any parse mentioning a
verb's principal parts"). The note at l.233 said:

> "ἐνέηκε, from ἐνίημι, keeps the verb's own long root vowel rather than adding a separate
> augment"

and `gloss.json`'s own entry echoed it:

> "aor. 3 sg., root vowel kept in place of a separate augment"

Both phrasings imply ἐνέηκε has **no** augment. That is wrong, and is directly
self-contradicted two sentences later in the very same note, which correctly calls the
structurally identical form προσέειπεν "the uncontracted, **still-augmented** form" (augment
present but not fused with the following long vowel, because Homer still feels the lost
initial consonant of the root). ἐνέηκε is the same category: ἵημι-compounds in Homer
(ἐνέηκε, ἀφέηκε, μεθέηκε, προέηκε) show the augment ἐ- standing in hiatus before the root's
own long η, where Attic contracts the two into a single ἐνῆκε (per Monro's Homeric Grammar's
treatment of augment-plus-long-vowel-initial roots — the same phenomenon documented for
ἔειπε/εἶπε elsewhere in this same part). ἐνέηκε **is** augmented; it just isn't fused.

**Fix applied:**
- `units.json` l.233 `n`: now reads "ἐνέηκε, from ἐνίημι, IS augmented, like προσέειπεν just
  below: the augment ἐ- stands unfused before the root's own long η (ἐν-έ-ηκε), where Attic
  contracts the two into a single vowel, ἐνῆκε; ..." (rest of the note unchanged).
- `gloss.json` `"ἐνέηκε"`: now reads "ἐνίημι — put in, send into; aor. 3 sg., augmented,
  augment ἐ- uncontracted before the root's own long η (= Attic ἐνῆκε): 'put it in'".

### 2. Minor polish — `τοί` broaden entry wording

The added reading originally said "(= τοι, accented τοί here)". "Here" read as if pinning
the fact to this specific occurrence rather than stating the general orthographic rule
(the first of two successive enclitics is accented). Reworded to "(= τοι, accented before a
following enclitic, e.g. τοί τι)" so the entry states a rule usable wherever this word
recurs, per the "never pinned to a line" requirement for glossary entries. Not a
correctness bug — the underlying grammar was already right — just tightened for generality.

## Findings considered and NOT changed (with reasons)

- **`αὐτόθι` and `ἄντικλος` gloss entries contain the word "here"** — flagged by an automated
  string search, but both are legitimate: `αὐτόθι`'s English gloss is simply "here, on the
  spot, right there" (the word's actual dictionary meaning, not a line-pinning remark), and
  `Ἄντικλος`'s entry states "mentioned only here in the poem," a lexically checkable fact
  (Cunliffe's *Lexicon of the Homeric Dialect*, an approved aid, indexes it as occurring
  nowhere else in the Odyssey) rather than an invented or line-specific claim. The master
  glossary itself uses "here" this way in >50 existing entries (e.g. "here transferred to a
  speech," "here fig.," "here a district of Thessaly"), so this is house style, not a
  violation. Left unchanged.
- **Additional `__broaden__` entries beyond the 5 already present** — I checked all 386
  known forms' contexts against their master-glossary entries and found no case where the
  existing master reading fails to cover this part's usage, beyond the two forms (οἵ,
  δυσμενέων) that recur with a second sense within this same part, and ἐπὴν/ἐοικότα/ἐδήσατο,
  which needed broadening on their single occurrence — all five already caught by the first
  pass. No sixth broadening was warranted.
- **Repeated novel forms with potentially different senses**: four novel forms recur more
  than once in this part (καρτερὸς, κατέδυ, ἔρεξε, ἤγαγε). In every case the repeated
  occurrence carries the *same* sense/parse as the first (e.g. ἤγαγε means "brought/led" all
  three times it appears, with different objects but no grammatical difference), so a single
  entry legitimately covers all instances; no homograph-joining was needed for these.
- **Invented or smoothed-over disputes**: searched every `n` note and every `gloss.json`
  entry for "disputed"/"unknown"/"uncertain." Found exactly one, `ζείδωρος` (l.227,
  gloss.json), correctly noting the genuine ancient dispute between "grain-giving" and
  "life-giving" — this matches the already-fixed house-table entry for the same word at
  3.3 (odyssey-010) and is not an invented crux. No case was found of a real dispute being
  silently smoothed over, nor of a false dispute being invented.
- **Every other "augmented"/"unaugmented" claim in the 29 units whose notes discuss
  augment** (ll. 219, 220, 222, 224, 227, 233, 244, 247, 249, 250, 251, 252, 259×2, 266,
  267, 269, 271, 280, 282, 284, 287, 289, 300, 301, 302, 306, 309, 312, 316, 322, 325, 326,
  328) was checked individually against the verb's actual root and the standard augment
  rules (syllabic ἐ- for consonant-initial stems, temporal lengthening α/ε→η, ο→ω, ι→ῑ,
  υ→ῡ for vowel-initial stems, and the Homeric-specific "uncontracted augment before a
  root's own long vowel" category). All were correct except the one fixed above. In
  particular I double-checked the two second-pass-reviewer flagged bug pattern
  ("augmented called unaugmented") across the whole file and found no further instance of
  it beyond ἐνέηκε.
- **Translation-pass (pass 1) self-consistency**: re-read every note in `units.json` for the
  "augmented called unaugmented" bug both pass-1 reviewers reportedly found instances of.
  Found none remaining (the ἐνέηκε case found here is a glossary-note issue in the same
  family, not a leftover pass-1 regression — it was introduced/retained specifically in the
  augment-heavy commentary this part carries, and is now fixed).
- **Article-vs-pronoun, possessive ὅς/ἥ/ὅν vs relative, genuine homographs**: spot-checked
  throughout (e.g. `ὃς`, `ἣν`, `τὸν`, `οἱ`/`τοί` entries) — all correctly kept apart per the
  master glossary's existing entries and this part's added broadenings.
- **Line-pinning, length, homograph-joining across all 183 novel entries**: checked
  programmatically (length ≤ 230 for all entries, longest is 223) and by direct reading;
  no entry pins its sense to "here" (in the problematic sense) or to a specific line number.

## Summary of edits made in this pass

| File | What changed | Severity |
|---|---|---|
| `units.json` | l.233 `n`: corrected ἐνέηκε from "no separate augment" to "IS augmented, uncontracted" | Real (augment mislabeling) |
| `gloss.json` | `"ἐνέηκε"` entry: same correction | Real (augment mislabeling) |
| `gloss.json` | `__broaden__.τοί`: reworded "accented τοί here" → "accented before a following enclitic" | Polish (generality) |

No further edits were needed. `t` fields were never touched.
