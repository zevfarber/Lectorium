# read_C: pp. 120–121 (images n121–n122), plus the seam line 119.5 (n120), read from the images

## Lines, layout, and where text ga ends

- p. 120 (n121) has five lines. It is a leaf back, with no ornament. Skew is about −1.2°; I read it from a straightened copy. Headlines are at about 124, 180, 228, 276 and 324.
- p. 121 (n122) has five lines. It is a leaf front and opens with the swirl, `༔`, a wide blank, then `༔`, written `༄༅༔ ༔`. Skew is about +1.7°. Headlines are at about 140, 196, 252, 304 and 360. The left margin carries the usual leaf label, which I left out.
- p. 119 (n120) has a skew of about +0.7°. I read only line 5, for the seam.
- In all there are 10 print lines in read_C.txt, plus 119.5, which is only in this log.

**Seam with B (119.5 / 120.1).** I read 119.5 at ×4.5 as: `…[first stack unclear: ཉིད?]་ཡིད་ལ་བྱའོ༔ དུས་གསུམ་དུ་མ་ཆག་ ''(filler dots) པར་ཀློག་པར་བྱའོ༔ ཚིག་དོན་ཡིད་ལ་ཤིན་ཏུ་གསལ་བར་བྱའོ༔ གཤེད་མ་བརྒྱའི་དེད་ནས་བྱུང`.
- The line ends in `བྱུང`, and I see no tsheg before the frame. B should confirm this.
- p. 120 opens with `ཡང་འདིའི་ཚིག་དོན…`. The join is `བྱུང|ཡང`, "even if [a hundred executioners] come chasing". The seam is clean in sense. If B also sees no tsheg, it needs `# fix: དེད་ནས་བྱུངཡང་འདིའི => དེད་ནས་བྱུང་ཡང་འདིའི` (or however the editor joins across a page). B's reading of 119.5 governs; I read it only at ×4.5.

**END OF TEXT GA: 121.5, after `…གུས་པར་ཞུསོ།`.**
- This is the colophon's last sentence ("…I, Gagadharma(pa)mudra, respectfully requested it").
- After the shad, the rest of line 5 (about x≈1130–1850 of the straightened n122) is **blank**. Against the right frame, at line height, stands a single isolated `༔`. I wrote it as the last mark of the line (`ཞུསོ། ༔`). The editor may treat it as a closing ornament and leave it out of the text.
- **Nothing on p. 121 belongs to another text**: no new title, no new ornament line. Text ga ends on this page, and no sentence runs on to p. 122. Image n123 is not stored, but it is not needed.
- The other recension continues with a dedication (`འདི་བྲིས་དགེ་བས་སངས་རྒྱས་ཀྱི་བསྟན་པ…གནས་པར་གྱུར་ཅིག`). **This print does not have it.**

