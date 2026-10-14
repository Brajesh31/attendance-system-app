# Face Attendance System

Face Attendance System is a Streamlit prototype that registers face embeddings, recognizes faces from a live WebRTC stream, and writes attendance events to Redis. It uses InsightFace with the bundled `buffalo_sc` ONNX model and provides pages for live recognition, registration, and reporting.

> **Privacy and security warning:** Facial embeddings are biometric data. This repository is an educational prototype and is not ready for production or unsupervised use. Do not upload real biometric data, credentials, or identifiable attendance records without consent, access controls, retention rules, and a legal/privacy review.

## Features

- Streamlit authentication using `streamlit-authenticator`.
- Live camera recognition using `streamlit-webrtc`, OpenCV, and InsightFace.
- Registration of a person’s averaged face embedding in Redis.
- Redis-backed attendance logs in `attendance:logs`.
- Reporting by date, name, role, first/last timestamp, duration, and presence status.
- Local `buffalo_sc` model assets under `insightface_model/models/`.

## Requirements

- Python 3.10 or newer.
- Redis reachable from the application.
- A camera and browser that support WebRTC for live pages.
- CPU-compatible ONNX Runtime; GPU execution is not configured by default.

## Setup

```bash
git clone https://github.com/Brajesh31/attendance-system-app.git
cd attendance-system-app
python -m venv .venv
```

Activate the environment (`.venv\Scripts\activate` on Windows or `source .venv/bin/activate` on POSIX), then install:

```bash
python -m pip install -r requirements.txt
```

Configure Redis and authentication through an untracked deployment configuration. The committed `config.yaml` contains sample identity data and a sample cookie key; replace it before any shared run. Redis connection values are currently placeholders in the source and should be externalized.

## Run

The Streamlit entry point is `Home.py`:

```bash
streamlit run Home.py
```

Open the displayed local URL, normally `http://localhost:8501`. The pages are:

- `1_Real_Time_Prediction.py`: camera recognition and log collection.
- `2_Registration_form.py`: captures frames and saves averaged embeddings.
- `3_Report.py`: reads registered data and attendance logs from Redis.

## Data flow

1. Registration captures multiple face embeddings and writes their mean to the Redis hash `academy:register` using `Name@Role` as the field.
2. Recognition compares a live embedding with stored vectors using cosine similarity.
3. Recognized names are buffered and periodically pushed to the Redis list `attendance:logs` as `Name@Role@Timestamp`.
4. The report page parses the list and calculates daily in/out times and duration.

## Development

Keep credentials, Redis endpoints, embeddings, logs, and camera captures outside version control. Validate changes with a disposable Redis database and synthetic identities. There is no automated test suite or lint configuration; at minimum run `python -m compileall` on the Python source and exercise registration, recognition, and reporting manually.

See [docs/architecture.md](docs/architecture.md), [docs/database.md](docs/database.md), and [docs/troubleshooting.md](docs/troubleshooting.md).

## License

This project is available under the MIT License. See [LICENSE](LICENSE).

Last updated: 2026-10-14 00:01 UTC
