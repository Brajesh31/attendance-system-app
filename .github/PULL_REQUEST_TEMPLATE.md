## 🎯 Summary

Describe the change, user need, and expected outcome.

## 🧩 Areas affected

- [ ] Streamlit UI / navigation
- [ ] Authentication / session
- [ ] Face registration / embeddings
- [ ] Live recognition / WebRTC
- [ ] Redis data contracts
- [ ] Attendance reporting
- [ ] Configuration / deployment
- [ ] Documentation / CI

List exact modules and Redis keys affected.

## 🔐 Security and privacy impact

- [ ] No biometric data, face images, personal attendance data, or credentials included in the diff.
- [ ] Purpose and data minimization reviewed.
- [ ] Consent/notice and non-biometric alternative considered.
- [ ] Access control and Redis permissions reviewed.
- [ ] Retention and deletion behavior reviewed.
- [ ] Logs do not include embeddings or personal data.
- [ ] Model threshold/accuracy/spoofing impact evaluated if relevant.

Explain remaining risk and approvals required.

## 🗄️ Data contract / migration

Redis keys or schema changes:
Compatibility and migration plan:
Rollback plan:
Retention/deletion impact:

## 🧪 Validation

- [ ] Python syntax compilation
- [ ] Unit tests
- [ ] Redis integration tests with disposable data
- [ ] Streamlit page/manual workflow checks
- [ ] Empty/malformed data tests
- [ ] Concurrency/session isolation tests
- [ ] Model evaluation where matching behavior changes
- [ ] Documentation links and diagrams reviewed

Commands and actual results:

## 📚 Documentation

- [ ] README updated
- [ ] API/data-model docs updated
- [ ] Architecture/flow diagrams updated
- [ ] Security/threat-model/privacy docs updated
- [ ] CHANGELOG/ROADMAP updated

## ⚠️ Limitations

List untested behavior, assumptions and deferred work.

**Do not attach real face images, embeddings, attendance logs, credentials, or private configuration.**