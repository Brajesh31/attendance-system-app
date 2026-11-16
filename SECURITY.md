# 🔐 Security policy

## Project status

This repository is an educational face-attendance prototype. It is not a production identity-verification or attendance system. Face embeddings are sensitive biometric data. The source contains sample configuration secrets and multiple security/privacy gaps documented in docs/security-review.md.

## Reporting a vulnerability

Use GitHub's private Security Advisories:
https://github.com/Brajesh31/attendance-system-app/security/advisories/new

Do not publish biometric samples, embeddings, real attendance events, passwords, cookie values or private endpoints in public issues.

Include the affected commit/file, environment, minimal synthetic reproduction, expected/actual behavior and sanitized logs.

## Known areas requiring review

- Sample account and cookie signing key in config.yaml.
- Hard-coded Redis connection placeholders in Python modules.
- Biometric template and attendance event access control.
- Shared temporary registration file and global mutable recognition state.
- Missing demonstrated consent, retention, deletion and access-audit workflows.
- No demonstrated liveness/anti-spoofing or validated model performance.
- Delimiter-based unversioned Redis event format.

## Safe use

Use only isolated development environments and synthetic or explicitly authorized test data. Do not use real biometric data or consequential attendance decisions without qualified legal/privacy review, explicit governance, accessible alternatives, security testing and model evaluation.

## Response

Restrict access, preserve evidence, rotate exposed secrets, assess impact, follow applicable notification duties, remediate root causes and add regression tests. Passing CI does not constitute penetration testing or biometric validation.
