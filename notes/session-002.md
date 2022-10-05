## Session 002

- Scaffolded `src/entries.py` with the SignalEntry dataclass and helpers for loading/saving JSON data so future sessions can focus on features instead of wiring storage.
- Added a minimalist CLI (`src/cli.py`) that reads/writes from `samples/journal-template.json` and exposes `add`/`list` commands for quick testing.
- Dropped a starter JSON file with one example entry to keep the repo runnable without needing the actual journal yet.

Next up: wire a quick exporter and maybe a sample dashboard script so there is something tangible to push daily.
