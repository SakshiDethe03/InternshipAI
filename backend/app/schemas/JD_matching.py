from pydantic import BaseModel
from typing import List


class JDMatchingResult(BaseModel):
    match_score: float
    matched_skills: List[str]
    missing_skills: List[str]
    strengths: List[str]
    summary: str
