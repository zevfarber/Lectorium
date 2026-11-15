# Review — cid-tiradas-27-31 (tiradas 27–31, lines 557–622 + 585b)

Adversarial review against the pinned packet, Pidal's footnotes on the scan (PDF pp. 166–170, read on the
image), conventions.md, the pilot (01-04) and the preceding part (24-26). All edits made by script
(json load/dump, ensure_ascii=False, indent=1). No `t` changed: the 67 `t` lines concatenated equal the
packet's 67 lines exactly (checked by script after the edits); one `l` line per `t` line in every unit.

## Pass 1 — units.json

Counts: error 1 · weak 4 · style 2 (7 changes)

| unit (first words) | field | sev. | what was wrong | what was done |
|---|---|---|---|---|
| 606 Dando grandes alaridos | n | error | "por[a]l = pora al, 'toward the'": wrong analysis — pora + al would be "toward to-the"; the form is pora + el, which is why Pidal restores the a | "por[a]l = pora + el, 'toward the' (pora = para)" |
| 606 Dando grandes alaridos | i | weak | "leave the fighting before them" adds "fighting" (not in dexando van los delant) and does not match the note's own reading ("those in front", uncertain) | "leave behind the men in front of them" — keeps the text's object and its ambiguity |
| 599 Bueltos son | n | weak | Pidal's footnote ('revueltos van con ellos por medio de la llanura') was given as an English paraphrase "turned back upon them", fixing one sense of revueltos as Pidal's | quotes Pidal's Spanish and says revueltos can mean 'turned about' or 'mingled with them'; the feigned retreat becomes the attack either way |
| 576 dexa una tienda | n | weak | stated as fact that the reflexive s "is swallowed before the S- of Salón" — Pidal says only cojó' = cogióse | "apparently lost before the S- … (the apostrophe marks the cut; compare cojós, v. 589)" |
| 557 Bien puebla | n | weak | "modern prender survives only as 'seize'" is untrue (prender also 'catch, take root, pin') | "modern prender is chiefly 'to seize, arrest'" |
| 583 De guisa va | n | style | "feremos = faremos" glosses one old form with another | "feremos, future of fazer … (= haremos; f- again)", as the glossary has it |
| 611 Vino Per Verm[udoz] | n | style | "in modern spelling Pero Bermúdez" — Pero is the old form, not the modern one | "Per is a short form of Pero, that is Pedro (modern Pedro Bermúdez)" |

Checked and found sound (no change):
- Rubrics and assonance in each tirada's first note, checked against the scan: 27 á-a (El Cid acampa sobre
  Alcocer), 28 á-o (Temor de los moros), 29 á-a (El Campeador toma a Alcocer mediante un ardid), 30 á-o (La seña
  del Cid ondea sobre Alcocer), 31 é-o (Clemencia del Cid con los moros). All line-ends fit.
- Pidal's footnotes are reported correctly: 561 (cárcava, fincança), 567 (ganar = labrar la tierra, Old French
  gaignier — given as "likely but not certain", which is fair to "debe ser"), 569 (ir + gerund pleonastic), 571,
  572 (ma' les por mal les), 575 (art 'ardid de guerra'), 577, 582, 583 (arrancada 'derrota'), 595, 597 (sines
  dubdança 'sin temor'), 603 (en essora 'entonces'), 606 ("la narración es confusa"; part of the Çid's men in
  ambush; cf. 631; the chronicles do not help).
- Restorations: cinxo espada, Alegr-, s[o]s, Ter[rer], se[d]manas, vi[d]o, el[le], V[id]ienlo, [ha], [la casa],
  585b's first half, [anda], da[van], por[a]l, Verm[udoz], R[o]y, la[s] all match the italics on the image and
  are each said to be Pidal's. 585b: the note says the first hemistich is supplied, that Pidal numbers it 585b
  himself and that his footnotes do not discuss it (true: no footnote for 585/585b on p. 168–169). [anda] is
  called a conjecture. la casa (571) is said to be uncertain.
