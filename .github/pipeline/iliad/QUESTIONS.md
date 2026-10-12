# Iliad pipeline — open questions

## Pilot verdict (raised 2026-10-12)
iliad-001 (1.1–100) is published for Zev to judge. Until he approves the presentation, `iliad` is **not** in
`queue.txt`. Approving it means: add `iliad` to `.github/pipeline/queue.txt` (after beowulf, per the
2026-10-11 three-runs plan).

## The opening line (decided at the pilot, open to the owner)
House rendering: `l` "The wrath sing, goddess, of Peleus’-son Achilles", `i` "Goddess, sing the wrath of
Peleus’ son Achilles". "Wrath" was chosen over "rage"/"anger" (the famous modern choices) and because μῆνις
is the god-sized word (1.75). The Odyssey opened with "Muse, tell me of the man"; the two openings are
deliberately built the same way (vocative first in `i`).

## Δαναοί: "Danaans", not "Greeks" (decided at the pilot)
The Odyssey's `i` layer renders Δαναοί "Greeks". The Iliad keeps "Danaans" in both layers, because the three
names alternate constantly here. This makes the two poems differ on one word; the alternative is to align
the Iliad with the Odyssey. Decided meanwhile: "Danaans".

## Edition imprint
Perseus describes its source as the OCT "Editio Tertia", Oxford 1908–1920 (two volumes). The source field
cites the 3rd edition, 1920. Both volumes are pre-1930 either way.

## Audio
Ancient Greek audio is built on push only for `odyssey-` and `hammurabi-` ids (`pick_targets.py`
BUILD_ON_PUSH); every other Greek story waits for the daily "missing" sweep, which takes stories in
MISSING_PRIORITY order (odyssey, slovo, aesop, ovid, pyramus) and then alphabetically, 40 a day, inside the
WaveNet free allowance — which for October 2026 is already at its cap (3,598,007 of 3,600,000 characters).
So iliad-001 gets no audio until November at the earliest, and then behind the remaining Aesop/Ovid backlog
unless `iliad-` is added to BUILD_ON_PUSH or MISSING_PRIORITY. Not changed here: the audio scripts are shared
and the order is Zev's.
