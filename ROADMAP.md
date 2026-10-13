# Roadmap

## Reliability

- Add automated tests for embedding search, Redis serialization, and report aggregation.
- Add explicit configuration validation and health checks.
- Resolve entry-point and dependency compatibility across supported Python versions.

## Security and privacy

- Move Redis and authentication secrets to a secret manager.
- Add consent, retention, deletion, access audit, and tenant isolation controls.
- Encrypt biometric data in transit and at rest and restrict operator access.
- Add evaluation for false positives, false negatives, and spoofing.

## Product

- Improve camera/device error handling and offline behavior.
- Add export controls and administrator audit views.
- Document model licensing and a repeatable model-download process.
