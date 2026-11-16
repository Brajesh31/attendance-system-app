# 🛠️ Development guide

## Working principles

- Use synthetic identities and disposable Redis.
- Never commit face images, face embeddings, real attendance records, or authentication data.
- Keep the recognition algorithm, Redis serialization, and report parser synchronized.
- Do not change thresholds without documenting the evaluation data and false match/false reject trade-off.
- Treat biometric-data lifecycle changes as security-sensitive.

## Local workflow

```bash
git checkout -b feature/short-description
python -m venv .venv
# Activate the virtual environment
python -m pip install -r requirements.txt
python -m compileall -q Home.py auth.py face_rec.py upload_logs.py pages
streamlit run Home.py
```

## Code organization recommendations

1. Move Redis setup and model initialization into explicit service factories.
2. Keep Streamlit page code as UI orchestration, not data access implementation.
3. Make recognition functions pure where possible so vectors can be unit tested without camera or Redis.
4. Use a per-session registration buffer, not a shared current-working-directory file.
5. Use structured records and UTC timestamps for event serialization.
6. Add explicit error types for Redis, model loading, validation, and camera failures.

## Testing data

Use synthetic vectors for unit-level math tests. Use only authorized, consented test images for end-to-end evaluation, store them outside the repository, and delete them according to the test data plan.

## Before opening a PR

- Compile changed Python files.
- Run targeted unit tests.
- Verify no secrets or generated data were added.
- Update data contracts and diagrams if keys or formats changed.
- Update security/privacy docs if collection, matching, identity, or retention behavior changed.
- Explain any change to thresholds with evaluation evidence.
