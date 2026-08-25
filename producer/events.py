from __future__ import annotations

import uuid
from datetime import datetime, timezone
from random import Random
from typing import Any

EVENT_TYPES = (
    "product_view",
    "add_to_cart",
    "purchase",
    "search",
    "recommendation_click",
)

_EVENT_WEIGHTS = {
    "product_view": 50,
    "add_to_cart": 20,
    "search": 15,
    "purchase": 10,
    "recommendation_click": 5,
}

_DEVICES = ("mobile", "desktop", "tablet")

_SEARCH_QUERIES = (
    "wireless headphones",
    "running shoes",
    "espresso machine",
    "laptop stand",
    "winter jacket",
    "yoga mat",
    "mechanical keyboard",
    "water bottle",
)

Event = dict[str, Any]


def generate_event(rng: Random | None = None, event_type: str | None = None) -> Event:
    """Return one structurally valid e-commerce behavioral event."""
    rng = rng or Random()
    chosen_type = event_type or rng.choices(
        population=list(_EVENT_WEIGHTS),
        weights=list(_EVENT_WEIGHTS.values()),
        k=1,
    )[0]

    if chosen_type not in EVENT_TYPES:
        raise ValueError(f"unsupported event_type: {chosen_type}")

    event: Event = {
        "event_id": str(uuid.UUID(int=rng.getrandbits(128), version=4)),
        "event_type": chosen_type,
        "user_id": f"user_{rng.randint(1, 500)}",
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "device": rng.choice(_DEVICES),
    }

    if chosen_type == "search":
        event["query"] = rng.choice(_SEARCH_QUERIES)
    else:
        event["product_id"] = f"prod_{rng.randint(100, 999)}"

    return event
