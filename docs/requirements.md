# Self-Hosted Hints Tutor Bot Service — Requirements (Phase 0)

## Product Vision
- Provide a privacy-safe hints tutor that operates entirely on-premises.
- Deliver context-aware guidance that helps learners progress without revealing answers.
- Lower instructor support burden through automated, policy-compliant hints.

## Core Functional Requirements
- **Context-Scoped Retrieval**: Maintain a FAISS index per activity; retrieval stays within that scope.
- **Tiered Hinting Logic**: Offer three hint levels (nudge, clue, method outline) based on learner history.
- **Progress Awareness**: Track attempts and latest score to determine eligible hint tier.
- **Safety Layer**: Combine regex and semantic leak detection, refusal templates, cooldowns, and audit logging.
- **Schema-Based API**: `/v1/hint` endpoint returns tiered hints with citations and cooldown metadata.
- **Admin Operations**: Trigger re-indexing, review usage metrics, and export audit logs.

## Non-Functional Requirements
- **Technology Constraints**: Use FastAPI, FAISS, llama.cpp, Postgres, MinIO, open-source monitoring.
- **Latency & Availability**: Achieve < 3 s average inference on CPU; maintain ≥ 99% uptime for internal pilot.
- **Privacy & Security**: No outbound network calls; encrypt data at rest and in transit; maintain auditability.
- **Accessibility**: LMS widget complies with WCAG 2.1 AA.

## User Roles
- **Learner**: Requests hints through LMS chat widget within a specific activity.
- **Instructor/Admin**: Manages indexing and reviews audit logs.
- **System Maintainer**: Deploys, monitors, and upgrades the service.

## Success Metrics
- ≥ 80% of pilot learners rate hints as helpful or very helpful.
- Zero verified solution leaks in audit logs.
- Average response time under 3 seconds during pilot.
- Model uptime ≥ 99% over the pilot month.

## Key Risks & Mitigations
- **Leakage of full answers**: Remove solutions from corpus, enforce detectors, and serve refusal templates.
- **Slow CPU inference**: Cache embeddings, tighten retrieval scope, plan GPU upgrade path.
- **Data privacy issues**: Keep all components on-prem, log access, encrypt storage.
- **Hint quality concerns**: Iterate on prompts using learner feedback loop.

## Phase 0 Deliverables
- Confirmed requirements (this document).
- Compliance checklist baseline.
- Repository bootstrapped with FastAPI skeleton, containerization, and CI pipeline.

