# read_B: pp. 66–68 (leaves n67–n69), established from the images

Line counts: p. 66 has five lines (a leaf back, no ornament). p. 67 has five lines. It is a leaf front and opens with ༄༅༔, then a blank stretch, then ༔ before སྔར (×3, both ༔ clear). p. 68 has five lines (a leaf back, no ornament). That makes 15 print lines.
The witness's line breaks match the print on every line (15 of 15).

Method: line bands were found from the row profile and the full page. Headlines are at about y≈165/220/275/330/385 on n67, 100/155/210/265/320 on n68, and 160/215/270/325/380 on n69. Each line was cropped in four overlapping segments at ×3 (LANCZOS). Doubtful syllables and every line end were cropped at ×5–×10. A pixel dump (threshold 128) was used for the tsheg before ༔ where the ×8 crop left doubt (67.4 first དང་༔; 68.1 three instances).
Note: the shared scratchpad held another reader's `crop.py`. My tools and crops were kept in a separate folder (`readerB_tools/`, `cb/`).

## The image overruled the witness (17 changes in 17 rows)

| page.line | witness → print | why |
|---|---|---|
| 66.1 | (line end) བའི་ → བའི | ×6: the gi-gu of འི runs up against the inner frame rule, with no room and no dot. Needs `# fix` |
| 66.2 | (line end) གྲུབ་ → གྲུབ | ×6: about 15 px of clean white between བ and the frame at headline height. Needs `# fix` |
| 66.3 | (line end) ཡེ་ཤེས་ → ཡེ་ཤེས | ×6: ས touches the frame. Needs `# fix` |
| 66.4 | ཞིས་བྱ → ཞེས་བྱ | ×5: the vowel over ཞ is a straight e-stroke. It has no gi-gu hook; compare the གི of གསེང་གི in the same line |
| 66.4 | རྡོ་རྗེས་སེམས → རྡོ་རྗེ་སེམས | ×9: after the རྗེ stack come only ས (carrying its own e-stroke), མ and ས. There is no second ས. Typing error |
| 66.4 | ཁྱོང་གསེང → ཁོང་གསེང | ×8: ཁ with the o-vowel and no ya-btags under it (its legs end clean). The other recension has ཁོང་སེང |
| 66.4 | (line end) པའི་ → པའི | ×7: clean white between the འི and the frame. Needs `# fix` |
| 66.5 | ལྟ་བུའ་མ༔ → ལྟ་བུའམ༔ | ×8: འ and མ stand together with no tsheg between them ("[like mother and child meeting,] or…") |
| 67.2 | (line end) ནས་ → ནས | ×7: ས meets the frame. Needs `# fix` |
| 67.4 | (line end) བཀྲག་ → བཀྲག | ×6: ག meets the frame. Needs `# fix` |
| 67.5 | ཡི་དྭངས་ཀྱི → ཡི་དྭགས་ཀྱི | ×5/×8: ད with the wa-zur (a small closed triangle at its foot), then a box ག, then ས. There is no ང. "Hungry ghosts" |
| 67.5 | འོང་སེར་པོ → འོད་སེར་པོ | ×5: the letter after འོ is ད, as in every other འོད of the line. Typing error |
| 67.5 | (line end) དམྱལ་ → དམྱལ | ×7: ལ meets the frame. Needs `# fix` |
| 68.1 | བཀྲག་མེད་དང་༔ (first) → …དང༔ | ×8: the head of ང runs straight into the upper ring of ༔, and there is no separate drop. This is a close call (see below) |
| 68.1 | འཆར་དུ་འོང་༔ → …འོང༔ | ×8 and pixel dump: the head bar of ང runs into the ༔ with no blob between |
| 68.1 | (line end) བྱེད་ → བྱེད | ×7: ད stands just short of the frame, and there is no dot. Needs `# fix` |
| 68.3 | འོ་རྒྱལལོ༔ → འོ་རྒྱལོ༔ | ×6/×8: after འོ come only the རྒྱ stack and one ལ carrying the o-vowel, then ༔. That makes a contraction རྒྱལོ for རྒྱལ་ལོ. Needs `# fix` |

In all there are:
- 7 letter or vowel changes: 66.4 ×3, 67.5 ×2, 66.5 tsheg removed inside a word, 68.3 contraction.
- 2 tsheg-before-༔ removals: 68.1 ×2.
- 8 line-end tsheg removals: 66.1, 66.2, 66.3, 66.4, 67.2, 67.4, 67.5, 68.1.

