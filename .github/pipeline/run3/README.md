# Run 3 — the unusual texts

The owner's third production run (decided 2026-10-11, set up 2026-10-12): finish the unusual texts already
begun, one part per firing, moving to the next text by itself when one is done. Its own routine, its own queue
(`../queue-run3.txt`), its own records; it never touches the shared queue (`../queue.txt`), the Nights, or
another work's files.

Order: Hammurabi → Kebra Nagast → Secret History → Mabinogi → Cid → Azatiwada → Sumerian King List.

| work | edition | parts left | kind |
|---|---|---|---|
| hammurabi | Harper 1904 (stele) + Ungnad 1909 / Poebel 1914 / Cuq 1918 (the erased section) | 21 (2 establish first) | cuneiform words, signs from the plates |
| kebra-nagast | Bezold 1905 via HaCohen's Unicode text | 86 | Geʿez words, mechanical interlinear |
| secret-history | Shiratori 1943 (Ye Dehui print) via ja.wikisource | 66 | one glyph per word, mechanical |
| mabinogi | Evans 1907, White Book | 13 (each established first) | Middle Welsh prose |
| cid | Pidal 1923 | 50 (each established first) | Old Spanish verse |
| azatiwada | ACLT 2, copy Hu. | 3 | Luwian hieroglyphs, sign keys |
| king-list | Langdon 1923 | 8 | cuneiform words, signs from the plates |

How a firing works: `RUNBOOK.md`. Tools: `r3.py` (next / claim / establish-packet / pin / packet / build /
validate / publish / done / plan), `r3lib.py`, `cun.py` (cuneiform), `signs.py` (adds a sign to a shared sign
glossary and its copy embedded in the reader), `page.py` (renders a scanned page), `fetch_run3.py` +
`../../workflows/fetch-run3.yml` (the runner fetches public-domain sources listed in `fetch-requests.json`,
since Claude's cloud sessions cannot reach archive.org or Wikisource).

Sources were fetched and checked at setup (2026-10-12): see each work's LOG.md.

## Audio (the $10/month rule, 2026-10-11)
Every text gets audio once its voice is settled; `audio.yml` builds it on push or in the daily sweep, inside
the monthly budget (`build_pinned.py MONTHLY_BUDGET_USD`), and the daily budget check warns the owner at $8.
- Hammurabi: voice settled (German carrier, 2026-10-11) — every new `hammurabi-` part is voiced on push.
- Kebra Nagast (Geʿez), Secret History (Middle Mongol), Mabinogi (Middle Welsh), Cid (Old Spanish), Azatiwada
  (Luwian), King List (Sumerian): voice not chosen — they publish without audio; when the owner chooses a voice,
  the language goes into `build_pinned.py` PINNED / `pick_targets.py` PINNED_AUTO and the sweep voices every
  published part.
The run itself never builds or edits audio.

## Aqhat
Left off. The run needs the tablets' attested signs (the text-as-fact rule); every edition that gives them
(Virolleaud 1936, Gordon's textbooks, CTA, KTU) is in copyright and none is accessible here — the archive.org
copies are lending-only. The pilot (1.17 i 1–33) stays as it is.
