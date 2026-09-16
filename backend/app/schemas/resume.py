from pydantic import BaseModel, Field
from typing import List, Optional


class Resume(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None
    role: str
    experience: Optional[str] = None
    skills: List[str] = Field(default_factory=list)
    projects: List[str] = Field(default_factory=list)
    summary: Optional[str] = None
