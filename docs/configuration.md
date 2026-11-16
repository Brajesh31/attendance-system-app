# ⚙️ Configuration and secrets

## Current configuration sources

| Setting | File | Current behavior |
|---|---|---|
| Streamlit authenticator users | `config.yaml` | YAML loaded by `auth.py` |
| Cookie name/key/expiry | `config.yaml` | Passed to authenticator |
| Redis hostname/port/password | `face_rec.py` | Hard-coded placeholders |
| Redis hostname/port/password | `upload_logs.py` | Separate hard-coded placeholders |
| Model root/name/provider | `face_rec.py` | Hard-coded model settings |
| Similarity threshold | Live page call | Hard-coded 0.5 |
| Attendance flush interval | Live page | Hard-coded 30 seconds |

## Critical committed sample values

The committed `config.yaml` contains a human name/email, a password hash derived from a trivial sample password, a preauthorized email, and a sample cookie signing key. This must not be used in any shared environment. Remove the sample identity and replace the signing key with a random secret. If the account/key has ever been used outside a local demo, rotate it and invalidate existing cookies.

## Environment example caveat

`.env.example` documents `REDIS_HOST`, `REDIS_PORT`, and `REDIS_PASSWORD`, but the source does not load these values. There is no dotenv integration. Merely creating a local `.env` file will not configure the existing Redis clients.

## Recommended configuration refactor

1. Introduce a single settings module.
2. Read required values from process environment or an approved secret manager.
3. Validate missing values and types at startup.
4. Use TLS and certificate verification for remote Redis.
5. Inject a configured Redis client into application services.
6. Keep a sanitized template such as `config.example.yaml`, with no real identity or secrets.
7. Make startup fail closed if production credentials or encryption settings are missing.

Example environment variable names for a future implementation:

```dotenv
APP_ENV=development
REDIS_HOST=127.0.0.1
REDIS_PORT=6379
REDIS_USERNAME=
REDIS_PASSWORD=
REDIS_TLS=false
STREAMLIT_AUTH_CONFIG=/run/secrets/attendance-auth.yaml
FACE_MODEL_ROOT=insightface_model
FACE_MODEL_NAME=buffalo_sc
FACE_MATCH_THRESHOLD=0.5
ATTENDANCE_FLUSH_SECONDS=30
```

These names are a proposed contract; the current code does not consume them.

## Secret handling checklist

- Never commit a Redis URL/password, cookie signing key, auth password, or cloud token.
- Never log secrets or full connection URLs.
- Scope Redis credentials to the minimum required keyspace and commands.
- Rotate secrets after exposure and invalidate old sessions.
- Restrict filesystem permissions on private configuration.
- Scan repository history and CI logs when responding to an exposure.
