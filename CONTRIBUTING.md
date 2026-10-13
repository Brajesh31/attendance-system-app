# Contributing

Contributions should preserve privacy and keep the project useful as an educational prototype.

## Development workflow

1. Create a focused branch.
2. Use synthetic names, images, embeddings, and attendance records.
3. Configure a disposable Redis instance and an untracked authentication file.
4. Run `python -m compileall .` and manually exercise affected Streamlit pages.
5. Document changes to Redis keys, model behavior, or privacy controls.

Do not commit passwords, Redis URLs, cookie keys, face images, embeddings, camera captures, or attendance logs. Pull requests should explain consent, retention, and access-control implications for any biometric feature.
