from collections import Counter
from pathlib import Path

from .entries import load_entries


def mood_distribution(path: Path) -> Counter[str]:
    entries = load_entries(path)
    return Counter(entry.mood for entry in entries)


def print_moodboard(path: Path) -> None:
    distribution = mood_distribution(path)
    print("SignalWeave Moodboard")
    for mood, count in distribution.most_common():
        print(f"- {mood}: {count}")


if __name__ == "__main__":
    sample = Path.cwd() / "samples" / "journal-template.json"
    print_moodboard(sample)
