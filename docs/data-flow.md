# 🔄 Data flow and lifecycle

## Registration

```mermaid
sequenceDiagram
    actor Operator
    participant UI as Streamlit registration
    participant RTC as WebRTC camera
    participant Model as InsightFace
    participant File as Local temporary file
    participant Redis
    Operator->>UI: Enter name and role
    UI->>RTC: Start video stream
    RTC->>UI: Video frame
    UI->>Model: Extract face embedding
    Model-->>UI: 512-value vector when a face is found
    UI->>File: Append vector to face_embedding.txt
    Operator->>UI: Submit registration
    UI->>File: Load and reshape samples
    UI->>UI: Calculate coordinate mean
    UI->>Redis: HSET academy:register Name@Role, bytes
    UI-->>Operator: Show result
```

The temporary file is a concurrency and privacy risk. It is written in the process working directory and is not scoped to an individual browser session. A safer design uses per-session memory or isolated temporary storage with explicit cleanup.

## Recognition

```mermaid
sequenceDiagram
    actor Operator
    participant Browser
    participant Streamlit
    participant Model as InsightFace
    participant Redis
    Browser->>Streamlit: WebRTC frame
    Streamlit->>Model: Detect faces and embeddings
    Model-->>Streamlit: Face bounding boxes and vectors
    Streamlit->>Redis: HGETALL academy:register
    Redis-->>Streamlit: Stored vector bytes
    Streamlit->>Streamlit: Decode float32 vectors
    Streamlit->>Streamlit: Compute cosine similarities
    Streamlit->>Streamlit: Select best qualifying match
    Streamlit->>Streamlit: Buffer recognized event
    Streamlit->>Redis: LPUSH attendance:logs periodically
```

## Report

```mermaid
sequenceDiagram
    actor Viewer
    participant UI as Report page
    participant Redis
    participant Pandas
    Viewer->>UI: Refresh report
    UI->>Redis: LRANGE attendance:logs
    Redis-->>UI: Event records
    UI->>Pandas: Decode, parse and group
    Pandas-->>UI: Daily aggregate table
    UI-->>Viewer: Render inferred summary
```

## Data inventory and sensitivity

| Data | Source | Current location | Sensitivity |
|---|---|---|---|
| Face image frame | User camera | In-memory frame callback | High |
| Face embedding | InsightFace model | Temporary file and Redis hash | Very high, biometric |
| Name and role | Registration input | Redis hash field | Personal data |
| Attendance timestamp | Recognition callback | Redis list | Personal/behavioral |
| Authentication user/email | YAML configuration | `config.yaml` | Personal and account data |
| Cookie signing key | YAML configuration | `config.yaml` | Secret |

## Lifecycle gaps

The code does not implement a consent record, purpose/expiry metadata, deletion request path, export approval, correction workflow, or proof of deletion. Redis backups and replicas can also preserve records beyond deletion from the primary keyspace. Define lifecycle controls across primary data, backups, logs, and temporary files.
