# 🚀 Installation and local development

## Requirements

- Python 3.10+ as used by existing bytecode caches; no formal tested-version matrix is published.
- Redis reachable by the application process.
- Webcam and browser camera permission for registration/recognition.
- Python packages from requirements.txt.
- Model assets under insightface_model/models/buffalo_sc.
- Native/system compatibility for OpenCV, InsightFace, ONNX Runtime and WebRTC dependencies.

## Clone

~~~bash
git clone https://github.com/Brajesh31/attendance-system-app.git
cd attendance-system-app
~~~

## Create and activate a virtual environment

~~~bash
python -m venv .venv
~~~

Windows PowerShell:

~~~powershell
.venv\Scripts\Activate.ps1
~~~

macOS/Linux:

~~~bash
source .venv/bin/activate
~~~

## Install dependencies

~~~bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
~~~

requirements.txt does not pin exact versions. Introduce a tested lock/constraints file with a platform and Python version matrix for reproducible environments.

## Configure Redis

face_rec.py and upload_logs.py currently use hard-coded Redis connection values. .env.example is not loaded by the application. Do not assume setting variables there changes runtime behavior. A configuration refactor is required. Never expose Redis publicly.

## Review authentication configuration

config.yaml contains sample identity, password hash and cookie signing key. Replace these for every shared environment. Never reuse the sample credentials/key. Restrict configuration file permissions and keep real secrets outside Git.

## Start Redis and Streamlit

Start an isolated local Redis instance, then run:

~~~bash
streamlit run Home.py
~~~

Open the local URL printed by Streamlit, normally http://localhost:8501.

## Local smoke test

1. Confirm app and authentication UI load.
2. Confirm Redis connection using disposable test data.
3. Verify model assets load.
4. Grant browser camera permission.
5. Register a synthetic/consenting test identity.
6. Verify an embedding entry is written.
7. Run recognition and check event writes.
8. Open report and test empty, valid and malformed event data.

## Safety boundary

Use synthetic data only. Do not enroll real people without documented legal basis, consent where required, a non-biometric alternative, risk assessment and approval. This is not a production deployment guide.