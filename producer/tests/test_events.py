from __future__ import annotations

import json
import unittest
from datetime import datetime, timezone
from random import Random

from producer.events import EVENT_TYPES, generate_event


class GenerateEventTests(unittest.TestCase):
    def test_required_fields_are_present(self) -> None:
        event = generate_event(Random(1))
        for field in ("event_id", "event_type", "user_id", "timestamp"):
            self.assertIn(field, event)
            self.assertTrue(event[field])

    def test_event_type_is_supported(self) -> None:
        event = generate_event(Random(2))
        self.assertIn(event["event_type"], EVENT_TYPES)

    def test_each_event_type_can_be_generated(self) -> None:
        for event_type in EVENT_TYPES:
            event = generate_event(Random(3), event_type=event_type)
            self.assertEqual(event["event_type"], event_type)

    def test_product_events_include_product_id(self) -> None:
        for event_type in ("product_view", "add_to_cart", "purchase", "recommendation_click"):
            event = generate_event(Random(4), event_type=event_type)
            self.assertIn("product_id", event)
            self.assertTrue(str(event["product_id"]).startswith("prod_"))
            self.assertNotIn("query", event)

    def test_search_events_include_query(self) -> None:
        event = generate_event(Random(5), event_type="search")
        self.assertIn("query", event)
        self.assertTrue(event["query"])
        self.assertNotIn("product_id", event)

    def test_timestamp_is_iso8601_utc(self) -> None:
        event = generate_event(Random(6))
        parsed = datetime.fromisoformat(event["timestamp"].replace("Z", "+00:00"))
        self.assertEqual(parsed.tzinfo, timezone.utc)

    def test_event_is_json_serializable(self) -> None:
        event = generate_event(Random(7))
        payload = json.dumps(event)
        self.assertEqual(json.loads(payload), event)

    def test_unsupported_event_type_raises(self) -> None:
        with self.assertRaises(ValueError):
            generate_event(Random(8), event_type="refund")

    def test_event_ids_are_unique(self) -> None:
        rng = Random(9)
        ids = {generate_event(rng)["event_id"] for _ in range(50)}
        self.assertEqual(len(ids), 50)


if __name__ == "__main__":
    unittest.main()
