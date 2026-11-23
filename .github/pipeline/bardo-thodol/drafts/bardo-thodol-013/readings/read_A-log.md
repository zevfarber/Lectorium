# read_A: the rest of 115.5, then pp. 116–117 (images n116 l. 5, n117, n118), read from the images

## Lines and layout

- **p. 115 (n116)** has five lines (skew +1.1°). I read only line 5, after `…ཡི་དམ་རིན་པོ་ཆེ་ཞེས་བོས་ལ་གསོལ་བ་ཐོབ་ཅིག༔` (about x≈1470 on the straightened copy).
  - Nothing else sits between that `༔` and `ཁྱོད`. The small curved stroke just left of `ཁྱོ` is the head of the ཁ, not a shad.
  - The line ends `བླ་མའི་`, with a tsheg, followed by filler dots, which I left out.
  - So `{115}` in read_A.txt holds only `ཁྱོད་རང་གི་བླ་མའི་`.
- **p. 116 (n117)** has five lines (skew −1.4°). It is a leaf back with no ornament. Headlines are at about 132, 184, 236, 290, 342.
- **p. 117 (n118)** has five lines (skew +1.1°). It is a leaf front and opens with the swirl, `༔`, a wide blank, `༔`, written `༄༅༔ ༔` as in 012. Headlines are at about 150, 206, 262, 318, 372.
- In all, read_A.txt has 11 print lines: 1 part-line on p. 115 and 5 + 5 on pp. 116–117.

**Content.**
- 116.1 closes the call on the lama.
- 116.1–2 is the call on the blood-drinkers and "take this prayer too".
- At 116.2 the verse prayer begins (`ཀྱཻ་མ་བག་ཆགས་དྲག་པོས…`), and it runs through p. 117.
- p. 117 ends mid-verse at `འབྱུང་ལྔའི་ཁམས་`, followed by filler dots. B continues on 118.1, presumably with `རྣམས་སྒྲ་རུ…` as in the other recension.

## Method

- I found the skew by maximising the row-profile variance (PIL only, since this python has no numpy). All reading was done on rotated copies.
- I took line bands from the row profile and cropped each line in four overlapping segments at ×3 (LANCZOS).
- Doubtful syllables I cropped at ×6–×11, some binarised. I also made side-by-side montages:
  - the ང of 116.1 `བཏང` against the ང of `འཐུང` on 116.2;
  - the doubtful letter in 117.1 `འཇིགས་ང` against `པ` (117.2 `ཤེས་པར`) and `ང` (117.1 `དངངས`).
- witness_ga.txt was used only to know which words to expect. The crops have been deleted.

## [?] (5); no […] gaps

| place | as written | candidates / why |
|---|---|---|
| 116.1 | `ཐུགས་རྗེས་མ་བཏང་ཞིག[?]་གྱིས་ལ` | After `བཏང`, at ×10, I see one stack with an i-sign, then ག, then `གྱིས`. The stack's letter has the notch and long down-right tail of ཞ, like the ཞ of `ཞི་ཁྲོའི` on 116.3. `གྱིས` is certain: it is the same stack as in 116.2 `མོས་བ་གྱིས་ལ`. So the reading is "do not abandon [me] with your compassion!" (cf. 115.5 `ཐུགས་རྗེས་བཟུང་ཞིག`), followed by `གྱིས་ལ་གསོལ་བ་ཐོབ་ཅིག`. **This corrects C's ×3 provisional `མ་བཏང་བར་གྱིས་ལ`:** there is no ར. The other recension has `མ་གཏང་གྱིས་ལ`. |
| 116.3 | `འཇིགས་སྣང་སྤངས[?]་པའི` | Filler dots follow `སྣང`. Then comes a short stack: a པ-box with a small element above it, which may be a compressed ས. Then `ངས`. The other recension has `སྤངས་པའི`, and nothing else fits. |
| 117.1 | `ཐུགས་རྗེའི་ཤུགས[?]་ཕྱུངས༔` | I see ཤ with ུ, then a narrow joined element, which I take for the -གས ligature (the editor writes it གས). Then come `ཕྱུ`, ང and ས. There is no `ནས`. The other recension has `ཐུགས་རྗེས་ཤུགས་ཕྱུངས་ནས`. |
| 117.1 | `བར་དོའི་འཇིགས་ང[?]་མི་འབྱུང་ཤོག` | Between `འཇིགས` and `མི` there is one letter. It has a top bar and a diagonal running down to the left, which is the ང shape. It is clearly not the box of པ. The verse needs one syllable here: other recension `འཇིགས་པ`; cf. this print's `འཇིགས་སྣང` at 116.3. See Suspected misprints. |
| 117.4 | `ཐུགས་རྗེ་ཆེན་པས[?]་བདག་ལ` | I see no o-sign over པ. The space above it is crowded with strokes from line 3, so an o-sign could be hidden. The other recension has `ཆེན་པོས`. See Suspected misprints. |

