# ⚠️ Risk register

| ID | Risk | Likelihood | Impact | Priority | Mitigation |
|---|---|---:|---:|---|---|
| R-01 | Committed sample identity/cookie key is reused | Medium | Critical | Critical | Replace and rotate secrets; private config |
| R-02 | Unauthorized access to biometric templates | Medium | Critical | Critical | Access control, Redis ACL/TLS, audit |
| R-03 | False match causes incorrect attendance | Medium | High | High | Threshold evaluation, human correction, alternatives |
| R-04 | No liveness/anti-spoof control | High | High | High | Evaluate presentation-attack detection |
| R-05 | Shared temporary embedding file leaks/mixes sessions | Medium | High | High | Per-session isolated temporary data |
| R-06 | Global timer/buffer affects concurrent users | Medium | High | High | Per-session/stream state isolation |
| R-07 | Malformed vector/event crashes or corrupts report | Medium | Medium | Medium | Versioned schema and validation |
| R-08 | No deletion/retention enforcement | High | High | High | Defined lifecycle and verified deletion |
| R-09 | Unpinned packages change behavior | Medium | Medium | Medium | Tested constraints/lock file |
| R-10 | Redis exposed or weakly configured | Medium | Critical | Critical | Private network, ACL, TLS, firewall |
| R-11 | Report span misrepresents actual time | High | High | High | Explicit check-in/out and correction |
| R-12 | Model/license provenance unclear | Medium | High | High | Verify model terms, provenance and notices |

## Risk acceptance

A risk cannot be accepted solely because a prototype is educational. A pilot involving real people, biometric data, or consequential attendance decisions needs a documented owner, legal/privacy assessment, accessible alternative, and security/model evaluation.