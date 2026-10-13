# Deployment

Deploy behind an authenticated HTTPS reverse proxy and use a managed Redis service with private networking and TLS. Supply authentication and Redis secrets through the platform secret manager, never through committed YAML or source code.

Before exposing the app:

- obtain and record biometric consent and retention policy;
- enforce operator roles and audit access to embeddings and reports;
- restrict camera permissions and validate WebRTC transport;
- configure Redis backups, expiry/deletion, encryption, and network ACLs;
- monitor false matches, resource usage, and failed authentication;
- document model/license provenance and incident response.

No deployment manifest or CI workflow is provided in this repository.
