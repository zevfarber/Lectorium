# read_B: pp. 84–86 (leaves n85–n87), read from the images

**Line counts.**
- p. 84 (n85) has five lines. It is a leaf back with no ornament.
- p. 85 (n86) has five lines. It is a leaf front and opens ༄༅༔ ༔ with a wide blank between the two ༔.
- p. 86 (n87) has five lines. It is a leaf back with no ornament.
- That makes 15 print lines.

**Where I started.** p. 84 opens ཁྲོ་བོའི་བར་དོ་ཡིན་པས༔. In witness_ga.txt this is the sentence འདིར་ཁྲོ་བོའི་བར་དོ་ཡིན་པས… (char. ~626). The word འདིར that comes before it belongs to the end of p. 83 (Reader A). p. 86 ends …ནང་ནས་གསང་, and the witness continues there with སྔགས་ཀྱི་ཉམས་ལེན་མེད་པས.

**Method.**
- Row profiles gave the headlines. They are at about y 125/180/235/290/345 on n85, 140/195/250/305/360 on n86, and 135/190/245/300/355 on n87. The lines slope by up to about 15 px.
- Each line was cropped in 4–6 overlapping segments at ×3–×4 (LANCZOS).
- Doubtful syllables were cropped at ×5–×12, with binarised pixel dumps (threshold 128/140) for tshegs and letter shapes.
- A connected-component pass found the free tsheg blobs on p. 84 l. 1–2.
- Filler dots at line ends and in mid-line were left out. Where a run of dots follows a syllable, the first dot is taken as the tsheg, as at 61.3 and 74.1.

## Line-end tsheg status

| Line | Ends with | Tsheg |
|---|---|---|
| 84.1 | ཐོབ | none (ends at the frame) → fix |
| 84.2 | གྱི་ | yes |
| 84.3 | འདི་ | yes |
| 84.4 | མཚན་ | yes |
| 84.5 | པ་ | yes, then fillers |
| 85.1 | སྡུག་ | yes, then fillers |
| 85.2 | ཏུ་ | yes, then fillers |
| 85.3 | འགྱུར་ | yes, a clear blob |
| 85.4 | རིས་ | yes |
| 85.5 | པའི | none (clean white to the frame) → fix |
| 86.1 | ཞིང་༔ | ends in ༔ |
| 86.2 | ནི་ | yes, a dot before the frame |
| 86.3 | རྣམྶ | none: a line-end subscript-ས abbreviation at the frame → fix |
| 86.4 | སྡང་ | yes, then fillers |
| 86.5 | གསང་ | yes, a small dot. There are smudges near the frame. Not certain |

The join 84.5→85.1 crosses the leaf-front ornament: …ཐ་མལ་པ་ ༄༅༔ ༔རྣམས་ནི. The tsheg is present, and this matches how part 008 handled 74.5→75.1.

## [?] (1)

