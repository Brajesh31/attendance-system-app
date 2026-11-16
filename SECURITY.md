# 🔐 Security policy

## Project status

This is an educational face-attendance prototype. It processes biometric embeddings and attendance histories. It is not production-hardened and has known configuration, concurrency, authorization, and privacy gaps. Do not expose it to public networks or use it for consequential attendance decisions without a separate security/privacy program.

## Reporting a vulnerability

Do not publish credentials, biometric vectors, face images, attendance records, or exploit details in a public issue. Use the maintainer contact path at <https://github.com/Brajesh31> and provide the affected component, sanitized reproduction steps, expected impact, and suggested remediation. Do not attach personal or biometric samples.

## Sensitive-data handling

- Treat embeddings as biometric data.
- Treat attendance history as sensitive personal/behavioral data.
- Never commit real configuration, cookie keys, passwords, Redis URLs, camera captures, or production logs.
- Do not expose Redis publicly.
- Rotate any credential that has entered Git history or a public issue.
- Keep incident evidence access-restricted.

## Required deployment controls

Private networking, TLS, Redis ACLs, managed secrets, strong authentication, role-based authorization, consent, retention/deletion, audit logging, backups control, model provenance, and an incident response process are required before any real-person pilot.

## Scope

This policy does not promise a service-level response time. Report urgent exposures through a private channel and notify the data/security owner of the affected organization.
