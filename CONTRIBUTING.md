# 🤝 Contributing to Face Attendance System

Thank you for considering a contribution. This repository is a Streamlit/InsightFace/Redis prototype that processes biometric data. Correctness, privacy, security and honest reporting are more important than feature count.

## Before opening an issue

- Read README.md and the documentation hub.
- Check known issues and current roadmap.
- Use synthetic identities and disposable Redis data.
- Never attach real face images, embeddings, attendance histories, credentials or private configuration.
- For security/privacy concerns, use the private reporting process in SECURITY.md.

## Local development

~~~bash
python -m venv .venv
python -m pip install -r requirements.txt
streamlit run Home.py
~~~

Start an isolated local Redis instance first. See docs/installation.md. Replace all sample authentication/configuration secrets.

## Coding expectations

- Use typed, validated data at module boundaries where practical.
- Do not share temporary registration files between users/sessions.
- Avoid process-global mutable attendance buffers/timers.
- Use stable subject IDs rather than delimiter-concatenated names.
- Validate Redis value types, embedding dimensions, dtype, and timestamps.
- Keep face images and embeddings out of logs.
- Fail clearly when Redis or model assets are unavailable.
- Treat threshold changes as model/system changes that require evaluation.
- Maintain a non-biometric attendance path in any real deployment design.

## Tests

Include unit tests, Redis integration tests using disposable data, malformed-input cases, concurrent-session cases, and report edge cases. Changes to matching behavior require evaluation of false acceptance and false rejection, threshold rationale, and uncertainty. Do not claim accuracy without measured evidence.

## Privacy and security review

Any change that collects, stores, matches, exports, or deletes biometric data must include:
- purpose and data-minimization impact;
- consent/notice and alternative workflow;
- access-control implications;
- retention and verified deletion behavior;
- logging and incident-response implications.

## Documentation

Update API/data contracts, architecture and flow diagrams, threat model, privacy documentation, known-issues register, and changelog where affected.

## Pull requests

Use the PR template. State exact commands and results. Mark untested behavior clearly. Never add real personal/biometric data to a diff.
