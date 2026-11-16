# 🐛 Known issues register

The following are visible in the inspected source. Some runtime consequences require execution to confirm, so they are labeled accordingly.

| ID | Severity | Area | Observation | Recommended fix |
|---|---|---|---|---|
| KI-01 | High | Secrets | `config.yaml` commits a sample user identity and cookie key | Replace sample configuration; rotate key if reused |
| KI-02 | High | Redis config | Placeholder host/port/password are hard-coded in two modules | Add centralized environment/secret config |
| KI-03 | High | Registration data | Shared `face_embedding.txt` in current working directory | Use per-session isolated in-memory/temporary state |
| KI-04 | High | Privacy | No demonstrated consent, retention, or deletion workflow | Define governance before processing real people |
| KI-05 | Medium | Reporting | Calls `retrieve_data`; core defines `retrive_data` | Normalize function spelling and add test |
| KI-06 | Medium | Registration UI | Adjacent role strings in `selectbox` lack a comma | Correct option tuple and add UI test |
| KI-07 | Medium | Authentication | `auth.py` invokes login and renders at import time; Home also performs auth UI | Separate construction from page rendering |
| KI-08 | Medium | Concurrency | Global recognition buffer/timer shared in module/page scope | Scope processing state per session/stream |
| KI-09 | Medium | Event model | Delimiter-based `Name@Role@Timestamp` has no escaping/validation | Use structured versioned events |
| KI-10 | Medium | Report semantics | First/last sightings are treated as in/out times | Label as observations; add reviewed check-in/out workflow |
| KI-11 | Medium | Report status | Present/absent based on 60-second span | Define policy and make thresholds configurable and auditable |
| KI-12 | Low | Import script | Depends on `simulated_logs.txt`, not present in tracked tree | Add synthetic fixture or clear CLI validation |
| KI-13 | Low | Dependencies | Requirements are unpinned | Add tested constraints/lock approach |
| KI-14 | Low | Generated files | Python bytecode cache committed | Remove generated artifacts in a separate cleanup change and ignore future caches |

## Change-control notes

Do not mix a large source refactor with a documentation-only commit. Fix each issue with focused tests, migration notes, and rollback guidance. The files under `__pycache__/` are currently tracked; this documentation update does not remove them.
