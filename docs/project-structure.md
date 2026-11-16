# 🗂️ Project structure and file responsibilities

This map describes the tracked application structure. Model binaries are summarized rather than expanded into the tree.

~~~text
attendance-system-app/
├── Home.py                         # Streamlit app entrypoint
├── auth.py                         # Streamlit authenticator setup/UI
├── face_rec.py                     # InsightFace, Redis, registration and matching
├── config.yaml                     # Authenticator sample configuration (replace secrets)
├── .env.example                    # Illustrative environment variable names
├── requirements.txt                # Python dependency list
├── configure.sh                    # Apache reverse-proxy example generator
├── upload_logs.py                  # Simulated attendance-log importer
├── pages/
│   ├── 1_Real_Time_Prediction.py   # WebRTC recognition and event callback
│   ├── 2_Registration_form.py      # Capture and register embeddings
│   └── 3_Report.py                # Redis event parsing and daily report
├── insightface_model/
│   └── models/buffalo_sc/          # Local ONNX model assets
├── docs/
│   ├── assets/                     # Original SVG illustrations
│   ├── diagrams/                   # Workflow/architecture diagrams
│   ├── demo/                       # Screenshot and demo guidance
│   └── adr/                        # Architecture decisions
├── scripts/
│   ├── check_docs.py               # Documentation link/content checks
│   └── check_svg.py                # SVG validation
├── .github/
│   ├── ISSUE_TEMPLATE/             # Bug, feature, docs, privacy templates
│   └── workflows/                  # Documentation quality and README automation
└── README.md
~~~

## Root components

| Path | Responsibility | Main concern |
|---|---|---|
| Home.py | Streamlit page shell | Authentication/UI lifecycle |
| auth.py | streamlit-authenticator integration | Import-time UI side effects |
| face_rec.py | Model setup, vectors, matching, logs | Module globals, Redis config, biometric data |
| config.yaml | Auth users and cookie settings | Sample identity and signing key are committed |
| requirements.txt | Runtime libraries | Dependencies are not pinned |
| upload_logs.py | Import local log data to Redis | Hard-coded Redis placeholder and local input file |
| configure.sh | Apache reverse-proxy example | Placeholder host and TLS paths |

## Generated artifacts

`__pycache__/` contains tracked Python bytecode files in the current repository. They are generated artifacts, not source. This documentation pass preserves them. A separate cleanup should remove tracked caches and maintain `.gitignore` rules.

## Model assets

`insightface_model/models/buffalo_sc/` contains model binaries. Treat model assets as dependent artifacts: document provenance, licensing, version, checksums, and compatibility before changing or redistributing them.