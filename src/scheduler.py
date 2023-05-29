from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Optional

from .entries import load_entries


def _parse_timestamp(value: str) -> datetime:
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")


def latest_entry_time(path: Path) -> Optional[datetime]:
    entries = load_entries(path)
    if not entries:
        return None
    return max(_parse_timestamp(entry.timestamp) for entry in entries)


def plan_next_sessions(base_date: datetime, slots: int = 3, gap_days: int = 7) -> List[datetime]:
    return [base_date + timedelta(days=gap_days * i) for i in range(1, slots + 1)]


def print_schedule(path: Path) -> None:
    last = latest_entry_time(path)
    if not last:
        print("No session timing yet.")
        return
    print("SignalWeave session schedule")
    for session in plan_next_sessions(last, slots=3, gap_days=7):
        print(f"- {session.strftime('%Y-%m-%d %H:%M')}")


if __name__ == "__main__":
    sample_path = Path.cwd() / "samples" / "journal-template.json"
    print_schedule(sample_path)
