# SignalWeave

SignalWeave is a solo journal + insight tracker that captures daily trading/AI signals and logs personal observations in a storytelling way. It mixes lightweight analytics with runnable prompts and keeps everything simple so the solo developer can riff on ideas without worrying about production polish.

## Vision
- Capture unusual moves, AI experiments, or research notes as short, timestamped snippets.
- Attach basic metadata (trend, intuition, mood, confidence) and export it for later review.
- Keep the project deliberately small: scripts, markdown notes, and a single CLI/web view for browsing.

## First Steps
1. Draft journal schema and CLI helpers.
2. Store test entries and export templates.
3. Keep a dev log for each coding session to mimic an actual solo workflow.

## CLI Helper
- `python -m src.cli list`: dumps saved entries.
- `python -m src.cli add ...`: creates basic records without needing a full app.
- `python -m src.cli filter --tags ai`: limits output so you can review subsets.
- `python -m src.reports`: prints a quick summary of moods/tags based on `samples/journal-template.json`.
- `python -m src.exporter`: generates a markdown digest and prints a timestamped brief.
- `python -m src.timeline`: tells you how much time passed between recent entries to keep the solo cadence honest.
- `python -m src.scheduler`: suggests future weekends or evenings for the next few sessions.
- `python -m src.moodboard`: prints the current mood counts so the journal feels personal.
- `python -m src.cli list`: dumps saved entries.
- `python -m src.cli add ...`: creates basic records without needing a full app.
- `python -m src.cli filter --tags ai`: limits output so you can review subsets.
- `python -m src.reports`: prints a quick summary of moods/tags based on `samples/journal-template.json`.
- `python -m src.exporter`: generates a markdown digest and prints a timestamped brief.
- `python -m src.timeline`: tells you how much time passed between recent entries to keep the solo cadence honest.
