from pydantic import BaseModel
from typing import List, Optional


class Internship(BaseModel):
    company: str
    role: str
    stipend: str
    experience: Optional[str] | None = None
    location: str
    duration: Optional[str] | None = None
    description: str
    requirements: List[str]
