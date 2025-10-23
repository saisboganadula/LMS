import pytest
from httpx import AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_health_endpoint_returns_ok():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/internal/healthz")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_hint_endpoint_returns_placeholder_payload():
    payload = {
        "activity_id": "activity-123",
        "learner_id": "learner-456",
        "query": "I am stuck on step 2.",
        "attempt_count": 1,
        "last_score": 0.4,
    }

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post("/v1/hint", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert body["tier"] == "nudge"
    assert "placeholder" in body["hint_text"].lower()
    assert body["cooldown_seconds"] == 30

