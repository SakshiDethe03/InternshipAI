from pydantic import BaseModel


class MatchDecisionResult(BaseModel):
    should_continue: bool
    category: str
    reason: str
