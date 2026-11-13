# Review — cid-tiradas-10-14 (lines 174–241)

## Pass 1 — units.json

**Continuity (before and after edits):** PASS. 29 units; concatenated `t` = the packet's 72 lines exactly, in order
(181b–d and 228b included); every `l` has as many lines as its `t`; all units 1–4 lines; no unit crosses a tirada
break (tiradas start at units 0, 7, 16, 22, 25). The draft carries no `p`/`v`/`ln` fields; those are left to assembly.
Every cross-reference to vv. 1–173 was checked against the published parts (all correct except the one at u3).
Assonance re-derived from the line-endings: 10 á-a, 11 á-o, 12 í-a, 13 á, 14 ó (with ó-e albores). All correct.

### Changes
| unit | field | severity | what was wrong | what was done |
|---|---|---|---|---|
| 21 | l | error | "that I-have there sung thousand masses" reads as a perfect; faga is present subjunctive, a causative with cantar | "that I-may-make there to-sing thousand masses" |
| 9 | n | error | Offered "hedes read as aver de of obligation", but there is no de: aver + bare infinitive is the split future. The non-for-no' alternative goes against the edition's apostrophe | Both alternatives cut. Kept: no' = nos, and the sense of mereçer/atorgar is uncertain |
| 25 | n | error | "the manuscript reads otherwise at those letters, and the restored endings bring the lines into the ó assonance": a claim about the MS that the brackets do not show | Cut down to: the bracketed endings at the rhyme-word are Pidal's restorations |
| 26 | n | error | [cr]ebar: "the restoration is uncertain … his reconstruction of the line, not what the copyist wrote", which says more about the MS than the brackets show | "its cr restored by Pidal: 'the dawns are about to break'" |
| 3 | n | error | Called con todo recabdo "the phrase used of the king's sealed letter at v. 24"; v. 24 reads con grand recabdo | Reworded: recabdo as in con grand recabdo (v. 24) |
| 2 | i | weak | Added "well and good", an apodosis the Spanish does not have | The si-clause now hangs on the promise: "…from this moment, if I bring it you from over there; if not…" |
| 2 | n | weak | Long hedge with two readings of contalda sobre las arcas that barely differ, and "both halves uncertain" | Compressed to one reading (debt secured on the chests, sobre as at v. 161) plus "exact sense not certain" |
| 1 | l | weak | "a pelt" (a raw skin), against the note's "fur garment, not a raw skin" | "a fur" |
| 1 | i | weak | "a fine and splendid one" doubled ondrada; "to ask it of you" glossed en don que la yo aya loosely | "a fine crimson Moorish fur — Çid, I kiss your hand, that I may have it as a gift" |
| 6 | i | weak | "Now, don Raquel and Vidas": the l and the house gloss take ya as vocative 'O'; v. 155 (same phrase) is published as "Ah, don Raquel and Vidas" | "Ah, don Raquel and Vidas" |
| 12 | l | weak | "Come-you" reads as an imperative; Venides is present indicative | "You-come" |
| 12 | n | weak | "promises … the reward", but vea is a wish, not a promise | "wishes" |
| 15 | n | weak | "the grammar of the line … favours a curtailed visit": the grammar does not decide this, the context does | "the pairing with quitaremos el reynado and the haste of the next line favour…" |
| 5 | n | weak | "five squires are needed because the coin is genuinely heavy, as the sand was": an inference the text does not state | Clause cut |
| 7 | n | weak | Wordy hedge on no' lo, including a "non lo" reading the apostrophe rules out | no' = nos (Pidal's apostrophe); only the sense of buscar is flagged as the likeliest one |
| 23 | i | weak | "and take my ease with her" adds to a todo mio solaz | "I shall see my wife, to my heart's content" |
| 23 | n | style | "at leisure … a short stay" contradicted itself; los of castigar los he not identified | Reworded; "(los, his household)" added |
| 27 | i | weak | "a true Christian": the "true" is not in the Spanish | "a Christian of the Creator" |
| 19 | n | style | Cited v. 114 for ira, but v. 114 has ayrado, not ira | Now cites v. 74 only |
| 22 | n | style | The assonance list showed leal without saying it is in Pidal's restored half-line | Now "[leal] … leal in Pidal's restoration" |

### Considered and refused
- u0 n: [h]a besa[da] agreement rests on a restored -da. Refused: the note already says the -da is Pidal's.
- u3 n: "not in the manuscript" for 181b–d. Refused: a wholly italic line is exactly what Pidal's italics show, and the pilot says the same of 14b.
- u10 n (gradó: "pleasure or relief"). Refused: speculative, but it is marked as open.
- u11 n: nasçer in the note against the glossary lemma nacer. Refused: a spelling variant, not a contradiction.
- u22 n (caboso referent uncertain). Kept: a real ambiguity, stated as such; i keeps it neutral ("the worthy man").
- u24 i: "before the sun is ready to rise" for rayar 'send out rays'. Refused: a fair English idiom; the note gives the literal sense.
- u26 i: "crowing thick and fast" for Apriessa. Refused: it gives the sense of haste and is not stock English.
- u28 i: "There too was". Refused: "too" is a light connective, harmless.
- u21 n: "the poem plainly presents it as [a pious bargain]". Refused: a fair reading of the mando … si clause.
- House renderings checked: "in a good hour you girded on your sword" (u0), "born in a good hour" (u11), "my Çid" in narration, the Campeador, don Martino. All consistent.
- Every grammatical label was checked and found correct apart from those changed above: the split futures (mereçer no' lo hedes, atorgar nos hedes, castigar los he), the synthetic futures (mesuraremos, quitaremos), the future subjunctives (aduxier, fiziéredes, f[o]re, quisiere), the imperatives (contalda, mandad, val), the preterite anterior (ovo fecho) and the ser-perfect (exido es).

## Pass 2 — gloss.json

**Continuity / coverage:** PASS. All 179 keys of novel-forms.json are present, plus `__broaden__`. The 316 tokens of the
text are fully covered by gloss + known-forms. Every `__broaden__` value = old entry whole + " · " + new reading
(checked by script).

### Changes
| key | severity | what was wrong | what was done |
|---|---|---|---|
| menbrada | error | "renowned, esteemed": wrong. menbrado = prudent (the glossary's own menbrado entry and the u14 note) | "prudent, sensible (fem.; lit. 'mindful' …)" |
| albores | error | Lemma "alborada"; albores is the plural of albor | "albor — dawn, first light (pl. albores)" |
| mereçer | error | Quoted the line as "mereçer vos lo hedes"; the text reads mereçer no' lo hedes. Sense 'repay' missing | Quotation corrected; "to deserve; to earn back, repay" |
| mereçía | error | "he deserved (3rd sg.)", but here the subject is yo; the form is 1st/3rd sg. | "I/he deserved (imperfect 1st/3rd sg.)" |
| mesuraremos | error | "settle up … 'reckon up the lodging'" disagreed with the note's preferred 'cut short our stay' | "measure, keep within measure …; probably 'we shall cut our stay short' (sense uncertain)" |
| mandada | error | "bequeathed, assigned, ordered" left out 'promised', the sense here and in the note | "promised, pledged; ordered" |
| cinxiestes | weak | Lemma "cinxir"; the glossary (çinxiestes, çinxo) and the note use çeñir | Lemma çeñir |
| aduxier | weak | Lemma "aduzir"; the glossary and the note use aducir (as spelt at v. 144) | Lemma aducir |
| ixieron | weak | Lemma "ixir … cf. exir"; the note and the glossary (exien) use exir | Lemma exir |
| caboso | weak | "epithet of the Cid; sense debated" contradicted the note (sense clear, referent uncertain) | "accomplished, excellent (adj., also used alone as a noun)" |
| buscado | weak | Only 'sought'; the note and the line need 'procured' | "sought; procured, brought about" |
| gradó | weak | "it pleased … = agradó" sat badly with the note's 'was glad' (gradar, as in grádanse) | "he was glad, took pleasure" |
| mando | weak | 'I vow, I bequeath' left out the 'promise' the note gives | "I promise, vow; I order" |
| fiziéredes | weak | "you shall have done" mistranslates a future subjunctive | "(if) you do, should do" |
| faga | weak | "may he make", but here the subject is 1st sg. | "may I/he make …; faga cantar 'have sung'" |
| sabor | weak | "a so sabor 'to their liking'", though the line means his (the Çid's) pleasure | "at his (their) pleasure" |
| plazdo | weak | Pinned to "the nine days of grace", which this part does not mention | "term, time limit, appointed day" |
| dalgo | style | "daughter of someone" against the note's "of something" (algo) | "of something; fija dalgo 'daughter of something', well-born" |
| tú | style | "addressed to Christ/God": Christ is not named | "used in prayer to God" |
| recibió | style | Lemma recebir, but reçibir for reçibiólo | Both reçibir |
| nasco | style | Lemma nascer against the glossary's nacer (naçido) | nacer |
| __broaden__ coger | error | Known "to take in, shelter (= acoger)" misfits coger la tienda (v. 208) | Broadened: "to take up, strike (a tent)" |
| __broaden__ contado | weak | Known entry restricts it to the Campeador; v. 193 applies it to Martín Antolínez | Broadened |
| __broaden__ recabdo | weak | 'care, precaution' misfits con todo buen recabdo (v. 206) | Broadened: "business secured, a sure outcome" |
| __broaden__ aun | weak | 'even, besides' misfits aun vea el dia (v. 205) | Broadened: "yet, still" |

### Considered and refused
- The draft's broadens for no, nos, y, don and es: all needed and correctly formed. Kept.
- matines → lemma matín. Left: arguable, but not wrong enough to change.
- The known entries santa/maría ("the cathedral of Burgos") against v. 218 (the Virgin). Refused: "Mary" stands first in the entry.
- The known entry antes ('before') against antes … que 'sooner than' (v. 231). Refused: close enough.
- Contested forms now agree between notes and glossary: gradó (gradar, 'was glad'), caboso (accomplished; referent left to the note), mesuraremos (probably 'cut the stay short', uncertain), aduxier (aducir, future subjunctive 1st/3rd sg.), hedes (2nd pl. present of aver, the auxiliary of the split future), no' (= nos).
