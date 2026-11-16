# 🚀 Installation

## System requirements

| Requirement | Guidance |
|---|---|
| Python | 3.10+ is a practical starting point; validate exact supported versions |
| pip | Current pip recommended |
| Redis | Local or managed private instance |
| Camera | Browser-accessible camera for live features |
| Browser | WebRTC support and camera permission |
| Runtime | CPU ONNX Runtime is configured by default |
| Storage | Space for model files, Python packages, and Redis data |

The repository includes ONNX model files under `insightface_model/models/buffalo_sc/`. The larger model file is approximately 13.6 MB, so a fresh clone and package install may take time.

## Clone

```bash
git clone https://github.com/Brajesh31/attendance-system-app.git
cd attendance-system-app
```

## Virtual environment

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Activate on macOS/Linux:

```bash
source .venv/bin/activate
```

## Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If OpenCV, InsightFace, or ONNX Runtime fails to install, record OS version, Python version, architecture, and the exact sanitized pip error. Do not randomly install GPU packages when the source explicitly configures CPU execution.

## Configure Redis

1. Start a local Redis instance or provision a private managed one.
2. Require authentication and TLS for remote traffic.
3. Restrict access by network ACL.
4. Create a disposable database/namespace for development.
5. Externalize connection settings in source before expecting `.env.example` values to take effect.

The existing source has placeholder connection values in two modules. A configuration refactor is required.

## Configure authentication

Do not run the committed sample account/key in a shared environment. Create a private authenticator configuration with a unique strong password hash, a random cookie key, and only intended operators. Keep the file outside version control and restrict file permissions.

## Start the app

```bash
streamlit run Home.py
```

Streamlit normally prints a localhost URL on port 8501. A camera may require HTTPS in a remote deployment.

## Verify installation

- Login screen loads.
- Redis is reachable with the configured credentials.
- InsightFace can load the local model.
- Browser can start a WebRTC stream.
- No-face frames do not crash the callback.
- Registration stores a test vector in disposable Redis.
- Recognition can return Unknown for an unregistered test identity.
- Reporting parses a synthetic event list (after correcting the known function-name mismatch).

See [Troubleshooting](troubleshooting.md).
