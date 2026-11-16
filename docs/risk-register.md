# ⚠️ Risk register

| Risk | Likelihood | Impact | Priority | Mitigation |
|---|---|---|---|---|
| Reused sample auth/cookie secret | Medium | High | Critical | Replace and rotate; private config |
| Unauthorized Redis access | Medium | Critical | Critical | Private network, ACL, TLS, least privilege |
| Biometric template disclosure | Medium | Critical | Critical | Encryption, separation, restricted access, retention |
| False identity match | Medium | High | High | Evaluate FAR/FRR, human review, alternative process |
| Photo/video spoof | Medium | High | High | Do not claim liveness; evaluate anti-spoof controls |
| Incorrect attendance inference | High | High | High | Distinguish sightings from official attendance events |
| Cross-session sample collision | Medium | High | High | Session-isolated capture state |
| Report parsing failure | Medium | Medium | Medium | Structured schema and validation |
| Model asset provenance unclear | Medium | High | High | Verify source, hashes, license and use terms |
| Unbounded event list/retention | High | High | High | Retention limits and lifecycle automation |
| Dependency drift | Medium | Medium | Medium | Pin/test dependencies and schedule updates |
| Camera unavailable | Medium | Medium | Medium | Non-biometric fallback and clear status |

## Risk acceptance

Biometric privacy, unauthorized access, and high-impact false matches should not be accepted merely because this is a student or demo project. Any real-world use requires a named accountable owner, documented review, a mitigation plan, and a non-biometric alternative.
