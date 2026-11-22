# read_A: pp. 72–74 (leaves n73–n75), established from the images

Line counts: p. 72 has five lines (a leaf back, no ornament; checked). p. 73 has five lines (a leaf front, opens ༄༅༔ ༔ with a wide blank between the two ༔, both clear on n74). p. 74 has five lines (a leaf back, no ornament). That makes 15 print lines.
The witness's line breaks match the print on every line (15 of 15).

**Seam with part 007.** As the brief asks, all of p. 72 is transcribed. 72.1 and the start of 72.2 are already in source/established/bardo-thodol-007.txt, and my reading of them agrees with it letter for letter (72.1 མཁའགྲོ, 72.1 ཅིང་༔, 72.2 འོང་ངོ༔ with no tsheg).
The seam falls mid-line on 72.2, right after …ཕྱག་རྒྱ་ནམ་མཁའ་ལ་མཛད་པ་ཅིག་འཆར་དུ་འོང་ངོ༔ and its following space. **Part 008 begins on 72.2 with དཀྱིལ་འཁོར་དེའི་ཤར་ནས་ས་ལ་གནས་པའི་རིག་འཛིན…** The assembler should drop all of 72.1 and the 72.2 text up to and including འོང་ངོ༔.

Method: I found the line bands from the row profile. Headlines are at about n73 140/190/245/290/350, n74 135/190/245/300/355 and n75 135/195/245/300/355. The lines slope by up to about 15 px, so I re-cut bands locally where needed. Each line was cropped in four overlapping segments at ×3 (LANCZOS). Doubtful syllables were cropped at ×5–×8, with pixel dumps (threshold 128) for tshegs and letter shapes. I checked every ངོ(་)༔ at ×5 side by side. A connected-component pass found the separate tsheg blobs (73.4 x 927–933; 73.5 x 1773–1779).

## The image overruled the witness (18 changes in 17 rows)

| page.line | witness → print | why |
|---|---|---|
| 72.1 | མཁའ་གྲོ → མཁའགྲོ | As read for part 007 (×10 there). ×3 here: ཁ, one འ and གྲོ run on with no tsheg. The contraction is on the 007 side of the seam |
| 72.2 | འོང་ངོ་༔ → འོང་ངོ༔ | ×5: the tail of ངོ runs into the ༔ with no dot, as part 007 found. Compare 72.4, where the dot is clear |
| 72.3 | འཛིན་པའི → འཛུམ་པའི | ×6: the stack is ཛ with a zhabs-kyu hook, then མ. No ན. "A smiling radiance", the same formula as 73.2 འཛུམ་པའི. The other recension also has འཛུམ |
| 72.3 | འཁྱིལ་ཞིང → འཁྲིལ་ཞིང | ×8: under ཁ is the short bar-and-tick of ra-btags, not the curled ya-btags. The same shape as 72.1/72.5 འཁྲིལ |
| 72.3 | ཐོག་ཁྲག → ཐོད་ཁྲག | ×7: the letter after ཐོ is ད (long right tail), followed by a tsheg. As at 72.1 and 73.3 |
| 72.3 | (line end) བལྟ་ → བལྟ | Pixel dump: ལ ends at x 1806 and the frame starts at 1818. The gap is clean at headline height. Needs `# fix` |
| 72.4 | (line end) སྐུ་མདག → སྐུ་མདོག[?] | ×8 and pixel dump: a naro-shaped stroke (x 1767–1806, rows 272–282) hangs above ད–ག. It is separate from the ཏ of 72.3 བལྟ above, whose tail ends at row ~271, and no such stroke stands under the བལྟ of 72.1. The witness's མདག is no word. No tsheg after ག (the gap x 1803–1807 to the frame is clean). Needs `# fix` |
| 73.1 | ནམ་མཁའ་མཛད → ནམ་མཁའ་ལ་མཛད | ×3/×7: a ལ stands between མཁའ and མཛད, as in every other instance of the formula |
| 73.2 | ཞེས་གྱ་བ༔ → ཞེས་བྱ་བ༔ | ×8: the letter is a closed box, so བ (not ག with its notch), with ya-btags under it |
| 73.3 | ཅིག་དུ་འོང → ཅིག་འཆར་དུ་འོང | ×3: འཆར is clearly printed. The witness dropped a word |
| 73.3 | (line end) ལྷུན → ལྷུན་ | Pixel dump: a separate blob (x 1819–1822, rows 260–267) stands at headline height between ན (ends 1814) and the frame (1824). Read as a tsheg. A close call (see below) |
| 73.4 | ལྗང་ཁུ་སྐུ → ལྗང་ཁུསྐུ | Pixel dump: ཁུ (x 1605–1629, with the hook below) and the ས of སྐུ (from x 1631) are 1 px apart at the head bar, and no blob stands between them. A tsheg does stand between ང and ཁུ (x 1598–1602). Needs `# fix` |
| 73.5 | ཐོད་ཁྲུག → ཐོད་ཁྲག | ×6: ཁ with ra-btags, then ག. Nothing below the stack |
| 74.1 | རིགས་བཞིའི་མཁའ་འགྲོ༔ → …མཁའ་གྲོ༔ | Pixel dump: ཁ, one འ (x 1700–1721), a tsheg (x 1723–1729, rows 134–138), then གྲོ with no འ prefix. Abbreviation, needs `# fix` |
| 74.2 | རྣམས་དང་༔ དཔའ་མོ་དང་༔ → རྣམས་དང་༔ དཔའ་བོ་དང་༔ དཔའ་མོ་དང་༔ | ×3: the print has both དཔའ་བོ་དང་༔ and དཔའ་མོ་དང་༔. The witness skipped one (eye-skip). The other recension has both too |
| 74.2 | (line end) ཆོས་ → ཆོས | Pixel dump: ས (x 1846–1860) touches the frame (1862). There is no room for a dot. Needs `# fix` |
| 74.5 | འོང་ངོ་༔ → འོང་ངོ༔ (2×) | ×5 side by side: in both (…འགུལ་འགུལ་དུ་འོང་ངོ༔ and …འདིར་བ་འོང་ངོ༔) the ༔ ring abuts ངོ with no free dot. Compare 72.4, 73.1, 73.3, 73.5, where a dot is clear |

