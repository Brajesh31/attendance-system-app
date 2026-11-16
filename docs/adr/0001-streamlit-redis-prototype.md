# ADR 0001: Streamlit and Redis prototype

- **Status:** Accepted for the educational prototype
- **Date:** 2026-11-16
- **Decision owners:** Repository maintainers

## Context

The project demonstrates face registration, real-time recognition, and reporting in a small Python codebase. Streamlit provides rapid UI iteration and multipage navigation. Redis provides a simple hash for registration vectors and a list for attendance observations.

## Decision

Use Streamlit for the interactive pages, InsightFace and ONNX Runtime for face analysis, NumPy/scikit-learn for vector operations, and Redis for the current prototype's persistence.

## Consequences

### Benefits
- Small number of components.
- Easy local demonstration.
- Shared recognition code between pages.
- Fast iteration on computer-vision experiments.

### Costs and risks
- UI, inference, and Redis operations are coupled in one process.
- Module-level initialization complicates tests and recovery.
- Global callback state has concurrency implications.
- Redis key formats are informal and weakly versioned.
- Biometric governance is not built in.
- Current implementation is unsuitable for high-impact attendance decisions.

## Revisit when

- Multiple institutions or tenants are required.
- High availability or high throughput is required.
- Attendance affects pay, grades, access, or disciplinary decisions.
- Formal audit, retention, correction, or deletion controls are required.
- Recognition models or data formats change.
