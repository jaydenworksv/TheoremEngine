import argparse
import json
from pathlib import Path

from .entries import SignalEntry, load_entries, save_entries


ENTRY_PATH = Path.cwd() / "samples" / "journal-template.json"


def create_entry(args: argparse.Namespace) -> None:
    entry = SignalEntry(
        timestamp=args.timestamp,
        summary=args.summary,
        tags=[tag.strip() for tag in args.tags.split(",") if tag.strip()],
        mood=args.mood,
        confidence=args.confidence,
    )
    entries = load_entries(ENTRY_PATH)
    entries.append(entry)
    save_entries(ENTRY_PATH, entries)
    print(f"Saved entry at {ENTRY_PATH}")


def show_entries(_: argparse.Namespace) -> None:
    entries = load_entries(ENTRY_PATH)
    if not entries:
        print("No entries yet.")
        return
    print(json.dumps([entry.to_dict() for entry in entries], indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description="SignalWeave journal CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new journal entry")
    add_parser.add_argument("--timestamp", required=True, help="ISO timestamp for the entry")
    add_parser.add_argument("--summary", required=True, help="Short summary or observation")
    add_parser.add_argument(
        "--tags",
        default="",
        help="Comma-separated tags for filtering (macro, ai, algo, mood, etc.)",
    )
    add_parser.add_argument("--mood", default="neutral", help="Mood for the entry")
    add_parser.add_argument(
        "--confidence",
        type=float,
        default=0.5,
        help="Confidence score between 0.0 and 1.0",
    )
    add_parser.set_defaults(func=create_entry)

    subparsers.add_parser("list", help="Print all saved entries").set_defaults(func=show_entries)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return
    args.func(args)


if __name__ == "__main__":
    main()
