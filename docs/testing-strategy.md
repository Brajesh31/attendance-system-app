# ✅ Testing strategy

## Current state

The repository has no automated test directory, test runner configuration, linter, or continuous integration test job. The only reproducible baseline currently available from the source is Python compilation.

```bash
python -m compileall -q Home.py auth.py face_rec.py upload_logs.py pages
```

Compilation does not import dependencies or prove runtime operation.

## Recommended test layers

### Unit tests

- Cosine similarity for identical, orthogonal, and below-threshold vectors.
- Unknown behavior for empty registration data.
- Float32 byte serialization and deserialization.
- Vector dimension and dtype validation.
- Registration aggregation and sample count.
- Attendance event parser and timestamp normalization.
- Report grouping and duration edge cases.

### Integration tests

Use a disposable Redis service and synthetic vectors to verify:
- HSET/HGETALL registration contract.
- LPUSH/LRANGE event contract.
- Empty and unavailable Redis handling.
- Duplicate subject behavior.
- Data expiry and deletion once implemented.

### UI/system tests

- Authentication page and session transitions.
- Page navigation.
- WebRTC camera available/unavailable paths.
- Registration submission validation.
- Report rendering for valid, empty, and malformed data.

## Test-data policy

Never commit biometric data. Generate synthetic vectors for most unit tests. For integration tests requiring images, obtain explicit approval and consent, store them outside version control, use the minimum necessary data, restrict access, and delete on schedule.

## Future test organization

```text
tests/
├── unit/
│   ├── test_similarity.py
│   ├── test_embedding_codec.py
│   ├── test_event_parser.py
│   └── test_reporting.py
├── integration/
│   ├── test_redis_registration.py
│   └── test_redis_attendance.py
├── fixtures/
│   └── synthetic_vectors.py
└── conftest.py
```

This is a proposed structure, not a claim that the test files already exist.
