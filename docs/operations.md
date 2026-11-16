# 🧰 Operations runbook

## Service dependencies

| Dependency | Used by | Failure symptom |
|---|---|---|
| Streamlit process | All pages | App unavailable |
| Redis | Registration, recognition, reporting | Data read/write errors |
| InsightFace model assets | Registration and recognition | Model load or inference failure |
| Browser camera/WebRTC | Live and registration pages | No frames or connection state |
| Apache reverse proxy (optional) | Remote deployment | UI/WebSocket proxy failure |

## Startup checks

1. Confirm the intended Python environment is active.
2. Confirm private authentication configuration exists and is not a sample.
3. Confirm Redis endpoint, TLS, credentials, and ACL.
4. Confirm model asset files and runtime provider.
5. Start Streamlit under an unprivileged account.
6. Verify health manually through the browser and a synthetic test workflow.

## Monitoring signals

- Streamlit process liveness and restart count.
- Redis availability, latency, memory, key counts, and rejected connections.
- Model load time, inference latency, CPU and memory.
- WebRTC connection and frame processing failure rate.
- Registration success/failure counts without identity or vector contents.
- Invalid event parse count.
- Report generation latency and row counts.
- Authentication failure and administrative access events.

Do not log raw camera frames, face embeddings, passwords, cookie values, or complete personal attendance rows.

## Backup and restore

Backups can contain biometric templates and attendance history. Encrypt backups, restrict access, set retention, test restore, and ensure deletion requests are propagated to backup expiry or verified purge. Do not copy production data to local development machines.

## Incident response

For suspected biometric exposure: restrict access, preserve sanitized system evidence, involve security/privacy owners, rotate secrets, assess affected data and backups, follow notification duties, and document remediation. Never attach affected biometric samples to public tickets.
