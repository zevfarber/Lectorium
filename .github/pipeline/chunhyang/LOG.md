# Chunhyang — log

- 2026-11-22 · pilot 001 · leaves 1a–2a of the Jeonju 84-leaf woodblock (열여츈향슈졀가, Dagaseopo printing,
  c. 1912–1926; University of Tokyo L174842, Ogura collection). Zev asked what Korean text would suit Lectorium,
  especially one tied to native tradition, and chose Chunhyang. Transcribed by eye from the IIIF scan
  (https://iiif.dl.itc.u-tokyo.ac.jp/iiif/ogura/L174842/0002.tif and 0003.tif; the scans are not copied into the
  repository). Ends at the proverb that closes Wolmae's speech (공든 탑이 무너지며…), 2a column 3.
  21 units, 174 words, 167 glossary forms. Translations fresh from the Korean; no translation consulted.
  Built with build_chunhyang.py (units.py + glossary.py), which checks: every printed word has one modern
  form (mt), the voice's text (say) has the same words as mt, 100% glossary coverage, no unused keys.
  Reader: Hangul added to WORD_CLASS (and to wordre.py / align_wordref.py), a 'ᄒᆞ→하' modern-spelling switch
  (script "hangul", per-word mt), Korean fonts that assemble old syllables. Audio: ko-KR added to
  build_audio.py with the name left empty, so the first run picks the voice (Chirp 3 HD first) — for Zev to
  hear and approve or replace.
- 2026-11-22 · romanization line added: `tr` per unit (Revised Romanization of `say`, romanize.py), trStyle "line".
- 2026-11-22 · romanization line shown by default (trShown); Hangul alphabet added to the reader (📜 Alphabet: consonants, vowels, syllable blocks, the print's old letters, spelling to sound).
