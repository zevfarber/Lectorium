# read_B: pp. 118–119 (images n119–n120), plus the seam line 117.5 (n118), read from the images

## Lines and layout

- **p. 118 (n119)** has five lines. It is a leaf back, with no ornament. Skew about −1.4°. Headlines at about 124, 182, 236, 292, 342 on the straightened copy.
- **p. 119 (n120)** has five lines. It is a leaf front and opens with the swirl, `༔`, a wide blank, then `༔`, written `༄༅༔ ༔`. Skew about +0.7°. Headlines at about 146, 200, 254, 308, 362.
- **p. 117 (n118)**, skew about +1.1°: I read only line 5, for the seam.
- In all there are 10 print lines in read_B.txt, plus 117.5 in this log only.

**Content.** These pages hold:
- the end of the bardo prayer (118.1);
- the instruction to say it three or seven times, and the promise that this frees anyone (118.1–3);
- the forward reference to the srid pa'i bar do (118.3–4);
- the value of habituation and of practice while alive (118.4–119.3);
- the injunctions to keep, read, master and recite this text (119.3–5).

p. 119 ends mid-sentence: `…གཤེད་མ་བརྒྱའི་དེད་ནས་བྱུང|`, and p. 120 opens `ཡང་འདིའི་ཚིག་དོན…`. I looked only at the first syllables of n121 to check the join.

## Seam with A (117.5)

I read 117.5 (n118 line 5) as:
`ཏུ་གསོལ༔ བག་ཆགས་ལས་ཀྱིས་སྡུག་བསྔལ་མྱོང་ཙ་ན༔ འོད་གསལ་བདེ་བའི་ཏིང་འཛིན[?] X[?]ར་བར་ཤོག༔ འབྱུང་ལྔའི་ཁམས་`

- `མྱོང་ཙ` is followed by a tsheg and filler dots, then `ན༔`. That makes it `ཙ་ན`; the filler dots are left out.
- **ཏིང་འཛིན X-ར་བར་ཤོག.** After `ཏིང་འཛི` there is a small `ན`-like mark with a dot. Then comes a tall stack: a ཆ/ས-like head with a small ཀ/ཏ-like letter hanging below, and after it a `ར`. The other recension has `ཏིང་འཛིན་འཆར་བར་ཤོག`. I could not resolve it at ×10 and leave it to Reader A. (`འཆར`, or perhaps `སྐྱེ…`, would be the candidates, but neither fits the stack well.)
- The line ends `ཁམས` followed by a run of filler dots. The first dot sits at tsheg height, so I take it as `ཁམས་`.
- 118.1 opens `རྣམས་སྒྲ་རུ…`. The join `ཁམས་|རྣམས` is clean and needs no fix.

## Method

- Skew found by maximising the variance of the row profile, in 0.1° steps, using PIL only (no numpy). All reading was done on rotated copies.
- Line bands came from the row profile. Each line was cropped in five overlapping segments at ×3, then again in seven segments at ×5.
- Doubtful syllables were enlarged ×6–×10, some binarised and enlarged NEAREST.
- witness_ga.txt was used only to know which words to expect.

## [?] (8), no […] gaps