- House renderings: "who in a good hour girded on his sword" (559) and "born in a good hour" (613), as in
  05-09/15-17; "my Çid" in `i` as in parts 05 onward; Álbar Fáñez → Álvar Fáñez in `i` (no Minaya in the text
  here, so none added); Alcocer, Jalón, Ateca, Calatayud as in 24-26.
- Grammar labels checked one by one (yogo, sopiessen, escapasse, diessen, vidien imperfect, the split future
  tornar nos la ha, participle agreement a dexada / a presa, ser with verbs of motion, que + subjunctive as a
  condition, cojámoslos): all right.
- Nothing bowdlerized (the beheading line, the dead Moors, "mercy that pays" are rendered straight).

Findings refused:
- l of imperfects (levava "he-took-away", pesava "it-weighed", vidien "They-saw-him") rendered with the simple
  past: refused — the published parts render the imperfect the same way in `l`; the notes name the tense.
- Letter-level brackets in `l` ("[Rejoic]ing") look odd: refused — 24-26 brackets restored words in `l` too,
  and the bracket here marks just the restored letters.
- Note 585b "so the traditional count is not disturbed": an inference about Pidal's motive, but the only
  reason a b-number exists; left.
- 559 note "the á-a assonance needs a word like espada": an editorial inference, but plainly true (all the
  line-ends are á-a and the formula elsewhere ends in espada); left.

## Pass 2 — gloss.json

Counts: error 7 · weak 4 · style 1 (12 changes)

| key | sev. | what was wrong | what was done |
|---|---|---|---|
| ma | error | glossed as "mas — but": Pidal's footnote 572 says ma' les for mal les, 'ill to them' (the units note had it right) | "mal — ill, sorely (adverb, with the l lost before les …; = mal)" |
| vidienlo | error | called a preterite, "= vieron + lo" (and "it" for the object); vidien is the old imperfect | "veer + lo — they saw him (imperfect 3rd pl. vidien … ; = lo veían)" |
| cinxo | error | invented infinitive "cinxir"; the glossary's lemma for cinxo/çinxiestes is çeñir | lemma çeñir, "strong preterite 3rd sg., Latin cinxit" |
| çintas | error | "past part. … of cinxir" — same invented verb | "old strong past part. of çeñir, Latin cinctus" |
| art | error | "(fem. in Old Spanish; un art …)" — contradicts its own example, which is masculine | "masc. here, un art"; Pidal's 'ardid de guerra' added |
| dent | error | "apocopated ende" — dent is de + ent (ende), not a cut ende | "de + ent, a form of ende 'thence'" |
| poral | error | "por + al … probably por + a + el": the form is pora + el, which is why Pidal restores the a | "pora + el — toward the (pora 'toward, for' + article …; = para el, hacia el)" |
| __broaden__ fita (new) | weak | existing entry gives only Fita = Hita, the town; in v. 576 fita is the participle 'pitched' — the reader would see the wrong gloss | broadened: "also fito — fixed, pitched (past part. fem. …; = hincada)" |
| __broaden__ ganar (new) | weak | existing entry lacks Pidal's sense in v. 567 ('till the land') | broadened with 'to till, work the land' (Pidal; = labrar) |
| __broaden__ ha (new) | weak | existing entry lacks the split-future ending (tornar nos la ha, v. 586) | broadened with the future ending |
| __broaden__ avié (new) | weak | existing entry says only "a full verb 'to have, hold'"; v. 595 is impersonal 'there was' | broadened with the impersonal sense |
| __broaden__ tornar | style | v. 596 mandó tornar la seña, transitive 'to turn', not covered | appended "; to turn (round), transitive (…)" |

Checked: every token in novel-forms.json (118) has an entry; every __broaden__ value begins with the existing
glossary entry exactly, then " · ". Other entries checked against the text and found right (person, number,
tense, mood, modern equivalent).

Findings refused:
- treven: lemma "trever" (rather than se atrever) — kept: trever is the old verb; modern = atreven given.
- cogiós "= se recogió", arrebata "probably = arrebato/arrebatada", terrer "probably modern Terrer": loose
  but not wrong; left.
- calatauth "from Arabic Qal'at Ayyūb": not from Pidal, but a standard etymology; left.
- bueltos "mingled, mixed in": fits Pidal's revueltos; left.
