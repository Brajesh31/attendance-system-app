# 🧾 Documentation maintenance

## Source-of-truth hierarchy

1. Checked-in implementation files define current behavior.
2. Configuration and dependency manifests define declared settings/dependencies.
3. Tests define verified behavior when tests exist and pass.
4. Documentation explains behavior and known limitations.
5. Roadmap and diagrams marked proposed describe future work only.

## Required updates

| Code change | Documentation to review |
|---|---|
| Redis key/serialization change | `database.md`, `api.md`, `data-flow.md`, diagrams |
| Model/provider/threshold change | `system-design.md`, `qa.md`, `security-review.md` |
| Registration workflow change | `architecture.md`, `data-privacy.md`, `api.md` |
| Attendance semantics change | `system-design.md`, `qa.md`, product overview |
| Auth/config change | `configuration.md`, deployment, security |
| Retention/deletion change | `data-privacy.md`, operations, security |
| New pages or modules | README, project structure, architecture |

## Writing standards

- Distinguish present, partial, absent, and proposed features.
- Never call a test passing unless it was actually executed.
- Use synthetic examples only.
- Mermaid diagrams must be fenced with ```mermaid.
- Do not add images from real users or camera sessions.
- Do not include secrets, biometric data, personal attendance data, or private endpoints.
