from pydantic import BaseModel

# import Schemas
from .resume import Resume
from .JD_matching import JDMatchingResult
from .internship_search import Internship


class ApplicationWriterInput(BaseModel):
    internship: Internship
    resume: Resume
    jd_match: JDMatchingResult
