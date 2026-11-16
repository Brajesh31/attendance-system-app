# 🗺️ Roadmap

This roadmap distinguishes current prototype foundations from proposed improvements.

## Existing foundations

- [x] Streamlit multipage application.
- [x] InsightFace buffalo_sc embedding pipeline.
- [x] WebRTC camera integration.
- [x] Redis registration hash and attendance event list.
- [x] Similarity-based matching.
- [x] Daily reporting page.
- [x] Documentation for architecture, privacy, security, QA and deployment.

## Critical security and privacy

- [ ] Replace committed sample user identity and cookie signing key.
- [ ] Centralize Redis configuration using private environment/secret loading.
- [ ] Enforce authenticated authorization for registration, lookup, report and deletion operations.
- [ ] Define consent/notice, non-biometric alternative, purpose limitation and retention.
- [ ] Implement verifiable deletion of templates and events from stores/backups.
- [ ] Add audit trail for sensitive administrative access.
- [ ] Restrict Redis network access with ACLs and TLS.

## Reliability and correctness

- [ ] Fix report retrieval function spelling mismatch.
- [ ] Fix registration role option concatenation.
- [ ] Isolate registration samples per session and cleanup reliably.
- [ ] Scope recognition buffer/timer per stream.
- [ ] Validate embedding dimension/dtype and malformed Redis records.
- [ ] Replace delimiter strings with versioned structured events.
- [ ] Correct report semantics and add review/correction workflow.
- [ ] Add tests for empty/malformed Redis data and multi-session behavior.

## Model and deployment quality

- [ ] Evaluate false acceptance and false rejection with representative, approved data.
- [ ] Evaluate presentation-attack resistance; do not claim liveness without evidence.
- [ ] Document model provenance, license and checksums.
- [ ] Pin tested dependency versions.
- [ ] Add deployment/container/process supervision and Redis backup runbooks.
- [ ] Add monitoring that does not leak personal/biometric content.
- [ ] Define support matrix and release process.

## Priority

Privacy, security, data integrity, and accuracy evaluation take precedence over cosmetic additions or automated attendance decisions.
