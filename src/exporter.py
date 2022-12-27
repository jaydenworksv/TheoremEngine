from pathlib import Path
from typing import Iterable

from .entries import load_entries, SignalEntry


def format_entry(entry: SignalEntry) -> str:
    lines = [
        f"## {entry.summary}",
        f"- timestamp: {entry.timestamp}",
        f"- trend: {entry.trend or 'undecided'}",
        f"- mood: {entry.mood} (confidence {entry.confidence})",
        f"- tags: {', '.join(entry.tags) or 'none'}",
    ]
    if entry.context:
        lines.append(f"- context: {entry.context}")
    return "\n".join(lines)


def export_to_markdown(source: Path, destination: Path) -> None:
    entries = load_entries(source)
    chunks = [format_entry(entry) for entry in entries]
    destination.write_text("\n\n".join(chunks))


def export_to_brief(source: Path) -> Iterable[str]:
    entries = load_entries(source)
    for entry in entries:
        yield f"{entry.timestamp} | {entry.summary[:40]} | {entry.confidence:.2f}"


if __name__ == "__main__":
    SOURCE_PATH = Path.cwd() / "samples" / "journal-template.json"
    TARGET_PATH = Path.cwd() / "exports" / "journal-summary.md"
    export_to_markdown(SOURCE_PATH, TARGET_PATH)
    for line in export_to_brief(SOURCE_PATH):
        print(line)
