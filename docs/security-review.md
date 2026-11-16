# 🔐 Security review

## Scope

This review is based on the checked-in application files and configuration. It is a source-level risk assessment, not a penetration test or legal compliance certification.

## High-priority findings

| ID | Finding | Evidence | Risk | Recommended action |
|---|---|---|---|---|
| SEC-01 | Sample authentication identity and cookie signing key committed | `config.yaml` | Account exposure/session forgery if reused | Remove sample values from deployment path, rotate key, invalidate cookies |
| SEC-02 | Redis credentials are placeholders hard-coded in modules | `face_rec.py`, `upload_logs.py` | Secret/config hygiene failure and weak deployment safety | Centralize environment/secret manager config |
| SEC-03 | Sensitive biometric vectors stored as raw bytes | `face_rec.py` | Unauthorized access may expose biometric identifiers | Restrict Redis access, encryption, retention and deletion |
| SEC-04 | Fixed temporary embedding filename | `face_rec.py`, registration page | Cross-session collisions and local data exposure | Session-scoped memory or isolated secure temp file |
| SEC-05 | No liveness/anti-spoofing implementation shown | Recognition flow | Photo/video spoofing risk | Do not claim identity assurance; evaluate controls |
| SEC-06 | No demonstrated role-based authorization for reports/admin actions | Page structure | Excessive access to biometric and attendance data | Enforce roles server-side at every data operation |
| SEC-07 | Attendance events contain personal labels and timestamps | Redis list | Behavior tracking and excessive retention | Pseudonymize, minimize and expire records |
| SEC-08 | Import-time side effects in authentication and model modules | `auth.py`, `face_rec.py` | Fragile app initialization and test isolation | Use explicit factories and dependency injection |

## Threat actors

- Unauthorized internet user probing exposed Streamlit or Redis services.
- Malicious or compromised authenticated operator.
- Person attempting to spoof recognition with an image/video.
- Insider accessing attendance history without legitimate purpose.
- Accidental operator misconfiguration or data export.
- Compromised dependency/model artifact.

## Required baseline controls

1. Keep Redis private and protected with ACL/TLS.
2. Remove committed sample identities and rotate cookie signing keys.
3. Use secret storage for auth and datastore credentials.
4. Restrict access to enrollment, live recognition, reports, and deletion.
5. Define consent, retention, deletion, and alternative procedures.
6. Validate event and vector dimensions before processing.
7. Audit administrative access without recording raw biometric values.
8. Keep dependencies patched and model assets verified.
9. Test authentication and authorization separately from UI visibility.
10. Prepare an incident response plan for biometric-data exposure.

## Security acceptance criteria

Do not consider the application production-ready until the high-risk findings have owners, fixes, independent verification, and documented residual risk. See [Threat model](threat-model.md) and [Risk register](risk-register.md).
