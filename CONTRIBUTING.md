# 🤝 Contributing

Thank you for considering a contribution. This repository is an educational face-recognition attendance prototype. Contributions must preserve privacy and describe limitations honestly.

## Before you begin

- Read [README](README.md), [security policy](SECURITY.md), [privacy guide](docs/data-privacy.md), and [known issues](docs/known-issues.md).
- Use a focused branch and a focused pull request.
- Never use real attendance or biometric data in test fixtures.
- Check model and package licensing before adding assets.

## Development setup

```bash
python -m venv .venv
# Activate the virtual environment
python -m pip install -r requirements.txt
python -m compileall -q Home.py auth.py face_rec.py upload_logs.py pages
```

## Contribution requirements

- Add tests for changed behavior wherever possible.
- Document changes to Redis keys, embedding dimension, dtype, threshold, and timestamp semantics.
- Include privacy impact for any collection, matching, export, or retention change.
- Keep credentials and private config out of commits.
- Do not commit camera captures, face embeddings, Redis dumps, `face_embedding.txt`, or real logs.
- Avoid unrelated formatting churn.
- Update docs and diagrams where architecture changes.

## Pull request checklist

- [ ] Change is scoped and explained.
- [ ] Syntax checks run.
- [ ] Tests added or missing coverage explained.
- [ ] No secrets, biometric data, caches, or generated files added.
- [ ] Redis data contracts are documented.
- [ ] Privacy/security implications reviewed.
- [ ] Screenshots use synthetic/non-identifiable data only.
- [ ] Documentation marks proposed features as proposed.

## Review standard

A face-recognition change must include evaluation evidence and discuss false acceptance/rejection, liveness limitations, accessibility, and a non-biometric alternative. Do not claim production readiness from a successful demo.