| place | as written | candidates / why |
|---|---|---|
| 118.4 | `འཁྱམས་དགོས་པས[?]༔` | The letter before the final ས is blotted. Its top-left corner looks closed (བ) at ×9, but the image is not clear. The other recension has `དགོས་པས`; `བས` is the alternative. The sense is the same. |
| 118.4 | `ངོ་སྤྲོད་འོག[?]་ཏུ` | The first letter has an o-sign over it and is cramped (འ or ར-like). Then come a clear `ག` and `ཏུ`. The other recension has `འོག་ཏུ` ("below"); `རོག` is no word. |
| 118.4 | `སྤྱིར[?]་གོམ་པ` | A three-tier stack: box, zigzag, then a ྱ-hook. The i-sign is merged with a descender from line 3. Then comes `ར`. The other recension has `སྤྱིར`; `ཕྱིར` is the alternative. It is not the ༈ that the other recension has here; the print has no ༈ (see below). |
| 118.5 | `ཆོས་ཉིད་ལམ་གྱིས་འོངོ[?]༔` | After `གྱིས` there is a narrow letter (འ, perhaps ཡ) with an o-sign, then `ང` with an o-sign, then `༔`, against the frame. I read a contraction for `འོང་ངོ` (other recension `འོང་ངོ`). This print writes `ཡོང་ངོ` at 113.5 and 114.2, so `ཡོངོ` = `ཡོང་ངོ` is possible. The sense is the same either way. |
| 119.3 | `ཆོས་ཉིད་བར་དོ[?]་ལས` | I see no o-sign over ད, but a descender from line 2 crosses exactly there, and the o-sign may be merged into it. `བར་དོ` is the only reading that makes sense. |
| 119.3 | `ཞི་ཁྲོའི[?]་སྣང་བ` | There is a clear `ཞི`, then `ཁྲ`, then `འ` with an i-curl. The o-sign over ཁྲ is lost among strokes from line 2. The other recension has `ཞི་ཁྲོའི`. |
| 119.3 | `གསོན[?]་པོའི་དུས་སུ` | The o-sign over ས is hidden by a subscript from line 2 (the `ྔ` of `སྔགས`). The `པོའི` after it is clear. |
| (118.1) | `སྒྲ་རུ` (no [?] in the file) | A three-tier stack: a small ས head, ག, then ྲ. There is no separate letter before it (the ས before it ends `རྣམས`), so `དགྲ` is ruled out. The other recension has `སྒྲ`. Listed here because `ལྡང` would ordinarily pair with `དགྲ` (see the sense differences). |

## Where this print differs from the other recension (print followed)

Spelling only (same sense):
- 118.2 `གསུམ་འམ` for `གསུམ་མམ`.
- 118.4 `གོམ་པ`, and 118.5 `གོམ་འདྲིས`, for `གོམས་`.
- 118.5 `མང་བས` for `མང་པས`.
- 119.2 `གསོན་པའི` for `གསོན་པོའི`.
- 119.2 `བསྒོམ་པ` for `བསྒོམས་པ`.
- 119.4 and 119.5 `ཀློག` for `ཀླག`/`བཀླག`.
- 119.5 `མ་ཆག་པར` for `མ་ཆགས་པར`.
- 118.4 `གང་ལ་ཡང` for `གང་ལའང`.

Sense or wording differences:
- **118.1** `སྒྲ་རུ་མི་ལྡང་ཞིང` ("may [the elements] not rise up as sounds"). The other recension has `སྒྲ་རུ་མི་སྡང་ཞིང` ("not be hostile as sounds"). The verb ལྡང is clear: ལ with ད subjoined.
- **118.1** `ཅེས་མོས་གུས…` without `དེ་སྐད`.
- **118.3** `དེ་ནི་སྡིག་པ…` ("as for this…"). The other recension has `དེས་ནི` ("by this…"). `ལས་འཕྲོ` stands without `ནི`.
- **118.3/4** `ངོ་མ་འཕྲོད་ན་ནི༔ བར་དོ་གསུམ་པ་སྲིད་པའི་བར་དོར…` (the other recension has `ན༔ … སྲིད་པ་བར་དོར`).
- **118.4** There is **no ༈** before `དེའི་ངོ་སྤྲོད`; the other recension has one.
- **118.4** `གོམ་པ་ཆེ་ཆུང` ("great or small habituation"). The other recension has `གོམས་འདྲིས་ཆེ་ཆུང`.
- **118.5** `བག་རེ་འཁྲུལ་བ`, without `ཙམ`. The sense ("a little confusion") is kept by `བག་རེ`.
- **118.5** `གོམ་འདྲིས་ཆེ་བ་རྣམས་ལ` (the other recension has `གོམས་པ་ཆེ་བ`). The two recensions have the two words swapped between 118.4 and 118.5.
- **119.1** `གསོན་པོས་དུས་སུ` (the other recension has `གསོན་པོའི`). See Suspected misprints.
- **119.1** `ཉམས་མྱོང་ཡོད་པ་རྣམས་ནི་འཆི་ཁའི` adds `ནི`.
- **119.1/2** **`འོད་གསལ་ཤར་བའི|སྟོབས་ཤིན་ཏུ་ཆེ་བས`** ("the power of the dawning of clear light is very great"). The other recension has `ཤར་བའི་དུས་སུ༔ སྟོབས་ཤིན་ཏུ་ཆེ་བས` ("at the time when clear light dawns, [their] power is very great"). The print lacks `དུས་སུ`, and the sentence still reads.
- **119.2** `གསོན་པའི་དུས་སུ་ཉམས་ལེན` adds `སུ`.
- **119.3** `ཆོས་ཉིད་བར་དོ་ལས` (ablative). The other recension has `བར་དོ་ལ`.
- **119.3/4** `གསོན་པོའི་དུས་སུ་ཡང་བར་|དོ་ཐོས་གྲོལ་འདི་ཁྱད་པར་དུ་ཡིད་ལ་བྱང་བར་བྱེད་པ་ནི་ཤིན་ཏུ་གལ་ཆེའོ`. The other recension has `…ཡང་ཁྱད་པར་བར་དོ་ཐོས་གྲོལ་འདི་ཡིད་ལ་ཤིན་ཏུ་བྱང་བར་བྱེད་པ་ནི་གལ་ཆེའོ`.
  - In the print, `ཁྱད་པར་དུ` comes after `འདི`, and `ཤིན་ཏུ` qualifies "important" instead of "familiar". The meaning is: "it is extremely important to make this especially familiar to the mind".
