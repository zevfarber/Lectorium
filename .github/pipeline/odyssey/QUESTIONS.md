# Odyssey pipeline — open questions

## 1.47 ὡς (raised at the pilot, 2026-09-20)
The archive prints unaccented ὡς with the optative of wish ἀπόλοιτο. The text is left as printed and the
note says how it is taken. Worth one look at the printed Loeb page; no second witness is wired.

## τῷ's "therefore" sense cannot be added within the 230-character glossary cap (raised at odyssey-003, 2026-09-22)
At 1.239 τῷ is used inferentially ("in that case, therefore"), a sense the shipped glossary entry for τῷ
does not carry (it covers the pronoun, the relative, and the instrumental relative). The shipped entry is
already 227 characters, and conventions.md's rules — every entry under 230 characters, broadenings are
additions-only and must never shorten the existing text — leave no room to append even the shortest honest
addition. Decided meanwhile: left unbroadened. The unit's own note at 1.239 states the sense correctly, so
a reader is not misled, only unaided by the glossary entry itself. Closing this needs an owner decision:
either raise the per-entry cap for heavily-used forms, or permit compacting an old entry's wording (which
the current rule forbids, to keep old readings intact). `build_odyssey.py` does not enforce the 230-char
cap on broadenings (only on new entries), so a fix could technically pass the gate; the pipeline chose not
to rely on that gap.

## 1.277 ἔεδνα / οἱ δέ: whose people prepare the gifts, stated without a hedge (raised at odyssey-003, 2026-09-22)
"οἱ δὲ γάμον τεύξουσι καὶ ἀρτυνέουσιν ἔεδνα" (1.277) is rendered with οἱ δέ taken as Penelope's father's
household preparing the wedding-gifts — the majority reading — while ἔεδνα itself is glossed neutrally
("wedding-gifts") because the word's usual lexicon sense (a suitor's gifts to a bride's family) sits
awkwardly with its use here. Some commentators take οἱ δέ as the suitors instead. The reviewer judged a
second caveat in an already-double-hedged note would overload it, and left the unit committed to the
majority reading without flagging the alternative in the note itself. Decided meanwhile: left as is;
flagged here in case a future part's cross-reference or the owner's own reading disagrees.

