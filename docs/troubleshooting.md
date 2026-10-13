# Troubleshooting

## Streamlit cannot start

Activate the intended virtual environment, install `requirements.txt`, and run `streamlit run Home.py` from the repository root.

## Redis connection fails

Confirm the host, port, password, TLS mode, and network access. Do not paste credentials into issue reports. A local disposable Redis instance is easiest for development.

## No faces are recognized

Confirm the `buffalo_sc` model files exist, the camera is permitted, lighting is adequate, and the stored embedding was registered with the same preprocessing/model. Review the similarity threshold before changing it.

## Report is empty

Confirm that recognition wrote values to `attendance:logs` and that each value contains exactly `Name@Role@Timestamp`. Clear stale test data only in a disposable Redis database.
