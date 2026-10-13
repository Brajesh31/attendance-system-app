# FAQ

## Does this identify people reliably?

No. It is a prototype; similarity thresholds, camera conditions, spoofing, and model limitations can produce false matches or misses.

## What data is stored?

Face embeddings are stored in `academy:register`; recognition events are stored in `attendance:logs`. Both are sensitive and require strict retention and access controls.

## Can I use real employee or student data?

Not without consent, legal/privacy review, security controls, and a documented retention/deletion process.

## Which command starts the app?

`streamlit run Home.py`.

## Where should vulnerabilities be reported?

Use the private process in [SECURITY.md](../SECURITY.md), not a public issue.
