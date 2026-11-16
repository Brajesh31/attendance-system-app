# 🛠️ Operations and maintenance

## Runtime components

The operational dependency chain includes Streamlit, Redis, local InsightFace ONNX model files, camera/WebRTC transport, and the host's native Python/OS libraries.

## Startup checks

- Python runtime and dependencies match the tested constraints.
- Authentication config exists, is private, and contains non-default secrets.
- Redis is reachable on a private interface.
- Required Redis keys are in the expected data format.
- Model directory and ONNX files exist.
- Camera/WebRTC transport works through the deployment route.
- Host clock and reporting timezone are configured consistently.

## Monitoring

Monitor process availability, restart count, memory, CPU, Redis connectivity/latency, WebRTC processing errors, model load failures, malformed events, and report-generation errors. Metrics should avoid names, raw embeddings, camera frames, cookie values, and other personal information.

## Redis care

- Use ACLs and least privilege.
- Restrict network access and enable TLS.
- Separate environments and prevent test/production cross-use.
- Define retention, backup encryption, restore tests, and deletion propagation.
- Monitor memory growth of attendance:logs.

## Incident response

1. Restrict access and preserve security evidence.
2. Rotate affected credentials and signing keys.
3. Restrict Redis network access.
4. Identify affected records and access scope without unnecessary copying.
5. Notify responsible privacy/security owners.
6. Follow applicable notification requirements.
7. Remediate and add regression tests.
8. Verify deletion/retention tasks, including replicas and backups.

## Recovery

Restore Redis only into a restricted environment. Validate key type, embedding length, event schema, timestamp parsing, and retention policy before reopening service. Current event/vector formats are not versioned, so cross-version recovery is fragile.

No production monitoring, alerting, backup schedule, SLO, on-call rota, or disaster-recovery procedure is configured in the source. This document defines requirements, not existing automation.