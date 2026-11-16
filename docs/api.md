# 🔌 Application interfaces

The repository does not define a REST or GraphQL HTTP API. Its application interface consists of Streamlit pages, browser camera streams, and Redis data contracts.

## Streamlit pages

| Page | User action | Reads | Writes |
|---|---|---|---|
| `Home.py` | Authenticate and view landing content | YAML auth configuration | Authenticator session/cookie state |
| `pages/1_Real_Time_Prediction.py` | Start live recognition | `academy:register` | `attendance:logs` periodically |
| `pages/2_Registration_form.py` | Enter name/role and capture face samples | Model assets | `face_embedding.txt`, then `academy:register` |
| `pages/3_Report.py` | Refresh registered data/logs/report | `academy:register`, `attendance:logs` | No intended writes |

## Redis contract

See [Redis data model](database.md). Current formats are:

- Hash key: `academy:register`, hash field: `Name@Role`, binary float32 vector.
- List key: `attendance:logs`, list element: `Name@Role@Timestamp`.

## Function-level interface

| Function/class | Module | Input | Output / side effect |
|---|---|---|---|
| `retrive_data(name)` | `face_rec.py` | Redis hash key | DataFrame of names, roles, vectors |
| `ml_search_algorithm(...)` | `face_rec.py` | DataFrame, vector, threshold | Matched name and role or Unknown |
| `RealTimePred.face_prediction(...)` | `face_rec.py` | Image frame and vectors | Annotated image; appends observations |
| `RealTimePred.saveLogs_redis()` | `face_rec.py` | Buffered observations | LPUSH records to Redis |
| `RegistrationForm.get_embedding(frame)` | `face_rec.py` | BGR frame | Annotated frame and detected embedding |
| `RegistrationForm.save_data_in_redis_db(name, role)` | `face_rec.py` | Identity fields and temporary sample file | Stores averaged vector |
| `load_logs(name, end)` | `pages/3_Report.py` | Redis list key | List of raw Redis values |

**Known mismatch:** report code calls `retrieve_data`; only `retrive_data` is defined in the shared module. The report refresh action therefore needs a source fix before it can be relied on.

## Event format examples

The current code expects a string shape similar to:

```text
Example Person@Student@2026-11-16 09:30:00
```

This example is synthetic. Delimiter-based parsing is fragile and should be replaced with a validated structured schema before extending the interface.
