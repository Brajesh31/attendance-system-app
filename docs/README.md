# 📚 Documentation hub

Welcome to the technical documentation for the Face Attendance System. This project combines a Streamlit multipage application, InsightFace embedding extraction, Redis persistence, and pandas-based attendance reporting.

> **Scope warning:** these documents describe the checked-in prototype. They do not certify biometric accuracy, legal compliance, security, or production readiness. Read [Data privacy](data-privacy.md) and [Security review](security-review.md) before operating on real identities.

## Start here

| Goal | Read |
|---|---|
| Understand the product and boundaries | [Product overview](product-overview.md) |
| Install and run locally | [Installation](installation.md), [Configuration](configuration.md) |
| Understand the source layout | [Architecture](architecture.md), [Project structure](project-structure.md) |
| Trace recognition and storage | [System design](system-design.md), [Data flow](data-flow.md), [Database](database.md) |
| Understand app interfaces | [Application interfaces](api.md) |
| Prepare a deployment | [Deployment](deployment.md), [Operations](operations.md) |
| Assess privacy and security | [Data privacy](data-privacy.md), [Security review](security-review.md), [Threat model](threat-model.md) |
| Test a change | [QA strategy](qa.md), [Testing strategy](testing-strategy.md) |
| Diagnose errors | [Troubleshooting](troubleshooting.md), [Known issues](known-issues.md) |
| Contribute | [Development](development.md), [Contribution policy](../CONTRIBUTING.md) |
| Understand terminology | [Glossary](glossary.md) |
| Navigate diagrams | [Diagram index](diagrams/README.md) |
| Capture genuine product images | [Demo policy](demo/README.md) |

## Current system at a glance

- **UI:** Streamlit and its multipage page discovery.
- **Authentication:** `streamlit-authenticator`, configured from YAML.
- **Camera:** `streamlit-webrtc` video-frame callbacks.
- **Face analysis:** InsightFace `buffalo_sc`, CPU ONNX Runtime.
- **Matching:** cosine similarity over registered float32 embeddings.
- **Persistence:** Redis hash `academy:register` and list `attendance:logs`.
- **Reporting:** pandas aggregation over event strings.

## Data and privacy boundary

The system can handle face embeddings, identity labels, timestamps, roles, and attendance histories. Treat all of them as sensitive. Do not include live face images, embeddings, real names, emails, or attendance records in issues, pull requests, screenshots, test fixtures, or logs. Use synthetic data unless the responsible institution has approved the processing.

## Document maintenance rules

1. Keep statements about current behavior tied to a checked-in source file.
2. Label intended future behavior as proposed, not implemented.
3. Update the Redis contract and flow diagrams whenever serialization or key names change.
4. Do not publish credentials or biometric data in documentation.
5. Keep screenshot examples genuine and synthetic-data-only.
6. Record breaking data-contract changes and migration steps.

See [Documentation maintenance](documentation-maintenance.md).
