# Installation

## Prerequisites

Install Python 3.10+, Redis, and a browser/camera compatible with WebRTC. CPU ONNX Runtime is used by default.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
```

Provide Redis connectivity and a private Streamlit authenticator configuration. Do not use the committed sample email, password hash, or cookie key for shared environments.

## Run

```bash
streamlit run Home.py
```

The model directory must contain the InsightFace assets expected by `FaceAnalysis(name='buffalo_sc', root='insightface_model')`.
