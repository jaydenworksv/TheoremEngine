from datetime import datetime
from pathlib import Path
from typing import List, Tuple

from .entries import load_entries


def _parse_timestamp(value: str) -> datetime:
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")


def compute_intervals(path: Path) -> List[Tuple[str, str, float]]:
    entries = sorted(load_entries(path), key=lambda entry: entry.timestamp)
    intervals = []
    for previous, current in zip(entries, entries[1:]):
        prev_ts = _parse_timestamp(previous.timestamp)
        curr_ts = _parse_timestamp(current.timestamp)
        delta = curr_ts - prev_ts
        intervals.append((previous.summary, current.summary, delta.total_seconds() / 3600))
    return intervals


def print_timeline(path: Path) -> None:
    print("SignalWeave Timeline")
    for prev_summary, curr_summary, hours in compute_intervals(path):
        print(f"- {prev_summary} → {curr_summary}: {hours:.1f}h gap")


if __name__ == "__main__":
    sample = Path.cwd() / "samples" / "journal-template.json"
    print_timeline(sample)
