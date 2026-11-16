# 🧭 Diagram index

All diagrams are maintained as Mermaid source in Markdown so that they can be reviewed and updated with the architecture.

| Diagram | Location | Use |
|---|---|---|
| Application context | [flows.md](flows.md#1-system-context) | Browser, app, Redis and model |
| Runtime modules | [flows.md](flows.md#2-runtime-components) | Page and service dependencies |
| Registration sequence | [flows.md](flows.md#3-registration-sequence) | Embedding capture and persistence |
| Recognition sequence | [flows.md](flows.md#4-recognition-sequence) | Match and event generation |
| Reporting sequence | [flows.md](flows.md#5-reporting-sequence) | Redis events to table |
| Biometric lifecycle | [flows.md](flows.md#6-biometric-data-lifecycle) | Consent through deletion |
| Deployment topology | [flows.md](flows.md#7-deployment-topology) | Reverse proxy and private Redis |
| Failure handling | [flows.md](flows.md#8-failure-boundaries) | Error states |

Check Mermaid rendering in GitHub before merging diagram edits. Keep node labels quoted when they contain punctuation, slashes, parentheses, or special characters.
