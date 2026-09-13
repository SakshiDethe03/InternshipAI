from pydantic import BaseModel
from typing import List, Optional


class Internship(BaseModel):
    internship_id: str
    company: str
    role: str
    stipend: str
    experience: Optional[str] = None
    location: str
    duration: Optional[str] = None
    description: str
    requirements: List[str]
    posted_at: str
