#!/usr/bin/env bash
set -euo pipefail

# Create the local behavioral-events topic if it does not already exist.
# Uses the Kafka CLI inside the compose kafka container.

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "${ROOT_DIR}"

TOPIC="behavioral-events"
BOOTSTRAP="localhost:19092"
PARTITIONS=1
REPLICATION_FACTOR=1

docker compose exec -T kafka /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server "${BOOTSTRAP}" \
  --create \
  --if-not-exists \
  --topic "${TOPIC}" \
  --partitions "${PARTITIONS}" \
  --replication-factor "${REPLICATION_FACTOR}"

echo "topic ${TOPIC} is present (${PARTITIONS} partition, replication factor ${REPLICATION_FACTOR})"
