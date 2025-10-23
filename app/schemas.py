"""Pydantic schemas for API request and response payloads."""

from typing import List, Literal, Optional

from pydantic import BaseModel, Field


HintTier = Literal["nudge", "clue", "method_outline"]


class HintRequest(BaseModel):
    """Inbound payload from the LMS requesting a hint."""

    activity_id: str = Field(..., description="Unique identifier for the LMS activity.")
    learner_id: str = Field(..., description="Unique identifier for the learner within the LMS.")
    query: str = Field(..., description="Latest learner question or context to refine hints.")
    attempt_count: int = Field(0, ge=0, description="Number of attempts made by the learner.")
    last_score: Optional[float] = Field(
        None,
        ge=0,
        le=1,
        description="Most recent normalized score between 0 and 1, if available.",
    )


class HintCitation(BaseModel):
    """Reference to a piece of source material used for hint generation."""

    source_id: str = Field(..., description="Identifier of the source document chunk.")
    text_snippet: str = Field(..., description="Excerpt shown to justify the hint.")


class HintResponse(BaseModel):
    """Structured response delivered to the LMS widget."""

    tier: HintTier = Field(..., description="Hint tier served to the learner.")
    hint_text: str = Field(..., description="Natural language hint content.")
    citations: List[HintCitation] = Field(default_factory=list, description="Supporting evidence.")
    cooldown_seconds: int = Field(
        0, ge=0, description="Cooldown period before the next hint request is allowed."
    )


class HealthResponse(BaseModel):
    """Simple health indicator exposed for monitoring."""

    status: Literal["ok"] = "ok"

