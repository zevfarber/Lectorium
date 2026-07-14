# Lesestube — your language reading room

## What's here

**reader.html** — the reading app. Open it in any browser (double-click it). Aschenputtel is already built in. It works entirely offline; audio uses your browser's built-in German/French voices.

**project-instructions.md** — paste this into your new project's instructions (or add it as a project file). It tells Claude how to behave as your reading tutor and how to process new texts into story files.

**aschenputtel.json** — the processed story as a standalone file. You don't need it to read Aschenputtel (it's already inside reader.html); keep it in the project as the reference example of the story format.

**aschenputtel-de.txt** — the raw 1857 German source text, for reference.

## Using the reader

- **Original only** mode shows just the German; press **EN** on any sentence (or the E key) to peek at the English. **Side by side** shows everything.
- The English shown is the *literal* translation. Where literal isn't how you'd say it in English, an **≈ natural** button switches to the natural phrasing.
- **📝 note** opens the grammar/culture note where one exists.
- Click any word for its meaning; the popup can pronounce it normally or slowly.
- **🔊 Listen / 🐢 Slow** read the whole sentence aloud. The slider in the header adjusts normal speed.
- Your reading position is remembered per story.

## Adding stories

In the project chat, ask Claude for a story — e.g. "Process Rotkäppchen for the reader" or "Do Perrault's Cendrillon." Claude produces a `.json` file; open it in the reader with **＋ Load story**. (Loaded stories last for the session; to make one permanent, ask Claude to embed it into reader.html the way Aschenputtel is.)

## Tutoring while you read

The app answers the instant questions. For everything else — "I don't get how this sentence means that" — ask in the project chat, quoting the sentence. The project instructions make Claude answer at exactly the depth you ask, without quizzing or over-correcting.