## Where the print differs from the other recension (print followed)

Spelling and particles only (same sense):
- 116.2 `མོས་བ` for `མོས་པ`. `ཀྱཻ་མ`, with two e-signs as usual, for `ཀྱེ་མ`.
- 116.3 and 117.1 `དངངས་སྐྲག` for `སྔངས་སྐྲག` (the print's spelling, as in 012).
- Instrumental `-ས` is missing:
  - 116.4 `ཚོགས་ཀྱི་རྒྱབ་ནས` (`ཀྱིས`);
  - 117.1 `རྣམས་ཀྱི` (`ཀྱིས`);
  - 117.3 `དབང་གི` (`གིས`) and `ལྷ་ཡི` (`ཡིས`);
  - 117.5 `ལས་ཀྱི` (`ཀྱིས`).
  These are the print's habit (conventions: `གཅིག་གི for གིས`), so I propose no fix.
- 116.5 `སྟོང་པའི` for `སྟོང་བའི`.
- 117.4 `སྐྱབ་ཏུ་གསོལ` for `བསྐྱབ་ཏུ`.
- 116.1 `ལ༔` after `བརྗོད` (other recension `ལ་`).

Sense differences:
- **116.1** `བདག་བར་དོར་འཁྱམས་ནས་ཡོད་པས`: the print adds `བདག` ("I am wandering in the bardo"), as in the yidam call at 115.4–5. Also `ཐུགས་རྗེས་མ་བཏང་ཞིག་གྱིས་ལ` (see [?]), where the other recension has `མ་གཏང་གྱིས་ལ`.
- **116.2** `ཁྲག་འཐུང་གི་ལྷ་ཚོགས་རྣམས་ལ་ཡང་མོས་བ་གྱིས་ལ`. The print adds `རྣམས` and `ཡང` ("to the blood-drinking deities too, be devoted").
- **116.5** `གཅིག་པུར་འཁྱམས` ("wander alone"), where the other recension has `གཅིག་པར`. `པུ` is clear, with a ུ loop.
- **117.1** `ཐུགས་རྗེའི་ཤུགས་ཕྱུངས༔` ("put forth the force of compassion"). The other recension has `ཐུགས་རྗེས་ཤུགས་ཕྱུངས་ནས`. The print lacks `ནས`, and its verse line has eight syllables.
- **117.1** `འཇིགས་ང[?]`, where the other recension has `འཇིགས་པ` (see misprints).
- **117.3** `སྡུག་བསྔལ་སེལ་བར་ཤོག`: the print adds `བར`, giving a ten-syllable line. The other recension has `སེལ་ཤོག`.
- **117.4** `ཐུགས་རྗེ་ཆེན་པས[?]`, where the other recension has `ཆེན་པོས`.
- **117.5** `ཏིང་འཛིན་ཆཱར་བར་ཤོག` (= `འཆར`; see fixes).

**Seam with B (117.5 → 118.1).** The other recension goes on `…ཁམས་རྣམས་སྒྲ་རུ་མི་སྡང་ཞིང་…`. B should confirm that 118.1 opens with `རྣམས`.

## Line-end tsheg status

- **With a tsheg:**
  - p. 115: 115.5 `མའི་`.
  - p. 116: 116.4 `རུ་` (a dot close after རུ, before the filler); 116.5 `རྒྱས་` (a dot, then filler).
  - p. 117: 117.1 `འཆར་` (a dot at the frame); 117.2 `ཤེས་` (a dot).
- **With a tsheg written, but it cannot be told from the filler dots that follow:** 116.2 `བར་`, 116.3 `དབྱིངས་`, 117.4 `སྐྱབ་` (dashes), 117.5 `ཁམས་`. I wrote the tsheg, as C did.
- **Ending in ༔:** 117.3 `ཙ་ན༔`.
- **No tsheg (fix below):** 116.1 `ཁྲག`, which runs right against the right frame.
- **Mid-line filler** (left out, tsheg written):
  - 116.3 `སྣང…སྤངས`;
  - 117.3 `ཙ…ན` (twice);
  - 117.4 `རྗེ…ཆེན`;
  - 117.5 `ཙ…ན`.
- At 116.1 `བཏང་ཞིག་གྱིས` the tshegs are fused into the head bar. I wrote them by syllable division, so there is no fix.

## Fixes needed (`# fix:` lines)

```
# fix: གསོལ་བ་ཐོབ་ཅིག༔ ཁྲག => གསོལ་བ་ཐོབ་ཅིག༔ ཁྲག་
# fix: ཏིང་འཛིན་ཆཱར་བར => ཏིང་འཛིན་འཆར་བར
```

- **116.1/2.** The `ཁྲག|འཐུང` line join has no tsheg.
- **117.5.** The cutter set the prefix འ small, *beneath* ཆ, rather than before it. This is a space-saving stack or a later insertion; at ×11 there is a clear little a-chung under ཆ. I wrote it as printed with U+0F71 (`ཆཱར`). Written out it is `འཆར`.
- There are no `པའཾ`, `ལཾ` or subscript-ས contractions on these lines.

## Suspected misprints

1. **Page-turn dittography, 116.5/117.1.** 116.5 ends `…སངས་རྒྱས་` and 117.1 opens, after the ornament, with `རྒྱས་རྣམས་ཀྱི…`. So `རྒྱས` is printed twice across the leaf turn. Both are clear at ×7. Certainty: high. Proposed:
   `# fix: ༄༅༔ ༔རྒྱས་རྣམས་ཀྱི => ༄༅༔ ༔རྣམས་ཀྱི` (rule 5b; the note gives the print's reading).
2. **117.1 `འཇིགས་ང[?]་མི་འབྱུང`.** `ང` is not a word here, and the verse needs one syllable. The candidates are `པ` (other recension) and `སྣང` (this print's `འཇིགས་སྣང` at 116.3). Both give "may the terror / terrifying appearances of the bardo not arise", so the sense is the same either way, but which word was meant is not certain. **Kept, note only** (or `པ` if the editor wants a letter-level correction).
3. **117.4 `ཆེན་པས[?]`** for `ཆེན་པོས`. The o-sign is dropped or hidden. Only `ཐུགས་རྗེ་ཆེན་པོས` ("by great compassion") makes sense. Certainty: moderate. Proposed: `# fix: ཐུགས་རྗེ་ཆེན་པས་བདག => ཐུགས་རྗེ་ཆེན་པོས་བདག`. If the editor treats the o-sign as only hidden by the crowding, the same fix applies.

## Open

- B should check 118.1 for `རྣམས` and the seam.
- The editor decides on the `རྒྱས` dittography and on `འཇིགས་ང`.
