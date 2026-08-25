# Roadmap

This document describes the intended evolution of the project. It does not include dates. No future phase is complete.

> Only one roadmap item or tightly related group of items should be implemented at a time. The next implementation step should not begin until the current change has been reviewed.

The project should evolve through small, controlled increments.

## Phase 0 — Project Foundation

Goal:

Establish the project direction, repository structure, documentation, and development roadmap.

- [x] Define project scope
- [x] Define initial architecture
- [x] Create repository foundation
- [x] Create README
- [x] Create roadmap

## Phase 1 — Streaming Ingestion

Goal:

Create the first end-to-end streaming path.

Planned work:

- [x] synthetic Python event producer
- [ ] Kafka
- [ ] behavioral event topic
- [ ] Spark Structured Streaming consumer
- [ ] explicit event schema
- [ ] basic validation
- [ ] valid events persisted to Apache Iceberg
- [ ] invalid events routed to a DLQ

Target architecture:

```text
Python Producer
      |
      v
Kafka
      |
      v
Spark Structured Streaming
      |
      v
Validation
   /       \
valid     invalid
  |          |
Iceberg     DLQ
```

## Phase 2 — Schema Evolution

Planned work:

- [ ] schema versioning
- [ ] compatible schema changes
- [ ] breaking schema changes
- [ ] Iceberg schema evolution
- [ ] producer / consumer compatibility experiments

## Phase 3 — CDC to Lakehouse

Planned work:

- [ ] PostgreSQL source
- [ ] Debezium
- [ ] CDC events through Kafka
- [ ] insert handling
- [ ] update handling
- [ ] delete handling
- [ ] merge/upsert into Iceberg

## Phase 4 — Data Quality

Planned work:

- [ ] null validation
- [ ] uniqueness validation
- [ ] domain rules
- [ ] freshness checks
- [ ] quarantine strategy
- [ ] rejected-record metrics

## Phase 5 — Dataset Versioning

Planned work:

- [ ] Iceberg snapshots
- [ ] time travel
- [ ] historical dataset reconstruction
- [ ] reproducible datasets for AI/ML workloads

## Phase 6 — Batch vs Streaming

Planned work:

- [ ] equivalent batch pipeline
- [ ] equivalent streaming pipeline
- [ ] latency comparison
- [ ] freshness comparison
- [ ] operational complexity comparison

## Phase 7 — AI-Ready Dataset Layer

Planned work:

- [ ] curated datasets
- [ ] feature derivation
- [ ] dataset contracts
- [ ] metadata
- [ ] lineage

## Phase 8 — Incremental Embeddings

Planned work:

- [ ] detect new records
- [ ] detect changed records
- [ ] generate embeddings incrementally
- [ ] avoid unnecessary reprocessing
- [ ] track embedding processing state

## Phase 9 — Retrieval Infrastructure

Planned work:

- [ ] vector storage
- [ ] metadata filtering
- [ ] hybrid retrieval
- [ ] incremental index updates
- [ ] retrieval evaluation

## Phase 10 — Observability

Planned work:

- [ ] ingestion throughput
- [ ] Kafka lag
- [ ] pipeline latency
- [ ] rejected records
- [ ] data freshness
- [ ] Iceberg statistics
- [ ] embedding processing metrics

## Future Exploration

These items are possible later extensions. They are not committed work:

- cloud deployment
- AWS
- Terraform
- orchestration
- Kubernetes
- feature store
- inference
- RAG
- cost monitoring