The 66.5 བུའམ change is counted under letters.

Where the print has a tsheg before ༔ (witness confirmed):
- 66.3 སྣང་ངོ་༔: a clear separate triangle between ངོ and ༔ (×6).
- 67.4–67.5 every བཀྲག་མེད་དང་༔ / དཀར་པོ…དང་༔ (6 instances). The pixel dump of 67.4 དཀར་པོ་བཀྲག་མེད་དང་༔ shows a separate 6×5 px blob at x 1408–1413 between ང and the ring. The others show a visible dot at ×3–×6.
- 68.1 འཛིན་པ་དང་༔: a drop at the upper left of the ༔ ring, separate at the top (×8).
- 68.2 སྐྲག་ཅིང་༔: a clear separate drop (×8).
- All other ༔ on these pages have no tsheg before them, as the witness has it.

Witness readings checked and confirmed, though they look odd:
- 66.1 ཅིག་མི་རྟོག་བའི: there is no ༔ after ཅིག, and the letter is བ (a closed box), not པ (×6). The other recension has མི་རྟོག་པའི. The print's own spelling.
- 66.2 **ཐཾས་ཅད**: ཐ with the anusvāra sign (ring and dot), then ས. A mid-line contraction (×6). Needs `# fix`.
- 66.2 and 66.3 ཀྱཻ (double vowel).
- 66.4 གསེང (e-vowel on ས).
- 66.4 དཔའ (no gi-gu; the other recension has དཔའི).
- 66.4 ཡིན་ནོ༔.
- 67.1 སྒྲོ་འདོགས་ཆོད་པ.
- 67.1 (line end) ཉིད་: a tsheg stands after ད.
- 67.2 རྒྱུན་གྱི: the subscribed letter has a triangular interior, like ག in this cut. ཀྱི in རིགས་ཀྱི (67.3) has a vertical in the middle instead. The same holds for 67.4 ཡིན་གྱི and 68.5 གུས་གྱིས.
- 67.3 མཉམ་དུ: a small ཉ between the two མ.
- 67.3 (line end) སྣང་: a tsheg is present.
- 67.4 ཀྱང་གཅིག་འཆར་དུ (×5).
- 67.4 གང་ཞེ་ན༔: tshegs after ང and after ཞེ.
- 68.1 **འོད་དུ་ཁ**: ×7 shows འོད, then one ད with zhabs-kyu, then a tsheg, then ཁ. There is no final ད (see misprints).
- 68.1 གཤིབས་མར.
- 68.1 དེ་ཙ་ན.
- 68.2 (line end) ཆགས་: a tsheg, then filler dots (left out).
- 68.3 (line end) བུ༔: the ༔ is squeezed small under the right of བུ against the frame.
- 68.4 ངག་ངོ་སྤྲོད (the o-strokes of ངོ and སྤྲོ run together).
- 68.4 (line end) འཁོར་: a tsheg is present.
- 68.5 དག་པ་ཡེ་ཤེས: the letter after དག might be read as a closed box (བ). It is too close to call against the པ of 68.1 དག་པ, so the witness's པ is kept.
- 68.5 (line end) བཅོམ་: a dot at headline height, then filler dots, as at 61.3/62 (the first dot counted as the tsheg).

## [?] (1)

- 68.3 **མེད་བས[?]**: the letter after མེད་ is rounded, and at ×8 it looks more like the འ of the following འོ than like this cut's པ or བ. A reading མེད་འས makes no sense. The other recension has མེད་པས, and the witness has བས. The witness is taken, marked [?].

Close calls not marked [?]:
- 68.1 first མེད་དང༔: at ×8 the ང's head shows as a closed little triangle fused to the ༔ ring. There is no separate drop of the kind seen at 68.1 པ་དང་༔ in the same line. It is read without a tsheg. If the drafter sees the fused triangle as a tsheg, the witness's དང་༔ stands.

## Tsheg status at my borders

