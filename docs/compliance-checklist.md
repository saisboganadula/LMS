# Compliance & Privacy Checklist — Phase 0 Baseline

## Governance
- [ ] Identify data owners for learner, instructor, and system records.
- [ ] Document data retention policy and review cadence.
- [ ] Confirm open-source license compatibility for all dependencies.

## Data Protection
- [ ] Classify ingested LMS content and learner interaction data.
- [ ] Define encryption standards for data at rest (Postgres, MinIO) and in transit (TLS).
- [ ] Specify access controls for service, database, and object storage credentials.
- [ ] Establish audit log schema, retention window, and access review process.

## Privacy & Consent
- [ ] Review LMS terms to confirm on-prem inference is permitted.
- [ ] Draft learner-facing disclosure about hint generation and data usage.
- [ ] Validate that hint prompts exclude solution keys and personally identifiable information.

## Security Operations
- [ ] Create incident response runbook for model leakage or data breach.
- [ ] Define vulnerability scanning schedule for containers and dependencies.
- [ ] Plan for secrets management (env vars, vault, or secrets manager).

## Accessibility & Compliance
- [ ] Align chat widget with WCAG 2.1 AA (keyboard navigation, ARIA labels, contrast).
- [ ] Provide alternative hint delivery channel for assistive technologies if needed.

## Documentation & Sign-off
- [ ] Record assumptions, open questions, and approvals from stakeholders.
- [ ] Schedule recurring compliance review prior to pilot launch.