**Proposed `# name:`** `The benefits of hearing, and the colophon`. Alternatives: `Spreading the Great Liberation by Hearing; colophon`; `The end of the Reality Bardo: benefits and colophon`.
- pp. 120–121 cover how the text must be read aloud: to crowds, at the pillow of the sick, beside corpses. They say that meeting it is great fortune and that it is the essence of all dharma. Then comes the title closing "the pointing-out of the bardo of reality", and the colophon: Karma Lingpa's treasure from Mount Gampodar, passed to his son Chöje Lingpa, then to Guru Sūrya Candra, and requested by Gagadharma.
- For pp. 115–121 as a whole (with A/B's pages: the lama call, the bardo prayer, the instruction to recite it, the summary): `The bardo prayer, its benefits, and the colophon`.

## Method

- I found the skew per image by maximising the variance of the row profile (PIL only, since numpy is absent) and read everything on rotated copies.
- I found the line bands from the row profile. Each line was cropped in overlapping segments at ×4.5–×5.5.
- Doubtful syllables were enlarged ×7–×12 (bicubic, and once binarised with NEAREST).
- I used the other recension only to know which words to expect. The crops are deleted.

## [?] (9), no […] gaps

| place | as written | candidates / why |
|---|---|---|
| 120.1 | `ལྔ་བྱས[?]་པའི` | Two stacks: བ with a ྱ-like tail, then ས. The other recension has `བསགས`. The traces fit བྱས better, and the sense is the same: "who has committed / accumulated the five boundless acts". |
| 120.4 | `ཀློག[?]་པར་བྱའོ` (first word) | A ཀ (or ས) with ལ below and an o-sign. The other recension has `བསྒྲགས་པར་བྱའོ` ("proclaim"). The shape is the same as the clear `ཀློག` later on the same line and at 120.2, so I read `ཀློག` ("read [into everyone's ear]"). |
| 120.5 | `བྱང་བ[?]་མ་གཏོགས` | Between ང and གཏོ there is a blotched mass about two letters wide. The other recension has `བྱང་བ་རྣམས་མ་གཏོགས`. There is no room for རྣམས as well, and `བ་མ` fits the width. |
| 120.5 | `གལ་ཏེ་འཕྲད[?]་ན` | The first stack could be ར or འ, and the next is ཕྲ. The other recension has `གལ་ཏེ་ཕྲད་ན་ཡང`. The print has no ཡང: ད is followed directly by ན and then བློ. |
| 120.5 | `བློར་ཤོང[?]་བར་དཀའོ` | The letter after ར has three prongs and an o-sign. It looks more like ཡ (giving `ཡོང` "come [to mind]") than ཤ. The other recension has `ཤོང`, which is the idiom (`བློར་ཤོང` "fit in the mind"). I took ཤོང under the brief's rule. ཡོང is possible. |
| 121.3 | `སྒམ་པོ་བདར[?]་གྱི་རི` | The first letter is round-headed (བ) rather than ག. The other recension has `སྒམ་པོ་གདར`. It is a place name; I record it as printed. |
| 121.4 | `གུ་རུ་སུ་རྱ[?]་ཙནྡྲ` | The stacks between `རུ` and `ཙ` are cramped. The other recension has `སུརྱ་ཙནྡྲ་རསྨི`. The print has **no `རསྨི`**: `ཙནྡྲ་ལ་` ends the line. |
| 121.5 | `དྷརྨ་པ[?]་མུ་དྲས[?]` | The name is printed with no visible tshegs. I see `གྷ གྷ དྷ ཪྨ`, then a ཀ/པ-like letter, མུ (with a clear ུ), then ད/དྲ and ས. The other recension has `ག་ག་དྷརྨ་པ་མུ་དྲས`. The print writes `གྷ་གྷ` (with ྷ) where the other recension has `ག་ག`. The tsheg placement inside the name is mine. |

The two unsure readings in 121.5 (`པ` and `དྲས`) are counted separately: 9 marks in the file.

## Where the print differs from the other recension (print followed)

Spelling only (same sense):
- `ཀློག` for `བཀླག` (120.2, 120.4 three times).
- `སྐལ་པ` for `སྐལ་བ` (120.5).
- `བཟང་བ` for `བཟང་པ` (120.5).
- `གཅེས་སྤྲས` (121.1), the same in both.
- `གྷ་གྷ` for `ག་ག` (121.5).
- `ཅིག` for `གཅིག` (120.2 `ལན་ཅིག`).

Sense differences, or words added or left out:
- **120.2** `ད་ལྟ་ལན་ཅིག་ཚོར་བས` ("now, hearing it once"). The other recension has `དེ་ལྟར་ལན་གཅིག` ("thus, once"). The ད has no e-sign that I can see, and there is no ར after ལྟ.
- **120.2/3** `བར་དོར་རིག་པ` ("in the bardo, awareness…"). The other recension has `བར་དོའི་རིག་པ`.
- **120.3** `དེའི་ཕྱིར་གསོན་དུས་སུ` (no `པོའི`). The other recension has `དེའི་ཕྱིར་ན་གསོན་པོའི་དུས་སུ`.
- **120.4** `ཀུན་གྱི་རྣ་བར་ཀློག་པར་བྱའོ` ("read it into everyone's ear"). The other recension has `བསྒྲགས་པར་བྱའོ` ("proclaim").
- **120.4** `ནད་པ་ཐམས་ཅད་ཀྱི་སྔས་སུ` for `ནད་པ་ཀུན་གྱི`. Also `རྩར་ཀློག་པར` for `རྩར་བཀྲག་པར`.
- **120.5** `གལ་ཏེ་འཕྲད་ན` without `ཡང`.
- **121.1** `འདི་ཆོས་ཐམས་ཅད་ཀྱི་བཅུད` without `ནི`.
- **121.2** `ཞེས་བྱ་བ་ཆོས་ཉིད…` (no `༔` before `ཆོས`).
- **121.3** `རི་ལྷ་བྲན་|གར་བྱེད་པ` without `རི་བོ` and without `གྱིས` ("the mountain like a mountain-god servant dancing").
- **121.4** **`གར་བྱེད་པ་འདྲ་བའི་གནས་ནས`** ("from the place"). The other recension has `གཏེར་ནས` ("from the treasure"). The image clearly shows `གནས` at ×10.
- **121.4** `བཀའ་དང་ལུང་གཏད།` ("entrusted the command and transmission"). The other recension has `བཀའ་ལུང་གཏད་དོ༔`.
- **121.4** **`དེའི་གུ་རུ…`**, where the other recension has `དེས་`. It is clear as `དེའི`.
- **121.4–5** `ཙནྡྲ་ལ་|རིམ་པར་བཀའ་དང་ལུང་བབས་པ་ལགས་སོ།`: it lacks `རསྨི` and adds `རིམ་པར` ("in succession") and `དང་ལུང`.
- **121.5** It ends at `ཞུསོ།`. **The whole dedication `འདི་བྲིས་དགེ་བས…གྱུར་ཅིག` is absent.**

## Line-end tsheg status

- **With a tsheg:** 120.1 `ཡང་`; 120.2 `དོར་`; 120.3 `བར་`; 120.4 `ནི་`; 121.1 `བཅུད་`; 121.2 `སྤྲོད་`; 121.3 `བྲན་`; 121.4 `ལ་`.
- **No tsheg:** 120.5 `ཐོས`, which joins `ཐོས|[ornament]ནས` across the page (fix below). The seam line 119.5 `བྱུང` also appears to have none (see above; B decides).
- **Last line:** 121.5 ends with `།`, then a blank, then a lone `༔`.
- **Filler mark mid-line:** 120.3 `རིག་པ` is followed by a dash before `དགུ`. I left it out.
- **Mid-line:** at 121.2 `ཞེས་བྱ་བ་ཆོས` and in the 121.5 name the tshegs are fused or invisible. I wrote them by normal syllable division and propose no fix line.

## Fixes needed (`# fix:` lines)

```
# fix: བར་དཀའོ༔ འདི་ཐོས => བར་དཀའོ༔ འདི་ཐོས་
# fix: ངོ་སྤྲོད་རྫོགསོ༔ => ངོ་སྤྲོད་རྫོགས་སོ༔
# fix: གུས་པར་ཞུསོ། => གུས་པར་ཞུས་སོ།
```

- The first is the 120.5/121.1 page-join tsheg. Its context crosses the page boundary as `ཐོས|༄༅༔ ༔ནས`; the editor should adapt the fix to however page joins are stored.
- The other two write out contractions in which one o-sign stands over a single ས: `རྫོགསོ` (121.3) and `ཞུསོ` (121.5).
- There are no `པའཾ`, `ལཾ` or -གས ligature forms on these pages.

## Suspected misprints

None that need correcting. Kept, note only:
- 120.2 `ད་ལྟ་ལན་ཅིག` (the other recension has `དེ་ལྟར་ལན་གཅིག`). It reads acceptably as "now, once".
- 121.4 `གནས་ནས` for `གཏེར་ནས`. The sense holds ("from the place on Mount Gampodar"); the other recension's "treasure" should go in the note.
- 121.3 `བདར` for `གདར` in the place name: note only.

## Open

- Whether to keep the isolated final `༔` at 121.5 (printed, against the right frame after a blank).
- B should confirm 119.5, the tsheg after `བྱུང`, and its first stack.
