# Beowulf — editorial conventions

Distilled from the project's Old English rules (decided July 2026) and the three parts published in July
(`beowulf-prologue.json`, `beowulf-fitt-01.json`, `beowulf-fitt-02.json` in the repository root). Those three files
are the model of shape, register and note-writing: read at least one whole before drafting.

## The text

- **Edition:** Fr. Klaeber, *Beowulf and the Fight at Finnsburg*, 1st ed., 1922 — public domain everywhere. The whole
  poem is in `source/beowulf-klaeber1922.json`, transcribed from the page images on 2026-09-30 (every page read twice,
  every disagreement settled on the page). It is the only text. Never draft from memory of the poem.
- **Sole-source rule:** draft only from Klaeber's text plus public-domain lexical aids (Klaeber's 1922 glossary,
  Bosworth–Toller 1898, Clark Hall). No modern translation is opened or recalled for wording — Heaney, Tolkien,
  Chickering, Liuzza and the rest are in copyright and the famous passages tempt echoes. An English phrase that arrives
  fully formed is rebuilt from the grammar.
- **What the characters mean** (see the source file's `encoding`): þ ð æ as printed; macrons mark long vowels; a
  circumflex marks a contracted vowel — Klaeber prints one mark over a pair of vowels and we place it on the second
  (Līffreâ, geþeôn, heân); a dot under a vowel (dōgọra, trūwọde) is Klaeber's sign that the vowel does not count in the
  metre — explain it the first time a part meets one; ę is e caudata; `[ ]` = letters or words Klaeber added by
  emendation; `( )` = letters restored where the fire-damaged manuscript is lost; rows of dots = words lost; † = a
  passage Klaeber marks as corrupt. Klaeber's italics (letters he changed) are listed in the packet, not marked in `t`.

## Everything is speculative, and the reader is told so

The single manuscript was scorched in 1731; its edges are lost and some readings survive only in the 1787 Thorkelin
transcripts; the poem is full of words that occur nowhere else. Every part carries the standing `about` paragraph (the
build copies it). Notes admit uncertainty instead of papering over it: a word whose meaning is guessed is called a
guess; where Klaeber emends (brackets, parentheses, italics), the note says what the manuscript has when the packet's
apparatus gives it and it matters for the sense.

## Units

- The unit is Klaeber's punctuated sense-unit. It may begin or end in mid-line (Klaeber punctuates across the line
  constantly), but a line is never broken anywhere else: `t` holds whole verse lines joined by `\n`, except where the
  unit starts or ends at a mid-line punctuation mark. Every unit has `v: true` and `ln` = the line it starts on.
- `t` is cut from the packet's lines by a small script, never retyped.
- Long sentences may be cut at any semicolon or colon; eight lines is the ceiling for one unit.

## The three layers

- **`l` (literal):** structurally transparent where English can bear it, and stops before it becomes gibberish —
  Old English word order is freer than German's, and coherence wins ties. One paragraph (no line breaks).
- **`i` (idiomatic):** real English a person would say, lightly old-fashioned in register, never childish. Omit it only
  where it would equal `l`.
- **`n` (note):** on (nearly) every unit — the published parts sit at 95–100 % and that is the standard, not a defect to
  trim. Lead with what the reader needs to read these words: the grammar that produces the sense (case, mood, word
  order), then the word or kenning, then culture or story where it helps. Quote Old English in single curly quotes
  (‘…’). Plain sentences; no assert-by-negation, no vague atmospheric closers, no abstract aphorisms.

## Recurring treatments

- **Kennings and compounds:** hyphenated-literal in `l` ("whale-road", "bone-house"), unpacked in `i` ("sea", "body"),
  explained in a note on their first occurrence in the poem, a short nudge thereafter.
- **Proper names** stay untranslated as Klaeber prints them (Bēowulf, Hrōðgār, Grendel, Higelāc); the glossary gives
  their meaning or identity.
