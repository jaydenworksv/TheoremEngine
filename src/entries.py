from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable, List, Optional
import json


@dataclass
class SignalEntry:
    timestamp: str
    summary: str
    tags: List[str]
    mood: str
    confidence: float
    trend: Optional[str] = None
    context: Optional[str] = None

    def to_dict(self) -> dict:
        return asdict(self)


def load_entries(path: Path) -> List[SignalEntry]:
    data = []
    if not path.exists():
        return data
    raw = path.read_text()
    try:
        entries = json.loads(raw)
    except ValueError:
        return data
    for item in entries:
        data.append(SignalEntry(**item))
    return data


def save_entries(path: Path, entries: List[SignalEntry]) -> None:
    payload = [entry.to_dict() for entry in entries]
    path.write_text(json.dumps(payload, indent=2))


def filter_entries(
    entries: Iterable[SignalEntry],
    tags: Optional[List[str]] = None,
    mood: Optional[str] = None,
    min_confidence: Optional[float] = None,
) -> List[SignalEntry]:
    normalized_tags = {tag.lower() for tag in tags} if tags else set()

    def matches(entry: SignalEntry) -> bool:
        if tags:
            entry_tags = {tag.lower() for tag in entry.tags}
            if not normalized_tags & entry_tags:
                return False
        if mood and entry.mood.lower() != mood.lower():
            return False
        if min_confidence is not None and entry.confidence < min_confidence:
            return False
        return True

    return [entry for entry in entries if matches(entry)]
