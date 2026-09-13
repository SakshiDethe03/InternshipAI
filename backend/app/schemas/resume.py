from pydantic import BaseModel
from typing import List, Optional


class Resume(BaseModel):
    name: str
    email: str
    phone: str
    linkedin: str
    github: str
    role: str
    experience: Optional[str] = None
    skills: List[str]
    projects: List[str]
    summary: str
