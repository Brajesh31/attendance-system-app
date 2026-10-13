# Application interfaces

This project does not expose a public HTTP API. Its interfaces are Streamlit pages and Redis data contracts.

## Streamlit pages

| Page | Responsibility |
| --- | --- |
| `Home.py` | Authentication and landing page |
| `pages/1_Real_Time_Prediction.py` | Live face recognition and attendance capture |
| `pages/2_Registration_form.py` | Name/role entry and embedding capture |
| `pages/3_Report.py` | Registered data, raw logs, and daily reports |

## Redis contracts

- `academy:register`: hash field `Name@Role`, value is a float32 embedding byte string.
- `attendance:logs`: list values formatted as `Name@Role@Timestamp`.

Changing these formats requires coordinated updates to recognition, registration, reporting, and import scripts.