In all there are:
- 8 letter/word changes: 72.3 འཛུམ, 72.3 འཁྲིལ, 72.3 ཐོད, 72.4 མདོག, 73.1 ལ added, 73.2 བྱ, 73.3 འཆར added, 73.5 ཁྲག, plus 74.2 དཔའ་བོ་དང་༔ added and 74.1 འ dropped (10 counting those two).
- 1 contraction recognised: 72.1 མཁའགྲོ (part 007's side).
- 1 tsheg removed inside a line: 73.4 ཁུསྐུ.
- 3 tsheg-before-༔ removals: 72.2, 74.5 ×2.
- 3 line-end tsheg changes: 72.3 removed, 74.2 removed, 73.3 added. The witness already had none at 72.4.

Line-end tsheg status (all 15):
- With a tsheg: 72.1 བལྟ་ (tsheg, then fillers), 72.2 སྐུ་, 72.5 བལྟ་ (tsheg, then fillers), 73.1 རིག་, 73.2 དང་, 73.3 ལྷུན་ (close call), 73.4 འཁྲིལ་, 74.1 གནས་ (blob x 1851–1856 before the frame), 74.4 ཁམས་.
- Ending in ༔: 73.5, 74.3.
- No tsheg (fixes below): 72.3 བལྟ, 72.4 མདོག, 74.2 ཆོས, 74.5 གར.
- **My first line** (72.1) ends བལྟ་ with a tsheg. **Part 008's first line** is 72.2 from the seam, and it ends སྐུ་ with a tsheg. **My last line** (74.5) ends གར with NO tsheg (z ×6: clean white to the frame). The join to p. 75 crosses the leaf-front ornament (see fixes).

## Tsheg before ༔ (witness confirmed or kept)

- **ངོ་༔ with a clear free dot**: 72.4, 73.1, 73.3, 73.5. The pixel dump for 72.4 shows a blob at x 927–933, rows 294–299, separate on both sides. These confirm the witness.
- **ངོ༔ with none**: 72.2 and 74.5 ×2 (table above).
- **ཅིང་༔** (72.1, 72.3, 72.5, 73.3, 73.5): the ring's upper-left wall is thicker than its right wall (7 px against 5 px at 72.5; a bump on the top-left at 72.3, as part 007 found at 72.1). It reads as a fused tsheg. Kept as in the witness.
- **དང་༔** on p. 74 (74.1, 74.2 ×4, 74.3 ×4, 74.4 ×3): the ring is fused to or abuts the ང. Some show a thickened left wall or a dot on the ring's upper-left (×5 montage of 74.2). Not decidable as a free blob, so the witness's tsheg is kept, as with the fused tshegs on p. 61.
- **None, as in the witness**: every other ༔ (བ༔, པ༔, ནས༔, འགྲོ༔, ཤིག༔, ཏེ༔).

## Witness readings checked and confirmed, though they look odd

- 72.3 ཡུམ་མཁའ་འགྲོ་དཀར་མོ: no མ after འགྲོ (×6). The other recension has མཁའ་འགྲོ་མ་དཀར་མོ.
- 72.3 འཁྲིལ་ཞིང་གྲི་གུག: ཞིང, with no ༔ (the other recension has འཁྲིལ་བ༔).
- 72.5 **ལྡན་བ༔**: ×8, a closed box (བ), not the open-left པ of 72.3 ལྡན་པ༔. Print's own spelling (compare ཞུས་བ). Kept.
- 72.5 ཐོད་ཁྲག་གིས་གར (with ས), against 72.3/73.3 གི་གར.
- 72.5 འགྲོ་མ: the tsheg between གྲོ and མ is fused to the head bar of མ (blob x 926–930 hanging below the bar). Kept.
- 73.1 **པ་གཅིག** (×7: prefix ག before ཅི), against ཅིག everywhere else in the formula.
- 73.4 ཞིང་ཞལ་ཁྲོ་འཛུམ: ×6, ང (diagonal down-right), not ད.
- 73.5 ཐོད་ཁྲག་འཛིན་པས་གར (not གི་གར).
- 74.1 རིག་ + filler dots + འཛིན: there is a run of three dots mid-line after རིག (×6). The first is taken as the tsheg and the fillers are left out, as at 61.3.
- 74.1 **ཀྱི་རོལ་དུ**: ×8, ཀ with ya-btags and gi-gu, then ར with naro, then ལ. No ཕྱི (see misprints).
- 74.1 **ཚོགས་དབག་ཏུ**: ×8 montage against the པ of མེད་པ in the same line. This letter is a closed box with an enclosed white triangle (བ). The པ is open on the left. So the witness's དབག is right. **At 74.4 the print has དཔག་ཏུ** (×7, open-left པ).
- 74.2 གསུམ་མཁའ་འགྲོ (no གྱི), and གིང་དང.
- 74.3 རུས་པའི་ + filler dots + རྒྱན: a mid-line filler run. Fillers are left out.
- 74.3 བསྲུང་མ.
- 74.4 བླ་བྲེས (the other recension has བླ་རེ).
- 74.5 ཁེངས་པ་ཤིག་ཤིག༔: the separators after པ and after the first ཤིག each show a second dot below the tsheg (pixel dump x 497–503 / 562–567). It looks like a stray mark, not a ༑ or ཿ. Written as a tsheg.
- 74.5 མགོ་འགས་པ་ཙམ་འདིར་བ་འོང་ངོ༔: ×8. The letters are ཙ (tsa-phru), མ, འ, ད with gi-gu, ར, བ. There is no ལ over the ད (other recension ལྡིར). The tshegs in འདིར་བ are crowded and could not be isolated in the dump, so the witness's are kept.

## [?] (2)

- 72.4 **མདོག[?]** (line end): the o-vowel stroke sits where the descender of the བལྟ on 72.3 also reaches, so it could be read as that ཏ's tail. It is taken as naro, because the same ཏ on 72.1 has no such stroke and the sense needs མདོག. The witness's མདག is not taken.
- 74.4 **མི[?]** (first syllable): a heavy ink blot in the left margin (from 74.3 སྐྱོང) covers the space above མ, where the gi-gu would stand. The witness's མི is taken, and it fits the next two items (མི་ལྤགས, མི་གསུར).

Close calls not marked [?]:
- 73.3 (line end) ལྷུན་: the blob before the frame is 4×8 px, a little taller than most tshegs. If the drafter reads it as part of the frame or as a smudge: `# fix: བྱང་ནས་ལྷུནགྱིས => བྱང་ནས་ལྷུན་གྱིས`.
- 73.4 ཁུསྐུ: if a tsheg is hidden in the 1 px gap, no fix is needed.
- 73.2 མཁའ་འགྲོ (pixel dump unclear at x 1257–1263): the witness's tsheg is kept.

## Fixes needed (`# fix:` lines)

```
# fix: ཅིང་༔ བལྟསྟངས => ཅིང་༔ བལྟ་སྟངས
# fix: སྐུ་མདོགསེར་ཞིང => སྐུ་མདོག་སེར་ཞིང
# fix: ལྗང་ཁུསྐུ => ལྗང་ཁུ་སྐུ
# fix: བཞིའི་མཁའ་གྲོ༔ => བཞིའི་མཁའ་འགྲོ༔
# fix: ༔ ཆོསསྐྱོང => ༔ ཆོས་སྐྱོང
# fix: ངོ༔ གར༄༅༔ ༔སྣ => ངོ༔ གར་༄༅༔ ༔སྣ
```
These are:
- the joins 72.3→72.4 and 72.4→72.5;
- the internal 73.4 tsheg;
- the 74.1 abbreviation written out;
- the join 74.2→74.3;
- the join 74.5→75.1.

The last join crosses the leaf-front ornament of p. 75. Its exact form depends on how the build joins across an ornament, and on Reader B confirming that 75.1 opens ༄༅༔ ༔སྣ་ཚོགས.
The 72.1 contraction (`# fix: ཡུམ་མཁའགྲོ => ཡུམ་མཁའ་འགྲོ`) is already in part 007's list and lies before the seam, so part 008 does not need it.
No line-end པའཾ / ལཾ / ནམཁའ / subscript-ས forms occur on these pages. Every ནམ་མཁའ is written in full.

## Suspected misprints

1. 74.1 **ཚོགས་དབག་ཏུ་མེད་པ** for དཔག་ཏུ་མེད་པ ("immeasurable"). The image shows བ (moderate to high certainty). The same print has དཔག at 74.4, and the other recension has དཔག. The sense allows only one reading. Proposed fix (rule 5b, print's reading in the note): `# fix: ཚོགས་དབག་ཏུ => ཚོགས་དཔག་ཏུ`. If the editor treats it as a homophone spelling habit: kept, note only.
2. 74.1 **དེ་རྣམས་ཀྱི་རོལ་དུ**: "around/outside those knowledge-holders" would normally be ཕྱི་རོལ་དུ (the other recension has ཀྱི་ཕྱི་རིམ་དུ, "in the outer ring", compare 61.2 ཕྱི་རིམ་དུ). རོལ alone can mean "side", so the reading is not impossible. Kept, note only.
3. 74.5 **ཙམ་འདིར་བ་འོང་ངོ**: the other recension has ཙམ་དུ་ལྡིར་ནས ("booming as if to split the head"). The print's འདིར་བ is probably the same verb in a variant spelling (ldir / 'dir, "to roar, boom"). Kept, note only.
4. 72.4 མདོག[?] is not a misprint (see [?]). 72.5 ལྡན་བ and 73.1 གཅིག are the print's habits and are not corrected.

## Where the other recension differs in sense (print followed)

- 72.3: print ཡུམ་མཁའ་འགྲོ་དཀར་མོ…འཁྲིལ་ཞིང་ (clause continues); other recension མཁའ་འགྲོ་མ་དཀར་མོ…འཁྲིལ་བ༔. Same.
- 72.3, 72.5, 73.3, 73.5: print བལྟ་སྟངས་ཀྱི་ཕྱག་རྒྱ; other recension ལྟ་སྟངས. Same ("gazing gesture").
- 72.5: print ཐོད་ཁྲག་གིས་གར་མཛད ("dancing with a blood-filled skull"); other recension …གི་གར. Same.
- 73.1 གཅིག / ཅིག; other recension ཞིག. Same.
- **73.5: print གྲི་གུག་དང་ཐོད་ཁྲག་འཛིན་པས་གར་མཛད ("dancing while holding curved knife and blood-filled skull"); other recension ཐོད་ཁྲག་གི་གར་མཛད ("dancing with …")**. Compare 72.1 (print འཛིན་ཅིང, "holding", no dance).
- **74.1: print དེ་རྣམས་ཀྱི་རོལ་དུ ("beside/around them"); other recension ཀྱི་ཕྱི་རིམ་དུ ("in the outer ring around them")**.
- 74.1–2: print གནས་གསུམ་མཁའ་འགྲོ; other recension གནས་གསུམ་གྱི་མཁའ་འགྲོ. Print ཡུལ་ཉི་ཤུ་རྩ་བཞིའི་མཁའ་འགྲོ་རྣམས; other recension …མཁའ་འགྲོ་མ་རྣམས. Same.
- 74.3: print བསྲུང་མ; other recension སྲུང་མ. Same.
- 74.4: print མི་ལྤགས་ཀྱི་བླ་བྲེས ("canopy"); other recension བླ་རེ ("canopy"). Same.
- 74.4: print བཅས་ཏེ༔ འཇིག་རྟེན; other recension བཅས་ཏེ་འཇིག་རྟེན. Same.
- **74.5: print འཇིག་རྟེན་གྱི་ཁམས་ཐམས་ཅད་ཁེངས་པ་ཤིག་ཤིག༔ ཡོམ་ཡོམ་འགུལ་འགུལ་དུ་འོང་ངོ ("filling all world-realms, [it] comes quivering, swaying, shaking"); other recension ཁེངས་པར་ཕྱེད༔ ཤིག་ཤིག་ཡོམ་ཡོམ ("half-filling(?) …")**. The print has no ཕྱེད, and its ༔ falls after ཤིག་ཤིག rather than before.
- 74.5: print མགོ་འགས་པ་ཙམ་འདིར་བ་འོང་ངོ; other recension ཙམ་དུ་ལྡིར་ནས་འོང་ངོ. Close in sense (see misprints 3).
