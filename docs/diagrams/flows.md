# 🔁 System flow diagrams

## 1. System context

```mermaid
flowchart LR
    U["Operator browser"] <-->|"HTTPS / Streamlit"| APP["Streamlit app"]
    CAM["Camera"] -->|"WebRTC frames"| APP
    APP --> MODEL["InsightFace + ONNX"]
    APP <-->|"Redis protocol"| REDIS[("Private Redis")]
    APP --> OUT["Pages and report tables"]
```

## 2. Runtime components

```mermaid
flowchart TD
    ENTRY["Home.py"] --> AUTH["auth.py"]
    ENTRY --> PAGES["Streamlit page discovery"]
    PAGES --> LIVE["1_Real_Time_Prediction.py"]
    PAGES --> REG["2_Registration_form.py"]
    PAGES --> REPORT["3_Report.py"]
    LIVE --> CORE["face_rec.py"]
    REG --> CORE
    REPORT --> CORE
    CORE --> DB[("Redis")]
    CORE --> MODEL["FaceAnalysis buffalo_sc"]
```

## 3. Registration sequence

```mermaid
sequenceDiagram
    actor User
    participant Page as Registration page
    participant Model as InsightFace
    participant Temp as Temporary sample file
    participant Redis
    User->>Page: Provide name and role
    Page->>Model: Process video frame
    Model-->>Page: Face embedding
    Page->>Temp: Append embedding sample
    User->>Page: Submit
    Page->>Temp: Load and reshape vectors
    Page->>Page: Mean across samples
    Page->>Redis: HSET academy:register
    Redis-->>Page: Write result
```

## 4. Recognition sequence

```mermaid
sequenceDiagram
    participant Camera as Browser camera
    participant Page as Recognition page
    participant Model as InsightFace
    participant Redis
    Camera->>Page: Video frame
    Page->>Model: Detect face and extract vector
    Model-->>Page: Bounding box and embedding
    Page->>Redis: HGETALL academy:register
    Redis-->>Page: Stored float32 vectors
    Page->>Page: Compute cosine similarity
    Page->>Page: Select match or Unknown
    Page->>Page: Buffer sighting
    Page->>Redis: LPUSH attendance:logs periodically
```

## 5. Reporting sequence

```mermaid
sequenceDiagram
    actor Viewer
    participant Report as Report page
    participant Redis
    participant Pandas
    Viewer->>Report: Refresh attendance
    Report->>Redis: LRANGE attendance:logs
    Redis-->>Report: Raw event bytes
    Report->>Pandas: Decode, parse, group
    Pandas-->>Report: Daily aggregate
    Report-->>Viewer: Table
```

## 6. Biometric data lifecycle

```mermaid
flowchart TD
    A["Define approved purpose"] --> B["Notice and alternative method"]
    B --> C{"Appropriate consent/legal basis?"}
    C -->|"No"| D["Do not enroll; use alternative"]
    C -->|"Yes"| E["Collect minimum sample"]
    E --> F["Store protected template"]
    F --> G["Limited recognition use"]
    G --> H["Retention period reached or withdrawal"]
    H --> I["Delete primary, temporary and backup copies"]
    I --> J["Record deletion confirmation"]
```

## 7. Deployment topology

```mermaid
flowchart LR
    B["Browser"] -->|"HTTPS"| RP["Apache reverse proxy"]
    RP -->|"HTTP / WebSocket"| ST["Streamlit private listener"]
    ST -->|"Private Redis connection"| R[("Redis service")]
    ST --> M["Local ONNX model files"]
    OPS["System operator"] --> HOST["Hardened host"]
    HOST --> RP
    HOST --> ST
```

## 8. Failure boundaries

```mermaid
flowchart TD
    A["Page action"] --> B{"Dependency available?"}
    B -->|"Redis unavailable"| R["Show datastore error"]
    B -->|"Model unavailable"| M["Show model initialization error"]
    B -->|"Camera unavailable"| C["Show permission/network guidance"]
    B -->|"All ready"| D["Run requested operation"]
    D --> E{"Input valid?"}
    E -->|"No"| V["Reject with safe validation message"]
    E -->|"Yes"| OK["Continue and record sanitized outcome"]
```

## Diagram maintenance

These diagrams describe current architecture at a conceptual level or a clearly labeled target lifecycle. They do not prove that all source paths work. Keep known defects linked from [known issues](../known-issues.md).