- **86.5 དེས[?]་རྐྱེན** (…སེམས་སྐྱེས་ནས་དེས[?]་རྐྱེན་བྱས…).
  - What is visible (×7 and ×12): ད with the e-vowel, then a ས-shaped letter (two diagonal strokes, long left stroke), then a stack with ya-btags (ཀྱ/རྐྱ) and ན.
  - The other recension has དེའི་རྐྱེན. No gi-gu is visible over the second letter. In the same line, the clearly printed དེའི་ཕྱིར shows its gi-gu plainly.
  - So I read ས and mark it [?]. The top of the ya-btags stack is crowded, and ར over ཀ cannot be separated cleanly. རྐྱེན (the recension's word and the sense) is taken.
  - Candidates are དེས / དེའི. The sense is "with that as condition", and either reading gives it.

## Where the image overrides the other recension (or the print reads differently)

| page.line | recension → print | why / sense |
|---|---|---|
| 84.1 | ཡིན་པས་འཇིགས → ཡིན་པས༔ འཇིགས | ༔ printed |
| 84.1, 84.2, 85.1 | སྔངས → **དངངས** | ×5, all three times: a ད-headed stack, no ས prefix. Spelling variant of the same word, "dread" |
| 84.1–2 | མི་ཐོབ་པར་བརྒྱལ་ཏེ༔ དེ་ཁོ་ར་ཁོར་ཡུག → **མི་ཐོབ / བརྒྱལ་བབཁོར་ཡུག** | 84.1 ends ཐོབ at the frame, and 84.2 starts བརྒྱལ. There is no པར. The print has "fainting comes continuously" (བརྒྱལ་བ ཁོར་ཡུག་ཏུ་འོང), where the recension has "faints; that very [state] comes continuously". The print has no ཏེ༔ དེ་ཁོ་ར. See misprints for བབ |
| 84.2 | གྲོལ་བ་ཡང་སླ་སྟེ → **གྲོལ་བར་སླ་སྟེ** | ×7: after བ comes one narrow ར, with no ཡང. "Liberation is easy" against "liberation is also easy" |
| 84.3 | ཕྱིར་རོ༔ → **ཕྱིར༔** | No རོ. Same sense |
| 84.3 | འདིའི་སྐབས་སུ་འདི → འདིའི་སྐབས་སུ༔ འདི | ༔ printed |
| 84.4 | ཕན་པ་མེད༔ → **ཕན་པ་མེད་དེ༔** | Particle added |
| 84.4 | འདུལ་འཛིན་པའི → **འདུལ་བ་འཛིན་པའི** | Full form |
| 84.5 | མཚན་ཉིད་པའི་སྟོན་པ → **མཚན་ཉིད་ཀྱི་སྟོན་པ** | Same sense |
| 84.5 | རྣམས་ཀྱང་སྐབས → རྣམས་ཀྱང་༔ སྐབས | ༔ printed |
| 85.1 | གཡང་ས་ལ → **གཡང་ལ** | ×6: no ས between གཡང and ལ. "Fall into the abyss": the sense is unchanged, though གཡང་ས is the usual word. Kept, note only |
| 85.2 | ཐ་མའི་ཐ་མ་ཞིག → **ཐ་མའི་ཡང་ཐ་མ་ཅིག** | ཡང added ("even the lowest of the low"). ཅིག for ཞིག |
| 85.2 | རྣལ་འབྱོར་བ → རྣལ་འབྱོར་པ | Spelling |
| 85.3 | ལྟ་བུར་ཡི་དམ → **ལྟ་བུ་ཡི་དམ** | No ར. Same sense |
| 85.3 | ཡིན་པ་ངོ་ཤེས་པས་ཡིད་ཆེས་ཏེ༔ གཉིས → **ཡིན་པར་ངོ་ཤེས༔ ཡིད་ཆེས་ཏེ་གཉིས** | The print has no པས, and the ༔ falls after ཤེས instead of after ཏེ. The print reads "recognises [them] as yidam deities; trusting, [they] merge…". The recension reads "since [one] recognises, [one] trusts" |
| 85.4 | རྣམས་ལ་མངོན་རྟོགས་བསྒོམས → **རྣམས་མངོན་རྟོགས་སྒོམས** | No ལ. སྒོམས without the prefix བ (×6). The case relation is unmarked in the print. Same sense |
| 85.5 | ལ་སོགས་མཐོང | Same, with fillers after ལ |
| 85.5 | ཁོ་ནས་ཀྱང་འདིར → ཁོ་ནས་ཀྱང་༔ འདིར | ༔ printed |
| 85.5 | ཤར་བ་དང་༔ ངོ་ཤེས → **ཤར་བ་དང་ངོ་ཤེས** | No ༔ (×5, a clean gap). Same sense |
| 86.1 | འདུལ་འཛིན་གྱི་མཁན་པོ → **འདུལ་བ་འཛིན་པའི་མཁན་པོ** | |
| 86.1 | མཚན་ཉིད་ཀྱི་སྟོན་པ་ཆོས་སྤྱོད → **མཚན་ཉིད་ཀྱི་སྟོན་པའི་ཆོས་སྤྱོད** | "The dharma practice of the teacher" against "the teacher, in dharma practice". The structure differs slightly; the sense is close |
| 86.2 | མཁས་ཀྱང་གྲོངས་པའི་ཚེ༔གདུང་དང་རིང → **མཁས་ཀྱང་༔ གྲོངས་པའི་ཚེ་ན༔ གདུང་དང་༔ རིང** | ན added (×8, the tsheg between ཚེ and ན is clear). ༔ after ཀྱང and after དང |
| 86.2 | རིང་བསྲེལ → **རིངསྲེལ** | ×9: no prefix བ, and no tsheg between ང and ས (the head bars run together, with no blob). Kept as spelling; tsheg fix below |
| 86.3 | བློར་མ་ཤོང་པ་དང → **བློར་མ་ཤོང་དང** | ×7–×8: ཤོང is followed directly by ད-ང. There is no པ. Same sense |
| 86.3 | གཤེ་སྐུར | Same, with fillers after གཤེ (first dot taken as tsheg) |
| 86.4 | མཐོང་བ་ཞིག་གློ་བུར → **མཐོང་བ་གློ་བུར** | No ཞིག |
| 86.5 | དེའི་རྐྱེན་བྱས་ནས་ངན་སོང → **དེས[?]་རྐྱེན་བྱས་ངན་སོང** | ×7: བྱས is followed directly by ངན. There is no ནས. Same sense |
| **86.5** | འགྲོ་བས༔ **དེས**་འདུལ་བ་འཛིན་པ → **འགྲོ་བས༔ དེའིཕྱིར་འདུལ་བ་འཛིན་པ** | ×7: a clear gi-gu over འ and a second over the ཕྱ stack, then ར. The print has "**therefore**, a vinaya-holder…" (དེའི་ཕྱིར), where the recension has "thus…" (དེས). Same argument; a different connective |

Witness readings confirmed:
- ཞེ་ན༔
- ཧ་ཅང་ཡང་ཆེ་སྟེ
- ཐ་ན་སྐུ་གཟུགས་རིས་སུ
- འབུར་དུ་དོད་པ
- གནད་ཀྱང་དེ་ལྟར་ཡིན་ནོ
- ཇི་ལྟར་བརྩོན་ཞིང་༔
- འབྱོན་ཏེ (×8: naro over བྱ, ན, a free tsheg, ཏེ)
- གསང་སྔགས་ལ་གཤེ་སྐུར་བཏབ་པ
- དགྲར་སོང་ནས
- མཚན་ཉིད་པ་ཇི་ལྟར་བཟང་ཡང་༔

## Tsheg before ༔

- ང་༔ / ཅིང་༔ / ཞིང་༔ / ཀྱང་༔ / དང་༔ / ཡང་༔: the ring is fused to or abuts the ང. I kept the tsheg, following the convention of part 008.
- Every other ༔ has no tsheg, which is the plain reading:
  - པས༔, སྟེ༔, འགྲོའོ༔, ན༔
  - བས༔, ཕྱིར༔, སུ༔, དེ༔, དོ༔
  - ལོ༔, ཤེས༔, ནོ༔, ཏེ༔, ནས༔

## Proposed `# fix:` lines

```
# fix: དབང་མི་ཐོབབརྒྱལ => དབང་མི་ཐོབ་བརྒྱལ
# fix: ཐོབ་པའིགནད => ཐོབ་པའི་གནད
# fix: རིངསྲེལ => རིང་སྲེལ
# fix: རྣམྶརྒྱུས => རྣམས་རྒྱུས
# fix: དེའིཕྱིར => དེའི་ཕྱིར
```

These are:
- the line join 84.1→84.2;
- the line join 85.5→86.1;
- the mid-line tsheg at 86.2;
- the line-end subscript-ས abbreviation (མ + U+0FB6) written out across the join 86.3→86.4;
- the mid-line tsheg at 86.5. This last one is a close call. The head bars of འི and ཕྱི are continuous and no blob can be isolated. If the drafter takes the tsheg as fused, drop this fix.

Close calls not given a fix:
- 86.3 **ཤོང་དང**: the head bar runs on from ང to ད, with a raised bump (x 802–810, rows 225–227). I read the bump as a fused tsheg and kept it. If it is not a tsheg: `# fix: ཤོངདང => ཤོང་དང`.
- 86.5 **འགྲོ་བས**: the head bars of གྲོ and བ merge. The tsheg is kept. Same reasoning.

No line-end པའཾ / ལཾ / ནམཁའ forms occur on these pages.

## Suspected misprints

1. **84.2 བརྒྱལ་བབཁོར་ཡུག**. At ×10 there are two box letters (བ, then བ) with no tsheg between them, then ཁོ. The second བ is a dittography. Read as བརྒྱལ་བ་ཁོར་ཡུག་ཏུ་འོང ("fainting comes continuously"). The sense allows only that reading. Moderate certainty. Proposed: `# fix: བརྒྱལ་བབཁོར => བརྒྱལ་བ་ཁོར` (rule 5b, print's reading in the note).
2. **85.1 གཡང་ལ** for གཡང་ས་ལ: possibly a dropped ས, but གཡང alone also means "abyss". Kept, note only.
3. **86.2 རིངསྲེལ** for རིང་བསྲེལ: a spelling without the prefix. Kept (only the tsheg is fixed), note only.
4. 85.4 སྒོམས for བསྒོམས and 86.3 ཤོང་དང for ཤོང་བ་དང are the print's spellings or omissions. Kept, note only.

## Gaps

None. No […].
