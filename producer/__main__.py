from __future__ import annotations

import argparse
import json
import os
import sys
import time

from producer.events import generate_event

_DEFAULT_INTERVAL_SECONDS = 1.0


def _interval_from_env() -> float:
    raw = os.getenv("PRODUCER_INTERVAL_SECONDS")
    if raw is None or raw == "":
        return _DEFAULT_INTERVAL_SECONDS
    return float(raw)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Emit synthetic e-commerce behavioral events as JSON lines on stdout."
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=_interval_from_env(),
        help="Seconds to wait between events (env: PRODUCER_INTERVAL_SECONDS).",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=0,
        help="Number of events to emit. 0 runs continuously.",
    )
    return parser.parse_args(argv)


def run(interval: float, count: int = 0) -> None:
    if interval < 0:
        raise ValueError("interval must be >= 0")
    if count < 0:
        raise ValueError("count must be >= 0")

    emitted = 0
    while count == 0 or emitted < count:
        sys.stdout.write(json.dumps(generate_event()) + "\n")
        sys.stdout.flush()
        emitted += 1
        if count == 0 or emitted < count:
            time.sleep(interval)


def main() -> None:
    args = parse_args()
    try:
        run(interval=args.interval, count=args.count)
    except KeyboardInterrupt:
        return


if __name__ == "__main__":
    main()