- First line, 66.1, begins འཆར་བ… (it continues Reader A's 65.5).
- Last line, 68.5, ends བཅོམ་ with a tsheg, followed by filler dots. The join 68.5 → 69.1 (Reader C) needs no fix.
- The join 66.5 → 67.1 crosses the leaf-front ornament. 66.5 ends with ༔ (བུའམ༔), so nothing is needed there.

## Fixes needed (`# fix:` lines)

```
# fix: རྟོག་བའིངང་དུ => རྟོག་བའི་ངང་དུ
# fix: ཐཾས་ཅད => ཐམས་ཅད
# fix: བྱ་བ་གྲུབཔའི => བྱ་བ་གྲུབ་པའི
# fix: ཀྱི་ཡེ་ཤེསབཞི་སྦྱོར => ཀྱི་ཡེ་ཤེས་བཞི་སྦྱོར
# fix: སྤྲད་པའིགདམས => སྤྲད་པའི་གདམས
# fix: ཐིམ་ནསལོངས => ཐིམ་ནས་ལོངས
# fix: དམར་པོ་བཀྲགམེད => དམར་པོ་བཀྲག་མེད
# fix: དམྱལཔའི => དམྱལ་པའི
# fix: མ་བྱེདཔར༔ => མ་བྱེད་པར༔
# fix: འོ་རྒྱལོ༔ => འོ་རྒྱལ་ལོ༔
```
There are eight line-join tshegs: 66.1→2, 66.2→3, 66.3→4, 66.4→5, 67.2→3, 67.4→5, 67.5→68.1 and 68.1→2. There are two mid-line contractions: 66.2 ཐཾས, 68.3 རྒྱལོ. Each left side was checked to occur exactly once in the joined text of pp. 66–68.
No line-end abbreviations (པའཾ, ལཾ, ནམཁའ, subscript-ས) occur on these pages.

## Suspected misprints

1. 68.1 **འོད་དུ་ཁ** for དུད་ཁ ("smoke-coloured", the light of the hells). The image clearly has དུ་ཁ, and the witness agrees. The other recension has དུད་ཀ. The sense allows only one reading. Certainty is moderate: it could be a print spelling, but no such habit is known. Proposed as a misprint correction (rule 5b): `# fix: འོད་དུ་ཁ་བཀྲག => འོད་དུད་ཁ་བཀྲག`.
2. 68.3 བས[?] for པས: see [?]. Kept, note only.

Not misprints, the print's own spelling: མི་རྟོག་བའི (66.1), ཁོང་གསེང (66.4; the usual form is ཁོང་སེང), ཀྱཻ beside ཀྱེ, ཐཾས and རྒྱལོ (contractions, fixed above).

## Where the other recension differs in sense (print followed)

- 66.1: print ཡང་མ་བྱེད་ཅིག་མི་རྟོག་བའི་ངང་དུ་ཀློད ("do not [be afraid]; relax in the non-conceptual state"); other recension མ་བྱེད་པར་རྣམ་པར་མི་རྟོག་པའི་ངང་དུ་ལྷོད. Same in sense.
- 66.2: print སྐུ…ཁྱོད་རང་ལ་ཐིམ་ནས ("dissolve into you"); other recension ཁྱོད་རང་དང་དབྱེར་མེད་དུ་ཐིམ་ནས ("dissolve inseparably with you"). Close.
- 66.4: print རྡོ་རྗེ་སེམས་དཔའ་ཁོང་གསེང་གི་ལམ་ཞེས་བྱ་བ་ཡིན་ནོ; other recension རྡོ་རྗེ་སེམས་དཔའི་ཁོང་སེང་གི་ལམ་ཞེས་བྱའོ. Same ("the inner passage of Vajrasattva").
- 67.1: print མཐོང་བ་ཙམ་གྱིས་ངོ་ཤེས ("recognises at mere sight"); other recension མཐོང་བ་བཞིན་ངོ་ཤེས་ཏེ. Close. Print རང་སྣང་དུ; other recension རང་སྣང་ལ་རང་སྣང་དུ.
- 67.4: print འོད་དྲུག་ཀྱང་གཅིག་འཆར་དུ ("the six lights also arise as one"); other recension དུས་གཅིག་ཏུ་འཆར ("arise at the same time"). Close.
- 68.1: print དུ་ཁ; other recension དུད་ཀ (see misprints).
- 68.3: print འོ་རྒྱལོ ("how wearisome"); other recension འོ་བརྒྱལ་ལོ. Same.
- 68.4: print བླ་མའི་གདམས་ངག་ངོ་སྤྲོད་མེད་པ…ཡིན་ན་ནི; other recension གདམ་ངག་གི་ངོ་སྤྲོད་…ཡིན་ན. Same.