- **House renderings already set** (do not relitigate): `Hwæt` = "What!" in `l`, "Listen!" in `i`. Before choosing an
  English rendering for a recurring word or formula (maþelode, the speech introductions, epithets of God, of Beowulf, of
  Hrothgar), search the published parts (`grep` the root `beowulf-*.json`) and reuse what they chose. A new formula that
  will plainly recur gets a rendering chosen with care and recorded in the table below.
- **A famous crux** with no house rendering: render it from the lexica as plainly as the grammar allows, say in the
  note that the reading is disputed, and write it to `QUESTIONS.md` with what you chose.

## Audio (decided 2026-10-12)

Zev chose the American English carrier (Voice B of the sample round, audio-pilot/beowulf.html): en-US-Neural2-D, rate
0.85, a 350 ms pause at each verse-line end, every word pinned to IPA by `oe_g2p.py` (reconstructed late West Saxon,
c. 1000, after Campbell). The audio is built by the site's automatic audio job, never by a drafting run: a newly
published part is voiced when it is pushed, in poem order, within the monthly audio budget. Every part's `source` ends
with the standing audio statement (`AUDIO_STATEMENT` in `beowulf_lib.py`; the build copies it) naming the convention, the
carrier and its limits. Do not edit it by hand in a part; change it in `beowulf_lib.py`, and only with the voice.

## Glossary (`beowulf-glossary.json`, shared by every part)

- Key = the word as printed, lowercased, brackets and parentheses stripped (þon[n]e → þonne) — exactly the reader's
  `wordKey()`. Dots below and circumflexes are part of the key (dōgọra, heân).
- Entry: `"lemma — meaning (parse; brief remark)"`, general to the form, never pinned to a line: no line numbers, no
  "here". Names give identity ("Hrōðgār — Hrothgar, king of the Danes, son of Healfdene").
- Additions only. An existing entry may be broadened (the old entry whole, then " · " and the new reading) under
  `"__broaden__"`; it is never rewritten.

## House renderings added by runs

