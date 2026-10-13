# Architecture

The application is a Streamlit multipage app with shared recognition logic and Redis persistence.

## Components

- `Home.py` configures Streamlit authentication and the landing page.
- `auth.py` loads `config.yaml` and creates the authenticator.
- `face_rec.py` initializes InsightFace, reads Redis embeddings, compares vectors, and buffers attendance events.
- `pages/1_Real_Time_Prediction.py` captures WebRTC frames and invokes recognition.
- `pages/2_Registration_form.py` captures samples and stores an averaged embedding.
- `pages/3_Report.py` reads Redis and aggregates daily attendance.
- `upload_logs.py` imports simulated log lines into Redis.

## Runtime flow

Registration writes `Name@Role` fields to the `academy:register` Redis hash. Recognition performs cosine similarity against those embeddings and pushes recognized events to `attendance:logs`. Reporting parses those events into a pandas DataFrame.