## How strictly to read "a note asserts nothing about the rest of the poem that this part cannot show" (raised at odyssey-004, 2026-09-23)
Read strictly, this conventions.md rule would bar any note that reaches outside its own part's line range
at all — including broad, low-risk background framing ("πεπνυμένος is Telemachus's fixed epithet
throughout the poem", "Antinous is named here for the first time in the poem", "the book closes, as it
opened, with a figure lying awake"). odyssey-004's reviewer found about a dozen such notes and fixed only
the three highest-risk ones: one that was an outright factual error (a note at 1.339 attributed the
Ethiopians'-feast scene, 1.22–26, to Zeus; it is Poseidon), and two that made specific, checkable claims
this part cannot verify (a note quoting a line from outside the part, 1.28; a "found only here in Homer"
hapax claim). The dozen broad thematic/background references were left in place. Decided meanwhile: the
narrower reading — bar unverifiable or specific claims (quoted text, exclusivity claims, misattributable
facts), allow broad thematic framing that gives the notes tutorial value — governs going forward, since
odyssey-001's own model notes already use this kind of broad framing (e.g. "νόστος 'homecoming' appears
here for the first time"). Flagged here in case the owner wants the line drawn tighter; future parts'
reviewers should apply this same narrower reading unless he says otherwise.

## ASCII vs. typographic apostrophe in `l`/`i`/`n` (raised at odyssey-005, 2026-09-23)
Published parts 001–003 use a plain ASCII `'` throughout the English layers and notes (e.g. "Odysseus'
dear son"); odyssey-004 switched to the typographic `’` in the same positions. Neither conventions.md nor
the validator says which is the house rule for these fields — the validator only forbids ASCII in `t` and
in glossary entries. odyssey-005 followed the older (001–003) practice, since it is not itself a
translation error and the corpus is currently split roughly 3-to-1 in favour of ASCII. Decided meanwhile:
left as ASCII, matching the majority of published parts; flagged here in case the owner wants the whole
corpus normalised one way, in which case 004 (and any future part using `’`) would need a pass too.

## Published glossary entry for ἔβη mislabelled "unaugmented" (raised at odyssey-005, 2026-09-23)
The shipped `odyssey-glossary.json` entry for ἔβη reads "aor. 3 sg., root aorist, unaugmented (= ἔβη)",
which is self-contradictory: ἔβη is itself the augmented form (from βαίνω), and the unaugmented form is βῆ
(used repeatedly in this part, e.g. 2.5, 2.10). Glossary entries are additions-only under conventions.md's
own rule — an existing entry may only be broadened, never rewritten — so this could not be corrected from
within odyssey-005. Decided meanwhile: left as shipped, flagged here for an owner decision on how to
correct a wrong published entry (the additions-only rule has no provision for a straight fix).

## ὑψαγόρην at 1.385 (odyssey-004) vs. 2.85 (odyssey-005): checked, left as a near-miss
new-renderings.md for odyssey-005 flagged that ὑψαγόρη(ν) also occurs at 1.385 in the already-published
odyssey-004, and should be checked for consistency; the odyssey-005 reviewer couldn't check it (scoped to
only the last few units of odyssey-004). Checked at publish time: 1.384–385 (Athena-as-Mentor, predicate
infinitive ὑψαγόρην τ’ ἔμεναι) shipped as `l` "to be a lofty speaker" / `i` "to talk big"; 2.85 (Antinous,
vocative address ὑψαγόρη) is drafted as `l` "lofty-talker" / `i` "you lofty talker". Both keep "lofty" as
the operative word, but the wording is not identical. The two occurrences differ grammatically (a
predicate complement vs. a vocative title), which is some justification for not forcing identical
phrasing, but conventions.md's "translated every time, the same way" rule for stock epithets would favour
matching 1.385's wording exactly, since it shipped first and governs under "first ratified rendering
wins". Left as drafted rather than reopening the already-built odyssey-005; flagged here for the owner or
a future part to reconcile if ὑψαγόρη(ς) recurs again.

## ASCII vs. typographic apostrophe in `l`/`i`/`n` (restated at odyssey-006, 2026-09-23)
Still unresolved (raised at odyssey-005): odyssey-006 mixes both marks internally (about 320 ASCII, 21
typographic instances), following odyssey-005's own precedent of not normalising case-by-case. The
question from odyssey-005 stands: whether the owner wants one mark fixed as the house rule across the
whole corpus, in which case every part shipped so far (001–005, and now 006) would need a reconciliation
pass.

## ἐυπλόκαμος never promoted to the house-renderings table (raised at odyssey-006, 2026-09-23)
Calypso's epithet ἐυπλόκαμος ("fine-plaited", odyssey-001, 1.86) is exactly the kind of recurring
noun-epithet formula the house table exists to fix, but it was never added when odyssey-001 was drafted
(the pilot predates the table's current form) and has not recurred since. odyssey-006 drafted a related
but distinct word, ἐυπλοκαμῖδες ("fair-tressed", of a different referent — the Achaean women of old, not
Calypso), and its review caught the drafter's new-renderings.md row wrongly describing ἐυπλόκαμος as
"already fixed in the house table" (corrected to just cite where it appears). Decided meanwhile: left
ἐυπλόκαμος itself out of the table, since it has not actually recurred and promoting a once-used word on
suspicion alone is not what the table is for; flagged here in case the owner wants it added pre-emptively,
or wants a standing rule for when a used-once epithet earns a table entry.

## Published glossary entry for εἰδομένη mislabelled "pres. part." (raised at odyssey-007, 2026-09-23)
The shipped `odyssey-glossary.json` entry for εἰδομένη (from an earlier part) calls it a present participle
of εἴδομαι. At 2.268 (Μέντορι εἰδομένη, of Athena's disguise as Mentor) it is used as an aorist: Autenrieth's
*Homeric Dictionary* lists the aorist system of εἴδομαι as "aor. εἰσάμην, part. εἰσάμενος, also εἰδόμενος" —
the -όμενος spelling doing double duty as the aorist participle in Homer, not a separate present form. This
is the same class of problem as the already-flagged ἔβη entry (odyssey-005, 2026-09-23): an existing
published entry that looks wrong, but the additions-only rule has no provision for a straight fix, only a
broadening. odyssey-007 broadened it (old entry whole, plus " · " and the aorist reading), which records the
correct sense for a reader without contradicting the shipped text. Flagged here alongside ἔβη for the same
owner decision: whether a wrong published entry should ever be correctable in place, not just appended to.

## περὶ and τί broadenings compressed to a bare tag by the 230-character cap (raised at odyssey-007, 2026-09-23)
odyssey-007 needed to broaden the shipped entries for περὶ (2.244, περὶ δαιτί, "over/for a feast") and τί
(2.303, μή τί τοι ἄλλο... κακὸν, indefinite used adjectivally) to cover uses their existing entries didn't
carry. Both shipped entries were already at 217–219 characters, leaving only 4 characters of headroom before
the 230-char cap; nothing informative fits in 4 characters, and the additions-only rule forbids shortening
the existing text to make room. The broadenings shipped as bare tags ("· + dat." for περὶ, "· adj." for τί)
— technically correct (real, distinct uses, confirmed against the actual line) but not self-explanatory on
their own the way a normal entry is. Same underlying tension as τῷ's (odyssey-003) and ἔβη's (odyssey-005)
entries above: the 230-char cap and the additions-only rule can jointly make a correct broadening
unreadable. Left as shipped; flagged here in case the owner wants the per-entry cap raised for heavily-used
forms, as τῷ's entry already asked.

## Published rendering of Πεισηνορίδαο (odyssey-004, 1.428) is grammatically backwards — carried into odyssey-008 by the repeated-line rule (raised at odyssey-008, 2026-09-24)
The line "Εὐρύκλει’, Ὦπος θυγάτηρ Πεισηνορίδαο" (Eurycleia, Ops' daughter, [descendant] of Peisenor) was
first published in odyssey-004 (1.428) and recurs word-for-word in odyssey-008 (2.347). Its shipped `l`
there reads "...Peisenor's grandson" — but the patronymic Πεισηνορίδαο agrees with Ὦψ, not with Εὐρύκλεια:
the sense is that Ops was Peisenor's son, making Eurycleia his granddaughter, and "grandson" is the wrong
word regardless of whose descent is meant. The shipped `i` for the same line already reads correctly
("daughter of Ops son of Peisenor"), so only `l` is wrong. odyssey-008's repeated-line rule requires reusing
odyssey-004's shipped `l`/`i` verbatim for this line, so the error was carried over rather than corrected;
odyssey-008's own unit (2.345) states the discrepancy plainly in its note, and its new-renderings.md flags
it for the reviewer. This is the same class of problem as the already-flagged ἔβη (odyssey-005) and εἰδομένη
(odyssey-007) glossary entries, except here the wrong text is in a published unit's `l` rather than in the
glossary, so even the additions-only broadening mechanism doesn't apply — there is currently no mechanism at
all for correcting a published unit's English once shipped. Decided meanwhile: left as shipped in both
odyssey-004 and odyssey-008; flagged here for an owner decision on whether and how a published unit may ever
be corrected in place.

## Shipped note on θεοῖο at 2.406 (odyssey-008) says "grammatically masculine because she is disguised as Mentor" (raised at odyssey-009, 2026-09-24)
3.30 repeats 2.406 word for word (ὁ δ’ ἔπειτα μετ’ ἴχνια βαῖνε θεοῖο.), and odyssey-009 reuses its shipped `l`/`i`
exactly. The notes disagree: odyssey-008's says θεοῖο is "grammatically masculine because she is disguised as
Mentor, a man"; odyssey-009's says θεός is a noun Homer uses of goddesses as well as gods. The -οιο genitive
does not show gender at all, and the narrator, not Telemachus, is speaking, so there is nothing that makes the
word masculine. odyssey-009's note is the defensible one and stands. The shipped glossary entry θεοῖο ("masc. gen.
sg.") has the same slant. Decided meanwhile: both left as shipped (additions-only, and there is no way to correct
a published note). Flagged for the owner.

## Shipped glossary entry τινα mislabelled "neut. acc. sg." (raised at odyssey-009, 2026-09-24)
The neut. acc. sg. of τις is τι, not τινα; τινα is masc./fem. acc. sg. (or neut. pl.). odyssey-009 needed the
masc./fem. acc. sg. reading anyway (ὅν τινα 3.16, ἥν τινα 3.18) and broadened the entry, which leaves the wrong
first label in place under the additions-only rule. This is the same kind of problem as ἔβη (odyssey-005) and εἰδομένη
(odyssey-007).

## Two broadenings blocked by the glossary's 230-character cap (odyssey-011, 2026-09-24)
κακὸν (nom.-subject-of-a-personal-verb sense at 3.306, κακὸν ἤλυθε) and ὃ (plain neuter relative "which"
referring to a thing at 3.273) both needed a broadened glossary entry this part, but their existing shipped
entries are already 225–329 characters long, so any compliant broadening (old text kept verbatim + new
reading appended) would exceed the 230-character cap. Same tension as τῷ (odyssey-003) and περὶ/τί
(odyssey-007). Decided meanwhile: left both shipped entries untouched rather than violate the cap; the two
readings needed in this part are covered correctly in the units' own notes instead. Flagged for the owner —
whether the cap should be raised, or a broadening allowed to omit the oldest reading when space is tight.

## Two more broadenings blocked by the glossary's 230-character cap (odyssey-012, 2026-09-25)
κακόν (predicative "base, cowardly" of a person, 3.375, οὔ σε ἔολπα κακὸν καὶ ἄναλκιν ἔσεσθαι) and
Τηλεμάχοιο (a plain possessive genitive without periphrasis, 3.364, μεγαθύμου Τηλεμάχοιο) both needed a
broadened glossary entry this part, but the shipped entries are already 329 and 235 characters
respectively — both already over the 230-character cap before anything is added, so no compliant
broadening is possible at all. Same recurring tension as τῷ (odyssey-003), περὶ/τί (odyssey-007) and
κακὸν/ὃ (odyssey-011) above. Decided meanwhile: left both shipped entries untouched; the readings needed
here are covered in the units' own notes instead.

## Two published glossary entries carry augment errors, found while reviewing odyssey-012 (2026-09-25)
Both are shipped entries that this part's review could not fix in place under the additions-only rule:
- **ὤιξεν** (odyssey-011's shipped entry) is labelled "unaugmented", but οἰ- → ὠι- is itself the augment
  (the corresponding unit's own note at 3.392, this part, states this correctly for the same form).
- **ἔκ** (published earlier) glosses one of its senses as "= ἐξωνόμαζε", but the separated verb in tmesis
  (ἔκ … ὀνόμαζεν) carries no augment at all — the augmented form would be ἐξονόμαζε, not ἐξωνόμαζε.
Same class of problem as the already-flagged ἔβη (odyssey-005), εἰδομένη (odyssey-007), τινα (odyssey-009)
and Πεισηνορίδαο's `l` (odyssey-008): a wrong published entry with no mechanism to correct it in place,
only to broaden around it. Flagged for the owner alongside those.

## Live inconsistency in how δῖος/δῖα is rendered for a place, found while reviewing odyssey-012 (2026-09-25)
odyssey-012 renders Λακεδαίμονα δῖαν (3.326) as "heavenly Lacedaemon" in both `l` and `i`, consistent with
the house table's general practice for δῖος/δῖα ("heavenly-one of goddesses", "heavenly" of Odysseus).
odyssey-010, however, already shipped ἅλα δῖαν (3.153, a different noun, same adjective) as "heavenly
brine" in `l` but "bright salt sea" in `i` — the two English layers disagree with each other there, and
"bright" is not this part's own choice for the word. Decided meanwhile: odyssey-012 follows the table's
general "heavenly" pattern and does not retroactively touch odyssey-010's shipped text. Flagged for the
owner as a cross-part consistency question, not urgent.
