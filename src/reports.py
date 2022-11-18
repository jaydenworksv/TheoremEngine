from collections import Counter
from pathlib import Path

from .entries import load_entries


def summarize_entries(path: Path) -> dict:
    entries = load_entries(path)
    tag_counter = Counter(tag for entry in entries for tag in entry.tags)
    mood_counter = Counter(entry.mood for entry in entries)
    confidence_scores = [entry.confidence for entry in entries]

    summary = {
        "total_entries": len(entries),
        "tag_counts": dict(tag_counter),
        "mood_counts": dict(mood_counter),
        "average_confidence": round(
            sum(confidence_scores) / len(confidence_scores), 2
        )
        if confidence_scores
        else 0,
    }
    return summary


def print_summary(path: Path) -> None:
    data = summarize_entries(path)
    print("SignalWeave Summary")
    print(f"  entries: {data['total_entries']}")
    print(f"  avg confidence: {data['average_confidence']}")
    print("  moods:")
    for mood, count in data["mood_counts"].items():
        print(f"    {mood}: {count}")
    print("  tags:")
    for tag, count in data["tag_counts"].items():
        print(f"    {tag}: {count}")


if __name__ == "__main__":
    SAMPLE_PATH = Path.cwd() / "samples" / "journal-template.json"
    print_summary(SAMPLE_PATH)
