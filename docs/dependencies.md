# 📦 Dependency and compatibility review

## Declared dependencies

| Package | Purpose | Notes |
|---|---|---|
| numpy | Vector arrays and binary codec | Embedding dimension/dtype contract |
| pandas | Tables and report aggregation | Timestamp parsing and grouping |
| redis | Redis client | Configure TLS and ACL for remote service |
| opencv-python-headless | Frame manipulation | Headless package intended for server use |
| scikit-learn | Cosine similarity | Uses pairwise metrics |
| streamlit | UI and page runtime | Multipage discovery |
| streamlit-webrtc | Browser video streaming | Network and WebRTC configuration |
| insightface | Face detection and embeddings | Check model and package terms |
| onnxruntime | Model inference | CPU provider in source |
| streamlit-authenticator | Login/cookie workflow | Version compatibility matters |

## Reproducibility gap

The current `requirements.txt` has no version constraints. Installation may resolve different versions over time. The repository also does not provide a lockfile or tested platform matrix.

## Recommended maintenance

- Select and document supported Python versions.
- Pin direct dependencies after a successful compatibility test.
- Generate a platform-aware lock/constraints file.
- Run dependency vulnerability scans.
- Review transitive packages and licenses.
- Test Streamlit-authenticator API compatibility.
- Verify InsightFace and ONNX Runtime model loading after updates.
- Avoid unreviewed upgrades in production.
