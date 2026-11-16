# 🗺️ Roadmap

This roadmap is ordered by risk reduction. New visual features should not take priority over protecting people and correcting data integrity.

## Phase 1: Configuration and correctness
- [ ] Remove sample identity and cookie key from shared configuration.
- [ ] Add secret-safe auth configuration template.
- [ ] Centralize Redis configuration and validate startup.
- [ ] Fix reporting function-name mismatch.
- [ ] Fix registration role option tuple.
- [ ] Isolate registration samples by session.
- [ ] Remove module import-time UI side effects.

## Phase 2: Data contracts and tests
- [ ] Version embedding records and validate model/dimension.
- [ ] Replace delimiter-based attendance strings with structured events.
- [ ] Normalize timestamps to UTC with explicit timezone display.
- [ ] Add unit tests for matching, codecs, parsing, and reporting.
- [ ] Add integration tests against disposable Redis.
- [ ] Add pinned/constraints dependency strategy.

## Phase 3: Privacy and security
- [ ] Document consent and lawful basis.
- [ ] Provide non-biometric attendance method.
- [ ] Implement role-based access and audit trail.
- [ ] Implement expiry, deletion, correction, and backup retention.
- [ ] Perform privacy impact and security review.
- [ ] Evaluate accuracy and spoof risks with an approved protocol.

## Phase 4: Operations and maintainability
- [ ] Add validated deployment manifests.
- [ ] Add health diagnostics and resource monitoring.
- [ ] Add backup/restore and incident runbooks.
- [ ] Add accessible empty/error/loading states.
- [ ] Verify model/package licensing and provenance.

No item should be represented as implemented until merged, tested, and documented.
