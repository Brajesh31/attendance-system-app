# 🔐 Security review

## Scope

This is a source-level review of the tracked application structure and key Python/configuration files. It is not a penetration test, model validation, legal opinion, or security certification.

## Findings

### Critical: sample credentials and cookie signing material

config.yaml contains a sample account identity, a hash for a trivial example password, and a cookie signing key. If reused, these values permit credential abuse or cookie-related compromise.

**Action:** replace sample configuration for every environment, rotate any reused signing key, and keep secrets outside version control.

### High: Redis configuration is hard-coded

face_rec.py and upload_logs.py declare Redis connection details separately. .env.example is not loaded by the current source.

**Action:** centralize configuration, load secrets at startup, fail closed on missing production config, and use Redis ACL/TLS/private networking.

### High: biometric data lifecycle is incomplete

Embeddings and attendance logs are written to Redis. No implemented consent, retention, subject deletion, export/correction, or complete audit workflow is shown.

**Action:** define lawful purpose, consent/alternative process, retention, correction/deletion, access control, and audit.

### High: shared temporary embedding file

Registration samples use face_embedding.txt in the process working directory. Multiple users/sessions can collide or read each other's temporary samples.

**Action:** remove shared mutable disk state; use per-session isolated temporary storage and cleanup on cancellation/completion.

### High: global recognition state

Model/Redis objects and live prediction buffer/timer are module/page-level globals. Multi-session concurrency and thread safety are not established.

**Action:** explicitly scope buffers and timers per stream/session; protect shared model state where required.

### Medium: weak event schema

Records use delimiter-separated strings such as Name@Role@Timestamp. Names/roles containing the delimiter can break parsing. Event format has no version or validation.

**Action:** use structured versioned records with stable subject IDs, UTC timestamps, event type, source, and audit metadata.

### Medium: report semantics overstate observations

Periodic sightings are used to infer first/last attendance times, and a minimum span rule determines present status. This does not prove exact arrival or departure.

**Action:** label values as first/last observed, add human correction and a documented policy, or use explicit verified check-in/out events.

### Medium: runtime defects

Known spelling mismatch in report retrieval function and adjacent role string literals in registration page are recorded in known-issues.md.

**Action:** fix with focused tests and regression coverage.

## Secure deployment minimum

Do not use real people until secrets, Redis access, biometric access, consent, alternative attendance, retention, deletion, model accuracy, spoof resistance, and incident response have been reviewed and approved. See threat-model.md and data-privacy.md.