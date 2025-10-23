# LMS

## Hints Tutor Bot Service — Phase 0 Scaffold

This repository bootstraps the self-hosted Hints Tutor Bot service outlined in the MVP PRD. It includes the FastAPI skeleton, container setup, and CI pipeline needed to begin Phase 1 development.

## Getting Started

### Prerequisites
- Python 3.11+
- Docker & Docker Compose

### Install dependencies
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```

### Run the API locally
```bash
uvicorn app.main:app --reload
```

### Run tests and lint
```bash
ruff check .
pytest
```

### Run with Docker Compose
```bash
docker compose up --build
```

The compose stack starts the API, Postgres, and MinIO services with development credentials.

## Repository Layout
- `app/`: FastAPI application package with placeholder endpoints.
- `docs/`: Requirements summary and compliance checklist (Phase 0 deliverables).
- `tests/`: Pytest suite covering health and hint endpoints.
- `Dockerfile`, `docker-compose.yml`: Container build and local orchestration.
- `.github/workflows/ci.yml`: Continuous integration workflow running lint, tests, and Docker build.
