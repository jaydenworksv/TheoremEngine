from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Optional
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