- **119.4** The order of the injunctions is `བཅང་བར` / `ཀློག་པར` / `ཀུན་ཆུབ་པར`. The other recension has `བཅང` / `ཀུན་ཆུབ` / `ཀླག`.
- **119.5** `དུས་གསུམ་དུ་མ་ཆག་པར་ཀློག་པར་བྱའོ` (the other recension has `བཀླག་བྱའོ`).

## Line-end tsheg status

- **With a tsheg:** 118.2 `བདུན་`; 118.4 `ཁར་`; 119.3 `བར་`; 119.4 `ཚུལ་`.
- **Ending in ༔:** 118.1 `ཅིག༔`; 118.3 `ནི༔`; 118.5 `ངོ༔`.
- **No tsheg (fixes below):** 119.1 `བའི`, 119.2 `བསྒོམ`, 119.5 `བྱུང`.
- **Filler marks mid-line**, left out with the tsheg written:
  - 118.4 `བར་དོ་`, then filler dashes, then `གསུམ`;
  - 119.1 `རིག་`, then a dash, then `ཐོག`;
  - 119.5 `ཆག་`, then filler dots, then `པར`.
- **Mid-line:** tshegs are fused or invisible at 118.2 `འཇིགས་སྐྲག` and 119.3 `ན་ནི༔`. I wrote them by normal syllable division, so there is no fix line.

## Fixes needed (`# fix:` lines)

```
# fix: འོད་གསལ་ཤར་བའིསྟོབས་ཤིན => འོད་གསལ་ཤར་བའི་སྟོབས་ཤིན
# fix: བསྐྱེད་རྫོགས་བསྒོམཔ་རྣམས => བསྐྱེད་རྫོགས་བསྒོམ་པ་རྣམས
# fix: ལམ་གྱིས་འོངོ༔ => ལམ་གྱིས་འོང་ངོ༔
# fix: དེད་ནས་བྱུངཡང => དེད་ནས་བྱུང་ཡང
```

- The last fix spans the 119.5/120.1 join. 120.1 opens `ཡང་འདིའི་ཚིག་དོན`, which is Reader C's line, so it should go in whichever part holds the join.
- There are no `པའཾ`, `ལཾ` or subscript-ས forms on these pages. The only contraction is `འོངོ` at 118.5.

## Suspected misprints

1. **119.1 `གསོན་པོས་དུས་སུ` → `གསོན་པོའི་དུས་སུ`.** The image shows `པོ` followed by a three-pronged `ས`, with no i-sign, at ×8 binarised. "At the time of being alive" needs the genitive. The print writes `གསོན་པའི་དུས་སུ` at 119.2 and `གསོན་པོའི་དུས་སུ` at 119.2 and 119.3, and the other recension has `གསོན་པོའི`.
   - Certainty: moderate.
   - Proposed: `# fix: གསོན་པོས་དུས་སུ་རིག => གསོན་པོའི་དུས་སུ་རིག` (rule 5b). Alternatively, keep it with a note only.
2. **119.1/2 omission of `དུས་སུ`.** The sentence reads as it stands, so it is kept, note only.
3. **119.3 `བར་དོ་ལས`** for `ལ`. It reads ("from the bardo of reality"), so it is kept, note only.

## Open

- The stack at 117.5 (`ཏིང་འཛིན X-ར་བར་ཤོག`) is for Reader A to settle.
- The first letter of `འོངོ` at 118.5 may be ཡ (giving `ཡོངོ`). Either way it is written out as `…ང་ངོ`.
