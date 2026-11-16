# 🎯 Product overview

## Purpose

The Face Attendance System is a learning prototype that explores automatic attendance event collection using facial embeddings. It demonstrates a workflow from person registration to live face matching and a derived daily report.

It is not a verified identity system, payroll system, student information system, access-control device, or authoritative source of attendance. The project does not demonstrate the governance and controls required to make consequential attendance decisions.

## Intended learning outcomes

- Understand a Streamlit multipage Python application.
- Capture frames using browser camera and WebRTC.
- Extract embeddings with a pretrained face-analysis model.
- Compare vectors using cosine similarity.
- Serialize vector values and store them in Redis.
- Aggregate timestamped events with pandas.

## Actors represented in the source

| Actor | Current relationship |
|---|---|
| Administrator/operator | Uses the configured Streamlit authenticator |
| Person being registered | Name and role are associated with a stored face vector |
| Attendance operator | Starts a camera recognition session |
| Report viewer | Reads registration and attendance data |

The code does not provide robust role-based authorization for these distinct actors. This is a design gap.

## Core workflow boundaries

1. Registration captures face samples and writes a mean vector.
2. Recognition searches registered vectors for each detected face.
3. Matching names are buffered and periodically written to Redis.
4. Reports interpret event timestamps as first and last observation within a day.

## Non-goals and prohibited assumptions

- A similarity score does not establish legal identity.
- Face recognition is not liveness detection.
- A periodic sighting is not proof of arrival or departure.
- A computed duration is not a legally or institutionally approved attendance decision.
- A successful demo does not establish model fairness or accuracy.
- A Redis key existing does not establish data integrity, access authorization, or retention compliance.

## Success criteria for a responsible prototype

- Installation can be reproduced from documented dependencies.
- Redis data structures are documented and validated.
- Recognition thresholds are evaluated on authorized, consented test data.
- Failed camera, Redis, authentication, and parsing states are visible.
- The operator can inspect and correct records under an auditable policy.
- A non-biometric alternative is available for anyone who declines face processing.
