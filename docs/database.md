# 🗄️ Redis data model

## Storage overview

Redis is used as the application datastore. No relational database or ORM is configured in the inspected repository.

## Current keyspace

### Registration hash

| Attribute | Value |
|---|---|
| Key | `academy:register` |
| Redis type | Hash |
| Field | `Name@Role` |
| Value | Float32 embedding serialized to raw bytes |
| Writer | `RegistrationForm.save_data_in_redis_db` |
| Reader | `retrive_data` in `face_rec.py` |

The reader converts each hash value using `np.frombuffer(..., dtype=np.float32)`, decodes the field as text, and splits it on `@`. The current design assumes two field components and 512 vector coordinates.

### Attendance list

| Attribute | Value |
|---|---|
| Key | `attendance:logs` |
| Redis type | List |
| Value | `Name@Role@Timestamp` |
| Writer | `RealTimePred.saveLogs_redis` and `upload_logs.py` |
| Reader | `pages/3_Report.py` |
| Write operation | `LPUSH` |
| Read operation | `LRANGE` |

## Serialization contract

A registered embedding has 512 float32 values. Its binary representation is not self-describing. The record does not include a model identifier, vector dimension, dtype marker, creation timestamp, consent status, or data version. A future migration should wrap the vector with explicit metadata or use a versioned storage key.

## Current limitations

- Names and roles are combined into a single field with an unescaped delimiter.
- Duplicate identity handling relies on overwriting a hash field.
- No unique internal person ID exists.
- No key TTL or retention enforcement is configured.
- No tenant/organization namespace is implemented.
- No application-level encryption of embeddings is shown.
- No schema validation or invalid-record quarantine is implemented.
- Full attendance history is loaded for report computation.
- Deletion and correction operations are not implemented.

## Operational requirements

Use a dedicated Redis service per environment, private network access, authentication, TLS, least-privilege credentials, monitoring, and approved backup/restore practices. Avoid storing raw face images. Protect embedding access separately from ordinary report access.

## Proposed key design

An example future namespace could be:

| Key pattern | Type | Purpose |
|---|---|---|
| `attendance:v2:subjects:{subject_id}` | Hash | Non-biometric subject metadata |
| `attendance:v2:templates:{subject_id}:{model_version}` | Restricted value/hash | Biometric template |
| `attendance:v2:events:{date}` | Stream/list | Structured observation events |
| `attendance:v2:audit:{date}` | Stream | Administrative access/change audit |

This is a proposal, not an existing schema. A migration must define dual-read/write behavior, validation, rollback, retention, and deletion across old and new key patterns.
