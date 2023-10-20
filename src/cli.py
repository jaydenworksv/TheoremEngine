import argparse
import argparse
import json
from pathlib import Path

from .entries import SignalEntry, filter_entries, load_entries, save_entries
from .templates import build_entry, list_templates


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


def filter_command(args: argparse.Namespace) -> None:
    entries = load_entries(ENTRY_PATH)
    tags = [tag.strip() for tag in args.tags.split(",") if tag.strip()]
    filtered = filter_entries(
        entries,
        tags=tags or None,
        mood=args.mood or None,
        min_confidence=args.min_confidence,
    )
    if not filtered:
        print("No entries match the filters.")
        return
    print(json.dumps([entry.to_dict() for entry in filtered], indent=2))


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
    filter_parser = subparsers.add_parser("filter", help="Filter entries by criteria")
    filter_parser.add_argument("--tags", default="", help="Comma-separated tag filters")
    filter_parser.add_argument("--mood", default="", help="Mood filter (exact match)")
    filter_parser.add_argument(
        "--min-confidence",
        type=float,
        help="Only include entries with confidence at or above this value",
    )
    filter_parser.set_defaults(func=filter_command)
    template_parser = subparsers.add_parser("template", help="Create entry from a template")
    template_parser.add_argument(
        "--name",
        choices=list_templates(),
        required=True,
        help="Template to use for the new entry",
    )
    template_parser.add_argument("--timestamp", required=True, help="ISO timestamp")
    template_parser.add_argument("--mood", default="reflective", help="Mood tag")
    template_parser.add_argument(
        "--confidence",
        type=float,
        default=0.55,
        help="Confidence score for the template entry",
    )
    template_parser.set_defaults(func=template_command)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return
    args.func(args)


def template_command(args: argparse.Namespace) -> None:
    entries = load_entries(ENTRY_PATH)
    entry = build_entry(args.name, args.timestamp, args.mood, args.confidence)
    entries.append(entry)
    save_entries(ENTRY_PATH, entries)
    print(f"Added entry from template {args.name}")


if __name__ == "__main__":
    main()
