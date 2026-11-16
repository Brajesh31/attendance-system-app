# 🖼️ Demo and screenshot policy

The repository currently contains no verified application screenshots. The SVGs under `docs/assets/` are technical illustrations, not UI captures.

## Capture workflow

1. Install the app using the documented setup.
2. Use a disposable Redis instance and synthetic test identities.
3. Replace the sample auth config with a local-only test configuration.
4. Avoid real face imagery. Use a controlled synthetic/test image only where the test protocol allows it.
5. Capture each page after checking that no personal data, credentials, or connection details are visible.
6. Crop browser chrome only if it does not hide important app context.
7. Add alt text and a short caption.
8. Record the commit/version used for the capture.

## Suggested screenshot inventory

| File | Screen | Status |
|---|---|---|
| `login.png` | Login screen | Pending real capture |
| `home.png` | Home dashboard | Pending real capture |
| `registration.png` | Registration page | Pending real capture |
| `prediction.png` | Live recognition with synthetic data | Pending real capture |
| `report.png` | Report with synthetic events | Pending real capture |

Do not publish identifiable faces, names, email addresses, embeddings, or actual attendance histories. Never fabricate a screenshot or present diagram artwork as a screenshot.
