from pydantic import BaseModel, Field
from typing import List, Optional


class EligibilityResult(BaseModel):
    is_eligible: bool
    feedback: Optional[str] = None
    unmet_requirements: List[str] = Field(default_factory=list)
