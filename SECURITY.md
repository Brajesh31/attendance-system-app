# Security and privacy policy

## Prototype limitations

This application processes face embeddings and attendance records. The current implementation uses a sample `config.yaml`, placeholder Redis connection values, browser camera access, and Redis keys without documented tenant isolation or retention enforcement. These are not production security controls.

Before deployment, require explicit consent, a lawful biometric-data basis, strict access control, encrypted transport and storage, secret management, rate limiting, audit logs, retention/deletion workflows, model abuse safeguards, and a review of false matches and accessibility impact. Never expose Redis directly to the public internet.

## Reporting

Do not publish credentials, biometric data, or exploit details in an issue. Contact Brajesh Kumar privately through <https://github.com/brajesh31> with the affected file, reproduction steps, impact, and a sanitized proof of concept. Report privacy incidents promptly and do not attach face images or embeddings.
