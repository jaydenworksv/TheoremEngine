from typing import List

from .entries import SignalEntry


TEMPLATES = {
    "late-night": {
        "summary": "Late-night recap, noticing how volatility calms near the edges.",
        "tags": ["reflection", "night"],
        "context": "Writing while sipping coffee after the markets close.",
    },
    "weekend-batch": {
        "summary": "Weekend batch of ideas around building a micro hedging helper.",
        "tags": ["weekend", "planning"],
        "context": "Drafting plans for the next SignalWeave iteration.",
    },
}


def list_templates() -> List[str]:
    return list(TEMPLATES.keys())


def build_entry(
    template: str, timestamp: str, mood: str, confidence: float
) -> SignalEntry:
    spec = TEMPLATES[template]
    return SignalEntry(
        timestamp=timestamp,
        summary=spec["summary"],
        tags=spec["tags"],
        mood=mood,
        confidence=confidence,
        context=spec["context"],
    )


if __name__ == "__main__":
    print("Available templates:")
    for name in list_templates():
        print(f"- {name}")
