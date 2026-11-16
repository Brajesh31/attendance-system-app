# 🧨 Threat model

## Assets

- Face images and live camera frames.
- Face embeddings and identity association.
- Attendance observations and derived reports.
- Authentication credentials and cookie signing key.
- Redis service credentials and data.
- Model files and Python dependencies.

## Trust boundaries

- Browser to Streamlit over HTTPS/WebRTC.
- Streamlit process to Redis.
- Application process to local model assets.
- Operator authentication to privileged pages.
- Repository and CI to deployable configuration.

## Threat scenarios

| Scenario | Potential impact | Controls to require |
|---|---|---|
| Public Redis exposure | Exfiltration or modification of biometric/event data | Network isolation, ACL, TLS |
| Reused sample cookie key | Forged or replayed session cookies | Secret rotation, strong random key |
| Malicious camera replay | False attendance observation | Liveness evaluation and human review |
| Compromised operator account | Enrollment/report misuse | MFA/SSO, least privilege, audit |
| Malicious model asset | Code/runtime compromise or manipulated output | Trusted provenance and checksum |
| Temporary file collision | Wrong person/vector association | Session-specific isolated state |
| Malformed event injection | Report corruption or parsing failure | Schema validation and safe parser |
| Excessive retention | Long-term privacy harm | TTL, deletion and backup expiry |
| Insider export | Unauthorized disclosure | Export approval, audit, least privilege |

## Out of scope for current prototype

The source does not show a liveness subsystem, organization tenancy, production key management, formal incident response integration, or a complete access-control matrix. Treat these as missing controls, not assumed protections.
