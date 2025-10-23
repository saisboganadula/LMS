"""FastAPI application entry point for the Hints Tutor Bot service."""

from fastapi import FastAPI

from app import __version__
from app.schemas import HealthResponse, HintRequest, HintResponse

app = FastAPI(
    title="Hints Tutor Bot Service",
    version=__version__,
    description="Phase 0 skeleton for the self-hosted hints tutor API.",
)


@app.get("/internal/healthz", response_model=HealthResponse, tags=["internal"])
async def healthz() -> HealthResponse:
    """Simple health check endpoint for readiness probes."""
    return HealthResponse()


@app.post("/v1/hint", response_model=HintResponse, tags=["hinting"])
async def generate_hint(payload: HintRequest) -> HintResponse:
    """
    Return a placeholder hint response.

    Retrieval, policy enforcement, and llama.cpp integration will be wired in subsequent phases.
    """
    return HintResponse(
        tier="nudge",
        hint_text="Phase 0 placeholder: retrieval and generation pipeline not yet connected.",
        citations=[],
        cooldown_seconds=30,
    )


def get_app() -> FastAPI:
    """Expose the FastAPI application for ASGI servers."""
    return app

