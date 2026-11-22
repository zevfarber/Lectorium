# Chunhyang — conventions

## Edition
열여츈향슈졀가 (Yeollyeo Chunhyang sujeolga), the Jeonju (Wanpan) woodblock in 84 leaves (vol. 1: 45 leaves,
vol. 2: 39), Dagaseopo printing, c. 1912–1926. Copy: University of Tokyo, Linguistics Library, Ogura Shinpei
collection, L174842, scanned with Korea University. IIIF images:
`https://iiif.dl.itc.u-tokyo.ac.jp/iiif/ogura/L174842/NNNN.tif/<x,y,w,h>/,900/0/default.jpg`; each image is an
open spread (5616 × 3744). 0002 = leaf 1a (left page); 0003 = 1b (right) + 2a (left); and so on.
The text block of a page runs about y 840–3250; columns are about 120 px wide, read right to left.
Crops of three columns by a third of the page height are legible enough to see the dot of ㆍ.

## Text
- Spelling exactly as printed, including ㆍ (arae-a) and ㆎ, written with conjoining jamo (ᄒᆞ = U+1112 U+119E),
  and the repeat mark 〻 (U+303B), which stays inside the word it doubles.
- The print has no spaces and no punctuation. Word division is editorial, by modern spacing, with these
  exceptions kept as one word because the voice and the modern spelling need one token per word:
  어려잇다, 나계시고, 나계시사.
- Where the woodcut hides the dot of ㆍ, read the edition's regular spelling: ᄒᆞ (하), ᄃᆡ (대), ᄉᆡᆼ (생),
  ᄆᆡ (매), ᄌᆡ (재), ᄂᆡ (내), ᄇᆡᆨ (백), ᄯᆡ (때), ᄭᆡ (깨). Where the print plainly has ㅏ (하난, 하야,
  당하야, 하리), keep ㅏ.
- Misprints and dialect forms stay in the text as printed; the modern spelling (mt) gives the intended word and
  a note says so (조경 → 조정, 혜륙 → 혈육, 잔여 → 자녀, 신고 → 신공). Doubtful readings are said to be doubtful
  in the note (쳔영, 쎅길손가).

## Layers
- `mt`: one modern-spelling word per printed word (shown by the ᄒᆞ→하 switch). Modern spelling, same wording:
  archaic words stay (뉘라, 어이, 무삼 → 무슨 only because 무삼 is a spelling of 무슨).
- `say`: the mt words with modern punctuation, for the voice. Same words as mt, enforced by the build.
- `tr` (shown under the Korean, `trStyle: "line"`): the Revised Romanization of `say`, made by romanize.py with
  the sound changes inside each word (linking, nasalization, ㄴ/ㄹ → ll, ㅎ), tensification unwritten, the h kept
  after k/t/p (덕화 deokhwa); proper names and the first word capitalized. Shown by default (`trShown`).
- `wordSay`: the modern form of every printed word that differs, for the word clips.
- `l`: structurally transparent, following the Korean clause order where English can bear it.
- `i`: plain English, lightly old-fashioned where the narrator is grand; never childish.
- Notes: name the old letter or spelling, give the modern word, explain Sino-Korean phrases with their
  characters, flag the pansori narrator's voice. Recurring patterns (-의 for -에, 마리 for 말이, -난 for -는,
  ㆍ) get a full note the first few times, then a nudge.

## Audio
Standard modern Korean (Seoul), reading `say`. Voice: resolved by the first build (Chirp 3 HD first); for Zev to
judge by ear.
