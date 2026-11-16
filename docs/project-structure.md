# 🗂️ Project structure

```text
attendance-system-app/
├── .github/
│   ├── ISSUE_TEMPLATE/             # Structured bug, feature and privacy forms
│   ├── workflows/                  # GitHub Actions automation
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── adr/                        # Architecture decisions
│   ├── assets/                     # Technical SVG artwork
│   ├── demo/                       # Real screenshot guidance
│   ├── diagrams/                   # Mermaid diagrams
│   └── *.md                        # Engineering and governance docs
├── insightface_model/
│   └── models/buffalo_sc/          # ONNX face analysis assets
├── pages/
│   ├── 1_Real_Time_Prediction.py   # WebRTC frame recognition
│   ├── 2_Registration_form.py      # Person/embedding registration
│   └── 3_Report.py                 # Logs and inferred report
├── Home.py                         # Streamlit entry page
├── auth.py                         # Authenticator construction
├── face_rec.py                     # Recognition and Redis logic
├── upload_logs.py                  # Simulated event importer
├── config.yaml                     # Current sample auth configuration
├── configure.sh                    # Apache reverse-proxy config generator
├── requirements.txt                # Python dependencies (un-pinned)
├── .env.example                    # Illustrative values, not currently loaded
└── LICENSE
```

## Source roles

### `Home.py`

Sets page title/layout and displays authenticated welcome content. It imports `auth.py`, which itself performs a login operation at import time. This creates a fragile coupling between app bootstrap and authentication.

### `auth.py`

Loads `config.yaml`, builds a Streamlit authenticator, and immediately invokes login. It also contains UI rendering. A future refactor should expose a factory or service and keep page rendering in the app layer.

### `face_rec.py`

Owns the Redis client, FaceAnalysis model, embedding retrieval, cosine matching, event buffering, and registration aggregation. It has module-level initialization side effects.

### `pages/`

Streamlit multipage scripts. Pages import `face_rec` through `Home`, coupling feature code to the application entry script. A neutral service module would be easier to test and avoid page import side effects.

### `insightface_model/`

Contains model files required by the configured InsightFace model root. Review upstream and model-specific terms before redistributing or using commercially.

## Generated and local files

`face_embedding.txt`, `simulated_logs.txt`, local auth configuration, Redis dumps, camera images, and runtime caches are data artifacts, not source code. Keep them out of commits and backups unless an approved retention policy explicitly includes them.
