# 🧪 QA and acceptance strategy

## Quality dimensions

| Dimension | What to verify |
|---|---|
| Functional | Registration, recognition, logging, reports |
| Reliability | Redis/model/camera failures and recovery |
| Data integrity | Vector dimension, serialization, timestamps, duplicate events |
| Security | Authentication, authorization, secrets, network exposure |
| Privacy | Consent, data minimization, deletion, retention |
| Model quality | False acceptance, false rejection, subgroup performance |
| Usability | Camera guidance, unknown state, correction and alternative path |
| Accessibility | Non-camera workflow and readable status communication |

## Test matrix

| ID | Scenario | Expected outcome |
|---|---|---|
| QA-01 | Empty Redis registration hash | Recognition returns Unknown without crashing |
| QA-02 | Valid 512-float vector | Vector decodes with expected dimension |
| QA-03 | Malformed byte length | Record rejected with sanitized diagnostic |
| QA-04 | No face in frame | No embedding is written |
| QA-05 | Multiple faces in a frame | Each face is handled consistently; events are not conflated |
| QA-06 | Similarity below threshold | Unknown result |
| QA-07 | Similarity above threshold | Candidate selection is deterministic |
| QA-08 | Redis unavailable | Clear error; no false success message |
| QA-09 | Registration with blank name | Validation error |
| QA-10 | Two sessions register concurrently | Samples remain isolated |
| QA-11 | Empty attendance list | Empty state rendered |
| QA-12 | Malformed event string | Invalid row is isolated, not whole report crash |
| QA-13 | Timestamp across midnight/timezone | Correct date grouping using explicit timezone rules |
| QA-14 | Repeated sightings | Dedupe/report behavior matches documented policy |
| QA-15 | Camera permission denied | Actionable browser guidance |
| QA-16 | Wrong credentials | No sensitive auth detail leaked |
| QA-17 | User without report permission | Data read is denied by server-side authorization |
| QA-18 | Deletion request | Data removed from primary storage and scheduled backup lifecycle |

## Model evaluation

A useful evaluation must use approved, consented, representative test data and a defined protocol. Track at least:
- False acceptance rate (FAR).
- False rejection rate (FRR).
- ROC/DET curve and threshold selection rationale.
- Performance by relevant demographic groups, with appropriate safeguards.
- Lighting, pose, camera, image quality, and device conditions.
- Presentation attack/spoof evaluation.
- Confidence intervals and sample size.

Do not optimize only for overall accuracy. Document uncertainty and limitations.

## Acceptance gate

A feature that changes identity matching, biometric collection, retention, report semantics, or access permissions requires:
1. Unit tests.
2. Integration tests against disposable Redis.
3. A privacy/security review.
4. Documentation and diagram updates.
5. Human review and explicit product approval.