| form | l | i | first used |
|---|---|---|---|
| meþelwordum / maþelode | speech-words (`l`) | asked in formal words (`i`) | beowulf-fitt-03 line 236 |
| Weard maþelode (verb; same row) | spoke in speech-words (`l`) | spoke in formal words (`i`) | beowulf-fitt-04 line 286 |
| Fæder alwalda | Father all-ruler (`l`) | the Father, ruler of all (`i`) | beowulf-fitt-04 line 316 |
| mānscaða | crime-scather (`l`) | wicked marauder (`i`) | beowulf-fitt-11 line 712 |
| fyrena hyrde | keeper of crimes (`l`) | keeper of wickedness (`i`) | beowulf-fitt-11 line 750 |
| Godes andsacan | God's adversary (`l`) | God's enemy (`i`) | beowulf-fitt-11 line 786 |
| herebyrne | war-byrnie (`l`) | war-corslet (`i`) | beowulf-fitt-21 |
| bāncofa | bone-chamber (`l`) | body (`i`) | beowulf-fitt-21 |
| sund cunnian | try the swim (`l`) | try the water (`i`) | beowulf-fitt-21 |
| heaþoswāt | battle-sweat (`l`) | blood of battle (`i`) | beowulf-fitt-21 |
| wǣgbora | wave-bearer (`l`) | wave-bearer (`i`) | beowulf-fitt-21 |
| nicorhūs | water-monster-houses (`l`) | water-monster-houses (`i`) | beowulf-fitt-21 |
| seglrād | sail-road (`l`) | sail-road (`i`) | beowulf-fitt-21 |
| brimwylf | sea-she-wolf | sea-she-wolf | beowulf-fitt-22 |
| merewīf | mere-woman | mere-woman | beowulf-fitt-22 |
| beadolēoma | battle-light | battle-light | beowulf-fitt-22 |
| brēostnet | breast-net | breast-net | beowulf-fitt-22 |
| herenet | war-net | war-net | beowulf-fitt-22 |
| selegyst | hall-guest | hall-guest | beowulf-fitt-22 |
| fēþecempa | foot-fighter | foot-fighter | beowulf-fitt-22 |
| Weder-Gēata | Weder-Geats (`l`) | Geats | beowulf-fitt-22 |
| Sǣ-Gēatas | Sea-Geats (`l`) | Geats (`i`) | beowulf-fitt-26 |
| freoðuwebbe | peace-weaver | peace-weaver | beowulf-fitt-27 |
| hȳðweard | harbour-guard | harbour-guard | beowulf-fitt-27 |
| bātweard | boat-guard | guardian of the boat | beowulf-fitt-27 |
| hringnet | ring-net | mail | beowulf-fitt-27 |
| merehrægl | sea-garment | sail | beowulf-fitt-27 |
| wēgflota | wave-floater | ship | beowulf-fitt-27 |
| bundenstefna | bound-prowed | bound prow | beowulf-fitt-27 |
| sceādenmǣl | divided-marked | patterned sword | beowulf-fitt-27 |
| hildestrengo | battle-strength | battle-strength | beowulf-fitt-30 |
| gūðwiga | war-man | war-man | beowulf-fitt-30 |
| fyrnwita | ancient-counsellor (`l`) | old counsellor (`i`) | beowulf-fitt-30 |
| wīghete | war-hate | war-hate | beowulf-fitt-30 |
| gyrnwræc | grief-vengeance | grief-vengeance | beowulf-fitt-30 |
| unhȳre | monstrous / ungentle | monstrous | beowulf-fitt-30 |
| grundhyrde | ground-guardian (`l`) | guardian of the depths (`i`) | beowulf-fitt-30 |
| dēaðwērig | death-weary | death-weary | beowulf-fitt-30 |
| hand gemǣne | hand in common (`l`) | hand-to-hand blows (`i`) | beowulf-fitt-30 |
| wyrm | worm (`l`) | dragon (`i`) | beowulf-fitt-32 |
| ūhtsceaða | dawn-scather | dawn-scather | beowulf-fitt-32 |
| ðēodsceaða | people-scather | people-scather | beowulf-fitt-32 |
| hordwynn | hoard-joy | hoard-joy | beowulf-fitt-32 |
| sincgifa | treasure-giver | lord, giver of treasure | beowulf-fitt-32 |
| herepād | war-coat | war-coat | beowulf-fitt-32 |
| hordærn | hoard-house | hoard-house | beowulf-fitt-32 |
| mandryhten | liege-lord | liege-lord | beowulf-fitt-32 |
| frioðowǣr | peace-pledge | peace-pledge | beowulf-fitt-32 |
| seledrēam | hall-joy | hall-joy | beowulf-fitt-32 |
| feorhbealo | life-bale | life-bale | beowulf-fitt-32 |
| gūðdēað | war-death | war-death | beowulf-fitt-32 |
| bealocwealm | baleful-death | baleful-death | beowulf-fitt-32 |
| glēobēam | glee-wood | glee-wood | beowulf-fitt-32 |
| beadogrīma | battle-mask | battle-mask | beowulf-fitt-32 |
| frēawine | lord-friend (`l`) | lord and friend (`i`) | beowulf-fitt-34 |
| frēowine | noble-friend | noble friend | beowulf-fitt-06 |
| goldwine | gold-friend | gold-friend | beowulf-fitt-17 |
| bealonīð | bale-malice | baleful malice | beowulf-fitt-25 |
| lēodhryre | people-fall | fall of a prince | beowulf-fitt-34 |
| eorðsele | earth-hall | earth-hall | beowulf-fitt-34 |
| ellorsīð | journey elsewhere | journey away from this world | beowulf-fitt-34 |
| feohlēas gefeoht | fee-less fight | a fight no payment could settle | beowulf-fitt-34 |
| morþorbed | murder-bed | bed of murder | beowulf-fitt-34 |
| Bīowulf maþelade (same row as Weard maþelode) | spoke in speech-words | spoke in formal words | beowulf-fitt-34 |
| bānhūs | bone-house (`l`) | house of his bones (`i`) | beowulf-fitt-35 |
| gryregiest | terror-guest (`l`) | dread visitor (`i`) | beowulf-fitt-35 |
| gūðflogan | war-flier | war-flier | beowulf-fitt-35 |
| lǣndagas | loan-days | lent days | beowulf-fitt-35 |
| hiorosercean | sword-shirt (`l`) | mail-shirt (`i`) | beowulf-fitt-35 |
| hringboga | ring-bowed (`l`) | coiled creature (`i`) | beowulf-fitt-35 |
| bēotwordum | vow-words | vow-words | beowulf-fitt-35 |
| inwitscear | malice-cutting | malice-cutting | beowulf-fitt-35 |
| wæll-seaxe | slaughter-knife | deadly knife | beowulf-fitt-37 |
| eorðdraca | earth-dragon | earth-dragon | beowulf-fitt-37 |
| eorðreced | earth-hall (as eorðsele) | earth-hall | beowulf-fitt-37 |
| winedryhten | friend-lord | friend-lord | beowulf-fitt-37 |
| sibæðelingas | kin-athelings | kin-athelings | beowulf-fitt-37 |
| mǣlgesceaft | time-fate | time-fate | beowulf-fitt-37 |
| feorhbennum | life-wounds | life-wounds | beowulf-fitt-37 |
| ǣrwela | ancient-wealth | ancient-wealth | beowulf-fitt-37 |
| goldǣht | gold-possession | gold-possession | beowulf-fitt-37 |
| searogimmas | cunning-gems | cunning-gems | beowulf-fitt-37 |
| dōgorgerīm | day-count | day-count | beowulf-fitt-37 |
| hildlatan | battle-laggards | slackers in battle | beowulf-fitt-39 |
| trēowlogan | troth-breakers | oath-breakers | beowulf-fitt-39 |
| attorsceaða | poison-scather | poison-scather | beowulf-fitt-39 |
| hringsele | ring-hall | ring-hall | beowulf-fitt-39 |
| frumgār | chieftain (first-spear) | chief | beowulf-fitt-39 |
| ferhðgenīðla | life-enemy | deadly foe | beowulf-fitt-39 |
| līfwraðe | life-protection | protection for his life | beowulf-fitt-39 |
| edwītlīf | reproach-life | to live on in reproach | beowulf-fitt-39 |
| sincþego / swyrdgifu / ēðelwyn | treasure-receiving / sword-gift / native-joy | receiving of treasure / giving of swords / joy of the homeland | beowulf-fitt-39 |
| dōmlēas | glory-less | without glory | beowulf-fitt-39 |
| wīdfloga | wide-flier | far-flier | beowulf-fitt-39 |
| homera lāfe | leavings of hammers | what the hammers left | beowulf-fitt-39 |
| hildfruma | battle-leader | battle-leader | beowulf-fitt-39 |
| hondgeweorc | hand-work | handiwork | beowulf-fitt-39 |
| swātswaðu | blood-track | blood-track | beowulf-fitt-41 |
| wælrǣs | slaughter-rush | slaughter-rush | beowulf-fitt-41 |
| wælhlem | slaughter-blow | slaughter-blow | beowulf-fitt-41 |
| ondslyht | return-blow | return-blow | beowulf-fitt-41 |
| lyftwynne | air-joy | air-joy | beowulf-fitt-41 |
| lēgdraca | flame-dragon | fire-dragon | beowulf-fitt-41 |
| endedæg | end-day | end-day | beowulf-fitt-41 |
| gūðrǣs | war-rush | war-rush | beowulf-fitt-41 |
| herewīsa | army-wise one | leader of the host | beowulf-fitt-41 |
| ādfær | pyre-journey | pyre-journey | beowulf-fitt-41 |
| Sōðcyning | true king of victories | true king of victories | beowulf-fitt-41 |
