# ⚙️ Configuration and secrets

## Configuration sources currently used

| Setting | Location | Current behavior |
|---|---|---|
| Authenticator usernames/password hashes | config.yaml | Loaded by authentication integration |
| Cookie name/key/expiry | config.yaml | Used by authenticator |
| Redis host/port/password | face_rec.py | Hard-coded placeholder values |
| Redis host/port/password | upload_logs.py | Separate hard-coded placeholder values |
| Model root/name | face_rec.py | Relative local path and buffalo_sc |
| ONNX provider | face_rec.py | CPUExecutionProvider configured |
| Detection size | face_rec.py | 640 × 640 |
| Matching threshold | Page call | 0.5 passed to search |
| Event flush interval | Live page | 30 seconds |
| Status duration rule | Report page | 60-second span heuristic |

## .env.example limitation

The repository contains .env.example, but the current source does not load it through python-dotenv or a similar mechanism. Its values are documentation placeholders only. A configuration refactor is required before environment variables affect Redis connections.

## Secret handling

- Never commit real passwords, hashes, cookie keys, Redis passwords, tokens, or private endpoints.
- config.yaml includes sample identity and cookie signing material. Replace these before shared use.
- Generate a new cryptographically random cookie signing key for each environment.
- Rotate any secret that may have been reused outside a disposable local environment.
- Keep configuration readable only by the service account.
- Do not print credentials into Streamlit output or logs.

## Proposed environment contract

| Variable | Purpose |
|---|---|
| APP_ENV | Development/staging/production mode |
| REDIS_HOST | Redis host |
| REDIS_PORT | Redis port |
| REDIS_USERNAME | Redis ACL username |
| REDIS_PASSWORD | Redis credential |
| REDIS_TLS | Enable TLS |
| AUTH_CONFIG_PATH | Private authenticator YAML path |
| MODEL_ROOT | Trusted model asset root |
| FACE_MATCH_THRESHOLD | Reviewed matching threshold |
| ATTENDANCE_EVENT_INTERVAL_SECONDS | Event buffer interval |
| APP_TIMEZONE | Explicit reporting timezone |

These names are proposed; current source does not load them.